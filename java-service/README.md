# Java Service Mirror (`kpi-alert-api`)

This module is a minimal Spring Boot reference implementation that mirrors one KPI endpoint from the Python FastAPI service.

## Endpoints
- `GET /health`
- `GET /v1/kpis/overview`

## Run (local)
```bash
cd java-service
./mvnw spring-boot:run
```

If you do not have Maven Wrapper generated yet, run with system Maven:
```bash
mvn spring-boot:run
```

Default port is `8081`.
