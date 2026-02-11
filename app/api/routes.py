from __future__ import annotations

from pathlib import Path

import pandas as pd
from fastapi import APIRouter, HTTPException

from app.core.settings import get_export_dir
from app.models.schemas import AlertResult, AlertRule, HealthResponse, KPIOverviewResponse
from app.services.alert_service import evaluate_alerts
from app.services.kpi_service import get_experiment_summary, get_latest_kpi

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="kpi-alert-api")


@router.get("/v1/kpis/overview", response_model=KPIOverviewResponse)
def kpi_overview() -> KPIOverviewResponse:
    export_dir = get_export_dir()
    try:
        latest = get_latest_kpi(export_dir)
        return KPIOverviewResponse(**latest)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.get("/v1/experiments")
def experiments() -> dict[str, object]:
    export_dir = get_export_dir()
    try:
        rows = get_experiment_summary(export_dir)
        return {"count": len(rows), "items": rows}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.post("/v1/alerts/evaluate", response_model=AlertResult)
def evaluate(rule: AlertRule) -> AlertResult:
    export_dir = get_export_dir()
    daily_path = Path(export_dir) / "daily_kpis.csv"
    if not daily_path.exists():
        raise HTTPException(status_code=500, detail=f"missing export file: {daily_path}")

    daily = pd.read_csv(daily_path)
    if daily.empty:
        raise HTTPException(status_code=500, detail="daily_kpis.csv is empty")

    latest = daily.sort_values("metric_date").iloc[-1].to_dict()
    severity, alerts = evaluate_alerts(latest, rule)
    return AlertResult(metric_date=str(latest["metric_date"]), severity=severity, alerts=alerts)
