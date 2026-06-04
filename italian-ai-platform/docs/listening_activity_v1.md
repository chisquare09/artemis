# Listening Activity v1

## Overview

Deterministic transcript-based listening activity for A1.5 — Food, Café, and Restaurant.

## A1.5 Café Dialogue Transcript

```
Cameriere: Buongiorno, desidera?
Cliente: Vorrei un cappuccino e un cornetto, per favore.
Cameriere: Altro?
Cliente: No, grazie. Quanto costa?
Cameriere: Sono tre euro.
```

## Endpoints

### GET /api/listening/units/{unit_code}

Returns listening task with transcript, questions (no correct answers exposed).

### POST /api/listening/submit

Submits answers and returns score, feedback, weak points.

## Questions

1. What does the customer order? (cappuccino and cornetto)
2. How much does it cost? (tre euro / 3 euro)
3. Which polite phrase is used? (per favore)

## Evaluation Rules

- Question 1: Must include both "cappuccino" and "cornetto"
- Question 2: Accepts "tre euro", "3 euro", "three euro"
- Question 3: Accepts "per favore"

## Weak Points

- `listening_cafe_order` — incorrect order items
- `listening_prices` — incorrect price
- `polite_phrases` — missing polite phrase

## Frontend Behavior

- Transcript hidden by default
- Show/Hide transcript toggle
- Submit answers to get feedback

## Future Steps

- Real audio playback
- YouTube/video ingestion
- Speech recognition
- Speaking roleplay
