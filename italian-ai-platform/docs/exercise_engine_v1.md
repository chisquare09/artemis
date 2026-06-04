# Exercise Engine v1

## Overview

Deterministic exercise generation and evaluation for A1.5 — Food, Café, and Restaurant.

## Supported Exercise Types

- `multiple_choice` — Select one correct answer
- `fill_blank` — Fill in the missing word
- `short_answer` — Keyword-based evaluation
- `short_writing` — Keyword-based evaluation (no AI scoring yet)

## A1.5 Coverage

- Café vocabulary (ordering food/drinks)
- Asking prices ("Quanto costa...?")
- Asking for the bill
- Negation with "non"
- Articles with food nouns
- Question words (quanto, cosa, dove)
- Introduction to piacere

## Endpoints

### POST /api/exercises/generate

Generate an exercise for a unit.

Request:
```json
{"unit_code": "A1.5", "activity_type": "quiz", "count": 5}
```

Response includes items without correct answers.

### POST /api/exercises/submit

Submit answers and receive feedback.

Request:
```json
{"exercise_id": "...", "answers": [{"item_id": "...", "answer": "..."}]}
```

Response includes score, feedback, weak points, and explanations.

## Storage

Uses in-memory store when DATABASE_URL is not configured. Exercises persist for the process lifetime only.

## Future Steps

- Frontend exercise UI (Step 10)
- AI-generated exercises
- Real writing evaluation
- Progress tracking
