from __future__ import annotations

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str
    service: str


class KPIOverviewResponse(BaseModel):
    metric_date: str
    new_users: int
    active_users: int
    paid_conversions: int
    conversion_rate: float
    net_revenue_usd: float
    tickets_opened: int


class AlertRule(BaseModel):
    min_conversion_rate: float = Field(default=0.03, ge=0, le=1)
    max_refund_rate: float = Field(default=0.12, ge=0, le=1)
    min_net_revenue_usd: float = Field(default=3000, ge=0)


class AlertResult(BaseModel):
    metric_date: str
    severity: str
    alerts: list[str]
