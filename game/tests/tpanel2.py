from playwright.sync_api import sync_playwright
import pathlib,sys,io
from PIL import Image
p=pathlib.Path('index.html').resolve();base=pathlib.Path('node_modules/three').resolve()
with sync_playwright() as pw:
    b=pw.chromium.launch(args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']);pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=3)
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:m.type in('warning','error') and 'GL Driver' not in m.text and errs.append(m.text[:200]))
    pg.route('**/fonts.g*/**',lambda r:r.abort())
    pg.route('**/cdn.jsdelivr.net/npm/three@0.128.0/**',lambda r:r.fulfill(path=str(base/r.request.url.split('three@0.128.0/')[1]),content_type='application/javascript'))
    pg.goto('file://'+str(p));pg.wait_for_timeout(3000);pg.evaluate("()=>window.__tb.setPick(0)");pg.evaluate("()=>document.getElementById('startbtn').click()");pg.wait_for_timeout(1500)
    pg.evaluate("()=>{const tb=window.__tb,G=tb.G,h=G.S[0].hall;tb.centerOnPt(h.x+2,h.y+2);tb.zoom(1);for(let i=0;i<18;i++){const u=tb.makeUnit(['g0_0','g0_1','g0_2','g0_3','megamummy','sower'][i%6],0,h.x+5+(i%6),h.y+5+Math.floor(i/6));G.units.push(u)}}")
    ims=[]
    for k in range(6):
        pg.evaluate("()=>{const tb=window.__tb;tb.select(tb.G.S[0].hall)}");pg.wait_for_timeout(900)
        if k%3==2:ims.append(Image.open(io.BytesIO(pg.screenshot())).resize((390,844)))
        pg.evaluate("()=>{const tb=window.__tb;tb.select(null)}");pg.wait_for_timeout(2500)
        if k%3==2:ims.append(Image.open(io.BytesIO(pg.screenshot())).resize((390,844)))
        print(k,pg.evaluate("()=>JSON.stringify(window.__r3d)"))
    W=Image.new('RGB',(390*len(ims),844));[W.paste(t,(i*390,0)) for i,t in enumerate(ims)];W.save('shots/panel.png');print(errs[:5]);b.close()
