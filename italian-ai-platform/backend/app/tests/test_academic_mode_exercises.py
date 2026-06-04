from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_exercise_defaults_to_daily():
    response = client.post("/api/exercises/generate", json={"unit_code": "A1.5", "count": 3})
    assert response.status_code == 200
    assert response.json()["study_mode"] == "daily_communication"


def test_daily_exercise_has_practical_title():
    response = client.post("/api/exercises/generate", json={"unit_code": "A1.5", "count": 3, "study_mode": "daily_communication"})
    assert response.status_code == 200
    title = response.json()["title"]
    assert "Grammar and Vocabulary" in title


def test_academic_exercise_has_academic_title():
    response = client.post("/api/exercises/generate", json={"unit_code": "A1.5", "count": 3, "study_mode": "academic_purpose"})
    assert response.status_code == 200
    title = response.json()["title"]
    assert "Academic" in title


def test_academic_has_different_instructions():
    daily = client.post("/api/exercises/generate", json={"unit_code": "A1.5", "count": 3, "study_mode": "daily_communication"})
    academic = client.post("/api/exercises/generate", json={"unit_code": "A1.5", "count": 3, "study_mode": "academic_purpose"})
    assert daily.json()["instructions"] != academic.json()["instructions"]


def test_academic_items_differ():
    daily = client.post("/api/exercises/generate", json={"unit_code": "A1.5", "count": 3, "study_mode": "daily_communication"})
    academic = client.post("/api/exercises/generate", json={"unit_code": "A1.5", "count": 3, "study_mode": "academic_purpose"})
    daily_prompts = [i["prompt"] for i in daily.json()["items"]]
    academic_prompts = [i["prompt"] for i in academic.json()["items"]]
    assert daily_prompts != academic_prompts


def test_exercise_hides_correct_answer():
    response = client.post("/api/exercises/generate", json={"unit_code": "A1.5", "count": 3, "study_mode": "academic_purpose"})
    for item in response.json()["items"]:
        assert "correct_answer" not in item
