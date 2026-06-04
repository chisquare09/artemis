from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import setup_logging
from app.modules.ai.router import router as ai_router
from app.modules.curriculum.router import router as curriculum_router
from app.modules.exercises.router import router as exercises_router
from app.modules.lessons.router import router as lessons_router
from app.modules.listening.router import router as listening_router
from app.modules.progress.router import router as progress_router
from app.modules.speaking.router import router as speaking_router
from app.modules.materials.router import router as materials_router
from app.modules.rag.router import router as rag_router
from app.modules.auth.router import router as auth_router

setup_logging()
settings = get_settings()

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)

app.include_router(curriculum_router, prefix=settings.API_PREFIX)
app.include_router(lessons_router, prefix=settings.API_PREFIX)
app.include_router(ai_router, prefix=settings.API_PREFIX)
app.include_router(exercises_router, prefix=settings.API_PREFIX)
app.include_router(progress_router, prefix=settings.API_PREFIX)
app.include_router(listening_router, prefix=settings.API_PREFIX)
app.include_router(speaking_router, prefix=settings.API_PREFIX)
app.include_router(materials_router, prefix=settings.API_PREFIX)
app.include_router(rag_router, prefix=settings.API_PREFIX)
app.include_router(auth_router, prefix=settings.API_PREFIX)


@app.get("/")
def root():
    return {"service": "italian-ai-platform-api", "environment": settings.APP_ENV}


@app.get("/health")
def health():
    return {"status": "ok", "service": "italian-ai-platform-api"}
