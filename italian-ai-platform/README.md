# Italian AI Learning Platform

An AI-powered Italian language learning platform supporting Daily Communication and Academic Purpose study modes.

## Current MVP Status

- A1.5 vertical slice with café vocabulary and grammar
- AI tutor panel with lesson explanations and Q&A
- Deterministic exercises with evaluation
- Listening activity (transcript-based)
- Speaking roleplay (text-based)
- Progress tracking and review system
- Materials ingestion with keyword RAG
- Supabase Auth integration
- Academic/Daily mode selection

## Monorepo Structure

```
italian-ai-platform/
├── frontend/          # Next.js + TypeScript + Tailwind CSS
├── backend/           # FastAPI + Pydantic
├── packages/
│   ├── shared-types/  # Shared TypeScript types
│   └── shared-config/ # Shared configuration
├── docs/              # Documentation
├── scripts/           # Utility scripts
└── .github/workflows/ # CI/CD
```

## Local Development

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:3000

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000

### Run Tests

```bash
# Backend
cd backend
pytest -v

# Frontend
cd frontend
npm run lint
npm run build
```

## Deployment

See [docs/deployment.md](docs/deployment.md) for cloud deployment instructions:

- Frontend on Vercel
- Backend on Railway/Render
- Database/Auth on Supabase

## Documentation

- [Deployment Guide](docs/deployment.md)
- [Supabase Auth](docs/supabase_auth_v1.md)
- [Academic Mode](docs/academic_mode_v1.md)
- [RAG Retrieval](docs/rag_retrieval_v1.md)
- [Materials Ingestion](docs/materials_ingestion_v1.md)
- [Speaking Roleplay](docs/speaking_roleplay_v1.md)
- [Listening Activity](docs/listening_activity_v1.md)
- [Progress/Review](docs/progress_review_v1.md)
- [Exercise Engine](docs/exercise_engine_v1.md)
- [AI Orchestrator](docs/ai_orchestrator.md)
- [Curriculum/Lessons API](docs/api_curriculum_lessons.md)
