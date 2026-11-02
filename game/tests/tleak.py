from playwright.sync_api import sync_playwright
import pathlib,io,sys,json
p=pathlib.Path(sys.argv[1]).resolve();base=pathlib.Path('node_modules/three').resolve()
teams=json.loads(sys.argv[2])
with sync_playwright() as pw:
    b=pw.chromium.launch(args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']);pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.route('**/fonts.g*/**',lambda r:r.abort())
    pg.route('**/cdn.jsdelivr.net/npm/three@0.128.0/**',lambda r:r.fulfill(path=str(base/r.request.url.split('three@0.128.0/')[1]),content_type='application/javascript'))
    pg.add_init_script("localStorage.setItem('tb_arena',JSON.stringify({teams:%s}))"%json.dumps(teams))
    pg.goto('file://'+str(p));pg.wait_for_timeout(3500)
    for r in range(4):
        pg.evaluate("()=>document.getElementById('arstart')&&document.getElementById('arstart').click()");pg.wait_for_timeout(400);pg.evaluate("()=>document.getElementById('arfight').click()");pg.wait_for_timeout(300)
        pg.evaluate("()=>window.__tb.zoom(.7)")
        for k in range(3):
            pg.wait_for_timeout(2500)
            print(r,pg.evaluate("()=>{const R=window.__r3d;return JSON.stringify({tex:R.tex,geo:R.geo,ct:R.ct,demo:R.demo,dd:window.__DD,n:R.n,miss:R.miss||0,alive:window.__tb.G.units.length})}"))
        # rematch
        pg.evaluate("()=>{const b=[...document.querySelectorAll('button')].find(x=>x.textContent.trim()==='Rematch');if(b)b.click()}");pg.wait_for_timeout(500)
    print(errs[:3])
