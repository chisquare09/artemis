from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_manual_text_material():
    response = client.post("/api/materials", json={
        "title": "Test café menu",
        "description": "Test material",
        "source_type": "manual_text",
        "raw_text": "Caffè espresso 1,20 euro.",
        "unit_code": "A1.5",
        "tags": ["cafe", "menu"]
    })
    assert response.status_code == 200
    assert "material_id" in response.json()


def test_created_material_has_chunks():
    response = client.post("/api/materials", json={
        "title": "Test chunks",
        "source_type": "manual_text",
        "raw_text": "Buongiorno. Come stai?",
        "unit_code": "A1.5"
    })
    assert response.json()["chunk_count"] > 0


def test_get_unit_materials():
    client.post("/api/materials", json={
        "title": "Unit material",
        "source_type": "manual_text",
        "raw_text": "Ciao mondo.",
        "unit_code": "A1.5"
    })
    response = client.get("/api/materials/units/A1.5")
    assert response.status_code == 200
    assert response.json()["unit_code"] == "A1.5"
    assert len(response.json()["materials"]) > 0


def test_get_material_returns_chunks():
    create = client.post("/api/materials", json={
        "title": "Detail test",
        "source_type": "manual_text",
        "raw_text": "Vorrei un cappuccino.",
        "unit_code": "A1.5"
    })
    material_id = create.json()["material_id"]
    response = client.get(f"/api/materials/{material_id}")
    assert response.status_code == 200
    assert "chunks" in response.json()


def test_link_material_to_unit():
    create = client.post("/api/materials", json={
        "title": "Link test",
        "source_type": "manual_text",
        "raw_text": "Grazie mille.",
        "unit_code": "A1.5"
    })
    material_id = create.json()["material_id"]
    response = client.post(f"/api/materials/{material_id}/link-unit", json={"unit_code": "A1.5", "purpose": "reading"})
    assert response.status_code == 200
    assert response.json()["linked"] is True


def test_unknown_unit_returns_404():
    response = client.post("/api/materials", json={
        "title": "Unknown unit",
        "source_type": "manual_text",
        "raw_text": "Test.",
        "unit_code": "UNKNOWN"
    })
    assert response.status_code == 404


def test_unsupported_source_type_returns_error():
    response = client.post("/api/materials", json={
        "title": "Invalid type",
        "source_type": "invalid_type",
        "raw_text": "Test.",
        "unit_code": "A1.5"
    })
    assert response.status_code == 422


def test_manual_text_without_raw_text_returns_error():
    response = client.post("/api/materials", json={
        "title": "No raw text",
        "source_type": "manual_text",
        "unit_code": "A1.5"
    })
    assert response.status_code == 400


def test_create_material_for_a2_unit():
    response = client.post("/api/materials", json={
        "title": "A2 travel story",
        "source_type": "manual_text",
        "raw_text": "Ieri sono andato a Roma.",
        "unit_code": "A2.1"
    })
    assert response.status_code == 200
    assert response.json()["unit_code"] == "A2.1"
