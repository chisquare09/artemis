from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_listening_task_returns_200():
    response = client.get("/api/listening/units/A1.5")
    assert response.status_code == 200


def test_response_includes_unit_code():
    response = client.get("/api/listening/units/A1.5")
    assert response.json()["unit_code"] == "A1.5"


def test_response_includes_transcript():
    response = client.get("/api/listening/units/A1.5")
    assert "Buongiorno" in response.json()["transcript"]


def test_response_includes_3_questions():
    response = client.get("/api/listening/units/A1.5")
    assert len(response.json()["questions"]) == 3


def test_response_does_not_expose_correct_answers():
    response = client.get("/api/listening/units/A1.5")
    for q in response.json()["questions"]:
        assert "correct_answer" not in q
        assert "correct_keywords" not in q


def test_submit_correct_returns_100():
    response = client.post("/api/listening/submit", json={
        "unit_code": "A1.5",
        "answers": [
            {"question_id": "a15-listen-1", "answer": "cappuccino and cornetto"},
            {"question_id": "a15-listen-2", "answer": "tre euro"},
            {"question_id": "a15-listen-3", "answer": "per favore"},
        ]
    })
    assert response.status_code == 200
    assert response.json()["score"] == 100


def test_submit_incorrect_price_has_weak_point():
    response = client.post("/api/listening/submit", json={
        "unit_code": "A1.5",
        "answers": [
            {"question_id": "a15-listen-1", "answer": "cappuccino and cornetto"},
            {"question_id": "a15-listen-2", "answer": "wrong"},
            {"question_id": "a15-listen-3", "answer": "per favore"},
        ]
    })
    assert response.status_code == 200
    assert "listening_prices" in response.json()["weak_points"]


def test_unknown_unit_returns_404():
    response = client.get("/api/listening/units/UNKNOWN")
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "NOT_FOUND"
