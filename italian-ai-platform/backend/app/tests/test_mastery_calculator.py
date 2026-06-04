from app.modules.progress.mastery_calculator import (
    calculate_completion_percentage,
    calculate_unit_status,
    calculate_mastery_score,
    update_skill_score,
)


def test_completion_percentage():
    assert calculate_completion_percentage(3, 7) == 42.9


def test_status_not_started():
    assert calculate_unit_status(0) == "not_started"


def test_status_in_progress():
    assert calculate_unit_status(50) == "in_progress"


def test_status_completed():
    assert calculate_unit_status(100) == "completed"


def test_mastery_score_empty():
    assert calculate_mastery_score([]) is None


def test_mastery_score_average():
    assert calculate_mastery_score([80, 90]) == 85.0


def test_skill_score_update():
    assert update_skill_score(80, 90) == 85.0


def test_skill_score_first():
    assert update_skill_score(None, 80) == 80.0
