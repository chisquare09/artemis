# MVP Limitations

Known limitations in the current MVP release.

## Data Persistence

- **In-memory fallback stores**: Without database connection, progress, materials, and sessions are stored in memory and lost on restart
- **Dev fallback user**: Without Supabase JWT verification, dev mode uses a hardcoded user ID

## AI Provider

- **Fake provider in dev**: Without GEMINI_API_KEY or GROQ_API_KEY, the fake AI provider returns deterministic responses
- **No streaming**: AI responses are returned in full, not streamed

## Materials & RAG

- **Manual text only**: Materials only support `manual_text` source type — no PDF parsing, web scraping, or YouTube extraction
- **Keyword RAG**: RAG uses keyword overlap scoring, not vector embeddings

## Audio/Voice

- **Text-based speaking**: Speaking roleplay is text input only — no voice recording or pronunciation scoring
- **Transcript-based listening**: Listening uses pre-written transcripts — no real audio playback yet

## Curriculum Coverage

- **A1.5 vertical slice only**: Only A1.5 has fully interactive activities (quiz, listening, speaking, materials)
- **Other units structured only**: A1.1-A1.4, A1.6-A1.10, A2.*, B1.*, B2.* have curriculum objectives but no custom interactive exercises

## Authentication

- **Supabase-dependent**: Full auth requires Supabase project setup
- **No role-based access**: Single user role, no admin/teacher/student separation
- **No org/team features**: Individual use only

## Missing Features

- Full mock exams for certification units (B1.11, B2.11)
- Spaced repetition algorithm tuning
- Gamification/badges/streaks
- Mobile app
- Offline mode
- Analytics dashboard

## Production Hardening

- **Rate limiting**: No API rate limiting implemented
- **Input validation**: Basic Pydantic validation only
- **Error tracking**: No Sentry or similar integration
- **Monitoring**: No APM or metrics collection

## Next Phase Recommendations

1. Add activities/exercises for A1.1-A1.10 units
2. Integrate real AI provider (Gemini/Groq)
3. Add vector embeddings for RAG (pgvector)
4. Add audio playback for listening activities
5. Add voice input for speaking activities
6. Implement certification mock exams
