F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a)
    assert c==n,(c,a[:100])
    s=s.replace(a,b)
def cut(start,end,new):
    """replace s[start_anchor .. end_anchor(inclusive)] with new"""
    global s
    i=s.find(start);assert i>=0,start[:80]
    j=s.find(end,i);assert j>=0,end[:80]
    s=s[:i]+new+s[j+len(end):]

# ================= research-gated Egyptian defenses (Obelisk, then Canopic Urns at tier 2) + Sand Traps =================
rep("function LIM(side,k){if(k==='tower'&&EGY(side)&&!hasT(side,'btower'))return 0;",
    "const NEEDR={tower:'btower',mortar:'bmortar',sandtrap:'sandtrap'},needR=(side,k)=>EGY(side)&&NEEDR[k]&&!hasT(side,NEEDR[k]);\nfunction LIM(side,k){if(needR(side,k))return 0;if(k==='sandtrap'&&EGY(side))return count(side,'sandtrap')+Math.max(0,12-count(side,'sandtrap')-(G.traps||[]).filter(t=>t.side===side).length);")
rep("if(T.bty&&(T.bty!=='tower'||S.god!==0))return{hide:true};","if((T.bty&&(T.bty==='cannon'||S.god!==0))||(k==='sandtrap'&&S.god!==0))return{hide:true};")
rep("&&!(TECH[k].bty&&(TECH[k].bty!=='tower'||g!==0)))","&&!(TECH[k].bty&&(TECH[k].bty==='cannon'||g!==0))&&!(k==='sandtrap'&&g!==0))")
rep("if(k==='btower'&&g===0)return`Unlocks the Obelisk,",
    "if(k==='bmortar'&&g===0)return`Unlocks the Canopic Urns, Egypt\\u2019s short-range splash defense. ${BLESS[0].mortar.desc} Short range: hits everything in the blast.`;if(k==='btower'&&g===0)return`Unlocks the Obelisk,")
rep("LIMIT[k][S.tier-1]===0||(k==='tower'&&EGY(0)&&!hasT(0,'btower')),full","LIMIT[k][S.tier-1]===0||needR(0,k),full")
rep("${locked&&k==='tower'?'Needs research':","${locked&&needR(0,k)?'Needs research':")
rep("if(locked&&k==='tower'){toast('Research the Obelisk in Tech first.');return}","if(locked&&needR(0,k)){toast(`Research ${techName(NEEDR[k],0)} in Tech first.`);return}")
rep("  quarry:{br:'Sowers',name:'Quarrying',",
    "  sandtrap:{br:'Sowers',name:'Sand Traps',tier:1,req:'quarry',cost:{stone:10,wheat:8},time:25,desc:'Stonebearers learn to dig Sand Traps: hidden pits of loose sand. The first enemy to step in is held for 2\\u00bd seconds and hurt for 25, and the pit refills 10 seconds later. Build them from the Defend menu.'},\n  quarry:{br:'Sowers',name:'Quarrying',")
# no walls for Egypt; traps instead
rep("const EGX=new Set(['barracks','storehouse','camp','workshop','aerie'])","const EGX=new Set(['barracks','storehouse','camp','workshop','aerie','wall'])")
rep("const BGROUPS_E=[['Faith',['chapel','altar','veil']],['Army',['wabet']],['Water',['well']],['Defend',['tower','mortar','wall']]];",
    "const BGROUPS_E=[['Faith',['chapel','altar','veil']],['Army',['wabet','sphinxmon']],['Water',['well']],['Defend',['tower','mortar','sandtrap']]];")
rep("const LIMIT={well:[40,40,40,40,40],wabet:[0,2,2,2,2],","const LIMIT={well:[40,40,40,40,40],wabet:[0,2,2,2,2],sphinxmon:[0,1,1,1,1],sandtrap:[12,12,12,12,12],")
rep("const BTIME={well:15,wabet:40,","const BTIME={well:15,wabet:40,sphinxmon:60,sandtrap:6,")
rep("  wabet:{name:'Wabet',",
    "  sphinxmon:{name:'Sphinx Monument',hp:900,cost:{stone:160,wheat:30},egy:1,desc:'A great sandstone sphinx crouched before a temple court. Trains Sphinxes. Needs the Great Pyramid.'},\n  sandtrap:{name:'Sand Trap',hp:40,cost:{stone:8},egy:1,desc:'A hidden pit of loose sand. The first enemy to step on it sinks in: held for 2\\u00bd seconds and hurt for 25. It refills 10 seconds later. Enemies can\\u2019t see it, and troops walk over it.'},\n  wabet:{name:'Wabet',")
# the trap becomes a ground hazard as soon as it is dug
rep("if(!built(b)){const ia=","if(b.type==='sandtrap'&&built(b)){(G.traps||(G.traps=[])).push({x:b.x+.5,y:b.y+.5,side:b.side,cd:0,fx:0});removeBuilding(b);continue}\n     if(!built(b)){const ia=")
rep("  updBuildings(dt);if(!G.arena)updResearch(dt);","  updBuildings(dt);if(G.traps)for(const tp of G.traps){if(tp.cd>0)tp.cd-=dt;if(tp.fx>0)tp.fx-=dt}if(!G.arena)updResearch(dt);")
rep("  if(G.brambles.length)for(const b of G.brambles)",
    "  if(G.traps&&G.traps.length&&!U[u.type].air&&!u.leap)for(const tp of G.traps)if(tp.side!==u.side&&tp.cd<=0&&Math.abs(tp.x-u.x)<.55&&Math.abs(tp.y-u.y)<.55){tp.cd=10;tp.fx=1.2;u.root=Math.max(u.root||0,2.5);u.slow=Math.max(u.slow||0,3);damageUnit(u,25);puff(tp.x,tp.y,8);burst(tp.x,tp.y,['#e8cf9a','#c9a274','#f3e3bb'],12);float(u.x,u.y,'Sand trap!','#b98c56');if(u.hp<=0)return;break}\n  if(G.brambles.length)for(const b of G.brambles)")
# draw traps on the ground (owner sees them; enemies only when sprung)
rep("  for(const pl of G.pools){if(!seeAt(pl.x,pl.y))continue;",
r"""  if(G.traps)for(const tp of G.traps){if(tp.side!==0&&!(tp.cd>0))continue;if(!seeAt(tp.x,tp.y)&&tp.side!==0)continue;const[px,py]=pj(tp.x,tp.y,hT(tp.x,tp.y));if(!onScreen(px,py))continue;drawTrap(px,py,Z,tp)}
  for(const pl of G.pools){if(!seeAt(pl.x,pl.y))continue;""")
rep("function drawWell(sx,sy,s,b){",
r"""function drawTrap(sx,sy,s,tp){const sprung=tp&&tp.cd>0;ctx.save();ctx.globalAlpha=tp&&tp.side===0&&!sprung?.85:1;
  ctx.fillStyle=sprung?'#9c7448':'#b98c56';ctx.beginPath();ctx.ellipse(sx,sy,15*s,7.5*s,0,0,TAU);ctx.fill();
  ctx.fillStyle=sprung?'#6e4f30':'#d9b27a';ctx.beginPath();ctx.ellipse(sx,sy+.6*s,11*s,5.4*s,0,0,TAU);ctx.fill();
  ctx.strokeStyle=sprung?'rgba(60,40,20,.55)':'rgba(120,84,44,.5)';ctx.lineWidth=1*s;const r0=(typeof time!=='undefined'?time:0)*(sprung?3:.6);
  for(let k=0;k<3;k++){ctx.beginPath();ctx.ellipse(sx,sy+.6*s,(3+k*2.6)*s,(1.5+k*1.3)*s,0,r0+k,r0+k+3.6);ctx.stroke()}
  if(tp&&tp.fx>0){ctx.fillStyle=`rgba(232,207,154,${tp.fx/1.2})`;ctx.beginPath();ctx.ellipse(sx,sy-6*s*(1.2-tp.fx),18*s,9*s,0,0,TAU);ctx.fill()}
  ctx.restore()}
function drawSphinxMon(sx,sy,s,gc,b){blobShadow(sx,sy,s,34);const P=(u,v,z)=>[sx+(u-v)*32*s,sy+(u+v)*16*s-z*s],SC=['#f2d6a2','#dcb57c','#b98c56'];
  ibox(sx,sy,s,.46,.4,0,5,'#efe2c2','#dcc79c','#c3a979');
  {const a=P(-.46,.4,5),c=P(.46,.4,5);ctx.strokeStyle='#d9a93a';ctx.lineWidth=1.4*s;line(a[0],a[1],c[0],c[1])}
  {const p=P(-.24,-.2,5);ibox(p[0],p[1],s,.12,.12,0,26,'#efe2c2','#dcc79c','#c3a979');const q=P(-.24,-.2,31);pyramid(q[0],q[1],7*s,9*s,'#ffe28a','#d7a22c');glow(q[0],q[1]-4*s,10*s,'#ffd86a',.45)}
  {const p=P(-.1,0,5);ibox(p[0],p[1],s,.26,.13,0,12,...SC);const h=P(-.32,0,5);ctx.fillStyle=SC[1];ctx.beginPath();ctx.ellipse(h[0],h[1]-9*s,9*s,9.5*s,0,Math.PI*.9,Math.PI*2.1);ctx.fill()}
  for(const v of[-.08,.08]){const p=P(.25,v,5);ibox(p[0],p[1],s,.12,.04,0,4,...SC);const t=P(.37,v,7);ctx.fillStyle='#a87f4d';for(let k=0;k<3;k++)ctx.fillRect(t[0]-2*s+k*1.6*s,t[1]-1*s,1*s,2*s)}
  {const p=P(.12,0,17);ibox(p[0],p[1],s,.08,.1,0,10,...SC);
   const hd=P(.13,0,31),w=11*s,hh=16*s;ctx.fillStyle='#2f5e9e';ctx.beginPath();ctx.moveTo(hd[0]-w,hd[1]+hh*.6);ctx.lineTo(hd[0]-w*.55,hd[1]-hh*.5);ctx.quadraticCurveTo(hd[0],hd[1]-hh*.85,hd[0]+w*.55,hd[1]-hh*.5);ctx.lineTo(hd[0]+w,hd[1]+hh*.6);ctx.closePath();ctx.fill();
   ctx.strokeStyle='#e8c35a';ctx.lineWidth=1.3*s;for(let k=-3;k<=3;k++){if(!k)continue;ctx.beginPath();ctx.moveTo(hd[0]+k*w*.13,hd[1]-hh*.55);ctx.lineTo(hd[0]+k*w*.27,hd[1]+hh*.58);ctx.stroke()}
   ctx.fillStyle='#e9c98f';ctx.beginPath();ctx.ellipse(hd[0],hd[1]-1*s,5.4*s,7*s,0,0,TAU);ctx.fill();ctx.fillStyle='#e8c35a';ctx.fillRect(hd[0]-6*s,hd[1]-8.5*s,12*s,2*s);
   ctx.fillStyle='#2b2440';for(const d of[-2,2]){ctx.beginPath();ctx.ellipse(hd[0]+d*s,hd[1]-2*s,1.1*s,.7*s,0,0,TAU);ctx.fill()}ctx.fillStyle='#b98c56';ctx.fillRect(hd[0]-.5*s,hd[1]+5.5*s,1*s,3*s);
   const u=P(.13,0,47);glow(u[0],u[1],12*s,gc,.5);ctx.fillStyle='#ffe28a';ctx.beginPath();ctx.arc(u[0],u[1],3*s,0,TAU);ctx.fill()}
}
function drawWell(sx,sy,s,b){""")
rep("    case 'wabet':{drawWabet(sx,sy,s,GODS[0].col,b);break}",
    "    case 'wabet':{drawWabet(sx,sy,s,GODS[0].col,b);break}\n    case 'sphinxmon':{drawSphinxMon(sx,sy,s,GODS[0].col,b);break}\n    case 'sandtrap':{drawTrap(sx,sy,s,null);break}")
# Sphinxes train at the Sphinx Monument
rep("U.g0_2.cost={wheat:30,water:12};U.g0_3.cost={wheat:50,water:20};",
    "U.g0_2.cost={wheat:30,water:12};U.g0_3.cost={wheat:50,water:20};U.g0_3.bld='sphinxmon';U.g0_3.lv=2;\nObject.assign(U.g0_1,{hp:170,dmg:10,special:'mega',desc:'Slow and easy to put down. Awakened, each Mummy that falls has a 1 in 10 chance to rise again as a Mega Mummy: twice the size, with far more health and a crushing blow.'});")
rep("b.type==='wabet'?gk('wabet'):[]","b.type==='wabet'?gk('wabet'):b.type==='sphinxmon'?gk('sphinxmon'):[]")
rep("{hall:FN(k,'hall'),wabet:'Wabet',","{hall:FN(k,'hall'),wabet:'Wabet',sphinxmon:'Sphinx Monument',")
# AI build plan: monument instead of the second Wabet, no walls for Egypt
rep("'veil','W8','tower','cannon','wabet','altar','mortar','TEMPLE','W8',","'veil','tower','sphinxmon','altar','mortar','TEMPLE',")
rep("(EGY(k)?['tower','cannon','mortar','well','W4','chapel','TEMPLE','altar','wabet','well']","(EGY(k)?['tower','mortar','well','sphinxmon','chapel','TEMPLE','altar','wabet','well']")
rep("for(const t of EGY(k)?['quarry','btower',...AITECH]:AITECH)","for(const t of EGY(k)?['quarry','btower','bmortar',...AITECH]:AITECH)")

# ================= Mega Mummy =================
rep("const isHoly=u=>U[u.type].champ!=null||!!U[u.type].gu;",
    "const isHoly=u=>U[u.type].champ!=null||!!U[u.type].gu;\nU.megamummy=Object.assign({},U.g0_1,{name:'Mega Mummy',role:'Undead melee',hp:650,dmg:32,rate:.9,range:1,spd:1.3,house:0,bld:'none',lv:9,special:null,fam:'g0_1',desc:'A Mummy that would not stay dead, risen twice its size.'});for(const f of['awaken','full','basic'])delete U.megamummy[f];")
rep("TYPES.champ0b=TYPES.champ0;","TYPES.champ0b=TYPES.champ0;TYPES.megamummy=Object.assign({},TYPES.g0_1,{ps:56,cap:210});")
rep("  if(U[u.type].special==='wrap'){if(src&&src.x!=null",
    "  if(U[u.type].special==='mega'&&u.hp<=0&&!u.megaT){u.megaT=1;if(R()<.1){u.type='megamummy';u.max=U.megamummy.hp*(1+.2*(u.rank||0));u.hp=u.max;u.down=1.6;u.root=1.6;u.slow=0;puff(u.x,u.y,10);burst(u.x,u.y,['#d9c9a0','#efe6d0','#7a5a36','#e8c35a'],18);ring(u.x,u.y,.9,'#e8c35a');float(u.x,u.y,'Mega Mummy!','#c9a23f');return}}\n  if(U[u.type].special==='wrap'){if(src&&src.x!=null")
rep("const SPNAME={","const SPNAME={mega:'Mega Mummy',")
rep("wrap:'Tangles \\u00b7 Rises once',","wrap:'Tangles \\u00b7 Rises once',mega:'1 in 10 rise as Mega Mummy',")

# ================= gold-capped Pyramid: brighter and ornate =================
rep("  ctx.fillStyle='#ecd5a2';poly([...L,...Fr,...tF,...tL]);ctx.fillStyle='#c7a873';poly([...Fr,...Rr,...tR,...tF]);",
    "  ctx.fillStyle=capd?'#fbeec8':'#ecd5a2';poly([...L,...Fr,...tF,...tL]);ctx.fillStyle=capd?'#e2c288':'#c7a873';poly([...Fr,...Rr,...tR,...tF]);")
rep("  if(capd){const t0=.8,ac=a*(1-t0),zc=z0+H*t0,ap=P(0,0,z0+H),",
r"""  if(capd){ctx.strokeStyle='#e9b93a';ctx.lineWidth=2.2*s;for(const t of[.18,.42,.64]){const aa=a*(1-t),z=z0+H*t,p1=P(-aa,aa,z),p2=P(aa,aa,z),p3=P(aa,-aa,z);ctx.beginPath();ctx.moveTo(p1[0],p1[1]);ctx.lineTo(p2[0],p2[1]);ctx.lineTo(p3[0],p3[1]);ctx.stroke()}
    {const tp=P(0,0,z0+H*.8);ctx.lineWidth=1.6*s;for(const q of[L,Fr,Rr]){ctx.beginPath();ctx.moveTo(q[0],q[1]);ctx.lineTo(q[0]+(tp[0]-q[0])*.97,q[1]+(tp[1]-q[1])*.97);ctx.stroke()}}
    {ctx.fillStyle='rgba(47,94,158,.75)';const t=.3,aa=a*(1-t),z=z0+H*t;for(let k=0;k<9;k++){const u=-aa*.8+k*aa*.2;if(Math.abs(u)<a*.2)continue;const p=P(u,aa,z+2*s/s);ctx.fillRect(p[0]-1.1*s,p[1]-5*s,2.2*s,3.2*s)}}
    {const sd=P(0,a*.93,z0+H*.24);glow(sd[0],sd[1],14*s*a,'#ffd86a',.7);ctx.fillStyle='#ffd24a';ctx.beginPath();ctx.arc(sd[0],sd[1],4.2*s*a,0,TAU);ctx.fill();ctx.fillStyle='#2f5e9e';for(const d of[-1,1]){ctx.beginPath();ctx.moveTo(sd[0]+d*4*s*a,sd[1]);ctx.quadraticCurveTo(sd[0]+d*11*s*a,sd[1]-4*s*a,sd[0]+d*15*s*a,sd[1]+1*s*a);ctx.quadraticCurveTo(sd[0]+d*9*s*a,sd[1]+1*s*a,sd[0]+d*4*s*a,sd[1]+2*s*a);ctx.fill()}}
    if(!reduceMotion){const ap=P(0,0,z0+H);ctx.save();ctx.globalCompositeOperation='lighter';for(let k=0;k<8;k++){const an=time*.25+k*Math.PI/4,r1=10*s*a,r2=(34+6*Math.sin(time*2+k))*s*a;ctx.strokeStyle=`rgba(255,220,120,${.18+.1*Math.sin(time*3+k)})`;ctx.lineWidth=2*s;ctx.beginPath();ctx.moveTo(ap[0]+Math.cos(an)*r1,ap[1]+Math.sin(an)*r1*.6);ctx.lineTo(ap[0]+Math.cos(an)*r2,ap[1]+Math.sin(an)*r2*.6);ctx.stroke()}ctx.restore()}
    const t0=.8,ac=a*(1-t0),zc=z0+H*t0,ap=P(0,0,z0+H),""")
rep("  else{ctx.fillStyle='#f4e4bd';poly([...tL,...tF,...tR,...tB]);const c=P(0,0,zt);ibox(c[0],c[1],s,at*.5,at*.5,0,5*a+2,'#efe2c2','#dcc79c','#c3a979');}\n}",
r"""  else{ctx.fillStyle='#f4e4bd';poly([...tL,...tF,...tR,...tB]);const c=P(0,0,zt);ibox(c[0],c[1],s,at*.5,at*.5,0,5*a+2,'#efe2c2','#dcc79c','#c3a979');}
  if(capd)for(const d of[-1,1]){const o=P(d*a*.55,a*1.16,0),w=3.2*s*a,h=30*s*a;ctx.fillStyle='#f7e3b0';ctx.beginPath();ctx.moveTo(o[0]-w,o[1]);ctx.lineTo(o[0]-w*.6,o[1]-h);ctx.lineTo(o[0],o[1]-h+1*s);ctx.lineTo(o[0],o[1]+w*.4);ctx.fill();ctx.fillStyle='#d9b77a';ctx.beginPath();ctx.moveTo(o[0],o[1]+w*.4);ctx.lineTo(o[0],o[1]-h+1*s);ctx.lineTo(o[0]+w*.6,o[1]-h);ctx.lineTo(o[0]+w,o[1]);ctx.fill();
    ctx.fillStyle='#ffd24a';ctx.beginPath();ctx.moveTo(o[0]-w*.6,o[1]-h);ctx.lineTo(o[0],o[1]-h-5*s*a);ctx.lineTo(o[0]+w*.6,o[1]-h);ctx.lineTo(o[0],o[1]-h+1*s);ctx.fill();glow(o[0],o[1]-h-2*s,6*s*a,'#ffd86a',.6)}
}""")

# ================= bottom bar: one chip per faith troop, scrolling sideways =================
rep("for(const k of[...CHIPS,'champ']){const b=document.createElement('button');","for(const k of CHIPS){const b=document.createElement('button');")
cut("{const el=$('cn-champ'),n=mine.filter(isHoly).length,","bt.replaceChild(unitIcon('champ'+S.god,42,40),bt.querySelector('canvas'));}}",
r"""{const C=$('chips'),fam=k=>U[k].fam||U[k].full||baseOf(k),hol=mine.filter(u=>isHoly(u)&&!u.leap),ks=[...new Set(hol.map(u=>fam(u.type)))];
    for(const k of ks)if(!$('cf-'+k)){const b=document.createElement('button');b.className='chip fx';b.id='cf-'+k;b.dataset.k=k;const nm=U[k].name;b.setAttribute('aria-label',nm);b.appendChild(unitIcon(k,42,50));b.insertAdjacentHTML('beforeend',`<b>${nm.length>11?nm.split(' ').slice(-1)[0]:nm}</b><span class="n">0</span>`);b.onclick=()=>chipTap(k);C.appendChild(b)}
    for(const b of C.querySelectorAll('.chip.fx')){const k=b.dataset.k,us=hol.filter(u=>fam(u.type)===k);b.querySelector('.n').textContent=us.length;b.classList.toggle('sel',us.some(u=>SEL.has(u)));b.classList.toggle('empty',!us.length)}}""")
rep("  const mine=G.units.filter(u=>u.side===0&&baseOf(u.type)===k&&!u.leap);\n  if(!mine.length){toast(G.S[0].tier<U[k].lv?",
    "  const fam=t=>U[t].fam||U[t].full||baseOf(t),mine=G.units.filter(u=>u.side===0&&(baseOf(u.type)===k||fam(u.type)===k)&&!u.leap);\n  if(!mine.length){toast(G.S[0].tier<U[k].lv?")

# ================= chosen special attacks, each with a cooldown =================
rep("if(u.skyCd>0)return false;const[f]=nearestFoeUnit(u,4.5);","if(u.skyCd>0)return false;if(u.side===0&&!(u.cast>G.t))return false;const[f]=nearestFoeUnit(u,4.5);")
rep("u.skyT=2.1;u.skyHit=0;u.skyCd=12;","u.skyT=2.1;u.skyHit=0;u.skyCd=12;u.cast=0;")
rep("u.psT=(u.psT==null?3:u.psT)-dt;if(u.psT>0)return false;","u.psT=(u.psT==null?3:u.psT)-dt;if(u.psT>0)return false;if(u.side===0&&!(u.cast>G.t))return false;")
rep("u.psT=12;u.pwT=3.0;","u.psT=12;u.pwT=3.0;u.cast=0;")
rep("u.tsT=(u.tsT==null?2.5:u.tsT)-dt;if(u.tsT>0)return false;","u.tsT=(u.tsT==null?2.5:u.tsT)-dt;if(u.tsT>0)return false;if(u.side===0&&!(u.cast>G.t))return false;")
rep("u.tsT=7;u.thT=1.45;","u.tsT=7;u.thT=1.45;u.cast=0;")
cut("if(sp==='ritual'){if(u.kneel>0)return true;","u.kneel=3.5;",
    "if(sp==='ritual'){if(u.kneel>0)return true;u.ritCd=(u.ritCd==null?4:u.ritCd)-dt;if(u.ritCd>0)return false;if(u.side===0){if(!(u.cast>G.t))return false}else{const sw0=u.sw||0;if(sw0>.9&&!u.ritSw){u.ritSw=1;if(R()>=.1)return false}else{if(sw0<.5)u.ritSw=0;return false}}u.ritCd=20;u.cast=0;u.kneel=3.5;")
rep("function chipTap(k){",
r"""const MANSP={skyfall:{cd:u=>u.skyCd==null?5:u.skyCd,max:12,col:'#e8c35a',ic:'↓'},ritual:{nm:'Heal Ritual',cd:u=>u.ritCd==null?4:u.ritCd,max:20,col:'#7fd87a',ic:'✚'},powershot:{cd:u=>u.psT==null?3:u.psT,max:12,col:'#4fd84a',ic:'◎'},thornslam:{cd:u=>u.tsT==null?2.5:u.tsT,max:7,col:'#8fbf5a',ic:'❂'}};
let SPXK='';
function updSpx(){let el=document.getElementById('spx');if(!el){el=document.createElement('div');el.id='spx';document.body.appendChild(el);
    const st=document.createElement('style');st.textContent='#spx{position:fixed;left:max(12px,env(safe-area-inset-left,0px));bottom:calc(env(safe-area-inset-bottom,0px) + 190px);display:flex;flex-direction:column;gap:10px;z-index:7;pointer-events:none}#spx button{pointer-events:auto;position:relative;width:62px;height:62px;border-radius:50%;border:0;padding:0;background:rgba(43,36,64,.88);box-shadow:0 4px 14px rgba(0,0,0,.25);color:#fff;font:700 9.5px var(--body,system-ui);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1px}#spx button i{font-style:normal;font-size:20px;line-height:1}#spx button .ring{position:absolute;inset:0;border-radius:50%;pointer-events:none}#spx button .ring::after{content:"";position:absolute;inset:5px;border-radius:50%;background:rgba(43,36,64,.92)}#spx button>i,#spx button>span{position:relative;z-index:1}#spx button .c{position:absolute;top:-4px;right:-4px;z-index:2;background:#fff;color:#2b2440;border-radius:9px;min-width:18px;height:18px;font-size:11px;line-height:18px}#spx button.ready{box-shadow:0 0 0 2px rgba(255,255,255,.9),0 0 16px var(--gl)}';document.head.appendChild(st)}
  const sel=G&&!G.arena?[...SEL].filter(u=>u.side===0&&u.hp>0&&MANSP[U[u.type].special]):[];const ks=[...new Set(sel.map(u=>U[u.type].special))];const key=ks.join(',');
  if(key!==SPXK){SPXK=key;el.innerHTML='';for(const k of ks){const b=document.createElement('button');b.dataset.k=k;b.style.setProperty('--gl',MANSP[k].col);b.innerHTML=`<div class="ring"></div><i>${MANSP[k].ic}</i><span>${MANSP[k].nm||SPNAME[k]||k}</span><b class="c"></b>`;b.onclick=e=>{e.stopPropagation();castSp(k)};el.appendChild(b)}}
  for(const b of el.children){const k=b.dataset.k,M=MANSP[k],us=sel.filter(u=>U[u.type].special===k),rd=us.filter(u=>M.cd(u)<=0),pend=us.some(u=>u.cast>G.t);const mn=Math.min(...us.map(u=>Math.max(0,M.cd(u)))),f=rd.length?1:1-mn/M.max;
    b.querySelector('.ring').style.background=`conic-gradient(${M.col} ${f*360}deg, rgba(255,255,255,.18) 0)`;b.classList.toggle('ready',rd.length>0&&!pend);b.querySelector('.c').textContent=rd.length?rd.length:Math.ceil(mn)+'s';b.style.opacity=rd.length||pend?1:.75}}
function castSp(k){const M=MANSP[k],us=[...SEL].filter(u=>u.side===0&&u.hp>0&&U[u.type].special===k),rd=us.filter(u=>M.cd(u)<=0);if(!rd.length){toast(`${M.nm||SPNAME[k]||k} is recharging.`);return}for(const u of rd)u.cast=G.t+6;float(rd[0].x,rd[0].y,M.nm||SPNAME[k]||k,M.col)}
function chipTap(k){""")
rep("hudT-=dt;if(hudT<=0){hudT=.2;renderHUD(false)}","hudT-=dt;if(hudT<=0){hudT=.2;renderHUD(false)}updSpx();")
open(F,'w').write(s);print('egypt2 ok',len(s))
s=open(F).read()
rep("SEL:()=>SEL,","SEL:()=>SEL,damageUnit:(u,d)=>damageUnit(u,d),")
open(F,'w').write(s)
s=open(F).read()
# ---------- Skyfall: flies to its target (troop or building), hits buildings too, waits for a target instead of fizzling ----------
cut("if(sp==='skyfall'){u.skyCd=(u.skyCd==null?5:u.skyCd)-dt;","u.skyX=f.x;u.skyY=f.y;face(u,f.x,f.y);return true}",
r"""if(sp==='skyfall'){u.skyCd=(u.skyCd==null?5:u.skyCd)-dt;if(u.skyT>0){u.skyT-=dt;const t=U[u.type];u.path=[];u.moving=false;
      const v=u.skyTg;if(v&&v.hp>0&&!u.skyHit){const bx=v.type&&B[v.type]&&v.s!=null?bcx(v):v.x,by=v.type&&B[v.type]&&v.s!=null?bcy(v):v.y;u.skyX=bx;u.skyY=by}
      if(u.skyS&&!u.skyHit){const k=clamp((2.1-.2-u.skyT)/(1.32-.2),0,1),e=k*k*(3-2*k),dx=u.skyX-u.skyS[0],dy=u.skyY-u.skyS[1],dl=Math.hypot(dx,dy)||1,stop=Math.max(0,dl-.7),lx=u.skyS[0]+dx/dl*stop*e,ly=u.skyS[1]+dy/dl*stop*e;if(landAt(lx,ly)){u.x=lx;u.y=ly;u.ax=lx;u.ay=ly}face(u,u.skyX,u.skyY)}
      if(!u.skyHit&&u.skyT<=2.1-1.32){u.skyHit=1;splashAt(u.skyX,u.skyY,1.3,t.dmg*1.8,u.side,false,true,true,u);ring(u.skyX,u.skyY,1.3,'#ffd27a');ring(u.skyX,u.skyY,1,'#fff2c8');puff(u.skyX,u.skyY,14);float(u.x,u.y,'Skyfall!','#e8bf55')}return true}
    if(u.skyCd>0)return false;if(u.side===0&&!(u.cast>G.t))return false;let[f]=nearestFoeUnit(u,6.5);if(f&&U[f.type].air)f=null;
    if(!f){let bd=6.5;for(const b of G.B){if(b.side===u.side||b.hp<=0||b.side==null||b.side<0)continue;const d=Math.hypot(bcx(b)-u.x,bcy(b)-u.y);if(d<bd){bd=d;f=b}}}
    if(!f){u.skyCd=.4;return false}const fx=f.s!=null&&B[f.type]?bcx(f):f.x,fy=f.s!=null&&B[f.type]?bcy(f):f.y;
    u.skyT=2.1;u.skyHit=0;u.skyCd=12;u.cast=0;u.skyTg=f;u.skyX=fx;u.skyY=fy;u.skyS=[u.x,u.y];face(u,fx,fy);return true}""")
# feedback only when it really goes, and the order waits up to 15s for something in reach
rep("for(const u of rd)u.cast=G.t+6;float(rd[0].x,rd[0].y,M.nm||SPNAME[k]||k,M.col)","for(const u of rd){u.cast=G.t+15;ring(u.x,u.y,.6,M.col)}")
open(F,'w').write(s);print('skyfall fix ok')
s=open(F).read()
# ---------- Skyfall is aimed: tap the button, then tap where to land (no enemy needed) ----------
rep("if(u.skyCd>0)return false;if(u.side===0&&!(u.cast>G.t))return false;let[f]=nearestFoeUnit(u,6.5);",
    "if(u.skyCd>0)return false;if(u.side===0&&!(u.cast>G.t))return false;if(u.side===0&&u.castXY){const[px,py]=u.castXY;u.castXY=null;let f=null,bd=1.3;for(const v of G.units)if(foeOf(u,v)&&!U[v.type].air){const d=Math.hypot(v.x-px,v.y-py);if(d<bd){bd=d;f=v}}u.skyT=2.1;u.skyHit=0;u.skyCd=12;u.cast=0;u.skyTg=f;u.skyPt=!f;u.skyX=f?f.x:px;u.skyY=f?f.y:py;u.skyS=[u.x,u.y];face(u,u.skyX,u.skyY);return true}u.skyPt=false;let[f]=nearestFoeUnit(u,6.5);")
rep("stop=Math.max(0,dl-.7)","stop=Math.max(0,dl-(u.skyPt?0:.7))")
rep("function castSp(k){const M=MANSP[k],",
r"""let SPAIM=null;
function aimSp(k,x,y){const M=MANSP[k],rd=[...SEL].filter(u=>u.side===0&&u.hp>0&&U[u.type].special===k&&M.cd(u)<=0);if(!rd.length)return;let n=0;
  for(const u of rd){let tx=x,ty=y;const d=Math.hypot(tx-u.x,ty-u.y),R=8;if(d>R){tx=u.x+(tx-u.x)/d*R;ty=u.y+(ty-u.y)/d*R}if(!landAt(tx,ty)){continue}u.castXY=[tx,ty];u.cast=G.t+3;n++;ring(tx,ty,1.3,M.col)}
  if(!n)toast('The Sphinx can’t land there.');renderHUD(true)}
function castSp(k){if(k==='skyfall'){const M=MANSP[k],rd=[...SEL].filter(u=>u.side===0&&u.hp>0&&U[u.type].special===k&&M.cd(u)<=0);if(!rd.length){toast('Skyfall is recharging.');return}if(SPAIM==='skyfall'){SPAIM=null;toast('Skyfall cancelled.');return}SPAIM='skyfall';toast('Tap where the Sphinx should land.');return}
  const M=MANSP[k],""")
rep("  setView();const g=toGrid(sx,sy);\n  if(buildMode){","  setView();const g=toGrid(sx,sy);\n  if(SPAIM){const k=SPAIM;SPAIM=null;aimSp(k,g.x,g.y);return}\n  if(buildMode){")
rep("b.classList.toggle('ready',rd.length>0&&!pend);","b.classList.toggle('ready',rd.length>0&&!pend);b.style.outline=SPAIM===k?'3px solid #fff':'';")
open(F,'w').write(s);print('skyfall aim ok')
s=open(F).read()
# ---------- Scarab Ark Plague: your call, aimed like Skyfall, 15s recharge ----------
rep("if(sp==='swarmplague'){if(u.plagueT>0){u.plagueT-=dt;return true}if(!u.plNow)return false;u.plNow=0;",
    "if(sp==='swarmplague'){u.plCd=(u.plCd==null?4:u.plCd)-dt;if(u.plagueT>0){u.plagueT-=dt;return true}\n    if(u.side===0){if(!(u.cast>G.t)||!u.castXY||u.plCd>0)return false;const[px,py]=u.castXY;u.castXY=null;u.cast=0;let tg=null,bd=2;for(const v of G.units)if(foeOf(u,v)&&!U[v.type].air){const d=Math.hypot(v.x-px,v.y-py);if(d<bd){bd=d;tg=v}}u.plCd=15;u.plagueT=3.6;face(u,px,py);(G.clouds||(G.clouds=[])).push({x:u.x,y:u.y,tx:px,ty:py,tgt:tg,t:-1.4,life:4.4,side:u.side,src:u,tk:0,seed:R()*99});float(u.x,u.y,'Plague!','#3f6fd8');return true}\n    if(!u.plNow)return false;u.plNow=0;")
rep("if(!best)return false;u.plagueT=3.6;face(u,best.x,best.y);","if(!best)return false;u.plagueT=3.6;u.plCd=15;face(u,best.x,best.y);")
rep("if(t.batk==='brood'){if(t.special==='swarmplague'&&!(u.plagueT>0)&&R()<.1){u.plNow=1;return}","if(t.batk==='brood'){if(t.special==='swarmplague'&&u.side!==0&&!(u.plagueT>0)&&!(u.plCd>0)&&R()<.1){u.plNow=1;return}")
rep("thornslam:{cd:u=>u.tsT==null?2.5:u.tsT,max:7,col:'#8fbf5a',ic:'\u2742'}};",
    "thornslam:{cd:u=>u.tsT==null?2.5:u.tsT,max:7,col:'#8fbf5a',ic:'\u2742'},swarmplague:{nm:'Plague',aim:'Tap where to send the Plague.',cd:u=>u.plCd==null?4:u.plCd,max:15,col:'#3f6fd8',ic:'\\u273a'}};")
rep("skyfall:{cd:u=>u.skyCd==null?5:u.skyCd,max:12,","skyfall:{aim:'Tap where the Sphinx should land.',land:1,cd:u=>u.skyCd==null?5:u.skyCd,max:12,")
rep("if(!landAt(tx,ty)){continue}","if(M.land&&!landAt(tx,ty)){continue}")
rep("if(!n)toast('The Sphinx can\u2019t land there.');","if(!n)toast(M.land?'The Sphinx can\u2019t land there.':'Out of reach.');")
rep("function castSp(k){if(k==='skyfall'){const M=MANSP[k],rd=[...SEL].filter(u=>u.side===0&&u.hp>0&&U[u.type].special===k&&M.cd(u)<=0);if(!rd.length){toast('Skyfall is recharging.');return}if(SPAIM==='skyfall'){SPAIM=null;toast('Skyfall cancelled.');return}SPAIM='skyfall';toast('Tap where the Sphinx should land.');return}",
    "function castSp(k){if(MANSP[k].aim){const M=MANSP[k],nm=M.nm||SPNAME[k]||k,rd=[...SEL].filter(u=>u.side===0&&u.hp>0&&U[u.type].special===k&&M.cd(u)<=0);if(!rd.length){toast(`${nm} is recharging.`);return}if(SPAIM===k){SPAIM=null;toast(`${nm} cancelled.`);return}SPAIM=k;toast(M.aim);return}")
open(F,'w').write(s);print('plague ctl ok')
