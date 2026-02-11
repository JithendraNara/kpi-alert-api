from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    res = client.get("/health")
    assert res.status_code == 200
    payload = res.json()
    assert payload["status"] == "ok"


def test_kpi_overview_shape() -> None:
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
