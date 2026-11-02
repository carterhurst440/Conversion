s=open('fact_charon.js').read()
def r(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:80]);s=s.replace(a,b)
r(s[:s.find("FACT.charon=function(){")],"// ---------- the Sobek Guard (Egypt): a crocodile warrior on the shared Tripo rig with a bronze khopesh; hacks, hooks, bites, spins his tail round, and drags foes into a death roll; awakened he wears Sobek's gold ----------\n")
r("FACT.charon=function(){const LAB=(typeof GLAB==='function')?GLAB('charon'):window.LABCFG;","FACT.croc=function(){const AW=FACT.__cu===1;const LAB=(typeof GLAB==='function')?GLAB(AW?'crocu':'croc'):window.LABCFG;")
r("const UPC=FACT.__chu===1;const G0=window.MODELS&&window.MODELS[UPC?'charonu':'charon']||window.MODELS.charon||window.MODELS.stoneb;","const UPC=false;const G0=window.MODELS&&window.MODELS[AW?'crocu':'croc']||window.MODELS.croc||window.MODELS.stoneb;")
r("oar.scale.setScalar(sc);SCN.add(oar);U.oar=oar;","oar.scale.setScalar(sc);SCN.add(oar);U.oar=oar;oar.visible=false;")
r("const lanternGlow=egSprite(GLW,.06,'#8fffd0');","const lanternGlow=egSprite(GLW,AW?.05:.03,AW?'#ffd35a':'#e8a03a');")
# the khopesh: a short grip, then the long hooked bronze blade
KH=r"""  const khM=M(AW?'#f2c14e':'#c98a3c'),khD=M(AW?'#b8862a':'#7a5226'),khG=M(AW?'#2f8f9a':'#5a3e24');for(const x of[khM,khD,khG]){x.userData.outlineParameters={visible:false};U.mats.push(x)}
  const khop=new T.Group();{const h=new T.Mesh(new T.CylinderGeometry(.011,.012,.11,6),khG);h.position.y=.0;khop.add(h);const pm=new T.Mesh(new T.SphereGeometry(.017,8,6),khD);pm.position.y=-.06;khop.add(pm);const gd=new T.Mesh(new T.BoxGeometry(.06,.014,.026),khD);gd.position.y=.058;khop.add(gd);
    const sh=new T.Mesh(new T.BoxGeometry(.022,.13,.008),khM);sh.position.y=.13;khop.add(sh);
    const cv=new T.CatmullRomCurve3([V(0,.19,0),V(.012,.25,0),V(.05,.3,0),V(.1,.31,0),V(.14,.28,0),V(.15,.24,0)]);const bl=new T.Mesh(new T.TubeGeometry(cv,20,.019,5,false),khM);bl.scale.z=.3;khop.add(bl);
    const tip=new T.Group();tip.position.set(.15,.24,0);khop.add(tip);khop.userData.tip=tip}
  inHand('R',khop);U.khop=khop;"""
r("  inHand('R',hatchet);U.hatchet=hatchet;hatchet.visible=false;","  inHand('R',hatchet);U.hatchet=hatchet;hatchet.visible=false;\n"+KH)
NEW=r"""  // ---- the Sobek Guard's moves (chest frame: +z forward, +x his left) ----
  const CH={hR:[-.17,-.07,.12],hL:[.18,-.09,.07],bR:[0,1,.35],bL:[0,-.2,1],eR:[-.8,-.3,-.4],eL:[.8,-.3,-.4]};
  const C0=o=>Object.assign({p:[0,-.05,0],pitch:6,bend:4},CH,o||{});
  const FT={fL:[.085,ANK,.04],fyL:-10,lfL:.04,fR:[-.085,ANK,-.04],fyR:10,lfR:.04};
  // HACK: the khopesh hauled up over his shoulder, a step, and a heavy downward chop
  const HACK=carry([K(0,C0()),
    K(.3,{p:[0,-.02,-.04],pitch:-10,tw:-18,bend:-8,headP:-10,hR:[-.08,SY+.22,-.05],bR:[0,1,-.6],eR:[-1,.3,-.3],hL:[.2,.02,.16],eL:[.8,-.4,-.3]},{fL:[.09,ANK,.17],fyL:-8,lfL:.06}),
    K(.44,{p:[0,-.16,.1],pitch:24,tw:10,bend:14,headP:12,hR:[-.02,-.12,.38],bR:[0,-.4,1],eR:[-.8,-.3,-.3],hL:[.2,-.12,.1]}),
    K(.6,{p:[0,-.14,.08],pitch:20,tw:8,bend:12,hR:[-.03,-.14,.34],bR:[0,-.5,1]}),
    K(1,C0(),FT)]);
  // HOOK: wound right, then the hooked blade raked across in front of him
  const HOOK=carry([K(0,C0()),
    K(.26,{p:[0,-.07,-.03],tw:-40,pitch:2,headY:22,hR:[-.36,SY-.05,-.05],bR:[-1,.3,.2],eR:[-1,.4,-.3],hL:[.18,-.04,.2]},{fR:[-.1,ANK,-.12],fyR:26,lfR:.04}),
    K(.42,{p:[0,-.12,.06],tw:36,pitch:12,bend:8,headY:-14,hR:[.25,SY-.12,.33],bR:[1,0,.4],eR:[-.6,-.5,-.2],hL:[.2,-.08,0]},{fL:[.1,ANK,.15],fyL:-12,lfL:.05}),
    K(.58,{p:[0,-.1,.04],tw:44,pitch:10,hR:[.32,SY-.18,.16],bR:[1,-.3,0]}),
    K(.95,C0(),FT)]);
  // CHOMP: he rears back, claws up, then throws his whole body forward jaws-first
  const CHOMP=carry([K(0,C0()),
    K(.26,{p:[0,0,-.06],pitch:-14,bend:-10,headP:-26,hR:[-.22,SY+.02,.1],hL:[.22,SY+.02,.1],bR:[0,1,.3],bL:[0,1,.3],eR:[-1,-.2,-.3],eL:[1,-.2,-.3]}),
    K(.4,{p:[0,-.18,.16],pitch:30,bend:16,headP:26,hR:[-.14,-.06,.34],hL:[.14,-.06,.34],bR:[0,-.4,1],bL:[0,-.4,1],eR:[-1,-.3,-.2],eL:[1,-.3,-.2]},{fL:[.09,ANK,.24],fyL:-8,lfL:.06}),
    K(.56,{p:[0,-.16,.13],pitch:26,bend:14,headP:20,hR:[-.15,-.08,.3],hL:[.15,-.08,.3]}),
    K(.95,C0(),FT)]);
  // SPIN: a full turn on the spot, the tail sweeping round low through everything behind and beside him, khopesh trailing
  const SPIN=carry([K(0,C0()),
    K(.18,{p:[0,-.12,0],yaw:28,tw:14,pitch:12,bend:8,headY:-10,hR:[.1,-.06,.3],bR:[1,0,.4],hL:[.22,-.04,-.04]}),
    K(.42,{p:[0,-.16,0],yaw:-190,tw:-10,pitch:14,bend:10,headY:20,hR:[-.34,SY-.14,-.02],bR:[-1,.2,0],hL:[.28,SY-.12,.02],bL:[1,.2,0]},{fL:[.09,ANK,.0],fyL:-100,lfL:.03,fR:[-.09,ANK,-.0],fyR:-80,lfR:.03}),
    K(.62,{p:[0,-.12,0],yaw:-350,tw:-6,pitch:10,bend:8,hR:[-.24,-.06,.18],hL:[.2,-.08,.08]},{fL:[.085,ANK,.04],fyL:-370,lfL:.03,fR:[-.085,ANK,-.04],fyR:-350,lfR:.03}),
    K(1,C0({yaw:-360}),{fL:[.085,ANK,.04],fyL:-370,lfL:.0,fR:[-.085,ANK,-.04],fyR:-350,lfR:.0})]);
  // ROLL (special): a lunge, jaws and arms clamp on, and he throws himself into a death roll, twisting over and over
  const RL={p:[0,-.24,.14],pitch:38,bend:14,headP:22,hR:[-.06,-.16,.34],hL:[.06,-.16,.34],bR:[0,-.4,1],bL:[0,-.4,1],eR:[-1,-.2,-.3],eL:[1,-.2,-.3],airL:1,airR:1,bfL:[.08,-.36,-.2],bfR:[-.08,-.36,-.2]};
  const ROLL=carry([K(0,C0()),
    K(.25,{p:[0,-.1,-.04],pitch:-8,headP:-20,hR:[-.24,SY,.12],hL:[.24,SY,.12],bR:[0,1,.3],bL:[0,1,.3],eR:[-1,-.2,-.3],eL:[1,-.2,-.3]},{fL:[.09,ANK,.2],fyL:-8,lfL:.06}),
    K(.42,Object.assign({},RL,{roll:0})),
    K(.9,Object.assign({},RL,{roll:-240,p:[0,-.3,.14]})),
    K(1.35,Object.assign({},RL,{roll:-480,p:[0,-.3,.14]})),
    K(1.62,Object.assign({},RL,{roll:-720})),
    K(1.95,C0({roll:-720}),FT)]);
  const STANCE=()=>JSON.parse(JSON.stringify(ST));"""
r("  const STANCE=()=>JSON.parse(JSON.stringify(ST));",NEW)
r("sweep:{dur:1,fn:t=>sampleKeys(SWEEP,t),hits:[[.42,1]]},","sweep:{dur:1,fn:t=>sampleKeys(SWEEP,t),hits:[[.42,1]]},hack:{dur:1,fn:t=>sampleKeys(HACK,t),hits:[[.44,1.2]]},hook:{dur:.95,fn:t=>sampleKeys(HOOK,t),hits:[[.42,1]]},chomp:{dur:.95,fn:t=>sampleKeys(CHOMP,t),hits:[[.4,1.1]]},spin:{dur:1,fn:t=>sampleKeys(SPIN,t),hits:[[.42,1]]},roll:{dur:1.95,fn:t=>sampleKeys(ROLL,t),hits:[[.7,1],[1.15,1],[1.6,1.4]]},")
r("let wph=0;const STRIDE=1.12,","let wph=0;const STRIDE=1.0,")
r("    if(S.clip==='idle'){const bob=Math.sin(wph*2)*.006*wk+Math.sin(performance.now()/900)*.004;p=Object.assign({},p,GRIP,{hR:[GRIP.hR[0],GRIP.hR[1]+bob,GRIP.hR[2]],hL:[GRIP.hL[0],GRIP.hL[1]+bob,GRIP.hL[2]],tw:p.tw*.4,headP:p.headP+6})}",
  "    if(S.clip==='idle'){const nw=performance.now()/1000,bob=Math.sin(wph*2)*.008*wk+Math.sin(nw*1.2)*.005,sw=Math.sin(wph)*.04*wk;p=Object.assign({},p,CH,{hR:[CH.hR[0],CH.hR[1]+bob-sw*.3,CH.hR[2]+sw],hL:[CH.hL[0],CH.hL[1]+bob+sw*.3,CH.hL[2]-sw],tw:p.tw*.5,pitch:p.pitch+5,bend:p.bend+3,headP:p.headP+2+Math.sin(nw*.5)*3,headY:p.headY*.6+Math.sin(nw*.4)*10})}")
# keep the yaw/roll keys whole (a full spin and a double roll are meant to go all the way round)
r("if(/^(yaw|fyL|fyR)$/.test(k))y=y+360*Math.round((x-y)/360);","if(/^(yaw|fyL|fyR|roll)$/.test(k))y=y+360*Math.round((x-y)/360);")
FX=r"""    if(S.hitNow==='hack'||S.hitNow==='hook'){const tp=khop.userData.tip.getWorldPosition(V());for(let i=0;i<9;i++)mote(tp.clone(),V((Math.random()-.5)*.6,.15+Math.random()*.4,(Math.random()-.5)*.6).multiplyScalar(sc),AW?(Math.random()<.5?'#ffd35a':'#fff3c0'):(Math.random()<.5?'#e8b45a':'#fff3c0'),.45);shake(S.hitNow==='hack'?.25:.12)}
    if(S.hitNow==='chomp'){const hd=B.Head.getWorldPosition(V());for(let i=0;i<8;i++)mote(hd.clone(),V((Math.random()-.5)*.5,.05+Math.random()*.3,(Math.random()-.5)*.5).multiplyScalar(sc),'#f4f0e0',.4);shake(.18)}
    if(S.hitNow==='spin'||S.clip==='roll'&&S.t>.45&&S.t<1.62&&Math.random()<dt*26){const hp=V(S.x,.01*sc,S.z);for(let i=0;i<(S.hitNow==='spin'?14:2);i++){const a=Math.random()*TAU,rr=(.1+Math.random()*.3)*sc;mote(V(hp.x+Math.cos(a)*rr,hp.y,hp.z+Math.sin(a)*rr),V(Math.cos(a)*.4,.3+Math.random()*.4,Math.sin(a)*.4).multiplyScalar(sc),Math.random()<.5?'#d9c49a':'#8fd0e0',.55)}if(S.hitNow==='spin')shake(.15)}
    if(S.hitNow==='roll'){shake(.3)}
    if(S.hitNow==='chop'||S.hitNow==='mine')"""
r("    if(S.hitNow==='chop'||S.hitNow==='mine')",FX)
open('fact_croc.js','w').write(s);print(len(s))
