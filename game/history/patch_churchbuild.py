F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
# ---------- a worker has to reach a village to raise a church there ----------
rep("function villageOwner(v){",r"""function workerNear(side,x,y,r){return G.units.some(u=>u.side===side&&u.hp>0&&isSow(u)&&!u.leap&&Math.hypot(u.x-x-.5,u.y-y-.5)<r)}
function sendBuilder(side,x,y,t){const m=isl[idx(x,y)];let w=null,bd=1e9;for(const u of G.units){if(u.side!==side||u.hp<=0||!isSow(u)||u.leap||isl[cellAt(u.x,u.y)]!==m)continue;const d=Math.hypot(u.x-x,u.y-y)+(u.carry?3:0);if(d<bd){bd=d;w=u}}
  if(!w)return null;w.buildAt={x,y,t};w.mode='move';w.wt=null;w.pv=null;w.path=[];w.plan=0;w.gx=x+.5;w.gy=y+.5;w.tgt=null;pathTo(w,idx(x,y));return w}
function finishBuildAt(u,ba){const side=u.side,D=B[ba.t],me=side===0;
  if(count(side,ba.t)>=LIM(side,ba.t)){if(me)toast(`You already have the most ${D.name}s allowed.`);return}
  if(!can(side,D.cost)){if(me)toast(`Not enough materials for a ${BNm(side,ba.t)}. Gather more, then send a worker again.`,true);return}
  const c=canPlace(side,ba.t,ba.x,ba.y);if(!c.ok){if(me)toast(c.why,true);return}
  pay(side,D.cost);const b=place(side,ba.t,ba.x,ba.y);b.store=0;puff(ba.x+.5,ba.y+.5,10);ring(ba.x+.5,ba.y+.5,1.2,GODS[G.S[side].god]?GODS[G.S[side].god].col:'#f2c14e');
  if(me){toast(`Your ${U[u.type].name} claims the village. A new ${BNm(0,ba.t)} is rising.`);renderHUD(true)}
  const ai=G.ai&&G.ai[side];if(ai){const PL=EGY(side)?PLAN_E:PLAN;if(PL[ai.step]==='chapel'){ai.step++;ai.wait=0}}}
function villageOwner(v){""")
rep("  const c=canPlace(0,type,x,y);if(!c.ok){if(!quiet)toast(c.why);return}\n  pay(0,D.cost);const b=place(0,type,x,y);",
    "  const c=canPlace(0,type,x,y);if(!c.ok){if(!quiet)toast(c.why);return}\n  if(type==='chapel'&&!workerNear(0,x,y,2.6)){const w=sendBuilder(0,x,y,'chapel');if(!w){toast(`A ${FN(S.god,'sower')} has to reach this village to build here, and none can walk there.`,true);return}ring(x+.5,y+.5,1.3,'#f2c14e');toast(`Your ${U[w.type].name} is walking to the village. The ${BNm(0,'chapel')} rises when they arrive.`);exitBuild();renderHUD(true);return}\n  pay(0,D.cost);const b=place(0,type,x,y);")
rep("  if(!G.arena&&u.mode!=='move'&&u.mode!=='board'&&EGY(u.side)){const ej=",
    "  if(u.buildAt){if(Math.hypot(u.x-u.buildAt.x-.5,u.y-u.buildAt.y-.5)<2.6){const ba=u.buildAt;u.buildAt=null;finishBuildAt(u,ba)}else if(u.mode!=='move')u.buildAt=null}\n  if(!G.arena&&u.mode!=='move'&&u.mode!=='board'&&EGY(u.side)){const ej=")
# the computer sends a worker to the village it wants
rep("  const c=aiSpot(k,item);if(c<0){next();return}\n  pay(k,B[item].cost);place(k,item,c%WN,c/WN|0);next();",
    "  const c=aiSpot(k,item);if(c<0){next();return}\n  if(item==='chapel'&&!workerNear(k,c%WN,c/WN|0,2.6)){if(!G.units.some(u=>u.side===k&&u.buildAt))sendBuilder(k,c%WN,c/WN|0,'chapel');return}\n  pay(k,B[item].cost);place(k,item,c%WN,c/WN|0);next();")
# ---------- build mode: open villages glow, with a bouncing marker over each ----------
rep("  if(G.villages)for(const v of G.villages){if(cells[idx(v.x,v.y)]||!exp0[idx(v.x,v.y)])continue;",
r"""  if(G.villages&&buildMode==='chapel'&&spotMap){const pulse=.5+.5*Math.sin(time*4);for(const v of G.villages){const i=idx(v.x,v.y),[px,py]=pj(v.x+.5,v.y+.5,hT(v.x+.5,v.y+.5));if(!onScreen(px,py,80))continue;const open=spotMap[i]>=0;
      if(open){ctx.save();ctx.globalCompositeOperation='lighter';glow(px,py,(46+8*pulse)*Z,'#f2c14e',.35+.2*pulse);ctx.restore();ctx.strokeStyle=`rgba(242,193,78,${.75+.25*pulse})`;ctx.lineWidth=3.4*Z;ctx.beginPath();ctx.ellipse(px,py,(34+6*pulse)*Z,(17+3*pulse)*Z,0,0,TAU);ctx.stroke();ctx.strokeStyle='rgba(255,255,255,.8)';ctx.lineWidth=1.4*Z;ctx.beginPath();ctx.ellipse(px,py,(30+6*pulse)*Z,(15+3*pulse)*Z,0,0,TAU);ctx.stroke()}
      else{ctx.strokeStyle='rgba(120,110,130,.6)';ctx.lineWidth=2*Z;ctx.setLineDash([5*Z,5*Z]);ctx.beginPath();ctx.ellipse(px,py,30*Z,15*Z,0,0,TAU);ctx.stroke();ctx.setLineDash([])}}}
  if(G.villages)for(const v of G.villages){if(cells[idx(v.x,v.y)]||!exp0[idx(v.x,v.y)])continue;""")
rep("function drawWell(sx,sy,s,b){",r"""function drawVillageMarks(){if(buildMode!=='chapel'||!spotMap||!G.villages)return;const Z=VW.Z,b=reduceMotion?0:Math.abs(Math.sin(time*3.2))*10;
  for(const v of G.villages){const i=idx(v.x,v.y);if(spotMap[i]<0)continue;const[px,py]=pj(v.x+.5,v.y+.5,hT(v.x+.5,v.y+.5));if(!onScreen(px,py,80))continue;const ay=py-(62+b)*Z,s2=Math.max(.8,Z);
    ctx.fillStyle='#f2c14e';ctx.strokeStyle='#2b2440';ctx.lineWidth=2.2*s2;ctx.beginPath();ctx.moveTo(px,ay+14*s2);ctx.lineTo(px-11*s2,ay);ctx.lineTo(px-4.5*s2,ay);ctx.lineTo(px-4.5*s2,ay-12*s2);ctx.lineTo(px+4.5*s2,ay-12*s2);ctx.lineTo(px+4.5*s2,ay);ctx.lineTo(px+11*s2,ay);ctx.closePath();ctx.stroke();ctx.fill();
    const t=workerNear(0,v.x,v.y,2.6)?'Build here':'Send a worker';ctx.font=`800 ${Math.round(10.5*s2)}px Figtree,sans-serif`;const w=ctx.measureText(t).width+14*s2,h=17*s2,ty=ay-24*s2;ctx.fillStyle='rgba(43,36,64,.88)';rrect(px-w/2,ty-h/2,w,h,h/2);ctx.fill();ctx.fillStyle='#fbf6ee';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(t,px,ty+.5);ctx.textBaseline='alphabetic'}}
function drawWell(sx,sy,s,b){""")
open(F,'w').write(s);print('church build ok')
s=open(F).read()
rep("  for(const u of G.units)if(U[u.type].air&&(u.side===0||seeAt(u.x,u.y))){const[sx,sy]=unitScreen(u);if(onScreen(sx,sy))drawUnit(u,Z)}\n  // mummy bandages",
    "  for(const u of G.units)if(U[u.type].air&&(u.side===0||seeAt(u.x,u.y))){const[sx,sy]=unitScreen(u);if(onScreen(sx,sy))drawUnit(u,Z)}\n  drawVillageMarks();\n  // mummy bandages")
rep("$('bannertext').textContent=k==='wall'?'Tap or drag across glowing squares':","$('bannertext').textContent=k==='chapel'?`Tap a glowing village \\u00b7 ${n} open`:k==='wall'?'Tap or drag across glowing squares':")
rep("if(!n){buildMode=null;toast(k==='outpost'?","if(!n){buildMode=null;toast(k==='chapel'?'Every village you can reach is already claimed.':k==='outpost'?")
open(F,'w').write(s);print('marks hooked')
s=open(F).read()
rep("desc:'Another house for your faith, and how you grow: build it anywhere that isn\\u2019t a rival\\u2019s land and it claims the land around it.","desc:'Another house for your faith, and how you grow. It can only rise on one of the map\\u2019s villages, and one of your workers must walk there to build it. It claims the land around it.")
rep("Another Pyramid for Anubis, and how Egypt spreads: build it anywhere that isn\\u2019t a rival\\u2019s land and it claims the land around it.","Another Pyramid for Anubis, and how Egypt spreads. It can only rise on one of the map\\u2019s villages, and a Stonebearer, Grainbearer or Waterbearer must walk there to build it. It claims the land around it.")
open(F,'w').write(s);print('desc ok')
