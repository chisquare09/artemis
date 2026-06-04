import base64
import json
from typing import Optional

from fastapi import Depends, Header, HTTPException

from app.core.config import get_settings, Settings


def get_current_user_id(
    authorization: Optional[str] = Header(None),
    settings: Settings = Depends(get_settings),
) -> str:
    """
    Extract user ID from Supabase JWT or fall back to dev-user in development.
    
    Dev fallback: In development without Authorization header, returns "dev-user".
    Production: Must have valid Authorization header with JWT.
    
    WARNING: This implementation uses simple JWT payload decoding for development/test.
    Production deployments must configure SUPABASE_JWT_SECRET and use proper verification.
    """
    is_dev = settings.APP_ENV == "development"
    
    # Dev fallback: no token in development returns dev-user
    if not authorization:
        if is_dev:
            return "dev-user"
        raise HTTPException(status_code=401, detail="Authorization required")
    
    # Extract token from "Bearer <token>"
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization format")
    
    token = authorization[7:]
    
    try:
        # Decode JWT payload (middle segment) without verification for dev
        # In production with JWT_SECRET, proper verification should be added
        parts = token.split(".")
        if len(parts) != 3:
            raise HTTPException(status_code=401, detail="Invalid token format")
        
        # Add padding for base64 decoding
        payload_b64 = parts[1]
        padding = 4 - len(payload_b64) % 4
        if padding != 4:
            payload_b64 += "=" * padding
        
        payload = json.loads(base64.urlsafe_b64decode(payload_b64))
        user_id = payload.get("sub")
        
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token: no user ID")
        
        return user_id
    except (ValueError, json.JSONDecodeError, KeyError) as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {e}")
