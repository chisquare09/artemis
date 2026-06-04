CAFE_VOCABULARY = ["caffè", "caffe", "cappuccino", "cornetto", "acqua", "tè", "te", "panino", "coffee", "croissant"]
POLITE_PHRASES = ["per favore", "grazie", "buongiorno", "prego"]
ORDERING_PHRASES = ["vorrei", "prendo", "mi dia"]
PRICE_PHRASES = ["quanto costa", "quanto"]
BILL_PHRASES = ["il conto", "conto"]
LIKE_PHRASES = ["mi piace", "non mi piace"]


def evaluate_response(text: str) -> dict:
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
