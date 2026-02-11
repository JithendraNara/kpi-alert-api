from __future__ import annotations

from app.models.schemas import AlertRule


def evaluate_alerts(kpi: dict[str, object], rule: AlertRule) -> tuple[str, list[str]]:
    alerts: list[str] = []

    if float(kpi["conversion_rate"]) < rule.min_conversion_rate:
        alerts.append(
            f"Conversion rate below threshold: {kpi['conversion_rate']:.4f} < {rule.min_conversion_rate:.4f}"
        )

    # `refund_rate` is not in KPIOverviewResponse but available in source mart row.
    refund_rate = float(kpi.get("refund_rate", 0.0))
    if refund_rate > rule.max_refund_rate:
        alerts.append(
            f"Refund rate above threshold: {refund_rate:.4f} > {rule.max_refund_rate:.4f}"
        )

    if float(kpi["net_revenue_usd"]) < rule.min_net_revenue_usd:
        alerts.append(
            f"Net revenue below threshold: {kpi['net_revenue_usd']:.2f} < {rule.min_net_revenue_usd:.2f}"
        )

    severity = "critical" if len(alerts) >= 2 else ("warning" if alerts else "ok")
    return severity, alerts
