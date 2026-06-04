from fastapi import APIRouter
from app.modules.materials import service
from app.modules.materials.schema import (
    CreateMaterialRequest,
    MaterialDetailResponse,
    UnitMaterialsResponse,
    LinkMaterialToUnitRequest,
    LinkMaterialToUnitResponse,
)

router = APIRouter(tags=["materials"])


@router.post("/materials")
def create_material(request: CreateMaterialRequest):
    return service.create_material(request.model_dump())


@router.get("/materials/units/{unit_code}", response_model=UnitMaterialsResponse)
def get_unit_materials(unit_code: str):
    return service.get_unit_materials(unit_code)


@router.get("/materials/{material_id}", response_model=MaterialDetailResponse)
def get_material(material_id: str):
    return service.get_material(material_id)


@router.post("/materials/{material_id}/link-unit", response_model=LinkMaterialToUnitResponse)
def link_material_to_unit(material_id: str, request: LinkMaterialToUnitRequest):
    return service.link_material_to_unit(material_id, request.unit_code, request.purpose)
