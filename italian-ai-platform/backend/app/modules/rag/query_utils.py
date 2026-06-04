import re

QUERY_EXPANSION = {
    "bill": "conto",
    "price": "prezzo",
    "cost": "costa",
    "coffee": "caffè",
    "cappuccino": "cappuccino",
    "croissant": "cornetto",
    "please": "per favore",
    "menu": "menu",
    "water": "acqua",
}


def normalize(text: str) -> list[str]:
    t = text.lower()
    t = re.sub(r"[^\w\s]", " ", t)
    return [w for w in t.split() if w]


def expand_query(terms: list[str]) -> list[str]:
    expanded = set(terms)
    for term in terms:
        if term in QUERY_EXPANSION:
            expanded.add(QUERY_EXPANSION[term])
    return list(expanded)
