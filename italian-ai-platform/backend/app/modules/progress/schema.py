from typing import Optional
from pydantic import BaseModel


class SkillProgressResponse(BaseModel):
    listening: float = 0
    reading: float = 0
    writing: float = 0
    speaking: float = 0


class ReviewQueueItemResponse(BaseModel):
    unit_code: str
    skill: str
    target: str
    priority: str
    status: str


class ProgressOverviewResponse(BaseModel):
    user_id: str
    active_level: str = "A1"
    active_mode: str = "daily-communication"
    overall_completion_percentage: float = 0
    skill_progress: SkillProgressResponse
    weak_points: list[str] = []
    review_queue: list[ReviewQueueItemResponse] = []
    recent_activity: list[str] = []


class UnitProgressResponse(BaseModel):
    user_id: str
    unit_code: str
    status: str
    completion_percentage: float
    mastery_score: Optional[float] = None
    completed_activities: int
    total_activities: int
    weak_points: list[str] = []
    last_studied_at: Optional[str] = None


class CompleteActivityRequest(BaseModel):
    unit_code: str
    activity_type: str
    skill: str = "reading"
    score: int = 100


class CompleteActivityResponse(BaseModel):
    unit_progress: UnitProgressResponse
    skill_progress: SkillProgressResponse
    next_suggested_action: str


class ExerciseResultProgressRequest(BaseModel):
    unit_code: str
    exercise_id: str
    score: int
    weak_points: list[str] = []
    skill_focus: str = "reading"


class ExerciseResultProgressResponse(BaseModel):
    unit_progress: UnitProgressResponse
    skill_progress: SkillProgressResponse
    review_items_created: int
    next_suggested_action: str
