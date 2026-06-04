from app.modules.lessons.content_builder import build_lesson_detail
from app.modules.lessons.schema import LessonDetailResponse

VALID_MODES = {"daily_communication", "academic_purpose"}


def get_lesson(unit_code: str, study_mode: str = "daily_communication") -> LessonDetailResponse:
    if study_mode not in VALID_MODES:
        study_mode = "daily_communication"
    return build_lesson_detail(unit_code, study_mode)
