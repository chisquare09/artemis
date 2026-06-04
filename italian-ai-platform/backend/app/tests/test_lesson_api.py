from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_lesson_a1_5():
    response = client.get("/api/lessons/A1.5")
    assert response.status_code == 200


def test_lesson_includes_level():
    response = client.get("/api/lessons/A1.5")
    assert response.json()["level"] == "A1"


def test_lesson_includes_unit_code():
    response = client.get("/api/lessons/A1.5")
    assert response.json()["unit_code"] == "A1.5"


def test_lesson_includes_title():
    response = client.get("/api/lessons/A1.5")
    assert response.json()["title"] == "Food, Café, and Restaurant"


def test_lesson_includes_objective_groups():
    response = client.get("/api/lessons/A1.5")
    objectives = response.json()["objectives"]
    expected = ["communicative_goal", "grammar", "vocabulary", "listening", "speaking", "reading", "writing", "culture"]
    for key in expected:
        assert key in objectives, f"Missing objective group: {key}"


def test_lesson_includes_seven_activities():
    response = client.get("/api/lessons/A1.5")
    assert len(response.json()["activities"]) == 7


def test_lesson_includes_progress_placeholder():
    response = client.get("/api/lessons/A1.5")
    progress = response.json()["progress"]
    assert progress["completion_percentage"] == 0
    assert progress["status"] == "not_started"


def test_lesson_includes_ai_helper_context():
    response = client.get("/api/lessons/A1.5")
    ctx = response.json()["ai_helper_context"]
    assert ctx["unit_code"] == "A1.5"
    assert ctx["level"] == "A1"
    assert "objective_types" in ctx


def test_get_unknown_lesson_returns_404():
    response = client.get("/api/lessons/UNKNOWN")
    assert response.status_code == 404
    data = response.json()
    assert "error" in data
    assert data["error"]["code"] == "NOT_FOUND"
