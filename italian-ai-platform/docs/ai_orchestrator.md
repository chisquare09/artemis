# AI Orchestrator

## Overview

All AI calls in the Italian AI Learning Platform go through the centralized AI orchestrator. This ensures consistent prompt handling, lesson context injection, and provider abstraction.

## Provider Abstraction

Base interface in `providers/base.py`:
- `generate_text(prompt, context)` → str
- `generate_json(prompt, schema_hint, context)` → dict

### Available Providers

| Provider | Status | Notes |
|----------|--------|-------|
| FakeAIProvider | Active | Deterministic responses for dev/test |
| GeminiProvider | Placeholder | Requires GEMINI_API_KEY |
| GroqProvider | Placeholder | Requires GROQ_API_KEY |
| FallbackAIProvider | Active | Chains multiple providers |

### FakeAIProvider

Returns deterministic responses for development and testing. No API keys required.

For A1.5 explain-lesson, returns text mentioning:
- ordering food and drinks
- asking prices
- asking for the bill
- expressing likes and dislikes

### Provider Selection

Default behavior in `service.py`:
- Uses FakeAIProvider by default
- Real providers (Gemini/Groq) will be enabled when API keys are configured

## Endpoints

### POST /api/ai/explain-lesson

Request:
```json
{"unit_code": "A1.5", "study_mode": "daily-communication"}
```

Response:
```json
{
  "unit_code": "A1.5",
  "provider": "fake",
  "explanation": "This is A1.5 — Food, Café, and Restaurant...",
  "used_context": {"unit_code": "A1.5", "level": "A1", ...}
}
```

### POST /api/ai/answer-question

Request:
```json
{"unit_code": "A1.5", "question": "How do I ask for the bill?"}
```

Response:
```json
{
  "unit_code": "A1.5",
  "provider": "fake",
  "answer": "For A1.5, regarding your question...",
  "used_context": {...}
}
```

## Why Use the Orchestrator?

- Centralizes prompt template loading
- Injects lesson context automatically
- Abstracts provider selection
- Enables testing with FakeAIProvider
- Prepares for future features (RAG, exercise generation)

## Future Steps

- Frontend AI panel (Step 8+)
- Exercise generation
- Writing evaluation
- RAG/material retrieval
- Streaming responses
