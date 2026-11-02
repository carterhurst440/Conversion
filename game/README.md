# CONVERSION

Island RTS for the browser. Open `index.html` to play (works from the file system or any static host, e.g. GitHub Pages).

- `index.html`: the whole game
- `m/`: 3D unit models (base64 GLB in small JS files)
- `assets/glb/`: the processed models; `assets/glb_raw/`: original downloads for Electra and the Sobek Guard
- `tools/`: model processing (add_model.py, wingrig.py, glbq.py, shrinktex.py)
- `tests/`: Playwright screenshot tests
- `history/`: the patch pipeline used before the move to a repo
- `CLAUDE.md`: architecture notes for Claude Code
