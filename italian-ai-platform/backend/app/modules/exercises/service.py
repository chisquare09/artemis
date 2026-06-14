from app.core.exceptions import NotFoundException
from app.modules.curriculum.unit_catalog import ensure_unit_exists
from app.modules.exercises.generator import generate_a1_5_quiz, generate_curriculum_quiz
from app.modules.exercises.evaluator import evaluate_item
from app.modules.exercises.scoring import calculate_score, collect_weak_points, collect_explanations

_exercise_store: dict[str, dict] = {}


def generate_exercise(unit_code: str, activity_type: str, count: int, study_mode: str = "daily_communication") -> dict:
    if activity_type != "quiz":
        raise NotFoundException(f"Activity type {activity_type} not supported")

    unit = ensure_unit_exists(unit_code)
    data = generate_a1_5_quiz(count, study_mode) if unit_code == "A1.5" else generate_curriculum_quiz(unit, count, study_mode)
    _exercise_store[data["exercise_id"]] = data
    response = {k: v for k, v in data.items() if k != "_internal"}
    return response


def submit_exercise(exercise_id: str, answers: list[dict]) -> dict:
    if exercise_id not in _exercise_store:
        raise NotFoundException(f"Exercise {exercise_id} not found")

    data = _exercise_store[exercise_id]
    internal_items = data["_internal"]
    answer_map = {a["item_id"]: a["answer"] for a in answers}

    feedbacks = []
    for i, item_data in enumerate(internal_items):
        item_id = f"{exercise_id}-{i}"
        answer = answer_map.get(item_id, "")
        result = evaluate_item(item_data, answer)
        feedbacks.append({
            "item_id": item_id,
            "is_correct": result["is_correct"],
            "message": "Correct!" if result["is_correct"] else "Incorrect.",
            "correct_answer": result["correct_answer"],
            "explanation": result["explanation"],
            "weak_point": result["weak_point"],
        })

    return {
        "exercise_id": exercise_id,
        "score": calculate_score(feedbacks),
        "status": "completed",
        "feedback": feedbacks,
        "weak_points": collect_weak_points(feedbacks),
        "explanations": collect_explanations(feedbacks),
    }
