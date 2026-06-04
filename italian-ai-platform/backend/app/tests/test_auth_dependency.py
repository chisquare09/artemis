import base64
import json
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def make_mock_jwt(payload: dict) -> str:
    """Create a mock JWT with given payload (no signature verification)."""
    header = base64.urlsafe_b64encode(json.dumps({"alg": "HS256", "typ": "JWT"}).encode()).rstrip(b"=").decode()
    body = base64.urlsafe_b64encode(json.dumps(payload).encode()).rstrip(b"=").decode()
    signature = "mock_signature"
    return f"{header}.{body}.{signature}"


def test_dev_fallback_without_authorization_header():
    """In development, no Authorization header returns dev-user."""
    response = client.get("/api/auth/me")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "dev-user"
    assert data["auth_mode"] == "development"


def test_with_mock_authorization_token_extracts_user_id():
    """With a mock JWT, extracts user ID from sub claim."""
    token = make_mock_jwt({"sub": "user-123-abc"})
    response = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "user-123-abc"
    assert data["auth_mode"] == "supabase"


def test_invalid_token_format_returns_401():
    """Invalid token format returns 401."""
    response = client.get("/api/auth/me", headers={"Authorization": "Bearer not.a.valid.jwt.format"})
    assert response.status_code == 401


def test_token_without_sub_returns_401():
    """Token without sub claim returns 401."""
    token = make_mock_jwt({"email": "test@example.com"})
    response = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 401


def test_invalid_authorization_format_returns_401():
    """Authorization header without Bearer prefix returns 401."""
    response = client.get("/api/auth/me", headers={"Authorization": "Basic abc123"})
    assert response.status_code == 401
