import uuid
from app.core.exceptions import NotFoundException
from app.modules.speaking.roleplay_engine import get_scenario, get_next_waiter_turn
from app.modules.speaking.evaluator import evaluate_response, calculate_finish_score, collect_all_weak_points
from app.modules.progress.review_planner import suggest_next_action

_sessions: dict[str, dict] = {}


def start_roleplay(unit_code: str, scenario_id: str) -> dict:
    if unit_code != "A1.5":
        raise NotFoundException(f"Speaking for unit {unit_code} not found")
    scenario = get_scenario(scenario_id)
    if not scenario:
        raise NotFoundException(f"Scenario {scenario_id} not found")

    session_id = str(uuid.uuid4())
    first_turn = scenario["waiter_turns"][0]
    _sessions[session_id] = {
        "unit_code": unit_code,
        "scenario_id": scenario_id,
        "turn_index": 1,
        "turns": [first_turn],
        "feedbacks": [],
        "completed": False,
    }
    return {
        "session_id": session_id,
        "unit_code": unit_code,
        "scenario_id": scenario_id,
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

    eval_result = evaluate_response(message)
    feedback = {"is_appropriate": eval_result["is_appropriate"], "message": eval_result["message"], "weak_points": eval_result["weak_points"]}
    session["feedbacks"].append(eval_result)
    session["turns"].append({"speaker": "learner", "text": message})

    next_turn = get_next_waiter_turn(session["turn_index"])
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

    return {
        "session_id": session_id,
        "unit_code": session["unit_code"],
        "score": score,
        "status": "completed",
        "summary": f"You completed the café roleplay with a score of {score}%.",
        "feedback": feedback_list,
        "weak_points": weak_points,
        "next_suggested_action": suggest_next_action(100, score, weak_points),
    }
