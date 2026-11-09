"""Battle plans: pre-built pipelines that chain specialists across the SDLC.

A pipeline is a list of stages. A stage deploys one agent, or a squad of
agents in parallel. A *gated* stage blocks the pipeline when any member
returns ``fail`` or ``needs_changes``; if the stage names a ``fixer``, the
fixer gets the findings and the squad re-checks, up to ``max_review_loops``.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Stage:
    name: str
    agents: list[str]
    task: str  # may reference {goal}
    gate: bool = False
    fixer: str | None = None

    @property
    def parallel(self) -> bool:
        return len(self.agents) > 1


@dataclass
class Pipeline:
    name: str
    description: str
    stages: list[Stage] = field(default_factory=list)
    read_only: bool = False  # never grants write permission, whatever the config says

    def agents(self) -> list[str]:
        seen: list[str] = []
        for st in self.stages:
            for a in st.agents + ([st.fixer] if st.fixer else []):
                if a not in seen:
                    seen.append(a)
        return seen


REVIEW_SQUAD = ["code_reviewer", "test_engineer", "security_auditor"]

PIPELINES: dict[str, Pipeline] = {}


def register(p: Pipeline, replace_existing: bool = False) -> Pipeline:
    """Add a custom pipeline (its agents must exist in the roster when it runs)."""
    if p.name in PIPELINES and not replace_existing:
        raise ValueError(f"Pipeline '{p.name}' already exists")
    PIPELINES[p.name] = p
    return p


_register = register


_register(Pipeline(
    "feature",
    "Idea to shippable change: requirements, design, plan, build, review squad, acceptance, docs, changelog.",
    [
        Stage("requirements", ["product_strategist"],
              "Write the requirements brief for this request:\n\n{goal}"),
        Stage("design", ["architect"],
              "Design the implementation for this request, based on the requirements above:\n\n{goal}"),
        Stage("plan", ["tech_lead"],
              "Write the step-by-step implementation plan for:\n\n{goal}"),
        Stage("build", ["developer"],
              "Implement the plan above, with tests, for:\n\n{goal}"),
        Stage("review", REVIEW_SQUAD,
              "Review the change just implemented for:\n\n{goal}\n\nFocus on your speciality.",
              gate=True, fixer="developer"),
        Stage("acceptance", ["qa_validator"],
              "Validate every acceptance criterion in the requirements against the implementation for:\n\n{goal}",
              gate=True, fixer="developer"),
        Stage("docs", ["docs_writer"],
              "Update the documentation affected by this change:\n\n{goal}"),
        Stage("changelog", ["release_manager"],
              "Add an Unreleased CHANGELOG entry for this change (do not cut a version):\n\n{goal}"),
    ],
))

_register(Pipeline(
    "bugfix",
    "Triage a bug, fix the root cause with a regression test, and verify with the review squad.",
    [
        Stage("triage", ["issue_triager"], "Triage this bug report:\n\n{goal}"),
        Stage("fix", ["bug_hunter"],
              "Reproduce, root-cause and fix this bug, adding a regression test:\n\n{goal}"),
        Stage("verify", ["code_reviewer", "test_engineer"],
              "Verify the fix for this bug is correct and well tested:\n\n{goal}",
              gate=True, fixer="bug_hunter"),
        Stage("changelog", ["release_manager"],
              "Add an Unreleased CHANGELOG entry under 'Fixed' for:\n\n{goal}"),
    ],
))

_register(Pipeline(
    "review",
    "Read-only pull-request review by code, security, performance and test specialists in parallel.",
    [
        Stage("review", ["code_reviewer", "security_auditor", "performance_analyst", "test_engineer"],
              "Review the current change set. {goal}\n\nReport only issues in your speciality.",
              gate=True),
    ],
    read_only=True,
))

_register(Pipeline(
    "security",
    "Security sweep: code audit, dependency audit and threat model in parallel.",
    [
        Stage("sweep", ["security_auditor", "dependency_auditor", "threat_modeler"],
              "Perform your security assessment of this repository. Scope / notes: {goal}", gate=True),
    ],
    read_only=True,
))

_register(Pipeline(
    "audit",
    "Whole-repository health check, synthesised into a prioritised engineering roadmap.",
    [
        Stage("survey", ["tech_debt_scout", "security_auditor", "dependency_auditor",
                         "performance_analyst", "observability_engineer"],
              "Assess this repository from your speciality. Do not change files. Notes: {goal}"),
        Stage("roadmap", ["tech_lead"],
              "Synthesise the audit reports above into a prioritised engineering roadmap. Notes: {goal}"),
    ],
    read_only=True,
))

_register(Pipeline(
    "refactor",
    "Find the worst technical debt, pay it down safely, and verify behaviour is unchanged.",
    [
        Stage("scout", ["tech_debt_scout"], "Find the highest-value refactoring targets. Focus: {goal}"),
        Stage("refactor", ["refactorer"],
              "Refactor the top targets from the debt backlog, keeping behaviour identical. Focus: {goal}"),
        Stage("verify", ["code_reviewer", "test_engineer"],
              "Verify the refactoring preserved behaviour and improved the code. Focus: {goal}",
              gate=True, fixer="refactorer"),
    ],
))

_register(Pipeline(
    "docs",
    "Codebase tour, README refresh and API reference.",
    [
        Stage("tour", ["onboarding_guide"], "Write a codebase tour. Notes: {goal}"),
        Stage("write", ["docs_writer", "api_documenter"],
              "Bring the documentation up to date using the codebase tour above. Notes: {goal}"),
    ],
))

_register(Pipeline(
    "release",
    "Prepare a release: changelog, version recommendation and user-facing release notes.",
    [
        Stage("readiness", ["test_engineer", "security_auditor"],
              "Check the repository is ready to release. Notes: {goal}", gate=True),
        Stage("notes", ["release_manager"],
              "Prepare the release: classify changes since the last tag, recommend the version, "
              "update CHANGELOG.md and write release notes. Notes: {goal}"),
    ],
))

_register(Pipeline(
    "incident",
    "Production incident: diagnose, mitigate, fix with a regression test, and write the postmortem.",
    [
        Stage("diagnose", ["incident_responder"], "Investigate this incident:\n\n{goal}"),
        Stage("fix", ["bug_hunter"],
              "Implement the durable fix identified in the incident report, with a regression test:\n\n{goal}"),
        Stage("verify", ["test_engineer", "code_reviewer"],
              "Verify the incident fix:\n\n{goal}", gate=True, fixer="bug_hunter"),
    ],
))

_register(Pipeline(
    "devops",
    "Set up or improve CI/CD and packaging, then review it.",
    [
        Stage("build", ["devops_engineer"], "Improve CI/CD and packaging for this repository. Notes: {goal}"),
        Stage("review", ["code_reviewer", "security_auditor"],
              "Review the CI/CD and packaging changes. Notes: {goal}", gate=True, fixer="devops_engineer"),
    ],
))


def get(name: str) -> Pipeline:
    try:
        return PIPELINES[name]
    except KeyError:
        raise KeyError(f"Unknown pipeline '{name}'. Available: {', '.join(PIPELINES)}") from None
