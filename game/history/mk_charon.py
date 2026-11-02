s=open('fact_stoneb.js').read()
def r(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:80]);s=s.replace(a,b)
r(s[:s.find("FACT.stoneb=function(){")],"// ---------- Charon / the Ferryman (Greek): hooded boatman on the shared Tripo rig, a long oar gripped in both hands; sweeping oar strikes ----------\n")
r("FACT.stoneb=function(){const LAB=(typeof GLAB==='function')?GLAB('stoneb'):window.LABCFG;","FACT.charon=function(){const LAB=(typeof GLAB==='function')?GLAB('charon'):window.LABCFG;")
r("const G0=window.MODELS&&window.MODELS[FACT.__sbm||'stoneb']||window.MODELS.stoneb;","const UPC=FACT.__chu===1;const G0=window.MODELS&&window.MODELS[UPC?'charonu':'charon']||window.MODELS.charon||window.MODELS.stoneb;")
# the oar, held between both palms
r("  U.chips=chips;",r"""  U.chips=chips;
  const oarW=M(UPC?'#e8bf4e':'#7a5634'),oarD=M(UPC?'#d4a23a':'#5a3e24'),oarT=M(UPC?'#9a1f2a':'#3f8f86');for(const x of[oarW,oarD,oarT]){x.userData.outlineParameters={visible:false};U.mats.push(x)}
  const oar=new T.Group();{const sh=new T.Mesh(new T.CylinderGeometry(.011,.013,1,7),oarW);sh.position.y=.5;oar.add(sh);const bl=new T.Mesh(new T.BoxGeometry(.075,.24,.014),oarD);bl.position.y=1.08;oar.add(bl);const st=new T.Mesh(new T.BoxGeometry(.05,.13,.016),oarT);st.position.set(.006,1.1,.001);oar.add(st);const nk=new T.Mesh(new T.CylinderGeometry(.016,.011,.06,7),oarD);nk.position.y=.95;oar.add(nk);if(UPC){const tip=new T.Mesh(new T.ConeGeometry(.016,.06,6),oarD);tip.rotation.x=Math.PI;tip.position.y=-.03;oar.add(tip);for(const y of[.62,.8]){const rg=new T.Mesh(new T.CylinderGeometry(.017,.017,.02,8),oarD);rg.position.y=y;oar.add(rg)}const tr=new T.Group();tr.position.set(.006,1.1,.009);for(const x of[-.016,0,.016]){const p=new T.Mesh(new T.BoxGeometry(.006,.07,.004),oarD);p.position.x=x;p.position.y=x?0:.008;tr.add(p)}const bar=new T.Mesh(new T.BoxGeometry(.04,.006,.004),oarD);bar.position.y=-.03;tr.add(bar);oar.add(tr)}}
  oar.scale.setScalar(sc);SCN.add(oar);U.oar=oar;
  const lanternGlow=egSprite(GLWT(),.06,'#8fffd0');SCN.add(lanternGlow);U.eyeGlow=lanternGlow;""")
r("  const STANCE=()=>JSON.parse(JSON.stringify(ST));","""  const GRIP={hR:[-.11,SY-.03,.13],hL:[.05,-.13,.17],bR:[.2,1,.4],bL:[.2,1,.4],eR:[-1,-.3,-.3],eL:[.8,-.5,-.3]};
  // SWEEP: coil to the right with the oar back, then a flat two-handed sweep across the front at waist height, follow through and recover
  const SWEEP=carry([K(0,Object.assign({p:[0,-.04,0],tw:0},GRIP)),
    K(.26,{p:[0,-.08,-.02],tw:-34,pitch:2,bend:2,headY:20,hR:[-.3,.02,-.06],hL:[-.06,-.04,.12],bR:[-1,.1,0],bL:[-1,.1,0],eR:[-1,.4,-.4],eL:[.6,-.6,-.4]},{fR:[-.1,ANK,-.1],fyR:24,lfR:.04}),
    K(.42,{p:[0,-.12,.05],tw:30,pitch:10,bend:8,headY:-12,hR:[.26,-.06,.33],hL:[.06,-.06,.18],bR:[1,0,.5],bL:[1,0,.5],eR:[-.6,-.6,-.2],eL:[.9,-.4,-.2]},{fL:[.1,ANK,.16],fyL:-12,lfL:.05}),
    K(.62,{p:[0,-.1,.03],tw:40,pitch:8,bend:6,hR:[.32,-.1,.18],hL:[.12,-.08,.14],bR:[1,-.2,0],bL:[1,-.2,0]}),
    K(1,Object.assign({p:[0,-.04,0],tw:0},GRIP),{fL:[.075,ANK,.03],fyL:-8,lfL:.04,fR:[-.075,ANK,-.03],fyR:8,lfR:.04})]);
  // THRUST: draw the oar back along the hip, lunge, and drive it out long like a spear, sliding it through the hands to full reach
  const THRUST=carry([K(0,Object.assign({p:[0,-.04,0]},GRIP)),
    K(.22,{p:[0,-.08,-.04],tw:-22,pitch:-2,headY:14,hR:[-.2,-.06,-.06],hL:[-.02,-.08,.1],bR:[0,.1,1],bL:[0,.1,1],eR:[-1,-.2,-.4],eL:[.8,-.5,-.3],slide:-.12},{fR:[-.09,ANK,-.1],fyR:20,lfR:.04}),
    K(.38,{p:[0,-.16,.1],tw:16,pitch:16,bend:8,headP:-4,hR:[.02,-.02,.42],hL:[.08,-.04,.26],bR:[0,0,1],bL:[0,0,1],eR:[-.6,-.6,-.2],eL:[.8,-.6,-.2],slide:.42},{fL:[.09,ANK,.22],fyL:-6,lfL:.05}),
    K(.55,{p:[0,-.15,.09],tw:12,pitch:14,bend:7,hR:[.02,-.03,.4],hL:[.08,-.05,.25],bR:[0,0,1],bL:[0,0,1],slide:.38}),
    K(.85,Object.assign({p:[0,-.04,0],slide:0},GRIP),{fL:[.075,ANK,.03],fyL:-8,lfL:.04,fR:[-.075,ANK,-.03],fyR:8,lfR:.04})]);
  // RISE: crouch with the blade low in front, then heave it up in a great rising arc until the oar stands high overhead
  const RISE=carry([K(0,Object.assign({p:[0,-.04,0]},GRIP)),
    K(.25,{p:[0,-.2,.04],tw:-10,pitch:18,bend:14,headP:10,hR:[.06,-.26,.3],hL:[.1,-.2,.16],bR:[0,-1,.4],bL:[0,-1,.4],eR:[-.7,-.2,-.5],eL:[.9,-.2,-.4],slide:.08},{fR:[-.09,ANK,-.08],fyR:16,lfR:.03}),
    K(.45,{p:[0,-.02,.0],tw:8,pitch:-10,bend:-8,headP:-16,hR:[.0,SY+.16,.24],hL:[.08,SY-.02,.18],bR:[0,1,.2],bL:[0,1,.2],eR:[-1,.2,-.3],eL:[1,.1,-.3],slide:.12}),
    K(.62,{p:[0,.0,-.02],tw:4,pitch:-14,bend:-10,headP:-20,hR:[-.02,SY+.3,.06],hL:[.06,SY+.12,.06],bR:[0,1,-.2],bL:[0,1,-.2],slide:.06}),
    K(.95,Object.assign({p:[0,-.04,0],slide:0},GRIP),{fR:[-.075,ANK,-.03],fyR:8,lfR:.04})]);
  // POUND: oar raised high in both hands, a step in, and a crushing two-handed slam of the blade into the ground
  const POUND=carry([K(0,Object.assign({p:[0,-.04,0]},GRIP)),
    K(.32,{p:[0,.02,-.04],tw:-6,pitch:-16,bend:-12,headP:-18,hR:[-.02,SY+.32,.0],hL:[.07,SY+.16,.02],bR:[0,1,-.4],bL:[0,1,-.4],eR:[-1,.3,-.3],eL:[1,.2,-.3],slide:.04},{fL:[.08,ANK,.16],fyL:-8,lfL:.06}),
    K(.62,{p:[0,-.24,.12],tw:4,pitch:30,bend:20,headP:14,hR:[.02,-.18,.46],hL:[.09,-.12,.3],bR:[0,-.6,1],bL:[0,-.6,1],eR:[-.7,-.3,-.3],eL:[.9,-.3,-.3],slide:.2}),
    K(.78,{p:[0,-.22,.1],tw:2,pitch:26,bend:18,headP:12,hR:[.02,-.17,.44],hL:[.09,-.11,.29],bR:[0,-.6,1],bL:[0,-.6,1],slide:.2}),
    K(1.1,Object.assign({p:[0,-.04,0],slide:0},GRIP),{fL:[.075,ANK,.03],fyL:-8,lfL:.04})]);
  const STANCE=()=>JSON.parse(JSON.stringify(ST));""")
r("punch:{dur:.62,fn:t=>sampleKeys(PUNCH,t),hits:[[.18,1],[.36,1]]},","punch:{dur:.62,fn:t=>sampleKeys(PUNCH,t),hits:[[.18,1],[.36,1]]},sweep:{dur:1,fn:t=>sampleKeys(SWEEP,t),hits:[[.42,1]]},thrust:{dur:.85,fn:t=>sampleKeys(THRUST,t),hits:[[.38,1]]},rise:{dur:.95,fn:t=>sampleKeys(RISE,t),hits:[[.45,1]]},pound:{dur:1.1,fn:t=>sampleKeys(POUND,t),hits:[[.62,1.6]]},")
# idle and walking keep the oar in both hands, blade up over the right shoulder
r("    if(S.ld>.01&&S.clip==='idle'){","    if(S.clip==='idle'){const bob=Math.sin(wph*2)*.006*wk+Math.sin(performance.now()/900)*.004;p=Object.assign({},p,GRIP,{hR:[GRIP.hR[0],GRIP.hR[1]+bob,GRIP.hR[2]],hL:[GRIP.hL[0],GRIP.hL[1]+bob,GRIP.hL[2]],tw:p.tw*.4,headP:p.headP+6})}\n    if(S.ld>.01&&S.clip==='idle'){")
r("const job=S.clip==='idle'?(S.lastJob||'reap'):S.clip;if(S.clip!=='idle')S.lastJob=S.clip;const busy=S.ld>.3||S.lw>.3;sickle.visible=!busy&&job==='reap';hatchet.visible=!busy&&(job==='chop'||job==='mine');",
  "sickle.visible=false;hatchet.visible=false;{const pL=U.palmL.getWorldPosition(V()),pR=U.palmR.getWorldPosition(V()),d=pR.clone().sub(pL),L=d.length()||1;d.multiplyScalar(1/L);oar.position.copy(pL).addScaledVector(d,(-.32+(p.slide||0))*sc);oar.quaternion.setFromUnitVectors(_Y,d);const hd=B.Head.getWorldPosition(V());U.eyeGlow.position.copy(hd).add(W(V(0,0,.05)).sub(W(V(0,0,0))));U.eyeGlow.material.opacity=.55+.25*Math.sin(performance.now()/300)}")
r("    if(S.hitNow==='chop'||S.hitNow==='mine'){chips(hatchet.userData.tip.getWorldPosition(V()),12)}","    if(S.hitNow==='pound'){const tp=oar.localToWorld(V(0,1.08,0));tp.y=.01*sc;for(let i=0;i<18;i++)mote(tp.clone(),V((Math.random()-.5)*1.1,.2+Math.random()*.5,(Math.random()-.5)*1.1).multiplyScalar(sc),Math.random()<.5?'#7fe0d0':'#c9b38a',.6);shake(.6)}\n    if(S.hitNow==='thrust'||S.hitNow==='rise'){const tp=oar.localToWorld(V(0,1.08,0));for(let i=0;i<8;i++)mote(tp.clone(),V((Math.random()-.5)*.5,.1+Math.random()*.3,(Math.random()-.5)*.5).multiplyScalar(sc),'#bff4ec',.45)}\n    if(S.hitNow==='sweep'){const tp=oar.localToWorld(V(0,1.08,0));for(let i=0;i<10;i++)mote(tp.clone(),V((Math.random()-.5)*.6,.15+Math.random()*.4,(Math.random()-.5)*.6).multiplyScalar(sc),Math.random()<.5?'#7fe0d0':'#bff4ec',.5)}\n    if(S.hitNow==='chop'||S.hitNow==='mine'){chips(hatchet.userData.tip.getWorldPosition(V()),12)}")
s=s.replace("const lanternGlow=egSprite(GLWT(),","const lanternGlow=egSprite(GLW,")

r("hwL:0,hwR:0,","hwL:0,hwR:0,slide:0,")
# the oar combo: a long spear thrust, a great rising sweep, then a two-handed pound into the ground
r("  const STANCE=()=>JSON.parse(JSON.stringify(ST));\"\"\")","  const STANCE=()=>JSON.parse(JSON.stringify(ST));\"\"\")",0) if False else None

open('fact_charon.js','w').write(s);print('ok',len(s))
