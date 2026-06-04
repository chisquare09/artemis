from pydantic import BaseModel


class AuthMeResponse(BaseModel):
    user_id: str
    auth_mode: str  # "supabase" or "development"
