# Academic Mode v1

One curriculum, two delivery modes for A1.5.

## Overview

The platform supports two study modes:
- **Daily Communication**: Practical conversation, listening, speaking, real-life interaction
- **Academic Purpose**: Structured grammar, reading comprehension, writing accuracy, exam-style practice

## Backend Study Mode Support

### Lesson API

```
GET /api/lessons/{unit_code}?study_mode=daily_communication
GET /api/lessons/{unit_code}?study_mode=academic_purpose
```

Response includes:
- `study_mode`: current mode
- `mode_label`: human-readable label
- `mode_focus`: brief focus description
- `mode_specific_guidance`: detailed guidance

### Exercise API

```json
POST /api/exercises/generate
{
  "unit_code": "A1.5",
  "study_mode": "academic_purpose"
}
```

Daily mode exercises: café vocabulary, ordering, practical questions
Academic mode exercises: article grammar, question words, negation, piacere, reading comprehension, short writing

### AI API

Both `/api/ai/explain-lesson` and `/api/ai/answer-question` accept `study_mode`.

AI context includes mode-specific guidance:
- Daily: practical conversation focus
- Academic: grammar accuracy and exam preparation focus

## Frontend Mode Selection

Access via query parameter:
- `/units/A1.5?mode=daily_communication`
- `/units/A1.5?mode=academic_purpose`

Mode selector buttons switch between modes.
Mode guidance text displays below the header.

## A1.5 Mode Behavior

### Daily Communication
- Café ordering vocabulary
- Practical listening exercises
- Speaking roleplay
- Conversational grammar

### Academic Purpose
- Article agreement practice
- Question word exercises
- Negation with piacere
- Menu reading comprehension
- Short written responses
- Exam-style instructions

## What is Postponed

- Full certification mock exams (CILS/CELI/PLIDA)
- Timed testing engine
- Official exam format simulation
- Advanced writing rubric scoring
- Adaptive difficulty
