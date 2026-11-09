"""The Army: deploys agents, runs pipelines and commander-led missions."""

from __future__ import annotations

import json
import re
import threading
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import pipelines as pipeline_registry
from . import roster
from .agent import Agent, AgentReport, EventHook, ExtraTool
from .config import ArmyConfig
from .llm import ClaudeBackend, LLMBackend, Usage
from .pipelines import Pipeline, Stage
from .report import render_markdown

MAX_CONTEXT_CHARS = 60_000
MAX_DISPATCHES = 25


@dataclass
class StageResult:
    stage: str
    status: str = "pending"  # passed | blocked | failed | done
    reports: list[AgentReport] = field(default_factory=list)
    loops: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {"stage": self.stage, "status": self.status, "loops": self.loops,
                "reports": [r.to_dict() for r in self.reports]}


@dataclass
class RunResult:
    run_id: str
    pipeline: str
    goal: str
    status: str = "running"  # completed | blocked | failed
    stages: list[StageResult] = field(default_factory=list)
    started: str = ""
    finished: str = ""
    run_dir: Path | None = None

    @property
    def reports(self) -> list[AgentReport]:
        return [r for s in self.stages for r in s.reports]

    @property
    def usage(self) -> Usage:
        total = Usage()
        for r in self.reports:
            total.add(r.usage)
        return total

    @property
    def changed_files(self) -> list[str]:
        files: set[str] = set()
        for r in self.reports:
            files.update(r.changed_files)
        return sorted(files)

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id, "pipeline": self.pipeline, "goal": self.goal,
            "status": self.status, "started": self.started, "finished": self.finished,
            "usage": self.usage.as_dict(), "changed_files": self.changed_files,
            "stages": [s.to_dict() for s in self.stages],
        }


class Blackboard:
    """Shared memory: every report filed during a run, in order."""

    def __init__(self, goal: str) -> None:
        self.goal = goal
        self.reports: list[AgentReport] = []
        self._lock = threading.Lock()

    def add(self, report: AgentReport) -> None:
        with self._lock:
            self.reports.append(report)

    def context(self) -> str:
        with self._lock:
            latest: dict[str, AgentReport] = {}
            for r in self.reports:  # keep each agent's most recent report
                latest.pop(r.agent, None)
                latest[r.agent] = r
            ordered = list(latest.values())
        header = f"# Mission goal\n{self.goal.strip()}\n"
        if not ordered:
            return header
        sections = [r.as_context() for r in ordered]
        # If too long, shrink the oldest reports to their summaries first.
        i = 0
        while sum(map(len, sections)) > MAX_CONTEXT_CHARS and i < len(sections) - 1:
            sections[i] = ordered[i].as_context(max_chars=1500)
            i += 1
        body = "\n\n".join(sections)
        if len(body) > MAX_CONTEXT_CHARS:
            body = body[-MAX_CONTEXT_CHARS:]
        return f"{header}\n# Reports from earlier specialists\n\n{body}"


class Army:
    def __init__(
        self,
        config: ArmyConfig,
        backend: LLMBackend | None = None,
        on_event: EventHook | None = None,
    ) -> None:
        self.config = config
        self.backend = backend or ClaudeBackend(use_fallbacks=config.use_fallbacks)
        self.on_event = on_event

    # ---------------------------------------------------------- one agent
    def deploy(
        self,
        agent_name: str,
        task: str,
        context: str = "",
        config: ArmyConfig | None = None,
        extra_tools: dict[str, ExtraTool] | None = None,
    ) -> AgentReport:
        spec = roster.get(agent_name)
        agent = Agent(spec, config or self.config, self.backend, self.on_event, extra_tools)
        return agent.run(task, context)

    # ----------------------------------------------------------- pipeline
    def run_pipeline(self, pipeline: Pipeline | str, goal: str) -> RunResult:
        if isinstance(pipeline, str):
            pipeline = pipeline_registry.get(pipeline)
        cfg = replace(self.config, allow_write=False) if pipeline.read_only else self.config
        run = self._new_run(pipeline.name, goal)
        board = Blackboard(goal)

        for stage in pipeline.stages:
            self._emit("army", "stage", f"{stage.name}: {', '.join(stage.agents)}")
            result = self._run_stage(stage, goal, board, cfg)
            run.stages.append(result)
            self._save(run)
            if result.status in {"blocked", "failed"}:
                run.status = result.status
                break
        else:
            run.status = "completed"
        return self._finish(run)

    def _run_stage(self, stage: Stage, goal: str, board: Blackboard, cfg: ArmyConfig) -> StageResult:
        result = StageResult(stage.name)
        task = stage.task.format(goal=goal)
        reports = self._squad(stage.agents, task, board, cfg)
        result.reports.extend(reports)

        if any(r.error for r in reports):
            result.status = "failed"
            return result
        if not stage.gate:
            result.status = "done"
            return result

        while any(r.blocking for r in reports):
            blockers = [r for r in reports if r.blocking]
            if not stage.fixer or result.loops >= self.config.max_review_loops:
                result.status = "blocked"
                return result
            result.loops += 1
            self._emit("army", "gate", f"{stage.name} blocked by {', '.join(r.agent for r in blockers)}; "
                                       f"fix round {result.loops}")
            fix_task = (
                f"The '{stage.name}' gate is blocked. Address every blocking finding below, then report what "
                f"you changed for each one.\n\n" + "\n\n".join(r.as_context() for r in blockers)
                + f"\n\nOriginal goal:\n{goal}"
            )
            fix = self.deploy(stage.fixer, fix_task, board.context(), cfg)
            board.add(fix)
            result.reports.append(fix)
            if fix.error:
                result.status = "failed"
                return result
            recheck = (f"Re-check after fixes (round {result.loops}). Confirm whether your earlier findings are "
                       f"resolved and look for regressions.\n\n{task}")
            reports = self._squad([r.agent for r in blockers], recheck, board, cfg)
            result.reports.extend(reports)
            if any(r.error for r in reports):
                result.status = "failed"
                return result

        result.status = "passed"
        return result

    def _squad(self, agents: list[str], task: str, board: Blackboard, cfg: ArmyConfig) -> list[AgentReport]:
        context = board.context()
        if len(agents) == 1:
            reports = [self.deploy(agents[0], task, context, cfg)]
        else:
            with ThreadPoolExecutor(max_workers=max(1, self.config.max_parallel)) as pool:
                futures = [pool.submit(self.deploy, a, task, context, cfg) for a in agents]
                reports = [f.result() for f in futures]
        for r in reports:
            board.add(r)
        return reports

    # ------------------------------------------------------------ mission
    def mission(self, goal: str) -> RunResult:
        """Commander-led: the commander decides who to deploy and when."""
        run = self._new_run("mission", goal)
        board = Blackboard(goal)
        stage = StageResult("mission")
        run.stages.append(stage)
        dispatches = {"n": 0}

        def dispatch(args: dict[str, Any]) -> str:
            name = str(args.get("agent", ""))
            task = str(args.get("task", "")).strip()
            if name not in roster.ROSTER:
                return f"Error: unknown agent '{name}'. Choose from: {', '.join(roster.ROSTER)}"
            if not task:
                return "Error: task must not be empty."
            if dispatches["n"] >= MAX_DISPATCHES:
                return "Error: dispatch limit reached. Submit your final report now."
            dispatches["n"] += 1
            report = self.deploy(name, task, board.context())
            board.add(report)
            stage.reports.append(report)
            self._save(run)
            return report.as_context()

        dispatch_tool = ExtraTool(
            definition={
                "name": "dispatch_agent",
                "description": (
                    "Deploy one specialist on an assignment and wait for their report. The specialist "
                    "automatically receives the mission goal and the latest report from every specialist "
                    "deployed so far. Give precise, self-contained instructions."
                ),
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "agent": {"type": "string", "enum": sorted(roster.ROSTER)},
                        "task": {"type": "string", "description": "The assignment, written as a brief."},
                    },
                    "required": ["agent", "task"],
                    "additionalProperties": False,
                },
            },
            handler=dispatch,
        )
        roster_text = "\n".join(f"- {s.describe()}" for s in roster.ROSTER.values())
        commander = replace(roster.COMMANDER, mission=roster.COMMANDER.mission
                            + f"\n\nAvailable specialists (dispatch with `dispatch_agent`):\n{roster_text}")
        agent = Agent(commander, self.config, self.backend, self.on_event, {"dispatch_agent": dispatch_tool})
        final = agent.run(f"Accomplish this mission:\n\n{goal}")
        stage.reports.append(final)

        if final.error:
            stage.status, run.status = "failed", "failed"
        elif final.blocking:
            stage.status, run.status = "blocked", "blocked"
        else:
            stage.status, run.status = "done", "completed"
        return self._finish(run)

    # ------------------------------------------------------- bookkeeping
    def _new_run(self, name: str, goal: str) -> RunResult:
        now = datetime.now(timezone.utc)
        slug = re.sub(r"[^a-z0-9]+", "-", goal.lower()).strip("-")[:40] or "run"
        run_id = f"{now:%Y%m%d-%H%M%S}-{name}-{slug}"
        run = RunResult(run_id, name, goal, started=now.isoformat(timespec="seconds"))
        run.run_dir = self.config.runs_path / run_id
        self._emit("army", "run", f"{run_id}")
        return run

    def _finish(self, run: RunResult) -> RunResult:
        run.finished = datetime.now(timezone.utc).isoformat(timespec="seconds")
        self._save(run)
        self._emit("army", "finish", f"{run.status} -> {run.run_dir}")
        return run

    def _save(self, run: RunResult) -> None:
        if run.run_dir is None:
            return
        try:
            run.run_dir.mkdir(parents=True, exist_ok=True)
            (run.run_dir / "run.json").write_text(json.dumps(run.to_dict(), indent=2))
            (run.run_dir / "report.md").write_text(render_markdown(run))
        except OSError as exc:
            self._emit("army", "error", f"could not save run: {exc}")

    def _emit(self, who: str, kind: str, detail: str) -> None:
        if self.on_event:
            self.on_event(who, kind, detail)


def latest_run(config: ArmyConfig) -> Path | None:
    base = config.runs_path
    if not base.is_dir():
        return None
    runs = sorted(p for p in base.iterdir() if p.is_dir())
    return runs[-1] if runs else None
