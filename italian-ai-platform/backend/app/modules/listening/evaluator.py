A1_5_QUESTIONS = [
    {
        "question_id": "a15-listen-1",
        "question_type": "short_answer",
        "prompt": "What does the customer order?",
        "correct_keywords": ["cappuccino", "cornetto"],
        "correct_answer": "cappuccino and cornetto",
        "explanation": "The customer orders 'un cappuccino e un cornetto' (a cappuccino and a croissant).",
        "weak_point": "listening_cafe_order",
    },
    {
        "question_id": "a15-listen-2",
        "question_type": "short_answer",
        "prompt": "How much does it cost?",
        "correct_keywords": ["tre euro", "3 euro", "three euro", "3€"],
        "correct_answer": "tre euro (3 euros)",
        "explanation": "'Sono tre euro' means 'it is three euros'.",
        "weak_point": "listening_prices",
    },
    {
        "question_id": "a15-listen-3",
        "question_type": "short_answer",
        "prompt": "Which polite phrase is used by the customer?",
        "correct_keywords": ["per favore"],
        "correct_answer": "per favore",
        "explanation": "'Per favore' means 'please' and is a common polite phrase.",
        "weak_point": "polite_phrases",
    },
]


def evaluate_answer(question_data: dict, answer: str) -> dict:
    ans = answer.strip().lower()
    keywords = question_data["correct_keywords"]

    if question_data["question_id"] == "a15-listen-1":
        is_correct = all(kw.lower() in ans for kw in ["cappuccino", "cornetto"])
    else:
        is_correct = any(kw.lower() in ans for kw in keywords)

    return {
        "question_id": question_data["question_id"],
        "is_correct": is_correct,
        "message": "Correct!" if is_correct else "Incorrect.",
        "correct_answer": question_data["correct_answer"],
        "explanation": question_data["explanation"],
        "weak_point": None if is_correct else question_data["weak_point"],
    }


def calculate_score(feedbacks: list[dict]) -> int:
    if not feedbacks:
        return 0
    correct = sum(1 for f in feedbacks if f["is_correct"])
    return round(correct / len(feedbacks) * 100)


def collect_weak_points(feedbacks: list[dict]) -> list[str]:
    return list({f["weak_point"] for f in feedbacks if f.get("weak_point")})
