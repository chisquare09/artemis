from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "italian-ai-platform-api"}


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "service" in data
    assert "environment" in data
