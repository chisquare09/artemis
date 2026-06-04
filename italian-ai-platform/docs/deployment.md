# Deployment Guide

Deploy the Italian AI Learning Platform to cloud services.

## Architecture

- **Frontend**: Vercel (Next.js)
- **Backend**: Railway or Render (FastAPI)
- **Database/Auth**: Supabase (PostgreSQL + Auth)
- **Source**: GitHub

## Frontend (Vercel)

### Setup

1. Connect GitHub repository to Vercel
2. Set root directory: `frontend`
3. Build command: `npm run build`
4. Output directory: `.next`

### Environment Variables

```
NEXT_PUBLIC_API_BASE_URL=https://your-backend.railway.app
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
```

## Backend (Railway/Render)

### Setup

1. Connect GitHub repository
2. Set root directory: `backend`
3. Install command: `pip install -r requirements.txt`
4. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### Health Check

```
GET /health
```

### Environment Variables

```
APP_ENV=production
PROJECT_NAME=Italian AI Learning Platform API
API_PREFIX=/api
FRONTEND_ORIGIN=https://your-frontend.vercel.app

DATABASE_URL=postgresql://user:pass@host:5432/db
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
SUPABASE_JWT_SECRET=your-jwt-secret

GEMINI_API_KEY=your-gemini-key
GROQ_API_KEY=your-groq-key

STORAGE_BUCKET=your-bucket
```

## Supabase Setup

### Database

1. Create Supabase project at supabase.com
2. Copy PostgreSQL connection string to `DATABASE_URL`
3. Enable Row Level Security if needed

### Auth

1. Enable Email/Password auth in Supabase dashboard
2. Copy project URL to `SUPABASE_URL`
3. Copy anon key to `NEXT_PUBLIC_SUPABASE_ANON_KEY`
4. Copy service role key to `SUPABASE_SERVICE_ROLE_KEY`
5. Copy JWT secret to `SUPABASE_JWT_SECRET`

### Migrations

Run from backend directory:

```bash
cd backend
source .venv/bin/activate
alembic upgrade head
```

### Curriculum Import

Dry run first:

```bash
cd backend
python ../scripts/import_curriculum.py --dry-run
```

Then import:

```bash
python ../scripts/import_curriculum.py
```

## GitHub Setup

### Repository

1. Push code to GitHub
2. Protect main branch
3. Require CI checks to pass before merge

### Secrets

Add these as GitHub repository secrets for Actions if needed:
- `SUPABASE_URL`
- `DATABASE_URL`
- (CI runs without external services in dev mode)

### CI Workflows

- `.github/workflows/frontend-ci.yml` — lint, build, type-check
- `.github/workflows/backend-ci.yml` — pytest

## CORS Configuration

Set `FRONTEND_ORIGIN` in backend to your deployed frontend URL:

```
FRONTEND_ORIGIN=https://your-app.vercel.app
```

Multiple origins can be added by modifying `app/main.py` if needed.

## Verification

After deployment:

1. Backend health: `GET https://your-backend/health`
2. Frontend loads: `https://your-frontend`
3. Login works with Supabase credentials
4. A1.5 unit page loads
5. Progress endpoints work
