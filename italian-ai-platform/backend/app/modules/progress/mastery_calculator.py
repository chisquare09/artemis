def calculate_completion_percentage(completed: int, total: int) -> float:
    if total == 0:
        return 0
    return round(completed / total * 100, 1)


def calculate_unit_status(completion_percentage: float) -> str:
    if completion_percentage == 0:
        return "not_started"
    if completion_percentage >= 100:
        return "completed"
    return "in_progress"


def calculate_mastery_score(scores: list[int]) -> float | None:
    if not scores:
        return None
    return round(sum(scores) / len(scores), 1)


def update_skill_score(previous: float | None, new_score: int) -> float:
    if previous is None:
        return float(new_score)
    return round((previous + new_score) / 2, 1)
