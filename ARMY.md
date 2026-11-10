# Standing orders for Agent Army (this repository)

## Project
- Agent Army: a Python package (`agent_army/`) of specialised Claude agents that automate the SDLC.
- Python 3.10+, depends only on `anthropic` and `PyYAML`.

## Commands
- Run tests: `python -m pytest -q`

## Conventions
- Keep modules small and dependency-free beyond the two above.
- Core SDLC agents live in `agent_army/roster.py`; office agents are one line each in the
  department files under `agent_army/catalogue/`. After changing the roster, regenerate
  `CATALOGUE.md` with `python -m agent_army.catalogue > CATALOGUE.md`.
- New pipelines go in `agent_army/pipelines.py`; every pipeline is dry-run by the tests.
- Tests must never call the real API: use `ScriptedBackend` or `DryRunBackend`.
