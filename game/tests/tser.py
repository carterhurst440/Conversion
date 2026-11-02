from playwright.sync_api import sync_playwright
import pathlib,io,sys
from PIL import Image
p=pathlib.Path(sys.argv[1]).resolve();base=pathlib.Path('node_modules/three').resolve()
with sync_playwright() as pw:
    b=pw.chromium.launch(args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']);pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.route('**/fonts.g*/**',lambda r:r.abort())
    pg.route('**/cdn.jsdelivr.net/npm/three@0.128.0/**',lambda r:r.fulfill(path=str(base/r.request.url.split('three@0.128.0/')[1]),content_type='application/javascript'))
    pg.goto('file://'+str(p));pg.wait_for_timeout(4000)
    pg.evaluate("()=>document.getElementById('labstart').click()");pg.wait_for_timeout(500);pg.evaluate("()=>document.getElementById('labstart').click()");pg.wait_for_timeout(500)
    pg.locator('#labb button.ub').filter(has_text='Serpent').first.evaluate('b=>b.click()');pg.wait_for_timeout(1500)
    pg.evaluate("()=>{const tb=window.__tb,u=tb.G.labU,d=tb.G.units.find(e=>e.type.indexOf('dum')>=0||e.side===1);u.x=d.x-5.5;u.y=d.y+.5;u.hid=false;u.sink=0;u.mode=`attack`;u.tgt=d;tb.centerOnPt(d.x-3.2,d.y+.5);tb.zoom(3.2)}");ims=[];log=[]
    pg.evaluate("()=>document.getElementById('labslow').click()")
    pg.wait_for_function('()=>window.__tb.G.labU.hid',timeout=20000,polling=10)
    for t in range(16):
        pg.wait_for_timeout(40);ims.append(Image.open(io.BytesIO(pg.screenshot())).crop((0,300,780,1300)));log.append(pg.evaluate("()=>{const u=window.__tb.G.labU;return [u.hid?1:0,+(u.sink||0).toFixed(2),u.mode].join(' ')}"))
    print(log)
    W=Image.new('RGB',(780*16,1000));[W.paste(t,(i*780,0)) for i,t in enumerate(ims)];W.resize((260*16,333)).save(sys.argv[2])
    print(errs[:3]);b.close()
