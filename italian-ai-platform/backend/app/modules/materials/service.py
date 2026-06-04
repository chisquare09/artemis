import uuid
from app.core.exceptions import NotFoundException, BadRequestException
from app.modules.materials.chunker import chunk_text
from app.modules.materials.schema import SourceType

_materials: dict[str, dict] = {}
_unit_links: dict[str, list[str]] = {}  # unit_code -> [material_ids]

VALID_UNITS = {"A1.5"}


def _validate_unit(unit_code: str):
    if unit_code not in VALID_UNITS:
        raise NotFoundException(f"Unit {unit_code} not found")


def create_material(data: dict) -> dict:
    _validate_unit(data["unit_code"])
    if data["source_type"] == SourceType.manual_text and not data.get("raw_text"):
        raise BadRequestException("raw_text is required for manual_text source type")

    material_id = str(uuid.uuid4())
    chunks = []
    if data["source_type"] == SourceType.manual_text and data.get("raw_text"):
        chunks = chunk_text(data["raw_text"])

    material = {
        "material_id": material_id,
        "title": data["title"],
        "description": data.get("description"),
        "source_type": data["source_type"].value if isinstance(data["source_type"], SourceType) else data["source_type"],
        "source_url": data.get("source_url"),
        "language": data.get("language", "Italian"),
        "unit_code": data["unit_code"],
        "tags": data.get("tags", []),
        "chunks": chunks,
        "chunk_count": len(chunks),
    }
    _materials[material_id] = material
    if data["unit_code"] not in _unit_links:
        _unit_links[data["unit_code"]] = []
    _unit_links[data["unit_code"]].append(material_id)
    return material


def get_unit_materials(unit_code: str) -> dict:
    _validate_unit(unit_code)
    material_ids = _unit_links.get(unit_code, [])
    materials = [
        {
            "material_id": _materials[mid]["material_id"],
            "title": _materials[mid]["title"],
            "description": _materials[mid]["description"],
            "source_type": _materials[mid]["source_type"],
            "source_url": _materials[mid]["source_url"],
            "language": _materials[mid]["language"],
            "tags": _materials[mid]["tags"],
            "chunk_count": _materials[mid]["chunk_count"],
        }
        for mid in material_ids if mid in _materials
    ]
    return {"unit_code": unit_code, "materials": materials}


def get_material(material_id: str) -> dict:
    if material_id not in _materials:
        raise NotFoundException(f"Material {material_id} not found")
    return _materials[material_id]


def link_material_to_unit(material_id: str, unit_code: str, purpose: str) -> dict:
    if material_id not in _materials:
        raise NotFoundException(f"Material {material_id} not found")
    _validate_unit(unit_code)
    if unit_code not in _unit_links:
        _unit_links[unit_code] = []
    if material_id not in _unit_links[unit_code]:
        _unit_links[unit_code].append(material_id)
    return {"material_id": material_id, "unit_code": unit_code, "linked": True}
