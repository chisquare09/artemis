from app.core.exceptions import NotFoundException
from app.modules.listening.evaluator import A1_5_QUESTIONS, evaluate_answer, calculate_score, collect_weak_points
from app.modules.progress.review_planner import suggest_next_action

A1_5_TRANSCRIPT = """Cameriere: Buongiorno, desidera?
Cliente: Vorrei un cappuccino e un cornetto, per favore.
Cameriere: Altro?
Cliente: No, grazie. Quanto costa?
Cameriere: Sono tre euro."""


def get_listening_task(unit_code: str) -> dict:
    if unit_code != "A1.5":
        raise NotFoundException(f"Listening task for unit {unit_code} not found")
    return {
        "unit_code": "A1.5",
        "title": "Café dialogue",
        "instructions": "Listen to or read the café dialogue and answer the questions.",
        "transcript": A1_5_TRANSCRIPT,
        "show_transcript_by_default": False,
        "questions": [
            {"question_id": q["question_id"], "question_type": q["question_type"], "prompt": q["prompt"], "options": None}
            for q in A1_5_QUESTIONS
        ],
    }


def submit_listening(unit_code: str, answers: list[dict]) -> dict:
    if unit_code != "A1.5":
        raise NotFoundException(f"Listening task for unit {unit_code} not found")

    answer_map = {a["question_id"]: a["answer"] for a in answers}
    feedbacks = []
    for q in A1_5_QUESTIONS:
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
