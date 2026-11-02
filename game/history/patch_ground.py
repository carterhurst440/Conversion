F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
# ---------- smooth ground: one colour for the world, one for each faith's land; no per-tile speckle, zone or resource tints ----------
rep("const nb=BIO[bio[i]],bi=tfa[i]>=0?BIO[tfa[i]]:nb;","const nb=BIO[(THEMES[THEME]||THEMES.mountains).bios[0]],bi=tfa[i]>=0?BIO[tfa[i]]:nb;")
rep("(hs-.5)*.06+(((a+b+c+d)/4)-1.5)*.05);","(((a+b+c+d)/4)-1.5)*.04);")
for a in["    if(!beachA[i]&&zone[i])base=mixRgb(base,hexRgb(['','#d4b866','#5e8f5a','#a9a5ad','#c4a6e4'][zone[i]]),[0,.38,.24,.32,.3][zone[i]]);\n",
         "    if(!beachA[i]&&dp==='tree')base=mixRgb(base,hexRgb(bi.treeTint),.45);\n",
         "    if(!beachA[i]&&dp==='rock')base=mixRgb(base,hexRgb(bi.rock==='crystal'?'#c7b8f0':bi.rock[0]),.35);\n",
         "    if(!beachA[i]&&dp==='clay')base=mixRgb(base,hexRgb(bi.clay[0]),.35);",
         "    if(!beachA[i]&&dp==='wheat')base=mixRgb(base,hexRgb(bi.wheat==='glow'?'#bfe8c8':bi.wheat[1]),.3);\n",
         "    if(!beachA[i]&&!dp&&wither[i])base=mixRgb(base,hexRgb(['','#8f7c62','#b39b6e','#a49d94'][wither[i]]),wither[i]===3?.25:.42);\n"]:
    rep(a,"" if a.endswith("\n") else "    ")
rep("base=shade(base,(lvl%2?.035:-.02)-lvl*.012);base=mixRgb(base,mixRgb([240,245,251],[222,231,242],hs*.6),.86);","base=mixRgb(base,[236,242,250],.86);")
# gentler bumps, so the light doesn't checker the flats
rep("+n*.4*(THEME==='moon'?.5:1)}","+n*.14*(THEME==='moon'?.5:1)}")
# ---------- prettier trees: soft ground shadows, shaded broadleaf canopies and tiered conifers ----------
rep("    for(const[ox,oy,sc]of spots){const tx=sx+(ox-oy)*hw,ty=sy+(ox+oy)*hh,ss=s*sc,q=((hs*(sc*10|0))&255)/255;",
    "    for(const[ox,oy,sc]of spots){const tx=sx+(ox-oy)*hw,ty=sy+(ox+oy)*hh,ss=s*sc,q=((hs*(sc*10|0))&255)/255;\n      ctx.fillStyle='rgba(28,36,40,.2)';ctx.beginPath();ctx.ellipse(tx+3*ss,ty+1.2*ss,10*ss,4.2*ss,0,0,TAU);ctx.fill();\n      if(NICETREE[bi.tree]){NICETREE[bi.tree](tx,ty,ss,r1,r2,q,hs);continue}")
rep("function drawDep(k,sx,sy,s,hs,x,y,bio){",r"""function niceBroad(tx,ty,ss,H,R,pal,trunk,q,hs){
  ctx.fillStyle=trunk[0];ctx.beginPath();ctx.moveTo(tx-3*ss,ty);ctx.lineTo(tx-1.4*ss,ty-H*.62);ctx.lineTo(tx+1.4*ss,ty-H*.62);ctx.lineTo(tx+3*ss,ty);ctx.closePath();ctx.fill();
  ctx.fillStyle=trunk[1];ctx.beginPath();ctx.moveTo(tx,ty);ctx.lineTo(tx,ty-H*.62);ctx.lineTo(tx+1.4*ss,ty-H*.62);ctx.lineTo(tx+3*ss,ty);ctx.closePath();ctx.fill();
  const cy=ty-H,B=[[-.56,.12,.55],[.56,.16,.55],[0,.3,.6],[-.3,-.32,.56],[.32,-.28,.5],[0,-.04,.72]];
  ctx.fillStyle=pal[0];for(const[a,b,r]of B){ctx.beginPath();ctx.arc(tx+(a+.08)*R,cy+(b+.1)*R,r*R,0,TAU);ctx.fill()}
  ctx.fillStyle=pal[1];for(const[a,b,r]of B){ctx.beginPath();ctx.arc(tx+a*R,cy+b*R,r*R*.94,0,TAU);ctx.fill()}
  ctx.fillStyle=pal[2];for(const[a,b,r]of B)if(b<.2){ctx.beginPath();ctx.arc(tx+(a-.14)*R,cy+(b-.16)*R,r*R*.5,0,TAU);ctx.fill()}
  ctx.fillStyle=pal[3];for(let m=0;m<4;m++){const a=(((hs*(m+3)*29)%100)/100-.5)*1.3,b=(((hs*(m+7)*17)%100)/100-.7)*.9;ctx.beginPath();ctx.arc(tx+a*R,cy+b*R,R*.07,0,TAU);ctx.fill()}
  if(pal[4]&&q>.5){ctx.fillStyle=pal[4];for(let m=0;m<3;m++){const a=(((hs*(m+2)*13)%100)/100-.5)*1.1,b=(((hs*(m+5)*7)%100)/100-.4)*.8;ctx.beginPath();ctx.arc(tx+a*R,cy+b*R,R*.09,0,TAU);ctx.fill()}}}
function niceCone(tx,ty,ss,H,W,pal,snow){ctx.fillStyle='#6a4a36';ctx.fillRect(tx-1.6*ss,ty-6*ss,3.2*ss,6*ss);const n=4;
  for(let t=0;t<n;t++){const yb=ty-4*ss-t*H*.22,w=W*(1-t*.2),ht=H*.36;const jag=(sd)=>{ctx.beginPath();ctx.moveTo(tx,yb-ht);for(let k=0;k<=4;k++){const f=k/4,x=tx+sd*w*f;ctx.lineTo(x,yb+(k%2?-1.6:1.2)*ss*(f>0?1:0))}ctx.lineTo(tx,yb+2*ss);ctx.closePath();ctx.fill()};
    ctx.fillStyle=pal[0];jag(-1);ctx.fillStyle=pal[1];jag(1);if(snow){ctx.fillStyle='rgba(255,255,255,.92)';ctx.beginPath();ctx.moveTo(tx,yb-ht);ctx.lineTo(tx-w*.38,yb-ht*.42);ctx.lineTo(tx-w*.1,yb-ht*.5);ctx.lineTo(tx+w*.2,yb-ht*.38);ctx.closePath();ctx.fill()}}}
const NICETREE={
  grove:(tx,ty,ss,r1,r2,q,hs)=>niceBroad(tx,ty,ss,(26+r1*8)*ss,(10.5+r2*2.5)*ss,['#3f7552','#5d9a6c','#86bf8c','#a9d7a6','#f4e7a2'],['#7a5640','#5e3f2d'],q,hs),
  oak:(tx,ty,ss,r1,r2,q,hs)=>niceBroad(tx,ty,ss,(24+r1*7)*ss,(11.5+r2*2.5)*ss,['#2f6634','#4c8a46','#73b062','#9ccd84','#d4e88a'],['#7a5a42','#5a3f2c'],q,hs),
  jungle:(tx,ty,ss,r1,r2,q,hs)=>niceBroad(tx,ty,ss,(33+r1*10)*ss,(12+r2*3)*ss,['#23572b','#367a3a','#56a24c','#7cc46a','#ff6a78'],['#5a4030','#3e2b20'],q,hs),
  pine:(tx,ty,ss,r1,r2,q,hs)=>niceCone(tx,ty,ss,(34+r1*10)*ss,(10+r2*2)*ss,['#4f8a82','#2f625f'],THEME==='mountains'||q>.6)};
function drawDep(k,sx,sy,s,hs,x,y,bio){""")
# ---------- villages: the huts stand inside the church plot; a church raised there replaces them ----------
rep("if(G.villages)for(const v of G.villages){if(cells[idx(v.x,v.y)]||!exp0[idx(v.x,v.y)])continue;","if(G.villages)for(const v of G.villages){const c0=cells[idx(v.x,v.y)];if((c0&&!c0.obst)||!exp0[idx(v.x,v.y)])continue;")
rep("  if(cells[i])return{ok:false,why:'Something is already there.'};\n  {const sz=B[type].s||1;if(sz>1)for(let dy=0;dy<sz;dy++)for(let dx=0;dx<sz;dx++){const X=x+dx,Y=y+dy;if(!inb(X,Y)||!land[idx(X,Y)]||cells[idx(X,Y)]||",
    "  const VH=j=>type==='chapel'&&cells[j]&&cells[j].obst&&dep[j]==='hut';\n  if(cells[i]&&!VH(i))return{ok:false,why:'Something is already there.'};\n  {const sz=B[type].s||1;if(sz>1)for(let dy=0;dy<sz;dy++)for(let dx=0;dx<sz;dx++){const X=x+dx,Y=y+dy;if(!inb(X,Y)||!land[idx(X,Y)]||(cells[idx(X,Y)]&&!VH(idx(X,Y)))||")
rep("function place(side,type,x,y){\n  const D=B[type],s=D.s||1,S=G.S[side];","function place(side,type,x,y){\n  const D=B[type],s=D.s||1,S=G.S[side];if(type==='chapel'){for(let dy=0;dy<s;dy++)for(let dx=0;dx<s;dx++){const j=idx(x+dx,y+dy);if(dep[j]==='hut'){dep[j]=null;OBS[j]=0;HUTV[j]=-1;if(cells[j]&&cells[j].obst)cells[j]=null;if(typeof puff==='function'&&G.started)puff(x+dx+.5,y+dy+.5,3)}}}")
open(F,'w').write(s);print('ground ok')
s=open(F).read()
# the Proving Grounds and the Movement Lab clear the world's blocked ground (left over from the map behind the menu, it made invisible walls)
rep("land.fill(0);isl.fill(255);beachA.fill(0);","land.fill(0);isl.fill(255);beachA.fill(0);OBS.fill(0);HUTV.fill(-1);CFLOOR.fill(0);",3)
open(F,'w').write(s);print('arena obs ok')
s=open(F).read()
# getting hit tints a 3D unit warm red for an instant instead of blanking it to solid white (big fights looked like units flashing on and off)
s=s.replace("setHex(I.flash?0xffffff:0)","setHex(I.flash?0x5a2418:0)")
open(F,'w').write(s);print('flash ok')
