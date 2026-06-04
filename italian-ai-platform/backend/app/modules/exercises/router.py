from fastapi import APIRouter
from app.modules.exercises import service
from app.modules.exercises.schema import (
    GenerateExerciseRequest,
    GenerateExerciseResponse,
    SubmitExerciseRequest,
    SubmitExerciseResponse,
)

router = APIRouter(tags=["exercises"])


@router.post("/exercises/generate", response_model=GenerateExerciseResponse)
def generate_exercise(request: GenerateExerciseRequest):
    return service.generate_exercise(request.unit_code, request.activity_type, request.count, request.study_mode)


@router.post("/exercises/submit", response_model=SubmitExerciseResponse)
def submit_exercise(request: SubmitExerciseRequest):
    answers = [{"item_id": a.item_id, "answer": a.answer} for a in request.answers]
    return service.submit_exercise(request.exercise_id, answers)
