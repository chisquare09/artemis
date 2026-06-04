from app.modules.speaking.evaluator import evaluate_response, calculate_finish_score


def test_response_with_vorrei_per_favore_is_appropriate():
    result = evaluate_response("Vorrei un caffè, per favore.")
    assert result["is_appropriate"] is True


def test_response_without_polite_phrase():
    result = evaluate_response("Vorrei un caffè")
    assert "polite_phrases" in result["weak_points"]


def test_response_without_cafe_vocabulary():
    result = evaluate_response("Grazie mille")
    assert "cafe_vocabulary" in result["weak_points"]


def test_quanto_costa_detected():
    result = evaluate_response("Quanto costa?")
    assert result["has_price"] is True


def test_il_conto_detected():
    result = evaluate_response("Il conto, per favore.")
    assert result["has_bill"] is True


def test_finish_score_calculation():
    feedbacks = [{"is_appropriate": True}, {"is_appropriate": True}, {"is_appropriate": False}]
    assert calculate_finish_score(feedbacks) == 67
