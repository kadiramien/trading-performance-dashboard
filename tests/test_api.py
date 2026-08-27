import pytest

from app import create_app
from database import db


@pytest.fixture()
def client():
    app = create_app("sqlite:///:memory:")
    app.config.update(TESTING=True)

    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_create_trade_and_analytics(client):
    payload = {
        "symbol": "AAPL",
        "strategy": "momentum",
        "side": "long",
        "quantity": 10,
        "entry_price": 100,
        "exit_price": 105,
        "fees": 2,
    }
    created = client.post("/api/trades", json=payload)
    assert created.status_code == 201
    assert created.get_json()["pnl"] == 48.0

    analytics = client.get("/api/analytics")
    assert analytics.status_code == 200
    assert analytics.get_json()["total_pnl"] == 48.0
