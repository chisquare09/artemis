from collections.abc import Generator
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import get_settings

_engine: Optional[object] = None
_SessionLocal: Optional[sessionmaker] = None


def _get_engine():
    global _engine
    if _engine is None:
        settings = get_settings()
        if not settings.DATABASE_URL:
            raise RuntimeError("DATABASE_URL is not configured")
        _engine = create_engine(settings.DATABASE_URL)
    return _engine


def _get_session_local():
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_get_engine())
    return _SessionLocal


def get_db() -> Generator[Session, None, None]:
    SessionLocal = _get_session_local()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
