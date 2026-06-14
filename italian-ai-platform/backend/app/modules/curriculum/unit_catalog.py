from app.core.exceptions import NotFoundException
from app.modules.curriculum.schema import UnitDetailResponse
from app.modules.curriculum.service import get_unit, get_units_by_level, _get_seed


def get_valid_unit_codes() -> set[str]:
    seed = _get_seed()
    return {unit.code for level in seed.levels for unit in level.units}


def is_valid_unit_code(unit_code: str) -> bool:
    return unit_code in get_valid_unit_codes()


def ensure_unit_exists(unit_code: str) -> UnitDetailResponse:
    try:
        return get_unit(unit_code)
    except NotFoundException:
        raise


def get_unit_activity_types(unit_code: str) -> list[str]:
    unit = ensure_unit_exists(unit_code)
    return [activity.activity_type for activity in unit.activities]


def get_unit_skill_focuses(unit_code: str) -> list[str]:
    unit = ensure_unit_exists(unit_code)
    return sorted({activity.skill_focus for activity in unit.activities if activity.skill_focus})


def get_level_unit_codes(level_code: str) -> list[str]:
    return [unit.code for unit in get_units_by_level(level_code)]
