from fastapi import APIRouter
from app.modules.speaking import service
from app.modules.speaking.schema import (
    StartRoleplayRequest,
    StartRoleplayResponse,
    RespondRoleplayRequest,
    RespondRoleplayResponse,
    FinishRoleplayRequest,
    FinishRoleplayResponse,
)

router = APIRouter(tags=["speaking"])


@router.post("/speaking/roleplay/start", response_model=StartRoleplayResponse)
def start_roleplay(request: StartRoleplayRequest):
    return service.start_roleplay(request.unit_code, request.scenario_id)


@router.post("/speaking/roleplay/respond", response_model=RespondRoleplayResponse)
def respond_roleplay(request: RespondRoleplayRequest):
    return service.respond_roleplay(request.session_id, request.message)


@router.post("/speaking/roleplay/finish", response_model=FinishRoleplayResponse)
def finish_roleplay(request: FinishRoleplayRequest):
    return service.finish_roleplay(request.session_id)
