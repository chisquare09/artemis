from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_explain_lesson_a1_5_returns_200():
    response = client.post("/api/ai/explain-lesson", json={"unit_code": "A1.5"})
    assert response.status_code == 200


def test_explain_lesson_includes_unit_code():
    response = client.post("/api/ai/explain-lesson", json={"unit_code": "A1.5"})
    assert response.json()["unit_code"] == "A1.5"


def test_explain_lesson_includes_provider():
    response = client.post("/api/ai/explain-lesson", json={"unit_code": "A1.5"})
    assert "provider" in response.json()


def test_explain_lesson_includes_explanation():
    response = client.post("/api/ai/explain-lesson", json={"unit_code": "A1.5"})
    assert response.json()["explanation"]


def test_answer_question_returns_200():
    response = client.post("/api/ai/answer-question", json={
        "unit_code": "A1.5",
        "question": "How do I order coffee?"
    })
    assert response.status_code == 200


def test_answer_question_empty_returns_422():
    response = client.post("/api/ai/answer-question", json={
        "unit_code": "A1.5",
        "question": ""
    })
    assert response.status_code == 422


def test_unknown_unit_returns_404():
    response = client.post("/api/ai/explain-lesson", json={"unit_code": "UNKNOWN"})
    assert response.status_code == 404
    data = response.json()
    assert "error" in data
    assert data["error"]["code"] == "NOT_FOUND"


def test_answer_question_includes_retrieved_chunks_in_context():
    # Seed material first
    client.post("/api/materials", json={
        "title": "Test material",
        "source_type": "manual_text",
        "raw_text": "Il conto, per favore.",
        "unit_code": "A1.5"
    })
    response = client.post("/api/ai/answer-question", json={
        "unit_code": "A1.5",
        "question": "How do I ask for the bill?"
    })
    assert response.status_code == 200
    context = response.json()["used_context"]
    assert "retrieved_chunks" in context


def test_answer_question_works_without_materials():
    response = client.post("/api/ai/answer-question", json={
        "unit_code": "A1.5",
        "question": "What is the weather today?"
    })
    assert response.status_code == 200
    assert "answer" in response.json()


def test_explain_lesson_a2_1_returns_200():
    response = client.post("/api/ai/explain-lesson", json={"unit_code": "A2.1"})
    assert response.status_code == 200
    assert response.json()["unit_code"] == "A2.1"
