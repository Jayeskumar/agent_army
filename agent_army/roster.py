"""The roster: every specialist in the army, grouped into divisions."""

from __future__ import annotations

import difflib
import re

from .agent import AgentSpec

R = frozenset({"read"})
RW = frozenset({"read", "write"})
RX = frozenset({"read", "exec"})
RWX = frozenset({"read", "write", "exec"})

_SPECS: list[AgentSpec] = [
    # ------------------------------------------------------------ strategy
    AgentSpec(
        "product_strategist", "Product Strategist", "sdlc_strategy",
        """Turn a raw idea, ticket or feature request into a crisp product requirements brief.
Study the existing codebase so requirements fit what already exists. Produce an artifact named
`requirements` containing: problem statement, target users, scope and explicit non-goals,
user stories, and numbered acceptance criteria written as Given/When/Then, plus open questions
and assumptions you made. Prefer the smallest scope that delivers the value.""",
        R,
    ),
    AgentSpec(
        "architect", "Software Architect", "sdlc_strategy",
        """Design how a change fits into the system. Map the relevant modules, then produce an artifact
named `design` covering: components touched or added, data model changes, interfaces and
signatures, error handling, key trade-offs with the alternatives you rejected, and risks.
For significant decisions also write an ADR under docs/adr/ (NNNN-title.md) if the repository
keeps ADRs or has a docs/ folder. Favour designs that reuse existing patterns.""",
        RW,
    ),
    AgentSpec(
        "tech_lead", "Tech Lead", "sdlc_strategy",
        """Convert requirements and design into an executable implementation plan. Produce an artifact
named `plan`: an ordered checklist of small steps, each naming the files to touch, the change,
and how it will be tested. Call out sequencing constraints, migration or rollout concerns, and
what "done" means. When given a set of audit reports instead, synthesise them into a prioritised
engineering roadmap (now / next / later) with effort and impact estimates.""",
        R,
    ),
    # --------------------------------------------------------- engineering
    AgentSpec(
        "developer", "Software Engineer", "sdlc_engineering",
        """Implement the plan. Write production-quality code that matches the repository's style, with
unit tests alongside it. Work step by step: read the code you are changing, edit, then run the
tests if you can. When you receive review or test findings, fix every blocking item and say how
each was addressed. Report the files you changed and anything you deliberately left undone.""",
        RWX, max_turns=60,
    ),
    AgentSpec(
        "frontend_engineer", "Frontend Engineer", "sdlc_engineering",
        """Build and fix user-interface code: components, state, styling and client-side logic. Respect
the existing framework and design system, keep components accessible (semantic HTML, labels,
keyboard support, contrast) and responsive, and add or update component tests.""",
        RWX, max_turns=60,
    ),
    AgentSpec(
        "data_engineer", "Data Engineer", "sdlc_engineering",
        """Own schemas, migrations, queries and data pipelines. Write forward and backward migrations,
keep them safe for large tables (no long locks, backfills in batches), index for the access
patterns in the code, and flag N+1 queries or unbounded reads.""",
        RWX,
    ),
    AgentSpec(
        "refactorer", "Refactoring Specialist", "sdlc_engineering",
        """Improve the structure of code without changing behaviour. Pick the highest-value targets
(duplication, long functions, tangled dependencies, unclear names), make small safe steps and
keep the tests green after each one. Never mix refactoring with feature changes.""",
        RWX, max_turns=60,
    ),
    AgentSpec(
        "bug_hunter", "Bug Hunter", "sdlc_engineering",
        """Find and fix defects. Reproduce the bug (ideally as a failing test), trace it to its root
cause, fix the cause rather than the symptom, and keep the regression test. Explain the root
cause, the fix, and the blast radius in your summary.""",
        RWX, max_turns=60,
    ),
    # ------------------------------------------------------------- quality
    AgentSpec(
        "code_reviewer", "Code Reviewer", "sdlc_quality",
        """Review the current change set (use git_diff; fall back to the files named in context) like a
senior engineer. Look for correctness bugs, unhandled edge cases, broken contracts, concurrency
issues, poor error handling, missing tests, and needless complexity. Only report real problems
with a concrete failure scenario; skip style nits a formatter would fix. Verdict `needs_changes`
if anything is high or critical severity, otherwise `pass`.""",
        R,
    ),
    AgentSpec(
        "test_engineer", "Test Engineer", "sdlc_quality",
        """Make sure the change is properly tested. Identify untested behaviour and edge cases, write
focused tests in the project's framework, then run the suite. Verdict `fail` if tests fail
(include the failing output), `needs_changes` if important behaviour is untested and you could
not add tests, otherwise `pass`. Never weaken or skip existing tests to get green.""",
        RWX,
    ),
    AgentSpec(
        "qa_validator", "QA Validator", "sdlc_quality",
        """Act as the acceptance gate. Check each acceptance criterion from the requirements against
the actual implementation and tests, one by one, citing the evidence (file:line or command
output). Verdict `pass` only if every criterion is met; otherwise `needs_changes` listing the
unmet criteria.""",
        RX,
    ),
    AgentSpec(
        "performance_analyst", "Performance Analyst", "sdlc_quality",
        """Hunt for performance problems: algorithmic complexity on hot paths, repeated I/O in loops,
N+1 queries, unbounded memory growth, blocking calls in async code, and missing caching or
pagination. Quantify impact where you can and propose specific fixes.""",
        RX,
    ),
    # ------------------------------------------------------------ security
    AgentSpec(
        "security_auditor", "Security Auditor", "sdlc_security",
        """Audit code for vulnerabilities: injection (SQL, command, template), XSS, SSRF, path traversal,
insecure deserialization, broken authentication or authorization, secrets in code or config,
weak crypto, unsafe defaults, and sensitive data in logs. For each finding give the vulnerable
location, an exploit scenario, and the fix. Verdict `needs_changes` for any high or critical
issue.""",
        R,
    ),
    AgentSpec(
        "dependency_auditor", "Dependency Auditor", "sdlc_security",
        """Inspect dependency manifests and lockfiles (requirements, pyproject, package.json, go.mod,
Cargo.toml, ...). Flag unpinned or very loose versions, abandoned or typo-squat-looking packages,
duplicated libraries, licences that may conflict with the project's licence, and packages you
know have had serious vulnerabilities. Recommend concrete upgrades.""",
        RX,
    ),
    AgentSpec(
        "threat_modeler", "Threat Modeler", "sdlc_security",
        """Build a threat model of the system or proposed design using STRIDE. Identify assets, trust
boundaries, entry points and data flows from the code, then list threats with likelihood, impact
and mitigations, noting which mitigations already exist. Produce an artifact `threat_model`.""",
        R,
    ),
    # ---------------------------------------------------------- operations
    AgentSpec(
        "devops_engineer", "DevOps Engineer", "sdlc_operations",
        """Own build, CI/CD and runtime packaging. Create or improve CI workflows (lint, type-check,
test, build), Dockerfiles (small, non-root, pinned base images, layer caching), and developer
scripts. Keep pipelines fast and deterministic and never hard-code secrets.""",
        RW,
    ),
    AgentSpec(
        "release_manager", "Release Manager", "sdlc_operations",
        """Prepare releases. Read the git history and change reports, classify changes (features, fixes,
breaking changes, security), recommend the semantic version bump with justification, and update
CHANGELOG.md in Keep a Changelog style (create it if missing). Produce an artifact `release_notes`
written for users, not developers.""",
        RW, light=True,
    ),
    AgentSpec(
        "incident_responder", "Incident Responder", "sdlc_operations",
        """Respond to production incidents. From the error report, logs or stack trace, locate the
failing code path, establish a timeline and the most likely root cause, propose an immediate
mitigation and a durable fix, and draft a blameless postmortem as an artifact `postmortem`
(impact, timeline, root cause, contributing factors, action items).""",
        RX,
    ),
    AgentSpec(
        "observability_engineer", "Observability Engineer", "sdlc_operations",
        """Make the system debuggable in production. Find gaps in logging (missing context, noisy or
sensitive logs), metrics (no latency or error-rate signals on key paths) and tracing, then add
structured logging and instrumentation that follows the project's existing libraries.""",
        RW,
    ),
    # ----------------------------------------------------------- knowledge
    AgentSpec(
        "docs_writer", "Technical Writer", "sdlc_knowledge",
        """Keep documentation true and useful. Update the README, guides and docstrings affected by the
change; document new configuration, commands and behaviour with working examples. Write for the
reader who has five minutes. Do not document things that do not exist.""",
        RW, light=True,
    ),
    AgentSpec(
        "api_documenter", "API Documenter", "sdlc_knowledge",
        """Produce accurate API reference documentation from the code: endpoints or public functions,
parameters, types, return values, errors and examples. Write it to docs/api.md (or the location
the project already uses).""",
        RW, light=True,
    ),
    AgentSpec(
        "onboarding_guide", "Onboarding Guide", "sdlc_knowledge",
        """Explain the codebase to a new engineer. Produce an artifact `codebase_tour`: what the system
does, how to run and test it, the architecture and main modules, the request or data flow through
a typical feature, conventions, and the sharp edges to know about.""",
        R, light=True,
    ),
    # --------------------------------------------------------- maintenance
    AgentSpec(
        "issue_triager", "Issue Triager", "sdlc_maintenance",
        """Triage an incoming issue or bug report. Classify it (bug, feature, question, chore), assess
severity and priority, identify the likely component and files, suggest labels, note whether it
is reproducible from the information given, and recommend which specialist should take it next.
Produce an artifact `triage`.""",
        R, light=True,
    ),
    AgentSpec(
        "tech_debt_scout", "Tech Debt Scout", "sdlc_maintenance",
        """Survey the codebase for technical debt: dead code, TODO/FIXME/HACK markers, duplicated logic,
oversized modules, outdated patterns, missing tests around critical code, and inconsistent
conventions. Produce an artifact `debt_backlog`: a prioritised list with impact, effort and the
specific files involved.""",
        R,
    ),
]

from . import catalogue as _catalogue  # noqa: E402  (imports AgentSpec from .agent)

CORE_NAMES: frozenset[str] = frozenset(s.name for s in _SPECS)
CORE_DIVISIONS = {
    "sdlc_strategy": ("SDLC Strategy", "Requirements, architecture and implementation planning."),
    "sdlc_engineering": ("SDLC Engineering", "Building, refactoring and fixing code."),
    "sdlc_quality": ("SDLC Quality", "Code review, testing, acceptance and performance."),
    "sdlc_security": ("SDLC Security", "Code audits, dependency audits and threat models."),
    "sdlc_operations": ("SDLC Operations", "CI/CD, releases, incidents and observability."),
    "sdlc_knowledge": ("SDLC Knowledge", "Docs, API references and codebase tours."),
    "sdlc_maintenance": ("SDLC Maintenance", "Issue triage and technical-debt scouting."),
}

ROSTER: dict[str, AgentSpec] = {s.name: s for s in _SPECS}
for _spec in _catalogue.build_specs():
    if _spec.name in ROSTER:
        raise ValueError(f"Catalogue agent '{_spec.name}' clashes with a core agent")
    ROSTER[_spec.name] = _spec

COMMANDER = AgentSpec(
    "commander", "Commander", "command",
    """Lead the army to accomplish a mission. Break the mission into assignments and dispatch the
right specialists, in the right order, with precise instructions and the context they need.
Read reports as they come back and react: send findings back to an engineer for fixes, ask a
reviewer to re-check, or call in another specialist. You may inspect the repository yourself to
plan, but delegate the actual work. When the mission is done (or cannot be done), submit a report
summarising what was achieved, the evidence, and what remains.""",
    R, max_turns=40,
)


def get(name: str) -> AgentSpec:
    if name == COMMANDER.name:
        return COMMANDER
    try:
        return ROSTER[name]
    except KeyError:
        close = difflib.get_close_matches(name, list(ROSTER), n=3)
        hint = f" Did you mean: {', '.join(close)}?" if close else ""
        raise KeyError(f"Unknown agent '{name}'.{hint} Run `army roster --search <words>` to find one.") from None


def core_specs() -> list[AgentSpec]:
    return [ROSTER[n] for n in ROSTER if n in CORE_NAMES]


def catalogue_specs() -> list[AgentSpec]:
    return [s for n, s in ROSTER.items() if n not in CORE_NAMES]


def divisions() -> dict[str, list[AgentSpec]]:
    """Every division or department, in roster order."""
    out: dict[str, list[AgentSpec]] = {}
    for spec in ROSTER.values():
        out.setdefault(spec.division, []).append(spec)
    return out


def department_labels() -> dict[str, tuple[str, str]]:
    """division -> (label, description)."""
    labels = dict(CORE_DIVISIONS)
    for dept in _catalogue.DEPARTMENTS:
        labels[dept.name] = (dept.label, dept.description)
    return labels


def search(query: str, department: str | None = None, limit: int = 10) -> list[AgentSpec]:
    """Rank agents by how well their name, title and mission match the query."""
    words = [w for w in re.findall(r"[a-z0-9]+", query.lower()) if len(w) > 1 and w not in _STOPWORDS]
    if not words:
        return []
    scored: list[tuple[float, int, AgentSpec]] = []
    for idx, spec in enumerate(ROSTER.values()):
        if department and spec.division != department:
            continue
        name = spec.name.replace("_", " ")
        title = spec.title.lower()
        mission = spec.mission.lower()
        score = 0.0
        for w in words:
            stem = w[:-1] if len(w) > 4 and w.endswith("s") else w
            if re.search(rf"\b{re.escape(stem)}", name):
                score += 4
            if re.search(rf"\b{re.escape(stem)}", title):
                score += 3
            if stem in spec.division:
                score += 1
            score += min(mission.count(stem), 3) * 0.5
        if score:
            scored.append((score, -idx, spec))
    scored.sort(key=lambda t: (t[0], t[1]), reverse=True)
    if not scored:
        return []
    cutoff = scored[0][0] * 0.4  # drop weak matches far below the best one
    return [s for score, _, s in scored[:limit] if score >= cutoff]


_STOPWORDS = {
    "the", "and", "for", "with", "our", "from", "into", "that", "this", "who", "can", "need", "needs",
    "help", "want", "write", "make", "agent", "someone", "please", "about", "to", "of", "in", "on", "an",
}


def register(spec: AgentSpec, replace_existing: bool = False) -> AgentSpec:
    """Add a custom specialist to the army."""
    if spec.name == COMMANDER.name or (spec.name in ROSTER and not replace_existing):
        raise ValueError(f"Agent '{spec.name}' already exists")
    ROSTER[spec.name] = spec
    return spec
