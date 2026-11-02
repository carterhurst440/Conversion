import { cpSync, createReadStream, existsSync, statSync } from 'node:fs';
import { extname, join, normalize, resolve } from 'node:path';
import { defineConfig, type Plugin } from 'vite';

// The game lives in game/ as a standalone page (no build step). Only these
// paths are shipped to players; tools, tests, source models and history stay
// in the repo.
const GAME_DIR = resolve(__dirname, 'game');
const GAME_SHIPPED = ['index.html', 'm', 'vendor'];

const MIME: Record<string, string> = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
};

function gamePlugin(): Plugin {
  let outDir = 'dist';
  return {
    name: 'conversion-game',
    configResolved(config) {
      outDir = resolve(config.root, config.build.outDir);
    },
    configureServer(server) {
      server.middlewares.use('/game', (req, res, next) => {
        let path = decodeURIComponent((req.url ?? '/').split('?')[0]);
        if (path === '/' || path === '') path = '/index.html';
        const top = path.split('/')[1];
        const file = normalize(join(GAME_DIR, path));
        if (!GAME_SHIPPED.includes(top) || !file.startsWith(GAME_DIR)) return next();
        if (!existsSync(file) || !statSync(file).isFile()) return next();
        res.setHeader('Content-Type', MIME[extname(file)] ?? 'application/octet-stream');
        createReadStream(file).pipe(res);
      });
    },
    closeBundle() {
      for (const entry of GAME_SHIPPED) {
        cpSync(join(GAME_DIR, entry), join(outDir, 'game', entry), { recursive: true });
      }
    },
  };
}

export default defineConfig({
  plugins: [gamePlugin()],
});
