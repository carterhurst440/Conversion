from playwright.sync_api import sync_playwright
import pathlib,io,sys
from PIL import Image
p=pathlib.Path('index.html').resolve();base=pathlib.Path('node_modules/three').resolve()
k=sys.argv[1];up=sys.argv[2]=='1';out=sys.argv[3]
with sync_playwright() as pw:
    b=pw.chromium.launch(args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']);pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:m.type in('warning','error') and 'GL Driver' not in m.text and 'Failed to load' not in m.text and errs.append(m.text[:300]))
    pg.route('**/fonts.g*/**',lambda r:r.abort())
    pg.route('**/cdn.jsdelivr.net/npm/three@0.128.0/**',lambda r:r.fulfill(path=str(base/r.request.url.split('three@0.128.0/')[1]),content_type='application/javascript'))
    pg.add_init_script('window.ZM=%s;window.CY=%s'%(sys.argv[5] if len(sys.argv)>5 else 2,sys.argv[6] if len(sys.argv)>6 else 1.2));pg.goto('file://'+str(p));pg.wait_for_timeout(4000)
    pg.evaluate("()=>document.getElementById('labstart').click()");pg.wait_for_timeout(500);pg.evaluate("()=>document.getElementById('labstart').click()");pg.wait_for_timeout(500)
    pg.locator('#labb button.ub').filter(has_text=k).first.evaluate('b=>b.click()');pg.wait_for_timeout(1500)
    if up:pg.evaluate("()=>document.getElementById('labup').click()");pg.wait_for_timeout(1200)
    pg.evaluate("()=>{const tb=window.__tb,u=tb.G.labU,d=tb.G.units.find(e=>e.type.indexOf('dum')>=0||e.side===1);u.x=d.x-1.3;u.y=d.y+.5;u.mode='attack';u.tgt=d;tb.centerOnPt(u.x+.3,u.y-(window.CY||1.2));tb.zoom(+(window.ZM||2))}");ims=[]
    pg.wait_for_timeout(1500);ims.append(Image.open(io.BytesIO(pg.screenshot())))
    for t in range(4):
        pg.wait_for_timeout(700);ims.append(Image.open(io.BytesIO(pg.screenshot())))
    if len(sys.argv)>4:
        pg.evaluate("()=>document.getElementById('labgo').click()")
        for t in range(5):
            pg.wait_for_timeout(450);ims.append(Image.open(io.BytesIO(pg.screenshot())))
    print(pg.evaluate("()=>{const u=window.__tb.G.labU;return JSON.stringify({type:u.type,wrT:u.wrT,wrCd:u.wrCd,R:window.__r3d.n})}"))
    for n,i in enumerate(ims):i.crop((0,0,780,1100)).resize((390,550)).save(out.replace('.png','_%d.png'%n))
    ims=[i.crop((40,150,740,1250)) for i in ims]
    W=Image.new("RGB",(700*len(ims),1100));[W.paste(t,(i*700,0)) for i,t in enumerate(ims)];W.resize((350*len(ims),550)).save(out)
    print(errs[:5]);b.close()
