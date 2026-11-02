from playwright.sync_api import sync_playwright
import pathlib,io,sys,json
from PIL import Image
p=pathlib.Path(sys.argv[1]).resolve();base=pathlib.Path('node_modules/three').resolve()
teams=json.loads(sys.argv[2])
with sync_playwright() as pw:
    b=pw.chromium.launch(args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']);pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=3)
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)+' @ '+str(e.stack)[:600]));cons=[];pg.on('console',lambda m:cons.append(m.text[:300]) if m.type in('warning','error') and 'GL Driver' not in m.text else None)
    pg.route('**/fonts.g*/**',lambda r:r.abort())
    pg.route('**/cdn.jsdelivr.net/npm/three@0.128.0/**',lambda r:r.fulfill(path=str(base/r.request.url.split('three@0.128.0/')[1]),content_type='application/javascript'))
    pg.add_init_script("localStorage.setItem('tb_arena',JSON.stringify({teams:%s}))"%json.dumps(teams))
    pg.goto('file://'+str(p));pg.wait_for_timeout(3500);pg.evaluate("()=>document.getElementById('arstart').click()");pg.wait_for_timeout(500);pg.evaluate("()=>document.getElementById('arfight').click()");pg.wait_for_timeout(1000)
    pg.evaluate("()=>window.__tb.zoom(float(sys.argv[3]) if False else 1)") if False else None
    pg.evaluate("()=>window.__tb.zoom(%s)"%(sys.argv[3] if len(sys.argv)>3 else '1'))
    for k in range(6):
        pg.wait_for_timeout(3000)
        print(pg.evaluate("()=>{const G=window.__tb.G,R=window.__r3d;return JSON.stringify({t:G.t.toFixed(1),hp:[0,1].map(s=>Math.round(G.units.filter(u=>u.side===s).reduce((a,u)=>a+u.hp,0))),mv:G.units.filter(u=>u.moving).length,R:{k:R.atlK,n:R.n,miss:R.miss,f:R.failed,tick:R.tick|0,render:R.render|0},types0:G.units.map(u=>u.side+':'+u.type).reduce((a,t)=>(a[t]=(a[t]||0)+1,a),{})})}"))
    pg.screenshot(path='shots/ar11.png');print(errs[:3],cons[:5]);b.close()
