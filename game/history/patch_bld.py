F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
# ---------- 1) ground troops can't walk through buildings (they slide along walls and path round them) ----------
rep("function stepToward(u,tx,ty,dt,arrive){","const blkAt=(x,y)=>{const X=Math.floor(x),Y=Math.floor(y);if(!inb(X,Y))return false;const b=cells[idx(X,Y)];return!!b&&!b.obst&&b.type!=='sandtrap'};\nfunction stepToward(u,tx,ty,dt,arrive){")
rep("if(!U[u.type].air&&!U[u.type].water&&!landAt(nx,ny)){if(landAt(nx,u.y))ny=u.y;else if(landAt(u.x,ny))nx=u.x;else{u.moving=false;return false}}",
    "if(!U[u.type].air&&!U[u.type].water&&!landAt(nx,ny)){if(landAt(nx,u.y))ny=u.y;else if(landAt(u.x,ny))nx=u.x;else{u.moving=false;return false}}\n  if(!U[u.type].air&&!u.leap&&!blkAt(u.x,u.y)&&blkAt(nx,ny)){if(!blkAt(nx,u.y)&&landAt(nx,u.y))ny=u.y;else if(!blkAt(u.x,ny)&&landAt(u.x,ny))nx=u.x;else{const tb=cells[cellAt(tx,ty)];if(!u.path||!u.path.length){const e=bfs(cellAt(u.x,u.y),c=>tb&&!tb.obst?distB(cx_(c),cy_(c),tb)<.9:Math.hypot(cx_(c)-tx,cy_(c)-ty)<1.2,5000);if(e>=0)u.path=trace(e)}u.moving=false;return false}}")
# ---------- 2) the main Church/Pyramid is 4x4, and every Church/Temple matches it ----------
rep("hall:{name:'Church',hp:2400,s:2,","hall:{name:'Church',hp:2400,s:4,")
rep("function startLayout(k){const h=hallPos(k);place(k,'hall',h.x,h.y)}","function startLayout(k){const h=hallPos(k);place(k,'hall',h.x-1,h.y-1)}")
rep("Needs a clear 2\\u00d72 patch of your land.","Needs a clear '+sz+'\\u00d7'+sz+' patch of your land.")
rep("if(!inb(X,Y)||!land[idx(X,Y)]||cells[idx(X,Y)]||beachA[idx(X,Y)]||ownerAt(X,Y)!==side)","if(!inb(X,Y)||!land[idx(X,Y)]||cells[idx(X,Y)]||beachA[idx(X,Y)]||(type!=='chapel'&&ownerAt(X,Y)!==side))")
s=s.replace("why:'Needs a clear '+sz+'","why:'Needs a clear '+sz+'")
rep("drawBld(b,sx,sy,Z,true)","drawBld(b,sx,sy,Z*(b.type==='hall'?b.s/2:b.type==='chapel'?b.s*.82:1),true)")
for a,b in[("S.hall.x+1","bcx(S.hall)"),("S.hall.y+1","bcy(S.hall)"),("S0.hall.x+1","bcx(S0.hall)"),("S0.hall.y+1","bcy(S0.hall)"),
           ("const h=G.S[k].hall,hx=h.x+1,hy=h.y+1","const h=G.S[k].hall,hx=bcx(h),hy=bcy(h)"),("Math.floor(h.x+1+rnd(-11,11)),y=Math.floor(h.y+1+rnd(-11,11))","Math.floor(bcx(h)+rnd(-11,11)),y=Math.floor(bcy(h)+rnd(-11,11))"),
           ("const h=seen[G.rivI].hall;centerOnPt(h.x+1,h.y+1)","const h=seen[G.rivI].hall;centerOnPt(bcx(h),bcy(h))")]:
    c=s.count(a);assert c>=1,(a,c);s=s.replace(a,b)
s=s.replace("G.S[0].hall.x+1","bcx(G.S[0].hall)").replace("G.S[0].hall.y+1","bcy(G.S[0].hall)")
# villages: a 4x4 plaza (where the Church will stand) ringed by huts
rep("VILLS.forEach((v,vi)=>{for(let y=v.y-2;y<=v.y+2;y++)for(let x=v.x-2;x<=v.x+2;x++)","VILLS.forEach((v,vi)=>{for(let y=v.y-2;y<=v.y+5;y++)for(let x=v.x-2;x<=v.x+5;x++)")
rep("const sp=[[-1,-1],[1,-1],[-1,1],[1,1],[0,-2],[-2,0]];shuffle(sp);for(const[a,b]of sp.slice(0,3+(R()*2|0))){","const sp=[[0,0],[3,0],[0,3],[3,3],[1,0],[2,0],[0,1],[0,2],[3,1],[3,2],[1,3],[2,3]];shuffle(sp);for(const[a,b]of sp.slice(0,6+(R()*3|0))){")
rep("if(x<4||y<4||x>WN-5||y>WN-5||!land[i]||beachA[i]||ldist[i]<3","if(x<5||y<5||x>WN-9||y>WN-9||!land[i]||beachA[i]||ldist[i]<4||[[0,0],[3,0],[0,3],[3,3]].some(([a,b])=>{const j=idx(x+a,y+b);return!land[j]||beachA[j]||ldist[j]<2})")
rep("VILLS.some(v=>Math.hypot(v.x-x,v.y-y)<4.5)","VILLS.some(v=>Math.hypot(v.x+1.5-x,v.y+1.5-y)<6)")
s=s.replace("(v.x+.5,v.y+.5,hT(v.x+.5,v.y+.5))","(v.x+2,v.y+2,hT(v.x+2,v.y+2))")
rep("chapel:{name:'Church',hp:700,","chapel:{name:'Church',hp:700,s:4,")
# ---------- 3) every world builds its villages its own way ----------
a=s.index("}else if(k==='hut'){");b=s.index("    if(own>=0){const fx=sx+rx*.9,fy=ty-2*s;",a)
s=s[:a]+r"""}else if(k==='hut'){const vi=x!=null?HUTV[idx(x,y)]:-1,v=G&&G.villages&&vi>=0?G.villages[vi]:null,own=v?villageOwner(v):-1,hs2=(hs%7)/7;const th=(G&&G.theme)||THEME;
    ctx.fillStyle='rgba(60,44,30,.18)';ctx.beginPath();ctx.ellipse(sx+2*s,sy+2*s,15*s,7*s,0,0,TAU);ctx.fill();
    const rx=11*s,ry=5.5*s;let wh=9*s;
    const drum=(c1,c2,h)=>{ctx.fillStyle=c1;ctx.fillRect(sx-rx,sy-h,rx,h);ctx.fillStyle=c2;ctx.fillRect(sx,sy-h,rx,h);ctx.fillStyle=c1;ctx.beginPath();ctx.ellipse(sx,sy,rx,ry,0,Math.PI/2,Math.PI);ctx.lineTo(sx,sy);ctx.fill();ctx.fillStyle=c2;ctx.beginPath();ctx.ellipse(sx,sy,rx,ry,0,0,Math.PI/2);ctx.lineTo(sx,sy);ctx.fill()};
    const box=(w,d,h,y0,cT,cL,cR)=>{const P=(u,v,z)=>[sx+(u-v)*w,sy+(u+v)*d*.5-z-y0];ctx.fillStyle=cL;poly([P(-1,1,0),P(1,1,0),P(1,1,h),P(-1,1,h)].flat());ctx.fillStyle=cR;poly([P(1,-1,0),P(1,1,0),P(1,1,h),P(1,-1,h)].flat());ctx.fillStyle=cT;poly([P(-1,-1,h),P(1,-1,h),P(1,1,h),P(-1,1,h)].flat())};
    let ty;
    if(th==='volcano'){wh=11*s;box(10*s,10*s,wh,0,'#3a3236','#2a2428','#1f1a1e');ctx.fillStyle='#ffb04a';glow(sx-5*s,sy-5*s,7*s,'#ff7a2a',.6);ctx.fillRect(sx-7*s,sy-7*s,4*s,4*s);ty=sy-wh;
      ctx.fillStyle='#4a3a3a';ctx.beginPath();ctx.moveTo(sx-11*s,ty);ctx.lineTo(sx,ty-9*s);ctx.lineTo(sx+11*s,ty);ctx.lineTo(sx,ty+5*s);ctx.closePath();ctx.fill();ctx.fillStyle='#2a2024';ctx.fillRect(sx+3*s,ty-12*s,3*s,8*s);
      ctx.fillStyle='rgba(90,80,90,.35)';for(let i=0;i<3;i++){const k=((time*.6+i/3+hs2)%1);ctx.beginPath();ctx.arc(sx+4.5*s+k*4*s,ty-14*s-k*16*s,(2+k*4)*s,0,TAU);ctx.fill()}}
    else if(th==='mushroom'){const capC=['#d94a5a','#9a5ad9','#e0703a'][(hs%3)];ctx.fillStyle='#efe2c8';ctx.fillRect(sx-5*s,sy-12*s,10*s,12*s);ctx.fillStyle='#d9c8a8';ctx.fillRect(sx,sy-12*s,5*s,12*s);ctx.fillStyle='#6a4a36';ctx.beginPath();ctx.ellipse(sx-1.5*s,sy-2.5*s,2.2*s,3*s,0,0,TAU);ctx.fill();
      ty=sy-12*s;ctx.fillStyle=capC;ctx.beginPath();ctx.ellipse(sx,ty,15*s,(11+hs2*3)*s,0,Math.PI,0);ctx.fill();ctx.fillStyle=tint(capC,-.25);ctx.beginPath();ctx.ellipse(sx,ty,15*s,3.5*s,0,0,Math.PI);ctx.fill();ctx.fillStyle='#fff6ea';for(const[a,b,r]of[[-7,-6,2.2],[3,-9,2.6],[8,-4,1.8],[-1,-3,1.5]]){ctx.beginPath();ctx.ellipse(sx+a*s,ty+b*s,r*s,r*.7*s,0,0,TAU);ctx.fill()}
      glow(sx+3*s,sy-7*s,6*s,'#b8ffcf',.4);ctx.fillStyle='#d8ffe6';ctx.beginPath();ctx.arc(sx+3*s,sy-7*s,1.6*s,0,TAU);ctx.fill();ty-=6*s}
    else if(th==='moon'){ctx.fillStyle='#d8dce8';ctx.beginPath();ctx.ellipse(sx,sy,13*s,6.5*s,0,0,Math.PI);ctx.ellipse(sx,sy,13*s,13*s,0,Math.PI,0);ctx.fill();ctx.fillStyle='#b8bed0';ctx.beginPath();ctx.moveTo(sx,sy+6.5*s);ctx.ellipse(sx,sy,13*s,13*s,0,-Math.PI/2,0);ctx.lineTo(sx+13*s,sy);ctx.ellipse(sx,sy,13*s,6.5*s,0,0,Math.PI/2);ctx.fill();
      ctx.strokeStyle='rgba(120,130,160,.6)';ctx.lineWidth=1*s;ctx.beginPath();ctx.ellipse(sx,sy-4*s,12*s,5*s,0,Math.PI,0);ctx.stroke();ctx.fillStyle='#4f6b9a';ctx.beginPath();ctx.arc(sx-5*s,sy-5*s,2.6*s,0,TAU);ctx.fill();glow(sx-5*s,sy-5*s,6*s,'#9fd0ff',.5);
      ctx.fillStyle='#9aa2b8';ctx.fillRect(sx+2*s,sy-4*s,6*s,6*s);ty=sy-13*s;ctx.strokeStyle='#8a90a4';ctx.lineWidth=1.2*s;line(sx,ty,sx,ty-8*s);ctx.fillStyle=(Math.sin(time*3+hs)>0)?'#ff5a5a':'#7a3a3a';ctx.beginPath();ctx.arc(sx,ty-8*s,1.5*s,0,TAU);ctx.fill()}
    else if(th==='jungle'){ctx.strokeStyle='#5a3e24';ctx.lineWidth=2*s;for(const[a,b]of[[-8,2],[8,2],[-3,5],[4,-2]])line(sx+a*s,sy+b*s,sx+a*s,sy+b*s-9*s);const py=sy-9*s;ctx.fillStyle='#8a6a3a';ctx.beginPath();ctx.ellipse(sx,py,12*s,6*s,0,0,TAU);ctx.fill();
      ctx.fillStyle='#b88a52';ctx.fillRect(sx-8*s,py-9*s,8*s,9*s);ctx.fillStyle='#9a7040';ctx.fillRect(sx,py-9*s,8*s,9*s);ctx.fillStyle='#3a2a1a';ctx.fillRect(sx-5*s,py-6*s,3.2*s,6*s);ty=py-9*s;
      ctx.fillStyle='#4f8a3a';ctx.beginPath();ctx.moveTo(sx-13*s,ty+2*s);ctx.lineTo(sx,ty-12*s);ctx.lineTo(sx+13*s,ty+2*s);ctx.lineTo(sx,ty+6*s);ctx.closePath();ctx.fill();ctx.fillStyle='#3a6e2c';ctx.beginPath();ctx.moveTo(sx,ty-12*s);ctx.lineTo(sx+13*s,ty+2*s);ctx.lineTo(sx,ty+6*s);ctx.closePath();ctx.fill();
      ctx.strokeStyle='#6a4a2a';ctx.lineWidth=1.2*s;line(sx-9*s,sy+3*s,sx-6*s,py);line(sx-6*s,sy+3*s,sx-3*s,py)}
    else if(th==='mountains'){wh=9*s;box(10*s,9*s,wh,0,'#8a5a36','#7a4e2e','#5e3a22');ctx.strokeStyle='rgba(60,36,20,.5)';ctx.lineWidth=1*s;for(let i=1;i<4;i++)line(sx-10*s,sy+4.5*s-i*2.3*s,sx,sy+9*s-i*2.3*s);ctx.fillStyle='#ffd27a';glow(sx-5*s,sy-1*s,6*s,'#ffb04a',.5);ctx.fillRect(sx-6.5*s,sy-3*s,3*s,3*s);ty=sy-wh;
      ctx.fillStyle='#f4f8fc';ctx.beginPath();ctx.moveTo(sx-12*s,ty+1*s);ctx.lineTo(sx-2*s,ty-10*s);ctx.lineTo(sx+12*s,ty-3*s);ctx.lineTo(sx+2*s,ty+7*s);ctx.closePath();ctx.fill();ctx.fillStyle='#d6e2ee';ctx.beginPath();ctx.moveTo(sx-2*s,ty-10*s);ctx.lineTo(sx+12*s,ty-3*s);ctx.lineTo(sx+12*s,ty-1*s);ctx.lineTo(sx-2*s,ty-8*s);ctx.fill();
      ctx.fillStyle='#5a4a44';ctx.fillRect(sx+4*s,ty-10*s,3*s,7*s);ctx.fillStyle='rgba(200,206,220,.45)';for(let i=0;i<3;i++){const k=((time*.5+i/3+hs2)%1);ctx.beginPath();ctx.arc(sx+5.5*s+k*3*s,ty-12*s-k*14*s,(1.6+k*3)*s,0,TAU);ctx.fill()}}
    else{drum('#d9b98a','#bf9a68',wh);ctx.fillStyle='#4a3628';ctx.fillRect(sx-5*s,sy-6*s,4*s,6*s);
      ty=sy-wh;ctx.fillStyle='#b8924e';ctx.beginPath();ctx.moveTo(sx,ty-(11+hs2*4)*s);ctx.lineTo(sx-rx*1.2,ty);ctx.ellipse(sx,ty,rx*1.2,ry*1.2,0,Math.PI,0,true);ctx.closePath();ctx.fill();ctx.fillStyle='#977436';ctx.beginPath();ctx.moveTo(sx,ty-(11+hs2*4)*s);ctx.lineTo(sx,ty+ry*1.2);ctx.ellipse(sx,ty,rx*1.2,ry*1.2,0,Math.PI/2,0,true);ctx.closePath();ctx.fill()}
"""+s[b:]
# the plaza: a 4x4 square where the Church will rise, paved to suit the world, with its hearth at the middle
rep("ctx.fillStyle='rgba(222,196,150,.85)';ctx.beginPath();ctx.ellipse(px,py,26*Z,13*Z,0,0,TAU);ctx.fill();ctx.strokeStyle='rgba(150,118,80,.6)';ctx.lineWidth=1.4*Z;ctx.setLineDash([4*Z,4*Z]);ctx.beginPath();ctx.ellipse(px,py,20*Z,10*Z,0,0,TAU);ctx.stroke();ctx.setLineDash([]);",
    "{const PV={volcano:['rgba(70,58,62,.85)','rgba(255,140,60,.55)'],mushroom:['rgba(200,180,220,.8)','rgba(140,100,180,.6)'],moon:['rgba(214,218,232,.85)','rgba(120,130,170,.6)'],jungle:['rgba(150,120,72,.8)','rgba(90,70,40,.6)'],mountains:['rgba(236,242,250,.9)','rgba(140,150,170,.6)']}[G.theme]||['rgba(222,196,150,.85)','rgba(150,118,80,.6)'];const D=(a,b)=>[px+(a-b)*32*Z,py+(a+b)*16*Z];ctx.fillStyle=PV[0];poly([...D(-1.8,-1.8),...D(1.8,-1.8),...D(1.8,1.8),...D(-1.8,1.8)]);ctx.strokeStyle=PV[1];ctx.lineWidth=1.4*Z;ctx.setLineDash([4*Z,4*Z]);ctx.beginPath();ctx.moveTo(...D(-1.4,-1.4));ctx.lineTo(...D(1.4,-1.4));ctx.lineTo(...D(1.4,1.4));ctx.lineTo(...D(-1.4,1.4));ctx.closePath();ctx.stroke();ctx.setLineDash([])}")
# ---------- 4) fog of war toggle on the start screen ----------
rep("const FOG=false;","let FOG=false;try{FOG=localStorage.getItem('tb-fog')==='1'}catch(e){}")
rep('<p class="report" id="mapinfo" style="margin-top:6px"></p>','<div class="np" id="fpick">Fog of war <button data-f="0">Off</button><button data-f="1">On</button></div>\n     <p class="report" id="mapinfo" style="margin-top:6px"></p>')
rep("function newGame(np){","function syncFog(){document.querySelectorAll('#fpick button').forEach(b=>b.classList.toggle('on',(b.dataset.f==='1')===FOG))}\nsetTimeout(()=>{const fp=document.getElementById('fpick');if(!fp)return;syncFog();fp.onclick=e=>{const b=e.target.closest('button');if(!b)return;FOG=b.dataset.f==='1';try{localStorage.setItem('tb-fog',FOG?'1':'0')}catch(e2){}syncFog();if(G&&!G.started){computeVision();terrDirty=true}}},0);\nfunction newGame(np){")
# fog toggle also lives in the ••• menu, live during a game
rep("mk('adm','Admin',null,()=>openAdmin());","mk('fog','Fog of war',null,()=>{FOG=!FOG;try{localStorage.setItem('tb-fog',FOG?'1':'0')}catch(e){}syncFog();computeVision();terrDirty=true;const bb=document.getElementById('pbfog');if(bb)bb.textContent=FOG?'On':'Off';toast(FOG?'Fog of war on: you only see what your people can see.':'Fog of war off: the whole map is visible.')});setTimeout(()=>{const bb=document.getElementById('pbfog');if(bb)bb.textContent=FOG?'On':'Off'});\n  mk('adm','Admin',null,()=>openAdmin());")
# ---------- maps twice as big (240 x 240), with villages, obstacles and resources scaled to the area ----------
rep("const WN=120,HU=14,","const WN=240,MAPAR=(WN/120)**2,HU=14,")
rep("const want=10+(R()*3|0),okV=","const want=Math.round((10+(R()*3|0))*MAPAR*.6),okV=")
rep("for(let tr=0;tr<9000&&VILLS.length<want;tr++)","for(let tr=0;tr<9000*MAPAR&&VILLS.length<want;tr++)")
rep("const nc=13+(R()*5|0);","const nc=Math.round((13+(R()*5|0))*MAPAR);")
rep("else if(kind==='peak'||kind==='pines'){const n=16+(R()*5|0);","else if(kind==='peak'||kind==='pines'){const n=Math.round((16+(R()*5|0))*MAPAR);")
rep("else{const n=kind==='thicket'?24+(R()*8|0):18+(R()*6|0);","else{const n=Math.round((kind==='thicket'?24+(R()*8|0):18+(R()*6|0))*MAPAR);")
rep("for(let tr=0;tr<3000&&cov<landN*.4;tr++)","for(let tr=0;tr<3000*MAPAR&&cov<landN*.4;tr++)")
open(F,'w').write(s);print('buildings ok')
s=open(F).read()
rep("cam.z=clamp(cam.z,.28,1.7)","cam.z=clamp(cam.z,.16,1.7)")
open(F,'w').write(s);print('zoom ok')
s=open(F).read()
# big (4x4) churches: a troop standing off either front side is drawn in front of it, and a church turns see-through while any of your troops is behind it
rep("for(const u of G.units){if(u.x<x0-2||u.x>x1+2||u.y<y0-2||u.y>y1+2)continue;if(u.side!==0&&!seeAt(u.x,u.y))continue;if(!U[u.type].air)L.push([u.x+u.ox+u.y+u.oy+.45,2,u])}",
    "const BIG=G.B.filter(b=>b.s>=2&&b.x>=x0-6&&b.x<=x1+2&&b.y>=y0-6&&b.y<=y1+2);for(const b of BIG)b.seeThru=false;\n  for(const u of G.units){if(u.x<x0-2||u.x>x1+2||u.y<y0-2||u.y>y1+2)continue;if(u.side!==0&&!seeAt(u.x,u.y))continue;if(U[u.type].air)continue;let key=u.x+u.ox+u.y+u.oy+.45;const ux=u.x+(u.ox||0),uy=u.y+(u.oy||0);let ghost=0;\n    for(const b of BIG){if(ux<b.x-4||uy<b.y-4||ux>b.x+b.s+3||uy>b.y+b.s+3)continue;const bk=b.x+b.y+b.s+.6;if(ux>=b.x+b.s-.05||uy>=b.y+b.s-.05){if(key<bk)key=bk+.01}else if(!ghost&&key<bk&&ux>b.x-3.5&&uy>b.y-3.5)ghost=bk+.02}\n    L.push([key,2,u]);if(ghost)L.push([ghost,6,u])}")
rep("    else if(k===2){const[sx,sy]=unitScreen(o);if(onScreen(sx,sy))drawUnit(o,Z)}","    else if(k===2){const[sx,sy]=unitScreen(o);if(onScreen(sx,sy))drawUnit(o,Z)}\n    else if(k===6){const[sx,sy]=unitScreen(o);if(onScreen(sx,sy)){ctx.save();ctx.globalAlpha=.5;drawUnit(o,Z);ctx.restore()}}")
open(F,'w').write(s);print('depth ok')
s=open(F).read()
# 3D units on high-density phone screens: never let the sprite atlas run out (a unit with no atlas slot was drawn as nothing)
rep("let cells=new Map(),lastGT=null,frameNo=0,failed=false,atlK=1,","let cells=new Map(),lastGT=null,frameNo=0,failed=false,atlK=1,atlCap=1,")
rep("const P=Math.min(st.ty.ps*Z*DPR,st.ty.cap);list.push(","const P=Math.min(st.ty.ps*Z*DPR,st.ty.cap,ATLAS*.45/st.ty.W,ATLAS*.45/st.ty.H);list.push(")
rep("const bud=ATLAS*ATLAS*.5;const k=need>bud?Math.sqrt(bud/need):1;atlK+=(k-atlK)*(k<atlK?1:.05);","const bud=ATLAS*ATLAS*.5;atlCap=Math.min(1,atlCap*1.0008);const k=Math.min(atlCap,need>bud?Math.sqrt(bud/need):1);atlK+=(k-atlK)*(k<atlK?1:.05);")
rep("if(!sl){repackNext=true;STATS.miss=(STATS.miss||0)+1;continue}","if(!sl){repackNext=true;STATS.miss=(STATS.miss||0)+1;atlCap=Math.max(.3,Math.min(atlCap,atlK)*.85);continue}")
open(F,'w').write(s);print('atlas ok')
s=open(F).read()
rep("function drawTroop(u,sx,sy,s,fl){","function drawTroop(u,sx,sy,s,fl){if((u.type==='grainb'||u.type==='waterb'||u.type==='stoneb')&&!(R3D&&R3D.draw(u,sx,sy,s,fl))){const tt=u.type;u.type='sower';const r=drawTroop(u,sx,sy,s,fl);u.type=tt;return r}if(u.type==='grainb'||u.type==='waterb'||u.type==='stoneb')return sy-R3D.top(u)*s;")
open(F,'w').write(s);print('bearer fallback ok')
s=open(F).read()
# a rig whose pose ever goes bad (a non-number creeps into a bone) is rebuilt instead of staying invisible
rep("if(!st)st=create(u,ty);drive(u,st,dt);st.seen=frameNo}",
    "if(!st)st=create(u,ty);drive(u,st,dt);st.seen=frameNo;\n    if(st.chk==null){st.chk=[];st.scene.traverse(o=>{if(o.isSkinnedMesh&&!st.chk.length)st.chk=o.skeleton.bones.filter((b,i)=>i%6===0)});if(!st.chk.length&&st.ctl.U&&st.ctl.U.root)st.chk=[st.ctl.U.root]}\n    if(!Number.isFinite(st.ctl.S.x)||!Number.isFinite(st.ctl.S.z)||st.chk.some(b=>!Number.isFinite(b.matrixWorld.elements[13])||!Number.isFinite(b.quaternion.w))){dispose(st);CT.delete(u);STATS.reset=(STATS.reset||0)+1}}")
open(F,'w').write(s);print('nan guard ok')
s=open(F).read()
# icons and previews get their own strip of the atlas, so a crowded battlefield can never leave a card blank
rep("function allocSlot(w,h){for(const s of shelves){","let shelvesD=[];const DEMOY=Math.round(ATLAS*.78);\nfunction allocSlotD(w,h){for(const s of shelvesD){if(s.h>=h&&s.h<h*1.4){const f=s.free.findIndex(q=>q.w>=w&&q.w<w*1.5);if(f>=0)return s.free.splice(f,1)[0];if(s.x+w<=ATLAS){const q={x:s.x,y:s.y,w,h:s.h,shelf:s};s.x+=w;return q}}}\n  const y=shelvesD.reduce((m,s)=>Math.max(m,s.y+s.h),DEMOY);if(y+h>ATLAS){shelvesD=[];for(const[du]of DEMO){const q=slots.get(du);if(q&&q.shelf&&q.shelf.demo)slots.delete(du)}return null}const s={y,h,x:w,free:[],demo:1};shelvesD.push(s);return{x:0,y,w,h,shelf:s}}\nfunction allocSlot(w,h){for(const s of shelves){")
rep("const y=shelves.reduce((m,s)=>Math.max(m,s.y+s.h),0);if(y+h>ATLAS)return null;","const y=shelves.reduce((m,s)=>Math.max(m,s.y+s.h),0);if(y+h>DEMOY)return null;")
rep("if(!sl){sl=allocSlot(w,h);if(!sl)return false;slots.set(u,sl)}\n  const S=st.ctl.S,cam=st.cam;","if(!sl){sl=allocSlotD(w,h)||allocSlotD(w,h);if(!sl)return false;slots.set(u,sl)}\n  const S=st.ctl.S,cam=st.cam;")
rep("if(Math.abs(Z-slotZ)/slotZ>.08||repackNext){repackNext=false;slots.clear();shelves=[];","if(Math.abs(Z-slotZ)/slotZ>.08||repackNext){repackNext=false;slots.clear();shelves=[];shelvesD=[];")
rep("const bud=ATLAS*ATLAS*.5;atlCap","const bud=ATLAS*DEMOY*.55;atlCap")
open(F,'w').write(s);print('demo atlas ok')
s=open(F).read()
# the 3D renderer heals itself: a lost WebGL context (phones drop it under memory pressure) or a failed draw no longer switches 3D off for good
rep("function frame(){if(failed||!G)return;","let lost=false,failT=0;glc.addEventListener('webglcontextlost',e=>{e.preventDefault();lost=true;failed=true;failT=performance.now()},false);glc.addEventListener('webglcontextrestored',()=>{lost=false;heal()},false);\nfunction heal(){for(const st of CT.values())try{dispose(st)}catch(e){}CT.clear();for(const ds of DEMO.values())try{dispose(ds)}catch(e){}DEMO.clear();slots.clear();shelves=[];shelvesD=[];failed=false;STATS.heal=(STATS.heal||0)+1}\nwindow.__r3dLose=()=>{const x=renderer.getContext().getExtension('WEBGL_lose_context');if(x){x.loseContext();setTimeout(()=>x.restoreContext(),1500)}};\nfunction frame(){if(!G)return;if(!lost&&renderer.getContext().isContextLost()){lost=true;failed=true;failT=performance.now()}if(failed){if(!lost&&performance.now()-failT>2500)heal();else return}")
rep("try{(useOutline?effect:renderer).render(st.scene,cam)}catch(e){console.warn('R3D render',e);failed=true;return}","try{(useOutline?effect:renderer).render(st.scene,cam)}catch(e){console.warn('R3D render',e);failed=true;failT=performance.now();return}")
open(F,'w').write(s);print('r3d heal ok')
s=open(F).read()
rep("catch(e){console.warn('R3D tick',e);failed=true}","catch(e){console.warn('R3D tick',e);failed=true;failT=performance.now()}")
rep("catch(e){failed=true;return false}","catch(e){failed=true;failT=performance.now();return false}")
open(F,'w').write(s);print('r3d heal2 ok')
s=open(F).read()
# while 3D is down (e.g. the phone dropped it when you switched apps), troops are drawn from a snapshot of their own model instead of vanishing
rep("function draw(u,sx,sy,s,fl){const c=cells.get(u);","const SNAP={};\nfunction draw(u,sx,sy,s,fl){if(failed){const ty=TYU(u),sn=ty&&SNAP[ty.f];if(!sn||!(G&&G.units&&G.units.includes(u)))return false;const Ps=ty.ps*VW.Z,dw=ty.W*Ps,dh=ty.H*Ps;ctx.save();if((u.fx||0)-(u.fy||0)<0){ctx.translate(sx,0);ctx.scale(-1,1);ctx.translate(-sx,0)}ctx.drawImage(sn,sx-dw/2,sy-dh*(1-ty.a),dw,dh);ctx.restore();return true}const c=cells.get(u);")
rep("n++}\n    cells.set(it.u,","n++;if(!SNAP[ty.f]&&S.clip==='idle'&&(st.slotN||0)>20){try{const cv=document.createElement('canvas');cv.width=it.w;cv.height=it.h;cv.getContext('2d').drawImage(glc,sl.x,sl.y,it.w,it.h,0,0,it.w,it.h);SNAP[ty.f]=cv}catch(e){}}}\n    cells.set(it.u,")
rep("const owns=u=>!!TYU(u)&&!failed;","const owns=u=>!!TYU(u)&&(!failed||!!SNAP[TYU(u).f]);")
open(F,'w').write(s);print('snap ok')
s=open(F).read()
# a worker icon is only remembered once its 3D picture really drew; a stand-in drawn while 3D was loading or down is retried next time
rep("function uIconURL(k){const v=k+iconVer(k);return UIURL[v]||(UIURL[v]=unitIcon(k,44,48).toDataURL())}","function uIconURL(k){const v=k+iconVer(k);if(UIURL[v])return UIURL[v];unitIcon.ok=false;const url=unitIcon(k,44,48).toDataURL();if(v[k.length]!=='3'||unitIcon.ok)UIURL[v]=url;return url}")
rep("R3D.draw(u,w/2,h-3,sc*1.05,1);ctx.clearRect(0,0,w,h);if(R3D.draw(u,w/2,h-3,sc*1.05,1))return}","R3D.draw(u,w/2,h-3,sc*1.05,1);ctx.clearRect(0,0,w,h);if(R3D.draw(u,w/2,h-3,sc*1.05,1)){unitIcon.ok=true;return}}")
# while 3D is down, icons use the model's snapshot too
rep("function drawDemo(u,sx,sy,s,fl){const ty=TYU(u);if(!ty||failed)return false;","function drawDemo(u,sx,sy,s,fl){const ty=TYU(u);if(!ty)return false;if(failed){const sn=SNAP[ty.f];if(!sn)return false;const ss=u.icon?Math.max(.05,(sy-2)/(ty.top*ty.ps)):s,Ps=ty.ps*ss,dw=ty.W*Ps,dh=ty.H*Ps;ctx.drawImage(sn,sx-dw/2,sy-dh*(1-ty.a),dw,dh);return true}")
open(F,'w').write(s);print('icon cache ok')
