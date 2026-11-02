F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
# ---------- 20% larger maps ----------
rep("const WN=100","const WN=120")
# ---------- state: impassable ground, villages, admin map pick ----------
rep("let SEED=1,STARTS=[],MAIN=0,terrDirty=true;","let SEED=1,STARTS=[],MAIN=0,terrDirty=true;const OBS=new Uint8Array(WN*WN),HUTV=new Int16Array(WN*WN).fill(-1);let VILLS=[],MAPPICK='random';const OBST={type:'obst',obst:true,side:-9,x:-1,y:-1,s:1,hp:1e9,max:1e9,queue:[]};\nconst MAPNAME={continent:'Highlands',straits:'Riven Straits',isles:'Fire Isles'};")
rep("const LIMIT={well:","B.obst={name:'Impassable ground',hp:1e9,desc:''};\nconst LIMIT={well:")
rep("const landAt=(x,y)=>{const X=Math.floor(x),Y=Math.floor(y);return inb(X,Y)&&!!land[idx(X,Y)]};","const landAt=(x,y)=>{const X=Math.floor(x),Y=Math.floor(y);return inb(X,Y)&&!!land[idx(X,Y)]&&!OBS[idx(X,Y)]};")
rep("return b=>b.side!==u.side&&b.type!=='wall'}","return b=>!b.obst&&b.side!==u.side&&b.type!=='wall'}")
rep("const f=b=>b.side!==u.side&&(b.type==='wall'||B[b.type].def||b.type==='hall');","const f=b=>!b.obst&&b.side!==u.side&&(b.type==='wall'||B[b.type].def||b.type==='hall');")
rep("?f:(b=>b.side!==u.side)}","?f:(b=>!b.obst&&b.side!==u.side)}")
rep("FULL={tree:1,wheat:1,rock:1,clay:1}","FULL={tree:1,wheat:1,rock:1,clay:1,peak:1,chasm:1,spire:1,hut:1}")
rep("if(dep[i]&&!cells[i]&&exp0[i])L.push([x+y+1,0,i])","if(dep[i]&&(!cells[i]||cells[i].obst)&&exp0[i])L.push([x+y+1,0,i])")
# ---------- world generation: three map types with their own nature ----------
rep("  land.fill(0);isl.fill(255);beachA.fill(0);dep.fill(null);ldist.fill(0);","  land.fill(0);isl.fill(255);beachA.fill(0);dep.fill(null);ldist.fill(0);OBS.fill(0);HUTV.fill(-1);VILLS=[];")
rep("MODE=rm<.38?'continent':rm<.68?'straits':'isles';","MODE=MAPPICK!=='random'?MAPPICK:rm<.38?'continent':rm<.68?'straits':'isles';")
rep("const e=elev[i],r=R();let t=r<.3?1:r<.64?2:r<.9?3:4;","const e=elev[i],r=R(),TH=MODE==='continent'?[.26,.52,.9]:MODE==='isles'?[.36,.78,.92]:[.3,.6,.9];let t=r<TH[0]?1:r<TH[1]?2:r<TH[2]?3:4;")
rep("  // heights\n  for(let vy=0;vy<=WN;vy++)",r"""  // villages: 10-12 natural sites, the only places a new church can be raised
  {const want=10+(R()*3|0),okV=i=>{const x=i%WN,y=i/WN|0;if(x<4||y<4||x>WN-5||y>WN-5||!land[i]||beachA[i]||ldist[i]<3||(sizes[isl[i]]||0)<70)return false;if(STARTS.some(h=>Math.hypot(h.x+1-x,h.y+1-y)<12))return false;return!VILLS.some(v=>Math.hypot(v.x-x,v.y-y)<10)};
    for(let tr=0;tr<9000&&VILLS.length<want;tr++){const i=(R()*WN*WN)|0;if(okV(i))VILLS.push({x:i%WN,y:i/WN|0,seed:R()})}
    if(VILLS.length<10)return false;
    VILLS.forEach((v,vi)=>{for(let y=v.y-2;y<=v.y+2;y++)for(let x=v.x-2;x<=v.x+2;x++)if(inb(x,y)){const i=idx(x,y);dep[i]=null;zone[i]=0}
      const sp=[[-1,-1],[1,-1],[-1,1],[1,1],[0,-2],[-2,0]];shuffle(sp);for(const[a,b]of sp.slice(0,3+(R()*2|0))){const i=idx(v.x+a,v.y+b);if(land[i]&&!beachA[i]){dep[i]='hut';OBS[i]=1;HUTV[i]=vi}}})}
  // impassable ground: mountain ridges in the Highlands, chasms on the Riven Straits, basalt spires on the Fire Isles
  {const kind=MODE==='continent'?'peak':MODE==='straits'?'chasm':'spire',near=(x,y)=>STARTS.some(h=>Math.hypot(h.x+1-x,h.y+1-y)<9)||VILLS.some(v=>Math.hypot(v.x-x,v.y-y)<4.5);
    const put=(x,y)=>{if(!inb(x,y))return;const i=idx(x,y);if(!land[i]||beachA[i]||OBS[i]||near(x,y)||ldist[i]<2)return;OBS[i]=1;dep[i]=kind;zone[i]=0};
    const n=kind==='spire'?16+(R()*6|0):kind==='peak'?9+(R()*4|0):11+(R()*4|0);
    for(let k=0;k<n;k++){let x=0,y=0,ok=false;for(let tr=0;tr<200&&!ok;tr++){x=4+R()*(WN-8)|0;y=4+R()*(WN-8)|0;const i=idx(x,y);ok=land[i]&&!beachA[i]&&ldist[i]>=3&&!near(x,y)}if(!ok)continue;
      if(kind==='spire'){const m=2+(R()*4|0);for(let q=0;q<m;q++)put(x+(R()*3|0)-1,y+(R()*3|0)-1)}
      else{let a=R()*TAU;const L=kind==='peak'?6+(R()*8|0):7+(R()*9|0);let fx=x+.5,fy=y+.5;for(let q=0;q<L;q++){put(Math.floor(fx),Math.floor(fy));if(kind==='peak'&&R()<.45)put(Math.floor(fx)+(R()<.5?1:0),Math.floor(fy)+(R()<.5?1:0));a+=(R()-.5)*(kind==='chasm'?1.1:.6);fx+=Math.cos(a);fy+=Math.sin(a)}}}
    // never seal off part of an island: open any obstacle that walls in a pocket
    for(let it=0;it<10;it++){const comp=new Int32Array(WN*WN).fill(-1),csz=[],cisl=[];let nc=0;
      for(let i=0;i<WN*WN;i++){if(!land[i]||OBS[i]||comp[i]>=0)continue;const q=[i];comp[i]=nc;for(let h=0;h<q.length;h++){const c=q[h],x=c%WN,y=c/WN|0;for(const[a,b]of N4){const X=x+a,Y=y+b;if(!inb(X,Y))continue;const m=idx(X,Y);if(land[m]&&!OBS[m]&&comp[m]<0){comp[m]=nc;q.push(m)}}}csz.push(q.length);cisl.push(isl[i]);nc++}
      const big={};for(let c=0;c<nc;c++){const k2=cisl[c];if(big[k2]==null||csz[c]>csz[big[k2]])big[k2]=c}
      let opened=false;for(let i=0;i<WN*WN;i++){if(!OBS[i]||dep[i]==='hut')continue;const x=i%WN,y=i/WN|0;for(const[a,b]of N4){const X=x+a,Y=y+b;if(!inb(X,Y))continue;const c=comp[idx(X,Y)];if(c>=0&&big[cisl[c]]!==c){OBS[i]=0;dep[i]=null;opened=true;break}}}
      if(!opened)break}}
  // heights
  for(let vy=0;vy<=WN;vy++)""")
rep("  tcol=new Array(WN*WN);tcrgb=new Array(WN*WN);tdim=new Array(WN*WN);\n  for(let y=0;y<WN;y++)for(let x=0;x<WN;x++){if(land[idx(x,y)])tileCol(x,y)}\n  wdist.fill(9);","  for(const v of VILLS){const cx=v.x,cy=v.y,hc=hv[cy*VN+cx];for(let vy=cy-3;vy<=cy+4;vy++)for(let vx=cx-3;vx<=cx+4;vx++){if(vx<0||vy<0||vx>WN||vy>WN||hv[vy*VN+vx]<.9)continue;const d=Math.max(Math.abs(vx-cx-.5),Math.abs(vy-cy-.5));hv[vy*VN+vx]+=(hc-hv[vy*VN+vx])*(d<=2?1:.5)}}\n  tcol=new Array(WN*WN);tcrgb=new Array(WN*WN);tdim=new Array(WN*WN);\n  for(let y=0;y<WN;y++)for(let x=0;x<WN;x++){if(land[idx(x,y)])tileCol(x,y)}\n  wdist.fill(9);")
rep("if(!beachA[i]&&dp==='clay')base=mixRgb(base,hexRgb(bi.clay[0]),.35);","if(!beachA[i]&&dp==='clay')base=mixRgb(base,hexRgb(bi.clay[0]),.35);if(!beachA[i]&&dp==='chasm')base=mixRgb(base,[58,44,40],.55);if(!beachA[i]&&dp==='spire')base=mixRgb(base,[70,60,58],.35);if(!beachA[i]&&dp==='peak')base=mixRgb(base,[150,146,140],.35);")
# ---------- new game: obstacles block the grid; villages go live ----------
rep("cells=new Array(WN*WN).fill(null);exp0.fill(0);","cells=new Array(WN*WN).fill(null);for(let i=0;i<WN*WN;i++)if(OBS[i])cells[i]=OBST;G.villages=VILLS.map(v=>Object.assign({},v));G.mapMode=MAPMODE;exp0.fill(0);")
# ---------- a new church only on an unclaimed village ----------
rep("  if(type==='chapel'){if(o>=0&&o!==side)return{ok:false,why:'That’s a rival’s land.'};","  if(type==='chapel'){if(!(G.villages||[]).some(v=>v.x===x&&v.y===y))return{ok:false,why:'A new church can only rise on a village. Claim one before a rival does.'};if(o>=0&&o!==side)return{ok:false,why:'That village lies in a rival\\u2019s land.'};")
rep("function aiSpot(k,type){\n  if(type==='chapel'){","function aiSpot(k,type){\n  if(type==='chapel'&&G.villages){const h=G.S[k].hall,m=isl[idx(h.x,h.y)];const vs=G.villages.filter(v=>isl[idx(v.x,v.y)]===m&&canPlace(k,'chapel',v.x,v.y).ok).sort((a,b)=>Math.hypot(a.x-h.x,a.y-h.y)-Math.hypot(b.x-h.x,b.y-h.y));return vs.length?idx(vs[0].x,vs[0].y):-1}\n  if(type==='chapel'){")
# ---------- Egypt: 4 Wells per Pyramid, 6 per Great Pyramid / crowned Pyramid ----------
rep("function LIM(side,k){","function LIM(side,k){if(k==='well'&&EGY(side)){const S=G.S[side];let n=S&&S.hall?(S.tier>=2?6:4):0;for(const b of G.B)if(b.side===side&&b.type==='chapel'&&built(b))n+=b.temple?6:4;return n}")
rep("Dig them within 5\\u00bd squares of a Pyramid, as many as fit.","Dig them within 5\\u00bd squares of a Pyramid: 4 for each Pyramid, 6 once it is crowned with gold.")
# ---------- drawing: villages, huts and the three kinds of impassable ground ----------
rep("  }else if(k==='rock'){\n    if(bi.rock==='crystal'){",r"""  }else if(k==='hut'){const vi=x!=null?HUTV[idx(x,y)]:-1,v=G&&G.villages&&vi>=0?G.villages[vi]:null,own=v?villageOwner(v):-1,hs2=(hs%7)/7;
    ctx.fillStyle='rgba(60,44,30,.18)';ctx.beginPath();ctx.ellipse(sx+2*s,sy+2*s,15*s,7*s,0,0,TAU);ctx.fill();
    const rx=11*s,ry=5.5*s,wh=9*s;ctx.fillStyle='#d9b98a';ctx.fillRect(sx-rx,sy-wh,rx,wh);ctx.fillStyle='#bf9a68';ctx.fillRect(sx,sy-wh,rx,wh);ctx.fillStyle='#d9b98a';ctx.beginPath();ctx.ellipse(sx,sy,rx,ry,0,Math.PI/2,Math.PI);ctx.lineTo(sx,sy);ctx.fill();ctx.fillStyle='#bf9a68';ctx.beginPath();ctx.ellipse(sx,sy,rx,ry,0,0,Math.PI/2);ctx.lineTo(sx,sy);ctx.fill();
    ctx.fillStyle='#4a3628';ctx.fillRect(sx-5*s,sy-6*s,4*s,6*s);
    const ty=sy-wh;ctx.fillStyle='#b8924e';ctx.beginPath();ctx.moveTo(sx,ty-(11+hs2*4)*s);ctx.lineTo(sx-rx*1.2,ty);ctx.ellipse(sx,ty,rx*1.2,ry*1.2,0,Math.PI,0,true);ctx.closePath();ctx.fill();ctx.fillStyle='#977436';ctx.beginPath();ctx.moveTo(sx,ty-(11+hs2*4)*s);ctx.lineTo(sx,ty+ry*1.2);ctx.ellipse(sx,ty,rx*1.2,ry*1.2,0,Math.PI/2,0,true);ctx.closePath();ctx.fill();
    if(own>=0){const fx=sx+rx*.9,fy=ty-2*s;ctx.strokeStyle='#5a4a3a';ctx.lineWidth=1.2*s;line(fx,fy,fx,fy-14*s);ctx.fillStyle=SIDE[own].c1;ctx.beginPath();ctx.moveTo(fx,fy-14*s);ctx.lineTo(fx+8*s,fy-11.5*s);ctx.lineTo(fx,fy-9*s);ctx.fill()}
  }else if(k==='peak'){const h0=(34+r1*20)*s,w=(hw*.9);
    ctx.fillStyle='rgba(40,34,50,.2)';ctx.beginPath();ctx.ellipse(sx+3*s,sy+2*s,hw*1.05,hh*1.05,0,0,TAU);ctx.fill();
    ctx.fillStyle='#8d8a90';ctx.beginPath();ctx.moveTo(sx-w,sy+2*s);ctx.lineTo(sx-w*.15,sy-h0);ctx.lineTo(sx+w*.05,sy-h0+4*s);ctx.lineTo(sx,sy+hh);ctx.fill();ctx.fillStyle='#6d6a73';ctx.beginPath();ctx.moveTo(sx,sy+hh);ctx.lineTo(sx+w*.05,sy-h0+4*s);ctx.lineTo(sx+w*.25,sy-h0*.8);ctx.lineTo(sx+w,sy+2*s);ctx.fill();
    ctx.fillStyle='#fbfbff';ctx.beginPath();ctx.moveTo(sx-w*.15,sy-h0);ctx.lineTo(sx-w*.38,sy-h0*.62);ctx.lineTo(sx-w*.18,sy-h0*.68);ctx.lineTo(sx-w*.05,sy-h0*.56);ctx.lineTo(sx+w*.05,sy-h0+4*s);ctx.fill();ctx.fillStyle='#dfe4ee';ctx.beginPath();ctx.moveTo(sx+w*.05,sy-h0+4*s);ctx.lineTo(sx-w*.05,sy-h0*.56);ctx.lineTo(sx+w*.12,sy-h0*.62);ctx.lineTo(sx+w*.25,sy-h0*.8);ctx.fill();
    if(r2>.5){const ox=sx+w*.55,oy=sy+hh*.2,h2=h0*.55;ctx.fillStyle='#7d7a82';ctx.beginPath();ctx.moveTo(ox-w*.5,oy);ctx.lineTo(ox,oy-h2);ctx.lineTo(ox+w*.45,oy);ctx.fill();ctx.fillStyle='#fbfbff';ctx.beginPath();ctx.moveTo(ox,oy-h2);ctx.lineTo(ox-w*.14,oy-h2*.7);ctx.lineTo(ox+w*.12,oy-h2*.72);ctx.fill()}
  }else if(k==='chasm'){const w=hw*.92,h=hh*.92;
    ctx.fillStyle='#3a2c28';poly([sx-w,sy,sx,sy-h,sx+w,sy,sx,sy+h]);ctx.fillStyle='#1d1416';poly([sx-w*.7,sy,sx,sy-h*.7,sx+w*.7,sy,sx,sy+h*.7]);
    const gl=.35+.15*Math.sin(time*1.6+hs);ctx.fillStyle=`rgba(255,110,60,${gl})`;poly([sx-w*.32,sy,sx,sy-h*.32,sx+w*.32,sy,sx,sy+h*.32]);
    ctx.fillStyle='#5a4640';poly([sx-w,sy,sx,sy+h,sx,sy+h+4*s,sx-w,sy+4*s]);ctx.fillStyle='#4a3934';poly([sx,sy+h,sx+w,sy,sx+w,sy+4*s,sx,sy+h+4*s]);
  }else if(k==='spire'){for(const[ox,oy,h0,w0]of[[-6,1,30,5],[5,3,22,4.5],[0,-3,16,4]]){const bx=sx+ox*s,by=sy+oy*s,h=(h0+r1*10)*s,w=w0*s;
      ctx.fillStyle='rgba(30,20,20,.22)';ctx.beginPath();ctx.ellipse(bx+2*s,by+1*s,w*1.6,w*.55,0,0,TAU);ctx.fill();
      ctx.fillStyle='#3b3438';poly([bx-w,by,bx,by+w*.45,bx+.5*s,by-h,bx-w*.7,by-h+w*.4]);ctx.fillStyle='#2a2428';poly([bx,by+w*.45,bx+w,by,bx+w*.6,by-h+w*.5,bx+.5*s,by-h]);
      ctx.strokeStyle=`rgba(255,120,50,${.55+.25*Math.sin(time*2+hs+ox)})`;ctx.lineWidth=1.1*s;ctx.beginPath();ctx.moveTo(bx-w*.3,by-h*.15);ctx.lineTo(bx-w*.1,by-h*.5);ctx.lineTo(bx-w*.35,by-h*.75);ctx.stroke()}
    glow(sx,sy-4*s,14*s,'#ff6a2a',.18)
  }else if(k==='rock'){
    if(bi.rock==='crystal'){""")
rep("function drawWell(sx,sy,s,b){","function villageOwner(v){const c=cells[idx(v.x,v.y)];return c&&c.type==='chapel'?c.side:-1}\nfunction drawWell(sx,sy,s,b){")
# plaza on unclaimed village centers (ground pass)
rep("  if(G.traps)for(const tp of G.traps){","  if(G.villages)for(const v of G.villages){if(cells[idx(v.x,v.y)]||!exp0[idx(v.x,v.y)])continue;const[px,py]=pj(v.x+.5,v.y+.5,hT(v.x+.5,v.y+.5));if(!onScreen(px,py))continue;\n    ctx.fillStyle='rgba(222,196,150,.85)';ctx.beginPath();ctx.ellipse(px,py,26*Z,13*Z,0,0,TAU);ctx.fill();ctx.strokeStyle='rgba(150,118,80,.6)';ctx.lineWidth=1.4*Z;ctx.setLineDash([4*Z,4*Z]);ctx.beginPath();ctx.ellipse(px,py,20*Z,10*Z,0,0,TAU);ctx.stroke();ctx.setLineDash([]);\n    ctx.fillStyle='#8a7a68';ctx.beginPath();ctx.ellipse(px,py,5*Z,2.6*Z,0,0,TAU);ctx.fill();const fl=reduceMotion?0:Math.sin(time*8+v.seed*9)*1.2*Z;glow(px,py-4*Z,9*Z,'#ffb04a',.5);ctx.fillStyle='#ff9a3a';ctx.beginPath();ctx.moveTo(px-3*Z,py-1*Z);ctx.quadraticCurveTo(px+fl,py-11*Z,px+3*Z,py-1*Z);ctx.fill()}\n  if(G.traps)for(const tp of G.traps){")
# ---------- admin map pick on the start screen ----------
rep('<div class="np" id="npick">Players <button data-n="2">2</button><button data-n="3" class="on">3</button><button data-n="4">4</button></div>',
    '<div class="np" id="npick">Players <button data-n="2">2</button><button data-n="3" class="on">3</button><button data-n="4">4</button></div>\n     <div class="np" id="mpick">Map <button data-m="random" class="on">Random</button><button data-m="continent">Highlands</button><button data-m="straits">Straits</button><button data-m="isles">Isles</button></div>')
rep("document.querySelectorAll('#npick button').forEach(b=>b.onclick=()=>{","document.querySelectorAll('#mpick button').forEach(b=>b.onclick=()=>{document.querySelectorAll('#mpick button').forEach(x=>x.classList.toggle('on',x===b));MAPPICK=b.dataset.m;newGame(NP);toast(MAPPICK==='random'?'Random map':MAPNAME[MAPPICK])});\ndocument.querySelectorAll('#npick button').forEach(b=>b.onclick=()=>{")
rep("SEL:()=>SEL,","SEL:()=>SEL,villages:()=>G.villages,obsAt:(x,y)=>OBS[idx(x,y)],setMap:m=>{MAPPICK=m;newGame(NP)},")
open(F,'w').write(s);print('villages ok',len(s))
s=open(F).read()
rep("const amt=new Float32Array(100*100),seedA=new Uint8Array(100*100),wither=new Uint8Array(100*100),zone=new Uint8Array(100*100),","const amt=new Float32Array(WN*WN),seedA=new Uint8Array(WN*WN),wither=new Uint8Array(WN*WN),zone=new Uint8Array(WN*WN),")
open(F,'w').write(s);print('arrays sized')
s=open(F).read()
rep("!['harbor','barracks','lumber','farm','HALL','altar','well','wabet'].includes(item)","!['harbor','barracks','lumber','farm','HALL','altar','well','wabet','chapel'].includes(item)")
open(F,'w').write(s);print('ai waits for villages')
