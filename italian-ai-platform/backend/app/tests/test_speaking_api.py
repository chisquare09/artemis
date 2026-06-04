from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_start_roleplay_returns_200():
    response = client.post("/api/speaking/roleplay/start", json={"unit_code": "A1.5", "scenario_id": "cafe_ordering"})
    assert response.status_code == 200


def test_start_includes_session_id():
    response = client.post("/api/speaking/roleplay/start", json={"unit_code": "A1.5", "scenario_id": "cafe_ordering"})
    assert "session_id" in response.json()


def test_start_includes_first_waiter_turn():
    response = client.post("/api/speaking/roleplay/start", json={"unit_code": "A1.5", "scenario_id": "cafe_ordering"})
    assert response.json()["current_turn"]["speaker"] == "waiter"


def test_respond_accepts_message():
    start = client.post("/api/speaking/roleplay/start", json={"unit_code": "A1.5", "scenario_id": "cafe_ordering"})
    session_id = start.json()["session_id"]
    response = client.post("/api/speaking/roleplay/respond", json={"session_id": session_id, "message": "Vorrei un cappuccino, per favore."})
    assert response.status_code == 200
    assert response.json()["accepted"] is True


def test_respond_returns_next_turn():
    start = client.post("/api/speaking/roleplay/start", json={"unit_code": "A1.5", "scenario_id": "cafe_ordering"})
    session_id = start.json()["session_id"]
    response = client.post("/api/speaking/roleplay/respond", json={"session_id": session_id, "message": "Vorrei un caffè"})
    assert response.json()["next_turn"] is not None


def test_finish_returns_score():
    start = client.post("/api/speaking/roleplay/start", json={"unit_code": "A1.5", "scenario_id": "cafe_ordering"})
    session_id = start.json()["session_id"]
    client.post("/api/speaking/roleplay/respond", json={"session_id": session_id, "message": "Vorrei un cappuccino, per favore."})
    finish = client.post("/api/speaking/roleplay/finish", json={"session_id": session_id})
    assert finish.status_code == 200
    assert finish.json()["status"] == "completed"
    assert "score" in finish.json()


def test_unknown_unit_returns_404():
    response = client.post("/api/speaking/roleplay/start", json={"unit_code": "UNKNOWN", "scenario_id": "cafe_ordering"})
    assert response.status_code == 404


def test_unknown_session_returns_404():
    response = client.post("/api/speaking/roleplay/respond", json={"session_id": "fake-session", "message": "test"})
    assert response.status_code == 404
