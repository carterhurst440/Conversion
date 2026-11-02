# CONVERSION

Island RTS shipped from one repo as a web app (Vercel) and an iOS app (Capacitor).

## Layout
- `src/`: the app shell (Vite + TypeScript): Supabase login, home screen, and the Play button, which opens `/game/index.html`
- `game/`: the game itself, a standalone page with no build step. See `game/CLAUDE.md` for its architecture. Edit `game/index.html` directly.
  - Only `game/index.html`, `game/m/` and `game/vendor/` ship to players (`GAME_SHIPPED` in `vite.config.ts`). `assets/`, `tools/`, `tests/` and `history/` are dev-only.
  - Three.js r128 is vendored in `game/vendor/three/` (no CDN), so the iOS app doesn't depend on jsdelivr.
- `supabase/migrations/`: SQL for the Supabase project "Conversion" (`public.users` profiles + RLS)
- `ios/`: Capacitor Xcode project. `npm run ios` builds, syncs and opens Xcode.

## Commands
- `npm run dev`: app at http://localhost:5173, game at http://localhost:5173/game/index.html
- `npm run build`: type-check + build to `dist/` (game files copied to `dist/game/`)
- `npm run ios:sync`: build + copy into the iOS project

## Notes
- The app and the game share one origin, so they share localStorage (the game uses `tb-*` / `r3d-*` keys; Supabase uses `sb-*`).
- It's played mostly on iPhone: test on phone-sized viewports, and watch WebGL memory on iOS.
