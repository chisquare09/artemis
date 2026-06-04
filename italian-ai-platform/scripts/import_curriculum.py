#!/usr/bin/env python
"""Import curriculum seed data into the database."""
import argparse
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

from app.modules.curriculum.importer import load_curriculum_seed, import_curriculum_seed
from app.core.config import get_settings

SEED_PATH = Path(__file__).parent.parent / "backend/app/modules/curriculum/seed_data/curriculum.yaml"


def main():
    parser = argparse.ArgumentParser(description="Import curriculum seed data")
    parser.add_argument("--dry-run", action="store_true", help="Validate without importing")
    args = parser.parse_args()

    print(f"Loading curriculum from {SEED_PATH}")
    seed = load_curriculum_seed(SEED_PATH)
    print(f"✓ Loaded: {seed.curriculum.title}")

    if args.dry_run:
        summary = import_curriculum_seed(None, seed, dry_run=True)
        print("\n[DRY RUN] No database changes made.")
    else:
        settings = get_settings()
        if not settings.DATABASE_URL:
            print("\nERROR: DATABASE_URL is not configured. Set DATABASE_URL to import.")
            print("Use --dry-run to validate without a database.")
            sys.exit(1)

        from app.db.session import get_db
        db = next(get_db())
        summary = import_curriculum_seed(db, seed, dry_run=False)
        print("\n✓ Import complete.")

    print(f"\nSummary:")
    print(f"  Curriculum: {summary['curriculum_title']}")
    print(f"  Levels: {summary['levels_count']}")
    print(f"  Units: {summary['units_count']}")
    print(f"  Objectives: {summary['objectives_count']}")
    print(f"  Activities: {summary['activities_count']}")
    print(f"  Created: {summary['created_count']}")


if __name__ == "__main__":
    main()
