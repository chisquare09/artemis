from app.modules.listening.evaluator import evaluate_answer, calculate_score, A1_5_QUESTIONS


def test_cappuccino_cornetto_correct():
    q = A1_5_QUESTIONS[0]
    result = evaluate_answer(q, "cappuccino and cornetto")
    assert result["is_correct"] is True


def test_missing_one_item_incorrect():
    q = A1_5_QUESTIONS[0]
    result = evaluate_answer(q, "cappuccino")
    assert result["is_correct"] is False


def test_tre_euro_accepted():
    q = A1_5_QUESTIONS[1]
    assert evaluate_answer(q, "tre euro")["is_correct"] is True


def test_3_euro_accepted():
    q = A1_5_QUESTIONS[1]
    assert evaluate_answer(q, "3 euro")["is_correct"] is True


def test_per_favore_accepted():
    q = A1_5_QUESTIONS[2]
    assert evaluate_answer(q, "per favore")["is_correct"] is True


def test_score_calculation():
    feedbacks = [{"is_correct": True}, {"is_correct": True}, {"is_correct": False}]
    assert calculate_score(feedbacks) == 67


def test_weak_point_on_incorrect():
    q = A1_5_QUESTIONS[1]
    result = evaluate_answer(q, "wrong")
    assert result["weak_point"] == "listening_prices"
