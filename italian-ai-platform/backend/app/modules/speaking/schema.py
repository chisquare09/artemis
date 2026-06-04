from typing import Optional
from pydantic import BaseModel


class StartRoleplayRequest(BaseModel):
    unit_code: str
    scenario_id: str = "cafe_ordering"


class RoleplayTurnResponse(BaseModel):
    speaker: str
    text: str


class StartRoleplayResponse(BaseModel):
    session_id: str
    unit_code: str
    scenario_id: str
    title: str
    system_role: str
    learner_role: str
    current_turn: RoleplayTurnResponse
    turns: list[RoleplayTurnResponse]


class RespondRoleplayRequest(BaseModel):
    session_id: str
    message: str


class RoleplayFeedback(BaseModel):
    is_appropriate: bool
    message: str
    weak_points: list[str] = []


class RespondRoleplayResponse(BaseModel):
    session_id: str
    accepted: bool
    feedback: RoleplayFeedback
    next_turn: Optional[RoleplayTurnResponse] = None
    is_complete: bool


class FinishRoleplayRequest(BaseModel):
    session_id: str


class FinishRoleplayResponse(BaseModel):
    session_id: str
    unit_code: str
    score: int
    status: str
    summary: str
    feedback: list[RoleplayFeedback]
    weak_points: list[str]
    next_suggested_action: str
