from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generate_a1_5_returns_200():
    response = client.post("/api/exercises/generate", json={"unit_code": "A1.5", "activity_type": "quiz", "count": 5})
    assert response.status_code == 200


def test_submit_correct_returns_high_score():
    gen = client.post("/api/exercises/generate", json={"unit_code": "A1.5", "activity_type": "quiz", "count": 5})
    data = gen.json()
    answers = [
        {"item_id": f"{data['exercise_id']}-0", "answer": "Vorrei un caffè."},
        {"item_id": f"{data['exercise_id']}-1", "answer": "Quanto"},
        {"item_id": f"{data['exercise_id']}-2", "answer": "Non mi piace il tè."},
        {"item_id": f"{data['exercise_id']}-3", "answer": "Il conto, per favore."},
        {"item_id": f"{data['exercise_id']}-4", "answer": "una"},
    ]
    submit = client.post("/api/exercises/submit", json={"exercise_id": data["exercise_id"], "answers": answers})
    assert submit.status_code == 200
    assert submit.json()["score"] == 100


def test_submit_incorrect_returns_weak_points():
    gen = client.post("/api/exercises/generate", json={"unit_code": "A1.5", "activity_type": "quiz", "count": 5})
    data = gen.json()
    answers = [{"item_id": f"{data['exercise_id']}-{i}", "answer": "wrong"} for i in range(5)]
    submit = client.post("/api/exercises/submit", json={"exercise_id": data["exercise_id"], "answers": answers})
    assert submit.status_code == 200
    assert len(submit.json()["weak_points"]) > 0


def test_unknown_unit_returns_404():
    response = client.post("/api/exercises/generate", json={"unit_code": "UNKNOWN", "activity_type": "quiz", "count": 5})
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "NOT_FOUND"


def test_unknown_exercise_id_returns_404():
    response = client.post("/api/exercises/submit", json={"exercise_id": "fake-id", "answers": []})
    assert response.status_code == 404
