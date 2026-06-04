from typing import Optional

from pydantic import BaseModel


class LessonActivityResponse(BaseModel):
    activity_type: str
    title: str
    description: Optional[str] = None
    skill_focus: Optional[str] = None
    order_index: int


class LessonProgressResponse(BaseModel):
    completion_percentage: float = 0
    mastery_score: Optional[float] = None
    status: str = "not_started"


class LessonAIHelperContextResponse(BaseModel):
    unit_code: str
    level: str
    title: str
    summary: Optional[str] = None
    objective_types: list[str] = []
    note: str = "AI tutor will use this lesson context in a later step"


class LessonDetailResponse(BaseModel):
    level: str
    unit_code: str
    title: str
    summary: Optional[str] = None
    objectives: dict[str, list[str]] = {}
    activities: list[LessonActivityResponse] = []
    progress: LessonProgressResponse
    ai_helper_context: LessonAIHelperContextResponse
    study_mode: str = "daily_communication"
    mode_label: str = "Daily Communication"
    mode_focus: Optional[str] = None
    mode_specific_guidance: Optional[str] = None
