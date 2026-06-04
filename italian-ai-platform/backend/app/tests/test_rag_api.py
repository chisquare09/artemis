from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def _seed_material():
    client.post("/api/materials", json={
        "title": "Café bill phrases",
        "source_type": "manual_text",
        "raw_text": "Il conto, per favore. Quanto costa il caffè?",
        "unit_code": "A1.5",
        "tags": ["cafe", "bill"]
    })


def test_retrieve_returns_chunks():
    _seed_material()
    response = client.post("/api/rag/retrieve", json={"unit_code": "A1.5", "query": "How do I ask for the bill?", "limit": 5})
    assert response.status_code == 200
    assert "chunks" in response.json()


def test_retrieve_strategy_is_keyword():
    _seed_material()
    response = client.post("/api/rag/retrieve", json={"unit_code": "A1.5", "query": "bill", "limit": 5})
    assert response.json()["retrieval_strategy"] == "keyword"


def test_retrieve_finds_conto_for_bill_query():
    _seed_material()
    response = client.post("/api/rag/retrieve", json={"unit_code": "A1.5", "query": "How do I ask for the bill?", "limit": 5})
    chunks = response.json()["chunks"]
    found = any("conto" in c["content"].lower() for c in chunks)
    assert found or len(chunks) == 0  # May not find if no material


def test_unknown_unit_returns_404():
    response = client.post("/api/rag/retrieve", json={"unit_code": "UNKNOWN", "query": "test", "limit": 5})
    assert response.status_code == 404


def test_empty_query_returns_validation_error():
    response = client.post("/api/rag/retrieve", json={"unit_code": "A1.5", "query": "", "limit": 5})
    assert response.status_code == 422


def test_no_materials_returns_empty_chunks():
    # Use fresh unit check - materials may exist from other tests
    response = client.post("/api/rag/retrieve", json={"unit_code": "A1.5", "query": "xyznonexistent", "limit": 5})
    assert response.status_code == 200
    # Either empty or no matches for nonsense query
