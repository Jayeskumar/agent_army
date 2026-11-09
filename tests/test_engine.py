import json

from agent_army.engine import Army
from agent_army.llm import DryRunBackend, ScriptedBackend
from agent_army.pipelines import PIPELINES, Pipeline, Stage
from agent_army import roster

from conftest import call, submit


def test_every_pipeline_references_real_agents():
    for p in PIPELINES.values():
        for a in p.agents():
            assert a in roster.ROSTER, (p.name, a)
        for st in p.stages:
            st.task.format(goal="g")  # templates are valid


def test_dry_run_every_pipeline(config):
    army = Army(config, backend=DryRunBackend())
    for name in PIPELINES:
        run = army.run_pipeline(name, "rehearsal")
        assert run.status == "completed", name
        assert (run.run_dir / "report.md").exists()
        data = json.loads((run.run_dir / "run.json").read_text())
        assert data["status"] == "completed"


def test_gate_fix_loop(config):
    pipe = Pipeline("t", "test", [
        Stage("build", ["developer"], "build {goal}"),
        Stage("review", ["code_reviewer", "security_auditor"], "review {goal}", gate=True, fixer="developer"),
    ])
    finding = {"severity": "high", "title": "Off by one", "detail": "loop bound", "location": "app.py:2"}
    backend = ScriptedBackend({
        "developer": [[submit("pass", "built")], [submit("pass", "fixed off by one")]],
        "code_reviewer": [[submit("needs_changes", "bug", findings=[finding])], [submit("pass", "lgtm")]],
        "security_auditor": [[submit("pass", "secure")]],
    })
    run = Army(config, backend=backend).run_pipeline(pipe, "feature X")
    assert run.status == "completed"
    review = run.stages[1]
    assert review.status == "passed" and review.loops == 1
    # The fixer saw the finding; only the blocking reviewer re-checked.
    fixer_task = [m for a, m in backend.calls if a == "developer"][1][0]["content"]
    assert "Off by one" in fixer_task
    assert [r.agent for r in review.reports] == ["code_reviewer", "security_auditor", "developer", "code_reviewer"]
    # Later agents see earlier reports as context.
    reviewer_ctx = [m for a, m in backend.calls if a == "code_reviewer"][0][0]["content"]
    assert "Report from developer" in reviewer_ctx and "feature X" in reviewer_ctx


def test_gate_blocks_after_max_loops(config):
    config.max_review_loops = 1
    pipe = Pipeline("t", "test", [
        Stage("review", ["code_reviewer"], "review", gate=True, fixer="developer"),
        Stage("never", ["docs_writer"], "docs"),
    ])
    backend = ScriptedBackend({
        "code_reviewer": [[submit("needs_changes")], [submit("needs_changes")]],
        "developer": [[submit("pass")]],
    })
    run = Army(config, backend=backend).run_pipeline(pipe, "g")
    assert run.status == "blocked"
    assert len(run.stages) == 1


def test_gate_without_fixer_blocks_immediately(config):
    backend = ScriptedBackend({
        "code_reviewer": [[submit("needs_changes")]],
        "security_auditor": [[submit("pass")]],
        "performance_analyst": [[submit("pass")]],
        "test_engineer": [[submit("pass")]],
    })
    run = Army(config, backend=backend).run_pipeline("review", "PR #1")
    assert run.status == "blocked"


def test_read_only_pipeline_has_no_write_tools(config):
    seen = {}

    class Spy(DryRunBackend):
        def complete(self, **kw):
            seen[kw["agent_name"]] = {t["name"] for t in kw["tools"]}
            return super().complete(**kw)

    Army(config, backend=Spy()).run_pipeline("review", "x")
    assert "write_file" not in seen["test_engineer"]
    assert "run_command" in seen["test_engineer"]


def test_mission_dispatches_specialists(config):
    backend = ScriptedBackend({
        "commander": [
            [call("dispatch_agent", agent="issue_triager", task="triage it")],
            [call("dispatch_agent", agent="nobody", task="x")],
            [submit("pass", "mission accomplished")],
        ],
        "issue_triager": [[submit("info", "it's a bug", artifacts=[{"name": "triage", "content": "bug/P2"}])]],
    })
    run = Army(config, backend=backend).mission("Handle issue #7")
    assert run.status == "completed"
    assert [r.agent for r in run.reports] == ["issue_triager", "commander"]
    commander_turn2 = [m for a, m in backend.calls if a == "commander"][1]
    result = commander_turn2[-1]["content"][0]["content"]
    assert "bug/P2" in result
    commander_turn3 = [m for a, m in backend.calls if a == "commander"][2]
    assert "unknown agent" in commander_turn3[-1]["content"][0]["content"]


def test_llm_error_fails_pipeline(config):
    backend = ScriptedBackend({})  # raises LLMError: no steps
    run = Army(config, backend=backend).run_pipeline("docs", "x")
    assert run.status == "failed"
    assert run.reports[0].error
