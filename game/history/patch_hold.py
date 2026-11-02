s=open('tidebreak.html').read()
def R(a,b,n=1):
  global s
  c=s.count(a);assert c==n,(a[:60],c);s=s.replace(a,b)
# village claim distance: measure from the middle of the 4x4 plaza, not its corner
R("function workerNear(side,x,y,r){return G.units.some(u=>u.side===side&&u.hp>0&&isSow(u)&&!u.leap&&Math.hypot(u.x-x-.5,u.y-y-.5)<r)}",
  "function workerNear(side,x,y,r){return G.units.some(u=>u.side===side&&u.hp>0&&isSow(u)&&!u.leap&&Math.hypot(u.x-x-2,u.y-y-2)<r+1)}")
R("if(u.buildAt){if(Math.hypot(u.x-u.buildAt.x-.5,u.y-u.buildAt.y-.5)<2.6)","if(u.buildAt){if(Math.hypot(u.x-u.buildAt.x-2,u.y-u.buildAt.y-2)<3.6)")
# Egyptian workers: Stop Work hold
R("if(!G.arena&&u.mode!=='move'&&u.mode!=='board'&&EGY(u.side)){const ej=","if(!G.arena&&!u.hold&&u.mode!=='move'&&u.mode!=='board'&&EGY(u.side)){const ej=")
R("if(t.civ&&u.mode!=='move'&&u.mode!=='board'&&!(t.fights","if(u.hold&&t.civ&&u.mode!=='move'&&u.mode!=='board'){if(u.mode!=='idle'){u.mode='idle';u.tgt=null;u.path=[]}u.moving=false;return}\n  if(t.civ&&u.mode!=='move'&&u.mode!=='board'&&!(t.fights")
R("const ks=[...new Set(sel.map(u=>U[u.type].special))];const key=ks.join(',');",
  "const ks=[...new Set(sel.map(u=>U[u.type].special))];const ew=G&&!G.arena&&EGY(0)?[...SEL].filter(u=>u.side===0&&u.hp>0&&EJOB[u.type]):[];if(ew.length)ks.push('__hold');const key=ks.join(',');")
R("for(const k of ks){const b=document.createElement('button');b.dataset.k=k;",
  "for(const k of ks){const b=document.createElement('button');b.dataset.k=k;if(k==='__hold'){b.style.setProperty('--gl','#e8c35a');b.innerHTML='<div class=\"ring\"></div><i></i><span></span>';b.onclick=e=>{e.stopPropagation();holdTog()};el.appendChild(b);continue}")
R("for(const b of el.children){const k=b.dataset.k,M=MANSP[k],",
  "for(const b of el.children){if(b.dataset.k==='__hold'){const h=ew.length&&ew.every(u=>u.hold);b.querySelector('i').textContent=h?'⚒':'✋';b.querySelector('span').textContent=h?'Back to work':'Stop work';b.querySelector('.ring').style.background=h?'#e8c35a':'rgba(255,255,255,.18)';continue}const k=b.dataset.k,M=MANSP[k],")
R("let SPAIM=null;","""let SPAIM=null;
const EJOB={sower:'mine',grainb:'farm',waterb:'water'};
function holdTog(){const ew=[...SEL].filter(u=>u.side===0&&u.hp>0&&EJOB[u.type]);if(!ew.length)return;const h=ew.every(u=>u.hold);
  for(const u of ew){if(h){u.hold=false;if(u.mode!=='move')setWork(u,EJOB[u.type],u.x,u.y);else u.work=null}else{u.hold=true;u.wt=null;if(u.mode!=='move'){u.mode='idle';u.ax=u.x;u.ay=u.y;u.path=[];u.tgt=null}}float(u.x,u.y,h?'Back to work':'Holding','#e8c35a')}SPXK=null;updSpx()}""")
open('tidebreak.html','w').write(s)
s=open('tidebreak.html').read()
def R(a,b,n=1):
  global s
  c=s.count(a);assert c==n,(a[:60],c);s=s.replace(a,b)
R("STATS.n=list.length;STATS.calls=renderer.info.render.calls}","STATS.n=list.length;STATS.calls=renderer.info.render.calls;STATS.tex=renderer.info.memory.textures;STATS.geo=renderer.info.memory.geometries;STATS.ct=CT.size;STATS.demo=DEMO.size}")
R("function dispose(st){st.scene.traverse(o=>{if(o.geometry)o.geometry.dispose();if(o.material){const ms=Array.isArray(o.material)?o.material:[o.material];for(const m of ms)m.dispose()}})}",
"""// GPU memory a unit holds (its bone texture, glows, sprites, decals) must be freed with the unit, or the GPU slowly fills and iOS drops the 3D view
let TCOL=null;for(const k of['Texture','CanvasTexture','DataTexture']){const B0=T[k];if(!B0||B0.__w)continue;const W=class extends B0{constructor(...a){super(...a);if(TCOL)TCOL.push(this)}};W.__w=1;try{T[k]=W}catch(e){}}
const SHT=new Set(),TPROPS=['map','emissiveMap','normalMap','alphaMap','aoMap','roughnessMap','metalnessMap','bumpMap','gradientMap','lightMap','specularMap'];let shtN=-1;
function sharedTex(){const M=window.MODELS||{},ks=Object.keys(M);if(ks.length===shtN)return;shtN=ks.length;for(const k of ks){const r=M[k]&&(M[k].scene||M[k]);if(r&&r.traverse)r.traverse(o=>{if(!o.material)return;for(const m of(Array.isArray(o.material)?o.material:[o.material]))for(const p of TPROPS)if(m[p])SHT.add(m[p])})}
  try{for(const k in TEXC)SHT.add(TEXC[k])}catch(e){}try{for(const k in TEX)SHT.add(TEX[k])}catch(e){}SHT.add(grad)}
function dispose(st){sharedTex();const tx=new Set(),sk=new Set();st.scene.traverse(o=>{if(o.isSkinnedMesh&&o.skeleton)sk.add(o.skeleton);if(o.geometry)o.geometry.dispose();if(o.material){const ms=Array.isArray(o.material)?o.material:[o.material];for(const m of ms){for(const p of TPROPS)if(m[p]&&m[p].isTexture)tx.add(m[p]);if(m.uniforms)for(const k in m.uniforms){const v=m.uniforms[k]&&m.uniforms[k].value;if(v&&v.isTexture)tx.add(v)}m.dispose()}}});
  for(const k of sk){try{k.dispose()}catch(e){}}if(st.own)for(const t of st.own)tx.add(t);for(const t of tx)if(!SHT.has(t))t.dispose()}""")
R("function create(u,ty){scene=new T.Scene();const sun=lights(scene);const ctl=FACT[ty.f]();",
  "function create(u,ty){scene=new T.Scene();const sun=lights(scene);const own=TCOL=[];let ctl;try{ctl=FACT[ty.f]()}finally{TCOL=null}")
R("const st={ctl,scene,cam,sun,ty,lx:null,lz:null,","const st={own,ctl,scene,cam,sun,ty,lx:null,lz:null,")
R("try{c.tick(dt,I)}catch(e){console.warn('R3D tick',e);failed=true;failT=performance.now()}",
  "TCOL=st.own;try{c.tick(dt,I)}catch(e){console.warn('R3D tick',e);failed=true;failT=performance.now()}TCOL=null")
open('tidebreak.html','w').write(s)
s=open('tidebreak.html').read()
def R(a,b,n=1):
  global s
  c=s.count(a);assert c==n,(a[:60],c);s=s.replace(a,b)
R("glc.addEventListener('webglcontextlost',e=>{e.preventDefault();","glc.addEventListener('webglcontextlost',e=>{e.preventDefault();STATS.lost=(STATS.lost||0)+1;")
R("function frame(){if(!G)return;","function frame(){STATS.failed=failed;if(!G)return;")
# graphics info overlay in the ••• menu so a phone can show what the 3D renderer is doing
R("mk('adm','Admin',null,()=>openAdmin());","""mk('gfx','Graphics info',null,()=>{let el=document.getElementById('gfxinfo');if(el){clearInterval(el._t);el.remove();return}el=document.createElement('div');el.id='gfxinfo';el.style.cssText='position:fixed;left:8px;top:calc(env(safe-area-inset-top,0px) + 54px);z-index:50;background:rgba(20,16,32,.82);color:#fff;font:600 11px ui-monospace,monospace;padding:6px 8px;border-radius:8px;pointer-events:none;white-space:pre';document.body.appendChild(el);
  const up=()=>{const R=window.__r3d||{},M=window.MODELS||{};el.textContent=`3D ${R.failed?'PAUSED':'ok'}  lost ${R.lost||0}  heal ${R.heal||0}\\nunits ${R.n||0}  rigs ${R.ct||0}+${R.demo||0}  miss ${R.miss||0}\\ntex ${R.tex||0}  geo ${R.geo||0}  models ${Object.keys(M).length}\\nframe ${((R.tick||0)+(R.render||0)).toFixed(1)}ms`};up();el._t=setInterval(up,500)});mk('adm','Admin',null,()=>openAdmin());""")
open('tidebreak.html','w').write(s)
s=open('tidebreak.html').read()
def R(a,b,n=1):
  global s
  c=s.count(a);assert c==n,(a[:60],c);s=s.replace(a,b)
# models now stream in from their own files: a unit whose model has not arrived yet is simply skipped, never pauses the 3D view
R("if(!st)st=create(u,ty);drive(u,st,dt);st.seen=frameNo;","if(!st){const keep=scene;try{st=create(u,ty)}catch(e){scene=keep;continue}}drive(u,st,dt);st.seen=frameNo;")
R("if(!st){const keep=scene;st=create(u,ty);CT.delete(u);scene=keep;","if(!st){const keep=scene;try{st=create(u,ty)}catch(e){scene=keep;return false}CT.delete(u);scene=keep;")
open('tidebreak.html','w').write(s)
s=open('tidebreak.html').read()
def R(a,b,n=1):
  global s
  c=s.count(a);assert c==n,(a[:60],c);s=s.replace(a,b)
# send the builder to the nearest open square just outside the village plaza (the plaza itself is full of huts, so a path into its corner can fail)
R("if(!w)return null;w.buildAt={x,y,t};w.mode='move';w.wt=null;w.pv=null;w.path=[];w.plan=0;w.gx=x+.5;w.gy=y+.5;w.tgt=null;pathTo(w,idx(x,y));return w}",
  "if(!w)return null;let tc=idx(x,y),td=1e9;for(let Y=y-1;Y<=y+4;Y++)for(let X=x-1;X<=x+4;X++){if(X>=x&&X<x+4&&Y>=y&&Y<y+4)continue;if(!inb(X,Y))continue;const j=idx(X,Y);if(!land[j]||cells[j]||isl[j]!==m)continue;const d=Math.hypot(w.x-X-.5,w.y-Y-.5);if(d<td){td=d;tc=j}}\n  w.buildAt={x,y,t};w.hold=false;w.mode='move';w.wt=null;w.pv=null;w.path=[];w.plan=0;w.gx=cx_(tc);w.gy=cy_(tc);w.tgt=null;pathTo(w,tc);return w}")
R("if(u.buildAt){if(Math.hypot(u.x-u.buildAt.x-2,u.y-u.buildAt.y-2)<3.6){const ba=u.buildAt;u.buildAt=null;finishBuildAt(u,ba)}else if(u.mode!=='move')u.buildAt=null}",
  "if(u.buildAt){if(Math.hypot(u.x-u.buildAt.x-2,u.y-u.buildAt.y-2)<3.9){const ba=u.buildAt;u.buildAt=null;finishBuildAt(u,ba)}else if(u.mode!=='move'){if(u.side===0)toast(`Your ${U[u.type].name} couldn\\u2019t reach the village. Walk them closer and try again.`,true);u.buildAt=null}}")
R("SEL:()=>SEL,","SEL:()=>SEL,tryPlace:(t,x,y)=>{buildMode=t;tryPlace(x,y)},")
open('tidebreak.html','w').write(s)
s=open('tidebreak.html').read()
a="toast(`A ${FN(S.god,'sower')} has to reach this village to build here, and none can walk there.`,true)"
assert s.count(a)==1
s=s.replace(a,"toast(`This village is on another island. Carry a ${FN(S.god,'sower')} over by ship, then try again.`,true)")
open('tidebreak.html','w').write(s)
s=open('tidebreak.html').read()
a="U.shadow.position.y=.004;scene.add(U.shadow);"
i=s.index("FACT.serpent=");j=s.index(a,i)
# the serpent's body is cut off at the ground, so diving and tunnelling read as going into the earth
s=s[:j]+a+"{const gp=new T.Plane(new T.Vector3(0,1,0),.002);try{if(typeof renderer!=='undefined')renderer.localClippingEnabled=true}catch(e){}scene.traverse(o=>{if(o.isMesh&&o!==U.shadow){for(const m of(Array.isArray(o.material)?o.material:[o.material]))m.clippingPlanes=[gp]}})}"+s[j+len(a):]
open('tidebreak.html','w').write(s)
