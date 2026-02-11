# signal-services

Backend service exposing analytics and operational APIs for `signal-web` and `signal-copilot`.

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
