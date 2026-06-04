# Progress Tracking and Review System v1

## Overview

Backend progress tracking for user learning state, activity completion, weak points, and review queue.

## Endpoints

### GET /api/progress/overview

Returns overall user progress including skill scores, weak points, and review queue.

### GET /api/progress/units/{unit_code}

Returns progress for a specific unit including completion percentage, mastery score, and weak points.

### POST /api/progress/activities/complete

Records activity completion and updates unit/skill progress.

### POST /api/progress/exercise-result

Records exercise result, stores weak points, and creates review queue items.

## User ID Strategy

Currently uses hardcoded `dev-user`. TODO: Replace with Supabase Auth.

## Storage

Uses in-memory store when DATABASE_URL is not configured. Progress persists for process lifetime only.

## Rules

### Unit Completion
- completion_percentage = completed_activities / total_activities * 100
- Status: not_started (0%), in_progress (>0 and <100%), completed (100%)

### Mastery Score
- Average of submitted activity/exercise scores

### Skill Progress
- Updated with weighted average on each activity completion

### Review Queue
- Created from weak points on exercise result
- Priority: high (<60), medium (60-79), low (80+)
- Deduplicated by target

## Future Steps

- Frontend progress dashboard (Step 12)
- Supabase Auth integration
- Database persistence
