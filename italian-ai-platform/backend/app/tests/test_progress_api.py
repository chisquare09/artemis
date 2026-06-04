from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_overview_returns_user_id():
    response = client.get("/api/progress/overview")
    assert response.status_code == 200
    assert response.json()["user_id"] == "dev-user"


def test_unit_progress_a1_5():
    response = client.get("/api/progress/units/A1.5")
    assert response.status_code == 200
    assert response.json()["unit_code"] == "A1.5"


def test_complete_activity_updates_progress():
    response = client.post("/api/progress/activities/complete", json={
        "unit_code": "A1.5",
        "activity_type": "vocabulary",
        "skill": "reading",
        "score": 90
    })
    assert response.status_code == 200
    assert response.json()["unit_progress"]["completed_activities"] >= 1


def test_exercise_result_updates_weak_points():
    response = client.post("/api/progress/exercise-result", json={
        "unit_code": "A1.5",
        "exercise_id": "test-123",
        "score": 70,
        "weak_points": ["piacere", "negation"],
        "skill_focus": "reading"
    })
    assert response.status_code == 200
    assert "piacere" in response.json()["unit_progress"]["weak_points"]


def test_exercise_result_creates_review_items():
    response = client.post("/api/progress/exercise-result", json={
        "unit_code": "A1.5",
        "exercise_id": "test-456",
        "score": 50,
        "weak_points": ["articles"],
        "skill_focus": "writing"
    })
    assert response.status_code == 200
    assert response.json()["review_items_created"] >= 0


def test_unknown_unit_returns_404():
    response = client.get("/api/progress/units/UNKNOWN")
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "NOT_FOUND"
