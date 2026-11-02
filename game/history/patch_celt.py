F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:80]);s=s.replace(a,b)
CEL=r"""
// ---------- Celtic (Cernunnos) buildings: roundhouses, timber forts, earth stores, standing stones ----------
const CELC={wall:'#d8c29a',wallD:'#b89f74',thatch:'#c9a35a',thatchD:'#a07d3c',thatchL:'#e0bf78',wood:'#8a6a48',woodD:'#6c5238',stone:'#b9b6ae',stoneD:'#97948d',stoneL:'#d6d3cb',grass:'#86b45c',grassD:'#6a9646',grassL:'#a3cc78',moss:'#7fa85a'};
function celRound(cx,cy,s,R,wh,rh,trim,b){wh*=s;rh*=s;const rx=R*45.25*s,ry=R*22.63*s;
  ctx.fillStyle=CELC.wall;ctx.fillRect(cx-rx,cy-wh,rx,wh);ctx.fillStyle=CELC.wallD;ctx.fillRect(cx,cy-wh,rx,wh);
  ctx.fillStyle=CELC.wall;ctx.beginPath();ctx.ellipse(cx,cy,rx,ry,0,Math.PI/2,Math.PI);ctx.lineTo(cx,cy);ctx.fill();ctx.fillStyle=CELC.wallD;ctx.beginPath();ctx.ellipse(cx,cy,rx,ry,0,0,Math.PI/2);ctx.lineTo(cx,cy);ctx.fill();
  ctx.strokeStyle='rgba(110,82,52,.35)';ctx.lineWidth=.9*s;for(let k=1;k<4;k++){ctx.beginPath();ctx.ellipse(cx,cy-wh*k/4,rx,ry,0,0,Math.PI);ctx.stroke()}
  {const dx=cx-rx*.42,dy=cy+ry*.82;ctx.fillStyle='#3e3026';ctx.beginPath();ctx.moveTo(dx-4.5*s*R*2,dy);ctx.lineTo(dx-4.5*s*R*2,dy-wh*.62);ctx.quadraticCurveTo(dx,dy-wh*.9,dx+4.5*s*R*2,dy-wh*.66);ctx.lineTo(dx+4.5*s*R*2,dy-1*s);ctx.closePath();ctx.fill();glow(dx,dy-wh*.3,7*s*R*2,'#ffc27a',.25)}
  const ty=cy-wh,ex=rx*1.14,ey=ry*1.14,ap=[cx,ty-rh];
  ctx.fillStyle=CELC.thatch;ctx.beginPath();ctx.moveTo(ap[0],ap[1]);ctx.lineTo(cx-ex,ty);ctx.ellipse(cx,ty,ex,ey,0,Math.PI,Math.PI/2,true);ctx.closePath();ctx.fill();
  ctx.fillStyle=CELC.thatchD;ctx.beginPath();ctx.moveTo(ap[0],ap[1]);ctx.lineTo(cx,ty+ey);ctx.ellipse(cx,ty,ex,ey,0,Math.PI/2,0,true);ctx.closePath();ctx.fill();
  ctx.strokeStyle='rgba(90,66,30,.32)';ctx.lineWidth=.9*s;for(let k=0;k<=10;k++){const a=Math.PI*k/10,px=cx-Math.cos(a)*ex,py=ty+Math.sin(a)*ey;ctx.beginPath();ctx.moveTo(ap[0]+(px-ap[0])*.12,ap[1]+(py-ap[1])*.12);ctx.lineTo(px,py);ctx.stroke()}
  ctx.strokeStyle=CELC.thatchL;ctx.lineWidth=1.6*s;ctx.beginPath();ctx.ellipse(cx,ty,ex,ey,0,0,Math.PI);ctx.stroke();
  if(trim){ctx.fillStyle=trim;ctx.beginPath();ctx.ellipse(cx,ty-rh*.55,ex*.45,ey*.45,0,0,Math.PI);ctx.lineTo(cx-ex*.45,ty-rh*.55);ctx.fill()}
  if(!reduceMotion){for(let i=0;i<3;i++){const q=(time*.25+i/3+(b&&b.seed||0))%1;ctx.fillStyle=`rgba(235,230,222,${(1-q)*.4})`;ctx.beginPath();ctx.arc(ap[0]+Math.sin(q*4+i)*4*s,ap[1]-2*s-q*24*s,(1.6+q*3)*s,0,TAU);ctx.fill()}}
  return ap}
function celAntlers(x,y,s,col){ctx.strokeStyle=col||'#efe3c8';ctx.lineWidth=1.6*s;ctx.lineCap='round';for(const d of[-1,1]){ctx.beginPath();ctx.moveTo(x,y);ctx.quadraticCurveTo(x+d*6*s,y-4*s,x+d*9*s,y-12*s);ctx.stroke();ctx.beginPath();ctx.moveTo(x+d*5*s,y-4*s);ctx.lineTo(x+d*9*s,y-6*s);ctx.stroke();ctx.beginPath();ctx.moveTo(x+d*7.5*s,y-8.5*s);ctx.lineTo(x+d*11*s,y-10*s);ctx.stroke()}}
function celRing(cx,cy,s,R,n,front,kind,h){const out=[];for(let i=0;i<n;i++){const a=i/n*TAU+.2,px=cx+Math.cos(a)*R*45.25*s,py=cy+Math.sin(a)*R*22.63*s;if((Math.sin(a)>0)!==front)continue;out.push([px,py,a])}
  out.sort((p,q)=>p[1]-q[1]);for(const[px,py]of out){if(kind==='stone'){const w=3.4*s,hh=h*s;ctx.fillStyle=CELC.stone;ctx.beginPath();ctx.moveTo(px-w,py);ctx.lineTo(px-w*.8,py-hh);ctx.quadraticCurveTo(px,py-hh-2.5*s,px+w*.8,py-hh);ctx.lineTo(px+w,py);ctx.closePath();ctx.fill();ctx.fillStyle=CELC.stoneD;ctx.beginPath();ctx.moveTo(px,py);ctx.lineTo(px,py-hh-1*s);ctx.quadraticCurveTo(px+w*.6,py-hh-.5*s,px+w*.8,py-hh);ctx.lineTo(px+w,py);ctx.closePath();ctx.fill();ctx.fillStyle=CELC.moss;ctx.fillRect(px-w,py-2*s,w*2,2*s)}
    else{const w=1.7*s,hh=h*s;ctx.fillStyle=CELC.wood;ctx.fillRect(px-w,py-hh,w*2,hh);ctx.fillStyle=CELC.woodD;ctx.fillRect(px,py-hh,w,hh);ctx.fillStyle=CELC.wood;ctx.beginPath();ctx.moveTo(px-w,py-hh);ctx.lineTo(px,py-hh-3*s);ctx.lineTo(px+w,py-hh);ctx.fill()}}}
function celStake(px,py,s,h,lite){const w=2.1*s;ctx.fillStyle=lite?CELC.wood:CELC.woodD;ctx.beginPath();ctx.moveTo(px-w,py);ctx.lineTo(px-w,py-h);ctx.lineTo(px,py-h-3.5*s);ctx.lineTo(px+w,py-h);ctx.lineTo(px+w,py);ctx.closePath();ctx.fill();ctx.strokeStyle='rgba(50,36,24,.35)';ctx.lineWidth=.7*s;ctx.beginPath();ctx.moveTo(px+w,py);ctx.lineTo(px+w,py-h);ctx.stroke()}
function celMound(cx,cy,s,rx,ry,h){ctx.fillStyle=CELC.grassD;ctx.beginPath();ctx.ellipse(cx,cy,rx,ry,0,0,Math.PI);ctx.lineTo(cx-rx,cy);ctx.fill();
  const g=ctx.createLinearGradient(cx-rx,0,cx+rx,0);g.addColorStop(0,CELC.grassL);g.addColorStop(.55,CELC.grass);g.addColorStop(1,CELC.grassD);ctx.fillStyle=g;ctx.beginPath();ctx.moveTo(cx-rx,cy);ctx.bezierCurveTo(cx-rx,cy-h*1.05,cx+rx,cy-h*1.05,cx+rx,cy);ctx.ellipse(cx,cy,rx,ry,0,0,Math.PI);ctx.closePath();ctx.fill();
  ctx.fillStyle='rgba(255,255,255,.12)';ctx.beginPath();ctx.ellipse(cx-rx*.3,cy-h*.62,rx*.35,h*.18,-.2,0,TAU);ctx.fill()}
function drawCelt(b,sx,sy,s,live,C1,C2){const gc=GODS[8].col;
  switch(b.type){
    case 'hall':{const tier=live&&G.S[b.side]?G.S[b.side].tier:1,great=tier>=2;blobShadow(sx,sy,s,62);
      ctx.fillStyle='rgba(120,160,80,.35)';ctx.beginPath();ctx.ellipse(sx,sy,.98*45.25*s,.98*22.63*s,0,0,TAU);ctx.fill();
      celRing(sx,sy-2*s,s,.9,great?12:16,false,great?'stone':'post',great?17:12);
      const ap=celRound(sx,sy-2*s,s,.55,24,great?46:40,great?gc:null,b);
      if(great){celAntlers(ap[0],ap[1]+2*s,s*1.25);glow(ap[0],ap[1]+4*s,26*s,gc,.4)}else{ctx.strokeStyle=CELC.woodD;ctx.lineWidth=1.6*s;line(ap[0],ap[1],ap[0],ap[1]-10*s);ctx.fillStyle=C1;ctx.beginPath();ctx.moveTo(ap[0],ap[1]-10*s);ctx.lineTo(ap[0]+8*s,ap[1]-8*s);ctx.lineTo(ap[0],ap[1]-5.5*s);ctx.fill()}
      celRing(sx,sy-2*s,s,.9,great?12:16,true,great?'stone':'post',great?17:12);
      const fr=[];for(let k=0;k<tier;k++)fr.push([sx+(-.7+k*.155-.74)*32*s,sy+(-.7+k*.155+.74)*16*s-3*s]);for(const p of fr){glow(p[0],p[1],5*s,C1,.6);ctx.fillStyle='#fff3e6';ctx.beginPath();ctx.arc(p[0],p[1],1.4*s,0,TAU);ctx.fill()}
      return true}
    case 'chapel':{blobShadow(sx,sy,s,26);celRing(sx,sy,s,.42,9,false,b.temple?'stone':'post',b.temple?11:8);const ap=celRound(sx,sy,s,.27,13,22,b.temple?gc:null,b);if(b.temple){celAntlers(ap[0],ap[1]+1.5*s,s*.8);glow(ap[0],ap[1]+3*s,14*s,gc,.35)}celRing(sx,sy,s,.42,9,true,b.temple?'stone':'post',b.temple?11:8);return true}
    case 'barracks':{blobShadow(sx,sy,s,26);const P=(u,v,z)=>[sx+(u-v)*32*s,sy+(u+v)*16*s-z*s],a=.4,n=7,H=13;
      ctx.fillStyle='#a58a62';poly([...P(-a,a,0),...P(a,a,0),...P(a,-a,0),...P(-a,-a,0)]);
      for(let i=0;i<=n;i++){const t=-a+2*a*i/n;let p=P(t,-a,0);celStake(p[0],p[1],s,H,1);p=P(-a,t,0);celStake(p[0],p[1],s,H,1)}
      celRound(sx,sy-1*s,s,.2,9,16,null,b);{const p=P(-.05,-.05,0);ctx.strokeStyle=CELC.woodD;ctx.lineWidth=1.3*s;line(p[0]+12*s,p[1]-8*s,p[0]+12*s,p[1]-34*s);ctx.fillStyle=C1;ctx.beginPath();ctx.moveTo(p[0]+12*s,p[1]-34*s);ctx.lineTo(p[0]+22*s,p[1]-31*s);ctx.lineTo(p[0]+12*s,p[1]-27*s);ctx.fill()}
      for(let i=0;i<=n;i++){const t=-a+2*a*i/n;if(i===Math.floor(n/2)||i===Math.floor(n/2)+1){continue}let p=P(t,a,0);celStake(p[0],p[1],s,H,0)}
      for(let i=0;i<=n;i++){const t=-a+2*a*i/n;const p=P(a,t,0);celStake(p[0],p[1],s,H,0)}
      {const g=P(0,a,0),g2=P(.12,a,0);ctx.fillStyle=CELC.woodD;ctx.fillRect(g[0]-1.5*s,g[1]-H*s-6*s,2.4*s,H*s+6*s);ctx.fillRect(g2[0]-1*s,g2[1]-H*s-6*s,2.4*s,H*s+6*s);ctx.fillRect(g[0]-1.5*s,g[1]-H*s-6*s,g2[0]-g[0]+3*s,2.6*s)}
      for(const[u,c]of[[-.25,C1],[.25,'#c9a35a']]){const p=P(a,u,7);ctx.fillStyle=c;ctx.beginPath();ctx.arc(p[0]+2*s,p[1],3.4*s,0,TAU);ctx.fill();ctx.fillStyle='#e8dcc0';ctx.beginPath();ctx.arc(p[0]+2*s,p[1],1.1*s,0,TAU);ctx.fill()}
      return true}
    case 'storehouse':{blobShadow(sx,sy,s,22);celMound(sx,sy,s,22*s,11*s,17*s);
      const dx=sx-6*s,dy=sy+6*s;ctx.fillStyle=CELC.stoneD;ctx.fillRect(dx-6.5*s,dy-11*s,13*s,11*s);ctx.fillStyle='#2e2420';ctx.fillRect(dx-4*s,dy-8.5*s,8*s,8.5*s);ctx.fillStyle=CELC.stoneL;ctx.fillRect(dx-7.5*s,dy-12.5*s,15*s,3.4*s);ctx.fillStyle=CELC.stone;ctx.fillRect(dx-7.5*s,dy-9.1*s,15*s,1*s);
      for(const[ox,oy,c]of[[8,7,'#e8d29a'],[13,4,'#d9b44e'],[11,10,'#a87650']]){ctx.fillStyle=c;ctx.beginPath();ctx.ellipse(sx+ox*s,sy+oy*s-3*s,3.6*s,3.2*s,0,0,TAU);ctx.fill();ctx.fillStyle='rgba(43,36,64,.18)';ctx.beginPath();ctx.ellipse(sx+ox*s,sy+oy*s-.4*s,3.6*s,1.1*s,0,0,TAU);ctx.fill()}
      ctx.fillStyle=CELC.grassL;for(const[ox,oy]of[[-14,-6],[4,-14],[14,-6]]){ctx.beginPath();ctx.moveTo(sx+ox*s,sy+oy*s);ctx.lineTo(sx+ox*s+1.2*s,sy+oy*s-4*s);ctx.lineTo(sx+ox*s+2.4*s,sy+oy*s);ctx.fill()}
      return true}
    case 'altar':{blobShadow(sx,sy,s,28);const P=(u,v,z)=>[sx+(u-v)*32*s,sy+(u+v)*16*s-z*s];
      ctx.fillStyle='rgba(120,160,80,.4)';ctx.beginPath();ctx.ellipse(sx,sy,24*s,12*s,0,0,TAU);ctx.fill();
      const ty=sy-26*s+(reduceMotion?0:Math.sin(time*2+(b.seed||0)*6)*2*s);
      ibox(P(-.18,-.14,0)[0],P(-.18,-.14,0)[1],s,.06,.09,0,17,CELC.stoneL,CELC.stone,CELC.stoneD);
      glow(sx,sy-6*s,14*s,gc,.55);
      ibox(P(.2,-.16,0)[0],P(.2,-.16,0)[1],s,.08,.06,0,16,CELC.stoneL,CELC.stone,CELC.stoneD);
      ibox(P(-.16,.2,0)[0],P(-.16,.2,0)[1],s,.07,.07,0,15,CELC.stoneL,CELC.stone,CELC.stoneD);
      {const c=P(0,0,15);ctx.save();ctx.translate(c[0],c[1]);ctx.rotate(-.06);ibox(0,0,s,.34,.26,0,5,CELC.stoneL,CELC.stone,CELC.stoneD);ctx.fillStyle=CELC.moss;ctx.beginPath();ctx.ellipse(-6*s,-6*s,6*s,2.2*s,0,0,TAU);ctx.fill();ctx.restore()}
      glow(sx,ty,18*s,gc,.5);drawSigil(8,sx,ty,5.5*s,gc,true);
      if(!reduceMotion)for(let i=0;i<4;i++){const q=(time*.5+i/4+(b.seed||0))%1;ctx.fillStyle=hexA(gc,(1-q)*.6);ctx.beginPath();ctx.arc(sx+Math.sin(q*6+i)*9*s,sy-8*s-q*24*s,1.4*s,0,TAU);ctx.fill()}
      return true}
    case 'veil':{blobShadow(sx,sy,s,64);celRing(sx,sy,s,.95,14,false,'stone',13);
      celMound(sx,sy-2*s,s,52*s,26*s,44*s);
      const dx=sx-14*s,dy=sy+14*s,tt=live?time:1;ctx.fillStyle=CELC.stoneD;ctx.beginPath();ctx.moveTo(dx-12*s,dy);ctx.lineTo(dx-12*s,dy-20*s);ctx.quadraticCurveTo(dx,dy-32*s,dx+12*s,dy-20*s);ctx.lineTo(dx+12*s,dy);ctx.fill();
      const gr=ctx.createLinearGradient(0,dy-28*s,0,dy);gr.addColorStop(0,hexA(gc,.95));gr.addColorStop(1,hexA('#eafff0',.5));ctx.fillStyle=gr;ctx.beginPath();ctx.moveTo(dx-8.5*s,dy);ctx.lineTo(dx-8.5*s,dy-18*s);ctx.quadraticCurveTo(dx,dy-27*s,dx+8.5*s,dy-18*s);ctx.lineTo(dx+8.5*s,dy);ctx.fill();
      ctx.strokeStyle='rgba(255,255,255,.55)';ctx.lineWidth=1*s;for(let k=0;k<3;k++){const ph=tt*1.6+k*2;ctx.beginPath();ctx.moveTo(dx-5*s+k*5*s+Math.sin(ph)*1.5*s,dy-2*s);ctx.quadraticCurveTo(dx-5*s+k*5*s+Math.sin(ph+1)*3*s,dy-12*s,dx-5*s+k*5*s,dy-20*s+k*2*s);ctx.stroke()}
      glow(dx,dy-12*s,34*s,gc,.4);celRing(sx,sy,s,.95,14,true,'stone',13);
      {const t=[sx+6*s,sy-46*s];ctx.strokeStyle=CELC.woodD;ctx.lineWidth=2*s;line(t[0],t[1]+8*s,t[0],t[1]-6*s);celAntlers(t[0],t[1]-5*s,s*1.1);if(live)drawSigil(8,t[0],t[1]-22*s,5*s,'#fff4cf',true)}
      return true}
  }
  return false}
function drawBld(b,sx,sy,s,live){"""
rep("function drawBld(b,sx,sy,s,live){",CEL.lstrip('\n'))
rep("ctx.lineCap='round';ctx.lineJoin='round';\n  switch(b.type){\n    case 'hall':",
    "ctx.lineCap='round';ctx.lineJoin='round';\n  {const cg=live?(G.S[b.side]?G.S[b.side].god:-1):playerGod();if(cg===8&&b.type!=='wall'&&drawCelt(b,sx,sy,s,live,C1,C2)){if(b.bless!=null)drawBless(b,sx,sy,s);return}}\n  switch(b.type){\n    case 'hall':")
open(F,'w').write(s);print('celt ok')
s=open(F).read()
rep("drawSprout({moving:false,walk:0,sw:0,hurt:0,ph:1},x,y,s,-1,LOOK[2],'helm',.95);ctx.restore()}","drawDummy({hurt:0},x,y,s*.85);ctx.restore()}")
open(F,'w').write(s);print('foe ok')
import re
s=open(F).read()
rx=re.compile(r"drawSprout\((\{[^{}]*\}|\w+),([^,]+),([^,]+),([^,]+),[^,]+,LOOK\[2\],'(?:helm|hood)',[^)]+\)")
s,n=rx.subn(lambda m:f"drawDummy({m.group(1)},{m.group(2)},{m.group(3)},({m.group(4)})*.85)",s)
print('foes replaced',n)
open(F,'w').write(s)
s=open(F).read()
# allies in preview scenes were Warriors (removed) -> Sowers
i=s.index('function cxFoe(');head,tail=s[:i],s[i:]
n=tail.count("LOOK[0],'helm'");tail=tail.replace("LOOK[0],'helm'","LOOK[0],'shovel'");s=head+tail;print('allies',n)
rep("SPNAME={","SPNAME={swarmplague:'Plague Swarm',skyfall:'Skyfall',")
rep("ritual:5.4,wrap:6.2,","ritual:5.4,wrap:6.2,swarmplague:6.2,skyfall:5,")
rep("  else if(T.special==='scarab'){const bx=w*.24,tx=w-26;",
r"""  else if(T.special==='swarmplague'){const bx=w*.2,fs=[[w*.62,gy-6],[w*.76,gy+5],[w*.88,gy-4]],st=1.4;if(p<.1||!c.ph)c.ph=fs.map(()=>1);
    if(at(.4))u.sw=1;if(at(st)){u.plagueT=3.6;cxTxt(c,w*.45,gy-84,'Plague Swarm','#6f8f2a')}if(u.plagueT>0)u.plagueT-=dt;u.sw=Math.max(0,u.sw-dt*2.6);
    for(const[i,f]of fs.entries()){drawDummy({hurt:0},f[0],f[1],sc*.8);hpbar(f[0],f[1]-46,16,c.ph[i],1,1)}
    drawTroop(u,bx,gy,sc,1);
    if(p>st+.5){const k=Math.min(1,(p-st-.5)/1.3),fade=p>L-.7?Math.max(0,(L-p)/.7):1,cx=bx+(w*.76-bx)*k,cy=gy-46+k*20;
      for(let i=0;i<38;i++){const a=time*(2.4+(i%5)*.3)+i*1.7,r=5+((i*37)%19)+k*10,x=cx+Math.cos(a)*r*1.5,y=cy+Math.sin(a*1.3)*r*.6,fl=Math.sin(time*40+i)>0;ctx.fillStyle=`rgba(31,43,42,${.9*fade})`;ctx.beginPath();ctx.ellipse(x,y,1.9,1.3,a,0,TAU);ctx.fill();ctx.fillStyle=`rgba(200,235,140,${.55*fade})`;ctx.beginPath();ctx.ellipse(x+(fl?-1:1),y-1.6,1.6,.7,fl?.5:-.5,0,TAU);ctx.fill()}
      if(k>=1){c.ph=c.ph.map(v=>Math.max(.12,v-dt*.14));if(Math.floor(p*2)!==Math.floor(prev*2))for(const f of fs)cxTxt(c,f[0],f[1]-54,'-6','#6a8a2a')}}}
  else if(T.special==='skyfall'){const mx=w*.38,fs=[[w*.6,gy-6],[w*.72,gy+5],[w*.84,gy-4]],st=1,hit=st+1.75;if(p<.1||!c.ph)c.ph=fs.map(()=>1);
    if(p<st||p>hit+.6){if((c.swT=(c.swT||0)-dt)<=0){c.swT=.9;u.sw=1}}u.sw=Math.max(0,u.sw-dt*2.6);
    if(at(st)){u.skyT=2.1;cxTxt(c,mx,gy-86,'Skyfall','#c9a23f')}if(u.skyT>0)u.skyT-=dt;
    if(at(hit)){c.fx.push({ring:true,x:w*.68,y:gy,col:'#e8c35a',l:0,m:.7,big:true});c.fx.push({ring:true,x:w*.68,y:gy,col:'#a8865a',l:0,m:.5});c.ph=c.ph.map(v=>Math.max(.1,v-.6));for(const f of fs)cxTxt(c,f[0],f[1]-54,'-66','#c4553f');c.quake=.5}
    if(c.quake>0){c.quake-=dt;for(let i=0;i<10;i++){const a=i/10*Math.PI,q=1-c.quake/.5;ctx.fillStyle='#8a6a48';ctx.beginPath();ctx.arc(w*.68+Math.cos(a)*q*50,gy-Math.sin(a)*q*30+q*q*30,2,0,TAU);ctx.fill()}}
    const shake=c.quake>0?Math.sin(time*80)*2*c.quake/.5:0;ctx.save();ctx.translate(shake,0);
    for(const[i,f]of fs.entries()){drawDummy({hurt:c.quake>0?.15:0},f[0],f[1],sc*.8);hpbar(f[0],f[1]-46,16,c.ph[i],1,1)}
    drawTroop(u,mx,gy,sc*.95,1);ctx.restore()}
  else if(T.special==='scarab'){const bx=w*.24,tx=w-26;""")
open(F,'w').write(s);print('scenes ok')
s=open(F).read()
a=s.index("FACT.combo=function(){");e=s.index("// ----- game driver",a)
seg=s[a:e];n=seg.count("scene.add(")+seg.count("scene.remove(")
seg=seg.replace("scene.add(","SCN.add(").replace("scene.remove(","SCN.remove(")
for f in ["combo","sphinx","ark"]:
    k="FACT."+f+"=function(){";assert seg.count(k)==1,f;seg=seg.replace(k,k+"const SCN=scene;")
s=s[:a]+seg+s[e:];print('scene refs',n)
open(F,'w').write(s)
s=open(F).read()
old="for(const[i,a]of al.entries()){drawSprout({moving:false,walk:0,sw:0,hurt:0,ph:i},a[0],a[1],sc*.82,-1,LOOK[0],'shovel',1);hpbar(a[0],a[1]-46,16,c.ah[i],0,1)}\n    drawTroop(u,bx,gy,sc,1)}"
new="c.mum=c.mum||al.map((a,i)=>({type:'g0_1b',side:0,moving:false,walk:0,sw:0,hurt:0,ph:i*2,fx:-1,fy:1,hp:1,max:1}));for(const[i,a]of al.entries()){drawTroop(c.mum[i],a[0],a[1],sc*.8,1);hpbar(a[0],a[1]-50,16,c.ah[i],0,1)}\n    drawTroop(u,bx,gy,sc,1)}"
rep(old,new)
open(F,'w').write(s);print('mummy allies ok')
import re
s=open(F).read()
i=s.index('function cxSpecial(');e=s.index('\nfunction ',i+20);b=s[i:e]
rx=re.compile(r"drawSprout\((\{[^{}]*\}|\w+),([^,]+),([^,]+),([^,]+),[^,]+,LOOK\[0\],'shovel',[^)]+\)")
tot=0
for sp,key in [('horned','g8_0b'),('toll','g1_0b'),('fury','g1_0b')]:
    a=b.index("T.special==='%s'"%sp);z=b.find("T.special===",a+20);z=z if z>0 else len(b)
    seg=b[a:z];seg2,n=rx.subn(lambda m:f"drawTroop(cxAl(c,'{key}',{m.group(1)}),{m.group(2)},{m.group(3)},({m.group(4)})*.9,1)",seg);tot+=n
    b=b[:a]+seg2+b[z:]
s=s[:i]+b+s[e:]
rep("function cxSpecial(","function cxAl(c,k,s0){c.alc=c.alc||{};const id=k+':'+(s0&&s0.ph!=null?s0.ph:0);let a=c.alc[id];if(!a)a=c.alc[id]={type:k,side:0,moving:false,walk:0,sw:0,hurt:0,ph:s0&&s0.ph||0,fx:-1,fy:1,hp:1,max:1};if(s0){a.moving=s0.moving;a.walk=s0.walk;a.sw=s0.sw;a.hurt=s0.hurt}return a}\nfunction cxSpecial(")
open(F,'w').write(s);print('faith allies',tot)
s=open(F).read()
rep("g0_0:{f:'combo',ps:28,vref:6,W:3.4,H:2.7,a:.24,cap:110,","g0_0:{f:'combo',ps:56,vref:3,W:3.4,H:2.7,a:.24,cap:220,")
open(F,'w').write(s);print('nubian x2')
s=open(F).read()
# sizes
rep("g0_0:{f:'combo',ps:56,vref:3,W:3.4,H:2.7,a:.24,cap:220,","g0_0:{f:'combo',ps:50,vref:3.36,W:3.4,H:2.7,a:.24,cap:200,")
rep("g0_1:{f:'mummy',ps:38,vref:1.6,W:3,H:2,a:.3,cap:136,","g0_1:{f:'mummy',ps:34,vref:1.79,W:3,H:2,a:.3,cap:125,")
rep("g0_2:{f:'ark',ps:40,vref:3,W:3.8,H:2.7,a:.3,cap:96,","g0_2:{f:'ark',ps:50,vref:2.4,W:3.8,H:2.7,a:.3,cap:125,")
rep("g0_3:{f:'sphinx',ps:40,vref:5,W:4.2,H:3.6,a:.2,cap:96,","g0_3:{f:'sphinx',ps:50,vref:4,W:4.2,H:3.6,a:.2,cap:125,")
# bigger, legged, visible scarabs
old="ctx.save();ctx.translate(px,py);ctx.rotate(a);ctx.fillStyle='#1d2e7a';ctx.beginPath();ctx.ellipse(0,0,3.2*Z,2.1*Z,0,0,TAU);ctx.fill();\n    ctx.fillStyle='#2f55c8';ctx.beginPath();ctx.ellipse(-.3*Z,-.4*Z,2.4*Z,1.4*Z,0,0,TAU);ctx.fill();ctx.fillStyle='#e8bf55';ctx.beginPath();ctx.arc(2.8*Z,0,1.1*Z,0,TAU);ctx.fill();ctx.restore();if(c.lat>.35)glow(px,py,7*Z,'#ffd27a',.5)}"
new="const k=2.3*Z,lg=Math.sin(time*30+c.a*7);ctx.fillStyle='rgba(30,24,50,.28)';ctx.beginPath();ctx.ellipse(px,py+(up?up*30*Z:1.5*Z),4.2*k,1.8*k,0,0,TAU);ctx.fill();ctx.save();ctx.translate(px,py);ctx.rotate(a);\n    ctx.strokeStyle='#14204f';ctx.lineWidth=.55*k;for(const sd of[-1,1])for(let j=0;j<3;j++){const lx=(j-1)*1.3*k,sw=(j%2?lg:-lg)*.7*k;ctx.beginPath();ctx.moveTo(lx,sd*1.2*k);ctx.lineTo(lx+sw,sd*2.9*k);ctx.stroke()}\n    ctx.fillStyle='#1d2e7a';ctx.beginPath();ctx.ellipse(0,0,3.2*k,2.2*k,0,0,TAU);ctx.fill();ctx.fillStyle='#2f55c8';ctx.beginPath();ctx.ellipse(-.3*k,-.5*k,2.4*k,1.5*k,0,0,TAU);ctx.fill();ctx.strokeStyle='#e8bf55';ctx.lineWidth=.35*k;ctx.beginPath();ctx.moveTo(-3*k,0);ctx.lineTo(1.6*k,0);ctx.stroke();ctx.fillStyle='rgba(255,255,255,.35)';ctx.beginPath();ctx.ellipse(-1*k,-1.1*k,1.1*k,.45*k,0,0,TAU);ctx.fill();ctx.fillStyle='#e8bf55';ctx.beginPath();ctx.arc(3*k,0,1.2*k,0,TAU);ctx.fill();ctx.restore();if(c.lat>.35)glow(px,py,12*Z,'#ffd27a',.55)}"
rep(old,new)
# golden burst from the shell as each brood pours out
rep("for(let i=0;i<12;i++)C.push({x:u.x,y:u.y,tgt:fs[i%fs.length],t:-(.55+1.2*i/12),dmg:t.dmg,side:u.side,src:u,a:R()*TAU,lat:0});return}",
    "for(let i=0;i<12;i++)C.push({x:u.x+(R()-.5)*.3,y:u.y+(R()-.5)*.3,tgt:fs[i%fs.length],t:-(.55+1.2*i/12),dmg:t.dmg,side:u.side,src:u,a:R()*TAU,lat:0});setTimeout(()=>{if(u.hp>0){burst(u.x,u.y,['#e8bf55','#2f55c8','#ffe7a0'],14);ring(u.x,u.y,1.1,'#e8bf55')}},450);return}")
open(F,'w').write(s);print('sizes+scarabs ok')
s=open(F).read()
# behaviour: tumble out of the shell, land, wiggle-run, climb, pop in gold dust (as in the Ark lab)
rep("if(G.crawl&&G.crawl.length){for(const c of G.crawl){c.t+=dt;if(c.t<0)continue;",
    "if(G.crawl&&G.crawl.length){for(const c of G.crawl){c.t+=dt;if(c.t<0)continue;if(c.ph==null){c.ph='out';c.T=.45+R()*.2;const a0=R()*TAU,r0=.45+R()*.4;c.ox=c.x;c.oy=c.y;c.lx=c.x+Math.cos(a0)*r0;c.ly=c.y+Math.sin(a0)*r0;c.ot=0;c.fx=Math.cos(a0);c.fy=Math.sin(a0)}\n      if(c.ph==='out'){c.ot+=dt;const k=Math.min(1,c.ot/c.T);c.x=c.ox+(c.lx-c.ox)*k;c.y=c.oy+(c.ly-c.oy)*k;c.z=.95*(1-k)+Math.sin(k*Math.PI)*.4;c.spin=(c.spin||0)+dt*14;if(k>=1){c.ph='run';c.z=0;c.spin=0}continue}")
rep("if(c.lat>.55){c.dead=true;damageUnit(v,c.dmg,c.src&&c.src.hp>0?c.src:{side:c.side});burst(c.x,c.y,['#e8bf55','#2546b4'],4)}continue}",
    "if(c.lat>.62){c.dead=true;damageUnit(v,c.dmg,c.src&&c.src.hp>0?c.src:{side:c.side});burst(c.x,c.y,['#ffe28c','#f0be50','#ffd27a','#2546b4'],7);(G.fx||(G.fx=[])).push({kind:'gdust',x:c.x,y:c.y,z:(c.ch||.5),life:0,max:.45})}continue}")
rep("if(d<.22){c.lat=.001;continue}","if(d<.22){c.lat=.001;c.ch=.3+R()*.55;continue}")
# drawing
rep("const up=c.lat>0?(.25+Math.min(.5,c.lat)*.9):0;const[px,py]=pj(c.x,c.y,hT(c.x,c.y)+up);if(!onScreen(px,py))continue;",
    "const up=c.ph==='out'?(c.z||0):c.lat>0?(c.ch||.5)*Math.min(1,c.lat/.35):0;const[px,py]=pj(c.x,c.y,hT(c.x,c.y)+up);if(!onScreen(px,py))continue;const[gx0,gy0]=pj(c.x,c.y,hT(c.x,c.y));")
rep("ctx.fillStyle='rgba(30,24,50,.28)';ctx.beginPath();ctx.ellipse(px,py+(up?up*30*Z:1.5*Z),4.2*k,1.8*k,0,0,TAU);ctx.fill();ctx.save();ctx.translate(px,py);ctx.rotate(a);",
    "ctx.fillStyle=`rgba(30,24,50,${up>0?.16:.28})`;ctx.beginPath();ctx.ellipse(gx0,gy0+1.5*Z,4.2*k,1.8*k,0,0,TAU);ctx.fill();ctx.save();ctx.translate(px,py);if(c.lat>0)ctx.rotate(-Math.PI/2+Math.sin(time*7+c.a*3)*.5);else ctx.rotate(a);if(c.ph==='out')ctx.scale(1,Math.cos(c.spin||0));")
# gold dust pop fx
import re
m=re.search(r"function tickFx\(|function addFx\(",s)
open(F,'w').write(s);print('lab scarabs ok')
s=open(F).read()
rep("p.kind==='rootline'||p.kind==='sprout')continue;p.x+=p.vx*dt;","p.kind==='rootline'||p.kind==='sprout'||p.kind==='gdust')continue;p.x+=p.vx*dt;")
rep("  for(const p of G.fx){if(!seeAt(p.x,p.y))continue;const k=p.life/p.max,base=p.flat?WL:hT(p.x,p.y);\n    if(p.kind==='beam'){",
    "  for(const p of G.fx){if(!seeAt(p.x,p.y))continue;const k=p.life/p.max,base=p.flat?WL:hT(p.x,p.y);\n    if(p.kind==='gdust'){const[ax,ay]=pj(p.x,p.y,base+p.z+k*.25);ctx.save();ctx.globalCompositeOperation='lighter';glow(ax,ay,(7+k*12)*Z,'#ffd27a',(1-k)*.8);for(let i=0;i<5;i++){const an=i*1.26+p.x*7,r=(2+k*9)*Z;ctx.fillStyle=`rgba(255,226,140,${(1-k)*.9})`;ctx.beginPath();ctx.arc(ax+Math.cos(an)*r,ay+Math.sin(an)*r*.6-k*5*Z,(1.6-k)*Z+.3,0,TAU);ctx.fill()}ctx.restore();continue}\n    if(p.kind==='beam'){")
open(F,'w').write(s);print('gdust ok')
s=open(F).read()
# Nubian ritual: 1 in 10 per attack sequence
rep("  if(sp==='ritual'){u.ritT=(u.ritT==null?2:u.ritT)-dt;if(u.kneel>0)return true;if(u.ritT>0)return false;\n    const hurt=G.units.filter(a=>a.side===u.side&&a.hp>0&&a.hp<a.max*.8&&Math.hypot(a.x-u.x,a.y-u.y)<3);if(!hurt.length){u.ritT=.6;return false}\n    u.ritT=9;u.kneel=3.5;",
    "  if(sp==='ritual'){if(u.kneel>0)return true;const sw0=u.sw||0;if(sw0>.9&&!u.ritSw){u.ritSw=1;if(R()>=.1)return false}else{if(sw0<.5)u.ritSw=0;return false}\n    u.kneel=3.5;")
rep("When troops near her are hurt she drives both blades into the ground, kneels and lights a ring of healing:",
    "Each attack sequence has a 1 in 10 chance to end in a healing ritual: she drives both blades into the ground, kneels and lights a ring of healing:")
# brood scarabs drawn like the lab model
a=s.index("const k=2.3*Z,lg=Math.sin(time*30+c.a*7);");e=s.index("if(c.lat>.35)glow(px,py,12*Z,'#ffd27a',.55)}",a)
seg=s[a:e]
i1=seg.index("ctx.strokeStyle='#14204f';");i2=seg.index("ctx.restore();",i1)
body=("ctx.strokeStyle='#1a1622';ctx.lineWidth=.42*k;for(const sd of[-1,1])for(let j=0;j<3;j++){const lx=(j-1)*1.05*k,sw=(j%2?lg:-lg)*.75*k;ctx.beginPath();ctx.moveTo(lx,sd*.9*k);ctx.lineTo(lx+sw+(j-1)*.7*k,sd*3.3*k);ctx.stroke()}\n    "
 "ctx.fillStyle='#16296b';ctx.beginPath();ctx.ellipse(0,.15*k,2.9*k,2.1*k,0,0,TAU);ctx.fill();ctx.fillStyle='#2546b4';ctx.beginPath();ctx.ellipse(-.15*k,-.3*k,2.65*k,1.8*k,0,0,TAU);ctx.fill();ctx.fillStyle='#5a86ee';ctx.beginPath();ctx.ellipse(-.7*k,-.85*k,1.35*k,.55*k,-.15,0,TAU);ctx.fill();"
 "ctx.strokeStyle='#e6b84a';ctx.lineWidth=.5*k;ctx.beginPath();ctx.moveTo(-2.5*k,-.3*k);ctx.lineTo(1.9*k,-.3*k);ctx.stroke();ctx.fillStyle='#e6b84a';ctx.beginPath();ctx.arc(2.75*k,-.1*k,1.05*k,0,TAU);ctx.fill();ctx.fillStyle='#fff1c0';ctx.beginPath();ctx.arc(2.5*k,-.5*k,.35*k,0,TAU);ctx.fill();")
seg=seg[:i1]+body+seg[i2:]
seg=seg.replace("const k=2.3*Z,lg=Math.sin(time*30+c.a*7);","const k=1.3*Z,lg=Math.sin(time*34+c.a*7);").replace("ctx.ellipse(gx0,gy0+1.5*Z,4.2*k,1.8*k,0,0,TAU)","ctx.ellipse(gx0,gy0+1*Z,3.6*k,1.5*k,0,0,TAU)")
s=s[:a]+seg+s[e:]
open(F,'w').write(s);print('ritual+look ok')
s=open(F).read()
# plague: 1 brood in 10 becomes a Plague
rep("if(sp==='swarmplague'){u.plT=(u.plT==null?5:u.plT)-dt;if(u.plagueT>0){u.plagueT-=dt;return true}if(u.plT>0)return false;",
    "if(sp==='swarmplague'){if(u.plagueT>0){u.plagueT-=dt;return true}if(!u.plNow)return false;u.plNow=0;")
rep("if(!best){u.plT=.8;return false}u.plT=14;u.plagueT=3.6;","if(!best)return false;u.plagueT=3.6;")
rep("if(t.batk==='brood'){u.openT=2.6;","if(t.batk==='brood'){if(t.special==='swarmplague'&&!(u.plagueT>0)&&R()<.1){u.plNow=1;return}u.openT=2.6;")
rep("Awakened, it calls a Plague every 14 seconds: a flying swarm that churns over a whole group of enemies.",
    "Awakened, each brood has a 1 in 10 chance to burst out as a Plague instead: a flying swarm that churns over a whole group of enemies.")
# brood: no pre-assigned targets; they land, then run at the first enemy they find
rep("C.push({x:u.x+(R()-.5)*.3,y:u.y+(R()-.5)*.3,tgt:fs[i%fs.length],","C.push({x:u.x+(R()-.5)*.3,y:u.y+(R()-.5)*.3,tgt:null,")
rep("if(k>=1){c.ph='run';c.z=0;c.spin=0}continue}",
    "if(k>=1){c.ph='run';c.z=0;c.spin=0;let bd=9,bv=null;for(const e of G.units){if(e.side===c.side||e.hp<=0||e.leap||U[e.type].air||(c.src&&!foeOf(c.src,e)))continue;const d=Math.hypot(e.x-c.x,e.y-c.y);if(d<bd){bd=d;bv=e}}c.tgt=bv}continue}")
# plague-sized
rep("const k=1.3*Z,lg=Math.sin(time*34+c.a*7);","const k=.72*Z,lg=Math.sin(time*34+c.a*7);")
open(F,'w').write(s);print('plague 1/10 + small brood ok')
s=open(F).read()
rep('<h4>Cernunnos · Gaul</h4><ul>','<h4>Cernunnos · Celtic</h4><ul><li><a href="https://claude.ai/artifact/1uKmr4hpqYND1hMueaQY4t" target="_blank" rel="noopener"><b>Verdant Druid → Aged Druid</b><span>Worker and its upgrade: plant, reap, chop; cast, thorns</span></a></li><li><a href="https://claude.ai/artifact/UiyTtgNErB5zV5enJGQ6fv" target="_blank" rel="noopener"><b>Celtic Archer</b><span>Leaping shot, Power Shot</span></a></li>')
rep('<b>Druid</b><span>Wizard movement, burrow</span>','<b>Rootbound Druid</b><span>Wizard movement, burrow</span>')
open(F,'w').write(s);print('labs ok')
