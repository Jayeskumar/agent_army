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


# ----------------------------------------------------------------- office work
_register(Pipeline(
    "campaign",
    "Marketing campaign: research, strategy, copy for every channel, then brand and fact checks.",
    [
        Stage("research", ["market_research_analyst", "persona_researcher"],
              "Research the market and audience for this campaign:\n\n{goal}"),
        Stage("strategy", ["campaign_strategist"], "Write the campaign brief for:\n\n{goal}"),
        Stage("create", ["copywriter", "email_marketer", "social_media_manager"],
              "Create your channel's assets for the campaign brief above:\n\n{goal}"),
        Stage("review", ["brand_guardian", "fact_checker"],
              "Check the campaign assets above:\n\n{goal}", gate=True, fixer="copywriter"),
    ],
))

_register(Pipeline(
    "hiring",
    "Open a role: intake, job description, compliance check, sourcing plan, outreach and interview kit.",
    [
        Stage("intake", ["hiring_manager_intake"], "Run the intake for this role:\n\n{goal}"),
        Stage("job_description", ["job_description_writer"], "Write the job description for:\n\n{goal}"),
        Stage("compliance", ["recruiting_compliance_checker"],
              "Check the job description and hiring plan for:\n\n{goal}", gate=True, fixer="job_description_writer"),
        Stage("launch", ["sourcing_specialist", "candidate_outreach_writer", "interview_kit_designer"],
              "Prepare your part of the hiring launch for:\n\n{goal}"),
    ],
))

_register(Pipeline(
    "month_end",
    "Month-end close: reconciliations, accruals, ledger review, statements, audit check and variance commentary.",
    [
        Stage("reconcile", ["bank_reconciler", "accruals_accountant", "intercompany_accountant"],
              "Do your month-end close work from the data in the workspace. Period / notes: {goal}"),
        Stage("ledger", ["general_ledger_accountant"],
              "Review the trial balance and prepare adjusting entries. Period / notes: {goal}"),
        Stage("statements", ["financial_statement_preparer"],
              "Prepare the financial statements. Period / notes: {goal}"),
        Stage("review", ["internal_auditor"],
              "Review the close for errors and unsupported entries. Period / notes: {goal}",
              gate=True, fixer="general_ledger_accountant"),
        Stage("commentary", ["fpa_analyst"],
              "Write the variance commentary against budget. Period / notes: {goal}"),
    ],
))

_register(Pipeline(
    "rfp",
    "Answer an RFP: requirements matrix, answers, pricing, proposal, then contract and editorial review.",
    [
        Stage("analyse", ["rfp_analyst"], "Analyse this RFP:\n\n{goal}"),
        Stage("answer", ["rfp_response_writer", "quote_builder", "security_questionnaire_responder"],
              "Draft your part of the RFP response:\n\n{goal}"),
        Stage("proposal", ["proposal_writer"], "Assemble the full proposal:\n\n{goal}"),
        Stage("review", ["contract_reviewer", "editor"],
              "Review the proposal before submission:\n\n{goal}", gate=True, fixer="proposal_writer"),
    ],
))

_register(Pipeline(
    "board_report",
    "Board or investor update: financial and KPI analysis, board pack, fact check and executive brief.",
    [
        Stage("analysis", ["fpa_analyst", "data_analyst"],
              "Analyse performance for the board update. Period / notes: {goal}"),
        Stage("pack", ["board_pack_writer"], "Write the board pack. Period / notes: {goal}"),
        Stage("check", ["fact_checker"],
              "Check every number and claim in the board pack against the workspace data. Notes: {goal}",
              gate=True, fixer="board_pack_writer"),
        Stage("brief", ["executive_briefer"], "Write the one-page executive brief. Notes: {goal}"),
    ],
))

_register(Pipeline(
    "research_report",
    "Sourced research report: research, analysis, writing, then fact-check and edit.",
    [
        Stage("research", ["research_analyst", "data_source_scout"], "Research this question:\n\n{goal}"),
        Stage("write", ["report_writer"], "Write the report from the research above:\n\n{goal}"),
        Stage("review", ["fact_checker", "editor"], "Review the report:\n\n{goal}",
              gate=True, fixer="report_writer"),
    ],
))

_register(Pipeline(
    "policy",
    "Write or update a company policy, review it for compliance and clarity, then announce it.",
    [
        Stage("draft", ["policy_manager"], "Draft or update this policy:\n\n{goal}"),
        Stage("review", ["compliance_officer", "editor"], "Review the policy draft:\n\n{goal}",
              gate=True, fixer="policy_manager"),
        Stage("announce", ["internal_communications_manager"],
              "Write the employee announcement for the policy:\n\n{goal}"),
    ],
))

_register(Pipeline(
    "product_launch",
    "Cross-team launch: launch plan, messaging, release notes, press, sales enablement and brand review.",
    [
        Stage("plan", ["product_launch_manager"], "Plan the launch:\n\n{goal}"),
        Stage("assets", ["product_marketing_manager", "release_notes_writer", "press_release_writer",
                         "sales_enablement_trainer"],
              "Create your launch assets:\n\n{goal}"),
        Stage("review", ["brand_guardian", "communications_reviewer"], "Review all launch assets:\n\n{goal}",
              gate=True, fixer="product_marketing_manager"),
    ],
))

_register(Pipeline(
    "support_insights",
    "Turn support data into insights, then into knowledge base articles and macros.",
    [
        Stage("analyse", ["voice_of_customer_analyst", "support_operations_analyst"],
              "Analyse the support data in the workspace. Notes: {goal}"),
        Stage("deflect", ["knowledge_base_writer", "support_macro_writer"],
              "Write content that resolves the top issues found above. Notes: {goal}"),
    ],
))

_register(Pipeline(
    "vendor_selection",
    "Pick a vendor: sourcing, risk assessment, comparison, contract review and a decision memo.",
    [
        Stage("source", ["procurement_specialist"], "Run the sourcing for:\n\n{goal}"),
        Stage("assess", ["vendor_risk_assessor", "comparative_analyst"], "Assess the shortlisted vendors:\n\n{goal}"),
        Stage("contract", ["contract_reviewer"], "Review the preferred vendor's contract terms:\n\n{goal}"),
        Stage("decide", ["decision_memo_writer"], "Write the vendor decision memo:\n\n{goal}"),
    ],
))

_register(Pipeline(
    "meeting_followup",
    "After a meeting: minutes with decisions and owners, follow-up emails and a task list.",
    [
        Stage("minutes", ["meeting_minutes_taker"], "Write the minutes from these notes or transcript:\n\n{goal}"),
        Stage("follow_up", ["email_drafter", "task_list_manager"],
              "Prepare the follow-ups from the minutes above:\n\n{goal}"),
    ],
))

_register(Pipeline(
    "employee_onboarding",
    "Welcome a new hire: onboarding plan, learning path, IT setup guide and welcome message.",
    [
        Stage("plan", ["onboarding_coordinator"], "Build the onboarding plan for:\n\n{goal}"),
        Stage("prepare", ["onboarding_curriculum_designer", "it_documentation_writer", "email_drafter"],
              "Prepare your part of this new hire's onboarding (learning path, IT setup guide, or welcome "
              "email):\n\n{goal}"),
    ],
))


_register(Pipeline(
    "grant_application",
    "Win a grant: funder research, proposal, budget, then fact-check and edit before submission.",
    [
        Stage("research", ["grant_prospect_researcher"], "Find and assess funders for:\n\n{goal}"),
        Stage("draft", ["grant_writer", "nonprofit_budget_planner", "theory_of_change_designer"],
              "Prepare your part of the grant application:\n\n{goal}"),
        Stage("review", ["fact_checker", "editor"], "Review the grant application:\n\n{goal}",
              gate=True, fixer="grant_writer"),
    ],
))

_register(Pipeline(
    "automation_blueprint",
    "Automate a business process: find opportunities, design the workflow and agent, assess risk, plan evaluation.",
    [
        Stage("scout", ["automation_opportunity_scout"], "Find what to automate in:\n\n{goal}"),
        Stage("design", ["workflow_automation_designer", "agent_designer"],
              "Design the automation for the top opportunity above:\n\n{goal}"),
        Stage("assure", ["ai_risk_assessor", "ai_eval_designer"], "Assess and plan evaluation of the design:\n\n{goal}",
              gate=True, fixer="workflow_automation_designer"),
        Stage("roi", ["automation_roi_analyst"], "Estimate the return on this automation:\n\n{goal}"),
    ],
))

_register(Pipeline(
    "course_creation",
    "Build a training course: design, content, assessments and a learning-quality review.",
    [
        Stage("design", ["instructional_designer"], "Design the course:\n\n{goal}"),
        Stage("build", ["training_content_writer", "assessment_builder", "workshop_guide_writer"],
              "Build your part of the course:\n\n{goal}"),
        Stage("review", ["editor", "accessibility_compliance_auditor"], "Review the course materials:\n\n{goal}",
              gate=True, fixer="training_content_writer"),
    ],
))

_register(Pipeline(
    "event_planning",
    "Plan an event: overall plan, budget, agenda, attendee communications and a risk check.",
    [
        Stage("plan", ["conference_planner"], "Plan this event:\n\n{goal}"),
        Stage("details", ["event_budget_planner", "agenda_designer", "attendee_communications_writer"],
              "Prepare your part of the event plan:\n\n{goal}"),
        Stage("risk", ["event_risk_planner"], "Check the event plan for risks:\n\n{goal}",
              gate=True, fixer="conference_planner"),
    ],
))


def get(name: str) -> Pipeline:
    try:
        return PIPELINES[name]
    except KeyError:
        raise KeyError(f"Unknown pipeline '{name}'. Available: {', '.join(PIPELINES)}") from None
