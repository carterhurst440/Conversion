import re
F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a)
    assert c==n,(c,a[:80])
    s=s.replace(a,b)

# ---------- three faiths: Celtic, Egyptian, Greek ----------
rep("{n:'Cernunnos',land:'Gaul',","{n:'Cernunnos',land:'Celtic',")
rep("const ACTIVE=[1,7,8,4,6],","const ACTIVE=[8,0,1],")
rep("let PICKGOD=[1,7,8,4,6][Math.random()*5|0];","let PICKGOD=[8,0,1][Math.random()*3|0];")
rep("{n:'Anubis',land:'Egypt',col:'#e8c35a',ab:'Weighing of Hearts',d:'Troops heal for a quarter of the damage they deal.'}",
    "{n:'Anubis',land:'Egypt',col:'#e8c35a',ab:'Weighing of Hearts',d:'Troops heal for a quarter of the damage they deal.',eco:'Egypt builds in stone alone: no wood at all. Sowers farm wheat, forage berries in the woods and quarry stone from day one. No Storehouses: every load goes back to a Pyramid. Wells add troop space and water new fields. Nubian Warriors train at the Pyramid, Mummies rise from the Wabet, and the Altar summons the Scarab Ark and the Sphinx. Crown the Pyramid with gold to make it the Great Pyramid.'}")

# ---------- Egypt helpers ----------
rep("const RES=['wood','stone','wheat','souls'];",
"""const RES=['wood','stone','wheat','souls'];
const EGY=side=>!!(typeof G!=='undefined'&&G&&G.S&&G.S[side]&&G.S[side].god===0);
function CX(side,c){if(!c||!c.wood||!EGY(side))return c;const o=Object.assign({},c);o.stone=(o.stone||0)+o.wood;delete o.wood;return o}
const EGX=new Set(['barracks','storehouse','camp','workshop','aerie']),RINGR={storehouse:4.5,well:3.5};""")
rep("function can(side,c){const r=G.S[side].res;","function can(side,c){c=CX(side,c);const r=G.S[side].res;")
rep("function pay(side,c){const r=G.S[side].res;","function pay(side,c){c=CX(side,c);const r=G.S[side].res;")
rep("function costHTML(c,plain){const r=plain?{}:G.S[0].res;","function costHTML(c,plain){if(!plain)c=CX(0,c);const r=plain?{}:G.S[0].res;")
rep("function hasT(side,k){if(!k)return true;","function hasT(side,k){if(!k)return true;if((k==='mining'||k==='quarry')&&EGY(side))return true;")
# AI research uses its own affordability check
rep("if(st.ok){const c=TECH[t].cost;","if(st.ok){const c=CX(k,TECH[t].cost);")
# demolish refunds in the coin actually paid
rep("const c=B[b.type].cost||{};for(const k in c)S.res[k]+=Math.floor(c[k]/2);","const c=CX(0,B[b.type].cost||{});for(const k in c)S.res[k]+=Math.floor(c[k]/2);")

# ---------- new buildings: Well and Wabet ----------
rep("  camp:{name:'Army Camp',",
"""  well:{name:'Well',hp:300,cost:{stone:60},house:5,sow:3.5,egy:1,desc:'Egypt\\u2019s lifeblood, and how Egypt grows its army: every Well adds 5 troop space. Its water also opens a farm ring 3\\u00bd squares wide where Sowers can farm and forage. Wells are not drop-offs: every load still goes back to a Pyramid.'},
  wabet:{name:'Wabet',hp:560,cost:{stone:120},egy:1,desc:'The embalming chamber. Priests purify the dead here and raise them again as Mummies. Needs the Great Pyramid.'},
  camp:{name:'Army Camp',""")
rep("const LIMIT={altar:[1,1,1,1,1],","const LIMIT={well:[3,6,8,8,8],wabet:[0,2,2,2,2],altar:[1,1,1,1,1],")
rep("function LIM(side,k){if(k==='altar')","function LIM(side,k){if(EGY(side)?EGX.has(k):B[k]&&B[k].egy)return 0;if(k==='altar')")
rep("const BTIME={storehouse:20,","const BTIME={well:15,wabet:40,storehouse:20,")
rep("const BGROUPS=[['Faith',['chapel','altar','veil']],['Army',['barracks']],['Farm',['storehouse']],['Defend',['tower','cannon','mortar','wall']]];",
"""const BGROUPS=[['Faith',['chapel','altar','veil']],['Army',['barracks']],['Farm',['storehouse']],['Defend',['tower','cannon','mortar','wall']]];
const BGROUPS_E=[['Faith',['chapel','altar','veil']],['Army',['wabet']],['Water',['well']],['Defend',['tower','cannon','mortar','wall']]];
const BGR=side=>EGY(side)?BGROUPS_E:BGROUPS;
const EGN={hall:'Pyramid',chapel:'Pyramid'};
function BD(side,k){const D=B[k];if(!EGY(side))return D;if(k==='chapel')return Object.assign({},D,{name:'Pyramid',desc:'Another Pyramid for Anubis, and how Egypt spreads: build it anywhere that isn\\u2019t a rival\\u2019s land and it claims the land around it. A drop-off for stone, wheat and berries, and it trains Sowers, Missionaries and Nubian Warriors. Crown it with gold to make it a Temple. (Egyptian troop space comes from Wells.)'});return D}""")

# troop space: Egypt from the Pyramid plus Wells, not from extra churches
rep("function cap(side){const S=G.S[side];let c=S&&S.hall?(S.tier>=2?10:5):0;for(const b of G.B)if(b.side===side&&b.type==='chapel'&&built(b))c+=b.temple?10:5;return c}",
    "function cap(side){const S=G.S[side],eg=EGY(side);let c=S&&S.hall?(S.tier>=2?10:5):0;for(const b of G.B){if(b.side!==side||!built(b))continue;if(b.type==='chapel'&&!eg)c+=b.temple?10:5;else if(b.type==='well')c+=B.well.house}return c}")
# storage: the Great Pyramid is the granary
rep("function capRes(side,r){if(r==='souls')return 1e9;let c=30;const S=G.S[side];",
    "function capRes(side,r){if(r==='souls')return 1e9;let c=30;const S=G.S[side];if(EGY(side))c+=(S.tier>=2?40:10)+(S.tech&&S.tech.granary?30:0)+(S.tech&&S.tech.vaults?45:0);")

# farm rings: Storehouses or Wells
ring_old="for(const b of G.B)if(b.side===side&&b.type==='storehouse'&&built(b))rs.push([b.x+.5,b.y+.5,B.storehouse.sow]);"
rep(ring_old,"for(const b of G.B)if(b.side===side&&RINGR[b.type]&&built(b))rs.push([b.x+.5,b.y+.5,RINGR[b.type]]);",2)
rep("for(const b of G.B)if(b.side===side&&b.type==='storehouse'&&built(b)&&Math.hypot(px-b.x-.5,py-b.y-.5)<=B.storehouse.sow)return true;",
    "for(const b of G.B)if(b.side===side&&RINGR[b.type]&&built(b)&&Math.hypot(px-b.x-.5,py-b.y-.5)<=RINGR[b.type])return true;")
rep("for(const b of G.B)if(b.side===0&&b.type==='storehouse')rings.push([b.x+.5,b.y+.5,B.storehouse.sow]);",
    "for(const b of G.B)if(b.side===0&&RINGR[b.type])rings.push([b.x+.5,b.y+.5,RINGR[b.type]]);")
rep("buildMode==='storehouse'||(selected&&selected.side===0&&(selected.type==='storehouse'||selected.type==='hall'))",
    "buildMode==='storehouse'||buildMode==='well'||(selected&&selected.side===0&&(selected.type==='storehouse'||selected.type==='well'||selected.type==='hall'))")

# ---------- foraging: Egyptian Sowers pick berries in the woods for wheat ----------
rep("function workTick(u,dt){const job=u.gj&&GJ[u.work]?u.gj:u.work,kind=JOBK[job],res=WRES[job];if(!kind)return false;",
    "function workTick(u,dt){const job=u.gj&&GJ[u.work]?u.gj:u.work,kind=JOBK[job],fg=job==='chop'&&EGY(u.side),res=fg?'wheat':WRES[job];if(!kind)return false;const PK=G.pick||(G.pick={}),picked=i=>fg&&PK[i]>G.t;")
rep("  if(j==null||dep[j]!==kind||cells[j]){u.wt=null;if((u.wsT=(u.wsT||0)-dt)>0)return!!u.carry;u.wsT=1.2;",
    "  if(j==null||dep[j]!==kind||cells[j]||picked(j)){u.wt=null;if((u.wsT=(u.wsT||0)-dt)>0)return!!u.carry;u.wsT=1.2;")
rep("for(const i of ringTiles(u.side)){if(dep[i]!==kind||cells[i]||cl.has(i)||isl[i]!==i0)continue;const x=i%WN,y=i/WN|0,sc=",
    "for(const i of ringTiles(u.side)){if(dep[i]!==kind||cells[i]||cl.has(i)||isl[i]!==i0||picked(i))continue;const x=i%WN,y=i/WN|0,sc=")
rep("{tree:'No trees in your rings',","{tree:fg?'No berries ripe in your rings':'No trees in your rings',")
rep("burst(cx_(j),cy_(j),kind==='tree'?['#a87650','#8fbf5a']:",
    "burst(cx_(j),cy_(j),fg?['#c2304a','#8fbf5a','#7a2a6a']:kind==='tree'?['#a87650','#8fbf5a']:")
rep("if(u.wp>=WORKT[job]*(hasT(u.side,'tools')?.6:1)){const x=j%WN,y=j/WN|0;dep[j]=null;fpl[j]=-1;wither[j]=kind==='tree'?1:kind==='wheat'?2:3;tileCol(x,y);G.gv++;puff(x+.5,y+.5,4);",
    "if(u.wp>=WORKT[job]*(fg?.55:1)*(hasT(u.side,'tools')?.6:1)){const x=j%WN,y=j/WN|0;if(fg){PK[j]=G.t+40;burst(x+.5,y+.5,['#c2304a','#e0506a','#7a2a6a'],6)}else{dep[j]=null;fpl[j]=-1;wither[j]=kind==='tree'?1:kind==='wheat'?2:3;tileCol(x,y);G.gv++;puff(x+.5,y+.5,4)}")
rep("function anyTarget(u,kind){const cl=claimedTiles(u),i0=isl[cellAt(u.x,u.y)];for(const i of ringTiles(u.side))if(dep[i]===kind&&!cells[i]&&!cl.has(i)&&isl[i]===i0)return true;return false}",
    "function anyTarget(u,kind){const cl=claimedTiles(u),i0=isl[cellAt(u.x,u.y)],fg=kind==='tree'&&EGY(u.side),PK=G.pick||{};for(const i of ringTiles(u.side))if(dep[i]===kind&&!cells[i]&&!cl.has(i)&&isl[i]===i0&&!(fg&&PK[i]>G.t))return true;return false}")
rep("['forest','Forest']","['forest',EGY(0)?'Forage':'Forest']",2)
# Egyptian AI leans on stone
rep("const want={farm:2+Math.floor(lv/2),forest:2+Math.floor(lv/2),mine:hasT(k,'mining')?1+Math.floor(lv/3):0};",
    "const want=EGY(k)?{farm:2+Math.floor(lv/2),forest:1+Math.floor(lv/3),mine:2+Math.floor(lv/2)}:{farm:2+Math.floor(lv/2),forest:2+Math.floor(lv/2),mine:hasT(k,'mining')?1+Math.floor(lv/3):0};")

# ---------- who trains where ----------
rep("const BATK={","Object.assign(U.g0_0,{bld:'hall',cost:{wheat:6},time:18,house:1});Object.assign(U.g0_1,{bld:'wabet',time:50});\nconst BATK={")
rep("const ks=b.type==='hall'||b.type==='chapel'?CIV.filter(k=>U[k].bld==='hall'):b.type==='barracks'?UORDER.filter(k=>U[k].bld==='barracks'||U[k].alt==='barracks'):b.type==='altar'&&S.god>=0?GUK[S.god]:[];",
    "const gk=w=>S.god>=0?GUK[S.god].filter(k=>U[k].bld===w):[];const ks=b.type==='hall'||b.type==='chapel'?[...CIV.filter(k=>U[k].bld==='hall'),...gk('hall')]:b.type==='barracks'?UORDER.filter(k=>U[k].bld==='barracks'||U[k].alt==='barracks'):b.type==='altar'?gk('altar'):b.type==='wabet'?gk('wabet'):[];")
rep("return'Your army is full. Build another Church, or turn a Church into a Temple, for more room.'",
    "return EGY(0)?'Your army is full. Dig another Well for more room.':'Your army is full. Build another Church, or turn a Church into a Temple, for more room.'")

# ---------- AI build order for Egypt ----------
rep("function aiBuild(ai){\n  const k=ai.side,S=G.S[k];let item=PLAN[ai.step];\n  if(!item)item=['tower','cannon','mortar','barracks','W4','chapel','TEMPLE','altar','storehouse','storehouse'][R()*10|0];\n  const next=()=>{if(ai.step<PLAN.length)ai.step++;ai.wait=0};",
    "function aiBuild(ai){\n  const k=ai.side,S=G.S[k],PL=EGY(k)?PLAN_E:PLAN;let item=PL[ai.step];\n  if(!item)item=(EGY(k)?['tower','cannon','mortar','well','W4','chapel','TEMPLE','altar','wabet','well']:['tower','cannon','mortar','barracks','W4','chapel','TEMPLE','altar','storehouse','storehouse'])[R()*10|0];\n  const next=()=>{if(ai.step<PL.length)ai.step++;ai.wait=0};")
rep("if(ai.wait>25&&ai.step<PLAN.length&&!['harbor','barracks','lumber','farm','HALL','altar'].includes(item)){next();return}",
    "if(ai.wait>25&&ai.step<PL.length&&!['harbor','barracks','lumber','farm','HALL','altar','well','wabet'].includes(item)){next();return}")
rep("const PLAN=['storehouse',","const PLAN_E=['well','well','chapel','HALL','wabet','tower','well','altar','harbor','chapel','TEMPLE','well','veil','W8','tower','cannon','wabet','altar','mortar','TEMPLE','W8','chapel','cannon','TEMPLE'];\nconst PLAN=['storehouse',")

# ---------- Pyramid look ----------
rep("function drawBld(b,sx,sy,s,live){",
r"""function drawPyr(sx,sy,s,a,H,capd,gc,b){blobShadow(sx,sy,s,a*40);
  const P=(u,v,z)=>[sx+(u-v)*32*s,sy+(u+v)*16*s-z*s],z0=4;
  ibox(sx,sy,s,a*1.12,a*1.12,0,z0,'#efe2c2','#dcc79c','#c3a979');
  const top=capd?1:.8,at=a*(1-top),zt=z0+H*top,L=P(-a,a,z0),Fr=P(a,a,z0),Rr=P(a,-a,z0),tL=P(-at,at,zt),tF=P(at,at,zt),tR=P(at,-at,zt),tB=P(-at,-at,zt);
  ctx.fillStyle='#ecd5a2';poly([...L,...Fr,...tF,...tL]);ctx.fillStyle='#c7a873';poly([...Fr,...Rr,...tR,...tF]);
  ctx.strokeStyle='rgba(122,92,52,.28)';ctx.lineWidth=.9*s;const n=Math.max(3,Math.round(H/9));
  for(let k=1;k<n;k++){const t=k/n*top,aa=a*(1-t),z=z0+H*t;const p1=P(-aa,aa,z),p2=P(aa,aa,z),p3=P(aa,-aa,z);ctx.beginPath();ctx.moveTo(p1[0],p1[1]);ctx.lineTo(p2[0],p2[1]);ctx.lineTo(p3[0],p3[1]);ctx.stroke()}
  {const d=[P(-.16*a,a,z0),P(.16*a,a,z0),P(.1*a,a*.9,z0+H*.14),P(-.1*a,a*.9,z0+H*.14)];ctx.fillStyle='#4a3a2c';poly(d.flat());const dg=P(0,a*.95,z0+H*.08);glow(dg[0],dg[1],7*s*a,gc,.35)}
  if(capd){const t0=.8,ac=a*(1-t0),zc=z0+H*t0,ap=P(0,0,z0+H),c1=P(-ac,ac,zc),c2=P(ac,ac,zc),c3=P(ac,-ac,zc);
    glow(ap[0],ap[1]+3*s,26*s*a,'#ffd86a',.55);ctx.fillStyle='#ffe28a';poly([...c1,...c2,...ap]);ctx.fillStyle='#d7a22c';poly([...c2,...c3,...ap]);
    if(!reduceMotion){const q=(time*.35+(b&&b.seed||0))%1;if(q<.25){const k=q/.25;ctx.fillStyle=`rgba(255,250,220,${Math.sin(k*Math.PI)})`;ctx.beginPath();ctx.arc(ap[0]-4*s*a+8*s*a*k,ap[1]+6*s*a,1.6*s,0,TAU);ctx.fill()}}}
  else{ctx.fillStyle='#f4e4bd';poly([...tL,...tF,...tR,...tB]);const c=P(0,0,zt);ibox(c[0],c[1],s,at*.5,at*.5,0,5*a+2,'#efe2c2','#dcc79c','#c3a979');}
}
function drawWell(sx,sy,s,b){blobShadow(sx,sy,s,20);ctx.save();
  const rx=13*s,ry=6.5*s,h=9*s;ctx.fillStyle='#c7a873';ctx.fillRect(sx-rx,sy-h,2*rx,h);ctx.beginPath();ctx.ellipse(sx,sy,rx,ry,0,0,Math.PI);ctx.fill();
  ctx.strokeStyle='rgba(122,92,52,.35)';ctx.lineWidth=.8*s;for(let k=1;k<3;k++){ctx.beginPath();ctx.ellipse(sx,sy-h*k/3,rx,ry,0,0,Math.PI);ctx.stroke()}
  ctx.fillStyle='#ecd5a2';ctx.beginPath();ctx.ellipse(sx,sy-h,rx,ry,0,0,TAU);ctx.fill();ctx.fillStyle='#3d7fa8';ctx.beginPath();ctx.ellipse(sx,sy-h,rx*.72,ry*.72,0,0,TAU);ctx.fill();
  const sh=reduceMotion?0:Math.sin(time*2+(b&&b.seed||0)*7);ctx.fillStyle=`rgba(190,235,255,${.45+.2*sh})`;ctx.beginPath();ctx.ellipse(sx-3*s,sy-h-1*s,rx*.32,ry*.22,0,0,TAU);ctx.fill();
  ctx.strokeStyle='#8a6650';ctx.lineWidth=2*s;line(sx-rx*.8,sy-h,sx-rx*.8,sy-h-18*s);line(sx+rx*.8,sy-h,sx+rx*.8,sy-h-18*s);ctx.lineWidth=2.4*s;line(sx-rx*.95,sy-h-17*s,sx+rx*.95,sy-h-17*s);
  ctx.strokeStyle='#d9c08a';ctx.lineWidth=.9*s;line(sx+2*s,sy-h-17*s,sx+2*s,sy-h-8*s);ctx.fillStyle='#a87650';ctx.fillRect(sx-.5*s,sy-h-9*s,5*s,4*s);
  ctx.fillStyle='#4f9a4a';for(const[ox,oy]of[[-15,3],[15,4]]){ctx.beginPath();ctx.ellipse(sx+ox*s,sy+oy*s-2*s,3*s,4.5*s,0,0,TAU);ctx.fill()}
  ctx.restore()}
function drawWabet(sx,sy,s,gc,b){blobShadow(sx,sy,s,26);
  const P=ibox(sx,sy,s,.38,.3,0,4,'#efe2c2','#dcc79c','#c3a979');
  const W=(u,v,z)=>[sx+(u-v)*32*s,sy+(u+v)*16*s-z*s],tp=(a,b2,z0,h,inset)=>{const A=W(-a,b2,z0),Bq=W(a,b2,z0),C=W(a,-b2,z0),At=W(-a+inset,b2-inset*.4,z0+h),Bt=W(a-inset,b2-inset*.4,z0+h),Ct=W(a-inset,-b2+inset*.4,z0+h),Dt=W(-a+inset,-b2+inset*.4,z0+h);
    ctx.fillStyle='#e6cf9c';poly([...A,...Bq,...Bt,...At]);ctx.fillStyle='#c4a46e';poly([...Bq,...C,...Ct,...Bt]);ctx.fillStyle='#f3e3bb';poly([...At,...Bt,...Ct,...Dt])};
  tp(.34,.26,4,17,.05);
  ctx.fillStyle=hexA(gc,.9);const bd=[W(-.3,.25,17),W(.3,.25,17),W(.3,.25,19.5),W(-.3,.25,19.5)];poly(bd.flat());
  const d=[W(-.08,.26,4),W(.08,.26,4),W(.08,.26,15),W(-.08,.26,15)];ctx.fillStyle='#2e2430';poly(d.flat());const dg=W(0,.27,8);glow(dg[0],dg[1],9*s,'#9fe0c8',.35);
  for(const u of[-.2,.2]){const p=W(u,.27,4);ctx.fillStyle='#f4ead6';ctx.fillRect(p[0]-1.6*s,p[1]-13*s,3.2*s,13*s);ctx.fillStyle=gc;ctx.fillRect(p[0]-2.2*s,p[1]-14.5*s,4.4*s,2*s)}
  const jar=(u,v,c)=>{const p=W(u,v,4);ctx.fillStyle=c;ctx.beginPath();ctx.ellipse(p[0],p[1]-3*s,2.4*s,3.4*s,0,0,TAU);ctx.fill();ctx.fillStyle='#2b2440';ctx.beginPath();ctx.arc(p[0],p[1]-7*s,1.6*s,0,TAU);ctx.fill()};
  jar(.37,.34,'#e8dcc0');jar(.37,.18,'#d9c08a');
  if(!reduceMotion){for(let i=0;i<3;i++){const q=(time*.3+i/3+(b&&b.seed||0))%1,p=W(-.1,0,21);ctx.fillStyle=`rgba(230,220,200,${(1-q)*.45})`;ctx.beginPath();ctx.arc(p[0]+Math.sin(q*5+i)*4*s,p[1]-q*22*s,(2+q*3)*s,0,TAU);ctx.fill()}}}
function drawBld(b,sx,sy,s,live){""")
rep("    case 'hall':{const S=live?G.S[b.side]:{tier:1,god:-1},tier=S.tier,god=S.tier>=2?S.god:-1;\n",
    "    case 'hall':{const S=live?G.S[b.side]:{tier:1,god:-1},tier=S.tier,god=S.tier>=2?S.god:-1;\n      if(live&&EGY(b.side)){drawPyr(sx,sy,s,.86,tier>=2?96:84,tier>=2,GODS[0].col,b);break}\n")
rep("    case 'chapel':{blobShadow(sx,sy,s,24);",
    "    case 'well':{drawWell(sx,sy,s,b);break}\n    case 'wabet':{drawWabet(sx,sy,s,GODS[0].col,b);break}\n    case 'chapel':{if(live&&EGY(b.side)){drawPyr(sx,sy,s,.4,b.temple?50:44,!!b.temple,GODS[0].col,b);break}blobShadow(sx,sy,s,24);")

# ---------- names & messages ----------
rep("function hallName(k){const S=G.S[k];return ",
    "function hallName(k){const S=G.S[k];if(S.god===0)return S.tier>=2?'Great Pyramid of Anubis':'Pyramid of Anubis';return ")
rep("toast(`Your Church is now the Temple of ${GODS[S.god].n}. +5 troop space.`)",
    "toast(S.god===0?'Gold crowns the Pyramid. The Great Pyramid of Anubis rises. +5 troop space.':`Your Church is now the Temple of ${GODS[S.god].n}. +5 troop space.`)")
rep("toast('This Church is now a Temple. +5 troop space.')",
    "toast(S.god===0?'Gold crowns this Pyramid. It is now a Temple.':'This Church is now a Temple. +5 troop space.')")
rep("s.innerHTML=`<div class=\"sh\"><h2>Build</h2><span class=\"tag\">${S.tier>=2?'Temple':'Church'} \\u00b7 army",
    "s.innerHTML=`<div class=\"sh\"><h2>Build</h2><span class=\"tag\">${EGY(0)?(S.tier>=2?'Great Pyramid':'Pyramid'):S.tier>=2?'Temple':'Church'} \\u00b7 army")
rep("  for(const[g,list]of BGROUPS){\n    s.insertAdjacentHTML","  for(const[g,list]of BGR(0)){\n    s.insertAdjacentHTML")
rep("for(const k of list){const D=B[k],lim=LIM(0,k)","for(const k of list){const D=BD(0,k),lim=LIM(0,k)")
rep("${locked?(k==='veil'?'Needs Altar':'Needs Temple')","${locked?(k==='veil'?'Needs Altar':EGY(0)?'Needs Great Pyramid':'Needs Temple')")
rep("toast(k==='veil'?'The Veil needs an Altar first.':k==='altar'?'Each Altar needs its own Temple. Turn a Church into a Temple first.':'Turn your Church into a Temple first.')",
    "toast(k==='veil'?'The Veil needs an Altar first.':EGY(0)?(k==='altar'?'Each Altar needs a gold-crowned Pyramid. Crown your Pyramid first.':'Crown your Pyramid with gold first.'):k==='altar'?'Each Altar needs its own Temple. Turn a Church into a Temple first.':'Turn your Church into a Temple first.')")
# hide wood for Egypt
rep("  {const up=incomeOf(0);for(const r of ['wood','stone','wheat']){",
    "  {const cw=$('c-wood');if(cw){const hd=EGY(0)?'none':'';if(cw.style.display!==hd)cw.style.display=hd}}\n  {const up=incomeOf(0);for(const r of ['wood','stone','wheat']){")
# Egypt starts with stone instead of wood
rep("$('startbtn').onclick=()=>{$('startover').hidden=true;G.started=true;",
    "$('startbtn').onclick=()=>{$('startover').hidden=true;for(const S2 of G.S)if(S2.god===0){S2.res.stone+=S2.res.wood+4;S2.res.wood=0}G.started=true;")

# ---------- welcome screen: faith cards ----------
rep("<i>Altar</i>${U[key].bn?","<i>${{hall:EGY(0)||k===0?'Pyramid':'Church',wabet:'Wabet',altar:'Altar'}[U[key].bld]||'Altar'}</i>${U[key].bn?")
rep("      d.insertAdjacentHTML('beforeend','<h4>Faith troops</h4>');",
    "      if(g.eco)d.insertAdjacentHTML('beforeend',`<h4>How ${g.land==='Egypt'?'Egypt':g.n} builds</h4><p class=\"eco\">${g.eco}</p>`);\n      d.insertAdjacentHTML('beforeend','<h4>Faith troops</h4>');")
open(F,'w').write(s)
print('ok',len(s))
s=open(F).read()
rep("const yy=sy-(b.type==='hall'?84:{","const yy=sy-(b.type==='hall'?(g===0?106:84):b.type==='chapel'&&g===0?62:{")
open(F,'w').write(s);print('badge ok')
s=open(F).read()
rep("if(live&&EGY(b.side)){drawPyr(sx,sy,s,.4,","if(live?EGY(b.side):EGY(0)){drawPyr(sx,sy,s,.4,")
rep("if(live&&EGY(b.side)){drawPyr(sx,sy,s,.86,","if(live?EGY(b.side):EGY(0)){drawPyr(sx,sy,s,.86,")
rep(".fd h4{margin:6px 0 0;",".fd p.eco{margin:4px 0 6px;font-size:12.5px;line-height:1.45;color:var(--ink-soft)}\n.fd h4{margin:6px 0 0;")
open(F,'w').write(s);print('icons ok')
s=open(F).read()
rep("const upB=(act,c)=>`<button class=\"upb${can(0,c)?'':' off'}\" data-act=\"${act}\" aria-label=\"Become Temple\"><span>\\u2191 Temple</span><small>${Object.entries(c)",
    "const upB=(act,c)=>`<button class=\"upb${can(0,c)?'':' off'}\" data-act=\"${act}\" aria-label=\"${EGY(0)?'Crown with gold':'Become Temple'}\"><span>\\u2191 ${EGY(0)?'Gold cap':'Temple'}</span><small>${Object.entries(CX(0,c))")
rep("if(S.tier<MAXT){hup=upB('up',TEMPLECOST);h+=`<div class=\"pd\">Becoming a Temple adds",
    "if(S.tier<MAXT){hup=upB('up',TEMPLECOST);h+=EGY(0)?`<div class=\"pd\">Crowning the Pyramid with a gold capstone makes it the Great Pyramid: 5 more troop space, a bigger store, tougher walls, and it opens the Wabet and the Altar.</div>`:`<div class=\"pd\">Becoming a Temple adds")
rep("if(b.type==='chapel'){if(!b.temple){hup=upB('ctemple',TEMPLECOST);h+=`<div class=\"pd\">Adds 5 troop space.",
    "if(b.type==='chapel'&&EGY(0)){if(!b.temple)hup=upB('ctemple',TEMPLECOST);h+=`<div class=\"pd\">${b.temple?'A gold-crowned Pyramid. It':'Crown it with gold to make it a Temple, which'} counts toward deeper research. Egyptian troop space comes from Wells.</div>`}else if(b.type==='chapel'){if(!b.temple){hup=upB('ctemple',TEMPLECOST);h+=`<div class=\"pd\">Adds 5 troop space.")
open(F,'w').write(s);print('upb ok')
s=open(F).read()
# ---- v2: wells are Egypt's only troop space; wells must hug a Pyramid; Egyptian troops cost ~2x wheat ----
rep("function cap(side){const S=G.S[side],eg=EGY(side);let c=S&&S.hall?(S.tier>=2?10:5):0;",
    "function cap(side){const S=G.S[side],eg=EGY(side);let c=S&&S.hall?(eg?5:S.tier>=2?10:5):0;")
rep("const LIMIT={well:[3,6,8,8,8],","const LIMIT={well:[40,40,40,40,40],")
rep("const EGX=new Set(","const WELLR=5.5,wellNear=(side,x,y)=>G.B.some(b=>b.side===side&&(b.type==='hall'||b.type==='chapel')&&built(b)&&Math.hypot(x+.5-b.x-(b.type==='hall'?1:.5),y+.5-b.y-(b.type==='hall'?1:.5))<=WELLR);\nconst EGX=new Set(")
rep("  if(type==='altar'&&!freeTemples(side)",
    "  if(type==='well'&&!wellNear(side,x,y))return{ok:false,why:'Water runs close to the Pyramids. Dig Wells within their ring.'};\n  if(type==='altar'&&!freeTemples(side)")
rep("  if(type==='altar'){for(const t of freeTemples(k)){",
    "  if(type==='well'){const c=[];for(const b of G.B){if(b.side!==k||(b.type!=='hall'&&b.type!=='chapel'))continue;const cx=b.x+(b.type==='hall'?1:.5),cy=b.y+(b.type==='hall'?1:.5);for(let y=Math.floor(cy-6);y<=cy+6;y++)for(let x=Math.floor(cx-6);x<=cx+6;x++){if(!inb(x,y))continue;const i=idx(x,y);if(dep[i]||seedA[i]||Math.hypot(x+.5-cx,y+.5-cy)<2.2)continue;if(canPlace(k,'well',x,y).ok)c.push(i)}}return c.length?c[R()*c.length|0]:-1}\n  if(type==='altar'){for(const t of freeTemples(k)){")
# well rings while placing
rep("  if(buildMode==='altar'){const g=G.S[0].god,",
    "  if(buildMode==='well'){ctx.save();ctx.setLineDash([7*Z,5*Z]);ctx.lineDashOffset=-time*8*Z;for(const b of G.B){if(b.side!==0||(b.type!=='hall'&&b.type!=='chapel')||!built(b))continue;const x=b.x+(b.type==='hall'?1:.5),y=b.y+(b.type==='hall'?1:.5),[cx,cy]=pj(x,y,hT(x,y));ctx.strokeStyle='rgba(30,60,90,.3)';ctx.lineWidth=4.4*Z;ctx.beginPath();ctx.ellipse(cx,cy,WELLR*45.25*Z,WELLR*22.63*Z,0,0,TAU);ctx.stroke();ctx.strokeStyle='rgba(110,190,240,.95)';ctx.lineWidth=2.2*Z;ctx.stroke()}ctx.restore()}\n  if(buildMode==='altar'){const g=G.S[0].god,")
# Egyptian wheat prices
rep("Object.assign(U.g0_0,{bld:'hall',cost:{wheat:6},time:18,house:1});Object.assign(U.g0_1,{bld:'wabet',time:50});",
    "Object.assign(U.g0_0,{bld:'hall',cost:{wheat:10},time:18,house:1});Object.assign(U.g0_1,{bld:'wabet',time:50,cost:{wheat:22}});U.g0_2.cost={wheat:30};U.g0_3.cost={wheat:50};\nObject.defineProperty(U.sower.cost,'egw',{value:5/3});Object.defineProperty(U.missionary.cost,'egw',{value:9/5});")
rep("function CX(side,c){if(!c||!c.wood||!EGY(side))return c;const o=Object.assign({},c);o.stone=(o.stone||0)+o.wood;delete o.wood;return o}",
    "function CX(side,c){if(!c||!(c.wood||c.egw)||!EGY(side))return c;const o=Object.assign({},c);if(o.wood){o.stone=(o.stone||0)+o.wood;delete o.wood}if(c.egw&&o.wheat)o.wheat=Math.round(o.wheat*c.egw);return o}")
rep("<small>${Object.entries(t.cost).filter(e=>e[1])","<small>${Object.entries(CX(0,t.cost)).filter(e=>e[1])")
rep("const k=b.queue.splice(i,1)[0];const c=U[k].cost;","const k=b.queue.splice(i,1)[0];const c=CX(0,U[k].cost);")
# words
rep("toast(S.god===0?'Gold crowns the Pyramid. The Great Pyramid of Anubis rises. +5 troop space.':","toast(S.god===0?'Gold crowns the Pyramid. The Great Pyramid of Anubis rises.':")
rep("makes it the Great Pyramid: 5 more troop space, a bigger store, tougher walls, and it opens the Wabet and the Altar.","makes it the Great Pyramid: a bigger store, tougher walls, and it opens the Wabet and the Altar. (Troop space still comes only from Wells.)")
rep("desc:'Egypt\\u2019s lifeblood, and how Egypt grows its army: every Well adds 5 troop space. Its water also opens a farm ring 3\\u00bd squares wide where Sowers can farm and forage. Wells are not drop-offs: every load still goes back to a Pyramid.'",
    "desc:'Water is scarce in Egypt, so Wells are the only way to grow your army: every Well adds 5 troop space. Dig them within 5\\u00bd squares of a Pyramid, as many as fit. Each also opens a small farm ring where Sowers can farm and forage. Not a drop-off: loads still go back to a Pyramid.'")
rep("Wells add troop space and water new fields. Nubian Warriors train at the Pyramid,",
    "Water is scarce: Pyramids give no troop space, only Wells do, and Wells must be dug close to a Pyramid. Every Egyptian troop costs about twice the wheat. Nubian Warriors train at the Pyramid,")
open(F,'w').write(s);print('v2 ok')
