import subprocess

import pytest

from agent_army.config import ArmyConfig


@pytest.fixture
def workspace(tmp_path):
    (tmp_path / "app.py").write_text("def add(a, b):\n    return a + b\n")
    (tmp_path / "README.md").write_text("# Demo\n")
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    return tmp_path


@pytest.fixture
def config(workspace):
    return ArmyConfig.load(workspace, allow_exec=True)


def submit(verdict="pass", summary="done", findings=None, artifacts=None):
    return {"type": "tool_use", "name": "submit_report", "input": {
        "summary": summary, "verdict": verdict,
        "findings": findings or [], "artifacts": artifacts or [],
    }}


def call(name, **inp):
    return {"type": "tool_use", "name": name, "input": inp}
