from fastapi import APIRouter

from app.modules.curriculum import service
from app.modules.curriculum.schema import (
    CurriculumOverviewResponse,
    LevelResponse,
    UnitDetailResponse,
    UnitSummaryResponse,
)

router = APIRouter(tags=["curriculum"])


@router.get("/curriculum", response_model=CurriculumOverviewResponse)
def get_curriculum():
    return service.get_curriculum_overview()


@router.get("/levels", response_model=list[LevelResponse])
def get_levels():
    return service.get_levels()


@router.get("/levels/{level_code}", response_model=LevelResponse)
def get_level(level_code: str):
    return service.get_level(level_code)


@router.get("/levels/{level_code}/units", response_model=list[UnitSummaryResponse])
def get_level_units(level_code: str):
    return service.get_units_by_level(level_code)


@router.get("/units/{unit_code}", response_model=UnitDetailResponse)
def get_unit(unit_code: str):
    return service.get_unit(unit_code)
