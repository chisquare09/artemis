# Curriculum and Lesson APIs

## Overview

Backend APIs for retrieving curriculum structure and lesson details.

## Endpoints

### GET /api/curriculum

Returns curriculum overview with levels and study modes.

### GET /api/levels

Returns all levels ordered by order_index.

### GET /api/levels/{level_code}

Returns one level by code.

### GET /api/levels/{level_code}/units

Returns units for a level ordered by order_index.

### GET /api/units/{unit_code}

Returns unit detail with grouped objectives and activities.

### GET /api/lessons/{unit_code}

Returns full lesson detail for a unit.

## Example: GET /api/lessons/A1.5

```json
{
  "level": "A1",
  "unit_code": "A1.5",
  "title": "Food, Café, and Restaurant",
  "summary": "Learn to order food and drinks...",
  "objectives": {
    "communicative_goal": ["Order food and drinks", "Ask for prices", ...],
    "grammar": ["Present tense regular verbs: -are", ...],
    "vocabulary": ["Food", "Drinks", ...],
    "listening": ["Understand café orders", ...],
    "speaking": ["Order at a café", ...],
    "reading": ["Read a menu"],
    "writing": ["Write a short food preference paragraph"],
    "culture": ["Italian café culture", ...]
  },
  "activities": [
    {"activity_type": "intro", "title": "Lesson overview", ...},
    {"activity_type": "vocabulary", "title": "Food and café vocabulary", ...},
    ...
  ],
  "progress": {
    "completion_percentage": 0,
    "mastery_score": null,
    "status": "not_started"
  },
  "ai_helper_context": {
    "unit_code": "A1.5",
    "level": "A1",
    "title": "Food, Café, and Restaurant",
    "summary": "...",
    "objective_types": ["communicative_goal", "grammar", ...],
    "note": "AI tutor will use this lesson context in a later step"
  }
}
```

## Notes

- Progress and AI helper fields are placeholders for now
- Frontend integration happens in a later step
- Data is read from curriculum.yaml seed file
