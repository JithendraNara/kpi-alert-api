# kpi-alert-api

Backend service exposing analytics and operational APIs for `product-analytics-dashboard` and `analytics-copilot-rag`.

## What This Demonstrates
- Service-layer API design over analytics marts.
- Health/KPI/experiment endpoints plus rule-based alert evaluation.
- Testable backend contracts for frontend and AI integration.

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
- Pydantic models for request/response contracts
- Pandas-backed reads from `lakehouse-analytics-platform/data/exports`

## Architecture
- `app/api/routes.py`: endpoint layer and input validation.
- `app/services/`: KPI query and alert evaluation logic.
- `app/models/schemas.py`: typed request/response schemas.
- `app/core/settings.py`: configuration and export-path resolution.

## Repository Layout
```text
app/api/                # Endpoint layer
app/services/           # Business logic
app/models/             # Pydantic schemas
tests/                  # API tests
scripts/                # Local run scripts
```

## Quick Start
```bash
python3 -m venv --clear .venv
source .venv/bin/activate
pip install -r requirements.txt pytest
pytest -q
./scripts/run_local.sh
```

Set `LAKEHOUSE_EXPORT_DIR` if your lakehouse exports are in a different path.

## Example Request
```bash
curl -X POST http://localhost:8080/v1/alerts/evaluate \\
  -H 'Content-Type: application/json' \\
  -d '{\"min_conversion_rate\":0.03,\"max_refund_rate\":0.12,\"min_net_revenue_usd\":3000}'
```

## CI
GitHub Actions runs tests on push/PR:
- `.github/workflows/ci.yml`

## Development Trail
- Roadmap: `ROADMAP.md`
- Changelog: `CHANGELOG.md`
- Proof mapping: `PROOF.md`
- Resume bullets: `RESUME_BULLETS.md`

## Stack Coverage Extension
- Planned gap-coverage work is tracked in `STACK_COVERAGE_PLAN.md`.

## Container Runtime
```bash
# Build + run with Docker
 docker build -t kpi-alert-api:local .
 docker run -p 8080:8080 kpi-alert-api:local
```

```bash
# Compose with lakehouse exports mounted
 docker compose up --build
```

## Kubernetes
- Deployment manifest: `k8s/deployment.yaml`
- Service manifest: `k8s/service.yaml`
