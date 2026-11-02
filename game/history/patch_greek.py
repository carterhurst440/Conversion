F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
G=r"""
// ---------- Greek (Hades) houses of faith: marble temples on a rocky hill, the Great Temple a full peripteral temple ----------
const GRK={m0:'#f6f1e8',m1:'#e4dccc',m2:'#c9bca6',mD:'#a99c86',roofL:'#d4704f',roofD:'#a9472f',hillT:'#a7a274',hillL:'#9b8f74',hillR:'#7f7562',gold:'#e8c35a'};
function grkCol(P,u,v,z0,h,s,gild){const p=P(u,v,z0),w=2.3*s;ctx.fillStyle=GRK.m1;ctx.fillRect(p[0]-w,p[1]-h*s,w*2,h*s);ctx.fillStyle=GRK.m0;ctx.fillRect(p[0]-w,p[1]-h*s,w*.9,h*s);ctx.fillStyle=GRK.m2;ctx.fillRect(p[0]+w*.35,p[1]-h*s,w*.65,h*s);
  ctx.strokeStyle='rgba(150,135,110,.35)';ctx.lineWidth=.6*s;for(const dx of[-.35,.25])line(p[0]+dx*w,p[1]-h*s+2*s,p[0]+dx*w,p[1]-1*s);
  ctx.fillStyle=gild?GRK.gold:GRK.m0;ctx.fillRect(p[0]-w*1.45,p[1]-h*s-1.6*s,w*2.9,1.8*s);ctx.fillStyle=GRK.m2;ctx.fillRect(p[0]-w*1.3,p[1]-1.2*s,w*2.6,1.2*s)}
function grkTemple(sx,sy,s,a,b,z0,ch,rh,nU,nV,great,gc,b2){const P=(u,v,z)=>[sx+(u-v)*32*s,sy+(u+v)*16*s-z*s];
  // the cella behind the colonnade, then the columns from back to front
  const cols=[];for(let i=0;i<nU;i++){const u=-a+2*a*i/(nU-1);cols.push([u,-b],[u,b])}for(let j=1;j<nV-1;j++){const v=-b+2*b*j/(nV-1);cols.push([-a,v],[a,v])}
  cols.sort((p,q)=>(p[0]+p[1])-(q[0]+q[1]));const back=cols.filter(c=>c[0]+c[1]<0),front=cols.filter(c=>c[0]+c[1]>=0);
  for(const[u,v]of back)grkCol(P,u,v,z0,ch,s,great);
  {const C=ibox(sx,sy,s,a*.72,b*.62,z0,ch,null,GRK.m1,GRK.m2);const d=[C(a*.72,.12*b,z0),C(a*.72,-.12*b,z0),C(a*.72,-.12*b,z0+ch*.62),C(a*.72,.12*b,z0+ch*.62)];ctx.fillStyle='#2e2430';poly(d.flat());const dg=C(a*.72,0,z0+ch*.3);glow(dg[0],dg[1],9*s,gc,.55)}
  for(const[u,v]of front)grkCol(P,u,v,z0,ch,s,great);
  const E=ibox(sx,sy,s,a+.03,b+.03,z0+ch,4,GRK.m0,GRK.m1,GRK.m2);
  {ctx.strokeStyle=great?GRK.gold:'rgba(150,135,110,.5)';ctx.lineWidth=(great?1.4:.8)*s;const l0=E(-a-.03,b+.03,z0+ch+2),l1=E(a+.03,b+.03,z0+ch+2),l2=E(a+.03,-b-.03,z0+ch+2);ctx.beginPath();ctx.moveTo(l0[0],l0[1]);ctx.lineTo(l1[0],l1[1]);ctx.lineTo(l2[0],l2[1]);ctx.stroke()}
  gable(E,a+.03,b+.03,z0+ch+4,rh,.05,GRK.roofL,GRK.m1);
  {const t=E(a+.03,0,z0+ch+4+rh*.38);ctx.fillStyle=great?GRK.gold:GRK.m2;ctx.beginPath();ctx.arc(t[0],t[1],(great?3.6:2.4)*s,0,TAU);ctx.fill();if(great)drawSigil(1,t[0],t[1]-.5*s,2.6*s,'#2b2440',false)}
  {const r1=E(-a-.08,b+.08,z0+ch+1),r2=E(a+.08,b+.08,z0+ch+1);ctx.strokeStyle=GRK.roofD;ctx.lineWidth=1.2*s;line(r1[0],r1[1],r2[0],r2[1])}
  if(great){for(const[u,v]of[[a+.03,0],[a+.03,b+.03],[a+.03,-b-.03],[-a-.03,0]]){const p=E(u,v,z0+ch+4+(v===0?rh:0));ctx.fillStyle=GRK.gold;ctx.beginPath();ctx.moveTo(p[0],p[1]-5*s);ctx.lineTo(p[0]-2.4*s,p[1]);ctx.lineTo(p[0]+2.4*s,p[1]);ctx.fill()}}
  return E}
function grkBrazier(x,y,s,gc,b){ctx.fillStyle='#6e5338';ctx.fillRect(x-1*s,y-9*s,2*s,9*s);ctx.fillStyle='#c9a35a';ctx.beginPath();ctx.ellipse(x,y-9*s,4*s,1.6*s,0,0,TAU);ctx.fill();
  const fl=reduceMotion?0:Math.sin(time*9+(b&&b.seed||0)*7+x)*1.2*s;glow(x,y-12*s,10*s,'#ff7a4a',.55);ctx.fillStyle='#ff8a3a';ctx.beginPath();ctx.moveTo(x-3*s,y-9.5*s);ctx.quadraticCurveTo(x+fl,y-18*s,x+3*s,y-9.5*s);ctx.fill();ctx.fillStyle='#ffd27a';ctx.beginPath();ctx.moveTo(x-1.4*s,y-9.5*s);ctx.quadraticCurveTo(x+fl*.6,y-14*s,x+1.4*s,y-9.5*s);ctx.fill()}
function grkHill(sx,sy,s,a,b,h){const P=(u,v,z)=>[sx+(u-v)*32*s,sy+(u+v)*16*s-z*s];
  const tl=P(-a,b,h),tr=P(a,b,h),tb=P(a,-b,h),tt=P(-a,-b,h),bl=P(-a*1.12,b*1.12,0),bf=P(a*1.12,b*1.12,0),br=P(a*1.12,-b*1.12,0);
  ctx.fillStyle=GRK.hillL;poly([...bl,...bf,...tr,...tl]);ctx.fillStyle=GRK.hillR;poly([...bf,...br,...tb,...tr]);ctx.fillStyle=GRK.hillT;poly([...tl,...tr,...tb,...tt]);
  ctx.fillStyle='rgba(60,50,40,.25)';for(const[u,v,r]of[[-.5,1.02,3],[.2,1.04,2.4],[1.04,.3,2.8],[1.04,-.5,2]]){const p=P(u*a,v*b,h*.45);ctx.beginPath();ctx.ellipse(p[0],p[1],r*s,r*.6*s,0,0,TAU);ctx.fill()}
  ctx.fillStyle='#6f8f4a';for(const[u,v]of[[-.8,1.05],[.7,1.06],[1.06,-.7]]){const p=P(u*a,v*b,h*.2);ctx.beginPath();ctx.arc(p[0],p[1]-2*s,2.4*s,0,TAU);ctx.fill()}
  return P}
function drawGreek(b,sx,sy,s,live,C1,C2){const gc=GODS[1].col;
  if(b.type==='hall'){const tier=live&&G.S[b.side]?G.S[b.side].tier:1,great=tier>=2;blobShadow(sx,sy,s,64);
    const H=great?12:9;grkHill(sx,sy,s,.92,.86,H);
    // stepped stylobate and a stair down the hill in front
    const st1=ibox(sx,sy,s,.82,.74,H,2.5,GRK.m1,GRK.m2,GRK.mD);ibox(sx,sy,s,.77,.69,H+2.5,2.5,GRK.m0,GRK.m1,GRK.m2);ibox(sx,sy,s,.72,.64,H+5,2.5,GRK.m0,GRK.m1,GRK.m2);
    {const P=(u,v,z)=>[sx+(u-v)*32*s,sy+(u+v)*16*s-z*s];for(let k=0;k<5;k++){const u0=.92+(4-k)*.05,z=H*(k/5),A=P(u0,.22,z),Bq=P(u0,-.22,z),C=P(u0+.05,-.22,z),D=P(u0+.05,.22,z);ctx.fillStyle=k%2?GRK.m1:GRK.m0;poly([...A,...Bq,...C,...D])}}
    if(great){grkTemple(sx,sy,s,.62,.52,H+7.5,30,14,6,5,true,gc,b);const P=(u,v,z)=>[sx+(u-v)*32*s,sy+(u+v)*16*s-z*s];for(const v of[.36,-.36]){const p=P(.86,v,H+7.5);grkBrazier(p[0],p[1],s,gc,b)}}
    else{grkTemple(sx,sy,s,.56,.44,H+7.5,24,11,5,4,false,gc,b);const P=(u,v,z)=>[sx+(u-v)*32*s,sy+(u+v)*16*s-z*s];const p=P(.84,.3,H+7.5);grkBrazier(p[0],p[1],s,gc,b)}
    const fr=[];for(let k=0;k<tier;k++)fr.push([sx+(-.7+k*.155-.74)*32*s,sy+(-.7+k*.155+.74)*16*s-3*s]);for(const p of fr){glow(p[0],p[1],5*s,C1,.6);ctx.fillStyle='#fff3e6';ctx.beginPath();ctx.arc(p[0],p[1],1.4*s,0,TAU);ctx.fill()}
    return true}
  if(b.type==='chapel'){const great=!!b.temple;blobShadow(sx,sy,s,30);grkHill(sx,sy,s,.42,.38,5);ibox(sx,sy,s,.36,.32,5,2,GRK.m0,GRK.m1,GRK.m2);
    grkTemple(sx,sy,s,.26,.2,7,great?19:16,great?9:7,4,3,great,gc,b);if(great){const P=(u,v,z)=>[sx+(u-v)*32*s,sy+(u+v)*16*s-z*s],p=P(.38,.2,5);grkBrazier(p[0],p[1],s,gc,b)}
    return true}
  return false}
"""
rep("function drawBld(b,sx,sy,s,live){",G.lstrip('\n')+"function drawBld(b,sx,sy,s,live){")
rep("if(cg===8&&b.type!=='wall'&&drawCelt(b,sx,sy,s,live,C1,C2)){if(b.bless!=null)drawBless(b,sx,sy,s);return}}",
    "if(cg===8&&b.type!=='wall'&&drawCelt(b,sx,sy,s,live,C1,C2)){if(b.bless!=null)drawBless(b,sx,sy,s);return}if(cg===1&&drawGreek(b,sx,sy,s,live,C1,C2))return}")
open(F,'w').write(s);print('greek temples ok')
