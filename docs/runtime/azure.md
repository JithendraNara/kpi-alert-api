# Azure Runtime Pattern (`kpi-alert-api`)

## Objective
Run the backend API on Azure with production-style health and scaling controls.

## Suggested Topology
- Container image in Azure Container Registry
- API runtime on Azure Container Apps or AKS
- Azure Application Gateway / Front Door for ingress
- Secrets in Azure Key Vault
- Monitoring with Azure Monitor + Log Analytics

## Deployment Notes
1. Build image and push to ACR.
2. Configure runtime with `LAKEHOUSE_EXPORT_DIR`.
3. Mount Azure Files volume or stage exports from Blob/ADLS.
4. Route readiness checks to `/health`.
5. Configure autoscaling on request rate and CPU.

## Verification
1. Validate `/health` from ingress endpoint.
2. Confirm KPI and experiments endpoints return expected schema.
3. Execute alert-evaluation request and verify severity output.
