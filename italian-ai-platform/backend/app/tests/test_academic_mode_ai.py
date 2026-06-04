from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_explain_daily_includes_daily_context():
    response = client.post("/api/ai/explain-lesson", json={"unit_code": "A1.5", "study_mode": "daily_communication"})
    assert response.status_code == 200
    context = response.json()["used_context"]
    assert context["study_mode"] == "daily_communication"
    assert "practical" in context["mode_guidance"].lower() or "conversation" in context["mode_guidance"].lower()


def test_explain_academic_includes_academic_context():
    response = client.post("/api/ai/explain-lesson", json={"unit_code": "A1.5", "study_mode": "academic_purpose"})
    assert response.status_code == 200
    context = response.json()["used_context"]
    assert context["study_mode"] == "academic_purpose"
    assert "grammar" in context["mode_guidance"].lower() or "exam" in context["mode_guidance"].lower()


def test_answer_question_includes_study_mode():
    response = client.post("/api/ai/answer-question", json={
        "unit_code": "A1.5",
        "question": "How do I order coffee?",
        "study_mode": "academic_purpose"
    })
    assert response.status_code == 200
    context = response.json()["used_context"]
    assert context["study_mode"] == "academic_purpose"


def test_explain_defaults_to_daily():
    response = client.post("/api/ai/explain-lesson", json={"unit_code": "A1.5"})
    assert response.status_code == 200
    context = response.json()["used_context"]
    assert context["study_mode"] == "daily_communication"
