# Example orders

```bash
# Idea -> shipped change, with requirements, design, plan, code, review squad, QA, docs, changelog
army run feature "Users can export their dashboard as CSV" --allow-exec

# Bug -> root cause -> fix + regression test -> verified
army run bugfix @issue-142.md --allow-exec

# Read-only PR review squad (exit code 2 when the gate blocks)
army run review "Diff against origin/main" --allow-exec

# Security sweep, whole-repo health audit, docs refresh
army run security
army run audit "We are preparing for a SOC 2 review"
army run docs

# Production incident from a pasted stack trace
pbpaste | army run incident - --allow-exec

# Let the commander pick specialists dynamically
army mission "Migrate the settings module from JSON files to SQLite, with a data migration"

# One specialist, one task
army deploy threat_modeler "Model the threats of the public upload API"
army deploy onboarding_guide "Write a tour for a new backend engineer"
```

## Office work

```bash
# Finance & accounting (put bank statements, ledger exports and budgets in the workspace as CSV)
army run month_end "October 2026 close for the UK entity"
army deploy cash_flow_forecaster "13-week cash forecast from ar.csv, ap.csv and payroll.csv"

# Legal & compliance
army deploy contract_reviewer @vendor-msa.md
army run policy "Update the remote work policy to cover working abroad for up to 4 weeks"
army deploy soc2_readiness_specialist "Map our policies/ folder to the SOC 2 criteria"

# People & recruiting
army run hiring "Senior support engineer, Berlin, hybrid, reports to the Head of Support"
army run employee_onboarding "Priya, data analyst, starts Monday in the finance team"

# Marketing, sales & support
army run campaign "Spring launch of the mobile app for small retailers" --allow-web
army run rfp @city-rfp-2026.md
army run support_insights "Tickets export for Q3 is in tickets_q3.csv"

# Leadership
army run board_report "Q3 2026 board meeting"
army run research_report "How are mid-size logistics firms using AI for route planning?" --allow-web

# Everyday admin
army run meeting_followup @standup-transcript.txt
army deploy inbox_triager @inbox-export.md

# Not sure who to ask? Let the commander decide.
army mission "We are opening an office in Lisbon: plan hiring, IT setup, lease review and an announcement"
```
