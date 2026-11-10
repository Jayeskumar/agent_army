"""Runtime configuration for the army.

Configuration is resolved in this order (later wins):
  1. built-in defaults
  2. ``army.yaml`` in the workspace root (if present)
  3. environment variables (``ARMY_MODEL``, ``ARMY_EFFORT``, ...)
  4. explicit CLI flags
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field, fields, replace
from pathlib import Path
from typing import Any

import yaml

DEFAULT_MODEL = "claude-opus-5-5"

# Commands an agent may run when shell access is enabled. Each entry is a
# command prefix matched token-by-token against the parsed argv.
DEFAULT_ALLOWED_COMMANDS: list[str] = [
    "python -m pytest",
    "pytest",
    "python -m unittest",
    "python -m pip list",
    "python -m compileall",
    "ruff",
    "mypy",
    "npm test",
    "npm run lint",
    "npm run build",
    "npx tsc",
    "go test",
    "go vet",
    "go build",
    "cargo test",
    "cargo check",
    "make test",
    "git status",
    "git diff",
    "git log",
    "git show",
    "ls",
]


@dataclass
class ArmyConfig:
    """Everything an agent run needs to know about its environment."""

    workspace: Path = field(default_factory=lambda: Path.cwd())
    model: str = DEFAULT_MODEL
    # Cheaper model used by agents flagged ``light=True`` in the roster
    # (triage, summarising). Defaults to the main model.
    light_model: str | None = None
    effort: str = "high"  # low | medium | high | xhigh | max
    max_tokens: int = 16000
    max_turns: int = 40  # tool-use round trips per agent
    allow_write: bool = True
    allow_exec: bool = False
    allow_web: bool = False  # server-side web search / fetch for agents with the web tier
    web_max_uses: int = 5  # per tool, per model request
    allowed_commands: list[str] = field(default_factory=lambda: list(DEFAULT_ALLOWED_COMMANDS))
    command_timeout: int = 300
    max_review_loops: int = 3
    max_parallel: int = 4
    use_fallbacks: bool = True  # server-side refusal fallbacks
    runs_dir: str = ".army/runs"
    verbose: bool = False

    @property
    def runs_path(self) -> Path:
        return self.workspace / self.runs_dir

    def model_for(self, light: bool) -> str:
        if light and self.light_model:
            return self.light_model
        return self.model

    def with_overrides(self, **overrides: Any) -> "ArmyConfig":
        clean = {k: v for k, v in overrides.items() if v is not None}
        return replace(self, **clean)

    @classmethod
    def load(cls, workspace: str | Path | None = None, **overrides: Any) -> "ArmyConfig":
        ws = Path(workspace or Path.cwd()).resolve()
        data: dict[str, Any] = {}

        cfg_file = ws / "army.yaml"
        if cfg_file.exists():
            loaded = yaml.safe_load(cfg_file.read_text()) or {}
            if not isinstance(loaded, dict):
                raise ValueError(f"{cfg_file} must contain a mapping")
            data.update(loaded)

        env_map = {
            "ARMY_MODEL": ("model", str),
            "ARMY_LIGHT_MODEL": ("light_model", str),
            "ARMY_EFFORT": ("effort", str),
            "ARMY_MAX_TURNS": ("max_turns", int),
            "ARMY_ALLOW_EXEC": ("allow_exec", _parse_bool),
            "ARMY_ALLOW_WEB": ("allow_web", _parse_bool),
        }
        for env, (key, conv) in env_map.items():
            if env in os.environ:
                data[key] = conv(os.environ[env])

        extra_cmds = data.pop("extra_allowed_commands", None)
        known = {f.name for f in fields(cls)}
        unknown = set(data) - known
        if unknown:
            raise ValueError(f"Unknown config keys in army.yaml: {sorted(unknown)}")

        data["workspace"] = ws
        cfg = cls(**data)
        if extra_cmds:
            cfg.allowed_commands.extend(extra_cmds)
        return cfg.with_overrides(**overrides)


def _parse_bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}
