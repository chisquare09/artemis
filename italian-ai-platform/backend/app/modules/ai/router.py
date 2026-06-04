from fastapi import APIRouter

from app.modules.ai.schema import (
    AnswerLessonQuestionRequest,
    AnswerLessonQuestionResponse,
    ExplainLessonRequest,
    ExplainLessonResponse,
)
from app.modules.ai.service import get_orchestrator

router = APIRouter(tags=["ai"])


@router.post("/ai/explain-lesson", response_model=ExplainLessonResponse)
def explain_lesson(request: ExplainLessonRequest):
    orchestrator = get_orchestrator()
    return orchestrator.explain_lesson(request.unit_code, request.study_mode)


@router.post("/ai/answer-question", response_model=AnswerLessonQuestionResponse)
def answer_question(request: AnswerLessonQuestionRequest):
    orchestrator = get_orchestrator()
    return orchestrator.answer_lesson_question(request.unit_code, request.question, request.study_mode)
