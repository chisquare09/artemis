from pydantic import BaseModel
from enum import Enum


class SourceType(str, Enum):
    manual_text = "manual_text"
    pdf = "pdf"
    webpage = "webpage"
    youtube_transcript = "youtube_transcript"


class CreateMaterialRequest(BaseModel):
    title: str
    description: str | None = None
    source_type: SourceType
    source_url: str | None = None
    language: str = "Italian"
    raw_text: str | None = None
    level_code: str | None = None
    unit_code: str
    tags: list[str] = []


class MaterialChunkResponse(BaseModel):
    chunk_index: int
    content: str
    token_count: int


class MaterialSummaryResponse(BaseModel):
    material_id: str
    title: str
    description: str | None
    source_type: str
    source_url: str | None
    language: str
    tags: list[str]
    chunk_count: int


class MaterialDetailResponse(BaseModel):
    material_id: str
    title: str
    description: str | None
    source_type: str
    source_url: str | None
    language: str
    unit_code: str
    tags: list[str]
    chunk_count: int
    chunks: list[MaterialChunkResponse]


class UnitMaterialsResponse(BaseModel):
    unit_code: str
    materials: list[MaterialSummaryResponse]


class LinkMaterialToUnitRequest(BaseModel):
    unit_code: str
    purpose: str = "reading_practice"


class LinkMaterialToUnitResponse(BaseModel):
    material_id: str
    unit_code: str
    linked: bool
