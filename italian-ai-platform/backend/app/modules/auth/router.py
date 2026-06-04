from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user_id
from app.modules.auth.schema import AuthMeResponse
from app.modules.auth import service

router = APIRouter(tags=["auth"])


@router.get("/auth/me", response_model=AuthMeResponse)
def get_me(user_id: str = Depends(get_current_user_id)):
    return AuthMeResponse(user_id=user_id, auth_mode=service.get_auth_mode(user_id))
