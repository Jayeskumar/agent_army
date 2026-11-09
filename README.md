# 🪖 Agent Army

**A team of specialised Claude agents that automates the software development lifecycle,
from a raw idea to reviewed, tested, documented and released code.**

Agent Army gives you 24 specialists (product strategist, architect, engineers, reviewers,
testers, security auditors, DevOps, release, incident response, docs and more). They work
on your repository with real tools, hand structured reports to each other, and are
organised into **pipelines** with **quality gates** and automatic **fix loops**. You can
also hand a mission to the **Commander**, who decides which specialists to send and in
what order.

```
          idea / ticket / bug / incident / PR
                         │
     ┌───────────────────▼────────────────────┐
     │  Commander (dynamic)  or  Pipeline     │
     └───────────────────┬────────────────────┘
   strategy ─► engineering ─► quality ‖ security ─► acceptance ─► knowledge ─► operations
   PRD, design   code + tests   review squad in parallel   QA gate   docs     changelog
                     ▲                 │
                     └── fix loop ◄────┘   (gate blocked → findings go back to the engineer)
```

---

## Quick start

```bash
pip install -e .                 # Python 3.10+
export ANTHROPIC_API_KEY=...     # or: ant auth login

cd /path/to/your/repo
army init                        # writes army.yaml + ARMY.md (standing orders) templates
army run feature "Users can export their dashboard as CSV" --allow-exec
army report                      # after-action report of the latest run
```

Rehearse anything for free with `--dry-run`: every agent looks around once and reports
success, so you can see how a pipeline is wired without calling the model.

```bash
army run feature "Add a subtract function" --dry-run
```

## Commands

| Command | What it does |
|---|---|
| `army roster [--division D]` | List every specialist and the permissions they have |
| `army pipelines` | List the battle plans and their stages and gates |
| `army run <pipeline> "<goal>"` | Run a pipeline. Goal can be text, `-` (stdin) or `@file.md` |
| `army mission "<goal>"` | The Commander plans and dispatches specialists dynamically |
| `army deploy <agent> "<task>"` | Send one specialist on one task |
| `army report [run_id]` | Print the Markdown after-action report |
| `army init` | Write `army.yaml` and `ARMY.md` templates |

Common flags: `-C <repo>`, `--allow-exec`, `--read-only`, `--dry-run`, `--model`,
`--light-model`, `--effort low|medium|high|xhigh|max`, `--max-turns N`, `--json`, `-q`.

Exit codes are CI friendly: `0` completed, `1` failed, `2` blocked by a quality gate.

## The roster

| Division | Agent | Job | Tools |
|---|---|---|---|
| Strategy | `product_strategist` | Idea → requirements brief with Given/When/Then acceptance criteria | read |
| | `architect` | Design: components, data model, interfaces, trade-offs, ADRs | read, write |
| | `tech_lead` | Ordered implementation plan; or a roadmap from audit reports | read |
| Engineering | `developer` | Implements the plan with tests; fixes review findings | read, write, exec |
| | `frontend_engineer` | UI components, state, accessibility | read, write, exec |
| | `data_engineer` | Schemas, safe migrations, queries | read, write, exec |
| | `refactorer` | Behaviour-preserving structural improvements | read, write, exec |
| | `bug_hunter` | Reproduce → root cause → fix → regression test | read, write, exec |
| Quality | `code_reviewer` | Reviews the diff for real bugs, not nits | read |
| | `test_engineer` | Adds missing tests and runs the suite | read, write, exec |
| | `qa_validator` | Checks every acceptance criterion with evidence | read, exec |
| | `performance_analyst` | Complexity, N+1s, blocking I/O, memory growth | read, exec |
| Security | `security_auditor` | Injection, authz, secrets, SSRF, traversal... | read |
| | `dependency_auditor` | Pinning, risky packages, licences, upgrades | read, exec |
| | `threat_modeler` | STRIDE threat model of system or design | read |
| Operations | `devops_engineer` | CI/CD workflows, Dockerfiles, build scripts | read, write |
| | `release_manager` | Changelog, semver recommendation, release notes | read, write |
| | `incident_responder` | Diagnosis, mitigation, blameless postmortem | read, exec |
| | `observability_engineer` | Logging, metrics and tracing gaps | read, write |
| Knowledge | `docs_writer` | README, guides, docstrings | read, write |
| | `api_documenter` | API reference from code | read, write |
| | `onboarding_guide` | Codebase tour for new engineers | read |
| Maintenance | `issue_triager` | Classify, prioritise, route issues | read |
| | `tech_debt_scout` | Prioritised technical-debt backlog | read |
| Command | `commander` | Leads `army mission`, dispatching the others | read, dispatch |

## Pipelines

| Pipeline | Stages (‖ = parallel squad, 🚧 = gate with fix loop) |
|---|---|
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

**How gates work:** each agent ends by submitting a structured report with a verdict
(`pass`, `needs_changes`, `fail`, `info`), findings (severity, location, detail) and named
artifacts. If any member of a gated stage returns `needs_changes` or `fail`, the stage's
fixer gets those findings, and then only the agents that blocked check again. This repeats
up to `max_review_loops` times; after that the run stops as **blocked**.

**How context flows:** a shared blackboard holds every report. Each agent receives the
mission goal plus the latest report (summary, findings, artifacts such as `requirements`,
`design` and `plan`) from every specialist that ran before it.

## How it works

* **Agents** (`agent_army/agent.py`) run their own tool-use loop on the Claude API: shared
  doctrine plus the specialist's mission plus your project's standing orders (`ARMY.md`,
  `AGENTS.md` or `CLAUDE.md`) form the system prompt. Each agent finishes by calling
  `submit_report`.
* **Tools** (`agent_army/tools.py`): `list_files`, `read_file`, `search_code`, `git_diff`,
  `git_log` (read); `write_file`, `edit_file`, `delete_file` (write); `run_command` (exec).
* **Engine** (`agent_army/engine.py`) runs pipelines, parallel squads (thread pool), gates,
  fix loops and Commander missions, and writes every run to `.army/runs/<run_id>/`
  (`run.json` + `report.md`).
* **Model calls** (`agent_army/llm.py`) use the official `anthropic` SDK with:
  * `claude-opus-5-5` by default, with adaptive thinking and an explicit `effort` (default `high`).
  * Automatic prompt caching (`cache_control`), so the stable prefix (tools, system prompt,
    earlier turns) is read from cache on every loop iteration. Tool definitions are sorted
    so the prefix stays byte-stable.
  * **Server-side refusal fallbacks enabled by default** (`fallbacks: "default"`, beta
    `server-side-fallback-2026-07-01`) on models that support them. If a safety classifier
    declines a request, the API retries it on a fallback model within the same call. Turn
    this off with `--no-fallbacks` or `use_fallbacks: false`.
  * Assistant turns are passed back exactly as returned, so thinking blocks stay valid.
  * A turn cut off at `max_tokens` is discarded, and the agent is asked to work in smaller steps.

## Safety model

* **Workspace jail:** every path is resolved and must stay inside the repository, and `.git/`
  is never writable.
* **No shell:** commands are parsed with `shlex` and run without a shell. Pipes, redirects
  and chaining are rejected.
* **Allow-listed commands only** (tests, linters, type checkers, builds, read-only git), and
  `rm`, `sudo`, `curl`, `ssh`, `git push/reset/checkout/...` are always refused. Extend the list
  with `extra_allowed_commands` in `army.yaml`.
* **Execution is off by default**: pass `--allow-exec` to let agents run tests.
* **Credentials are scrubbed** from the environment of every command an agent runs, so tests
  in an untrusted change cannot read your API keys.
* **Read-only pipelines** (`review`, `security`, `audit`) never get write tools, whatever the
  config says. `--read-only` forbids writes for any run.
* Agents never commit or push. You review the working tree and commit.

## Configuration (`army.yaml`)

```yaml
model: claude-opus-5-5
light_model: claude-sonnet-5-5  # optional: used by triage, docs, release and onboarding agents
effort: high                    # low | medium | high | xhigh | max
max_turns: 40                   # tool round-trips per agent
max_review_loops: 3
max_parallel: 4
allow_write: true
allow_exec: false
command_timeout: 300
extra_allowed_commands: ["poetry run pytest", "pnpm test"]
```

The environment variables `ARMY_MODEL`, `ARMY_LIGHT_MODEL`, `ARMY_EFFORT`, `ARMY_MAX_TURNS`
and `ARMY_ALLOW_EXEC` override the file, and CLI flags override both.

## CI/CD integration

* `.github/workflows/ci.yml` runs the test suite and dry-runs every pipeline.
* `.github/workflows/army-pr-review.yml`: label a PR `army:review` and the review squad
  reviews it, posts the after-action report as a PR comment, and fails the check if the gate
  blocks. It needs the `ANTHROPIC_API_KEY` repository secret.
* `.github/workflows/army-issue-triage.yml`: label an issue `army:triage` to get a
  triage comment.

## Extending the army

```python
from agent_army import Army, ArmyConfig
from agent_army.agent import AgentSpec
from agent_army.pipelines import Pipeline, Stage, register as register_pipeline
from agent_army.roster import RW, register as register_agent

register_agent(AgentSpec("i18n_specialist", "Internationalisation Specialist", "engineering",
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
rehearses pipelines, and the SDK integration is exercised against a mock HTTP transport.

## Roadmap

* Git worktree isolation per run and automatic branch + PR creation
* Persistent memory across runs (lessons learned, project conventions)
* Cost budgets per run, and per-agent model routing from `army.yaml`
* MCP tool servers (issue trackers, observability backends) for agents
* Web dashboard for live runs
