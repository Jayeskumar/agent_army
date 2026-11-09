from agent_army import roster
from agent_army.agent import Agent
from agent_army.llm import LLMResponse, ScriptedBackend, Usage

from conftest import call, submit


def run(config, name, steps, task="do it"):
    backend = ScriptedBackend({name: steps})
    agent = Agent(roster.get(name), config, backend)
    return agent.run(task), backend


def test_agent_uses_tools_then_submits(config, workspace):
    report, backend = run(config, "developer", [
        [{"type": "text", "text": "Reading."}, call("read_file", path="app.py")],
        [call("edit_file", path="app.py", old_text="a + b", new_text="b + a")],
        [submit("pass", "Swapped operands.", artifacts=[{"name": "notes", "content": "n"}])],
    ])
    assert report.verdict == "pass"
    assert report.summary == "Swapped operands."
    assert report.artifacts == {"notes": "n"}
    assert report.changed_files == ["app.py"]
    assert report.turns == 3
    # The tool result of turn 1 was fed back on turn 2.
    second_call_messages = backend.calls[1][1]
    results = second_call_messages[-1]["content"]
    assert results[0]["type"] == "tool_result" and "return a + b" in results[0]["content"]


def test_tool_errors_are_returned_not_raised(config):
    report, backend = run(config, "code_reviewer", [
        [call("read_file", path="../../etc/passwd")],
        [submit("pass")],
    ])
    assert report.verdict == "pass"
    err = backend.calls[1][1][-1]["content"][0]
    assert err["is_error"] is True and "escapes" in err["content"]


def test_unavailable_tool_is_an_error(config):
    report, backend = run(config, "code_reviewer", [  # reviewer is read-only
        [call("write_file", path="x.py", content="x")],
        [submit("pass")],
    ])
    err = backend.calls[1][1][-1]["content"][0]
    assert err["is_error"] and "not available" in err["content"]
    assert report.changed_files == []


def test_nudges_then_gives_up_without_submit(config):
    report, _ = run(config, "tech_lead", [
        [{"type": "text", "text": "Here is my plan."}],
        [{"type": "text", "text": "Still talking."}],
        [{"type": "text", "text": "Final words."}],
    ])
    assert report.verdict == "info"
    assert report.summary == "Final words."


def test_invalid_verdict_becomes_info(config):
    report, _ = run(config, "tech_lead", [[submit("great")]])
    assert report.verdict == "info"


def test_turn_limit(config):
    config.max_turns = 3
    report, _ = run(config, "tech_lead", [[call("list_files")]] * 3)
    assert report.verdict == "fail" and report.error == "turn limit reached"


class TruncatingBackend:
    def __init__(self):
        self.n = 0
        self.seen = []

    def complete(self, **kw):
        self.n += 1
        self.seen.append(list(kw["messages"]))
        if self.n == 1:
            blocks = [{"type": "tool_use", "id": "t1", "name": "write_file", "input": {"path": "a"}}]
            return LLMResponse(blocks, blocks, "max_tokens", Usage())
        blocks = [submit("pass") | {"id": "t2"}]
        return LLMResponse(blocks, blocks, "tool_use", Usage())


def test_max_tokens_turn_is_discarded(config, workspace):
    backend = TruncatingBackend()
    report = Agent(roster.get("developer"), config, backend).run("big task")
    assert report.verdict == "pass"
    retry = backend.seen[1]
    assert [m["role"] for m in retry] == ["user"]
    assert "output limit" in str(retry[0]["content"])
    assert not (workspace / "a").exists()


def test_standing_orders_in_system_prompt(config, workspace):
    (workspace / "ARMY.md").write_text("Always use tabs.")
    agent = Agent(roster.get("developer"), config, ScriptedBackend({}))
    assert "Always use tabs." in agent.system_prompt()


def test_refusal_fails(config):
    class Refuser:
        def complete(self, **kw):
            return LLMResponse([], [], "refusal", Usage())
    report = Agent(roster.get("developer"), config, Refuser()).run("x")
    assert report.verdict == "fail" and report.error == "refusal"
