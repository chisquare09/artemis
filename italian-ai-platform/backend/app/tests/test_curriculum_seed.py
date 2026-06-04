from pathlib import Path

from app.modules.curriculum.importer import load_curriculum_seed

SEED_PATH = Path(__file__).parent.parent / "modules/curriculum/seed_data/curriculum.yaml"


def test_curriculum_yaml_loads():
    seed = load_curriculum_seed(SEED_PATH)
    assert seed is not None


def test_curriculum_title():
    seed = load_curriculum_seed(SEED_PATH)
    assert seed.curriculum.title == "Full Italian Curriculum A1 to B2"


def test_a1_level_exists():
    seed = load_curriculum_seed(SEED_PATH)
    codes = [l.code for l in seed.levels]
    assert "A1" in codes


def test_a1_units_exist():
    seed = load_curriculum_seed(SEED_PATH)
    a1 = next(l for l in seed.levels if l.code == "A1")
    unit_codes = [u.code for u in a1.units]
    for i in range(1, 11):
        expected = f"A1.{i}"
        assert expected in unit_codes, f"{expected} not found"


def test_a1_5_exists():
    seed = load_curriculum_seed(SEED_PATH)
    a1 = next(l for l in seed.levels if l.code == "A1")
    a1_5 = next((u for u in a1.units if u.code == "A1.5"), None)
    assert a1_5 is not None


def test_a1_5_title():
    seed = load_curriculum_seed(SEED_PATH)
    a1 = next(l for l in seed.levels if l.code == "A1")
    a1_5 = next(u for u in a1.units if u.code == "A1.5")
    assert a1_5.title == "Food, Café, and Restaurant"


def test_a1_5_has_communicative_goals():
    seed = load_curriculum_seed(SEED_PATH)
    a1 = next(l for l in seed.levels if l.code == "A1")
    a1_5 = next(u for u in a1.units if u.code == "A1.5")
    comm_goals = [o for o in a1_5.objectives if o.type == "communicative_goal"]
    assert len(comm_goals) >= 1


def test_a1_5_has_grammar():
    seed = load_curriculum_seed(SEED_PATH)
    a1 = next(l for l in seed.levels if l.code == "A1")
    a1_5 = next(u for u in a1.units if u.code == "A1.5")
    grammar = [o for o in a1_5.objectives if o.type == "grammar"]
    assert len(grammar) >= 1


def test_a1_5_has_vocabulary():
    seed = load_curriculum_seed(SEED_PATH)
    a1 = next(l for l in seed.levels if l.code == "A1")
    a1_5 = next(u for u in a1.units if u.code == "A1.5")
    vocab = [o for o in a1_5.objectives if o.type == "vocabulary"]
    assert len(vocab) >= 1


def test_a1_5_has_skills():
    seed = load_curriculum_seed(SEED_PATH)
    a1 = next(l for l in seed.levels if l.code == "A1")
    a1_5 = next(u for u in a1.units if u.code == "A1.5")
    types = {o.type for o in a1_5.objectives}
    assert "listening" in types
    assert "speaking" in types
    assert "reading" in types
    assert "writing" in types


def test_a1_5_has_culture():
    seed = load_curriculum_seed(SEED_PATH)
    a1 = next(l for l in seed.levels if l.code == "A1")
    a1_5 = next(u for u in a1.units if u.code == "A1.5")
    culture = [o for o in a1_5.objectives if o.type == "culture"]
    assert len(culture) >= 1


def test_a1_5_has_seven_activities():
    seed = load_curriculum_seed(SEED_PATH)
    a1 = next(l for l in seed.levels if l.code == "A1")
    a1_5 = next(u for u in a1.units if u.code == "A1.5")
    assert len(a1_5.activities) == 7


def test_validation_passes():
    seed = load_curriculum_seed(SEED_PATH)
    assert seed.curriculum.version == "0.2.0"
