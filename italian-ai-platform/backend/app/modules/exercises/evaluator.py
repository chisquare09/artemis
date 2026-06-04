def normalize(text: str) -> str:
    return text.strip().lower()


def evaluate_multiple_choice(answer: str, correct: str) -> bool:
    return normalize(answer) == normalize(correct)


def evaluate_fill_blank(answer: str, correct: str) -> bool:
    return normalize(answer) == normalize(correct)


def evaluate_short_answer(answer: str, keywords: list[str]) -> bool:
    ans = normalize(answer)
    return all(kw.lower() in ans for kw in keywords)


def evaluate_short_writing(answer: str, keywords: list[str]) -> bool:
    ans = normalize(answer)
    return all(kw.lower() in ans for kw in keywords)


def evaluate_item(item_data: dict, answer: str) -> dict:
    item_type = item_data["item_type"]
    correct_answer = item_data["correct_answer"]
    keywords = item_data.get("keywords", [])

    if item_type == "multiple_choice":
        is_correct = evaluate_multiple_choice(answer, correct_answer)
    elif item_type == "fill_blank":
        is_correct = evaluate_fill_blank(answer, correct_answer)
    elif item_type == "short_answer":
        is_correct = evaluate_short_answer(answer, keywords)
    elif item_type == "short_writing":
        is_correct = evaluate_short_writing(answer, keywords)
    else:
        is_correct = False

    return {
        "is_correct": is_correct,
        "correct_answer": correct_answer,
        "explanation": item_data.get("explanation", ""),
        "weak_point": None if is_correct else item_data.get("weak_point"),
    }
