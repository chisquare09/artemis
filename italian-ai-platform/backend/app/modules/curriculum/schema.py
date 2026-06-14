from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, model_validator


class ActivitySeed(BaseModel):
    activity_type: str
    title: str
    description: Optional[str] = None
    skill_focus: Optional[str] = None
    order_index: int


class ObjectiveSeed(BaseModel):
    type: str
    content: str


class UnitSeed(BaseModel):
    code: str
    title: str
    summary: Optional[str] = None
    order_index: int
    objectives: List[ObjectiveSeed] = []
    activities: List[ActivitySeed] = []

    @model_validator(mode="after")
    def check_has_content(self):
        if not self.objectives and not self.activities:
            raise ValueError(f"Unit {self.code} must have at least one objective or activity")
        return self


class LevelSeed(BaseModel):
    code: str
    name: str
    order_index: int
    goal: Optional[str] = None
    exit_outcomes: List[str] = []
    units: List[UnitSeed] = []


class StudyModeSeed(BaseModel):
    code: str
    name: str
    description: Optional[str] = None


class CurriculumInfoSeed(BaseModel):
    title: str
    description: Optional[str] = None
    language: str
    version: str


class CurriculumSeed(BaseModel):
    curriculum: CurriculumInfoSeed
    study_modes: List[StudyModeSeed] = []
    levels: List[LevelSeed] = []


# API Response Schemas

class StudyModeResponse(BaseModel):
    code: str
    name: str
    description: Optional[str] = None


class LevelSummaryResponse(BaseModel):
    code: str
    name: str
    order_index: int


class CurriculumOverviewResponse(BaseModel):
    title: str
    description: Optional[str] = None
    language: str
    version: str
    levels: List[LevelSummaryResponse] = []
    study_modes: List[StudyModeResponse] = []


class LevelResponse(BaseModel):
    code: str
    name: str
    order_index: int
    goal: Optional[str] = None
    exit_outcomes: List[str] = []


class UnitSummaryResponse(BaseModel):
    code: str
    title: str
    summary: Optional[str] = None
    order_index: int


class ActivityResponse(BaseModel):
    activity_type: str
    title: str
    description: Optional[str] = None
    skill_focus: Optional[str] = None
    order_index: int


class UnitDetailResponse(BaseModel):
    code: str
    title: str
    summary: Optional[str] = None
    order_index: int
    level_code: str
    objectives: Dict[str, List[str]] = {}
    activities: List[ActivityResponse] = []
