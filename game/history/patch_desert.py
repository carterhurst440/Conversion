F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a)
    assert c==n,(c,a[:90])
    s=s.replace(a,b)

# ---------- Egypt's faith ground: brown desert dirt, raw sandstone, date palms ----------
rep("wh:'dot'}\n];\nconst GODBIO","wh:'dot'},\n {name:'Deshret',grass:'#c9a274',sand:'#ead3a6',tree:'palm',treeTint:'#b59a63',rock:['#f2d6a2','#dcb57c','#b98c56'],rockS:'sandstone',clay:['#d99a6c','#b06e48'],wheat:['#b8964a','#e8cf82','#d4b55f','#f3dc95']}\n];\nconst GODBIO")
rep("const GODBIO={1:4,7:5,8:6,4:7,6:8};","const GODBIO={0:9,1:4,7:5,8:6,4:7,6:8};")

# sandstone: two or three squared blocks, stacked and chisel-scored
rep("    if(bi.rockS==='grave'){",
r"""    if(bi.rockS==='sandstone'){const pal=bi.rock,P=(u,v)=>[sx+(u-v)*hw,sy+(u+v)*hh];
      const blk=(u,v,a,b,z,h)=>{const p=P(u,v);const Q=ibox(p[0],p[1],s,a,b,z,h,pal[0],pal[1],pal[2]);ctx.strokeStyle='rgba(120,84,44,.35)';ctx.lineWidth=.7*s;
        const l0=Q(-a,b,z+h*.5),l1=Q(a,b,z+h*.5);line(l0[0],l0[1],l1[0],l1[1]);const r0=Q(a,b,z+h*.5),r1_=Q(a,-b,z+h*.5);line(r0[0],r0[1],r1_[0],r1_[1]);
        const m0=Q(0,b,z),m1=Q(0,b,z+h*.5);line(m0[0],m0[1],m1[0],m1[1])};
      ctx.fillStyle='rgba(90,60,30,.16)';ctx.beginPath();ctx.ellipse(sx+2*s,sy+2*s,hw*.62,hh*.62,0,0,TAU);ctx.fill();
      blk(-.1,-.08,.2,.15,0,9+r1*3);blk(.16,.12,.13,.12,0,7+r2*2);if(r1>.35)blk(-.08,-.05,.13,.1,9+r1*3,6);else blk(-.22,.2,.09,.08,0,5);
      return}
    if(bi.rockS==='grave'){""")
# date palms
rep("      else if(bi.tree==='cactus'){",
r"""      else if(bi.tree==='palm'){const Hh=(24+r1*10)*ss,lean=(q-.5)*8*ss;ctx.strokeStyle='#8a6a48';ctx.lineCap='round';ctx.lineWidth=3*ss;ctx.beginPath();ctx.moveTo(tx,ty);ctx.quadraticCurveTo(tx+lean*.2,ty-Hh*.5,tx+lean,ty-Hh);ctx.stroke();
        ctx.strokeStyle='rgba(60,42,26,.35)';ctx.lineWidth=.8*ss;for(let m=1;m<6;m++){const t=m/6,px=tx+lean*t*t,py=ty-Hh*t;line(px-1.4*ss,py,px+1.4*ss,py-.8*ss)}
        const top=[tx+lean,ty-Hh];for(const[a,c]of[[-2.7,'#4f8a46'],[-.45,'#4f8a46'],[-2.1,'#6aa65a'],[-1.05,'#6aa65a'],[-1.6,'#7fba68'],[.2,'#5d9850'],[-3.3,'#5d9850']]){const L=13*ss,ex=top[0]+Math.cos(a)*L,ey=top[1]+Math.sin(a)*L*.55+6*ss;
          ctx.fillStyle=c;ctx.beginPath();ctx.moveTo(top[0],top[1]);ctx.quadraticCurveTo((top[0]+ex)/2+Math.sin(a)*2*ss,top[1]-5*ss,ex,ey);ctx.quadraticCurveTo((top[0]+ex)/2,top[1]+1*ss,top[0],top[1]+1.5*ss);ctx.fill()}
        if(q>.4){ctx.fillStyle='#b5652e';for(const d of[-1.6,1.4,0])ctx.beginPath(),ctx.arc(top[0]+d*ss,top[1]+2.6*ss,1.3*ss,0,TAU),ctx.fill()}}
      else if(bi.tree==='cactus'){""")

# ---------- canals: pure blue traces that run in straight lines with right-angle turns ----------
a=s.find("const x0=b.x+.5,y0=b.y+.5,dx=py[0]-x0");b=s.find("for(const pl of G.pools){if(!seeAt(pl.x,pl.y))continue;",a)
assert a>0 and b>a
s=s[:a]+r"""const x0=b.x+.5,y0=b.y+.5,x1=py[0],y1=py[1],xm=Math.round((x0+x1)/2-.5)+.5,cn=[[x0,y0],[xm,y0],[xm,y1],[x1,y1]],pts=[],corn=[];
    for(let q=0;q<3;q++){const[ax,ay]=cn[q],[bx,by]=cn[q+1],n=Math.max(1,Math.ceil(Math.hypot(bx-ax,by-ay)*2));for(let k=0;k<=n;k++){if(q&&!k)continue;const t=k/n,x=ax+(bx-ax)*t,y=ay+(by-ay)*t;pts.push(pj(x,y,hT(x,y)))}if(q<2)corn.push(pj(bx,by,hT(bx,by)))}
    if(!pts.some(p=>onScreen(p[0],p[1])))continue;ctx.save();ctx.lineCap='square';ctx.lineJoin='miter';const path=()=>{ctx.beginPath();ctx.moveTo(pts[0][0],pts[0][1]);for(let k=1;k<pts.length;k++)ctx.lineTo(pts[k][0],pts[k][1])};
    path();ctx.strokeStyle='#1f8fff';ctx.lineWidth=3*Z;ctx.stroke();ctx.fillStyle='#1f8fff';for(const c of corn){ctx.fillRect(c[0]-2.6*Z,c[1]-2.6*Z,5.2*Z,5.2*Z)}
    {const p0=pts[0];ctx.beginPath();ctx.arc(p0[0],p0[1],3.4*Z,0,TAU);ctx.fill()}ctx.restore()}
  """+s[b:]

# ---------- Obelisk: Egypt's long-range defense, researched before it can be built ----------
rep("function LIM(side,k){","function LIM(side,k){if(k==='tower'&&EGY(side)&&!hasT(side,'btower'))return 0;")
rep("if(T.bty&&!(BLESS[S.god]&&BLESS[S.god][T.bty]))return{hide:true};","if(T.bty&&(T.bty!=='tower'||S.god!==0))return{hide:true};")
rep("&&!(TECH[k].bty&&!(BLESS[g]&&BLESS[g][TECH[k].bty])))","&&!(TECH[k].bty&&(TECH[k].bty!=='tower'||g!==0)))")
rep("function techDesc(k,side){const g=G.S[side]?G.S[side].god:-1;","function techDesc(k,side){const g=G.S[side]?G.S[side].god:-1;if(k==='btower'&&g===0)return`Unlocks the Obelisk, Egypt’s long-range defense. ${BLESS[0].tower.desc} Long range: picks off one target at a time.`;")
rep("btower:{br:'Defenses',bty:'tower',name:'',tier:1,cost:{wood:6,stone:4},time:25,","btower:{br:'Defenses',bty:'tower',name:'',tier:1,cost:{stone:12,wheat:8},time:25,")
rep("LIMIT[k][S.tier-1]===0,full=n>=lim&&!locked","LIMIT[k][S.tier-1]===0||(k==='tower'&&EGY(0)&&!hasT(0,'btower')),full=n>=lim&&!locked")
rep("${locked?'Needs '+(k==='veil'?","${locked&&k==='tower'?'Needs research':locked?'Needs '+(k==='veil'?")
rep("        if(locked){toast(k==='veil'?","        if(locked&&k==='tower'){toast('Research the Obelisk in Tech first.');return}\n        if(locked){toast(k==='veil'?")

# ---------- Quarrying is a research for Egypt too (mining stays free) ----------
rep("if((k==='mining'||k==='quarry')&&EGY(side))return true;","if(k==='mining'&&EGY(side))return true;")
rep("if(T.req&&!S.tech[T.req])return{lock:","if(T.req&&!(k==='quarry'&&S.god===0)&&!S.tech[T.req])return{lock:")

# ---------- Stonebearers find rock anywhere nearby, not only inside the rings ----------
rep("for(const i of ringTiles(u.side)){if(dep[i]!==kind||cells[i]||cl.has(i)||isl[i]!==i0||picked(i))continue;",
    "for(const i of(kind==='rock'&&EGY(u.side)?nearT(u,16):ringTiles(u.side))){if(dep[i]!==kind||cells[i]||cl.has(i)||isl[i]!==i0||picked(i))continue;")
rep("rock:'No rock in your rings'}[kind]","rock:EGY(u.side)?'No rock nearby':'No rock in your rings'}[kind]")
rep("function workTick(u,dt){","function nearT(u,r){const o=[],x0=u.x|0,y0=u.y|0;for(let y=Math.max(0,y0-r);y<=Math.min(WN-1,y0+r);y++)for(let x=Math.max(0,x0-r);x<=Math.min(WN-1,x0+r);x++)o.push(y*WN+x);return o}\nfunction workTick(u,dt){")

# ---------- hauling: Egyptian stone is a sandstone block dragged home on ropes ----------
rep("  let top;if(u.spin>0){","  if(u.carry&&u.carry.k==='stone'&&EGY(u.side))dragBlock(u,sx,sy,s,0);\n  let top;if(u.spin>0){")
rep("  if(u.carry){const c=MATCOL[u.carry.k],bx=sx-fl*7*s,by=sy-20*s;",
r"""  if(u.carry&&u.carry.k==='stone'&&EGY(u.side)){dragBlock(u,sx,sy,s,1)}
  else if(u.carry){const c=MATCOL[u.carry.k],bx=sx-fl*7*s,by=sy-20*s;""")
rep("function workTick(u,dt){",
r"""function dragBlock(u,sx,sy,s,pass){const mx=u.x-(u.dbx==null?u.x:u.dbx),my=u.y-(u.dby==null?u.y:u.dby),ml=pass?Math.hypot(mx,my):0;if(pass){u.dbx=u.x;u.dby=u.y}
  if(ml>.0005){u.ddx=(u.ddx||0)*.8+mx/ml*.2;u.ddy=(u.ddy||0)*.8+my/ml*.2}let dx=u.ddx||-.7,dy=u.ddy||-.7;const dl=Math.hypot(dx,dy)||1;dx/=dl;dy/=dl;
  const wx=u.x-dx*.55,wy=u.y-dy*.55,[bx,by]=pj(wx,wy,hT(wx,wy)),n=u.carry.n,a=.13+n*.015,h=8+n*1.5,pal=BIO[9].rock;if((by<sy)!==(pass===0))return;
  ctx.fillStyle='rgba(90,60,30,.22)';ctx.beginPath();ctx.ellipse(bx,by+1*s,(a*32+3)*s,(a*16+2)*s,0,0,TAU);ctx.fill();
  const Q=ibox(bx,by,s,a,a*.8,0,h,pal[0],pal[1],pal[2]);ctx.strokeStyle='rgba(120,84,44,.4)';ctx.lineWidth=.7*s;{const p=Q(-a,a*.8,h*.5),q=Q(a,a*.8,h*.5),r=Q(a,-a*.8,h*.5);line(p[0],p[1],q[0],q[1]);line(q[0],q[1],r[0],r[1])}
  const hx=sx,hy=sy-11*s,c1=Q(-a*.6,a*.8,h*.7),c2=Q(a,-a*.5,h*.7);ctx.strokeStyle='#7a5a36';ctx.lineWidth=1.3*s;ctx.lineCap='round';
  for(const c of[c1,c2]){ctx.beginPath();ctx.moveTo(c[0],c[1]);ctx.quadraticCurveTo((c[0]+hx)/2,Math.max(c[1],hy)+3*s,hx,hy);ctx.stroke()}
  ctx.strokeStyle='#a3824f';ctx.lineWidth=1.1*s;{const t0=Q(-a,a*.8,h*.7),t1=Q(a,a*.8,h*.7),t2=Q(a,-a*.8,h*.7);ctx.beginPath();ctx.moveTo(t0[0],t0[1]);ctx.lineTo(t1[0],t1[1]);ctx.lineTo(t2[0],t2[1]);ctx.stroke()}
  if(ml>.002&&!reduceMotion&&Math.random()<.06)burst(wx,wy,['#d9b98a','#c9a274'],1)}
function workTick(u,dt){""")
open(F,'w').write(s);print('desert ok',len(s))
s=open(F).read()
rep("function techState(side,k){const S=G.S[side],T=TECH[k];if(S.tech[k])return{done:true};","function techState(side,k){const S=G.S[side],T=TECH[k];if(S.tech[k]||(k==='mining'&&S.god===0))return{done:true};")
rep("for(const t of AITECH){const st=techState(k,t);","for(const t of EGY(k)?['quarry','btower',...AITECH]:AITECH){const st=techState(k,t);")
open(F,'w').write(s);print('egypt ai tech ok')
s=open(F).read()
# ---------- Sphinx balance: was ~2.7x the health and ~1.8x the damage of other big faith beasts ----------
rep("{name:'Sphinx',hp:900,dmg:30,rate:.9,range:1.1,spd:2,house:4,lv:3,body:'beast',kind:'hound',scale:1.3,splash:.7,",
    "{name:'Sphinx',hp:560,dmg:20,rate:.8,range:1.1,spd:1.8,house:4,lv:3,body:'beast',kind:'hound',scale:1.3,splash:.5,")
rep("splashAt(u.skyX,u.skyY,1.6,t.dmg*2.2,u.side,false,true,false,u);ring(u.skyX,u.skyY,1.6,","splashAt(u.skyX,u.skyY,1.3,t.dmg*1.8,u.side,false,true,false,u);ring(u.skyX,u.skyY,1.3,")
rep("Skyfall that hits everything around for 2.2\\u00d7 damag","Skyfall that hits everything around for 1.8\\u00d7 damag")
open(F,'w').write(s);print('sphinx nerf ok')
s=open(F).read()
# ---------- Admin switch: unlimited resources and zero build / train / research times for you ----------
RICH="(typeof ADM!=='undefined'&&ADM.rich)"
rep("function can(side,c){c=CX(side,c);","function can(side,c){if(side===0&&"+RICH+")return true;c=CX(side,c);")
rep("function pay(side,c){c=CX(side,c);","function pay(side,c){if(side===0&&"+RICH+")return;c=CX(side,c);")
rep("if(!built(b)){b.bp+=dt;b.hp=Math.min(b.max,b.hp+b.max*.75*dt/b.bt);",
    "if(!built(b)){const ia=b.side===0&&"+RICH+";b.bp+=ia?b.bt+1:dt;b.hp=ia?b.max:Math.min(b.max,b.hp+b.max*.75*dt/b.bt);")
rep("if(b.queue.length){b.qt+=dt;","if(b.queue.length){b.qt+=b.side===0&&"+RICH+"?1e6:dt;")
rep("if(!r||!S.alive)continue;r.t+=dt;","if(!r||!S.alive)continue;r.t+=S.side===0&&"+RICH+"?1e6:dt;")
rep("function update(dt){\n  G.t+=dt;","function update(dt){\n  G.t+=dt;if("+RICH+")for(const k of RES)if(k in G.S[0].res)G.S[0].res[k]=Math.max(G.S[0].res[k],k==='souls'?999:capRes(0,k));")
rep("opt('For','side',[[0,'You'],[1,'Enemy']]);","opt('Unlimited','rich',[[true,'On: free & instant'],[false,'Off']]);opt('For','side',[[0,'You'],[1,'Enemy']]);")
rep("function openAdmin(){select(null);","function openAdmin(){if(ADM.rich==null){ADM.rich=true;toast('Admin: unlimited resources, instant builds, training and research')}select(null);")
open(F,'w').write(s);print('admin rich ok')
