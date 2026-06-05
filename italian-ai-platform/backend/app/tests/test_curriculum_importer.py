from pathlib import Path

from app.modules.curriculum.importer import load_curriculum_seed, import_curriculum_seed

SEED_PATH = Path(__file__).parent.parent / "modules/curriculum/seed_data/curriculum.yaml"


def test_load_returns_validated_model():
    seed = load_curriculum_seed(SEED_PATH)
    assert seed.curriculum.title is not None
    assert len(seed.levels) > 0


def test_dry_run_returns_summary():
    seed = load_curriculum_seed(SEED_PATH)
    summary = import_curriculum_seed(None, seed, dry_run=True)
    assert summary["dry_run"] is True
    assert "curriculum_title" in summary


def test_dry_run_no_database_required():
    seed = load_curriculum_seed(SEED_PATH)
    summary = import_curriculum_seed(None, seed, dry_run=True)
    assert summary is not None


def test_summary_includes_counts():
    seed = load_curriculum_seed(SEED_PATH)
    summary = import_curriculum_seed(None, seed, dry_run=True)
    assert "levels_count" in summary
    assert "units_count" in summary
    assert "objectives_count" in summary
    assert "activities_count" in summary
    assert summary["levels_count"] == 4
    assert summary["units_count"] == 44
    assert summary["activities_count"] == 308


def test_importer_summary_values():
    seed = load_curriculum_seed(SEED_PATH)
    summary = import_curriculum_seed(None, seed, dry_run=True)
    assert summary["curriculum_title"] == "Full Italian Curriculum A1 to B2"
    assert summary["objectives_count"] > 0
