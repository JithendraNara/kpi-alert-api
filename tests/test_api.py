from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.fixture()
def sample_exports(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    export_dir = tmp_path / "exports"
    export_dir.mkdir(parents=True, exist_ok=True)

    pd.DataFrame(
        [
            {
                "metric_date": "2026-02-10",
                "new_users": 120,
                "active_users": 620,
                "paid_conversions": 14,
                "gross_revenue_usd": 5400.0,
                "refunded_usd": 220.0,
                "net_revenue_usd": 5180.0,
                "tickets_opened": 19,
                "conversion_rate": 0.1167,
                "refund_rate": 0.0407,
            }
        ]
    ).to_csv(export_dir / "daily_kpis.csv", index=False)

    pd.DataFrame(
        [
            {
                "experiment_name": "new_onboarding",
                "experiment_variant": "A",
                "users_exposed": 100,
                "users_converted": 12,
                "conversion_rate": 0.12,
                "avg_revenue_per_user": 61.2,
            }
        ]
    ).to_csv(export_dir / "experiment_performance.csv", index=False)

    monkeypatch.setenv("LAKEHOUSE_EXPORT_DIR", str(export_dir))
    return export_dir


def test_health() -> None:
    res = client.get("/health")
    assert res.status_code == 200
    payload = res.json()
    assert payload["status"] == "ok"


def test_kpi_overview_shape(sample_exports: Path) -> None:
    res = client.get("/v1/kpis/overview")
    assert res.status_code == 200
    payload = res.json()
    for key in [
        "metric_date",
        "new_users",
        "active_users",
        "paid_conversions",
        "conversion_rate",
        "net_revenue_usd",
        "tickets_opened",
    ]:
        assert key in payload


def test_experiments_endpoint(sample_exports: Path) -> None:
    res = client.get("/v1/experiments")
    assert res.status_code == 200
    body = res.json()
    assert body["count"] == 1
    assert body["items"][0]["experiment_name"] == "new_onboarding"


def test_alert_evaluate_endpoint(sample_exports: Path) -> None:
    res = client.post(
        "/v1/alerts/evaluate",
        json={
            "min_conversion_rate": 0.15,
            "max_refund_rate": 0.10,
            "min_net_revenue_usd": 6000.0,
        },
    )
    assert res.status_code == 200
    body = res.json()
    assert body["severity"] in {"warning", "critical"}
    assert len(body["alerts"]) >= 1
