from app.db.base import Base
from app.db import models
from app.shared.enums import ObjectiveType, Skill


def test_model_imports():
    """All model modules import successfully"""
    assert models.Curriculum is not None
    assert models.StudyMode is not None
    assert models.Level is not None
    assert models.Unit is not None
    assert models.UnitObjective is not None
    assert models.LessonActivity is not None
    assert models.Material is not None
    assert models.MaterialChunk is not None
    assert models.Exercise is not None
    assert models.ExerciseItem is not None
    assert models.ExerciseAttempt is not None
    assert models.UserProfile is not None
    assert models.UserUnitProgress is not None
    assert models.UserSkillProgress is not None
    assert models.ChatSession is not None
    assert models.ChatMessage is not None


def test_metadata_includes_tables():
    """SQLAlchemy metadata includes key tables"""
    table_names = Base.metadata.tables.keys()
    expected = [
        "curricula", "study_modes", "levels", "units", "unit_objectives",
        "lesson_activities", "materials", "material_chunks", "exercises",
        "exercise_items", "exercise_attempts", "user_profiles",
        "user_unit_progress", "user_skill_progress", "chat_sessions", "chat_messages",
    ]
    for name in expected:
        assert name in table_names, f"Table {name} not found in metadata"


def test_enum_model_compatibility():
    """Enum values can be used in model fields"""
    assert ObjectiveType.grammar.value == "grammar"
    assert Skill.listening.value == "listening"
    # These are string enums that can be stored in model string fields


def test_alembic_config_exists():
    """Alembic configuration exists"""
    import os
    assert os.path.exists("alembic.ini")
    assert os.path.exists("app/db/migrations/env.py")
    assert os.path.exists("app/db/migrations/versions")
