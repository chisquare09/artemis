import uuid
from app.core.exceptions import NotFoundException
from app.modules.curriculum.unit_catalog import ensure_unit_exists
from app.modules.speaking.roleplay_engine import get_scenario, get_next_waiter_turn
from app.modules.speaking.evaluator import evaluate_response, calculate_finish_score, collect_all_weak_points
from app.modules.progress.review_planner import suggest_next_action

_sessions: dict[str, dict] = {}


def _build_evaluation_context(unit_code: str, scenario_id: str, scenario: dict) -> dict:
    unit = ensure_unit_exists(unit_code)
    objective_values = [item for items in unit.objectives.values() for item in items]
    objective_keywords = [
        word.lower().strip(':,')
        for value in objective_values[:3]
        for word in value.split()
        if len(word) > 4
    ][:8]
    return {
        "unit_code": unit_code,
        "scenario_id": scenario_id,
        "title": unit.title,
        "objective_keywords": objective_keywords,
        "system_role": scenario["system_role"],
    }


def start_roleplay(unit_code: str, scenario_id: str) -> dict:
    ensure_unit_exists(unit_code)
    effective_scenario_id = "cafe_ordering" if unit_code == "A1.5" and scenario_id == "cafe_ordering" else scenario_id
    if unit_code != "A1.5" and effective_scenario_id == "cafe_ordering":
        effective_scenario_id = "unit-default"

    scenario = get_scenario(effective_scenario_id, unit_code)
    if not scenario:
        raise NotFoundException(f"Scenario {scenario_id} not found")

    session_id = str(uuid.uuid4())
    first_turn = scenario["waiter_turns"][0]
    _sessions[session_id] = {
        "unit_code": unit_code,
        "scenario_id": scenario["scenario_id"],
        "turn_index": 1,
        "turns": [first_turn],
        "scenario_turns": scenario["waiter_turns"],
        "feedbacks": [],
        "completed": False,
        "evaluation_context": _build_evaluation_context(unit_code, scenario["scenario_id"], scenario),
    }
    return {
        "session_id": session_id,
        "unit_code": unit_code,
        "scenario_id": scenario["scenario_id"],
        "title": scenario["title"],
        "system_role": scenario["system_role"],
        "learner_role": scenario["learner_role"],
        "current_turn": first_turn,
        "turns": [first_turn],
    }


def respond_roleplay(session_id: str, message: str) -> dict:
    if session_id not in _sessions:
        raise NotFoundException(f"Session {session_id} not found")
    session = _sessions[session_id]
    if session["completed"]:
        return {"session_id": session_id, "accepted": False, "feedback": {"is_appropriate": False, "message": "Session already completed.", "weak_points": []}, "next_turn": None, "is_complete": True}

    eval_result = evaluate_response(message, session.get("evaluation_context"))
    feedback = {"is_appropriate": eval_result["is_appropriate"], "message": eval_result["message"], "weak_points": eval_result["weak_points"]}
    session["feedbacks"].append(eval_result)
    session["turns"].append({"speaker": "learner", "text": message})

    next_turn = get_next_waiter_turn(session["turn_index"], session.get("scenario_turns"))
    session["turn_index"] += 1
    is_complete = next_turn is None

    if next_turn:
        session["turns"].append(next_turn)
    if is_complete:
        session["completed"] = True

    return {"session_id": session_id, "accepted": True, "feedback": feedback, "next_turn": next_turn, "is_complete": is_complete}


def finish_roleplay(session_id: str) -> dict:
    if session_id not in _sessions:
        raise NotFoundException(f"Session {session_id} not found")
    session = _sessions[session_id]
    session["completed"] = True

    feedbacks = session["feedbacks"]
    score = calculate_finish_score(feedbacks)
    weak_points = collect_all_weak_points(feedbacks)
    feedback_list = [{"is_appropriate": f["is_appropriate"], "message": f["message"], "weak_points": f["weak_points"]} for f in feedbacks]
    scenario_label = "café roleplay" if session["scenario_id"] == "cafe_ordering" else "unit roleplay"

    return {
        "session_id": session_id,
        "unit_code": session["unit_code"],
        "score": score,
        "status": "completed",
        "summary": f"You completed the {scenario_label} with a score of {score}%.",
        "feedback": feedback_list,
        "weak_points": weak_points,
        "next_suggested_action": suggest_next_action(100, score, weak_points),
    }
