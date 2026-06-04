from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_lesson_defaults_to_daily_communication():
    response = client.get("/api/lessons/A1.5")
    assert response.status_code == 200
    assert response.json()["study_mode"] == "daily_communication"


def test_daily_mode_returns_daily_metadata():
    response = client.get("/api/lessons/A1.5?study_mode=daily_communication")
    assert response.status_code == 200
    data = response.json()
    assert data["mode_label"] == "Daily Communication"
    assert "practical" in data["mode_focus"].lower() or "conversation" in data["mode_focus"].lower()


def test_academic_mode_returns_academic_metadata():
    response = client.get("/api/lessons/A1.5?study_mode=academic_purpose")
    assert response.status_code == 200
    data = response.json()
    assert data["mode_label"] == "Academic Purpose"
    assert "grammar" in data["mode_focus"].lower() or "exam" in data["mode_focus"].lower()


def test_invalid_mode_defaults_to_daily():
    response = client.get("/api/lessons/A1.5?study_mode=invalid_mode")
    assert response.status_code == 200
    assert response.json()["study_mode"] == "daily_communication"


def test_academic_mode_includes_objectives():
    response = client.get("/api/lessons/A1.5?study_mode=academic_purpose")
    assert response.status_code == 200
    data = response.json()
    assert "objectives" in data
    assert len(data["objectives"]) > 0


def test_academic_mode_includes_activities():
    response = client.get("/api/lessons/A1.5?study_mode=academic_purpose")
    assert response.status_code == 200
    data = response.json()
    assert "activities" in data
    assert len(data["activities"]) > 0
