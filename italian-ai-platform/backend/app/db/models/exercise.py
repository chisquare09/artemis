from datetime import datetime
from typing import List, Optional

from sqlalchemy import DateTime, Float, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, TimestampMixin, generate_uuid


class Exercise(Base, TimestampMixin):
    __tablename__ = "exercises"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    unit_id: Mapped[str] = mapped_column(ForeignKey("units.id"))
    activity_id: Mapped[Optional[str]] = mapped_column(ForeignKey("lesson_activities.id"))
    exercise_type: Mapped[str] = mapped_column(String(50))
    title: Mapped[str] = mapped_column(String(255))
    instructions: Mapped[Optional[str]] = mapped_column(Text)
    skill_focus: Mapped[Optional[str]] = mapped_column(String(50))
    difficulty: Mapped[Optional[str]] = mapped_column(String(20))
    generated_by: Mapped[Optional[str]] = mapped_column(String(50))
    items: Mapped[List["ExerciseItem"]] = relationship(back_populates="exercise")
    attempts: Mapped[List["ExerciseAttempt"]] = relationship(back_populates="exercise")


class ExerciseItem(Base, TimestampMixin):
    __tablename__ = "exercise_items"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    exercise_id: Mapped[str] = mapped_column(ForeignKey("exercises.id"))
    item_type: Mapped[str] = mapped_column(String(50))
    prompt: Mapped[str] = mapped_column(Text)
    options_json: Mapped[Optional[dict]] = mapped_column(JSON)
    correct_answer_json: Mapped[Optional[dict]] = mapped_column(JSON)
    explanation: Mapped[Optional[str]] = mapped_column(Text)
    order_index: Mapped[int] = mapped_column(Integer)
    exercise: Mapped["Exercise"] = relationship(back_populates="items")


class ExerciseAttempt(Base, TimestampMixin):
    __tablename__ = "exercise_attempts"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    exercise_id: Mapped[str] = mapped_column(ForeignKey("exercises.id"))
    user_id: Mapped[str] = mapped_column(String(36), index=True)
    answers_json: Mapped[Optional[dict]] = mapped_column(JSON)
    score: Mapped[Optional[float]] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(20))
    submitted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    exercise: Mapped["Exercise"] = relationship(back_populates="attempts")
    feedback: Mapped[List["ExerciseFeedback"]] = relationship(back_populates="attempt")


class ExerciseFeedback(Base, TimestampMixin):
    __tablename__ = "exercise_feedback"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    attempt_id: Mapped[str] = mapped_column(ForeignKey("exercise_attempts.id"))
    feedback_json: Mapped[Optional[dict]] = mapped_column(JSON)
    weak_points_json: Mapped[Optional[dict]] = mapped_column(JSON)
    explanations_json: Mapped[Optional[dict]] = mapped_column(JSON)
    attempt: Mapped["ExerciseAttempt"] = relationship(back_populates="feedback")
