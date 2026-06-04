# Cloud Deployment Execution Guide

Step-by-step instructions for deploying the Italian AI Learning Platform.

## Prerequisites

- GitHub account with repository access
- Supabase account (free tier works)
- Railway account (free tier works) OR Render account
- Vercel account (free tier works)

## Phase 1: Push Code to GitHub

If not already done:

```bash
cd italian-ai-platform
git init
git add .
git commit -m "Initial MVP commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/italian-ai-platform.git
git push -u origin main
```

## Phase 2: Supabase Setup

### 2.1 Create Project

1. Go to https://supabase.com/dashboard
2. Click "New Project"
3. Choose organization
4. Enter project name: `italian-ai-platform`
5. Generate a strong database password (save it!)
6. Choose region closest to you
7. Click "Create new project"
8. Wait for project to provision (~2 minutes)

### 2.2 Get Connection Details

From Supabase Dashboard > Project Settings > API:

```
SUPABASE_URL = https://xxxxx.supabase.co
SUPABASE_ANON_KEY = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_SERVICE_ROLE_KEY = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

From Project Settings > Database > Connection string > URI:

```
DATABASE_URL = postgresql://postgres.[PROJECT-REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:6543/postgres
```

Note: Use the "Transaction pooler" connection string for serverless deployments.

From Project Settings > API > JWT Settings:

```
SUPABASE_JWT_SECRET = (copy the JWT secret)
```

### 2.3 Enable Auth

1. Go to Authentication > Providers
2. Ensure "Email" is enabled
3. Optionally disable "Confirm email" for easier testing

## Phase 3: Backend Deployment (Railway)

### 3.1 Create Railway Project

1. Go to https://railway.app
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Connect your GitHub account if not already
5. Select your `italian-ai-platform` repository
6. Railway will auto-detect the repo

### 3.2 Configure Backend Service

1. Click "Add Service" > "GitHub Repo" (if not auto-created)
2. Set root directory: `backend`
3. Go to service Settings > Environment

Add environment variables:

```
APP_ENV=production
PROJECT_NAME=Italian AI Learning Platform API
API_PREFIX=/api
FRONTEND_ORIGIN=https://your-app.vercel.app
DATABASE_URL=postgresql://postgres.[ref]:[pass]@aws-0-[region].pooler.supabase.com:6543/postgres
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
SUPABASE_JWT_SECRET=your-jwt-secret
GEMINI_API_KEY=
GROQ_API_KEY=
```

Note: Leave FRONTEND_ORIGIN as placeholder for now - update after Vercel deployment.

### 3.3 Deploy Backend

1. Railway auto-deploys on push
2. Check "Deployments" tab for status
3. Once deployed, go to Settings > Networking > Generate Domain
4. Copy the public URL (e.g., `https://italian-ai-platform-production.up.railway.app`)

### 3.4 Verify Backend

```bash
curl https://YOUR-RAILWAY-URL/health
# Should return: {"status":"ok","service":"italian-ai-platform-api"}

curl https://YOUR-RAILWAY-URL/
# Should return: {"service":"italian-ai-platform-api","environment":"production"}
```

## Phase 4: Database Migration

### 4.1 Run Migrations Locally

From your local machine with DATABASE_URL set:

```bash
cd italian-ai-platform/backend
export DATABASE_URL="postgresql://postgres.[ref]:[pass]@aws-0-[region].pooler.supabase.com:6543/postgres"
source .venv/bin/activate
alembic upgrade head
```

### 4.2 Verify Tables

In Supabase Dashboard > Table Editor, you should see tables:
- curriculum
- levels
- units
- objectives
- activities
- user_progress
- materials
- material_chunks
- exercise_results

### 4.3 Import Curriculum

```bash
# Dry run first
python scripts/import_curriculum.py --dry-run

# If successful, run actual import
python scripts/import_curriculum.py
```

Expected output:
```
Levels: 4
Units: 44
Objectives: 741
Activities: 7
```

### 4.4 Verify Curriculum API

```bash
curl https://YOUR-RAILWAY-URL/api/levels
# Should return A1, A2, B1, B2

curl https://YOUR-RAILWAY-URL/api/lessons/A1.5
# Should return A1.5 lesson data
```

## Phase 5: Frontend Deployment (Vercel)

### 5.1 Create Vercel Project

1. Go to https://vercel.com
2. Click "Add New" > "Project"
3. Import your GitHub repository
4. Select `italian-ai-platform` repo

### 5.2 Configure Frontend

1. Set Framework Preset: Next.js
2. Set Root Directory: `frontend`
3. Add Environment Variables:

```
NEXT_PUBLIC_API_BASE_URL=https://YOUR-RAILWAY-URL
NEXT_PUBLIC_SUPABASE_URL=https://xxxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
```

### 5.3 Deploy

1. Click "Deploy"
2. Wait for build to complete
3. Copy the deployed URL (e.g., `https://italian-ai-platform.vercel.app`)

### 5.4 Update Backend CORS

Go back to Railway > Your backend service > Environment Variables:

Update:
```
FRONTEND_ORIGIN=https://italian-ai-platform.vercel.app
```

Railway will auto-redeploy.

## Phase 6: Verification

### 6.1 Backend Health

```bash
curl https://YOUR-RAILWAY-URL/health
curl https://YOUR-RAILWAY-URL/api/levels
curl https://YOUR-RAILWAY-URL/api/lessons/A1.5
```

### 6.2 Frontend Loads

1. Open https://YOUR-VERCEL-URL in browser
2. Dashboard should load
3. No console errors about missing env vars

### 6.3 CORS Works

1. Open browser DevTools > Network tab
2. Navigate to /units/A1.5
3. API calls should succeed (not blocked by CORS)

### 6.4 Auth Works

1. Go to /login
2. Sign up with email/password
3. Check email for confirmation (if enabled)
4. Log in
5. Verify AuthStatus shows your email
6. Sign out works

### 6.5 MVP Flow Works

1. Open /units/A1.5
2. Click "Explain this lesson" - AI response appears
3. Ask "How do I ask for the bill?" - AI responds
4. Generate quiz - 5 questions appear
5. Submit answers - score/feedback displays
6. Check /progress - shows updated progress
7. Try listening activity - submit works
8. Try speaking roleplay - conversation works
9. Add manual material - appears in list
10. Ask AI Q&A - RAG retrieves relevant content

## Troubleshooting

### CORS Errors

Update FRONTEND_ORIGIN in Railway to match exact Vercel URL (including https://).

### Database Connection

Ensure DATABASE_URL uses the pooler connection string, not direct connection.

### Auth Not Working

- Verify NEXT_PUBLIC_SUPABASE_URL and NEXT_PUBLIC_SUPABASE_ANON_KEY are set in Vercel
- Check Supabase Auth > Users to see if user was created
- Check Supabase Auth > Logs for errors

### Curriculum Not Loading

- Verify curriculum import completed successfully
- Check Railway logs for database errors
- Verify DATABASE_URL is correct in Railway

### Build Failures

- Check Railway/Vercel build logs
- Ensure requirements.txt and package.json are complete
- Verify root directory settings

## Post-Deployment Checklist

- [ ] Backend /health returns 200
- [ ] Backend /api/levels returns 4 levels
- [ ] Frontend loads without errors
- [ ] Login/signup works
- [ ] A1.5 lesson page loads
- [ ] AI Tutor responds
- [ ] Quiz generates and submits
- [ ] Progress updates
- [ ] Listening activity works
- [ ] Speaking roleplay works
- [ ] Materials can be added
- [ ] RAG retrieval works

## Environment Variables Summary

### Backend (Railway)

| Variable | Example |
|----------|---------|
| APP_ENV | production |
| PROJECT_NAME | Italian AI Learning Platform API |
| API_PREFIX | /api |
| FRONTEND_ORIGIN | https://italian-ai-platform.vercel.app |
| DATABASE_URL | postgresql://... |
| SUPABASE_URL | https://xxx.supabase.co |
| SUPABASE_SERVICE_ROLE_KEY | eyJ... |
| SUPABASE_JWT_SECRET | your-secret |
| GEMINI_API_KEY | (optional) |
| GROQ_API_KEY | (optional) |

### Frontend (Vercel)

| Variable | Example |
|----------|---------|
| NEXT_PUBLIC_API_BASE_URL | https://xxx.railway.app |
| NEXT_PUBLIC_SUPABASE_URL | https://xxx.supabase.co |
| NEXT_PUBLIC_SUPABASE_ANON_KEY | eyJ... |
