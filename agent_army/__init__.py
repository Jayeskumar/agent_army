"""Agent Army - a squad of specialised Claude agents for the whole software lifecycle."""

__version__ = "0.1.0"

from .agent import Agent, AgentReport, AgentSpec  # noqa: E402
from .config import ArmyConfig  # noqa: E402
from .engine import Army, RunResult  # noqa: E402
from .llm import ClaudeBackend, DryRunBackend, ScriptedBackend  # noqa: E402

__all__ = [
    "Agent", "AgentReport", "AgentSpec", "Army", "ArmyConfig", "RunResult",
    "ClaudeBackend", "DryRunBackend", "ScriptedBackend", "__version__",
]
