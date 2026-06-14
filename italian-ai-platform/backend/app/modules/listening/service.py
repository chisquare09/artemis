from app.core.exceptions import NotFoundException
from app.modules.curriculum.unit_catalog import ensure_unit_exists
from app.modules.listening.evaluator import (
    A1_5_QUESTIONS,
    build_generic_listening_questions,
    evaluate_answer,
    calculate_score,
    collect_weak_points,
)
from app.modules.progress.review_planner import suggest_next_action

A1_5_TRANSCRIPT = """Cameriere: Buongiorno, desidera?
Cliente: Vorrei un cappuccino e un cornetto, per favore.
Cameriere: Altro?
Cliente: No, grazie. Quanto costa?
Cameriere: Sono tre euro."""


def _build_generic_transcript(unit) -> str:
    objective_values = [item for items in unit.objectives.values() for item in items]
    first_objective = objective_values[0] if objective_values else unit.title
    second_objective = objective_values[1] if len(objective_values) > 1 else first_objective
    return (
        f"Tutor: Oggi studiamo {unit.title}.\n"
        f"Studente: Qual è l'obiettivo principale?\n"
        f"Tutor: L'obiettivo è {first_objective}.\n"
        f"Studente: Che cosa pratichiamo?\n"
        f"Tutor: Pratichiamo {second_objective}."
    )


def _get_questions_for_unit(unit_code: str) -> list[dict]:
    if unit_code == "A1.5":
        return A1_5_QUESTIONS
    unit = ensure_unit_exists(unit_code)
    return build_generic_listening_questions(unit)


def get_listening_task(unit_code: str) -> dict:
    unit = ensure_unit_exists(unit_code)
    if unit_code == "A1.5":
        questions = A1_5_QUESTIONS
        return {
            "unit_code": "A1.5",
            "title": "Café dialogue",
            "instructions": "Listen to or read the café dialogue and answer the questions.",
            "transcript": A1_5_TRANSCRIPT,
            "show_transcript_by_default": False,
            "questions": [
                {"question_id": q["question_id"], "question_type": q["question_type"], "prompt": q["prompt"], "options": None}
                for q in questions
            ],
        }

    questions = build_generic_listening_questions(unit)
    return {
        "unit_code": unit.code,
        "title": f"{unit.code} Listening Practice",
        "instructions": "Listen to or read the unit passage and answer the questions.",
        "transcript": _build_generic_transcript(unit),
        "show_transcript_by_default": False,
        "questions": [
            {"question_id": q["question_id"], "question_type": q["question_type"], "prompt": q["prompt"], "options": None}
            for q in questions
        ],
    }


def submit_listening(unit_code: str, answers: list[dict]) -> dict:
    questions = _get_questions_for_unit(unit_code)
    answer_map = {a["question_id"]: a["answer"] for a in answers}
    feedbacks = []
    for q in questions:
        answer = answer_map.get(q["question_id"], "")
        feedbacks.append(evaluate_answer(q, answer))

    score = calculate_score(feedbacks)
    weak_points = collect_weak_points(feedbacks)

    return {
        "unit_code": unit_code,
        "score": score,
        "status": "completed",
        "feedback": feedbacks,
        "weak_points": weak_points,
        "next_suggested_action": suggest_next_action(100, score, weak_points),
    }
