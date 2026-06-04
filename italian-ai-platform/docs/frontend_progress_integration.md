# Frontend Progress Integration

## Overview

Frontend components and pages connected to backend progress tracking APIs.

## Components

- `ProgressSummary` — Overall completion and level/mode display
- `SkillProgressCard` — Listening/reading/writing/speaking progress bars
- `UnitProgressCard` — Unit completion, mastery, activities count
- `WeakPointsList` — Areas needing review
- `ReviewRecommendationCard` — Review queue with priority
- `RecentActivityList` — Recent completed activities

## Endpoints Used

- `GET /api/progress/overview` — Overall progress dashboard
- `GET /api/progress/units/{unitCode}` — Unit-specific progress
- `POST /api/progress/exercise-result` — Update progress after quiz submission

## Flow

1. User completes A1.5 quiz
2. ExerciseSet submits answers to `/api/exercises/submit`
3. On success, calls `/api/progress/exercise-result`
4. Progress, weak points, and review items update
5. `/progress` and `/review` pages reflect new data

## Current Behavior

- User ID: `dev-user` (hardcoded, Supabase Auth coming later)
- Empty state shown when no progress exists
- Progress update failure does not break exercise feedback

## Future Steps

- Supabase Auth integration
- Listening/speaking progress tracking
- AI-generated review plans
