F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
def cut(start,end,new):
    global s
    i=s.find(start);assert i>=0,start[:80]
    j=s.find(end,i);assert j>=0,end[:80]
    s=s[:i]+new+s[j:]

# ================= five world themes =================
rep("const MAPNAME={continent:'Highlands',straits:'Riven Straits',isles:'Fire Isles'};",r"""const THEMES={
 volcano:{n:'Volcano',layout:'ring',bios:[10,11,10],obs:'lava',zt:[.3,.48,.9],deep:'#2e1f26',shallow:'#7a3f32',wave:'255,170,110',bg:['#3b2a2c','#22171b'],vig:'40,10,10',mote:'ember',twist:'The volcano erupts every so often: molten bombs rain down near its crater and burn anyone caught there.'},
 mushroom:{n:'Mushroom Magic',layout:'isles',bios:[12,13,12],obs:'gshroom',zt:[.34,.74,.9],deep:'#3d3478',shallow:'#7fd8cc',wave:'210,255,250',bg:['#3b3268','#262050'],vig:'30,20,70',mote:'spore',twist:'Glowing spores drift everywhere: every troop slowly heals on its own.'},
 moon:{n:'Moon',layout:'continent',bios:[14,15,14],obs:'craterrim',zt:[.28,.5,.9],deep:'#10102a',shallow:'#262848',wave:'230,235,255',bg:['#0c0c1e','#05050d'],vig:'0,0,20',mote:'star',twist:'Low gravity: every troop moves 15% faster. Crater rims block the way.'},
 jungle:{n:'Deep Jungle',layout:'straits',bios:[16,17,16],obs:'thicket',zt:[.28,.76,.9],deep:'#2a5f52',shallow:'#6aa886',wave:'210,255,230',bg:['#4a7a64','#33584a'],vig:'10,40,20',mote:'rain',twist:'The jungle grows back fast: groves regrow in half the time. Rivers and thickets wall off the land.'},
 mountains:{n:'High Mountains',layout:'continent',bios:[18,19,18],obs:'peak',zt:[.26,.5,.92],deep:'#4a80a6',shallow:'#a6d6e6',wave:'235,250,255',bg:['#a4c8da','#7fb0c8'],vig:'30,40,60',mote:'snow',twist:'Rich veins: boulders often give an extra stone. Long ridges leave only narrow passes.'}};
const THEME_K=Object.keys(THEMES);let THEME='mountains';const MAPNAME={};for(const k in THEMES)MAPNAME[k]=THEMES[k].n;
const VCEN={x:60,y:60},CFLOOR=new Uint8Array(WN*WN);""")
rep("const DEEP=hexRgb('#5f9fb6'),SHALLOW=hexRgb('#9fd8dc');","let DEEP=hexRgb('#5f9fb6'),SHALLOW=hexRgb('#9fd8dc');")
# biomes for each theme (indices 10-19)
rep(" {name:'Deshret',"," {name:'Deshret',",1)
i=s.find(" {name:'Deshret',");j=s.find("\n];",i)
s=s[:j]+r""",
 {name:'Ashlands',grass:'#6b5f5a',sand:'#3e3537',tree:'charred',treeTint:'#4a403c',rock:['#5a5060','#3a3442','#221e28'],rockS:'ember',clay:['#a0583c','#7a3a24'],wheat:['#b2452a','#ff8a3a','#e86a2a','#ffc27a'],wh:'bloom'},
 {name:'Cinder Plains',grass:'#8a5c4a',sand:'#4a3a3a',tree:'charred',treeTint:'#5a4038',rock:['#5f4f58','#3d3340','#251f28'],rockS:'ember',clay:['#b0623e','#84402a'],wheat:['#a8863a','#e8b86a','#cf9a4f','#f6d19a']},
 {name:'Spore Glade',grass:'#9384c8',sand:'#d9cff4',tree:'shroom',treeTint:'#b79be8',rock:'crystal',clay:['#e7a08f','#c27264'],wheat:'glow'},
 {name:'Fungal Fen',grass:'#62ab9e',sand:'#cfeee6',tree:'shroom',treeTint:'#7fd8c8',rock:'crystal',clay:['#d99ac0','#b06a94'],wheat:'glow'},
 {name:'Regolith',grass:'#bab8c6',sand:'#dcdbe4',tree:'moonbloom',treeTint:'#a6a3bd',rock:['#dcdbe4','#aaa8ba','#7f7d93'],rockS:'moon',clay:['#b8a8c8','#8a7aa0'],wheat:['#8f96c4','#dfe4ff','#c4caf0','#ffffff'],wh:'dot'},
 {name:'Dark Mare',grass:'#8e8ca0',sand:'#bdbccb',tree:'moonbloom',treeTint:'#8a87a4',rock:['#c4c2d0','#94929f','#6a6878'],rockS:'moon',clay:['#a898b8','#7a6a90'],wheat:['#8f96c4','#dfe4ff','#c4caf0','#ffffff'],wh:'dot'},
 {name:'Rainforest',grass:'#4a9446',sand:'#cfc79a',tree:'jungle',treeTint:'#2f7a3a',rock:['#90a68a','#6a8065','#4f6050'],rockS:'moss',clay:['#c98a5c','#9a5a34'],wheat:['#4f8a2a','#8cc44a','#6aa83a','#b8e06a'],wtall:1.3},
 {name:'Cloud Forest',grass:'#6aaa66',sand:'#d6d0a6',tree:'jungle',treeTint:'#4f9a5a',rock:['#a4b89e','#7d9278','#5a6c58'],rockS:'moss',clay:['#c98a5c','#9a5a34'],wheat:['#5f9a3a','#9cd45a','#7ab84a','#c8ea7a'],wtall:1.2},
 {name:'Alpine Meadow',grass:'#a8c49a',sand:'#e8ecef',tree:'pine',treeTint:'#7fa59a',rock:['#e0e4ea','#aab2bf','#7d8696'],clay:['#d9a890','#b07a62'],wheat:['#b8a85a','#e8d88a','#d4c46a','#f3e8a5']},
 {name:'Snowfield',grass:'#e4ecf2',sand:'#f2f5f7',tree:'pine',treeTint:'#c2d4dc',rock:['#f2f6fa','#c3d0de','#99a9bd'],clay:['#e4b5a3','#bf8270'],wheat:['#b3ae95','#ece6c8','#d6cfae','#fffbe6']}"""+s[j:]
# ---------- generation ----------
rep("function genWorld(np){for(let t=0;t<60;t++){","function genWorld(np){THEME=MAPPICK!=='random'&&THEMES[MAPPICK]?MAPPICK:THEME_K[R()*THEME_K.length|0];for(let t=0;t<60;t++){")
rep("MODE=MAPPICK!=='random'?MAPPICK:rm<.38?'continent':rm<.68?'straits':'isles';MAPMODE=MODE;","MODE=THEMES[THEME].layout;MAPMODE=THEME;CFLOOR.fill(0);")
rep("    if(MODE!=='continent'){const dx=x+.5-WN/2,","    if(MODE==='ring'){const rr=Math.hypot(x+.5-WN/2,y+.5-WN/2)/WN;e=.5+(.41-rr)*1.4+(fbm(x/13,y/13,SEED+11,4)-.5)*.42;if(rr<.12)e=Math.max(e,.9)}\n    else if(MODE!=='continent'){const dx=x+.5-WN/2,")
rep("pts.push([rnd(0,WN),rnd(0,WN),k<4?k:R()*4|0]);","pts.push([rnd(0,WN),rnd(0,WN),THEMES[THEME].bios[k<3?k:R()*3|0]]);")
rep("TH=MODE==='continent'?[.26,.52,.9]:MODE==='isles'?[.36,.78,.92]:[.3,.6,.9];","TH=THEMES[THEME].zt;")
rep("if(STARTS.some(h=>Math.hypot(h.x+1-x,h.y+1-y)<12))return false;return!VILLS","if(STARTS.some(h=>Math.hypot(h.x+1-x,h.y+1-y)<12))return false;if(THEME==='volcano'&&Math.hypot(x-WN/2,y-WN/2)<9)return false;return!VILLS")
cut("  {const kind=MODE==='continent'?'peak':MODE==='straits'?'chasm':'spire',near=","    // never seal off",r"""  {const kind=THEMES[THEME].obs,near=(x,y)=>STARTS.some(h=>Math.hypot(h.x+1-x,h.y+1-y)<9)||VILLS.some(v=>Math.hypot(v.x-x,v.y-y)<4.5);
    const put=(x,y,k2)=>{if(!inb(x,y))return;const i=idx(x,y);if(!land[i]||beachA[i]||OBS[i]||near(x,y)||ldist[i]<2)return;OBS[i]=1;dep[i]=k2||kind;zone[i]=0};
    const spot=()=>{for(let tr=0;tr<300;tr++){const x=4+R()*(WN-8)|0,y=4+R()*(WN-8)|0,i=idx(x,y);if(land[i]&&!beachA[i]&&ldist[i]>=3&&!near(x,y))return[x,y]}return null};
    const ridge=(x,y,a,L,wig,fat)=>{let fx=x+.5,fy=y+.5;for(let q=0;q<L;q++){put(Math.floor(fx),Math.floor(fy));if(fat&&R()<fat)put(Math.floor(fx)+(R()<.5?1:0),Math.floor(fy)+(R()<.5?1:0));a+=(R()-.5)*wig;fx+=Math.cos(a);fy+=Math.sin(a)}};
    if(THEME==='volcano'){const cx=WN/2|0,cy=WN/2|0;VCEN.x=cx+.5;VCEN.y=cy+.5;for(let y=cy-4;y<=cy+4;y++)for(let x=cx-4;x<=cx+4;x++){if(!inb(x,y))continue;const d=Math.hypot(x-cx,y-cy),i=idx(x,y);if(d<3.4&&land[i]){OBS[i]=1;dep[i]=(x===cx&&y===cy)?'volcano':'cinder';zone[i]=0}}
      const nr=6+(R()*3|0),a0=R()*TAU;for(let k=0;k<nr;k++){const a=a0+k*TAU/nr+(R()-.5)*.4;ridge(Math.floor(cx+Math.cos(a)*4),Math.floor(cy+Math.sin(a)*4),a,9+(R()*10|0),.5,0)}}
    else if(kind==='craterrim'){const nc=13+(R()*5|0);for(let k=0;k<nc;k++){const p=spot();if(!p)continue;const r=2+R()*2.4,gap=R()*TAU;for(let a=0;a<TAU;a+=.32){if(Math.abs(((a-gap+TAU)%TAU)-Math.PI)>Math.PI-.5)continue;put(Math.round(p[0]+Math.cos(a)*r),Math.round(p[1]+Math.sin(a)*r))}
      for(let y=Math.floor(p[1]-r);y<=p[1]+r;y++)for(let x=Math.floor(p[0]-r);x<=p[0]+r;x++)if(inb(x,y)&&Math.hypot(x-p[0],y-p[1])<r-.7){const i=idx(x,y);CFLOOR[i]=1;if(!OBS[i])dep[i]=null}}}
    else if(kind==='peak'){const n=16+(R()*5|0);for(let k=0;k<n;k++){const p=spot();if(p)ridge(p[0],p[1],R()*TAU,9+(R()*12|0),.45,.55)}}
    else{const n=kind==='thicket'?24+(R()*8|0):18+(R()*6|0);for(let k=0;k<n;k++){const p=spot();if(!p)continue;const m=kind==='thicket'?4+(R()*6|0):2+(R()*4|0);for(let q=0;q<m;q++)put(p[0]+(R()*4|0)-1,p[1]+(R()*4|0)-1)}}
    // never seal off""")
rep("    // never seal off part of an island: open any obstacle that walls in a pocket","    // never seal off part of an island: open any obstacle that walls in a pocket (the volcano itself stays)")
rep("let opened=false;for(let i=0;i<WN*WN;i++){if(!OBS[i]||dep[i]==='hut')continue;","let opened=false;for(let i=0;i<WN*WN;i++){if(!OBS[i]||dep[i]==='hut'||dep[i]==='volcano'||dep[i]==='cinder')continue;")
rep("hv[vy*VN+vx]=water?.72:bch?.95+n*.12:1.05+clamp((e-.52)*7,0,2.6)+n*.4}","const amp=THEME==='mountains'?1.7:THEME==='moon'?.6:1;hv[vy*VN+vx]=water?.72:bch?.95+n*.12:1.05+clamp((e-.52)*7*amp,0,2.6*amp)+n*.4*(THEME==='moon'?.5:1)}")
rep("if(!beachA[i]&&dp==='chasm')","if(!beachA[i]&&CFLOOR[i])base=mixRgb(base,[90,88,110],.28);if(!beachA[i]&&(dp==='lava'||dp==='cinder'||dp==='volcano'))base=mixRgb(base,[40,28,30],.6);if(!beachA[i]&&dp==='thicket')base=mixRgb(base,[30,70,36],.45);if(!beachA[i]&&dp==='gshroom')base=mixRgb(base,[90,60,140],.25);if(!beachA[i]&&dp==='chasm')")
rep("FULL={tree:1,wheat:1,rock:1,clay:1,peak:1,chasm:1,spire:1,hut:1}","FULL={tree:1,wheat:1,rock:1,clay:1,peak:1,chasm:1,spire:1,hut:1,lava:1,cinder:1,volcano:1,gshroom:1,craterrim:1,thicket:1}")
# apply the theme's sea when a game is made
rep("G.villages=VILLS.map(v=>Object.assign({},v));G.mapMode=MAPMODE;","G.villages=VILLS.map(v=>Object.assign({},v));G.mapMode=MAPMODE;G.theme=THEME;G.eruT=18;G.erupt=[];DEEP=hexRgb(THEMES[THEME].deep);SHALLOW=hexRgb(THEMES[THEME].shallow);{const mi=document.getElementById('mapinfo');if(mi)mi.innerHTML=`<b>${THEMES[THEME].n}</b> \\u00b7 ${THEMES[THEME].twist}`}")
# ---------- twists ----------
rep("(u.root>0?0:1)*(u.petal>0?1.4:1);","(u.root>0?0:1)*(u.petal>0?1.4:1)*(G&&G.theme==='moon'?1.15:1);")
rep("if(godOf(u.side)===8&&u.hp<u.max)u.hp=Math.min(u.max,u.hp+3*dt);","if(godOf(u.side)===8&&u.hp<u.max)u.hp=Math.min(u.max,u.hp+3*dt);if(G.theme==='mushroom'&&u.hp<u.max&&u.hp>0)u.hp=Math.min(u.max,u.hp+1.5*dt);")
s=s.replace("GROW[k]*","GROW[k]*(G.theme==='jungle'&&k==='tree'?.5:1)*")
rep("const n=hasT(u.side,'veins')&&R()<1/3?2:1;","const n=(hasT(u.side,'veins')&&R()<1/3?2:1)+(G.theme==='mountains'&&kind==='rock'&&R()<.35?1:0);")
rep("  updBuildings(dt);if(G.traps)",r"""  if(G.theme==='volcano'&&!G.arena&&G.started){G.eruT-=dt;if(G.eruT<=0){G.eruT=22+R()*10;for(let k=0;k<5;k++){const a=R()*TAU,d=4.5+R()*8,x=VCEN.x+Math.cos(a)*d,y=VCEN.y+Math.sin(a)*d;if(landAt(x,y))G.erupt.push({x,y,t:2,max:2})}if(seeAt(VCEN.x,VCEN.y))toast('The volcano erupts!',true)}
    for(const e of G.erupt){e.t-=dt;if(e.t<=0&&!e.done){e.done=1;for(const u of G.units)if(u.hp>0&&!u.leap&&!U[u.type].air&&Math.hypot(u.x-e.x,u.y-e.y)<1.4)damageUnit(u,24);burst(e.x,e.y,['#ff8a3a','#ffd27a','#3b2a2c'],16);puff(e.x,e.y,10);ring(e.x,e.y,1.4,'#ff6a2a')}}G.erupt=G.erupt.filter(e=>e.t>-.6)}
  updBuildings(dt);if(G.traps)""")
# ---------- sky, sea glints, weather ----------
rep("const g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#78afc0');g.addColorStop(1,'#649fb3');","const TT=THEMES[(G&&G.theme)||THEME]||THEMES.mountains,g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,G?TT.bg[0]:'#78afc0');g.addColorStop(1,G?TT.bg[1]:'#649fb3');")
rep("ctx.strokeStyle=`rgba(220,255,252,${(wv-.86)*3.4})`;","ctx.strokeStyle=`rgba(${TT.wave},${(wv-.86)*3.4})`;")
rep("  if(!reduceMotion)for(const m of motes){m.x=(m.x+Math.sin(time*.4+m.p)*.006*(.5+m.z)/60+1)%1;m.y=(m.y-.006*(.5+m.z)/60+1)%1;ctx.fillStyle=`rgba(255,247,214,${.3+m.z*.3})`;ctx.beginPath();ctx.arc(m.x*W,m.y*H,(1+m.z*2)*.8,0,TAU);ctx.fill()}",
r"""  drawWeather(TT);
  if(G.erupt)for(const e of G.erupt){const[px,py]=pj(e.x,e.y,hT(e.x,e.y));const k=1-Math.max(0,e.t)/e.max,Z=VW.Z;if(e.t>0){ctx.strokeStyle=`rgba(255,90,40,${.4+.4*Math.sin(time*12)})`;ctx.lineWidth=2*Z;ctx.beginPath();ctx.ellipse(px,py,1.4*45*Z,1.4*22.6*Z,0,0,TAU);ctx.stroke();
      const[vx,vy]=pj(VCEN.x,VCEN.y,hT(VCEN.x,VCEN.y)+3),bx=vx+(px-vx)*k,by=vy+(py-vy)*k-Math.sin(Math.PI*k)*160*Z;glow(bx,by,14*Z,'#ff8a3a',.8);ctx.fillStyle='#ffd27a';ctx.beginPath();ctx.arc(bx,by,4*Z,0,TAU);ctx.fill()}}""")
rep("const vg=ctx.createRadialGradient(W/2,H/2,Math.min(W,H)*.35,W/2,H/2,Math.max(W,H)*.75);vg.addColorStop(0,'rgba(43,36,64,0)');vg.addColorStop(1,'rgba(43,36,64,.16)');",
    "const vg=ctx.createRadialGradient(W/2,H/2,Math.min(W,H)*.35,W/2,H/2,Math.max(W,H)*.75);vg.addColorStop(0,`rgba(${TT.vig},0)`);vg.addColorStop(1,`rgba(${TT.vig},${G&&G.theme==='moon'?.32:.2})`);")
rep("const motes=Array.from({length:30},()=>({x:Math.random(),y:Math.random(),z:Math.random(),p:Math.random()*6.28}));",r"""const motes=Array.from({length:70},()=>({x:Math.random(),y:Math.random(),z:Math.random(),p:Math.random()*6.28}));
function drawWeather(TT){if(reduceMotion)return;const md=G?TT.mote:'dust',f=1/60;
  for(let i=0;i<motes.length;i++){const m=motes[i];if(md!=='rain'&&md!=='snow'&&i>=40)break;
    if(md==='ember'){m.x=(m.x+Math.sin(time*.8+m.p)*.002+1)%1;m.y=(m.y-.004*(.5+m.z)+1)%1;const a=.4+.4*Math.sin(time*5+m.p);glow(m.x*W,m.y*H,(3+m.z*4),'#ff7a2a',a*.5);ctx.fillStyle=`rgba(255,${150+m.z*80|0},80,${a})`;ctx.beginPath();ctx.arc(m.x*W,m.y*H,.8+m.z*1.6,0,TAU);ctx.fill()}
    else if(md==='spore'){m.x=(m.x+Math.sin(time*.3+m.p)*.0012+1)%1;m.y=(m.y-.0012*(.5+m.z)+1)%1;const a=.35+.35*Math.sin(time*2+m.p),c=i%3?'150,255,230':'220,170,255';glow(m.x*W,m.y*H,5+m.z*6,i%3?'#8fffe6':'#d9a6ff',a*.6);ctx.fillStyle=`rgba(${c},${a+.2})`;ctx.beginPath();ctx.arc(m.x*W,m.y*H,1+m.z*1.4,0,TAU);ctx.fill()}
    else if(md==='star'){const a=.25+.6*Math.abs(Math.sin(time*(.6+m.z)+m.p));ctx.fillStyle=`rgba(235,240,255,${a})`;const r=.6+m.z*1.3;ctx.fillRect(m.x*W-r/2,m.y*H*.5-r/2,r,r);if(m.z>.85){ctx.strokeStyle=`rgba(235,240,255,${a*.5})`;ctx.lineWidth=.6;line(m.x*W-4,m.y*H*.5,m.x*W+4,m.y*H*.5);line(m.x*W,m.y*H*.5-4,m.x*W,m.y*H*.5+4)}
      if(i<12){m.y2=((m.y2||m.y)-.0006+1)%1;ctx.fillStyle='rgba(200,198,220,.25)';ctx.beginPath();ctx.arc(((m.x+.37)%1)*W,(.5+m.y2*.5)*H,1.4,0,TAU);ctx.fill()}}
    else if(md==='rain'){m.y=(m.y+.02*(.6+m.z))%1;m.x=(m.x+.004+1)%1;ctx.strokeStyle=`rgba(210,240,230,${.18+m.z*.25})`;ctx.lineWidth=1;line(m.x*W,m.y*H,m.x*W-4,m.y*H+12+m.z*8)}
    else if(md==='snow'){m.y=(m.y+.0025*(.5+m.z))%1;m.x=(m.x+Math.sin(time*.7+m.p)*.0015+1)%1;ctx.fillStyle=`rgba(255,255,255,${.45+m.z*.45})`;ctx.beginPath();ctx.arc(m.x*W,m.y*H,1+m.z*2.2,0,TAU);ctx.fill()}
    else{m.x=(m.x+Math.sin(time*.4+m.p)*.006*(.5+m.z)/60+1)%1;m.y=(m.y-.006*(.5+m.z)/60+1)%1;ctx.fillStyle=`rgba(255,247,214,${.3+m.z*.3})`;ctx.beginPath();ctx.arc(m.x*W,m.y*H,(1+m.z*2)*.8,0,TAU);ctx.fill()}}
  if(G&&md==='rain'){ctx.fillStyle=`rgba(200,235,220,${.06+.03*Math.sin(time*.5)})`;ctx.fillRect(0,0,W,H)}}""")
# ---------- new trees, rocks and obstacles ----------
rep("      else if(bi.tree==='cactus'){",r"""      else if(bi.tree==='charred'){ctx.strokeStyle='#2b2224';ctx.lineCap='round';ctx.lineWidth=2.8*ss;const Hh=(18+r1*10)*ss;ctx.beginPath();ctx.moveTo(tx,ty);ctx.quadraticCurveTo(tx+2*ss,ty-Hh*.5,tx-1*ss,ty-Hh);ctx.stroke();ctx.lineWidth=1.4*ss;
        for(const[a,b,c,d]of[[0,-.55,-7,-.75],[0,-.65,6,-.9],[-1,-.9,-5,-1.1],[0,-.8,3,-1.12]])line(tx+a*ss,ty+b*Hh,tx+c*ss,ty+d*Hh);if(q>.55){const e=.5+.5*Math.sin(time*4+hs);glow(tx-6*ss,ty-.78*Hh,5*ss,'#ff7a2a',.5*e);ctx.fillStyle='#ffb36b';ctx.beginPath();ctx.arc(tx-6*ss,ty-.78*Hh,1*ss,0,TAU);ctx.fill()}}
      else if(bi.tree==='jungle'){const Hh=(30+r1*12)*ss;ctx.fillStyle='#5a4030';ctx.beginPath();ctx.moveTo(tx-4*ss,ty);ctx.lineTo(tx-1.6*ss,ty-Hh*.7);ctx.lineTo(tx+1.6*ss,ty-Hh*.7);ctx.lineTo(tx+4*ss,ty);ctx.fill();
        for(const[a,b,r,c]of[[-7,-.72,9,'#2f6e34'],[7,-.75,9,'#2f6e34'],[0,-.9,11,'#3d8240'],[-4,-1.02,7,'#4f9a4a'],[5,-1,6,'#5aa852']]){ctx.fillStyle=c;ctx.beginPath();ctx.ellipse(tx+a*ss,ty+b*Hh,r*ss,r*.62*ss,0,0,TAU);ctx.fill()}
        ctx.strokeStyle='#3f7a3a';ctx.lineWidth=1*ss;for(const a of[-8,-2,6]){ctx.beginPath();ctx.moveTo(tx+a*ss,ty-.72*Hh);ctx.quadraticCurveTo(tx+(a+2)*ss,ty-.45*Hh,tx+a*ss,ty-.3*Hh);ctx.stroke()}if(q>.6){ctx.fillStyle='#ff5a6a';ctx.beginPath();ctx.arc(tx+4*ss,ty-.62*Hh,1.6*ss,0,TAU);ctx.fill()}}
      else if(bi.tree==='moonbloom'){for(const[a,h,c]of[[-3,22,'#c9c4ef'],[3,16,'#b0aade'],[0,28,'#e2deff']]){const H2=(h+r1*6)*ss,bx=tx+a*ss;ctx.fillStyle=c;ctx.beginPath();ctx.moveTo(bx-1.8*ss,ty);ctx.lineTo(bx,ty-H2);ctx.lineTo(bx+1.8*ss,ty);ctx.fill();glow(bx,ty-H2,6*ss,'#c8d4ff',.5+.2*Math.sin(time*2+hs+a));ctx.fillStyle='#f4f6ff';ctx.beginPath();ctx.arc(bx,ty-H2,1.6*ss,0,TAU);ctx.fill()}}
      else if(bi.tree==='cactus'){""")
rep("    else if(bi.rockS==='moss'){","    else if(bi.rockS==='moon'){ctx.fillStyle='rgba(80,78,100,.35)';for(const[a,b,r]of[[-.3,-.1,.16],[.2,.05,.12],[-.05,.22,.1]]){ctx.beginPath();ctx.ellipse(cx+a*bw,cy+b*bh,r*bw,r*bh*.7,0,0,TAU);ctx.fill()}}\n    else if(bi.rockS==='moss'){")
rep("  }else if(k==='peak'){",r"""  }else if(k==='lava'){const w=hw*.95,h=hh*.95,gl=.75+.25*Math.sin(time*2+hs*.1);
    ctx.fillStyle='#2a1c1e';poly([sx-w,sy,sx,sy-h,sx+w,sy,sx,sy+h]);glow(sx,sy,w*1.1,'#ff5a1a',.45*gl);
    ctx.fillStyle=`rgb(255,${110+60*gl|0},40)`;poly([sx-w*.72,sy,sx,sy-h*.72,sx+w*.72,sy,sx,sy+h*.72]);ctx.fillStyle='#ffe08a';poly([sx-w*.3,sy,sx,sy-h*.3,sx+w*.3,sy,sx,sy+h*.3]);
    ctx.fillStyle='rgba(60,30,26,.85)';for(const[a,b,r]of[[-.4,-.1,.14],[.35,.12,.12],[.05,-.42,.1]]){ctx.beginPath();ctx.ellipse(sx+a*w,sy+b*h,r*w,r*h,0,0,TAU);ctx.fill()}
    if(Math.random()<.02)G&&G.fx&&G.fx.push({x:(x||0)+.5,y:(y||0)+.5,z:1,vx:(Math.random()-.5)*.4,vy:(Math.random()-.5)*.4,vz:1.2,g:1.5,life:0,max:.8,c:'#ffb04a',r:1.6})
  }else if(k==='cinder'){for(const[ox,oy,r]of[[-7,2,6],[6,3,5],[0,-3,4.5]]){ctx.fillStyle='#2a2326';ctx.beginPath();ctx.ellipse(sx+ox*s,sy+oy*s-r*.4*s,r*s,r*.7*s,0,0,TAU);ctx.fill();ctx.fillStyle='#4a3a3c';ctx.beginPath();ctx.ellipse(sx+ox*s-r*.3*s,sy+oy*s-r*.7*s,r*.5*s,r*.3*s,0,0,TAU);ctx.fill()}
    if(!reduceMotion){const q=(time*.5+hs/255)%1;ctx.fillStyle=`rgba(90,80,84,${(1-q)*.4})`;ctx.beginPath();ctx.arc(sx+Math.sin(q*5)*4*s,sy-8*s-q*30*s,(3+q*6)*s,0,TAU);ctx.fill()}
  }else if(k==='volcano'){const R0=3.3*45.25*s,H0=150*s,top=sy-H0,tw=R0*.22;
    ctx.fillStyle='rgba(30,16,16,.3)';ctx.beginPath();ctx.ellipse(sx,sy+8*s,R0*1.05,R0*.52,0,0,TAU);ctx.fill();
    ctx.fillStyle='#3a2e30';ctx.beginPath();ctx.moveTo(sx-R0,sy);ctx.quadraticCurveTo(sx-R0*.45,sy-H0*.35,sx-tw,top);ctx.lineTo(sx,top+8*s);ctx.lineTo(sx,sy+R0*.45);ctx.closePath();ctx.fill();
    ctx.fillStyle='#262022';ctx.beginPath();ctx.moveTo(sx,sy+R0*.45);ctx.lineTo(sx,top+8*s);ctx.lineTo(sx+tw,top);ctx.quadraticCurveTo(sx+R0*.45,sy-H0*.35,sx+R0,sy);ctx.closePath();ctx.fill();
    const gl=.7+.3*Math.sin(time*1.7);ctx.strokeStyle=`rgba(255,${120+60*gl|0},50,.9)`;ctx.lineCap='round';for(const[a,w0]of[[-.5,3.2],[.15,2.6],[.55,2.2],[-.15,1.8]]){ctx.lineWidth=w0*s;ctx.beginPath();ctx.moveTo(sx+a*tw*1.6,top+6*s);ctx.quadraticCurveTo(sx+a*R0*.5,sy-H0*.4,sx+a*R0*.85,sy-4*s);ctx.stroke()}
    glow(sx,top,tw*3.2,'#ff6a1a',.6*gl);ctx.fillStyle='#ff9a3a';ctx.beginPath();ctx.ellipse(sx,top+2*s,tw,tw*.38,0,0,TAU);ctx.fill();ctx.fillStyle='#ffe08a';ctx.beginPath();ctx.ellipse(sx,top+2*s,tw*.55,tw*.2,0,0,TAU);ctx.fill();
    if(!reduceMotion)for(let k2=0;k2<6;k2++){const q=(time*.18+k2/6)%1;ctx.fillStyle=`rgba(${70+q*40|0},${62+q*40|0},${66+q*40|0},${(1-q)*.55})`;ctx.beginPath();ctx.arc(sx+Math.sin(q*3+k2)*14*s+q*30*s,top-10*s-q*140*s,(10+q*26)*s,0,TAU);ctx.fill()}
  }else if(k==='gshroom'){const pal=[['#d06aa8','#a84886'],['#7fd8e6','#4aa8bf'],['#b48cff','#8a62d8']][hs%3],Hh=(26+r1*14)*s,cw=(15+r2*6)*s;
    ctx.fillStyle='rgba(40,20,60,.2)';ctx.beginPath();ctx.ellipse(sx+2*s,sy+2*s,cw*1.1,cw*.45,0,0,TAU);ctx.fill();
    ctx.fillStyle='#f0e6d6';ctx.beginPath();ctx.moveTo(sx-4*s,sy);ctx.quadraticCurveTo(sx-3*s,sy-Hh*.6,sx-3.5*s,sy-Hh);ctx.lineTo(sx+3.5*s,sy-Hh);ctx.quadraticCurveTo(sx+3*s,sy-Hh*.6,sx+4*s,sy);ctx.fill();
    glow(sx,sy-Hh,cw*2,pal[0][0],.35+.15*Math.sin(time*1.5+hs));ctx.fillStyle=pal[0][1];ctx.beginPath();ctx.ellipse(sx,sy-Hh+2*s,cw,cw*.5,0,0,Math.PI);ctx.fill();ctx.fillStyle=pal[0][0];ctx.beginPath();ctx.ellipse(sx,sy-Hh,cw,cw*.62,0,Math.PI,0);ctx.quadraticCurveTo(sx,sy-Hh+cw*.3,sx-cw,sy-Hh);ctx.fill();
    ctx.fillStyle='rgba(255,255,255,.8)';for(const[a,b,r]of[[-.45,-.3,.13],[.25,-.45,.1],[.55,-.15,.08],[-.1,-.5,.07]]){ctx.beginPath();ctx.arc(sx+a*cw,sy-Hh+b*cw,r*cw,0,TAU);ctx.fill()}
  }else if(k==='craterrim'){for(const[ox,oy,r]of[[-6,1,6],[5,2,5.4],[0,-3,4.6]]){const bx=sx+ox*s,by=sy+oy*s;ctx.fillStyle='#9a98aa';ctx.beginPath();ctx.ellipse(bx,by-r*.5*s,r*s,r*.75*s,0,0,TAU);ctx.fill();ctx.fillStyle='#c8c6d6';ctx.beginPath();ctx.ellipse(bx-r*.25*s,by-r*.8*s,r*.55*s,r*.38*s,0,0,TAU);ctx.fill();ctx.fillStyle='rgba(70,68,90,.35)';ctx.beginPath();ctx.arc(bx+r*.3*s,by-r*.45*s,r*.2*s,0,TAU);ctx.fill()}
  }else if(k==='thicket'){for(const[ox,oy,sc2]of[[-8,2,1],[7,3,.9],[0,-4,1.15],[-2,6,.8]]){const tx=sx+ox*s,ty=sy+oy*s,ss=s*sc2,Hh=(34+r1*10)*ss;ctx.fillStyle='#4a3424';ctx.fillRect(tx-2*ss,ty-Hh*.6,4*ss,Hh*.6);
      for(const[a,b,r,c]of[[-6,-.62,9,'#1f5428'],[6,-.66,9,'#1f5428'],[0,-.82,11,'#2a6a30'],[-3,-.95,7,'#3a7e3c']]){ctx.fillStyle=c;ctx.beginPath();ctx.ellipse(tx+a*ss,ty+b*Hh,r*ss,r*.6*ss,0,0,TAU);ctx.fill()}}
    ctx.strokeStyle='#2f6a30';ctx.lineWidth=1.2*s;for(const a of[-10,-3,4,10]){ctx.beginPath();ctx.moveTo(sx+a*s,sy-24*s);ctx.quadraticCurveTo(sx+(a+3)*s,sy-12*s,sx+a*s,sy-2*s);ctx.stroke()}
  }else if(k==='peak'){""")
# ---------- start screen: pick one of the five worlds ----------
rep('<div class="np" id="mpick">Map <button data-m="random" class="on">Random</button><button data-m="continent">Highlands</button><button data-m="straits">Straits</button><button data-m="isles">Isles</button></div>',
    '<div class="np" id="mpick" style="flex-wrap:wrap;row-gap:6px">World <button data-m="random" class="on">Random</button><button data-m="volcano">Volcano</button><button data-m="mushroom">Mushroom</button><button data-m="moon">Moon</button><button data-m="jungle">Jungle</button><button data-m="mountains">Mountains</button></div>\n     <p class="report" id="mapinfo" style="margin-top:6px"></p>')
open(F,'w').write(s);print('themes ok',len(s))
s=open(F).read()
# faith ground blends into the world's own colors rather than replacing them
rep("let base=beachA[i]?hexRgb(nb.sand):shade(hexRgb(bi.grass),","let base=beachA[i]?hexRgb(nb.sand):shade(bi===nb?hexRgb(bi.grass):mixRgb(hexRgb(nb.grass),hexRgb(bi.grass),.5),")
# snowy high ground in the mountains, and taller peaks
rep("if(!beachA[i]&&CFLOOR[i])","if(!beachA[i]&&THEME==='mountains'&&elev[i]>.66)base=mixRgb(base,[244,248,252],clamp((elev[i]-.66)*6,0,.85));if(!beachA[i]&&CFLOOR[i])")
rep("  }else if(k==='peak'){const h0=(34+r1*20)*s,w=(hw*.9);","  }else if(k==='peak'){const tall=G&&G.theme==='mountains'?1.8:1,h0=(34+r1*20)*s*tall,w=(hw*.9)*(tall>1?1.15:1);")
open(F,'w').write(s);print('theme polish ok')
