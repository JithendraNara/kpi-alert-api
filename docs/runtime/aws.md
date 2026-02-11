# AWS Runtime Pattern (`kpi-alert-api`)

## Objective
Deploy the API for low-latency KPI and alert checks with repeatable operations.

## Suggested Topology
- Container image in ECR
- API runtime on ECS Fargate (or EKS)
- ALB for traffic routing
- Config/secrets via AWS Systems Manager Parameter Store or Secrets Manager
- Observability via CloudWatch logs/alarms

## Deployment Notes
1. Build and push image from `Dockerfile`.
2. Define task with environment variable `LAKEHOUSE_EXPORT_DIR`.
3. Mount export data path (EFS) or sync from S3 before startup.
4. Expose `/health` behind ALB target-group health checks.
5. Add alarm on 5xx rate and p95 latency.

## Verification
1. `GET /health` returns `ok`.
2. `GET /v1/kpis/overview` returns latest KPI row.
3. `POST /v1/alerts/evaluate` returns severity classification.
