# Proof Map

| ID | Claim | Evidence | Metric |
|---|---|---|---|
| S1 | Built analytics APIs consumed by frontend and AI assistants. | `app/api/routes.py` | 4 endpoints exposed (`/health`, `/v1/kpis/overview`, `/v1/experiments`, `/v1/alerts/evaluate`) |
| S2 | Implemented threshold-based alerting over KPI outputs. | `app/services/alert_service.py` | Severity classification (`ok/warning/critical`) from configurable rules |
| S3 | Added backend test coverage for core API paths. | `tests/test_api.py` | Health, KPI, experiments, and alerts test cases |
| S4 | Added container and Kubernetes runtime artifacts for production-style deployment. | `Dockerfile`, `docker-compose.yml`, `k8s/*.yaml` | Docker/Compose/K8s deployment paths versioned and health-probed |
| S5 | Added JVM-based service parity and cloud runtime guides for platform breadth. | `java-service/*`, `docs/runtime/*.md` | Spring Boot mirror endpoint plus AWS/Azure runtime patterns documented |
