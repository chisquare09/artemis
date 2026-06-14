from __future__ import annotations

from pathlib import Path

import yaml
from sqlalchemy.orm import Session

from app.db.models import Curriculum, StudyMode, Level, Unit, UnitObjective, LessonActivity
from app.modules.curriculum.schema import CurriculumSeed


def load_curriculum_seed(path: str | Path) -> CurriculumSeed:
    with open(path) as f:
        data = yaml.safe_load(f)
    return CurriculumSeed.model_validate(data)


def validate_curriculum_seed(seed: CurriculumSeed) -> None:
    """Raises ValidationError if seed is invalid. Called implicitly by load_curriculum_seed."""
    pass


def import_curriculum_seed(db: Session | None, seed: CurriculumSeed, dry_run: bool = False) -> dict:
    summary = {
        "dry_run": dry_run,
        "curriculum_title": seed.curriculum.title,
        "levels_count": len(seed.levels),
        "units_count": sum(len(lvl.units) for lvl in seed.levels),
        "objectives_count": sum(len(u.objectives) for lvl in seed.levels for u in lvl.units),
        "activities_count": sum(len(u.activities) for lvl in seed.levels for u in lvl.units),
        "created_count": 0,
        "warnings": [],
    }

    if dry_run or db is None:
        summary["created_count"] = summary["levels_count"] + summary["units_count"] + summary["objectives_count"] + summary["activities_count"] + 1
        return summary

    # Upsert curriculum
    curriculum = db.query(Curriculum).filter_by(title=seed.curriculum.title, version=seed.curriculum.version).first()
    if not curriculum:
        curriculum = Curriculum(
            title=seed.curriculum.title,
            description=seed.curriculum.description,
            language=seed.curriculum.language,
            version=seed.curriculum.version,
        )
        db.add(curriculum)
        db.flush()
        summary["created_count"] += 1

    # Upsert study modes
    for sm in seed.study_modes:
        existing = db.query(StudyMode).filter_by(code=sm.code).first()
        if not existing:
            db.add(StudyMode(code=sm.code, name=sm.name, description=sm.description))
            summary["created_count"] += 1

    # Upsert levels and units
    for lvl in seed.levels:
        level = db.query(Level).filter_by(code=lvl.code).first()
        if not level:
            level = Level(
                curriculum_id=curriculum.id,
                code=lvl.code,
                name=lvl.name,
                order_index=lvl.order_index,
                goal=lvl.goal,
                exit_outcomes="\n".join(lvl.exit_outcomes) if lvl.exit_outcomes else None,
            )
            db.add(level)
            db.flush()
            summary["created_count"] += 1

        for u in lvl.units:
            unit = db.query(Unit).filter_by(code=u.code).first()
            if not unit:
                unit = Unit(
                    level_id=level.id,
                    code=u.code,
                    title=u.title,
                    summary=u.summary,
                    order_index=u.order_index,
                )
                db.add(unit)
                db.flush()
                summary["created_count"] += 1

            for obj in u.objectives:
                existing = db.query(UnitObjective).filter_by(unit_id=unit.id, objective_type=obj.type, content=obj.content).first()
                if not existing:
                    db.add(UnitObjective(unit_id=unit.id, objective_type=obj.type, content=obj.content, order_index=0))
                    summary["created_count"] += 1

            for act in u.activities:
                existing = db.query(LessonActivity).filter_by(unit_id=unit.id, activity_type=act.activity_type, title=act.title).first()
                if not existing:
                    db.add(LessonActivity(
                        unit_id=unit.id,
                        activity_type=act.activity_type,
                        title=act.title,
                        description=act.description,
                        skill_focus=act.skill_focus,
                        order_index=act.order_index,
                    ))
                    summary["created_count"] += 1

    db.commit()
    return summary
