from typing import Optional
from pydantic import BaseModel


class GenerateExerciseRequest(BaseModel):
    unit_code: str
    activity_type: str = "quiz"
    count: int = 5
    study_mode: str = "daily_communication"


class ExerciseItemResponse(BaseModel):
    item_id: str
    item_type: str
    prompt: str
    options: Optional[list[str]] = None
    order_index: int


class GenerateExerciseResponse(BaseModel):
    exercise_id: str
    unit_code: str
    activity_type: str
    title: str
    instructions: str
    items: list[ExerciseItemResponse]
    study_mode: str = "daily_communication"


class SubmitExerciseAnswer(BaseModel):
    item_id: str
    answer: str


class SubmitExerciseRequest(BaseModel):
    exercise_id: str
    answers: list[SubmitExerciseAnswer]


class ExerciseItemFeedback(BaseModel):
    item_id: str
    is_correct: bool
    message: Optional[str] = None
    correct_answer: str
    explanation: str
    weak_point: Optional[str] = None


class SubmitExerciseResponse(BaseModel):
    exercise_id: str
    score: int
    status: str
    feedback: list[ExerciseItemFeedback]
    weak_points: list[str]
    explanations: list[str]
