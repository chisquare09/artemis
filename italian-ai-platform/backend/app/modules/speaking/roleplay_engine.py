from app.modules.curriculum.unit_catalog import ensure_unit_exists

WAITER_TURNS = [
    {"speaker": "waiter", "text": "Buongiorno! Cosa desidera?"},
    {"speaker": "waiter", "text": "Certo. Altro?"},
    {"speaker": "waiter", "text": "Sono tre euro."},
]


def _build_generic_turns(unit_code: str) -> list[dict]:
    unit = ensure_unit_exists(unit_code)
    objective_values = [item for items in unit.objectives.values() for item in items]
    first_objective = objective_values[0] if objective_values else unit.title
    return [
        {"speaker": "tutor", "text": f"Ciao! Parliamo di {unit.title}. Puoi iniziare con una frase semplice?"},
        {"speaker": "tutor", "text": f"Bene. Ora aggiungi un dettaglio su questo obiettivo: {first_objective}."},
        {"speaker": "tutor", "text": "Ottimo. Concludi con una frase finale in italiano."},
    ]


def get_scenario(scenario_id: str, unit_code: str | None = None) -> dict | None:
    if scenario_id == "cafe_ordering":
        return {
            "scenario_id": "cafe_ordering",
            "title": "Ordering at an Italian café",
            "system_role": "cafe_waiter",
            "learner_role": "customer",
            "waiter_turns": WAITER_TURNS,
        }

    if scenario_id == "unit-default" and unit_code:
        unit = ensure_unit_exists(unit_code)
        return {
            "scenario_id": "unit-default",
            "title": f"Practice conversation for {unit.title}",
            "system_role": "italian_tutor",
            "learner_role": "italian_learner",
            "waiter_turns": _build_generic_turns(unit_code),
        }

    return None


def get_next_waiter_turn(turn_index: int, turns: list[dict] | None = None) -> dict | None:
    scenario_turns = turns or WAITER_TURNS
    if turn_index >= len(scenario_turns):
        return None
    return scenario_turns[turn_index]
