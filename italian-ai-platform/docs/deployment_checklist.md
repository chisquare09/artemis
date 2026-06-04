# Deployment Checklist

## Pre-Deployment

- [ ] Frontend build passes: `cd frontend && npm run build`
- [ ] Backend tests pass: `cd backend && pytest -v`
- [ ] No secrets in committed files
- [ ] `.env.example` files are up to date

## Supabase Setup

- [ ] Supabase project created
- [ ] PostgreSQL connection string obtained
- [ ] Auth Email/Password enabled
- [ ] Anon key and service role key obtained
- [ ] JWT secret obtained (optional but recommended)

## Backend Deployment

- [ ] `DATABASE_URL` configured
- [ ] `SUPABASE_URL` configured
- [ ] `SUPABASE_SERVICE_ROLE_KEY` configured
- [ ] `SUPABASE_JWT_SECRET` configured
- [ ] `GEMINI_API_KEY` or `GROQ_API_KEY` configured
- [ ] `FRONTEND_ORIGIN` set to frontend URL
- [ ] `APP_ENV=production`
- [ ] Health check works: `GET /health`
- [ ] Migrations applied: `alembic upgrade head`
- [ ] Curriculum imported: `python ../scripts/import_curriculum.py`

## Frontend Deployment

- [ ] `NEXT_PUBLIC_API_BASE_URL` set to backend URL
- [ ] `NEXT_PUBLIC_SUPABASE_URL` configured
- [ ] `NEXT_PUBLIC_SUPABASE_ANON_KEY` configured
- [ ] Build succeeds on Vercel

## Post-Deployment Verification

- [ ] Frontend loads at deployed URL
- [ ] Login page works
- [ ] User can sign up/sign in
- [ ] A1.5 unit page loads
- [ ] AI tutor panel responds
- [ ] Exercises load and submit
- [ ] Progress updates after activity
- [ ] Sign out works

## Troubleshooting

**CORS errors**: Check `FRONTEND_ORIGIN` matches deployed frontend URL exactly.

**Auth errors**: Verify Supabase keys match between frontend and backend.

**Database errors**: Verify `DATABASE_URL` and run `alembic upgrade head`.

**404 on lessons**: Run curriculum import script.
