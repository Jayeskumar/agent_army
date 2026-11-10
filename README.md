# 🪖 Agent Army

**556 Claude agents that handle the digital work of a whole office: software delivery,
finance, accounting, legal, compliance, HR, recruiting, marketing, sales, support, product,
design, data, IT, security, operations, communications, administration and more.**

Agent Army is organised like a company:

* **The commander** takes any mission, finds the right specialists among 555, sends them
  out in order and reacts to their reports.
* **24 core SDLC specialists** take software from a raw idea to reviewed, tested,
  documented and released code.
* **531 office specialists in 26 departments**, from the `bank_reconciler` and
  `contract_reviewer` to the `press_release_writer`, `interview_kit_designer`,
  `churn_risk_analyst` and `meeting_minutes_taker`.
* **22 pipelines** chain specialists together with parallel squads, **quality gates** and
  automatic **fix loops**: feature delivery, PR review, month-end close, RFP response,
  hiring, campaigns, board reports, policies, launches and more.

Every agent works on a real workspace (a code repository, or a folder of documents and
data), uses real tools, and files a structured report that the next specialist builds on.
**[Browse the full catalogue →](CATALOGUE.md)**

```
                    any mission: idea, ticket, contract, dataset, RFP, incident...
                                          │
                 ┌────────────────────────▼─────────────────────────┐
                 │   Commander (find_agents + dispatch_agent)       │
                 │   or a Pipeline (stages, squads, gates)          │
                 └────────────────────────┬─────────────────────────┘
  ┌───────────┬───────────┬────────────┬──┴─────────┬────────────┬────────────┬───────────┐
  SDLC core   Finance &   Legal &      People &     Growth:      Product,     Exec, IT, Eng,
  (24)        Accounting  Compliance   Talent, L&D  Mktg, Sales  Design, Data Ops, Comms,
              (40)        (40)         (61)         CS (84)      (61)         Admin... (245)
                                          │
                     reports + artifacts → shared blackboard → next specialist
                     gate blocked → findings go back to the fixer → re-check
```

---

## Quick start

```bash
pip install -e .                 # Python 3.10+
export ANTHROPIC_API_KEY=...     # or: ant auth login

cd /path/to/your/workspace       # a repo, or a folder of documents and data
army init                        # writes army.yaml + ARMY.md (standing orders) templates

army roster                                  # the 33 departments
army roster --search "reconcile bank"        # find a specialist
army deploy contract_reviewer @msa.md        # one specialist, one task
army run month_end "October 2026"            # a whole pipeline
army mission "Prepare everything we need to hire two support engineers in Berlin"
army report                                  # after-action report of the latest run
```

Rehearse anything for free with `--dry-run`: each agent looks around once and reports
success, so you can see how a pipeline is wired without calling the model.

## Commands

| Command | What it does |
|---|---|
| `army roster` | Departments and their agent counts |
| `army roster --department legal` | Every agent in a department |
| `army roster --search "<words>"` | Find agents by skill, deliverable or title |
| `army roster --show <agent>` | One agent's full brief |
| `army roster --all` | All 556 agents |
| `army pipelines` | Pipelines, their stages and gates |
| `army run <pipeline> "<goal>"` | Run a pipeline. The goal can be text, `-` (stdin) or `@file.md` |
| `army mission "<goal>"` | The commander plans and dispatches specialists dynamically |
| `army deploy <agent> "<task>"` | Send one specialist on one task |
| `army report [run_id]` | Print the Markdown after-action report |
| `army init` | Write `army.yaml` and `ARMY.md` templates |

Common flags: `-C <workspace>`, `--allow-exec`, `--allow-web`, `--read-only`, `--dry-run`,
`--model`, `--light-model`, `--effort low|medium|high|xhigh|max`, `--max-turns N`, `--json`, `-q`.

Exit codes are CI-friendly: `0` completed, `1` failed, `2` blocked by a quality gate.

## The departments

| Department | Agents | Examples |
|---|---|---|
| SDLC core (7 divisions) | 24 | `product_strategist`, `architect`, `developer`, `code_reviewer`, `test_engineer`, `security_auditor`, `release_manager`, `incident_responder` |
| Executive & Strategy | 20 | `okr_planner`, `board_pack_writer`, `decision_memo_writer`, `market_sizing_analyst`, `chief_of_staff` |
| Finance | 20 | `fpa_analyst`, `cash_flow_forecaster`, `financial_modeler`, `valuation_analyst`, `tax_research_analyst` |
| Accounting | 20 | `accounts_payable_clerk`, `bank_reconciler`, `month_end_close_coordinator`, `revenue_recognition_specialist`, `bookkeeper` |
| Legal | 20 | `contract_reviewer`, `nda_specialist`, `privacy_policy_writer`, `legal_researcher`, `corporate_secretary` |
| Compliance & Risk | 20 | `gdpr_specialist`, `soc2_readiness_specialist`, `enterprise_risk_manager`, `vendor_risk_assessor`, `carbon_accountant` |
| People & HR | 21 | `hr_generalist`, `compensation_analyst`, `performance_review_coach`, `workforce_planner`, `hr_policy_writer` |
| Talent Acquisition | 20 | `job_description_writer`, `sourcing_specialist`, `interview_kit_designer`, `offer_letter_drafter` |
| Learning & Development | 20 | `instructional_designer`, `assessment_builder`, `leadership_program_designer`, `technical_trainer` |
| Marketing | 22 | `campaign_strategist`, `seo_strategist`, `email_marketer`, `brand_guardian`, `ab_test_analyst` |
| Content & Creative | 21 | `copywriter`, `blog_writer`, `case_study_writer`, `editor`, `fact_checker`, `translator` |
| Sales | 21 | `sales_development_rep`, `proposal_writer`, `rfp_analyst`, `deal_desk_analyst`, `sales_forecaster` |
| Customer Success & Support | 20 | `support_agent`, `ticket_triager`, `knowledge_base_writer`, `churn_risk_analyst`, `qbr_preparer` |
| Product Management | 20 | `product_manager`, `prd_writer`, `roadmap_planner`, `prioritization_analyst`, `product_launch_manager` |
| Design & UX | 20 | `ux_researcher`, `journey_mapper`, `wireframe_designer`, `accessibility_designer`, `prototype_builder` |
| Data & Analytics | 21 | `data_analyst`, `sql_analyst`, `data_quality_analyst`, `statistician`, `data_scientist` |
| IT Operations | 20 | `it_helpdesk_agent`, `identity_access_admin`, `software_license_manager`, `it_change_manager` |
| Cybersecurity | 20 | `soc_analyst`, `vulnerability_manager`, `phishing_analyst`, `cloud_security_auditor`, `incident_response_planner` |
| Software Engineering | 22 | `backend_engineer`, `mobile_engineer`, `api_designer`, `integration_engineer`, `flaky_test_investigator` |
| Cloud & DevOps | 20 | `cloud_architect`, `iac_engineer`, `kubernetes_engineer`, `site_reliability_engineer`, `finops_analyst` |
| Operations & Supply Chain | 20 | `procurement_specialist`, `inventory_planner`, `demand_planner`, `logistics_coordinator`, `process_documenter` |
| Project & Program Management | 20 | `project_manager`, `scrum_master`, `status_report_writer`, `meeting_minutes_taker`, `change_manager` |
| Communications & PR | 20 | `press_release_writer`, `crisis_communications_lead`, `internal_communications_manager`, `executive_ghostwriter` |
| Office & Administration | 21 | `executive_assistant`, `inbox_triager`, `calendar_planner`, `travel_planner`, `spreadsheet_assistant` |
| Research & Knowledge | 20 | `research_analyst`, `literature_reviewer`, `document_qa_specialist`, `grant_writer`, `wiki_gardener` |
| E-commerce | 20 | `product_listing_writer`, `catalog_data_manager`, `promotions_planner`, `order_fraud_analyst` |
| Industry Specialists | 22 | `lease_abstractor`, `medical_billing_specialist`, `lesson_planner`, `construction_estimator`, `paralegal` |

The full list, with every agent's mission, deliverables and tools, is in **[CATALOGUE.md](CATALOGUE.md)**.

Every office specialist has named **deliverables** (for example `fpa_analyst` delivers
`forecast` and `variance_analysis`). It submits them as artifacts in its report and, when it
has write access, saves them under `deliverables/<agent>/`. Every office specialist is told
never to invent facts, figures, names, quotes or sources, and to list open questions
instead. Agents in regulated fields (finance, accounting, legal, compliance, HR, industry
specialists) also mark their output as a draft for a qualified professional to review.

## Pipelines

| Pipeline | Stages (‖ = parallel squad, 🚧 = gate with fix loop) |
|---|---|
| **Software** | |
| `feature` | requirements → design → plan → build → 🚧 review (code ‖ tests ‖ security) → 🚧 acceptance → docs → changelog |
| `bugfix` | triage → fix → 🚧 verify (code ‖ tests) → changelog |
| `review` *(read-only)* | 🚧 code ‖ security ‖ performance ‖ tests |
| `security` *(read-only)* | 🚧 code audit ‖ dependency audit ‖ threat model |
| `audit` *(read-only)* | debt ‖ security ‖ dependencies ‖ performance ‖ observability → roadmap |
| `refactor` | scout → refactor → 🚧 verify |
| `docs` | codebase tour → docs ‖ API reference |
| `release` | 🚧 readiness (tests ‖ security) → changelog + release notes |
| `incident` | diagnose → fix → 🚧 verify |
| `devops` | CI/CD and packaging → 🚧 review |
| **Office** | |
| `campaign` | market research ‖ personas → campaign brief → copy ‖ email ‖ social → 🚧 brand ‖ fact check |
| `hiring` | intake → job description → 🚧 compliance check → sourcing ‖ outreach ‖ interview kit |
| `month_end` | bank rec ‖ accruals ‖ intercompany → ledger review → statements → 🚧 internal audit → variance commentary |
| `rfp` | RFP analysis → answers ‖ quote ‖ security questionnaire → proposal → 🚧 contract ‖ editorial review |
| `board_report` | FP&A ‖ data analysis → board pack → 🚧 fact check → executive brief |
| `research_report` | research ‖ source scouting → report → 🚧 fact check ‖ edit |
| `policy` | draft → 🚧 compliance ‖ editorial review → employee announcement |
| `product_launch` | launch plan → messaging ‖ release notes ‖ press release ‖ sales training → 🚧 brand ‖ comms review |
| `support_insights` | voice of customer ‖ support ops analysis → knowledge base ‖ macros |
| `vendor_selection` | sourcing → risk ‖ comparison → contract review → decision memo |
| `meeting_followup` | minutes → follow-up emails ‖ task list |
| `employee_onboarding` | onboarding plan → learning path ‖ IT setup guide ‖ welcome email |

**How gates work:** each agent ends by submitting a structured report with a verdict
(`pass`, `needs_changes`, `fail`, `info`), findings (severity, location, detail) and named
artifacts. If any member of a gated stage returns `needs_changes` or `fail`, the stage's
fixer gets those findings, and then only the agents that blocked check again. This repeats
up to `max_review_loops` times; after that the run stops as **blocked**.

**How context flows:** a shared blackboard holds every report. Each agent receives the
mission goal plus the latest report (summary, findings and artifacts) from every
specialist that ran before it.

**How the commander copes with 555 specialists:** its prompt lists the departments, not
every agent. It calls `find_agents` to search the roster by skill or deliverable, then
`dispatch_agent` to deploy someone. If it gets a name wrong, it is offered the closest matches.

## How it works

* **Agents** (`agent_army/agent.py`) run their own tool-use loop on the Claude API. Their
  system prompt is the shared doctrine, plus the specialist's mission, plus your workspace's
  standing orders (`ARMY.md`, `AGENTS.md` or `CLAUDE.md`). Each agent finishes by calling
  `submit_report`.
* **Roster** (`agent_army/roster.py`): the 24 core specialists are written out in full. The
  531 office specialists come from compact department files in `agent_army/catalogue/`
  (one line per role: name, title, mission, deliverables, tools), which are expanded into
  full briefs.
* **Tools** (`agent_army/tools.py`): `list_files`, `read_file`, `search_code`, `git_diff`,
  `git_log` (read); `write_file`, `edit_file`, `delete_file` (write); `run_command` (exec);
  server-side `web_search` and `web_fetch` (web, for research roles, opt-in).
* **Engine** (`agent_army/engine.py`) runs pipelines, parallel squads (on a thread pool),
  gates, fix loops and commander missions. It writes every run to
  `.army/runs/<run_id>/` as `run.json` and `report.md`.
* **Model calls** (`agent_army/llm.py`) use the official `anthropic` SDK with:
  * `claude-opus-5-5` by default, with adaptive thinking and an explicit `effort` (default `high`).
  * Automatic prompt caching (`cache_control`), so the stable prefix (tools, system prompt,
    earlier turns) is read from cache on every loop iteration.
  * **Server-side refusal fallbacks on by default** (`fallbacks: "default"`) for models that
    support them: if a safety classifier declines a request, the API retries it on a fallback
    model within the same call. Turn this off with `--no-fallbacks` or `use_fallbacks: false`.
  * Assistant turns are passed back exactly as returned, so thinking blocks and web-search
    results stay valid. A turn cut off at `max_tokens` is discarded, and the agent is asked to
    work in smaller steps.

## Safety model

* **Workspace jail:** every path is resolved and must stay inside the workspace, and
  `.git/` is never writable.
* **No shell:** commands are parsed with `shlex` and run without a shell. Pipes, redirects
  and chaining are rejected.
* **Allow-listed commands only** (tests, linters, type checkers, builds, read-only git).
  `rm`, `sudo`, `curl`, `ssh` and `git push/reset/checkout/...` are always refused.
* **Running commands is off by default** (`--allow-exec`). **Web research is off by
  default** (`--allow-web`); even then, only research roles get it.
* **Credentials are scrubbed** from the environment of every command an agent runs.
* **Read-only pipelines** (`review`, `security`, `audit`) never get write tools. `--read-only`
  forbids writes on any run.
* Agents never commit, push, send emails or contact anyone. They produce drafts and files
  for you to review.

## Configuration (`army.yaml`)

```yaml
model: claude-opus-5-5
light_model: claude-sonnet-5-5  # optional: used by admin, L&D, docs, triage and release agents
effort: high                    # low | medium | high | xhigh | max
max_turns: 40                   # tool round-trips per agent
max_review_loops: 3
max_parallel: 4
allow_write: true
allow_exec: false
allow_web: false
web_max_uses: 5
command_timeout: 300
extra_allowed_commands: ["poetry run pytest", "pnpm test"]
```

The environment variables `ARMY_MODEL`, `ARMY_LIGHT_MODEL`, `ARMY_EFFORT`, `ARMY_MAX_TURNS`,
`ARMY_ALLOW_EXEC` and `ARMY_ALLOW_WEB` override the file, and CLI flags override both.

## CI/CD integration

* `.github/workflows/ci.yml` runs the test suite and dry-runs every pipeline.
* `.github/workflows/army-pr-review.yml`: label a PR `army:review` and the review squad
  reviews it, posts the after-action report as a PR comment, and fails the check if the
  gate blocks. It needs the `ANTHROPIC_API_KEY` repository secret.
* `.github/workflows/army-issue-triage.yml`: label an issue `army:triage` to get a triage comment.

## Growing the army

Add a role by adding one line to a department in `agent_army/catalogue/`:

```
expense_policy_coach | Expense Policy Coach | Answer employees' expense questions from the policy and explain why. | expense_answers
```

Then regenerate the catalogue: `python -m agent_army.catalogue > CATALOGUE.md`.

Or register agents and pipelines from code:

```python
from agent_army import Army, ArmyConfig
from agent_army.agent import AgentSpec
from agent_army.pipelines import Pipeline, Stage, register as register_pipeline
from agent_army.roster import RW, register as register_agent

register_agent(AgentSpec("i18n_specialist", "Internationalisation Specialist", "software_engineering",
                         "Move hard-coded user-facing strings into the translation catalogue.", RW))
register_pipeline(Pipeline("i18n", "Make the UI translatable", [
    Stage("extract", ["i18n_specialist"], "Internationalise: {goal}"),
    Stage("review", ["code_reviewer"], "Review the i18n change: {goal}", gate=True, fixer="i18n_specialist"),
]))

result = Army(ArmyConfig.load(".")).run_pipeline("i18n", "the settings page")
print(result.status, result.run_dir)
```

See `examples/custom_squad.py`, `examples/army.yaml` and `examples/missions.md`.

## Development

```bash
pip install -e ".[dev]"
python -m pytest -q
```

Tests never call the API. `ScriptedBackend` replays canned model turns, `DryRunBackend`
rehearses pipelines, and the SDK integration runs against a mock HTTP transport. A test
fails if `CATALOGUE.md` is out of date.

## Roadmap

* Connectors (MCP) for email, calendars, CRMs, ticketing and accounting systems, behind
  human approval for anything that sends or changes data outside the workspace
* Git worktree isolation per run, plus automatic branch and PR creation
* Persistent memory across runs (lessons learned, house style, glossary)
* Cost budgets per run and per-department model routing from `army.yaml`
* Web dashboard for live runs
