from typing import List, Optional

from sqlalchemy import ForeignKey, Index, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, TimestampMixin, generate_uuid


class ChatSession(Base, TimestampMixin):
    __tablename__ = "chat_sessions"
    __table_args__ = (Index("ix_chat_sessions_user_id", "user_id"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    user_id: Mapped[str] = mapped_column(String(36))
    unit_id: Mapped[Optional[str]] = mapped_column(ForeignKey("units.id"))
    title: Mapped[Optional[str]] = mapped_column(String(255))
    messages: Mapped[List["ChatMessage"]] = relationship(back_populates="session")


class ChatMessage(Base, TimestampMixin):
    __tablename__ = "chat_messages"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    session_id: Mapped[str] = mapped_column(ForeignKey("chat_sessions.id"))
    role: Mapped[str] = mapped_column(String(20))
    content: Mapped[str] = mapped_column(Text)
    metadata_json: Mapped[Optional[dict]] = mapped_column(JSON)
    session: Mapped["ChatSession"] = relationship(back_populates="messages")


class GeneratedContentCache(Base, TimestampMixin):
    __tablename__ = "generated_content_cache"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    unit_id: Mapped[Optional[str]] = mapped_column(ForeignKey("units.id"))
    content_type: Mapped[str] = mapped_column(String(50))
    cache_key: Mapped[str] = mapped_column(String(255), index=True)
    content_json: Mapped[Optional[dict]] = mapped_column(JSON)
    provider: Mapped[Optional[str]] = mapped_column(String(50))
