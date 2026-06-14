CAFE_VOCABULARY = ["caffè", "caffe", "cappuccino", "cornetto", "acqua", "tè", "te", "panino", "coffee", "croissant"]
POLITE_PHRASES = ["per favore", "grazie", "buongiorno", "prego"]
ORDERING_PHRASES = ["vorrei", "prendo", "mi dia"]
PRICE_PHRASES = ["quanto costa", "quanto"]
BILL_PHRASES = ["il conto", "conto"]
LIKE_PHRASES = ["mi piace", "non mi piace"]
GENERIC_ITALIAN_MARKERS = [
    "ciao",
    "buongiorno",
    "grazie",
    "sono",
    "vorrei",
    "posso",
    "studio",
    "parlo",
    "mi piace",
    "perché",
    "oggi",
]


def evaluate_response(text: str, context: dict | None = None) -> dict:
    if context and context.get("scenario_id") == "unit-default":
        return evaluate_generic_response(text, context)

    t = text.lower()
    weak_points = []

    has_vocab = any(w in t for w in CAFE_VOCABULARY)
    has_polite = any(p in t for p in POLITE_PHRASES)
    has_order = any(o in t for o in ORDERING_PHRASES)
    has_price = any(p in t for p in PRICE_PHRASES)
    has_bill = any(b in t for b in BILL_PHRASES)

    if not has_vocab and not has_price and not has_bill:
        weak_points.append("cafe_vocabulary")
    if not has_polite:
        weak_points.append("polite_phrases")
    if not has_order and not has_price and not has_bill:
        weak_points.append("ordering_phrase")

    is_appropriate = len(weak_points) < 2

    if is_appropriate:
        message = "Good response! You used appropriate café language."
    else:
        message = "Try to include ordering phrases (Vorrei...) and polite words (per favore, grazie)."

    return {
        "is_appropriate": is_appropriate,
        "message": message,
        "weak_points": weak_points,
        "has_vocab": has_vocab,
        "has_polite": has_polite,
        "has_order": has_order,
        "has_price": has_price,
        "has_bill": has_bill,
    }


def evaluate_generic_response(text: str, context: dict) -> dict:
    t = text.lower().strip()
    weak_points = []
    title = context.get("title", "this unit")
    objective_keywords = context.get("objective_keywords", [])

    has_italian_marker = any(marker in t for marker in GENERIC_ITALIAN_MARKERS)
    has_unit_keyword = any(keyword in t for keyword in objective_keywords)
    has_minimum_length = len(t.split()) >= 3

    if not has_minimum_length:
        weak_points.append("speaking_sentence_length")
    if not has_italian_marker:
        weak_points.append("basic_italian_response")
    if objective_keywords and not has_unit_keyword:
        weak_points.append("unit_topic_vocabulary")

    is_appropriate = len(weak_points) <= 1
    message = (
        f"Good response for {title}. Keep connecting your answer to the lesson topic."
        if is_appropriate
        else "Try to write a fuller Italian sentence and include vocabulary from the unit topic."
    )

    return {
        "is_appropriate": is_appropriate,
        "message": message,
        "weak_points": weak_points,
        "has_vocab": has_unit_keyword,
        "has_polite": any(p in t for p in POLITE_PHRASES),
        "has_order": False,
        "has_price": False,
        "has_bill": False,
    }


def calculate_finish_score(feedbacks: list[dict]) -> int:
    if not feedbacks:
        return 0
    appropriate = sum(1 for f in feedbacks if f["is_appropriate"])
    return round(appropriate / len(feedbacks) * 100)


def collect_all_weak_points(feedbacks: list[dict]) -> list[str]:
    all_wp = set()
    for f in feedbacks:
        for wp in f.get("weak_points", []):
            all_wp.add(wp)
    return list(all_wp)
