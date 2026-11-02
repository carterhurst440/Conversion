import sys,base64,pathlib
from playwright.sync_api import sync_playwright
glb=sys.argv[1];out=sys.argv[2]
base=pathlib.Path('node_modules/three')
b64=base64.b64encode(open(glb,'rb').read()).decode()
html=f"""<html><body style='margin:0;background:#dfe8d8'><script src='three.min.js'></script><script src='GLTFLoader.js'></script><script>
const r=new THREE.WebGLRenderer({{antialias:true,preserveDrawingBuffer:true}});r.setSize(1200,600);document.body.appendChild(r.domElement);
const bin=Uint8Array.from(atob('{b64}'),c=>c.charCodeAt(0)).buffer;
new THREE.GLTFLoader().parse(bin,'',g=>{{const sc=new THREE.Scene();sc.background=new THREE.Color('#dfe8d8');sc.add(new THREE.AmbientLight(0xffffff,.7));const d=new THREE.DirectionalLight(0xffffff,.6);d.position.set(1,2,3);sc.add(d);
 sc.add(g.scene);const box=new THREE.Box3().setFromObject(g.scene);const c=box.getCenter(new THREE.Vector3()),s=box.getSize(new THREE.Vector3());window.INFO=[box.min.toArray(),box.max.toArray()];
 const views=[[0,0,1],[1,0,0],[0,0,-1],[-1,0,0]];r.setScissorTest(true);
 views.forEach((v,i)=>{{const cam=new THREE.OrthographicCamera(-s.y*.6,s.y*.6,s.y*.6,-s.y*.6,.01,100);cam.position.copy(c).add(new THREE.Vector3(...v).multiplyScalar(10));cam.lookAt(c);r.setViewport(i*300,0,300,600);r.setScissor(i*300,0,300,600);cam.left=-s.y*.3;cam.right=s.y*.3;cam.updateProjectionMatrix();r.render(sc,cam)}});window.DONE=1}});
</script></body></html>"""
pathlib.Path(base/'view.html').write_text(html)
with sync_playwright() as pw:
    b=pw.chromium.launch(args=['--use-gl=swiftshader','--enable-webgl','--ignore-gpu-blocklist']);pg=b.new_page(viewport={'width':1200,'height':600})
    errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+str((base/'view.html').resolve()));pg.wait_for_function('window.DONE',timeout=60000);print(pg.evaluate('window.INFO'));pg.screenshot(path=out);print(errs);b.close()
