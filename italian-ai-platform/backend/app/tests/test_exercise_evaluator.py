from app.modules.exercises.evaluator import evaluate_item
from app.modules.exercises.scoring import calculate_score


def test_correct_multiple_choice():
    item = {"item_type": "multiple_choice", "correct_answer": "Vorrei un caffè.", "explanation": "", "weak_point": "cafe_vocabulary"}
    result = evaluate_item(item, "Vorrei un caffè.")
    assert result["is_correct"] is True


def test_incorrect_multiple_choice():
    item = {"item_type": "multiple_choice", "correct_answer": "Vorrei un caffè.", "explanation": "", "weak_point": "cafe_vocabulary"}
    result = evaluate_item(item, "Voglio caffè.")
    assert result["is_correct"] is False


def test_fill_blank_quanto():
    item = {"item_type": "fill_blank", "correct_answer": "Quanto", "explanation": "", "weak_point": "asking_prices"}
    result = evaluate_item(item, "Quanto")
    assert result["is_correct"] is True


def test_fill_blank_with_spaces():
    item = {"item_type": "fill_blank", "correct_answer": "Quanto", "explanation": "", "weak_point": "asking_prices"}
    result = evaluate_item(item, "  quanto  ")
    assert result["is_correct"] is True


def test_short_answer_accepts_bill():
    item = {"item_type": "short_answer", "correct_answer": "Il conto, per favore.", "keywords": ["conto", "favore"], "explanation": "", "weak_point": "asking_for_bill"}
    result = evaluate_item(item, "Il conto, per favore.")
    assert result["is_correct"] is True


def test_incorrect_bill_has_weak_point():
    item = {"item_type": "short_answer", "correct_answer": "Il conto, per favore.", "keywords": ["conto", "favore"], "explanation": "", "weak_point": "asking_for_bill"}
    result = evaluate_item(item, "Grazie")
    assert result["is_correct"] is False
    assert result["weak_point"] == "asking_for_bill"


def test_score_calculation():
    feedbacks = [{"is_correct": True}, {"is_correct": True}, {"is_correct": False}, {"is_correct": False}]
    assert calculate_score(feedbacks) == 50
