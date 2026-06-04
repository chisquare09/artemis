from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    APP_ENV: str = "development"
    PROJECT_NAME: str = "Italian AI Learning Platform API"
    API_PREFIX: str = "/api"
    FRONTEND_ORIGIN: str = "http://localhost:3000"
    DATABASE_URL: str = ""
    SUPABASE_URL: str = ""
    SUPABASE_SERVICE_ROLE_KEY: str = ""
    SUPABASE_JWT_SECRET: str = ""  # Required for production JWT verification
    GEMINI_API_KEY: str = ""
    GROQ_API_KEY: str = ""
    STORAGE_BUCKET: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()
