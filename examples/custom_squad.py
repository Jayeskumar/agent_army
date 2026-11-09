"""Extend the army with your own specialist and battle plan.

Run it (no API key needed) with:

    python examples/custom_squad.py --dry-run

Drop --dry-run to use Claude (needs ANTHROPIC_API_KEY or `ant auth login`).
"""

import sys

from agent_army import Army, ArmyConfig, DryRunBackend
from agent_army.agent import AgentSpec
from agent_army.pipelines import Pipeline, Stage, register as register_pipeline
from agent_army.roster import RW, register as register_agent

register_agent(AgentSpec(
    name="i18n_specialist",
    title="Internationalisation Specialist",
    division="engineering",
    mission="""Find user-facing strings that are hard-coded and move them into the project's
translation catalogue, using the i18n library the project already has (or recommend one).
Flag concatenated sentences, hard-coded date/number formats and right-to-left layout issues.""",
    tiers=RW,
))

register_pipeline(Pipeline(
    "i18n",
    "Make the product translatable, then review the change.",
    [
        Stage("extract", ["i18n_specialist"], "Internationalise the user-facing strings. Scope: {goal}"),
        Stage("review", ["code_reviewer", "frontend_engineer"],
              "Review the i18n change for regressions. Scope: {goal}", gate=True, fixer="i18n_specialist"),
    ],
))

if __name__ == "__main__":
    dry = "--dry-run" in sys.argv
    army = Army(ArmyConfig.load("."), backend=DryRunBackend() if dry else None,
                on_event=lambda who, kind, detail: print(f"[{who}] {kind}: {detail}"))
    result = army.run_pipeline("i18n", "the settings page")
    print(f"\n{result.status}: {result.run_dir}/report.md")
