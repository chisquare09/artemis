#!/usr/bin/env python3
"""Add standard activities to all units that don't have them."""
import yaml
from pathlib import Path

YAML_PATH = Path(__file__).parent.parent / "backend/app/modules/curriculum/seed_data/curriculum.yaml"

def make_activities(unit_code: str, unit_title: str) -> list:
    """Generate 7 standard activities for a unit."""
    return [
        {"activity_type": "intro", "title": "Lesson overview", "description": f"Understand the goals of {unit_title}", "skill_focus": "integrated", "order_index": 1},
        {"activity_type": "vocabulary", "title": "Key vocabulary", "description": f"Learn essential vocabulary for {unit_title}", "skill_focus": "reading", "order_index": 2},
        {"activity_type": "reading", "title": "Reading practice", "description": f"Read texts related to {unit_title}", "skill_focus": "reading", "order_index": 3},
        {"activity_type": "listening", "title": "Listening practice", "description": f"Listen to dialogues about {unit_title}", "skill_focus": "listening", "order_index": 4},
        {"activity_type": "speaking", "title": "Speaking roleplay", "description": f"Practice speaking scenarios for {unit_title}", "skill_focus": "speaking", "order_index": 5},
        {"activity_type": "writing", "title": "Writing exercise", "description": f"Write about topics from {unit_title}", "skill_focus": "writing", "order_index": 6},
        {"activity_type": "quiz", "title": "Review quiz", "description": f"Test your knowledge of {unit_title}", "skill_focus": "integrated", "order_index": 7},
    ]

def main():
    with open(YAML_PATH, "r") as f:
        data = yaml.safe_load(f)
    
    added = 0
    for level in data.get("levels", []):
        for unit in level.get("units", []):
            if "activities" not in unit or not unit["activities"]:
                unit["activities"] = make_activities(unit["code"], unit["title"])
                added += 1
                print(f"Added activities to {unit['code']}")
    
    with open(YAML_PATH, "w") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=1000)
    
    print(f"\nDone. Added activities to {added} units.")

if __name__ == "__main__":
    main()
