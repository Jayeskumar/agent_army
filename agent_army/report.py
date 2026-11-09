"""Human-readable after-action reports."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .engine import RunResult

STATUS_ICON = {
    "completed": "✅", "passed": "✅", "done": "✅",
    "blocked": "⛔", "failed": "❌", "running": "⏳", "pending": "⏳",
}
VERDICT_ICON = {"pass": "✅", "info": "ℹ️", "needs_changes": "⚠️", "fail": "❌"}
SEVERITY_ORDER = ["critical", "high", "medium", "low", "note"]


def render_markdown(run: "RunResult") -> str:
    u = run.usage
    lines = [
        f"# After-action report: `{run.pipeline}`",
        "",
        f"**Status:** {STATUS_ICON.get(run.status, '')} {run.status}  ",
        f"**Run:** `{run.run_id}`  ",
        f"**Started:** {run.started}  **Finished:** {run.finished or '-'}  ",
        f"**Tokens:** {u.input_tokens:,} in / {u.output_tokens:,} out "
        f"(cache read {u.cache_read_tokens:,}, cache write {u.cache_write_tokens:,})",
        "",
        "## Goal",
        "",
        run.goal.strip(),
        "",
        "## Stages",
        "",
        "| Stage | Status | Agents | Fix rounds |",
        "|---|---|---|---|",
    ]
    for s in run.stages:
        agents = ", ".join(f"{VERDICT_ICON.get(r.verdict, '')} {r.agent}" for r in s.reports)
        lines.append(f"| {s.stage} | {STATUS_ICON.get(s.status, '')} {s.status} | {agents} | {s.loops} |")

    findings = [(r.agent, f) for r in run.reports for f in r.findings]
    if findings:
        findings.sort(key=lambda af: _sev_rank(af[1].get("severity")))
        lines += ["", "## Findings", "", "| Severity | Agent | Title | Location |", "|---|---|---|---|"]
        for agent, f in findings:
            title = str(f.get("title", "")).replace("|", "\\|")
            loc = str(f.get("location", "") or "").replace("|", "\\|")
            lines.append(f"| {f.get('severity', 'note')} | {agent} | {title} | {loc} |")

    if run.changed_files:
        lines += ["", "## Files changed", ""] + [f"- `{p}`" for p in run.changed_files]

    lines += ["", "## Reports", ""]
    for s in run.stages:
        for r in s.reports:
            lines += [f"### {s.stage} / {r.agent} - {VERDICT_ICON.get(r.verdict, '')} {r.verdict}", ""]
            if r.error:
                lines += [f"> Error: {r.error}", ""]
            lines += [r.summary.strip() or "_(no summary)_", ""]
            for f in r.findings:
                loc = f" `{f['location']}`" if f.get("location") else ""
                lines.append(f"- **[{f.get('severity', 'note')}] {f.get('title', '')}**{loc}: {f.get('detail', '')}")
            if r.findings:
                lines.append("")
            for name, content in r.artifacts.items():
                lines += [f"<details><summary>Artifact: {name}</summary>", "", content.strip(), "", "</details>", ""]
    return "\n".join(lines).rstrip() + "\n"


def _sev_rank(sev: object) -> int:
    try:
        return SEVERITY_ORDER.index(str(sev))
    except ValueError:
        return len(SEVERITY_ORDER)
