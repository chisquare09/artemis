from pydantic import BaseModel, Field


class RetrieveRequest(BaseModel):
    unit_code: str
    query: str = Field(..., min_length=1)
    limit: int = Field(default=5, ge=1, le=10)


class RetrievedChunk(BaseModel):
    material_id: str
    material_title: str
    chunk_id: str
    chunk_index: int
    content: str
    score: float
    metadata: dict = {}


class RetrieveResponse(BaseModel):
    unit_code: str
    query: str
    chunks: list[RetrievedChunk]
    retrieval_strategy: str = "keyword"
