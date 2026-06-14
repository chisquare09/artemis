from datetime import datetime
from app.modules.curriculum.unit_catalog import ensure_unit_exists
from app.modules.progress.mastery_calculator import (
    calculate_completion_percentage,
    calculate_unit_status,
    calculate_mastery_score,
    update_skill_score,
)
from app.modules.progress.review_planner import (
    create_review_items_from_weak_points,
    suggest_next_action,
)

DEFAULT_ACTIVITY_COUNT = 7

# In-memory store (fallback when no DB)
_user_progress: dict[str, dict] = {}
_review_queue: dict[str, list[dict]] = {}


def _get_user_data(user_id: str) -> dict:
    if user_id not in _user_progress:
        _user_progress[user_id] = {
            "units": {},
            "skills": {"listening": None, "reading": None, "writing": None, "speaking": None, "integrated": None},
            "weak_points": set(),
            "recent": [],
        }
    return _user_progress[user_id]


def _get_activity_total(unit_code: str) -> int:
    unit = ensure_unit_exists(unit_code)
    return len(unit.activities) or DEFAULT_ACTIVITY_COUNT


def _get_unit_data(user_id: str, unit_code: str) -> dict:
    data = _get_user_data(user_id)
    if unit_code not in data["units"]:
        data["units"][unit_code] = {
            "completed_activities": set(),
            "scores": [],
            "weak_points": set(),
            "last_studied_at": None,
            "total": _get_activity_total(unit_code),
        }
    return data["units"][unit_code]


def _skill_response(skills: dict) -> dict:
    return {
        "listening": skills.get("listening") or 0,
        "reading": skills.get("reading") or 0,
        "writing": skills.get("writing") or 0,
        "speaking": skills.get("speaking") or 0,
    }


def _normalize_skill(skill: str) -> str:
    return skill if skill in {"listening", "reading", "writing", "speaking", "integrated"} else "reading"


def get_overview(user_id: str) -> dict:
    data = _get_user_data(user_id)
    total_completed = sum(len(u["completed_activities"]) for u in data["units"].values())
    total_possible = sum(u["total"] for u in data["units"].values()) or 1
    skills = data["skills"]
    review_items = _review_queue.get(user_id, [])
    return {
        "user_id": user_id,
        "active_level": "A1",
        "active_mode": "daily-communication",
        "overall_completion_percentage": calculate_completion_percentage(total_completed, total_possible),
        "skill_progress": _skill_response(skills),
        "weak_points": list(data["weak_points"]),
        "review_queue": [
            {"unit_code": r["unit_code"], "skill": r["skill"], "target": r["target"], "priority": r["priority"], "status": r["status"]}
            for r in review_items if r["status"] == "pending"
        ],
        "recent_activity": data["recent"][-5:],
    }


def get_unit_progress(user_id: str, unit_code: str) -> dict:
    ensure_unit_exists(unit_code)
    unit = _get_unit_data(user_id, unit_code)
    completed = len(unit["completed_activities"])
    total = unit["total"]
    pct = calculate_completion_percentage(completed, total)
    return {
        "user_id": user_id,
        "unit_code": unit_code,
        "status": calculate_unit_status(pct),
        "completion_percentage": pct,
        "mastery_score": calculate_mastery_score(unit["scores"]),
        "completed_activities": completed,
        "total_activities": total,
        "weak_points": list(unit["weak_points"]),
        "last_studied_at": unit["last_studied_at"],
    }


def complete_activity(user_id: str, unit_code: str, activity_type: str, skill: str, score: int) -> dict:
    ensure_unit_exists(unit_code)
    data = _get_user_data(user_id)
    unit = _get_unit_data(user_id, unit_code)
    normalized_skill = _normalize_skill(skill)
    unit["completed_activities"].add(activity_type)
    unit["scores"].append(score)
    unit["last_studied_at"] = datetime.utcnow().isoformat()
    data["skills"][normalized_skill] = update_skill_score(data["skills"].get(normalized_skill), score)
    data["recent"].append(f"{unit_code}:{activity_type}")
    unit_prog = get_unit_progress(user_id, unit_code)
    return {
        "unit_progress": unit_prog,
        "skill_progress": _skill_response(data["skills"]),
        "next_suggested_action": suggest_next_action(unit_prog["completion_percentage"], unit_prog["mastery_score"], list(unit["weak_points"])),
    }


def record_exercise_result(user_id: str, unit_code: str, exercise_id: str, score: int, weak_points: list[str], skill_focus: str) -> dict:
    ensure_unit_exists(unit_code)
    data = _get_user_data(user_id)
    unit = _get_unit_data(user_id, unit_code)
    normalized_skill = _normalize_skill(skill_focus)
    unit["completed_activities"].add("quiz")
    unit["scores"].append(score)
    unit["last_studied_at"] = datetime.utcnow().isoformat()
    for wp in weak_points:
        unit["weak_points"].add(wp)
        data["weak_points"].add(wp)
    data["skills"][normalized_skill] = update_skill_score(data["skills"].get(normalized_skill), score)
    data["recent"].append(f"{unit_code}:quiz")

    new_items = create_review_items_from_weak_points(user_id, unit_code, weak_points, score, normalized_skill)
    if user_id not in _review_queue:
        _review_queue[user_id] = []
    existing_targets = {r["target"] for r in _review_queue[user_id] if r["status"] == "pending"}
    added = 0
    for item in new_items:
        if item["target"] not in existing_targets:
            _review_queue[user_id].append(item)
            existing_targets.add(item["target"])
            added += 1

    unit_prog = get_unit_progress(user_id, unit_code)
    return {
        "unit_progress": unit_prog,
        "skill_progress": _skill_response(data["skills"]),
        "review_items_created": added,
        "next_suggested_action": suggest_next_action(unit_prog["completion_percentage"], unit_prog["mastery_score"], list(unit["weak_points"])),
    }
