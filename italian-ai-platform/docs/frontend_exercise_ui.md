# Frontend Exercise UI

## Overview

Interactive exercise UI for A1.5 — Food, Café, and Restaurant quizzes.

## Components

- `ExerciseSet` — Main container with generate/submit flow
- `ExerciseQuestion` — Routes to correct question component
- `MultipleChoiceQuestion` — Radio button selection
- `FillBlankQuestion` — Text input
- `ShortAnswerQuestion` — Text input
- `WritingQuestion` — Textarea
- `ExerciseFeedback` — Displays score, feedback, weak points

## Endpoints Used

- `POST /api/exercises/generate` — Generate quiz
- `POST /api/exercises/submit` — Submit answers

## Supported Types

- multiple_choice
- fill_blank
- short_answer
- short_writing

## Behavior

1. User clicks "Generate quiz"
2. 5 questions render (correct answers hidden)
3. User answers questions
4. User clicks "Submit answers"
5. Score, feedback, and explanations display

Missing answers are submitted as empty strings and marked incorrect by backend.

## Future Steps

- Progress tracking
- AI-generated exercises
- Listening and speaking modules
