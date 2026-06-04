def calculate_score(feedbacks: list[dict]) -> int:
    if not feedbacks:
        return 0
    correct = sum(1 for f in feedbacks if f["is_correct"])
    return round(correct / len(feedbacks) * 100)


def collect_weak_points(feedbacks: list[dict]) -> list[str]:
    return list({f["weak_point"] for f in feedbacks if f.get("weak_point")})


def collect_explanations(feedbacks: list[dict]) -> list[str]:
    return [f["explanation"] for f in feedbacks if f.get("explanation")]
