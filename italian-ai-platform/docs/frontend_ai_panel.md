# Frontend AI Panel

## Overview

The AI tutor panel on `/units/[unitCode]` lets learners request lesson explanations and ask questions.

## Components

- `AITutorPanel` — Main panel with explain button and question input
- `LessonQuestionInput` — Text input with submit button
- `AIResponseCard` — Displays AI response with provider label

## Backend Endpoints Used

- `POST /api/ai/explain-lesson` — Get lesson explanation
- `POST /api/ai/answer-question` — Answer learner question

## Behavior

- Explain button calls explain-lesson endpoint
- Question input calls answer-question endpoint
- Empty questions are blocked client-side
- Loading state shown during API calls
- Error state shown if backend unavailable

## Provider

Currently uses `fake` provider for development. Real providers (Gemini/Groq) will be enabled when API keys are configured.

## Future Steps

- Streaming responses
- Exercise generation
- RAG/material retrieval
