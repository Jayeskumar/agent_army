"""Model backends.

``ClaudeBackend`` talks to the Claude API through the official Anthropic SDK.
``DryRunBackend`` and ``ScriptedBackend`` never touch the network: the first
lets you rehearse a pipeline end to end for free, the second drives tests.
"""

from __future__ import annotations

import itertools
import threading
from dataclasses import dataclass, field
from typing import Any, Callable, Protocol

# Models that accept the server-side refusal fallback parameter.
FALLBACK_MODELS = {
    "claude-fable-5-2",
    "claude-fable-5-1",
    "claude-opus-5-5",
    "claude-opus-5",
    "claude-sonnet-5-5",
}
FALLBACK_BETA = "server-side-fallback-2026-07-01"


class LLMError(RuntimeError):
    """The model call failed in a way the agent cannot recover from."""


@dataclass
class Usage:
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    cache_write_tokens: int = 0

    def add(self, other: "Usage") -> None:
        self.input_tokens += other.input_tokens
        self.output_tokens += other.output_tokens
        self.cache_read_tokens += other.cache_read_tokens
        self.cache_write_tokens += other.cache_write_tokens

    def as_dict(self) -> dict[str, int]:
        return {
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "cache_read_tokens": self.cache_read_tokens,
            "cache_write_tokens": self.cache_write_tokens,
        }


@dataclass
class LLMResponse:
    # Normalised view used by the agent loop:
    #   {"type": "text", "text": ...}
    #   {"type": "tool_use", "id": ..., "name": ..., "input": {...}}
    blocks: list[dict[str, Any]]
    # Exactly what must be appended as the assistant turn. For Claude this is
    # the SDK's own content list, so thinking blocks travel back unchanged.
    assistant_content: Any
    stop_reason: str
    usage: Usage = field(default_factory=Usage)
    model: str = ""


class LLMBackend(Protocol):
    def complete(
        self,
        *,
        agent_name: str,
        model: str,
        system: str,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]],
        max_tokens: int,
        effort: str,
    ) -> LLMResponse: ...


# --------------------------------------------------------------------- Claude
class ClaudeBackend:
    def __init__(self, use_fallbacks: bool = True, client: Any = None) -> None:
        if client is None:
            import anthropic

            client = anthropic.Anthropic(max_retries=4)
        self.client = client
        self.use_fallbacks = use_fallbacks

    def complete(self, *, agent_name, model, system, messages, tools, max_tokens, effort) -> LLMResponse:
        import anthropic

        params: dict[str, Any] = dict(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=messages,
            tools=tools,
            thinking={"type": "adaptive"},
            output_config={"effort": effort},
            # Automatic prompt caching: the stable prefix (tools + system +
            # earlier turns) is re-read from cache on every loop iteration.
            cache_control={"type": "ephemeral"},
        )
        try:
            if self.use_fallbacks and model in FALLBACK_MODELS:
                resp = self.client.beta.messages.create(
                    betas=[FALLBACK_BETA], fallbacks="default", **params
                )
            else:
                resp = self.client.messages.create(**params)
        except anthropic.BadRequestError as exc:
            raise LLMError(f"[{agent_name}] bad request: {exc.message}") from exc
        except anthropic.AuthenticationError as exc:
            raise LLMError("Authentication failed - set ANTHROPIC_API_KEY or run `ant auth login`.") from exc
        except anthropic.RateLimitError as exc:
            raise LLMError(f"[{agent_name}] rate limited after retries: {exc.message}") from exc
        except anthropic.APIStatusError as exc:
            raise LLMError(f"[{agent_name}] API error {exc.status_code}: {exc.message}") from exc
        except anthropic.APIConnectionError as exc:
            raise LLMError(f"[{agent_name}] network error: {exc}") from exc

        blocks: list[dict[str, Any]] = []
        for b in resp.content:
            if b.type == "text":
                blocks.append({"type": "text", "text": b.text})
            elif b.type == "tool_use":
                blocks.append({"type": "tool_use", "id": b.id, "name": b.name, "input": b.input})
        u = resp.usage
        usage = Usage(
            input_tokens=u.input_tokens or 0,
            output_tokens=u.output_tokens or 0,
            cache_read_tokens=getattr(u, "cache_read_input_tokens", 0) or 0,
            cache_write_tokens=getattr(u, "cache_creation_input_tokens", 0) or 0,
        )
        return LLMResponse(blocks, resp.content, resp.stop_reason or "", usage, resp.model)


# -------------------------------------------------------------------- offline
class DryRunBackend:
    """Rehearsal mode: every agent looks around once, then reports success.

    Useful for checking how a pipeline is wired (stages, gates, parallelism,
    run reports) without spending tokens.
    """

    def __init__(self) -> None:
        self._ids = itertools.count(1)
        self._lock = threading.Lock()

    def _id(self) -> str:
        with self._lock:
            return f"toolu_dry_{next(self._ids)}"

    def complete(self, *, agent_name, model, system, messages, tools, max_tokens, effort) -> LLMResponse:
        tool_names = {t["name"] for t in tools}
        turns = sum(1 for m in messages if m["role"] == "assistant")
        if turns == 0 and "list_files" in tool_names:
            blocks = [
                {"type": "text", "text": "Surveying the workspace."},
                {"type": "tool_use", "id": self._id(), "name": "list_files", "input": {"max_results": 25}},
            ]
            return LLMResponse(blocks, blocks, "tool_use", Usage(), "dry-run")

        task = _first_user_text(messages)
        headline = task.strip().splitlines()[0][:160] if task.strip() else "(no task)"
        blocks = [{
            "type": "tool_use",
            "id": self._id(),
            "name": "submit_report",
            "input": {
                "summary": f"**[dry-run] {agent_name}** would handle: {headline}",
                "verdict": "pass",
                "findings": [],
                "artifacts": [{"name": f"{agent_name}_notes", "content": f"Dry-run output of {agent_name}."}],
            },
        }]
        return LLMResponse(blocks, blocks, "tool_use", Usage(), "dry-run")


Step = list[dict[str, Any]] | Callable[[list[dict[str, Any]]], list[dict[str, Any]]]


class ScriptedBackend:
    """Replays canned responses per agent - for tests.

    ``script`` maps an agent name to a list of steps; each step is a list of
    normalised blocks (or a callable receiving the messages and returning
    blocks). Tool-use ids are filled in automatically when missing.
    """

    def __init__(self, script: dict[str, list[Step]]) -> None:
        self.script = {k: list(v) for k, v in script.items()}
        self.calls: list[tuple[str, list[dict[str, Any]]]] = []
        self._ids = itertools.count(1)
        self._lock = threading.Lock()

    def complete(self, *, agent_name, model, system, messages, tools, max_tokens, effort) -> LLMResponse:
        with self._lock:
            self.calls.append((agent_name, [dict(m) for m in messages]))
            queue = self.script.get(agent_name)
            if not queue:
                raise LLMError(f"ScriptedBackend has no more steps for agent '{agent_name}'")
            step = queue.pop(0)
        blocks = step(messages) if callable(step) else step
        blocks = [dict(b) for b in blocks]
        for b in blocks:
            if b["type"] == "tool_use" and "id" not in b:
                b["id"] = f"toolu_s_{next(self._ids)}"
        stop = "tool_use" if any(b["type"] == "tool_use" for b in blocks) else "end_turn"
        return LLMResponse(blocks, blocks, stop, Usage(10, 5), "scripted")


def _first_user_text(messages: list[dict[str, Any]]) -> str:
    for m in messages:
        if m["role"] == "user":
            c = m["content"]
            if isinstance(c, str):
                return c
            for part in c:
                if isinstance(part, dict) and part.get("type") == "text":
                    return part["text"]
    return ""
