# CONVERSION — island RTS

A real-time island strategy game in one page: `index.html` (all game code, ~1.2 MB) plus the 3D models in `m/*.js`. No build step, no frameworks: vanilla JS + 2D canvas, with Three.js r128 (from cdn.jsdelivr.net) used only to render the 3D units.

## Run it
Open `index.html` in a browser (file:// works: models load through `<script>` tags), or serve the folder (`python3 -m http.server`). It is played mostly on iPhone Safari, so mobile performance and memory matter.

## Layout of index.html (search for these names)
- **Factions**: Celtic = god 8 (Cernunnos), Egypt = god 0 (Anubis), Greek = god 1 (Hades). `EGY(side)` tests for Egypt.
- **Units**: `U` (stats), `UORDER`, `GU[god]` = holy units, keys `g<god>_<i>` (e.g. `g0_4` = Sobek Guard, `g1_2` = Electra). For holy units `X` is the **awakened/upgraded** form and `Xb` the **basic** form (special stripped). `GUK[god]` lists the keys.
- **Buildings**: `B`, `place()`, `canPlace()`, `tryPlace()`; the church/temple/pyramid is type `chapel` (4×4, built on villages `G.villages`), the main one is `hall`.
- **Specials**: `function special(u,sp,dt)` handles every ability. Manual cast for the player's units is gated by `u.side===0&&!(u.cast>G.t)`; `MANSP` defines the on-screen special buttons; `SPNAME` the display names.
- **R3D** (the 3D unit renderer, `var R3D=(()=>{...`): one WebGL canvas `glc` (ATLAS 2048) used as a sprite atlas. Each frame `frame()` builds/drives a Three.js scene per visible unit (`CT` map), renders each into its own cell, and the 2D map draws cells with `drawImage`. Menu icons/cards use `drawDemo` and a separate strip below `DEMOY`.
  - `TYPES[unitKey]` = render settings `{f:factory, ps, vref, W, H, a, cap, top, sh, atk:[[clip,hitTime,rate],...]}`.
  - `TYU(u)` maps a unit to its TYPES entry and returns null until its model has loaded.
  - `FACT.<name>` = model factories (most humanoids derive from the Charon/"Tripo rig" factory: keyframed poses `K(t,{...})`, two-bone IK for arms/legs, `CL` clip table, `tick(dt,I)`). `GLAB` holds per-model heights (`mh`).
  - `drive(u,st,dt)` connects game state to animation (attacks, specials → `c.playG(clip)`).
  - **Crop**: each unit type learns how much of its camera box it fills (`CROP`, `cropSample`), baked defaults in `window.CROPBAKE`, learned values kept in localStorage `tb-crop2`. Cells grow if a move touches the edge.
  - **Memory**: `dispose(st)` frees geometry, materials, per-unit textures and skeleton bone textures. Leaks here crash the WebGL context on iOS.
  - Context loss self-heals (`heal()`); `SNAP` snapshots are the fallback image.
- **Models**: loader `window.MODELS={}` near the top; `KS=[...]` lists the model keys loaded from `m/<key>.js`.
- **Proving grounds** (`AR`, `newArena`), **Movement Lab** (`openLab`, `#labgo` = "Use special now", `#labup` = upgrade toggle).
- **Debug**: ••• menu → "Graphics info" overlay; `window.__r3d` stats; `window.__tb` test hooks (G, update, makeUnit, setMap, setPick, tryPlace, SEL, zoom, centerOnPt, …).

## Adding a 3D unit
1. `python3 tools/add_model.py model.glb key` → writes `m/key.js`; add `key` to `KS`.
2. Write a factory (copy the Electra `FACT.fury` / Sobek `FACT.croc` pattern), add `GLAB` height, `TYPES` for the unit key and its `b` key, a `TYU` guard, and `drive()` hooks for its special.
3. Tripo models share a 78-bone rig. Wings or tails need extra bones: `tools/wingrig.py` adds wing bones and re-skins wing vertices.

## Owner's standing preferences
- Every unit has two versions, basic and upgraded (upgrade through research); upgraded units show only a ground-ring glow.
- The Movement Lab must hold every character.
- Units cannot walk through buildings; each map's villages have a unique look.
- Test changes with screenshots (Playwright, tests/), on phone-sized viewports (390×844, DPR 2–3).

## Tests
`tests/` has Playwright scripts (`pip install playwright`, Chromium). They expect Three.js r128 locally: `npm i three@0.128.0` (scripts route the CDN to `node_modules/three`). Examples: `python3 tests/tlab5.py Electra 0 shots/el.png sp 3.2` (lab, special), `python3 tests/tar11.py index.html '<teams json>' 1.2` (arena), `python3 tests/tleak.py index.html '<teams json>'` (GPU texture leak check), `python3 tests/view.py model.glb out.png` (4-view model preview). Create a `shots/` folder first.
