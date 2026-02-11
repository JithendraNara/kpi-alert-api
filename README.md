# signal-services

Backend service exposing analytics and operational APIs for `signal-web` and `signal-copilot`.

## Role Positioning
- Primary fit: Software Engineer, Backend Engineer, Full-Stack Engineer
- Showcase focus: API design, service layering, alerting logic, test coverage
- Resume mapping: see `PROOF.md` and `RESUME_BULLETS.md`

## Endpoints
- `GET /health`
- `GET /v1/kpis/overview`
- `GET /v1/experiments`
- `POST /v1/alerts/evaluate`

## Stack
- Python FastAPI
- Pandas-backed reads from `signal-lakehouse/data/exports`

## Quick Start
```bash
python3 -m venv --clear .venv
source .venv/bin/activate
pip install -r requirements.txt pytest
pytest -q
./scripts/run_local.sh
```

Set `LAKEHOUSE_EXPORT_DIR` if your lakehouse exports are in a different path.

## Development Trail
- Roadmap: `ROADMAP.md`
- Changelog: `CHANGELOG.md`
- Proof mapping: `PROOF.md`
- Resume bullets: `RESUME_BULLETS.md`
