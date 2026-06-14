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


def build_generic_listening_questions(unit) -> list[dict]:
    topic_keywords = [word.lower().strip(':,') for word in unit.title.split() if len(word) > 3]
    objective_values = [item for items in unit.objectives.values() for item in items]
    first_objective = objective_values[0] if objective_values else unit.title
    skill_focuses = [activity.skill_focus for activity in unit.activities if activity.skill_focus]
    first_skill = skill_focuses[0] if skill_focuses else "integrated"
    objective_keywords = [word.lower().strip(':,') for word in first_objective.split() if len(word) > 3][:3] or topic_keywords[:2]

    return [
        {
            "question_id": f"{unit.code}-listen-1",
            "question_type": "short_answer",
            "prompt": "What is the topic of this listening passage?",
            "correct_keywords": topic_keywords[:3] or [unit.code.lower()],
            "correct_answer": unit.title,
            "explanation": f"The passage is about {unit.title}.",
            "weak_point": "listening_main_idea",
        },
        {
            "question_id": f"{unit.code}-listen-2",
            "question_type": "short_answer",
            "prompt": "Name one objective or skill mentioned in the passage.",
            "correct_keywords": objective_keywords,
            "correct_answer": first_objective,
            "explanation": f"One unit objective is: {first_objective}.",
            "weak_point": "listening_detail",
        },
        {
            "question_id": f"{unit.code}-listen-3",
            "question_type": "short_answer",
            "prompt": "Which skill focus is practiced in this lesson?",
            "correct_keywords": [first_skill.lower()],
            "correct_answer": first_skill,
            "explanation": f"The activity skill focus is {first_skill}.",
            "weak_point": "listening_skill_focus",
        },
    ]
