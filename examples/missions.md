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
