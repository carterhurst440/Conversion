F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
# ================= harbors with their own names, each launching two mythic ships =================
rep("8:{sower:'Verdant Druid',","8:{harbor:'Caladh',harbors:'Caladhs',sower:'Verdant Druid',")
rep("0:{hall:'Pyramid',","0:{harbor:'Meryt',harbors:'Meryts',hall:'Pyramid',")
rep("1:{sower:'Shade',","1:{harbor:'Limen',harbors:'Limens',sower:'Shade',")
rep("const FDEF={","const FDEF={harbor:'Harbor',harbors:'Harbors',")
rep("const FWORDS=[","const FWORDS=[['Harbors','harbors'],['Harbor','harbor'],")
rep("harbor:{name:'Harbor',hp:400,cost:{wood:60},coast:true,desc:'Docks a ship on your shore. Only needed when water stands between you and a rival. Comes with a ship.'},",
    "harbor:{name:'Harbor',hp:400,cost:{wood:60},coast:true,desc:'Your faith\\u2019s landing on the shore. It comes with a transport that carries troops across the water, and at your second level it launches a warship. Needed whenever water stands between you and a rival.'},")
rep("harbor:[0,0,0,0,0]","harbor:[1,2,2,2,2]")
rep("['Army',['barracks']],","['Army',['barracks','harbor']],")
rep("['Army',['wabet','sphinxmon']]","['Army',['wabet','sphinxmon','harbor']]")
rep("const SHIP={cap:20,hp:600,spd:2.6};",r"""const SHIP={cap:20,hp:600,spd:2.6};
const SHIPK={
 currach:{n:'Currach',cap:20,hp:460,spd:3,d:'A hide-and-wicker boat of the western isles. Light, quick, and carries 20 troops.'},
 sweeper:{n:'Wave-Sweeper',cap:6,hp:540,spd:4.2,noSail:1,war:{range:4.4,dmg:15,fr:1.25,col:'#7fe0d0',kind:'spray'},d:'Manannán mac Lir’s boat that needs no oar or sail. The fastest ship on the sea; it hurls bolts of sea-spray.'},
 papyrus:{n:'Papyrus Barque',cap:20,hp:560,spd:2.6,d:'Bound reeds from the Nile marshes, prow and stern curled high. Carries 20 troops.'},
 solar:{n:'Solar Barque',cap:6,hp:620,spd:2.9,noSail:1,war:{range:5.2,dmg:28,fr:.55,col:'#ffd24a',kind:'beam'},d:'The barque of the sun that sails the sky by day and the underworld by night. Burns its targets with long beams of sunlight.'},
 ferry:{n:'Charon’s Ferry',cap:24,hp:520,spd:2.6,noSail:1,d:'The ferryman’s skiff from the banks of the Styx, poled by a hooded figure with a lantern. Carries 24 troops.'},
 trireme:{n:'Trireme',cap:8,hp:740,spd:3.3,war:{range:3.9,dmg:20,fr:.9,col:'#c4553f',kind:'arrows',ram:1},d:'Three banks of oars and a bronze ram. Its archers volley at range, and it rams enemy ships it sails into.'}};
const FSHIP={8:['currach','sweeper'],0:['papyrus','solar'],1:['ferry','trireme']};
const shipKinds=side=>FSHIP[G.S[side]?G.S[side].god:-1]||['currach','sweeper'],SK=s=>SHIPK[s&&s.k]||{n:'Ship',cap:SHIP.cap,hp:SHIP.hp,spd:SHIP.spd};""")
# makeShip takes a kind (transport by default)
i=s.find("function makeShip(side,x,y){");j=s.find("G.ships.push(s);return s}",i)+len("G.ships.push(s);return s}")
s=s[:i]+"function makeShip(side,x,y,war){const k=shipKinds(side)[war?1:0],K=SHIPK[k],s={isShip:true,k,armed:!!K.war,gcd:0,side,x,y,hx:1,hy:0,hp:K.hp,max:K.hp,cargo:[],path:[],state:'idle',order:null,unl:null,hurt:0,ph:R()*6,ramT:0};G.ships.push(s);return s}"+s[j:]
rep("G.S[s.side].ship=null}}","if(G.S[s.side].ship===s)G.S[s.side].ship=null;if(G.S[s.side].war===s)G.S[s.side].war=null}}")
rep("if(s.side===0)toast(`Your ship was sunk","if(s.side===0)toast(`Your ${SK(s).n} was sunk")
# warship fire, by kind; ramming; per-kind speed
rep("if(s.armed){s.gcd-=dt;if(s.gcd<=0){let tg=null,bd=GUN.range;","if(s.armed){const WP=SK(s).war||{range:GUN.range,dmg:GUN.dmg,fr:GUN.fr,kind:'ball'};s.gcd-=dt;if(WP.ram){s.ramT-=dt;if(s.ramT<=0)for(const o of G.ships){if(o.dead||o.side===s.side||Math.hypot(o.x-s.x,o.y-s.y)>1.1)continue;damageShip(o,110,s.side);s.ramT=5;ring(o.x,o.y,.9,'#c9a35a');float(s.x,s.y,'Ram!','#c4553f');puff(o.x,o.y,8);break}}if(s.gcd<=0){let tg=null,bd=WP.range;")
rep("if(tg){s.gcd=1/GUN.fr;const tx=tg.s?bcx(tg):tg.x,ty=tg.s?bcy(tg):tg.y;s.gside=((tx-s.x)*-s.hy+(ty-s.y)*s.hx)>0?1:-1;s.gfire=.3;G.shots.push({x:s.x,y:s.y,z:WL+.8,tgt:tg,dmg:GUN.dmg,spd:9,kind:'ball',side:s.side});puff(s.x,s.y,3)}",
    "if(tg){s.gcd=1/WP.fr;const tx=tg.s?bcx(tg):tg.x,ty=tg.s?bcy(tg):tg.y;s.gside=((tx-s.x)*-s.hy+(ty-s.y)*s.hx)>0?1:-1;s.gfire=.3;\n        if(WP.kind==='beam'){G.fx.push({kind:'beam',x:s.x,y:s.y,x2:tx,y2:ty,z:WL+1.4,life:0,max:.45,col:WP.col});G.shots.push({x:s.x,y:s.y,z:WL+1.2,tgt:tg,dmg:WP.dmg,spd:40,kind:'arrow',side:s.side,col:WP.col})}\n        else if(WP.kind==='arrows'){for(let q=0;q<2;q++)G.shots.push({x:s.x+rnd(-.3,.3),y:s.y+rnd(-.3,.3),z:WL+1,tgt:tg,dmg:WP.dmg/2,spd:11+q,kind:'arrow',side:s.side})}\n        else{G.shots.push({x:s.x,y:s.y,z:WL+.8,tgt:tg,dmg:WP.dmg,spd:10,kind:'ball',side:s.side,col:WP.col});if(WP.kind==='spray')burst(s.x,s.y,['#bff4ec','#7fe0d0','#ffffff'],4)}puff(s.x,s.y,2)}")
rep("st=SHIP.spd*dt;","st=SK(s).spd*dt;")
rep("cargoHouse(s)+t.house>SHIP.cap){idleHere(u);break}","cargoHouse(s)+t.house>SK(s).cap){idleHere(u);break}")
rep("if(cargoHouse(s)+U[u.type].house>SHIP.cap)continue;","if(cargoHouse(s)+U[u.type].house>SK(s).cap)continue;")
rep("<b>${s.armed?'Warship':'Ship'} · ${ch} / ${SHIP.cap} aboard</b>","<b>${SK(s).n} · ${ch} / ${SK(s).cap} aboard</b>")
rep("if(mine&&b.type==='harbor'&&S.ship)st.push(`<div class=\"pst\"><span>Ship: <b>${cargoHouse(S.ship)} / ${SHIP.cap}</b> aboard</span></div>`);",
    "if(mine&&b.type==='harbor'&&S.ship)st.push(`<div class=\"pst\"><span>${SK(S.ship).n}: <b>${cargoHouse(S.ship)} / ${SK(S.ship).cap}</b> aboard</span></div>`);")
# harbor panel: the transport and the warship
i=s.find("if(b.type==='harbor'){if(!b.guns){h+=");j=s.find("\n",i)
s=s[:i]+r"""if(b.type==='harbor'){const[tk,wk]=shipKinds(0),T1=SHIPK[tk],W1=SHIPK[wk],s=S.ship,w=S.war&&!S.war.dead?S.war:null;h+=`<div class="pd"><b>${T1.n}</b>: ${T1.d}</div><div class="pd"><b>${W1.n}</b>: ${W1.d}${S.tier<2?' Needs your second level.':''}</div>`;
      if(!s)acts.push(btn('newship','New '+T1.n,SHIPCOST));else{acts.push(`<button class="btn" data-act="selship">${T1.n}</button>`);acts.push(btn('callship','Call home',null,Math.hypot(s.x-b.dock.x,s.y-b.dock.y)<1.5));acts.push(btn('loadall','Board all',null,!G.units.some(u=>u.side===0&&Math.hypot(u.x-b.x,u.y-b.y)<9)||Math.hypot(s.x-b.dock.x,s.y-b.dock.y)>1.5))}
      if(!w)acts.push(btn('newwar','Launch '+W1.n,GUNCOST,S.tier<2));else acts.push(`<button class="btn" data-act="selwar">${W1.n}</button>`)}"""+s[j:]
rep("if(a==='newship'&&can(0,SHIPCOST)){pay(0,SHIPCOST);S.ship=makeShip(0,b.dock.x,b.dock.y);toast('A new ship is docked at your Harbor.')}",
    "if(a==='newship'&&can(0,SHIPCOST)){pay(0,SHIPCOST);S.ship=makeShip(0,b.dock.x,b.dock.y);toast(`A new ${SK(S.ship).n} is docked at your ${BNm(0,'harbor')}.`)}\n  if(a==='newwar'&&S.tier>=2&&!(S.war&&!S.war.dead)&&can(0,GUNCOST)){pay(0,GUNCOST);S.war=makeShip(0,b.dock.x,b.dock.y,true);burst(b.dock.x,b.dock.y,['#fbf6ee','#7fbde8'],14);toast(`The ${SK(S.war).n} is launched.`)}\n  if(a==='selwar'&&S.war&&!S.war.dead){select(null);SEL.clear();SELSHIP=S.war;renderHUD(true);return}")
# the old Ship Cannons research is gone: warships replace it
rep("function techState(side,k){const S=G.S[side],T=TECH[k];","function techState(side,k){const S=G.S[side],T=TECH[k];if(k==='cannons')return{hide:true};")
# the computer launches its warship and sends it along on raids
rep("if(h&&!h.guns&&S.tier>=2&&S.res.wood>GUNCOST.wood+60&&S.res.stone>GUNCOST.stone+20){pay(k,GUNCOST);h.guns=true;if(S.ship&&!S.ship.armed){S.ship.armed=true;S.ship.max+=GUN.hp;S.ship.hp+=GUN.hp}}",
    "if(h&&!(S.war&&!S.war.dead)&&S.tier>=2&&can(k,{wood:GUNCOST.wood+6,stone:GUNCOST.stone+2})){pay(k,GUNCOST);S.war=makeShip(k,h.dock.x,h.dock.y,true)}")
rep("if(shipSail(s,L,{unload:L,mode:'raid',then:'home'})){ai.size+=3;ai.raids++}","if(shipSail(s,L,{unload:L,mode:'raid',then:'home'})){ai.size+=3;ai.raids++;const w=S.war;if(w&&!w.dead&&w.state==='idle')shipSail(w,L,null)}")
# culture-specific landing buildings
rep("const sp=P(-d.dx*.22,-d.dy*.22,0);const Q=ibox(sp[0],sp[1],s,.2,.18,0,12,null,WOODC[1],WOODC[2]);gable(Q,.2,.18,12,9,.03,C2,tint(C1,.15));",
    "const sp=P(-d.dx*.22,-d.dy*.22,0),hg=live&&G.S[b.side]?G.S[b.side].god:playerGod();\n      if(hg===8){celRound(sp[0],sp[1],s,.2,9,15,null,b);for(const t of[.3,.7]){const p=c(t,-w-.05,8);ctx.fillStyle='#d6d3cb';ctx.fillRect(p[0]-1.6*s,p[1]-9*s,3.2*s,9*s)}}\n      else if(hg===0){ibox(sp[0],sp[1],s,.2,.17,0,4,'#efe2c2','#dcc79c','#c3a979');for(const[u,v]of[[-.12,.12],[.12,.12],[.12,-.12]]){const p=[sp[0]+(u-v)*32*s,sp[1]+(u+v)*16*s-4*s];ctx.fillStyle='#d9b77a';ctx.fillRect(p[0]-2*s,p[1]-14*s,4*s,14*s);ctx.fillStyle='#5fae3e';ctx.beginPath();ctx.ellipse(p[0],p[1]-15*s,4.2*s,2.2*s,0,0,TAU);ctx.fill()}ibox(sp[0],sp[1]-18*s,s,.2,.17,0,3,'#f3e3bb','#e8c35a','#c9a23f')}\n      else if(hg===1){ibox(sp[0],sp[1],s,.2,.17,0,3,'#f4efe6','#e2d9c8','#c9bca6');for(const[u,v]of[[-.14,.14],[0,.14],[.14,.14],[.14,0],[.14,-.14]]){const p=[sp[0]+(u-v)*32*s,sp[1]+(u+v)*16*s-3*s];ctx.fillStyle='#fbf8f2';ctx.fillRect(p[0]-1.6*s,p[1]-13*s,3.2*s,13*s)}const Q=ibox(sp[0],sp[1]-16*s,s,.21,.18,0,3,'#f4efe6','#e2d9c8','#c9bca6');gable(Q,.21,.18,3,7,.03,'#b5523a','#d4704f')}\n      else{const Q=ibox(sp[0],sp[1],s,.2,.18,0,12,null,WOODC[1],WOODC[2]);gable(Q,.2,.18,12,9,.03,C2,tint(C1,.15))}")
# ship art by kind
rep("function drawShipSpr(sx,sy,Z,hx,hy,side,n,hurt,ph,sel,armed,gside,gfire){","function drawShipSpr(sx,sy,Z,hx,hy,side,n,hurt,ph,sel,armed,gside,gfire,kk){const K=SHIPK[kk]||{},HC={currach:['#4a3426','#5e4330','#7a5a42','#b08a62'],sweeper:['#4f8f96','#6fb4b8','#9fd8d0','#d8f4ee'],papyrus:['#a8904a','#c4aa5a','#d9c27e','#ecdca6'],solar:['#a8822e','#c9a23f','#e8c35a','#ffe9a8'],ferry:['#2b2440','#3b3550','#4f4660','#6e6380'],trireme:['#5a3d2a','#7a5238','#9c6e4a','#d9b48a']}[kk]||['#7a5a42','#8a6650','#9c7756','#d9b48a'];")
rep("ctx.fillStyle=hurt?'#fbf6ee':o>-1?'#7a5a42':'#8a6650';hull(Z);ctx.fill();ctx.restore()}","ctx.fillStyle=hurt?'#fbf6ee':o>-1?HC[0]:HC[1];hull(Z);ctx.fill();ctx.restore()}")
rep("ctx.fillStyle='#9c7756';hull(Z);ctx.fill();ctx.fillStyle='#d9b48a';hull(Z*.84);ctx.fill();\n  ctx.strokeStyle='rgba(138,102,80,.45)';ctx.lineWidth=1.2*Z;for(let k=-2;k<=2;k++){ctx.beginPath();ctx.moveTo(-20*Z,k*4*Z);ctx.lineTo(22*Z,k*4*Z);ctx.stroke()}",
r"""ctx.fillStyle=HC[2];hull(Z);ctx.fill();ctx.fillStyle=HC[3];hull(Z*.84);ctx.fill();
  if(kk==='papyrus'||kk==='solar'){ctx.strokeStyle='rgba(90,64,30,.5)';ctx.lineWidth=1.4*Z;for(let x=-22;x<=26;x+=6){ctx.beginPath();ctx.moveTo(x*Z,-10*Z);ctx.lineTo(x*Z,10*Z);ctx.stroke()}}
  else{ctx.strokeStyle='rgba(60,40,30,.35)';ctx.lineWidth=1.2*Z;for(let k=-2;k<=2;k++){ctx.beginPath();ctx.moveTo(-20*Z,k*4*Z);ctx.lineTo(22*Z,k*4*Z);ctx.stroke()}}
  if(kk==='trireme'){ctx.strokeStyle='#5a3d2a';ctx.lineWidth=1.4*Z;const sw=Math.sin(time*4+ph)*3*Z;for(const m of[-1,1])for(let x=-16;x<=18;x+=4){ctx.beginPath();ctx.moveTo(x*Z,m*10*Z);ctx.lineTo(x*Z+sw,m*19*Z);ctx.stroke()}ctx.fillStyle='#c9a35a';ctx.beginPath();ctx.moveTo(29*Z,-3*Z);ctx.lineTo(38*Z,0);ctx.lineTo(29*Z,3*Z);ctx.fill();ctx.fillStyle='#b5523a';ctx.fillRect(-20*Z,-1.2*Z,44*Z,2.4*Z)}
  if(kk==='solar'){ctx.fillStyle='#f3e3bb';ctx.fillRect(-10*Z,-6*Z,14*Z,12*Z);ctx.fillStyle='#2f5e9e';ctx.fillRect(-10*Z,-6*Z,14*Z,2*Z)}
  if(kk==='ferry'){ctx.fillStyle='rgba(120,220,180,.25)';hull(Z*.6);ctx.fill()}""")
rep("ctx.fillStyle=sd.c1;ctx.beginPath();ctx.arc(-17*Z,0,4*Z,0,TAU);ctx.fill();\n  if(armed){","ctx.fillStyle=sd.c1;ctx.beginPath();ctx.arc(-17*Z,0,4*Z,0,TAU);ctx.fill();\n  if(armed&&!K.war){")
rep("  const my=-7*Z,fx=(hx-hy)*32,fy=(hx+hy)*16,fl=Math.hypot(fx,fy)||1,ux=fx/fl,uy=fy/fl,px=(-hy-hx)*32,py=(-hy+hx)*16,pl=Math.hypot(px,py)||1,qx=px/pl,qy=py/pl;",
r"""  const my=-7*Z,fx=(hx-hy)*32,fy=(hx+hy)*16,fl=Math.hypot(fx,fy)||1,ux=fx/fl,uy=fy/fl,px=(-hy-hx)*32,py=(-hy+hx)*16,pl=Math.hypot(px,py)||1,qx=px/pl,qy=py/pl;
  const PR=[ux*28*Z*Math.hypot(Math.cos(a),Math.sin(a)*.5),my+uy*14*Z],ST=[-ux*25*Z,my-uy*12*Z];
  if(kk==='papyrus'||kk==='solar'){ctx.strokeStyle=HC[2];ctx.lineWidth=5*Z;ctx.lineCap='round';for(const[p,dd]of[[PR,1],[ST,-1]]){ctx.beginPath();ctx.moveTo(p[0],p[1]);ctx.quadraticCurveTo(p[0]+ux*dd*6*Z,p[1]-8*Z,p[0]+ux*dd*3*Z,p[1]-16*Z);ctx.stroke()}ctx.lineCap='butt'}
  if(kk==='sweeper'){ctx.strokeStyle='#d8f4ee';ctx.lineWidth=2.4*Z;ctx.beginPath();for(let q=0;q<=20;q++){const an=q/20*TAU*1.4,r=(8-q*.35)*Z;const x=PR[0]+Math.cos(an)*r*.6,y=PR[1]-10*Z+Math.sin(an)*r;q?ctx.lineTo(x,y):ctx.moveTo(x,y)}ctx.stroke();if(!reduceMotion){glow(ST[0],ST[1]+6*Z,16*Z,'#7fe0d0',.45)}}
  if(kk==='solar'){const sd2=[ux*-2*Z,my-26*Z];glow(sd2[0],sd2[1],22*Z,'#ffd86a',.6);ctx.fillStyle='#ffd24a';ctx.beginPath();ctx.arc(sd2[0],sd2[1],7*Z,0,TAU);ctx.fill();ctx.strokeStyle='#c9a23f';ctx.lineWidth=1.4*Z;ctx.stroke()}
  if(kk==='ferry'){const L=[PR[0],PR[1]-14*Z];ctx.strokeStyle='#2b2440';ctx.lineWidth=1.4*Z;line(PR[0],PR[1],L[0],L[1]-2*Z);glow(L[0],L[1]+3*Z,12*Z,'#8fffd0',.55+.15*Math.sin(time*3+ph));ctx.fillStyle='#c8ffe6';ctx.beginPath();ctx.arc(L[0],L[1]+3*Z,2.4*Z,0,TAU);ctx.fill();
    const F=[ST[0]*.6,ST[1]];ctx.fillStyle='#1d1830';ctx.beginPath();ctx.moveTo(F[0]-5*Z,F[1]);ctx.quadraticCurveTo(F[0]-4*Z,F[1]-20*Z,F[0],F[1]-24*Z);ctx.quadraticCurveTo(F[0]+4*Z,F[1]-20*Z,F[0]+5*Z,F[1]);ctx.fill();ctx.strokeStyle='#5a4a3a';ctx.lineWidth=1.6*Z;line(F[0]+3*Z,F[1]-20*Z,F[0]+10*Z,F[1]+8*Z)}
  if(K.noSail){ctx.restore();return drawShipTag(n,my,Z,sx,sy)}""")
rep("  ctx.fillStyle='#fbf6ee';ctx.beginPath();ctx.moveTo(qx*sw,b0+qy*sw*.4);","  ctx.fillStyle=kk==='currach'?'#d9c39a':'#fbf6ee';ctx.beginPath();ctx.moveTo(qx*sw,b0+qy*sw*.4);")
rep("ctx.fillStyle=sd.c1;ctx.beginPath();ctx.moveTo(qx*sw*.92,(b0+t0)/2+4*Z+qy*sw*.35);","ctx.fillStyle=kk==='trireme'?'#b5523a':kk==='currach'?'#4f8a3f':sd.c1;ctx.beginPath();ctx.moveTo(qx*sw*.92,(b0+t0)/2+4*Z+qy*sw*.35);")
rep("function drawShipSpr(","function drawShipTag(n,my,Z,sx,sy){ctx.save();ctx.translate(sx,sy);if(n>0){const s=Math.max(.85,Z),t=String(n);ctx.font=`700 ${Math.round(11*s)}px Figtree,sans-serif`;const w=ctx.measureText(t).width+12*s,h=16*s,y=my-40*Z;ctx.fillStyle='rgba(251,246,238,.92)';rrect(-w/2,y-h/2,w,h,h/2);ctx.fill();ctx.fillStyle='#2b2440';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(t,0,y+.5);ctx.textBaseline='alphabetic'}ctx.restore()}\nfunction drawShipSpr(")
rep("drawShipSpr(sx,sy,Z,o.hx,o.hy,o.side,o.side===0?o.cargo.length:0,o.hurt>0,o.ph,SELSHIP===o,o.armed,o.gside||1,o.gfire||0);","drawShipSpr(sx,sy,Z,o.hx,o.hy,o.side,o.side===0?o.cargo.length:0,o.hurt>0,o.ph,SELSHIP===o,o.armed,o.gside||1,o.gfire||0,o.k);")
rep("if(k==='ship'){drawShipSpr(w/2,h-8,.42*sc,1,-.3,0,0,false,0,false);return}","if(k==='ship'){drawShipSpr(w/2,h-8,.42*sc,1,-.3,0,0,false,0,false,false,1,0,(FSHIP[playerGod()]||['currach'])[0]);return}")

# ================= map variety: one continent, a land cut by straits, or separate isles =================
rep("  const off=.1+R()*.08,lakeT=.62+R()*.08;","  const off=.1+R()*.08,lakeT=.62+R()*.08,A0=R()*TAU,rm=R(),MODE=rm<.38?'continent':rm<.68?'straits':'isles';MAPMODE=MODE;")
rep("    const i=idx(x,y);elev[i]=e;land[i]=e>.5&&x>1",
r"""    if(MODE!=='continent'){const dx=x+.5-WN/2,dy=y+.5-WN/2,rr=Math.hypot(dx,dy),an=Math.atan2(dy,dx),wob=(vnoise(x/6,y/6,SEED+91)-.5)*2.4;
      if(MODE==='isles'){let md=9;for(let k=0;k<np;k++){const d=Math.abs((((an-(A0+(k+.5)*TAU/np))%TAU)+TAU+Math.PI)%TAU-Math.PI);md=Math.min(md,d)}if(rr>WN*.11&&md*rr<2.4+wob)e-=.6;if(Math.abs(rr-WN*.15)<1.7+wob*.5)e-=.6}
      else{const ch=Math.abs(fbm(x/17+300,y/17,SEED+300,3)-.5);if(ch<.026+.006*wob)e-=.5}}
    const i=idx(x,y);elev[i]=e;land[i]=e>.5&&x>1""")
rep("  if(sizes[MAIN]<WN*WN*.22)return false;","  {let tot=0;for(const v of sizes)tot+=v||0;if(MODE==='continent'?sizes[MAIN]<WN*WN*.22:tot<WN*WN*.26)return false}")
rep("STARTS=[];const a0=R()*TAU;","STARTS=[];const a0=A0;")
rep("if(isl[i]!==MAIN||ldist[i]<5)continue;const d=Math.hypot(x-tx,y-ty);","if((MODE==='continent'?isl[i]!==MAIN:(sizes[isl[i]]||0)<150)||ldist[i]<5)continue;const d=Math.hypot(x-tx,y-ty);")
rep("const N4=[[1,0],[-1,0],[0,1],[0,-1]];","const N4=[[1,0],[-1,0],[0,1],[0,-1]];let MAPMODE='continent';")
open(F,'w').write(s);print('harbor+maps ok',len(s))
s=open(F).read()
rep("SEL:()=>SEL,","SEL:()=>SEL,mapMode:()=>MAPMODE,massAt:(x,y)=>isl[idx(x,y)],dockSpot:(x,y)=>dockSpot(x,y),isBeach:(x,y)=>!!beachA[idx(x,y)],")
open(F,'w').write(s)
s=open(F).read()
rep("aiTech(ai);aiWork(ai);aiTrain(ai);aiRaid(ai);","aiTech(ai);aiWork(ai);aiTrain(ai);aiRaid(ai);aiShip(ai);")
open(F,'w').write(s);print('ai ships on')
s=open(F).read()
rep("const ref=B[b.type].cost?Object.fromEntries(Object.entries(B[b.type].cost)","const ref=B[b.type].cost?Object.fromEntries(Object.entries(CX(0,B[b.type].cost))")
open(F,'w').write(s);print('refund label ok')
