def determine_review_priority(score: int) -> str:
    if score < 60:
        return "high"
    if score < 80:
        return "medium"
    return "low"


def create_review_items_from_weak_points(
    user_id: str, unit_code: str, weak_points: list[str], score: int, skill: str
) -> list[dict]:
    priority = determine_review_priority(score)
    items = []
    for wp in weak_points:
        items.append({
            "user_id": user_id,
            "unit_code": unit_code,
            "skill": skill,
            "review_type": "weak_point",
            "target": wp,
            "priority": priority,
            "status": "pending",
        })
    return items


def suggest_next_action(completion_percentage: float, mastery_score: float | None, weak_points: list[str]) -> str:
    if weak_points:
        return "Review weak points before continuing."
    if completion_percentage < 100:
        return "Continue remaining lesson activities."
    if mastery_score is not None and mastery_score >= 80:
        return "Move to the next lesson."
    return "Repeat the quiz or review explanations."
