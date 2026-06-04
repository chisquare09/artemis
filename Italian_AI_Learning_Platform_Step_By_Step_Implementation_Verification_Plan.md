# Italian AI Learning Platform — Step-by-Step Implementation & Verification Plan

## Purpose of this document

This document is the **implementation control plan** for the Italian AI Learning Platform. It is designed to be used after each implementation step so an AI coding assistant can double-check whether the implementation follows the agreed architecture, scope, and finish criteria.

Use this document in this workflow:

1. Give the coding agent one implementation step prompt.
2. The coding agent implements only that step.
3. The coding agent runs tests.
4. The coding agent returns an implementation report.
5. Compare the report against this plan.
6. If the step passes, continue to the next step.
7. If the step fails, ask the coding agent to fix only the failed items.

---

## Core product goal

Build a personal, cloud-hosted Italian learning website with:

- structured curriculum-driven learning
- two study modes: Daily Communication and Academic Purpose / Certification Preparation
- integrated 4-skill learning: listening, reading, writing, speaking
- AI tutor for lesson explanation and Q&A
- exercise generation, scoring, and explanation
- progress tracking and review planning
- learning material support from PDFs, websites, and video transcripts

The platform is **personal-first**, but the codebase must remain clean enough to support multiple users in the future.

---

## Architecture principles

### 1. Modular monolith first

Use one frontend app, one backend app, one database, and clean internal modules. Do not start with microservices.

### 2. Curriculum-first

The curriculum defines what to learn. The platform defines how it is delivered. The AI enriches, explains, practices, and evaluates the lesson.

### 3. One unit equals one lesson container

A curriculum unit becomes one lesson page with multiple integrated activities.

### 4. AI through orchestrator only

No random direct Gemini/Groq calls from routes, React components, or unrelated services. All AI calls must pass through the AI module and provider abstraction.

### 5. User-state tables must include user_id

Even though the first version is for one user, all progress, attempts, review, and chat tables must be user-scoped.

### 6. Build one vertical slice first

The first full working unit should be **A1.5 — Food, Café, and Restaurant**.

---

## Target repository structure

```text
italian-ai-platform/
├── frontend/
├── backend/
├── packages/
│   ├── shared-types/
│   └── shared-config/
├── docs/
├── scripts/
├── .github/
│   └── workflows/
├── README.md
├── .gitignore
└── .env.example
```

---

## Target frontend structure

```text
frontend/
├── src/
│   ├── app/
│   ├── components/
│   ├── features/
│   ├── hooks/
│   ├── lib/
│   ├── services/
│   ├── styles/
│   └── types/
```

Expected frontend pages:

- `/`
- `/modes`
- `/modes/[modeId]`
- `/levels/[levelId]`
- `/units/[unitCode]`
- `/progress`
- `/review`
- `/settings`

---

## Target backend structure

```text
backend/
├── app/
│   ├── main.py
│   ├── core/
│   ├── db/
│   ├── modules/
│   ├── shared/
│   └── tests/
```

Expected backend modules:

```text
modules/
├── auth/
├── curriculum/
├── study_modes/
├── levels/
├── units/
├── lessons/
├── materials/
├── rag/
├── ai/
├── exercises/
├── progress/
├── review/
├── listening/
├── speaking/
└── users/
```

---

# Step-by-step implementation plan

## Step 0 — Repository initialization and project skeleton

### Goal
Create the monorepo, frontend skeleton, backend skeleton, and basic health endpoint.

### What to implement

- Root monorepo folders
- Next.js TypeScript frontend with Tailwind
- FastAPI backend
- `GET /health`
- root README
- `.env.example`
- minimal backend test

### How to implement

- Keep business logic out of this step.
- Create folders and basic bootstrapping only.
- Ensure both frontend and backend can start independently.

### Finish criteria

- Frontend app starts.
- Backend app starts.
- `GET /health` returns `{ "status": "ok", "service": "italian-ai-platform-api" }`.
- Backend health test passes.
- No Supabase, AI, database, curriculum, exercise, or progress logic exists yet.

### Verification checklist

- [ ] Root monorepo structure exists.
- [ ] Frontend Next.js app exists.
- [ ] Backend FastAPI app exists.
- [ ] `/health` endpoint works.
- [ ] Backend test passes.
- [ ] No unrelated business logic added.

---

## Step 1 — Backend foundation and configuration

### Goal
Prepare backend foundation for future modules.

### What to implement

- `backend/app/core/config.py`
- `backend/app/core/logging.py`
- `backend/app/core/exceptions.py`
- `backend/app/core/dependencies.py`
- `backend/app/shared/enums.py`
- root endpoint `/`
- CORS setup
- tests for config, enums, exceptions, root endpoint, health endpoint

### How to implement

- Use Pydantic settings or `pydantic-settings`.
- Keep configuration centralized.
- Add placeholder `get_current_user_id()` returning `dev-user`.
- Add string enums for study mode, CEFR level, skill, and objective type.
- Add reusable exception shape:

```json
{
  "error": {
    "code": "...",
    "message": "..."
  }
}
```

### Finish criteria

- Settings load correctly.
- CORS is configured.
- Exceptions return standard JSON format.
- Shared enums exist.
- Backend tests pass.
- No database, Supabase, AI, or curriculum logic added.

### Verification checklist

- [ ] `config.py` exists.
- [ ] `logging.py` exists.
- [ ] `exceptions.py` exists.
- [ ] `dependencies.py` exists.
- [ ] `enums.py` exists.
- [ ] `/health` still works.
- [ ] `/` returns service and environment.
- [ ] Backend tests pass.

---

## Step 2 — Frontend foundation and design shell

### Goal
Create the first usable website shell with navigation, reusable UI components, and placeholder pages.

### What to implement

- App shell
- Main navigation
- UI components: Card, Button, ProgressBar, Badge, SectionHeader
- Placeholder pages:
  - dashboard
  - modes
  - mode detail
  - level detail
  - unit detail
  - progress
  - review
  - settings
- Type files
- Placeholder API client

### How to implement

- Keep the UI clean, minimal, and card-based.
- Do not connect backend APIs yet.
- Hardcode A1 and A1.5 placeholder content for now.

### Finish criteria

- All target routes render.
- A1.5 unit page displays objectives and activities.
- Frontend build passes.
- No backend integration, Supabase, AI, or real persistence added.

### Verification checklist

- [ ] App shell exists.
- [ ] Main navigation exists.
- [ ] Dashboard renders.
- [ ] Modes render.
- [ ] A1 level page renders.
- [ ] A1.5 page renders.
- [ ] Progress/review/settings pages render.
- [ ] Frontend build passes.

---

## Step 3 — Database schema v1

### Goal
Create SQLAlchemy database foundation, ORM models, and Alembic setup.

### What to implement

Database model groups:

1. Curriculum models
   - Curriculum
   - StudyMode
   - Level
   - Unit
   - UnitObjective
   - LessonActivity

2. Material models
   - Material
   - MaterialSource
   - MaterialChunk
   - UnitMaterialLink

3. Exercise models
   - Exercise
   - ExerciseItem
   - ExerciseAttempt
   - ExerciseFeedback

4. Progress models
   - UserProfile
   - UserUnitProgress
   - UserActivityProgress
   - UserSkillProgress
   - MistakeLog
   - ReviewQueueItem

5. AI/chat models
   - ChatSession
   - ChatMessage
   - GeneratedContentCache

### How to implement

- Use SQLAlchemy.
- Use Alembic migrations.
- Use UUID primary keys where practical.
- Use JSON type for JSON fields to preserve SQLite/test compatibility.
- Add `created_at` and `updated_at` where practical.
- Add `user_id` to all user-learning-state models.
- Avoid Supabase Auth integration for now.

### Finish criteria

- SQLAlchemy base exists.
- Session setup exists.
- All model groups exist.
- Alembic is configured.
- Initial migration exists.
- Model import tests pass.
- Metadata tests pass.
- No seed data or APIs added yet.

### Verification checklist

- [ ] Curriculum models exist.
- [ ] Material models exist.
- [ ] Exercise models exist.
- [ ] Progress models exist.
- [ ] Chat models exist.
- [ ] User-learning-state tables include `user_id`.
- [ ] Alembic configured.
- [ ] Initial migration created.
- [ ] Tests pass.

---

## Step 4 — Curriculum seed format and importer

### Goal
Convert curriculum into structured YAML and import at least A1 + detailed A1.5.

### What to implement

- `backend/app/modules/curriculum/seed_data/curriculum.yaml`
- Curriculum importer
- Curriculum schemas
- Import script: `scripts/import_curriculum.py`
- Tests for YAML loading, A1.5 existence, validation, importer dry-run

### How to implement

- Do not parse the PDF dynamically at runtime.
- Treat YAML as structured source data.
- Seed A1 minimal units A1.1 to A1.10.
- Add full detailed A1.5 data.

### A1.5 required content

A1.5 — Food, Café, and Restaurant

Communicative goals:
- Order food and drinks
- Ask for prices
- Ask for the bill
- Express likes and dislikes

Grammar:
- Present tense regular verbs: -are
- Introduction to piacere
- Articles with food nouns
- Basic negation: non
- Questions with quanto, cosa, dove

Vocabulary:
- Food
- Drinks
- Café items
- Restaurant phrases
- Prices

Listening:
- Understand café orders
- Recognize prices

Speaking:
- Order at a café
- Ask for the bill
- Say what you like

Reading:
- Read a menu

Writing:
- Write a short food preference paragraph

Culture:
- Italian café culture
- Breakfast and meal habits

### Finish criteria

- Curriculum YAML exists.
- Importer validates data.
- A1.5 contains all required categories.
- Importer is safe to run repeatedly.
- No curriculum APIs yet.

### Verification checklist

- [ ] `curriculum.yaml` exists.
- [ ] A1 level exists.
- [ ] A1.1 to A1.10 exist.
- [ ] A1.5 is detailed.
- [ ] Importer dry-run works.
- [ ] Tests pass.

---

## Step 5 — Curriculum and lesson APIs

### Goal
Expose curriculum and lesson retrieval APIs.

### What to implement

Endpoints:

- `GET /api/curriculum`
- `GET /api/levels`
- `GET /api/levels/{level_code}`
- `GET /api/levels/{level_code}/units`
- `GET /api/units/{unit_code}`
- `GET /api/lessons/{unit_code}`

Lesson module:

- router
- schema
- service
- content_builder

### How to implement

- Use database-backed curriculum records.
- Return grouped objectives.
- Return lesson activities.
- Include progress placeholder only.
- Include AI helper context placeholder only.

### Finish criteria

- A1.5 lesson payload works.
- Invalid unit returns 404.
- Tests cover levels, units, and lesson payload.
- No AI calls yet.
- No real progress yet.

### Verification checklist

- [ ] Curriculum router exists.
- [ ] Lesson module exists.
- [ ] `/api/levels` returns A1.
- [ ] `/api/units/A1.5` works.
- [ ] `/api/lessons/A1.5` returns grouped objectives.
- [ ] Tests pass.

---

## Step 6 — Connect frontend to lesson APIs

### Goal
Render real A1.5 lesson data from the backend.

### What to implement

- frontend curriculum service
- frontend lesson service
- update `/units/[unitCode]`
- loading state
- error state

### How to implement

- Use the existing API client.
- Fetch `GET /api/lessons/{unitCode}`.
- Render objectives grouped by type.
- Render activities from API payload.

### Finish criteria

- A1.5 frontend page uses backend lesson payload.
- Loading/error states exist.
- No AI behavior yet.
- No exercise submission yet.

### Verification checklist

- [ ] Frontend calls lesson API.
- [ ] A1.5 data renders from backend.
- [ ] Loading state works.
- [ ] Error state works.
- [ ] Frontend build passes.

---

## Step 7 — AI provider abstraction

### Goal
Create AI module with provider abstraction and fake provider for tests.

### What to implement

- AI router
- AI schema
- AI service
- AI orchestrator
- provider base
- fake provider
- Gemini provider placeholder/implementation
- Groq provider placeholder/implementation
- fallback provider
- prompt files

### How to implement

- All AI usage goes through orchestrator.
- Fake provider must work without API keys.
- Gemini/Groq should fail gracefully if keys are missing.

### Finish criteria

- `POST /api/ai/explain-lesson` works with fake provider.
- Missing API keys do not crash app.
- Tests pass.
- No exercise generation logic yet beyond placeholders.

### Verification checklist

- [ ] AI module exists.
- [ ] Provider abstraction exists.
- [ ] Fake provider works.
- [ ] Explain lesson endpoint works.
- [ ] Tests pass.

---

## Step 8 — Lesson AI panel frontend

### Goal
Add AI tutor panel to the lesson page.

### What to implement

- AI tutor frontend feature
- Explain lesson button
- Ask question input
- AI response display
- loading/error states

### How to implement

- Use backend AI endpoints.
- Use fake provider if no real AI key exists.
- Keep UI simple.

### Finish criteria

- A1.5 page has AI panel.
- Explain lesson returns response.
- Empty question is blocked.
- Errors display friendly message.

### Verification checklist

- [ ] AI panel renders.
- [ ] Explain button works.
- [ ] Question input works.
- [ ] Loading/error states exist.
- [ ] Frontend build passes.

---

## Step 9 — Exercise engine v1

### Goal
Generate and evaluate deterministic A1.5 exercises.

### What to implement

Exercise types:

- multiple_choice
- fill_blank
- short_answer
- short_writing

Endpoints:

- `POST /api/exercises/generate`
- `POST /api/exercises/submit`

### How to implement

- Use deterministic generator first.
- Cover A1.5 café vocabulary, prices, negation, articles, question words, and `piacere` basics.
- Store attempts if DB is configured.
- Provide dev fallback if DB is unavailable.

### Finish criteria

- A1.5 quiz can be generated.
- Answers can be submitted.
- Score, feedback, weak points, explanations are returned.
- Tests cover correct and incorrect answers.

### Verification checklist

- [ ] Exercise module exists.
- [ ] Generate endpoint works.
- [ ] Submit endpoint works.
- [ ] Feedback includes explanations.
- [ ] Weak points detected.
- [ ] Tests pass.

---

## Step 10 — Exercise frontend

### Goal
Allow user to generate, complete, submit, and review exercises from A1.5 page.

### What to implement

- ExerciseSet
- ExerciseQuestion
- MultipleChoiceQuestion
- FillBlankQuestion
- ShortAnswerQuestion
- WritingQuestion
- ExerciseFeedback

### How to implement

- Add Generate Quiz button.
- Render questions.
- Submit answers.
- Show score and explanations.

### Finish criteria

- Quiz generation works from UI.
- User can answer and submit.
- Feedback displays correctly.
- Frontend build passes.

### Verification checklist

- [ ] Quiz button exists.
- [ ] Questions render.
- [ ] Answers submit.
- [ ] Score displays.
- [ ] Explanations display.

---

## Step 11 — Progress tracking v1

### Goal
Track activity completion, skill progress, weak points, and review queue.

### What to implement

Endpoints:

- `GET /api/progress/overview`
- `GET /api/progress/units/{unit_code}`
- `POST /api/progress/activities/complete`
- `POST /api/progress/exercise-result`

### How to implement

- Store unit completion percentage.
- Store activity completion.
- Store skill scores.
- Store weak points.
- Create review items from weak points.

### Finish criteria

- Exercise results update progress.
- Weak points appear in review queue.
- Progress overview returns skill scores.
- Tests pass.

### Verification checklist

- [ ] Progress module exists.
- [ ] Overview endpoint works.
- [ ] Unit progress endpoint works.
- [ ] Exercise result updates progress.
- [ ] Review item created.

---

## Step 12 — Progress frontend

### Goal
Show progress dashboard and unit progress in UI.

### What to implement

- ProgressSummary
- SkillProgressCard
- UnitProgressCard
- WeakPointsList
- ReviewRecommendationCard

### How to implement

- Fetch progress overview.
- Display skill bars.
- Display weak points.
- Update unit page after exercise submission.

### Finish criteria

- Progress page displays API data.
- Weak points display.
- A1.5 progress updates after quiz.

### Verification checklist

- [ ] Progress page uses backend data.
- [ ] Skill progress displays.
- [ ] Weak points display.
- [ ] Unit page progress updates.

---

## Step 13 — Listening activity v1

### Goal
Implement transcript-based listening for A1.5.

### What to implement

- Listening backend module
- A1.5 café transcript
- comprehension questions
- submit endpoint
- frontend listening component

### How to implement

Use this deterministic transcript:

Cameriere: Buongiorno, desidera?
Cliente: Vorrei un cappuccino e un cornetto, per favore.
Cameriere: Altro?
Cliente: No, grazie. Quanto costa?
Cameriere: Sono tre euro.

Questions:
- What does the customer order?
- How much does it cost?
- Which polite phrase is used?

### Finish criteria

- Listening task loads.
- Answers are scored.
- Listening progress updates.

### Verification checklist

- [ ] Listening backend exists.
- [ ] Listening frontend exists.
- [ ] A1.5 task loads.
- [ ] Submission works.
- [ ] Progress updates.

---

## Step 14 — Speaking roleplay v1

### Goal
Implement text-based speaking roleplay for A1.5.

### What to implement

- Speaking backend module
- Roleplay start/respond/finish endpoints
- Frontend roleplay component
- Speaking evaluation

### How to implement

Scenario:
- learner orders at Italian café
- AI acts as waiter
- learner responds in Italian

Evaluation criteria:
- café vocabulary
- ordering food/drink
- asking for price or bill
- politeness
- basic grammar correctness

### Finish criteria

- Roleplay session starts.
- Learner response is accepted.
- Finish returns evaluation.
- Speaking progress updates.

### Verification checklist

- [ ] Speaking module exists.
- [ ] Roleplay starts.
- [ ] Response endpoint works.
- [ ] Finish endpoint evaluates.
- [ ] Speaking score updates.

---

## Step 15 — Materials ingestion v1

### Goal
Store and link lesson materials.

### What to implement

Supported source types:

- manual_text
- pdf metadata placeholder
- webpage metadata placeholder
- youtube_transcript metadata placeholder

Endpoints:

- `POST /api/materials`
- `GET /api/materials/units/{unit_code}`
- `POST /api/materials/{material_id}/link-unit`

### How to implement

- Fully implement manual text first.
- Store metadata for other source types.
- Chunk raw text.
- Link material to unit.

### Finish criteria

- Manual material can be created.
- Material can be linked to A1.5.
- Chunks are created.
- Lesson page shows linked materials.

### Verification checklist

- [ ] Material module exists.
- [ ] Manual material creation works.
- [ ] Unit linking works.
- [ ] Chunks created.
- [ ] A1.5 materials retrievable.

---

## Step 16 — RAG retrieval v1

### Goal
Retrieve unit-specific material chunks for AI grounding.

### What to implement

- chunker
- retriever
- RAG service
- `POST /api/rag/retrieve`

### How to implement

- Use simple keyword retrieval first.
- Do not implement vector search yet.
- Update AI Q&A to include retrieved context.

### Finish criteria

- Query retrieves relevant A1.5 chunks.
- AI Q&A includes retrieved context.
- Tests pass.

### Verification checklist

- [ ] RAG module exists.
- [ ] Keyword retrieval works.
- [ ] Unit-scoped retrieval works.
- [ ] AI Q&A uses retrieved chunks.

---

## Step 17 — Academic mode v1

### Goal
Make lessons mode-aware.

### What to implement

- study_mode parameter in lesson payload
- mode-aware exercise generation
- mode-aware AI explanation
- mode-aware frontend selection

### How to implement

Daily mode emphasizes:
- practical dialogue
- listening/speaking
- everyday scenarios

Academic mode emphasizes:
- structured grammar
- reading comprehension
- writing tasks
- exam-like tasks

### Finish criteria

- A1.5 daily mode returns practical activities.
- A1.5 academic mode returns more structured exam-like tasks.
- Frontend can switch modes.

### Verification checklist

- [ ] Mode parameter exists.
- [ ] Daily mode works.
- [ ] Academic mode works.
- [ ] Frontend mode selection works.

---

## Step 18 — Supabase Auth integration

### Goal
Add real authentication while preserving dev fallback.

### What to implement

- frontend Supabase client
- login page
- protected routes
- backend JWT validation
- current user dependency
- user profile mapping

### How to implement

- Use Supabase Auth.
- Replace hardcoded `dev-user` when authenticated.
- Keep dev fallback only in development.

### Finish criteria

- Login works.
- Protected endpoints require authentication.
- Progress uses real user ID.
- Tests cover auth behavior.

### Verification checklist

- [ ] Supabase client configured.
- [ ] Login page exists.
- [ ] Backend validates auth.
- [ ] user_id is stored correctly.

---

## Step 19 — Deployment setup

### Goal
Prepare deployment for frontend, backend, and database.

### What to implement

- deployment docs
- Vercel frontend setup
- Railway/Render backend setup
- Supabase setup docs
- GitHub Actions for frontend and backend checks

### Finish criteria

- Deployment docs complete.
- Frontend environment variables documented.
- Backend environment variables documented.
- Backend health endpoint works after deployment.
- CI checks exist.

### Verification checklist

- [ ] Deployment docs exist.
- [ ] Frontend deploy config ready.
- [ ] Backend deploy config ready.
- [ ] GitHub Actions checks exist.

---

## Step 20 — Expand curriculum beyond A1.5

### Goal
Add full A1 to B2 curriculum seed data.

### What to implement

- detailed A1 units
- A2 unit records
- B1 unit records
- B2 unit records
- level exit outcomes
- validation for full curriculum

### How to implement

- Preserve A1 → A2 → B1 → B2 order.
- Every unit must have code and title.
- Every unit must have skill objectives.
- Importer must be idempotent.

### Finish criteria

- All levels exist.
- Expected unit counts exist.
- Sample units A1.5, A2.3, B1.11, B2.11 exist.
- Importer is idempotent.

### Verification checklist

- [ ] A1 exists.
- [ ] A2 exists.
- [ ] B1 exists.
- [ ] B2 exists.
- [ ] Key sample units exist.
- [ ] Full importer tests pass.

---

## Step 21 — Final MVP acceptance testing

### Goal
Verify the MVP end-to-end.

### Acceptance criteria

- User can open website.
- User can log in.
- User can choose Daily Communication.
- User can open A1.5.
- User can see objectives and activities.
- User can ask AI to explain lesson.
- User can ask lesson-specific question.
- User can generate and submit quiz.
- User can complete listening activity.
- User can complete text-based speaking roleplay.
- User can complete writing task.
- User receives score and explanation.
- User progress updates.
- Weak points appear in review queue.
- Progress dashboard displays skill progress.
- App works after refresh.
- Backend tests pass.
- Frontend type-check/lint passes.

### Finish criteria

- All acceptance criteria pass or failures are documented with fixes.
- MVP is deployable.
- Remaining risks are documented.

---

# Standard implementation report format

Every implementation step must return this report:

```markdown
# Implementation Report

## Step Completed
[Step name]

## Files Created
- ...

## Files Modified
- ...

## Key Implementation Details
- ...

## Tests Run
- Command:
- Result:

## Validation Checklist
- [ ] ...

## Issues / Blockers
- ...

## Recommended Next Step
- ...
```

---

# Standard double-check prompt

Use this after each coding agent finishes a step:

```text
Review the implementation report and the current codebase against the implementation plan.
Check only the current step.
Do not add new features.
Verify:
1. The implemented files match the expected files.
2. The implementation follows the architecture rules.
3. The step did not implement future-step features.
4. Tests were run and passed.
5. Finish criteria were satisfied.
6. Any blockers are clearly reported.
Return:
- PASS or FAIL
- Missing items
- Unrelated changes
- Required fixes before moving to next step
```

---

# Common failure patterns to watch for

- Implementing future-step features too early
- Calling AI providers directly outside AI orchestrator
- Hardcoding user progress without user_id
- Using the PDF directly at runtime instead of structured curriculum data
- Building many incomplete pages instead of one working vertical slice
- Adding Supabase Auth before backend/frontend foundations are stable
- Adding vector search before simple retrieval works
- Adding voice/pronunciation before text-based speaking works
- Mixing business logic inside FastAPI route handlers
- Mixing API/data logic directly inside React page components

---

# Recommended next action after this document

Continue with Step 3 if not completed yet:

Step 3 — Database schema v1

After Step 3 finishes, compare the report against the Step 3 finish criteria and verification checklist in this document.
