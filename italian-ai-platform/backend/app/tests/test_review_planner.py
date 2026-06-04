from app.modules.progress.review_planner import (
    determine_review_priority,
    create_review_items_from_weak_points,
    suggest_next_action,
)


def test_priority_high():
    assert determine_review_priority(50) == "high"


def test_priority_medium():
    assert determine_review_priority(70) == "medium"


def test_priority_low():
    assert determine_review_priority(90) == "low"


def test_create_review_items():
    items = create_review_items_from_weak_points("user1", "A1.5", ["piacere", "negation"], 60, "reading")
    assert len(items) == 2
    assert items[0]["target"] == "piacere"


def test_suggest_review_weak_points():
    assert "Review weak points" in suggest_next_action(50, 70, ["piacere"])


def test_suggest_continue():
    assert "Continue" in suggest_next_action(50, None, [])


def test_suggest_move_next():
    assert "next lesson" in suggest_next_action(100, 90, [])


def test_suggest_repeat():
    assert "Repeat" in suggest_next_action(100, 60, [])
