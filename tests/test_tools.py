import pytest

from agent_army.config import ArmyConfig
from agent_army.tools import Toolbox, ToolError


def box(config, tiers=("read", "write", "exec")):
    return Toolbox(config, set(tiers))


def test_read_and_list(config):
    tb = box(config)
    assert "app.py" in tb.list_files()
    assert "return a + b" in tb.read_file("app.py")
    assert "app.py:2:" in tb.search_code(r"return")


def test_paths_cannot_escape_workspace(config):
    tb = box(config)
    for bad in ("../outside.txt", "/etc/passwd", "sub/../../x"):
        with pytest.raises(ToolError):
            tb.write_file(bad, "x")
    with pytest.raises(ToolError):
        tb.read_file("../../etc/passwd")


def test_no_writes_into_git_dir(config):
    with pytest.raises(ToolError):
        box(config).write_file(".git/hooks/pre-commit", "evil")


def test_edit_requires_unique_match(config, workspace):
    tb = box(config)
    (workspace / "dup.py").write_text("x = 1\nx = 1\n")
    with pytest.raises(ToolError, match="2 places"):
        tb.edit_file("dup.py", "x = 1", "x = 2")
    with pytest.raises(ToolError, match="not found"):
        tb.edit_file("app.py", "nope", "x")
    tb.edit_file("app.py", "a + b", "b + a")
    assert "b + a" in (workspace / "app.py").read_text()
    assert tb.changed_files == {"app.py"}


def test_command_allowlist(config):
    tb = box(config)
    assert tb.command_allowed(["python", "-m", "pytest", "-q"])
    assert tb.command_allowed(["git", "status"])
    assert not tb.command_allowed(["bash", "-c", "ls"])
    assert not tb.command_allowed(["git", "push"])
    assert not tb.command_allowed(["ls", "rm"])
    with pytest.raises(ToolError, match="Shell operators"):
        tb.run_command("pytest && rm -rf /")
    with pytest.raises(ToolError, match="not allowed"):
        tb.run_command("python evil.py")


def test_run_command(config):
    out = box(config).run_command("git status")
    assert out.startswith("[exit code 0]")


def test_tiers_respect_config(workspace):
    cfg = ArmyConfig.load(workspace, allow_write=False, allow_exec=False)
    tb = Toolbox(cfg, {"read", "write", "exec"})
    assert "write_file" not in tb.names
    assert "run_command" not in tb.names
    assert "read_file" in tb.names and "submit_report" in tb.names
    with pytest.raises(ToolError):
        tb.execute("write_file", {"path": "x", "content": "y"})


def test_tool_definitions_are_strict_objects(config):
    for d in box(config).api_definitions():
        assert d["input_schema"]["type"] == "object"
        assert d["input_schema"]["additionalProperties"] is False


def test_config_rejects_unknown_keys(workspace):
    (workspace / "army.yaml").write_text("modle: typo\n")
    with pytest.raises(ValueError, match="modle"):
        ArmyConfig.load(workspace)


def test_config_extra_commands(workspace):
    (workspace / "army.yaml").write_text("effort: low\nextra_allowed_commands: ['poetry run pytest']\n")
    cfg = ArmyConfig.load(workspace)
    assert cfg.effort == "low"
    assert "poetry run pytest" in cfg.allowed_commands


def test_commands_do_not_see_secrets(monkeypatch):
    from agent_army.tools import scrubbed_env
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
    monkeypatch.setenv("GITHUB_TOKEN", "ghp")
    monkeypatch.setenv("PATH_EXTRA", "ok")
    env = scrubbed_env()
    assert "ANTHROPIC_API_KEY" not in env and "GITHUB_TOKEN" not in env
    assert env["PATH_EXTRA"] == "ok"
