from agent_army.cli import main


def test_roster_and_pipelines(capsys):
    assert main(["roster"]) == 0
    out = capsys.readouterr().out
    from agent_army import roster
    assert f"{len(roster.ROSTER) + 1} agents" in out and "accounting" in out and "commander" in out
    assert "Industries" in out
    assert main(["roster", "--all"]) == 0
    assert "developer" in capsys.readouterr().out
    assert main(["roster", "--search", "reconcile bank statements"]) == 0
    assert capsys.readouterr().out.splitlines()[0].split()[0] == "bank_reconciler"
    assert main(["roster", "--department", "legal"]) == 0
    assert "contract_reviewer" in capsys.readouterr().out
    assert main(["roster", "--show", "fpa_analyst"]) == 0
    assert "Deliverables" in capsys.readouterr().out
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


def test_unknown_agent_exits_cleanly(workspace, capsys):
    assert main(["deploy", "contract_reviwer", "x", "-C", str(workspace), "--dry-run"]) == 64
    assert "contract_reviewer" in capsys.readouterr().err  # suggestion
