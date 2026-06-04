from fastapi import APIRouter
from app.modules.listening import service
from app.modules.listening.schema import (
    ListeningTaskResponse,
    ListeningSubmitRequest,
    ListeningSubmitResponse,
)

router = APIRouter(tags=["listening"])


@router.get("/listening/units/{unit_code}", response_model=ListeningTaskResponse)
def get_listening_task(unit_code: str):
    return service.get_listening_task(unit_code)


@router.post("/listening/submit", response_model=ListeningSubmitResponse)
def submit_listening(request: ListeningSubmitRequest):
    answers = [{"question_id": a.question_id, "answer": a.answer} for a in request.answers]
    return service.submit_listening(request.unit_code, answers)
