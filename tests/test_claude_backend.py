"""Drive the real Anthropic SDK client against a mock HTTP transport."""

import json

import anthropic
import httpx2

from agent_army import roster
from agent_army.agent import Agent
from agent_army.llm import ClaudeBackend


def _msg(content, stop="tool_use"):
    return {
        "id": "msg_x", "type": "message", "role": "assistant", "model": "claude-opus-5-5",
        "content": content, "stop_reason": stop, "stop_sequence": None,
        "usage": {"input_tokens": 100, "output_tokens": 20,
                  "cache_read_input_tokens": 80, "cache_creation_input_tokens": 0},
    }


def test_agent_round_trip_through_sdk(config):
    bodies = []
    replies = [
        _msg([{"type": "thinking", "thinking": "", "signature": "sig1"},
              {"type": "tool_use", "id": "toolu_1", "name": "read_file", "input": {"path": "app.py"}}]),
        _msg([{"type": "tool_use", "id": "toolu_2", "name": "submit_report", "input": {
            "summary": "Looks fine", "verdict": "pass", "findings": [], "artifacts": []}}]),
    ]

    def handler(request):
        bodies.append((dict(request.headers), json.loads(request.content)))
        return httpx2.Response(200, json=replies[len(bodies) - 1])

    client = anthropic.Anthropic(
        api_key="test-key", max_retries=0,
        http_client=anthropic.DefaultHttpxClient(transport=httpx2.MockTransport(handler)),
    )
    agent = Agent(roster.get("code_reviewer"), config, ClaudeBackend(client=client))
    report = agent.run("review app.py")

    assert report.verdict == "pass" and report.summary == "Looks fine"
    assert report.usage.input_tokens == 200 and report.usage.cache_read_tokens == 160

    headers, first = bodies[0]
    assert first["model"] == "claude-opus-5-5"
    assert first["thinking"] == {"type": "adaptive"}
    assert first["output_config"] == {"effort": "high"}
    assert first["cache_control"] == {"type": "ephemeral"}
    assert first["fallbacks"] == "default"
    assert "server-side-fallback-2026-07-01" in headers["anthropic-beta"]
    assert [t["name"] for t in first["tools"]] == sorted(t["name"] for t in first["tools"])

    _, second = bodies[1]
    assistant = second["messages"][1]
    assert assistant["role"] == "assistant"
    # The thinking block is passed back unchanged.
    assert assistant["content"][0] == {"type": "thinking", "thinking": "", "signature": "sig1"}
    tool_result = second["messages"][2]["content"][0]
    assert tool_result["tool_use_id"] == "toolu_1" and "return a + b" in tool_result["content"]


def test_no_fallbacks_for_other_models(config):
    bodies = []

    def handler(request):
        bodies.append(json.loads(request.content))
        return httpx2.Response(200, json=_msg([{"type": "text", "text": "ok"}], stop="end_turn"))

    client = anthropic.Anthropic(
        api_key="k", max_retries=0,
        http_client=anthropic.DefaultHttpxClient(transport=httpx2.MockTransport(handler)),
    )
    ClaudeBackend(client=client).complete(
        agent_name="a", model="claude-haiku-5-5", system="s",
        messages=[{"role": "user", "content": "hi"}], tools=[], max_tokens=10, effort="low",
    )
    assert "fallbacks" not in bodies[0]
