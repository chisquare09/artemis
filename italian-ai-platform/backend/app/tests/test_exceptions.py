from fastapi.testclient import TestClient

from app.core.exceptions import NotFoundException
from app.main import app

client = TestClient(app)


@app.get("/test-not-found")
def raise_not_found():
    raise NotFoundException("Test resource not found")


def test_exception_handler_json_format():
    response = client.get("/test-not-found")
    assert response.status_code == 404
    data = response.json()
    assert "error" in data
    assert "code" in data["error"]
    assert "message" in data["error"]
    assert data["error"]["code"] == "NOT_FOUND"
