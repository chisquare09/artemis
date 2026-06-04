from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_curriculum():
    response = client.get("/api/curriculum")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Full Italian Curriculum A1 to B2"


def test_get_levels_returns_a1():
    response = client.get("/api/levels")
    assert response.status_code == 200
    codes = [l["code"] for l in response.json()]
    assert "A1" in codes


def test_get_level_a1():
    response = client.get("/api/levels/A1")
    assert response.status_code == 200
    assert response.json()["code"] == "A1"


def test_get_level_units():
    response = client.get("/api/levels/A1/units")
    assert response.status_code == 200
    codes = [u["code"] for u in response.json()]
    for i in range(1, 11):
        assert f"A1.{i}" in codes


def test_get_unit_a1_5():
    response = client.get("/api/units/A1.5")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Food, Café, and Restaurant"


def test_get_unit_a1_5_has_objectives():
    response = client.get("/api/units/A1.5")
    data = response.json()
    assert "communicative_goal" in data["objectives"]
    assert "grammar" in data["objectives"]


def test_get_unknown_unit_returns_404():
    response = client.get("/api/units/UNKNOWN")
    assert response.status_code == 404
    data = response.json()
    assert "error" in data
    assert "code" in data["error"]
    assert "message" in data["error"]
