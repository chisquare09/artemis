# Curriculum Import

## Overview

The Italian AI Learning Platform uses structured YAML seed data as the curriculum source. The curriculum PDF is **not parsed at runtime**. Instead, the curriculum has been manually structured into `curriculum.yaml`, which is then imported into the database.

## Seed Data Location

```
backend/app/modules/curriculum/seed_data/curriculum.yaml
```

## A1.5 Vertical Slice

Unit A1.5 (Food, Café, and Restaurant) is the first fully detailed vertical slice. It includes:
- Communicative goals
- Grammar objectives
- Vocabulary objectives
- Listening, speaking, reading, writing objectives
- Culture notes
- 7 lesson activities

## Commands

### Dry Run (Validate Without Database)

```bash
cd italian-ai-platform
python scripts/import_curriculum.py --dry-run
```

This validates the YAML structure without requiring a database connection.

### Real Import

```bash
cd italian-ai-platform
# Ensure DATABASE_URL is set
export DATABASE_URL=postgresql://user:pass@localhost:5432/italian_ai
python scripts/import_curriculum.py
```

## Import Behavior

- **Idempotent**: Running import multiple times will not create duplicates
- **Upsert logic**: Existing records are matched by code/title
- **Dry run**: Validates and reports counts without database changes
