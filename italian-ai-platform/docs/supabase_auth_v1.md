# Supabase Auth v1

Authentication integration using Supabase Auth for user identity.

## Environment Variables

### Frontend
```
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

### Backend
```
APP_ENV=development
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
SUPABASE_JWT_SECRET=your-jwt-secret
```

## Frontend Login Behavior

1. User visits `/login`
2. If Supabase not configured, shows configuration warning
3. User enters email/password
4. On success, redirects to dashboard `/`
5. AuthStatus in nav shows user email and sign out button

## Backend get_current_user_id Behavior

- **Development without token**: Returns `"dev-user"`
- **With valid JWT**: Extracts `sub` claim as user ID
- **Production without token**: Returns 401
- **Invalid token**: Returns 401

## Development Fallback

In `APP_ENV=development`, requests without Authorization header use `"dev-user"`. This allows local development without Supabase configuration.

## Production Warning

**Important**: The current implementation decodes JWT payload without cryptographic verification. Before public deployment:

1. Set `SUPABASE_JWT_SECRET` in backend environment
2. Implement proper JWT signature verification using PyJWT or similar
3. Never rely on unverified tokens in production

## Public Endpoints

These endpoints do not require authentication:
- `/api/curriculum/*`
- `/api/levels/*`
- `/api/units/*`
- `/api/lessons/*`
- `/` (health check)
- `/health`

## User-Scoped Endpoints

These endpoints use `get_current_user_id`:
- `/api/progress/*`
- `/api/auth/me`

## Testing Locally

### Without Supabase Configuration
1. Start backend: `cd backend && uvicorn app.main:app --reload`
2. Start frontend: `cd frontend && npm run dev`
3. Visit http://localhost:3000 - AuthGuard allows access
4. Progress endpoints use `"dev-user"`

### With Supabase Configuration
1. Create Supabase project at supabase.com
2. Set environment variables in `.env` files
3. Start backend and frontend
4. Visit http://localhost:3000/login
5. Sign up or sign in
6. Authorization header sent with API requests

## API Reference

### GET /api/auth/me

Returns current user identity.

Response:
```json
{
  "user_id": "dev-user",
  "auth_mode": "development"
}
```

Or with Supabase token:
```json
{
  "user_id": "uuid-from-supabase",
  "auth_mode": "supabase"
}
```
