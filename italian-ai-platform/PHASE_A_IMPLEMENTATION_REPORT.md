# Plan Phase A Implementation Report

## Completed

- Expanded frontend navigation from the A1.5-only vertical slice to curriculum-driven A1, A2, B1, and B2 level/unit pages.
- Preserved the existing A1.5 lesson, quiz, listening, speaking, materials, and progress behavior.
- Added shared backend curriculum unit validation so valid units are resolved from `curriculum.yaml` instead of hard-coded `A1.5` checks.
- Expanded progress, materials, RAG retrieval, quizzes, listening practice, and speaking roleplay to all valid curriculum units.
- Implemented the Gemini provider and provider selection so `GEMINI_API_KEY` activates Gemini on the backend.
- Kept fake AI fallback when Gemini is not configured.
- Removed the build-time Google font dependency so frontend builds do not fail in offline/locked-down environments.
- Added backend regression coverage for non-A1.5 units and Gemini provider activation.

## Files changed

### Backend

- `backend/requirements.txt`
- `backend/app/core/config.py`
- `backend/app/modules/curriculum/unit_catalog.py`
- `backend/app/modules/ai/service.py`
- `backend/app/modules/ai/providers/gemini_provider.py`
- `backend/app/modules/exercises/service.py`
- `backend/app/modules/exercises/generator.py`
- `backend/app/modules/listening/service.py`
- `backend/app/modules/listening/evaluator.py`
- `backend/app/modules/speaking/service.py`
- `backend/app/modules/speaking/roleplay_engine.py`
- `backend/app/modules/speaking/evaluator.py`
- `backend/app/modules/materials/service.py`
- `backend/app/modules/rag/service.py`
- `backend/app/modules/progress/service.py`
- `backend/app/tests/test_ai_api.py`
- `backend/app/tests/test_ai_provider.py`
- `backend/app/tests/test_exercise_api.py`
- `backend/app/tests/test_listening_api.py`
- `backend/app/tests/test_materials_api.py`
- `backend/app/tests/test_progress_api.py`
- `backend/app/tests/test_rag_api.py`
- `backend/app/tests/test_speaking_api.py`

### Frontend

- `frontend/src/app/layout.tsx`
- `frontend/src/app/globals.css`
- `frontend/src/app/page.tsx`
- `frontend/src/app/levels/[levelId]/page.tsx`
- `frontend/src/app/units/[unitCode]/page.tsx`
- `frontend/src/app/modes/[modeId]/page.tsx`
- `frontend/src/app/progress/page.tsx`
- `frontend/src/app/review/page.tsx`
- `frontend/src/types/curriculum.ts`
- `frontend/src/services/curriculum-service.ts`
- `frontend/src/services/speaking-service.ts`
- `frontend/src/features/speaking/SpeakingRoleplay.tsx`

## Tests run

From `backend/`:

```bash
python3 -m pytest app/tests -q
```

Result:

```text
194 passed, 4 warnings
```

From `frontend/`:

```bash
npm run lint
npm run build
```

Result:

```text
lint passed
build passed
```

## Notes

- `backend/requirements.txt` now uses `httpx==0.28.1` because `google-genai==1.54.0` requires `httpx>=0.28.1`.
- The frontend pages that call backend APIs are marked as dynamic server-rendered routes so Vercel builds do not depend on live backend data at build time.
- Generic quizzes/listening/speaking for non-A1.5 units are deterministic and curriculum-based. They do not call Gemini, which keeps tests stable.
- Gemini is used by the AI Tutor provider path when `GEMINI_API_KEY` is present.
