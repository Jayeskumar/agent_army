# Standing orders for Agent Army (this repository)

## Project
- Agent Army: a Python package (`agent_army/`) of specialised Claude agents that automate the SDLC.
- Python 3.10+, depends only on `anthropic` and `PyYAML`.

## Commands
- Run tests: `python -m pytest -q`

## Conventions
- Keep modules small and dependency-free beyond the two above.
- Every new agent goes in `agent_army/roster.py`; every new pipeline in `agent_army/pipelines.py`,
  and both need a test in `tests/`.
- Tests must never call the real API: use `ScriptedBackend` or `DryRunBackend`.
