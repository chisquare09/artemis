from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, Float, ForeignKey, Index, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, TimestampMixin, generate_uuid


class UserProfile(Base, TimestampMixin):
    __tablename__ = "user_profiles"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    display_name: Mapped[Optional[str]] = mapped_column(String(100))
    active_level: Mapped[Optional[str]] = mapped_column(String(10))
    active_mode: Mapped[Optional[str]] = mapped_column(String(50))
    learning_preferences_json: Mapped[Optional[dict]] = mapped_column(JSON)


class UserUnitProgress(Base, TimestampMixin):
    __tablename__ = "user_unit_progress"
    __table_args__ = (Index("ix_user_unit_progress_user_id", "user_id"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    user_id: Mapped[str] = mapped_column(String(36))
    unit_id: Mapped[str] = mapped_column(ForeignKey("units.id"))
    status: Mapped[str] = mapped_column(String(20))
    completion_percentage: Mapped[Optional[float]] = mapped_column(Float)
    mastery_score: Mapped[Optional[float]] = mapped_column(Float)
    weak_points_json: Mapped[Optional[dict]] = mapped_column(JSON)
    last_studied_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))


class UserActivityProgress(Base, TimestampMixin):
    __tablename__ = "user_activity_progress"
    __table_args__ = (Index("ix_user_activity_progress_user_id", "user_id"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    user_id: Mapped[str] = mapped_column(String(36))
    activity_id: Mapped[str] = mapped_column(ForeignKey("lesson_activities.id"))
    status: Mapped[str] = mapped_column(String(20))
    score: Mapped[Optional[float]] = mapped_column(Float)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))


class UserSkillProgress(Base, TimestampMixin):
    __tablename__ = "user_skill_progress"
    __table_args__ = (Index("ix_user_skill_progress_user_id", "user_id"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    user_id: Mapped[str] = mapped_column(String(36))
    skill: Mapped[str] = mapped_column(String(50))
    score: Mapped[Optional[float]] = mapped_column(Float)
    updated_reason: Mapped[Optional[str]] = mapped_column(Text)


class MistakeLog(Base, TimestampMixin):
    __tablename__ = "mistake_logs"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    user_id: Mapped[str] = mapped_column(String(36), index=True)
    unit_id: Mapped[Optional[str]] = mapped_column(ForeignKey("units.id"))
    skill: Mapped[Optional[str]] = mapped_column(String(50))
    mistake_type: Mapped[Optional[str]] = mapped_column(String(50))
    mistake_text: Mapped[Optional[str]] = mapped_column(Text)
    correction: Mapped[Optional[str]] = mapped_column(Text)
    explanation: Mapped[Optional[str]] = mapped_column(Text)


class ReviewQueueItem(Base, TimestampMixin):
    __tablename__ = "review_queue_items"
    __table_args__ = (Index("ix_review_queue_items_user_id", "user_id"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    user_id: Mapped[str] = mapped_column(String(36))
    unit_id: Mapped[Optional[str]] = mapped_column(ForeignKey("units.id"))
    skill: Mapped[Optional[str]] = mapped_column(String(50))
    review_type: Mapped[Optional[str]] = mapped_column(String(50))
    target: Mapped[Optional[str]] = mapped_column(Text)
    priority: Mapped[Optional[float]] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(20))
    due_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
