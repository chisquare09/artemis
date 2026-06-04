import base64
import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def make_mock_jwt(payload: dict) -> str:
    header = base64.urlsafe_b64encode(json.dumps({"alg": "HS256", "typ": "JWT"}).encode()).rstrip(b"=").decode()
    body = base64.urlsafe_b64encode(json.dumps(payload).encode()).rstrip(b"=").decode()
    return f"{header}.{body}.mock_sig"


def test_auth_me_returns_dev_user_in_development_without_token():
    """GET /api/auth/me returns dev-user in development without token."""
    response = client.get("/api/auth/me")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "dev-user"
    assert data["auth_mode"] == "development"


def test_auth_me_returns_user_id_with_token():
    """GET /api/auth/me returns mocked user ID with token."""
    token = make_mock_jwt({"sub": "supabase-user-456"})
    response = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "supabase-user-456"
    assert data["auth_mode"] == "supabase"
