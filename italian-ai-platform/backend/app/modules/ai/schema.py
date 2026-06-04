from typing import Optional

from pydantic import BaseModel, field_validator


class ExplainLessonRequest(BaseModel):
    unit_code: str
    study_mode: Optional[str] = None


class ExplainLessonResponse(BaseModel):
    unit_code: str
    provider: str
    explanation: str
    used_context: Optional[dict] = None


class AnswerLessonQuestionRequest(BaseModel):
    unit_code: str
    question: str
    study_mode: Optional[str] = None

    @field_validator("question")
    @classmethod
    def question_not_empty(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("question cannot be empty")
        return v.strip()


class AnswerLessonQuestionResponse(BaseModel):
    unit_code: str
    provider: str
    answer: str
    used_context: Optional[dict] = None
