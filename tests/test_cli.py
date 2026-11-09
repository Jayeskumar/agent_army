from agent_army.cli import main


def test_roster_and_pipelines(capsys):
    assert main(["roster"]) == 0
    out = capsys.readouterr().out
    assert "developer" in out and "commander" in out
    assert main(["pipelines"]) == 0
    assert "feature" in capsys.readouterr().out


def test_dry_run_pipeline(workspace, capsys):
    code = main(["run", "bugfix", "Crash on empty input", "-C", str(workspace), "--dry-run", "-q"])
    assert code == 0
    assert "Status: completed" in capsys.readouterr().out
    assert main(["report", "-C", str(workspace)]) == 0
    assert "After-action report" in capsys.readouterr().out


def test_dry_run_deploy_json(workspace, capsys):
    code = main(["deploy", "onboarding_guide", "Tour please", "-C", str(workspace), "--dry-run", "-q", "--json"])
    assert code == 0
    assert '"verdict": "pass"' in capsys.readouterr().out


def test_init(workspace, capsys):
    assert main(["init", "-C", str(workspace)]) == 0
    assert (workspace / "army.yaml").exists() and (workspace / "ARMY.md").exists()


def test_unknown_agent_exits_cleanly(workspace):
    import pytest
    with pytest.raises(SystemExit):
        main(["deploy", "ghost", "x", "-C", str(workspace)])
