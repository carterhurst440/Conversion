# Conversion

A real-time strategy game that ships from one codebase as a web app (Vercel) and an iOS app (Capacitor).

## Stack
- **Vite + TypeScript**: the web app in `src/`
- **Supabase**: auth and database (project "Conversion")
- **Capacitor**: wraps the web build as the iOS app in `ios/`

## Develop
```bash
npm install
npm run dev        # http://localhost:5173
npm run build      # type-check + production build to dist/
```

## iOS
```bash
npm run ios        # build, sync into ios/, open Xcode
npm run ios:sync   # build + sync only
```
Run the app from Xcode, either in a simulator or on a device. Every web change has to be rebuilt and synced before the iOS app picks it up.

## Database
SQL migrations live in `supabase/migrations/`. `public.users` holds one profile per auth user and is created automatically at signup from the `username` passed in the signup metadata.

## Config
`.env` holds the Supabase URL and the **publishable** key. Both are public by design, and Row Level Security protects the data. Never commit the secret/service-role key. Put local overrides in `.env.local`.

## Deploy (Vercel)
Framework preset: Vite. Build command: `npm run build`. Output directory: `dist`.
