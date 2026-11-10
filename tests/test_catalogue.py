from pathlib import Path

from agent_army import roster
from agent_army.agent import Agent
from agent_army.catalogue import DEPARTMENTS, render_markdown
from agent_army.config import ArmyConfig
from agent_army.engine import Army
from agent_army.llm import ScriptedBackend
from agent_army.tools import Toolbox, web_tool_definitions

from conftest import call, submit


def test_army_has_more_than_1000_agents():
    assert len(roster.ROSTER) + 1 >= 1000  # plus the commander
    assert len(roster.catalogue_specs()) >= 990
    assert {roster.sector_of(d) for d in roster.divisions()} == {"SDLC core", "Business functions", "Industries"}
    assert len(roster.core_specs()) == 24


def test_every_department_is_populated_and_names_are_valid():
    groups = roster.divisions()
    for dept in DEPARTMENTS:
        assert len(groups[dept.name]) >= 20, dept.name
    for spec in roster.ROSTER.values():
        assert spec.name.isidentifier() and spec.name.islower(), spec.name
        assert spec.title and spec.mission.strip()
        assert "read" in spec.tiers


def test_catalogue_agents_have_deliverables_and_guardrails():
    for spec in roster.catalogue_specs():
        assert spec.deliverables, spec.name
        assert "Never invent facts" in spec.mission
    regulated = [s for s in roster.catalogue_specs() if s.division in {"legal", "finance", "accounting"}]
    assert regulated and all("qualified professional" in s.mission for s in regulated)


def test_search_finds_the_right_specialist():
    expectations = {
        "reconcile bank statements": "bank_reconciler",
        "press release": "press_release_writer",
        "NDA": "nda_specialist",
        "job description": "job_description_writer",
        "cash flow forecast": "cash_flow_forecaster",
        "kubernetes manifests": "kubernetes_engineer",
        "meeting minutes": "meeting_minutes_taker",
        "phishing": "phishing_analyst",
        "HACCP plan": "haccp_plan_writer",
        "deposition transcript summary": "deposition_summarizer",
        "planogram": "planogram_designer",
        "prior authorization": "prior_authorization_specialist",
        "pitch deck": "pitch_deck_writer",
    }
    for query, expected in expectations.items():
        hits = roster.search(query)
        assert hits and hits[0].name == expected, (query, [h.name for h in hits[:3]])
    assert all(s.division == "legal" for s in roster.search("review", department="legal"))


def test_unknown_agent_suggests_close_match():
    try:
        roster.get("contract_reviwer")
    except KeyError as exc:
        assert "contract_reviewer" in str(exc)


def test_web_tier_requires_opt_in(workspace):
    spec = roster.get("research_analyst")
    assert "web" in spec.tiers
    off = Toolbox(ArmyConfig.load(workspace), set(spec.tiers))
    assert not off.server_tool_names
    assert all(d["name"] not in {"web_search", "web_fetch"} for d in off.api_definitions("claude-opus-5-5"))
    on = Toolbox(ArmyConfig.load(workspace, allow_web=True), set(spec.tiers))
    defs = {d["name"]: d for d in on.api_definitions("claude-opus-5-5")}
    assert defs["web_search"]["type"] == "web_search_20260209"
    assert defs["web_fetch"]["type"] == "web_fetch_20260209"


def test_web_tool_variant_depends_on_model():
    basic = {d["name"]: d["type"] for d in web_tool_definitions("claude-haiku-5-5", 3)}
    assert basic == {"web_search": "web_search_20250305", "web_fetch": "web_fetch_20250910"}


def test_agent_prompt_mentions_disabled_web(workspace):
    agent = Agent(roster.get("research_analyst"), ArmyConfig.load(workspace), ScriptedBackend({}))
    assert "web research is disabled" in agent.system_prompt()


def test_commander_can_search_and_dispatch_office_agents(config):
    backend = ScriptedBackend({
        "commander": [
            [call("find_agents", query="reconcile bank statements")],
            [call("dispatch_agent", agent="bank_reconciler", task="Reconcile October")],
            [call("dispatch_agent", agent="bank_reconcilr", task="typo")],
            [submit("pass", "Books reconciled")],
        ],
        "bank_reconciler": [[submit("pass", "Reconciled, 2 items explained")]],
    })
    run = Army(config, backend=backend).mission("Close the October books")
    assert run.status == "completed"
    turns = [m for a, m in backend.calls if a == "commander"]
    assert "bank_reconciler" in turns[1][-1]["content"][0]["content"]
    assert "Closest matches: bank_reconciler" in turns[3][-1]["content"][0]["content"]


def test_catalogue_markdown_is_up_to_date():
    expected = render_markdown(roster.core_specs(), roster.catalogue_specs())
    path = Path(__file__).resolve().parent.parent / "CATALOGUE.md"
    assert path.read_text() == expected, "Regenerate with: python -m agent_army.catalogue > CATALOGUE.md"
