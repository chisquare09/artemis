from fastapi import APIRouter, Query

from app.modules.lessons import service
from app.modules.lessons.schema import LessonDetailResponse

router = APIRouter(tags=["lessons"])


@router.get("/lessons/{unit_code}", response_model=LessonDetailResponse)
def get_lesson(unit_code: str, study_mode: str = Query(default="daily_communication")):
    return service.get_lesson(unit_code, study_mode)
