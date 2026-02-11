# Proof Map

| Claim | Evidence | Metric |
|---|---|---|
| Built analytics APIs consumed by frontend and AI assistants. | `app/api/routes.py` | 4 endpoints exposed (`/health`, `/v1/kpis/overview`, `/v1/experiments`, `/v1/alerts/evaluate`) |
| Implemented threshold-based alerting over KPI outputs. | `app/services/alert_service.py` | Severity classification (`ok/warning/critical`) from configurable rules |
| Added backend test coverage for core API paths. | `tests/test_api.py` | Health + KPI overview test cases |
