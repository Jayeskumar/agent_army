"""Command-line interface: ``army <command>``."""

from __future__ import annotations

import argparse
import json
import sys
import threading
from pathlib import Path

from . import __version__
from . import pipelines as pipeline_registry
from . import roster
from .config import ArmyConfig
from .engine import Army, RunResult, latest_run
from .llm import DryRunBackend

EXIT = {"completed": 0, "failed": 1, "blocked": 2}

ARMY_YAML_TEMPLATE = """\
# Agent Army configuration. Every key is optional.
model: claude-opus-5-5
# light_model: claude-sonnet-5-5   # cheaper model for triage/docs/release agents
effort: high                       # low | medium | high | xhigh | max
max_turns: 40
max_review_loops: 3
max_parallel: 4
allow_write: true
allow_exec: false                  # let agents run tests/linters (allow-listed commands only)
command_timeout: 300
# extra_allowed_commands:
#   - "poetry run pytest"
#   - "pnpm test"
"""

ARMY_MD_TEMPLATE = """\
# Standing orders for Agent Army

Every agent reads this file before starting work. Use it to tell the army how
this project works.

## Project
- What this project is:
- Main language / framework:

## Commands
- Run tests:
- Lint / type-check:

## Conventions
- Code style:
- Where tests live:
- Things agents must never touch:
"""


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "cmd", None):
        parser.print_help()
        return 0
    try:
        return args.func(args)
    except (KeyError, ValueError) as exc:
        print(f"army: {exc.args[0] if exc.args else exc}", file=sys.stderr)
        return 64


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="army", description="Agent Army - AI specialists for the whole SDLC.")
    p.add_argument("--version", action="version", version=f"agent-army {__version__}")
    sub = p.add_subparsers(dest="cmd")

    s = sub.add_parser("roster", help="List every agent in the army")
    s.add_argument("--division", help="Only show one division")
    s.set_defaults(func=cmd_roster)

    s = sub.add_parser("pipelines", help="List the built-in pipelines")
    s.set_defaults(func=cmd_pipelines)

    s = sub.add_parser("run", help="Run a pipeline")
    s.add_argument("pipeline", choices=sorted(pipeline_registry.PIPELINES))
    s.add_argument("goal", nargs="?", default="", help="Goal text, '-' for stdin or @file")
    _common(s)
    s.set_defaults(func=cmd_run)

    s = sub.add_parser("deploy", help="Deploy a single agent on a task")
    s.add_argument("agent", choices=sorted(roster.ROSTER))
    s.add_argument("task", help="Task text, '-' for stdin or @file")
    _common(s)
    s.set_defaults(func=cmd_deploy)

    s = sub.add_parser("mission", help="Let the commander plan and dispatch agents dynamically")
    s.add_argument("goal", help="Mission text, '-' for stdin or @file")
    _common(s)
    s.set_defaults(func=cmd_mission)

    s = sub.add_parser("init", help="Write army.yaml and ARMY.md templates into the workspace")
    s.add_argument("-C", "--workspace", default=".")
    s.add_argument("--force", action="store_true")
    s.set_defaults(func=cmd_init)

    s = sub.add_parser("report", help="Print the report of the latest (or a named) run")
    s.add_argument("run_id", nargs="?")
    s.add_argument("-C", "--workspace", default=".")
    s.set_defaults(func=cmd_report)
    return p


def _common(s: argparse.ArgumentParser) -> None:
    s.add_argument("-C", "--workspace", default=".", help="Repository to operate on (default: .)")
    s.add_argument("--model")
    s.add_argument("--light-model")
    s.add_argument("--effort", choices=["low", "medium", "high", "xhigh", "max"])
    s.add_argument("--max-turns", type=int)
    s.add_argument("--allow-exec", action="store_true", default=None,
                   help="Allow agents to run allow-listed commands (tests, linters, builds)")
    s.add_argument("--read-only", action="store_true", help="Forbid all file writes")
    s.add_argument("--dry-run", action="store_true", help="Rehearse without calling the model")
    s.add_argument("--no-fallbacks", action="store_true", help="Disable server-side refusal fallbacks")
    s.add_argument("-q", "--quiet", action="store_true")
    s.add_argument("--json", action="store_true", help="Print the run result as JSON")


# ----------------------------------------------------------------- commands
def cmd_roster(args) -> int:
    for division, specs in roster.divisions().items():
        if args.division and division != args.division:
            continue
        print(f"\n== {division.upper()} ==")
        for spec in specs:
            tiers = "/".join(sorted(spec.tiers))
            print(f"  {spec.name:<22} {tiers:<16} {spec.tagline}")
    print(f"\n== COMMAND ==\n  {roster.COMMANDER.name:<22} {'read/dispatch':<16} {roster.COMMANDER.tagline}")
    return 0


def cmd_pipelines(args) -> int:
    for p in pipeline_registry.PIPELINES.values():
        ro = " (read-only)" if p.read_only else ""
        print(f"\n{p.name}{ro}: {p.description}")
        for st in p.stages:
            mode = " ‖ ".join(st.agents)
            gate = f"  [gate{', fixer: ' + st.fixer if st.fixer else ''}]" if st.gate else ""
            print(f"   - {st.name:<12} {mode}{gate}")
    return 0


def cmd_run(args) -> int:
    army = _army(args)
    goal = _read_text(args.goal) if args.goal else "(no additional notes)"
    return _finish(args, army.run_pipeline(args.pipeline, goal))


def cmd_mission(args) -> int:
    army = _army(args)
    return _finish(args, army.mission(_read_text(args.goal)))


def cmd_deploy(args) -> int:
    army = _army(args)
    report = army.deploy(args.agent, _read_text(args.task))
    if args.json:
        print(json.dumps(report.to_dict(), indent=2))
    else:
        print(report.as_context(max_chars=1_000_000))
    if report.error:
        return 1
    return 2 if report.blocking else 0


def cmd_init(args) -> int:
    ws = Path(args.workspace)
    for name, body in (("army.yaml", ARMY_YAML_TEMPLATE), ("ARMY.md", ARMY_MD_TEMPLATE)):
        target = ws / name
        if target.exists() and not args.force:
            print(f"skip   {target} (exists; use --force to overwrite)")
            continue
        target.write_text(body)
        print(f"wrote  {target}")
    return 0


def cmd_report(args) -> int:
    cfg = ArmyConfig.load(args.workspace)
    run_dir = cfg.runs_path / args.run_id if args.run_id else latest_run(cfg)
    if not run_dir or not (run_dir / "report.md").exists():
        print("No runs found.", file=sys.stderr)
        return 1
    print((run_dir / "report.md").read_text())
    return 0


# ------------------------------------------------------------------ helpers
def _army(args) -> Army:
    overrides = dict(
        model=args.model, light_model=args.light_model, effort=args.effort,
        max_turns=args.max_turns, allow_exec=args.allow_exec,
    )
    if args.read_only:
        overrides["allow_write"] = False
    if args.no_fallbacks:
        overrides["use_fallbacks"] = False
    cfg = ArmyConfig.load(args.workspace, **overrides)
    backend = DryRunBackend() if args.dry_run else None
    hook = None if args.quiet else _printer()
    return Army(cfg, backend=backend, on_event=hook)


def _printer():
    lock = threading.Lock()
    icons = {"start": "▶", "tool": "  ⚙", "think": "  …", "done": "✔", "error": "✖",
             "stage": "\n■", "gate": "⛔", "run": "★", "finish": "★"}

    def hook(agent: str, kind: str, detail: str) -> None:
        if kind == "think":
            detail = detail.replace("\n", " ")[:140]
        with lock:
            print(f"{icons.get(kind, '-')} [{agent}] {detail}", file=sys.stderr, flush=True)

    return hook


def _read_text(value: str) -> str:
    if value == "-":
        return sys.stdin.read()
    if value.startswith("@"):
        return Path(value[1:]).read_text()
    return value


def _finish(args, run: RunResult) -> int:
    if args.json:
        print(json.dumps(run.to_dict(), indent=2))
    else:
        print(f"\nStatus: {run.status}")
        print(f"Report: {run.run_dir / 'report.md' if run.run_dir else '-'}")
        if run.changed_files:
            print("Changed files:\n  " + "\n  ".join(run.changed_files))
    return EXIT.get(run.status, 1)


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
