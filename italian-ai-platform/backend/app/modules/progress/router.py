from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user_id
from app.modules.progress import service
from app.modules.progress.schema import (
    ProgressOverviewResponse,
    UnitProgressResponse,
    CompleteActivityRequest,
    CompleteActivityResponse,
    ExerciseResultProgressRequest,
    ExerciseResultProgressResponse,
)

router = APIRouter(tags=["progress"])


@router.get("/progress/overview", response_model=ProgressOverviewResponse)
def get_overview(user_id: str = Depends(get_current_user_id)):
    return service.get_overview(user_id)


@router.get("/progress/units/{unit_code}", response_model=UnitProgressResponse)
def get_unit_progress(unit_code: str, user_id: str = Depends(get_current_user_id)):
    return service.get_unit_progress(user_id, unit_code)


@router.post("/progress/activities/complete", response_model=CompleteActivityResponse)
def complete_activity(request: CompleteActivityRequest, user_id: str = Depends(get_current_user_id)):
    return service.complete_activity(user_id, request.unit_code, request.activity_type, request.skill, request.score)


@router.post("/progress/exercise-result", response_model=ExerciseResultProgressResponse)
def record_exercise_result(request: ExerciseResultProgressRequest, user_id: str = Depends(get_current_user_id)):
    return service.record_exercise_result(user_id, request.unit_code, request.exercise_id, request.score, request.weak_points, request.skill_focus)
