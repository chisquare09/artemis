from typing import List, Optional

from sqlalchemy import ForeignKey, Index, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, TimestampMixin, generate_uuid


class Curriculum(Base, TimestampMixin):
    __tablename__ = "curricula"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)
    language: Mapped[str] = mapped_column(String(10))
    version: Mapped[str] = mapped_column(String(20))
    levels: Mapped[List["Level"]] = relationship(back_populates="curriculum")


class StudyMode(Base, TimestampMixin):
    __tablename__ = "study_modes"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    code: Mapped[str] = mapped_column(String(50), unique=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(Text)


class Level(Base, TimestampMixin):
    __tablename__ = "levels"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    curriculum_id: Mapped[str] = mapped_column(ForeignKey("curricula.id"))
    code: Mapped[str] = mapped_column(String(10), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    order_index: Mapped[int] = mapped_column(Integer)
    goal: Mapped[Optional[str]] = mapped_column(Text)
    exit_outcomes: Mapped[Optional[str]] = mapped_column(Text)
    curriculum: Mapped["Curriculum"] = relationship(back_populates="levels")
    units: Mapped[List["Unit"]] = relationship(back_populates="level")


class Unit(Base, TimestampMixin):
    __tablename__ = "units"
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    level_id: Mapped[str] = mapped_column(ForeignKey("levels.id"))
    code: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(255))
    summary: Mapped[Optional[str]] = mapped_column(Text)
    order_index: Mapped[int] = mapped_column(Integer)
    level: Mapped["Level"] = relationship(back_populates="units")
    objectives: Mapped[List["UnitObjective"]] = relationship(back_populates="unit")
    activities: Mapped[List["LessonActivity"]] = relationship(back_populates="unit")


class UnitObjective(Base, TimestampMixin):
    __tablename__ = "unit_objectives"
    __table_args__ = (Index("ix_unit_objectives_unit_id", "unit_id"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    unit_id: Mapped[str] = mapped_column(ForeignKey("units.id"))
    objective_type: Mapped[str] = mapped_column(String(50))
    content: Mapped[str] = mapped_column(Text)
    order_index: Mapped[int] = mapped_column(Integer)
    unit: Mapped["Unit"] = relationship(back_populates="objectives")


class LessonActivity(Base, TimestampMixin):
    __tablename__ = "lesson_activities"
    __table_args__ = (Index("ix_lesson_activities_unit_id", "unit_id"),)
    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=generate_uuid)
    unit_id: Mapped[str] = mapped_column(ForeignKey("units.id"))
    activity_type: Mapped[str] = mapped_column(String(50))
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)
    skill_focus: Mapped[Optional[str]] = mapped_column(String(50))
    order_index: Mapped[int] = mapped_column(Integer)
    unit: Mapped["Unit"] = relationship(back_populates="activities")
