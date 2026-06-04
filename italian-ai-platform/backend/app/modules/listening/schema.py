from typing import Optional
from pydantic import BaseModel


class ListeningQuestionResponse(BaseModel):
    question_id: str
    question_type: str
    prompt: str
    options: Optional[list[str]] = None


class ListeningTaskResponse(BaseModel):
    unit_code: str
    title: str
    instructions: str
    transcript: str
    show_transcript_by_default: bool = False
    questions: list[ListeningQuestionResponse]


class ListeningAnswer(BaseModel):
    question_id: str
    answer: str


class ListeningSubmitRequest(BaseModel):
    unit_code: str
    answers: list[ListeningAnswer]


class ListeningFeedbackItem(BaseModel):
    question_id: str
    is_correct: bool
    message: Optional[str] = None
    correct_answer: str
    explanation: str
    weak_point: Optional[str] = None


class ListeningSubmitResponse(BaseModel):
    unit_code: str
    score: int
    status: str
    feedback: list[ListeningFeedbackItem]
    weak_points: list[str]
    next_suggested_action: str
