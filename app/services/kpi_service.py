from __future__ import annotations

from pathlib import Path

import pandas as pd


def _read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"missing export file: {path}")
    return pd.read_csv(path)


def get_latest_kpi(export_dir: Path) -> dict[str, object]:
    daily = _read_csv(export_dir / "daily_kpis.csv")
    if daily.empty:
        raise ValueError("daily_kpis.csv is empty")

    latest = daily.sort_values("metric_date").iloc[-1].to_dict()
    return {
        "metric_date": str(latest["metric_date"]),
        "new_users": int(latest["new_users"]),
        "active_users": int(latest["active_users"]),
        "paid_conversions": int(latest["paid_conversions"]),
        "conversion_rate": float(latest["conversion_rate"]),
        "net_revenue_usd": float(latest["net_revenue_usd"]),
        "tickets_opened": int(latest["tickets_opened"]),
    }


def get_experiment_summary(export_dir: Path) -> list[dict[str, object]]:
    exp = _read_csv(export_dir / "experiment_performance.csv")
    if exp.empty:
        return []
    return exp.to_dict(orient="records")
