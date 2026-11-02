# Build history (reference only)

`index.html` at the repo root is now the source of truth. This folder is how it was produced during the claude.ai sessions:
`rebuild.sh` copies `tidebreak_v116.html` and applies the `patch_*.py` scripts in order (string replacements), then `patch_q.py` repacks the embedded models and `patch_split.py` moves them out to `m/`. `mk_*.py` generate the `fact_*.js` model factories from `fact_charon.js`. The patches reference `glb/*.glb`, which are in `../assets/glb/`.

You don't need to keep using this pipeline; edit index.html directly.
