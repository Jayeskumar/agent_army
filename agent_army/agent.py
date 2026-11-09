"""A single soldier: one specialist running its own tool-use loop."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Callable

from .config import ArmyConfig
from .llm import LLMBackend, LLMError, Usage
from .tools import SUBMIT_TOOL, Toolbox, ToolError

VERDICTS = {"pass", "fail", "needs_changes", "info"}
BLOCKING_VERDICTS = {"fail", "needs_changes"}
MAX_NUDGES = 2
STANDING_ORDER_FILES = ("ARMY.md", "AGENTS.md", "CLAUDE.md")
MAX_STANDING_ORDERS = 20_000

EventHook = Callable[[str, str, str], None]  # (agent, kind, detail)

DOCTRINE = """\
You are {title}, a specialist in Agent Army: a team of AI agents that together \
automate the software development lifecycle, from idea to release and operations. \
Other specialists work before and after you; their reports are given to you as context.

## Your speciality
{mission}

## How you work
- You are operating on a real repository through the tools listed below. Ground every \
claim in files you have actually read or commands you have actually run.
- Follow the conventions already present in the codebase (layout, style, test framework).
- Keep changes focused on your assignment. Do not reformat or rewrite unrelated code.
- Never invent results. If you could not run something (for example, you have no \
command tool), say so plainly in your report.
- Be efficient: explore with list_files/search_code before reading whole files, and \
batch independent tool calls in one turn.
- Your tools: {tools}.

## Finishing
End your assignment by calling `submit_report` exactly once:
- `summary`: concise Markdown for the next specialist and for humans.
- `verdict`: `pass` (your check passed / work complete), `needs_changes` (others must \
fix something before this can ship), `fail` (blocked or broken), `info` (purely \
informational deliverable).
- `findings`: concrete, actionable items with severity and file:line location when relevant.
- `artifacts`: named deliverables later specialists need (e.g. requirements, design, plan).
"""


@dataclass
class AgentSpec:
    name: str
    title: str
    division: str
    mission: str
    tiers: frozenset[str] = frozenset({"read"})
    light: bool = False  # may run on the cheaper light_model
    max_turns: int | None = None

    @property
    def tagline(self) -> str:
        """First sentence of the mission."""
        flat = " ".join(self.mission.split())
        return flat.split(". ")[0].rstrip(".") + "."

    def describe(self) -> str:
        return f"{self.name} ({self.title}, {self.division}): {self.tagline}"


@dataclass
class AgentReport:
    agent: str
    summary: str
    verdict: str
    findings: list[dict[str, Any]] = field(default_factory=list)
    artifacts: dict[str, str] = field(default_factory=dict)
    changed_files: list[str] = field(default_factory=list)
    turns: int = 0
    usage: Usage = field(default_factory=Usage)
    error: str | None = None

    @property
    def blocking(self) -> bool:
        return self.verdict in BLOCKING_VERDICTS

    def to_dict(self) -> dict[str, Any]:
        return {
            "agent": self.agent,
            "summary": self.summary,
            "verdict": self.verdict,
            "findings": self.findings,
            "artifacts": self.artifacts,
            "changed_files": self.changed_files,
            "turns": self.turns,
            "usage": self.usage.as_dict(),
            "error": self.error,
        }

    def as_context(self, max_chars: int = 12_000) -> str:
        parts = [f"### Report from {self.agent} - verdict: {self.verdict}", self.summary.strip()]
        if self.findings:
            parts.append("Findings:")
            for f in self.findings:
                loc = f" ({f['location']})" if f.get("location") else ""
                parts.append(f"- [{f.get('severity', 'note')}] {f.get('title', '')}{loc}: {f.get('detail', '')}")
        if self.changed_files:
            parts.append("Files changed: " + ", ".join(sorted(self.changed_files)))
        for name, content in self.artifacts.items():
            parts.append(f"#### Artifact `{name}`\n{content.strip()}")
        text = "\n".join(parts)
        if len(text) > max_chars:
            text = text[:max_chars] + "\n... [report truncated]"
        return text


@dataclass
class ExtraTool:
    """A tool owned by the orchestration layer (e.g. the commander's dispatch)."""

    definition: dict[str, Any]
    handler: Callable[[dict[str, Any]], str]


class Agent:
    def __init__(
        self,
        spec: AgentSpec,
        config: ArmyConfig,
        backend: LLMBackend,
        on_event: EventHook | None = None,
        extra_tools: dict[str, ExtraTool] | None = None,
    ) -> None:
        self.spec = spec
        self.config = config
        self.backend = backend
        self.on_event = on_event or (lambda *_: None)
        self.extra_tools = extra_tools or {}
        self.toolbox = Toolbox(config, set(spec.tiers))

    # -------------------------------------------------------------- prompts
    def system_prompt(self) -> str:
        tool_names = sorted(self.toolbox.names + list(self.extra_tools))
        prompt = DOCTRINE.format(title=self.spec.title, mission=self.spec.mission.strip(), tools=", ".join(tool_names))
        if "write" not in self.toolbox.tiers and "write" in self.spec.tiers:
            prompt += "\nNote: file writes are disabled for this run. Describe the changes instead of making them.\n"
        if "exec" not in self.toolbox.tiers and "exec" in self.spec.tiers:
            prompt += ("\nNote: command execution is disabled for this run. You cannot run tests; "
                       "state that in your report rather than claiming results.\n")
        orders = load_standing_orders(self.config)
        if orders:
            prompt += f"\n## Project standing orders\n{orders}\n"
        return prompt

    def tool_definitions(self) -> list[dict[str, Any]]:
        defs = self.toolbox.api_definitions()
        defs += [self.extra_tools[n].definition for n in sorted(self.extra_tools)]
        return defs

    # ----------------------------------------------------------------- loop
    def run(self, task: str, context: str = "") -> AgentReport:
        name = self.spec.name
        max_turns = self.spec.max_turns or self.config.max_turns
        model = self.config.model_for(self.spec.light)
        system = self.system_prompt()
        tools = self.tool_definitions()
        usage = Usage()

        opening = f"{context.strip()}\n\n" if context.strip() else ""
        opening += f"# Your assignment\n{task.strip()}"
        messages: list[dict[str, Any]] = [{"role": "user", "content": opening}]
        self.on_event(name, "start", task.strip().splitlines()[0][:120] if task.strip() else "")

        nudges = 0
        last_text = ""
        for turn in range(1, max_turns + 1):
            try:
                resp = self.backend.complete(
                    agent_name=name, model=model, system=system, messages=messages,
                    tools=tools, max_tokens=self.config.max_tokens, effort=self.config.effort,
                )
            except LLMError as exc:
                self.on_event(name, "error", str(exc))
                return self._report("Model call failed.", "fail", usage=usage, turns=turn, error=str(exc))
            usage.add(resp.usage)

            if resp.stop_reason == "max_tokens":
                # Drop the truncated turn (it may hold a half-written tool call)
                # and ask for smaller steps.
                messages.append({"role": "user", "content": (
                    "Your previous response hit the output limit and was discarded. "
                    "Work in smaller steps: split large files into several write/edit calls.")})
                messages = _merge_trailing_user(messages)
                continue

            messages.append({"role": "assistant", "content": resp.assistant_content})
            texts = [b["text"] for b in resp.blocks if b["type"] == "text" and b["text"].strip()]
            if texts:
                last_text = texts[-1]
                self.on_event(name, "think", last_text[:200])

            if resp.stop_reason == "refusal":
                return self._report("The model declined this assignment.", "fail", usage=usage,
                                    turns=turn, error="refusal")
            if resp.stop_reason == "pause_turn":
                continue

            calls = [b for b in resp.blocks if b["type"] == "tool_use"]
            if not calls:
                if nudges >= MAX_NUDGES:
                    return self._report(last_text or "(no report submitted)", "info", usage=usage, turns=turn)
                nudges += 1
                messages.append({"role": "user", "content":
                                 "Please finish by calling the submit_report tool with your final report."})
                continue

            results: list[dict[str, Any]] = []
            submitted: dict[str, Any] | None = None
            for call in calls:
                if call["name"] == SUBMIT_TOOL:
                    submitted = call["input"] if isinstance(call["input"], dict) else {}
                    results.append(_tool_result(call["id"], "Report received. Assignment complete."))
                    continue
                results.append(self._execute(call))

            if submitted is not None:
                messages.append({"role": "user", "content": results})
                return self._from_submission(submitted, usage, turn)

            if turn == max_turns - 2:
                results.append({"type": "text", "text":
                                "You are close to your turn limit. Wrap up now and call submit_report."})
            messages.append({"role": "user", "content": results})

        return self._report(last_text or "Turn limit reached before a report was submitted.", "fail",
                            usage=usage, turns=max_turns, error="turn limit reached")

    # -------------------------------------------------------------- helpers
    def _execute(self, call: dict[str, Any]) -> dict[str, Any]:
        name, args = call["name"], call.get("input") or {}
        self.on_event(self.spec.name, "tool", f"{name} {_preview(args)}")
        try:
            if name in self.extra_tools:
                output = self.extra_tools[name].handler(args)
            else:
                output = self.toolbox.execute(name, args)
            return _tool_result(call["id"], output)
        except ToolError as exc:
            return _tool_result(call["id"], f"Error: {exc}", is_error=True)
        except Exception as exc:  # keep the agent alive on unexpected tool crashes
            return _tool_result(call["id"], f"Error: unexpected {type(exc).__name__}: {exc}", is_error=True)

    def _from_submission(self, data: dict[str, Any], usage: Usage, turns: int) -> AgentReport:
        verdict = str(data.get("verdict", "info")).lower()
        if verdict not in VERDICTS:
            verdict = "info"
        findings = [f for f in data.get("findings") or [] if isinstance(f, dict)]
        artifacts: dict[str, str] = {}
        for a in data.get("artifacts") or []:
            if isinstance(a, dict) and a.get("name"):
                artifacts[str(a["name"])] = str(a.get("content", ""))
        report = self._report(str(data.get("summary", "")), verdict, findings, artifacts, usage, turns)
        self.on_event(self.spec.name, "done", f"verdict={verdict}, findings={len(findings)}")
        return report

    def _report(self, summary, verdict, findings=None, artifacts=None, usage=None, turns=0, error=None):
        return AgentReport(
            agent=self.spec.name, summary=summary, verdict=verdict,
            findings=findings or [], artifacts=artifacts or {},
            changed_files=sorted(self.toolbox.changed_files), turns=turns,
            usage=usage or Usage(), error=error,
        )


def load_standing_orders(config: ArmyConfig) -> str:
    for fname in STANDING_ORDER_FILES:
        p = config.workspace / fname
        if p.is_file():
            text = p.read_text(errors="replace")
            return text[:MAX_STANDING_ORDERS]
    return ""


def _tool_result(tool_use_id: str, content: str, is_error: bool = False) -> dict[str, Any]:
    block: dict[str, Any] = {"type": "tool_result", "tool_use_id": tool_use_id, "content": content or "(empty)"}
    if is_error:
        block["is_error"] = True
    return block


def _preview(args: dict[str, Any]) -> str:
    try:
        text = json.dumps(args, ensure_ascii=False)
    except (TypeError, ValueError):
        text = str(args)
    return text if len(text) <= 120 else text[:117] + "..."


def _merge_trailing_user(messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Collapse consecutive trailing user turns into one."""
    if len(messages) >= 2 and messages[-1]["role"] == messages[-2]["role"] == "user":
        prev, last = messages[-2], messages[-1]
        content = _as_blocks(prev["content"]) + _as_blocks(last["content"])
        return messages[:-2] + [{"role": "user", "content": content}]
    return messages


def _as_blocks(content: Any) -> list[dict[str, Any]]:
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    return list(content)
