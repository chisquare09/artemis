from app.modules.exercises.generator import generate_a1_5_quiz


def test_generate_returns_exercise_id():
    result = generate_a1_5_quiz(5)
    assert "exercise_id" in result


def test_generate_returns_requested_count():
    result = generate_a1_5_quiz(5)
    assert len(result["items"]) == 5


def test_generate_does_not_expose_correct_answers():
    result = generate_a1_5_quiz(5)
    for item in result["items"]:
        assert "correct_answer" not in item


def test_generate_includes_supported_types():
    result = generate_a1_5_quiz(8)
    types = {item["item_type"] for item in result["items"]}
    assert "multiple_choice" in types
    assert "fill_blank" in types


def test_generate_covers_a1_5_targets():
    result = generate_a1_5_quiz(8)
    prompts = " ".join(item["prompt"] for item in result["items"])
    assert "coffee" in prompts.lower() or "caffè" in prompts.lower()
    assert "costa" in prompts.lower()
