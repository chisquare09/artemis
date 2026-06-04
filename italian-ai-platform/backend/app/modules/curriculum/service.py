from pathlib import Path

from app.core.exceptions import NotFoundException
from app.modules.curriculum.importer import load_curriculum_seed
from app.modules.curriculum.schema import (
    ActivityResponse,
    CurriculumOverviewResponse,
    LevelResponse,
    LevelSummaryResponse,
    StudyModeResponse,
    UnitDetailResponse,
    UnitSummaryResponse,
)

SEED_PATH = Path(__file__).parent / "seed_data/curriculum.yaml"

_seed_cache = None


def _get_seed():
    global _seed_cache
    if _seed_cache is None:
        _seed_cache = load_curriculum_seed(SEED_PATH)
    return _seed_cache


def get_curriculum_overview() -> CurriculumOverviewResponse:
    seed = _get_seed()
    return CurriculumOverviewResponse(
        title=seed.curriculum.title,
        description=seed.curriculum.description,
        language=seed.curriculum.language,
        version=seed.curriculum.version,
        levels=[LevelSummaryResponse(code=l.code, name=l.name, order_index=l.order_index) for l in seed.levels],
        study_modes=[StudyModeResponse(code=m.code, name=m.name, description=m.description) for m in seed.study_modes],
    )


def get_levels() -> list[LevelResponse]:
    seed = _get_seed()
    return [LevelResponse(code=l.code, name=l.name, order_index=l.order_index, goal=l.goal, exit_outcomes=l.exit_outcomes) for l in sorted(seed.levels, key=lambda x: x.order_index)]


def get_level(level_code: str) -> LevelResponse:
    seed = _get_seed()
    level = next((l for l in seed.levels if l.code == level_code), None)
    if not level:
        raise NotFoundException(f"Level {level_code} not found")
    return LevelResponse(code=level.code, name=level.name, order_index=level.order_index, goal=level.goal, exit_outcomes=level.exit_outcomes)


def get_units_by_level(level_code: str) -> list[UnitSummaryResponse]:
    seed = _get_seed()
    level = next((l for l in seed.levels if l.code == level_code), None)
    if not level:
        raise NotFoundException(f"Level {level_code} not found")
    return [UnitSummaryResponse(code=u.code, title=u.title, summary=u.summary, order_index=u.order_index) for u in sorted(level.units, key=lambda x: x.order_index)]


def get_unit(unit_code: str) -> UnitDetailResponse:
    seed = _get_seed()
    for level in seed.levels:
        unit = next((u for u in level.units if u.code == unit_code), None)
        if unit:
            objectives: dict[str, list[str]] = {}
            for obj in unit.objectives:
                objectives.setdefault(obj.type, []).append(obj.content)
            activities = [ActivityResponse(activity_type=a.activity_type, title=a.title, description=a.description, skill_focus=a.skill_focus, order_index=a.order_index) for a in sorted(unit.activities, key=lambda x: x.order_index)]
            return UnitDetailResponse(code=unit.code, title=unit.title, summary=unit.summary, order_index=unit.order_index, level_code=level.code, objectives=objectives, activities=activities)
    raise NotFoundException(f"Unit {unit_code} not found")
