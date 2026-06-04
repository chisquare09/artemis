from fastapi import APIRouter
from app.modules.rag import service
from app.modules.rag.schema import RetrieveRequest, RetrieveResponse

router = APIRouter(tags=["rag"])


@router.post("/rag/retrieve", response_model=RetrieveResponse)
def retrieve(request: RetrieveRequest):
    return service.retrieve(request.unit_code, request.query, request.limit)
