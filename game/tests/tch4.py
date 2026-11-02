from playwright.sync_api import sync_playwright
import pathlib,sys
p=pathlib.Path('index.html').resolve();base=pathlib.Path('node_modules/three').resolve()
with sync_playwright() as pw:
    b=pw.chromium.launch(args=['--use-gl=swiftshader']);pg=b.new_page(viewport={'width':390,'height':844})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.route('**/fonts.g*/**',lambda r:r.abort())
    pg.route('**/cdn.jsdelivr.net/npm/three@0.128.0/**',lambda r:r.fulfill(path=str(base/r.request.url.split('three@0.128.0/')[1]),content_type='application/javascript'))
    for m in sys.argv[1:]:
        pg.goto('file://'+str(p));pg.wait_for_timeout(2500);pg.evaluate("m=>window.__tb.setMap(m)",m);pg.evaluate("()=>window.__tb.setPick(0)");pg.click('#startbtn');pg.wait_for_timeout(500)
        for vi in range(3):
            r=pg.evaluate("""vi=>{const tb=window.__tb,G=tb.G,h=G.S[0].hall;const vs=G.villages.filter(v=>!G.B.some(b=>b.type==='chapel'&&b.x===v.x&&b.y===v.y)).sort((a,b)=>Math.hypot(a.x-h.x,a.y-h.y)-Math.hypot(b.x-h.x,b.y-h.y));const v=vs[0];
              for(const k in G.S[0].res)G.S[0].res[k]=999;const toasts=[];const T=document.getElementById('toast');
              tb.tryPlace('chapel',v.x,v.y);window.__V=v;const w=G.units.find(u=>u.buildAt);return JSON.stringify({v:[v.x,v.y],w:w&&[w.type,w.mode,w.path.length],toast:(document.querySelector('#toast')||{}).textContent})}""",vi)
            print(m,r)
            for k in range(30):
                pg.evaluate("()=>{for(let i=0;i<20;i++)window.__tb.update(.05)}")
                st=pg.evaluate("()=>{const G=window.__tb.G,v=window.__V;const w=G.units.find(u=>u.buildAt);return JSON.stringify({built:G.B.some(b=>b.type==='chapel'&&b.x===v.x&&b.y===v.y),w:w&&[w.type,w.mode,Math.round(Math.hypot(w.x-v.x-2,w.y-v.y-2)*10)/10]})}")
                if '"built":true' in st or '"w":null' in st:break
            print('  ',k,st,pg.evaluate("()=>(document.querySelector('#toast')||{}).textContent"))
    print(errs[:3]);b.close()
