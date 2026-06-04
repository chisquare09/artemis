WAITER_TURNS = [
    {"speaker": "waiter", "text": "Buongiorno! Cosa desidera?"},
    {"speaker": "waiter", "text": "Certo. Altro?"},
    {"speaker": "waiter", "text": "Sono tre euro."},
]


def get_scenario(scenario_id: str) -> dict:
    if scenario_id != "cafe_ordering":
        return None
    return {
        "scenario_id": "cafe_ordering",
        "title": "Ordering at an Italian café",
        "system_role": "cafe_waiter",
        "learner_role": "customer",
        "waiter_turns": WAITER_TURNS,
    }


def get_next_waiter_turn(turn_index: int) -> dict | None:
    if turn_index >= len(WAITER_TURNS):
        return None
    return WAITER_TURNS[turn_index]
