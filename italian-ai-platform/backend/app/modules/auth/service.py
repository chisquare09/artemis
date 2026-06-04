def get_auth_mode(user_id: str) -> str:
    return "development" if user_id == "dev-user" else "supabase"
