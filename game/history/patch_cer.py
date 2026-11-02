import base64
F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
b64=lambda p:base64.b64encode(open(p,'rb').read()).decode()
# ---------- Cerberus (Greek): imported three-headed hound, rigged by us; three heads bite in a volley, the serpent tail strikes ----------
rep("',archer:'","',cer:'"+b64('glb/cer_g.glb')+"',archer:'")
rep("FACT.grkw=function(){",open('fact_cer.js').read()+"\nFACT.grkw=function(){")
rep("const GLAB=n=>({mh:{","const GLAB=n=>({mh:{cer:1.15,")
rep("TYPES.champ0b=TYPES.champ0;","TYPES.champ0b=TYPES.champ0;TYPES.g1_1={f:'cer',ps:50,vref:4,W:4.4,H:3.6,a:.2,cap:125,top:1.3,sh:26,atk:[['inferno',.7,1],['tribite',.36,1],['fang',.42,1],['inferno',.7,1],['maul',.26,1],['tribite',.36,1]]};TYPES.g1_1b=Object.assign({},TYPES.g1_1,{f:'cerb',atk:[['breath',.3,1],['tribite',.36,1],['breath',.3,1],['swipe',.208,1]]});")
rep("const TYU=u=>","const TYU=u=>u.type==='g1_1'&&!(window.MODELS&&window.MODELS.cer)?null:u.type==='g1_1b'&&!(window.MODELS&&window.MODELS.cerb)?null:")
rep("',archer:'","',cerb:'"+b64('glb/cerb_g.glb')+"',archer:'")
rep("FACT.grkw=function(){","FACT.cerb=function(){FACT.__cb=1;try{return FACT.cer()}finally{FACT.__cb=0}};\nFACT.grkw=function(){")
# Gates of Tartarus: the grown Cerberus's chosen special; the three-headed bite stays as a passive
rep("if(U[u.type].special==='heads'){u.slow=0;u.root=0}","if(U[u.type].special==='heads'||U[u.type].heads){u.slow=0;u.root=0}")
rep("if(t.special==='heads'){const fs=","if(t.special==='heads'||t.heads){const fs=")
rep("const isHoly=u=>U[u.type].champ!=null||!!U[u.type].gu;","const isHoly=u=>U[u.type].champ!=null||!!U[u.type].gu;\nif(U.g1_1){U.g1_1.heads=true;U.g1_1.special='hellgate';U.g1_1.desc='Three heads, three bites: every attack hits up to three different enemies, and all three heads can pour out a roaring stream of hellfire. The guardian of the gates can\\u2019t be slowed or held in place. Awakened, he can throw open the Gates of Tartarus: he howls, the ground splits in a ring of fire around him, everything near is blasted, and for 5 seconds the burning ground scorches every enemy inside while geysers of hellfire erupt under them.'}")
rep("const SPNAME={","const SPNAME={hellgate:'Gates of Tartarus',")
rep("  if(sp==='styx'){",r"""  if(sp==='hellgate'){u.hgCd=(u.hgCd==null?5:u.hgCd)-dt;if(u.hgT>0){u.hgT-=dt;u.path=[];u.moving=false;
      if(!u.hgHit&&u.hgT<=1.6-.7){u.hgHit=1;for(const e of G.units){if(!foeOf(u,e)||U[e.type].air)continue;const d=Math.hypot(e.x-u.x,e.y-u.y);if(d>3.2)continue;damageUnit(e,40,u);const k=(3.2-d)/3.2*.6,nx=e.x+(e.x-u.x)/(d||1)*k,ny=e.y+(e.y-u.y)/(d||1)*k;if(landAt(nx,ny)){e.x=nx;e.y=ny}}
        (G.hellgate||(G.hellgate=[])).push({x:u.x,y:u.y,r:3.2,t:5,side:u.side,src:u,gz:.35});ring(u.x,u.y,3.4,'#ff5a2a');ring(u.x,u.y,2.2,'#ffc27a');ring(u.x,u.y,1.2,'#ff5a2a');burst(u.x,u.y,['#ff5a2a','#ffc27a','#3a1010','#ff8a3a'],34);puff(u.x,u.y,16);float(u.x,u.y,'Gates of Tartarus!','#ff5a2a')}return true}
    if(u.hgCd>0)return false;if(u.side===0&&!(u.cast>G.t))return false;const[f]=nearestFoeUnit(u,3.5);if(!f&&u.side!==0){u.hgCd=.6;return false}
    u.hgT=1.6;u.hgHit=0;u.hgCd=18;u.cast=0;return true}
  if(sp==='styx'){""")
# the burning ground: scorches every enemy inside and throws up geysers under them
rep("G.pools=G.pools.filter(p=>p.t>0);",r"""G.pools=G.pools.filter(p=>p.t>0);
  if(G.hellgate&&G.hellgate.length){for(const h of G.hellgate){h.t-=dt;h.gz-=dt;const inn=G.units.filter(e=>e.side!==h.side&&e.hp>0&&!e.leap&&!U[e.type].air&&Math.hypot(e.x-h.x,e.y-h.y)<h.r);
    for(const e of inn){damageUnit(e,14*dt,h.src&&h.src.hp>0?h.src:{side:h.side});e.slow=Math.max(e.slow||0,.4)}
    if(h.gz<=0){h.gz=.5;const e=inn[Math.floor(R()*inn.length)];const gx=e?e.x:h.x+(R()-.5)*h.r*1.4,gy=e?e.y:h.y+(R()-.5)*h.r*1.4;(h.gs||(h.gs=[])).push({x:gx,y:gy,t:0});if(e)damageUnit(e,24,h.src&&h.src.hp>0?h.src:{side:h.side});burst(gx,gy,['#ff5a2a','#ffc27a','#ffe9a8'],12);puff(gx,gy,5)}
    if(h.gs)for(const g of h.gs)g.t+=dt;if(h.gs)h.gs=h.gs.filter(g=>g.t<.7)}G.hellgate=G.hellgate.filter(h=>h.t>0)}""")
rep("  for(const pl of G.pools){if(!seeAt(pl.x,pl.y))continue;",r"""  if(G.hellgate)for(const h of G.hellgate){if(!seeAt(h.x,h.y))continue;const[px,py]=pj(h.x,h.y,hT(h.x,h.y));if(!onScreen(px,py))continue;drawHellgate(px,py,Z,h)}
  for(const pl of G.pools){if(!seeAt(pl.x,pl.y))continue;""")
rep("function drawPool(x,y,s,a,r){",r"""function drawHellgate(x,y,s,h){const a=Math.min(1,h.t/.6,(5-h.t)/.25+.2),rx=h.r*30*s,ry=h.r*15*s;ctx.save();ctx.globalAlpha*=a;
  ctx.fillStyle='rgba(40,10,12,.45)';ctx.beginPath();ctx.ellipse(x,y,rx,ry,0,0,TAU);ctx.fill();glow(x,y,rx*.9,'#ff5a2a',.3);
  ctx.strokeStyle='rgba(255,120,50,.85)';ctx.lineWidth=2.2*s;for(let i=0;i<9;i++){const a0=i/9*TAU+.3;ctx.beginPath();ctx.moveTo(x+Math.cos(a0)*rx*.15,y+Math.sin(a0)*ry*.15);let px=x,py=y;for(let k=1;k<=4;k++){const aa=a0+Math.sin(i*3+k)*.25,rr=k/4*.95;px=x+Math.cos(aa)*rx*rr;py=y+Math.sin(aa)*ry*rr;ctx.lineTo(px,py)}ctx.stroke()}
  ctx.strokeStyle='rgba(255,200,120,.9)';ctx.lineWidth=3*s;ctx.beginPath();ctx.ellipse(x,y,rx,ry,0,0,TAU);ctx.stroke();
  for(let i=0;i<22;i++){const a2=i/22*TAU,fx=x+Math.cos(a2)*rx,fy=y+Math.sin(a2)*ry,hh=(10+Math.sin(time*11+i*1.7)*5+(i%3)*3)*s;ctx.fillStyle=i%2?'#ffc27a':'#ff5a2a';ctx.beginPath();ctx.moveTo(fx-3.5*s,fy);ctx.quadraticCurveTo(fx+Math.sin(time*7+i)*2*s,fy-hh*1.7,fx+3.5*s,fy);ctx.fill()}
  if(h.gs)for(const g of h.gs){const[gx,gy]=pj(g.x,g.y,hT(g.x,g.y)),k=g.t/.7,hh=(1-k)*70*s*Math.min(1,g.t*8);glow(gx,gy-hh*.5,22*s,'#ff7a3a',.55*(1-k));ctx.fillStyle='rgba(255,140,60,'+(.85*(1-k))+')';ctx.beginPath();ctx.moveTo(gx-7*s,gy);ctx.quadraticCurveTo(gx,gy-hh*1.3,gx+7*s,gy);ctx.fill();ctx.fillStyle='rgba(255,230,160,'+(.9*(1-k))+')';ctx.beginPath();ctx.moveTo(gx-3*s,gy);ctx.quadraticCurveTo(gx,gy-hh,gx+3*s,gy);ctx.fill()}
  ctx.restore()}
function drawPool(x,y,s,a,r){""")
rep("if(ty.f==='charonu'){if(u.styT>0){","if(ty.f==='cer'){if(u.hgT>0){special=true;if(S.clip!=='howl')c.playG('howl',1,Math.max(0,1.6-u.hgT));S.hold=true}else if(S.clip==='howl'&&S.hold)S.hold=false;if(u.hgT>0)special=true}\n  if(ty.f==='charonu'){if(u.styT>0){")
rep("styx:{nm:'Styx Surge',","hellgate:{nm:'Gates of Tartarus',cd:u=>u.hgCd==null?5:u.hgCd,max:18,col:'#ff5a2a',ic:'\\u2668'},styx:{nm:'Styx Surge',")
# Movement Lab: "Use special now" also clears cooldowns and grants the player's cast order
rep("$('labgo').onclick=()=>{const u=G&&G.labU;if(!u)return;for(const k in u){if(/T$/.test(k)&&k!=='atkT'&&typeof u[k]==='number'&&u[k]>0)u[k]=0}u.cd=0;",
    "$('labgo').onclick=()=>{const u=G&&G.labU;if(!u)return;for(const k in u){if(/(T|Cd)$/.test(k)&&k!=='atkT'&&typeof u[k]==='number'&&u[k]>0)u[k]=0}u.cd=0;u.cast=G.t+4;const fd=G.units.filter(e=>e.side!==u.side&&e.hp>0).sort((a,b)=>Math.hypot(a.x-u.x,a.y-u.y)-Math.hypot(b.x-u.x,b.y-u.y))[0];if(fd){u.castXY=[fd.x,fd.y];const d=Math.hypot(fd.x-u.x,fd.y-u.y),rg=Math.min(U[u.type].range||1,1.6);if(d>rg+.4){u.x=fd.x-(fd.x-u.x)/d*rg;u.y=fd.y-(fd.y-u.y)/d*rg;u.path=[]}face(u,fd.x,fd.y)}toast((spName(LAB.k)||'Special')+'!');return;")
open(F,'w').write(s);print('cerberus ok')
s=open(F).read()
# Dead Eye: the arrow leaves from the bow at the top of her leap and flies a straight line to the target's body
rep("G.shots.push({x:u.x,y:u.y,z:hT(u.x,u.y)+1.2,tgt:v,dmg:U[u.type].dmg*3.5,spd:16,kind:'arrow',side:u.side,src:u,col:'#4fd84a',power:1});","G.shots.push({x:u.x+(u.fx||0)*.25,y:u.y+(u.fy||0)*.25,z:hT(u.x,u.y)+2.25,tgt:v,dmg:U[u.type].dmg*3.5,spd:16,kind:'arrow',side:u.side,src:u,col:'#4fd84a',power:1,lin:1});")
rep("const dx=tx-s.x,dy=ty-s.y,d=Math.hypot(dx,dy);s.z+=(tz-s.z)*Math.min(1,dt*4);","const dx=tx-s.x,dy=ty-s.y,d=Math.hypot(dx,dy);if(s.lin){if(s.d0==null){s.d0=Math.max(.3,d);s.z0=s.z}s.z=tz+(s.z0-tz)*Math.min(1,d/s.d0)}else s.z+=(tz-s.z)*Math.min(1,dt*4);")
open(F,'w').write(s);print('dead eye ok')
