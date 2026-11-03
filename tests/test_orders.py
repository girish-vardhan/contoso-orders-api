from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app, raise_server_exceptions=False)


def test_health():
    assert client.get("/health").json() == {"status": "healthy"}


def test_existing_order():
    response = client.get("/orders/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "customer": "Demo Customer"}
