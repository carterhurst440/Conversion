s=open('fact_charon.js').read()
def r(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:80]);s=s.replace(a,b)
r(s[:s.find("FACT.charon=function(){")],"// ---------- the Mummy (Egypt) and the Mega Mummy it can rise as: Tripo rig, a shambling arms-out walk, clawing and grabbing; the Mega Mummy smashes with both fists and climbs out of the sand ----------\n")
r("FACT.charon=function(){const LAB=(typeof GLAB==='function')?GLAB('charon'):window.LABCFG;","FACT.mumm=function(){const MG=FACT.__mg===1;const LAB=(typeof GLAB==='function')?GLAB(MG?'mega':'mumm'):window.LABCFG;")
r("const UPC=FACT.__chu===1;const G0=window.MODELS&&window.MODELS[UPC?'charonu':'charon']||window.MODELS.charon||window.MODELS.stoneb;","const UPC=false;const G0=window.MODELS&&window.MODELS[MG?'mega':'mumm']||window.MODELS.mumm||window.MODELS.stoneb;")
# clip everything below the ground so he can sink into and climb out of the sand
r("const mat=M('#ffffff',{map:mp,skinning:true,gradientMap:soft});","const mat=M('#ffffff',{map:mp,skinning:true,gradientMap:soft});mat.clippingPlanes=[GCLIP];")
r("  src.updateMatrixWorld(true);const box=new T.Box3();","  const GCLIP=new T.Plane(new T.Vector3(0,1,0),0);try{if(typeof renderer!=='undefined')renderer.localClippingEnabled=true}catch(e){}\n  src.updateMatrixWorld(true);const box=new T.Box3();")
r("oar.scale.setScalar(sc);SCN.add(oar);U.oar=oar;","oar.scale.setScalar(sc);SCN.add(oar);U.oar=oar;oar.visible=false;")
r("const lanternGlow=egSprite(GLW,.06,'#8fffd0');","const lanternGlow=egSprite(GLW,MG?.1:.05,MG?'#5ff0d8':'#9fd0ff');")
r("slide:0,hgL:[0,0,0],hgR:[0,0,0]};","slide:0,hgL:[0,0,0],hgR:[0,0,0],sink:0};")
NEW=r"""  // ---- the mummy's moves (chest frame: +z forward, +x his left, y from the pelvis) ----
  const ARMS=MG?{hR:[-.2,-.13,.13],hL:[.2,-.13,.13],bR:[-.3,-1,.4],bL:[.3,-1,.4],eR:[-1,.2,-.3],eL:[1,.2,-.3]}:{hR:[-.09,SY-.05,.3],hL:[.1,SY-.03,.31],bR:[0,-.25,1],bL:[0,-.25,1],eR:[-1,-.3,0],eL:[1,-.3,0]};
  const A0=o=>Object.assign({p:[0,-.04,0]},ARMS,o||{});
  const FT={fL:[.075,ANK,.03],fyL:-8,lfL:.04,fR:[-.075,ANK,-.03],fyR:8,lfR:.04};
  // CLAW: both arms raised high, then raked down across the target
  const CLAW=carry([K(0,A0()),
    K(.3,{p:[0,0,-.03],pitch:-8,bend:-8,headP:-10,hR:[-.1,SY+.18,.12],hL:[.1,SY+.18,.12],bR:[0,1,.3],bL:[0,1,.3],eR:[-1,.2,-.3],eL:[1,.2,-.3]},{fL:[.08,ANK,.14],fyL:-8,lfL:.05}),
    K(.46,{p:[0,-.14,.08],pitch:20,bend:14,headP:14,hR:[-.08,-.12,.34],hL:[.08,-.12,.34],bR:[0,-1,.4],bL:[0,-1,.4],eR:[-1,-.2,-.2],eL:[1,-.2,-.2]}),
    K(.62,{p:[0,-.12,.06],pitch:16,bend:12,headP:10,hR:[-.1,-.16,.28],hL:[.1,-.16,.28],bR:[0,-1,.4],bL:[0,-1,.4]}),
    K(.95,A0(),FT)]);
  // GRAB: arms flung wide, a lunge, both hands clamp on and drag the victim in
  const GRAB=carry([K(0,A0()),
    K(.22,{p:[0,-.05,-.04],pitch:-4,tw:0,headP:-6,hR:[-.24,SY-.04,-.02],hL:[.24,SY-.04,-.02],bR:[-1,0,.5],bL:[1,0,.5],eR:[-1,-.2,-.4],eL:[1,-.2,-.4]}),
    K(.42,{p:[0,-.13,.12],pitch:16,bend:8,headP:6,hR:[-.05,SY-.07,.43],hL:[.05,SY-.07,.43],bR:[1,0,1],bL:[-1,0,1],eR:[-1,-.3,0],eL:[1,-.3,0]},{fL:[.08,ANK,.2],fyL:-6,lfL:.05}),
    K(.62,{p:[0,-.08,.03],pitch:10,bend:6,headP:18,hR:[-.04,SY-.03,.2],hL:[.04,SY-.03,.2],bR:[1,0,1],bL:[-1,0,1]}),
    K(1,A0(),FT)]);
  // FLAIL: wild alternating swipes, right then left
  const FLAIL=carry([K(0,A0()),
    K(.18,{p:[0,-.05,0],tw:-26,headY:16,hR:[-.3,SY,.05],hL:[.12,SY-.08,.22],bR:[-1,.3,.2],eR:[-1,.4,-.3]}),
    K(.3,{p:[0,-.09,.05],tw:24,pitch:8,headY:-10,hR:[.12,-.04,.32],hL:[.18,SY-.06,.1],bR:[1,-.2,.5],eR:[-.7,-.5,-.2]},{fR:[-.08,ANK,.08],fyR:10,lfR:.04}),
    K(.46,{p:[0,-.05,0],tw:26,headY:-16,hL:[.3,SY,.05],hR:[-.12,SY-.08,.2],bL:[1,.3,.2],eL:[1,.4,-.3]}),
    K(.6,{p:[0,-.09,.05],tw:-24,pitch:8,headY:10,hL:[-.12,-.04,.32],hR:[-.16,SY-.06,.1],bL:[-1,-.2,.5],eL:[.7,-.5,-.2]},{fL:[.08,ANK,.12],fyL:-10,lfL:.04}),
    K(.95,A0(),FT)]);
  // SMASH (Mega): both fists hauled high over the head, a step, and a crushing double-fisted slam into the ground
  const SMASH=carry([K(0,A0()),
    K(.38,{p:[0,.03,-.05],pitch:-14,bend:-12,headP:-20,hR:[-.05,SY+.3,.0],hL:[.05,SY+.3,.0],bR:[0,1,-.3],bL:[0,1,-.3],eR:[-1,.2,-.3],eL:[1,.2,-.3]},{fL:[.09,ANK,.18],fyL:-8,lfL:.07}),
    K(.66,{p:[0,-.26,.12],pitch:32,bend:22,headP:16,hR:[-.04,-.32,.4],hL:[.04,-.32,.4],bR:[0,-1,.3],bL:[0,-1,.3],eR:[-1,.2,-.2],eL:[1,.2,-.2]}),
    K(.85,{p:[0,-.24,.1],pitch:28,bend:20,headP:12,hR:[-.05,-.3,.38],hL:[.05,-.3,.38],bR:[0,-1,.3],bL:[0,-1,.3]}),
    K(1.25,A0(),FT)]);
  // HAY (Mega): a huge looping right haymaker, the whole body thrown behind it
  const HAY=carry([K(0,A0()),
    K(.3,{p:[0,-.06,-.04],tw:-40,pitch:-2,headY:22,hR:[-.34,SY+.04,-.12],hL:[.18,-.02,.2],bR:[-1,.5,-.3],eR:[-1,.5,-.4],eL:[1,-.4,-.3]},{fR:[-.1,ANK,-.12],fyR:26,lfR:.04}),
    K(.46,{p:[0,-.14,.08],tw:34,pitch:12,bend:10,headY:-14,hR:[.14,SY-.04,.36],hL:[.2,-.08,.04],bR:[1,0,.6],eR:[-.6,-.4,-.2]},{fL:[.1,ANK,.16],fyL:-12,lfL:.05}),
    K(.62,{p:[0,-.12,.06],tw:42,pitch:10,bend:8,hR:[.24,SY-.12,.2],hL:[.2,-.1,0]}),
    K(1.05,A0(),FT)]);
  // DOWN: the body sinks into the sand (the basic Mummy) / lies buried with only the hands clawing at the surface (the Mega Mummy)
  const DOWN=MG?carry([K(0,{sink:.96,p:[0,-.04,0],hR:[-.12,SY+.34,.1],hL:[.12,SY+.3,.12],bR:[0,1,.2],bL:[0,1,.2],eR:[-1,.2,-.2],eL:[1,.2,-.2],headP:-20}),K(.6,{sink:.96,p:[0,-.04,0],hR:[-.1,SY+.3,.14],hL:[.14,SY+.34,.08],bR:[0,1,.2],bL:[0,1,.2],eR:[-1,.2,-.2],eL:[1,.2,-.2],headP:-20}),K(1.2,{sink:.96,p:[0,-.04,0],hR:[-.12,SY+.34,.1],hL:[.12,SY+.3,.12],bR:[0,1,.2],bL:[0,1,.2],eR:[-1,.2,-.2],eL:[1,.2,-.2],headP:-20})])
    :carry([K(0,A0()),K(.35,{p:[0,-.3,.06],pitch:30,bend:24,headP:34,roll:6,hR:[-.13,-.44,.2],hL:[.12,-.42,.22],bR:[0,-1,.2],bL:[0,-1,.2],eR:[-1,.2,-.3],eL:[1,.2,-.3]},{fL:[.09,ANK,.14],fyL:-8,lfL:.04}),K(1.1,Object.assign({p:[0,-.3,.06],pitch:30,bend:24,headP:34,roll:6,hR:[-.13,-.44,.2],hL:[.12,-.42,.22],bR:[0,-1,.2],bL:[0,-1,.2],eR:[-1,.2,-.3],eL:[1,.2,-.3]},{sink:.06}))]);
  const SLUMP={p:[0,-.3,.06],pitch:30,bend:24,headP:34,roll:6,hR:[-.13,-.44,.2],hL:[.12,-.42,.22],bR:[0,-1,.2],bL:[0,-1,.2],eR:[-1,.2,-.3],eL:[1,.2,-.3]};
  // RISE: claws out of the sand, hauls itself up and stands with a roar
  const RISEB=carry([K(0,Object.assign({},SLUMP,{sink:.06}),{fL:[.09,ANK,.14],fyL:-8}),K(.45,{p:[0,-.2,.03],pitch:18,bend:14,headP:12,hR:[-.12,-.2,.24],hL:[.12,-.2,.24],bR:[0,-1,.4],bL:[0,-1,.4],eR:[-1,.2,-.2],eL:[1,.2,-.2]}),K(.85,{p:[0,0,-.02],pitch:-8,bend:-8,headP:-18,hR:[-.26,SY+.1,.06],hL:[.26,SY+.1,.06],bR:[-1,1,0],bL:[1,1,0],eR:[-1,-.2,-.4],eL:[1,-.2,-.4]}),K(1.2,A0(),FT)]);
  const RISEU=carry([K(0,{sink:.96,p:[0,-.04,0],hR:[-.12,SY+.34,.1],hL:[.12,SY+.3,.12],bR:[0,1,.2],bL:[0,1,.2],eR:[-1,.2,-.2],eL:[1,.2,-.2],headP:-20}),
    K(.35,{sink:.6,p:[0,-.04,0],pitch:10,headP:-10,hR:[-.2,SY+.08,.24],hL:[.2,SY+.1,.22],bR:[0,-1,.6],bL:[0,-1,.6],eR:[-1,.2,-.2],eL:[1,.2,-.2]}),
    K(.75,{sink:.22,p:[0,-.12,.02],pitch:22,bend:14,headP:6,hR:[-.18,-.2,.26],hL:[.18,-.2,.26],bR:[0,-1,.5],bL:[0,-1,.5],eR:[-1,.2,-.2],eL:[1,.2,-.2]}),
    K(1.05,{sink:0,p:[0,-.02,-.02],pitch:-10,bend:-10,headP:-22,hR:[-.3,SY+.12,.04],hL:[.3,SY+.12,.04],bR:[-1,1,0],bL:[1,1,0],eR:[-1,-.2,-.4],eL:[1,-.2,-.4]}),
    K(1.4,A0(),FT)]);
  const STANCE=()=>JSON.parse(JSON.stringify(ST));"""
r("  const STANCE=()=>JSON.parse(JSON.stringify(ST));",NEW)
r("sweep:{dur:1,fn:t=>sampleKeys(SWEEP,t),hits:[[.42,1]]},","sweep:{dur:1,fn:t=>sampleKeys(SWEEP,t),hits:[[.42,1]]},claw:{dur:.95,fn:t=>sampleKeys(CLAW,t),hits:[[.46,1]]},grab:{dur:1,fn:t=>sampleKeys(GRAB,t),hits:[[.42,1]]},flail:{dur:.95,fn:t=>sampleKeys(FLAIL,t),hits:[[.3,1],[.6,1]]},smash:{dur:1.25,fn:t=>sampleKeys(SMASH,t),hits:[[.66,1.6]]},hay:{dur:1.05,fn:t=>sampleKeys(HAY,t),hits:[[.46,1.2]]},down:{dur:1.2,loop:MG,fn:t=>sampleKeys(DOWN,t)},rise:{dur:MG?1.4:1.2,fn:t=>sampleKeys(MG?RISEU:RISEB,t)},")
r("let wph=0;const STRIDE=1.12,","let wph=0;const STRIDE=MG?1.0:.8,")
# idle and walk: arms out (basic) / heavy hanging fists (Mega), a dragging right foot and a lurching sway
r("    if(S.clip==='idle'){const bob=Math.sin(wph*2)*.006*wk+Math.sin(performance.now()/900)*.004;p=Object.assign({},p,GRIP,{hR:[GRIP.hR[0],GRIP.hR[1]+bob,GRIP.hR[2]],hL:[GRIP.hL[0],GRIP.hL[1]+bob,GRIP.hL[2]],tw:p.tw*.4,headP:p.headP+6})}",
  "    if(S.clip==='idle'){const nw=performance.now()/1000,bob=Math.sin(wph*2)*.008*wk+Math.sin(nw*1.1)*.006,sw=Math.sin(wph)*.03*wk;p=Object.assign({},p,ARMS,{hR:[ARMS.hR[0],ARMS.hR[1]+bob+sw,ARMS.hR[2]+sw*.5],hL:[ARMS.hL[0],ARMS.hL[1]+bob-sw,ARMS.hL[2]-sw*.5],tw:p.tw*.35,pitch:p.pitch+(MG?10:4),bend:p.bend+(MG?8:3),headP:p.headP+(MG?2:10)+Math.sin(nw*.7)*4,headY:p.headY*.5+Math.sin(nw*.5)*12,roll:p.roll+(MG?2:5)*Math.sin(wph)*wk+Math.sin(nw*.8)*1.5});if(wk>0){p.fR=p.fR.slice();p.fR[1]=ANK+(p.fR[1]-ANK)*(MG?.75:.3);p.ptR=(p.ptR||0)*.4}}")
r("root.position.set(S.x,0,S.z);","root.position.set(S.x,-(p.sink||0)*(LAB.mh||1)*1.04,S.z);")
FX=r"""    if(S.hitNow==='smash'){const a=U.palmL.getWorldPosition(V()),b=U.palmR.getWorldPosition(V()),hp=a.lerp(b,.5);hp.y=.01*sc;for(let i=0;i<22;i++)mote(hp.clone(),V((Math.random()-.5)*1.3,.25+Math.random()*.6,(Math.random()-.5)*1.3).multiplyScalar(sc),Math.random()<.5?'#d9c49a':'#5ff0d8',.65);shake(.7)}
    if(S.hitNow==='claw'||S.hitNow==='grab'||S.hitNow==='flail'||S.hitNow==='hay'){const hp=U.palmR.getWorldPosition(V());for(let i=0;i<7;i++)mote(hp.clone(),V((Math.random()-.5)*.5,.1+Math.random()*.3,(Math.random()-.5)*.5).multiplyScalar(sc),MG?'#5ff0d8':'#e8dcc0',.45);shake(MG?.35:.08)}
    if((S.clip==='rise'&&S.t<1.0)||(S.clip==='down'&&!MG&&S.t>.3&&S.t<1.1)){if(Math.random()<dt*30){const a=Math.random()*TAU,rr=(.06+Math.random()*.12)*sc;mote(V(S.x+Math.cos(a)*rr,.01*sc,S.z+Math.sin(a)*rr),V(Math.cos(a)*.3,.35+Math.random()*.4,Math.sin(a)*.3).multiplyScalar(sc),Math.random()<.6?'#d9c49a':'#b89f6a',.6)}}
    if(S.hitNow==='chop'||S.hitNow==='mine')"""
r("    if(S.hitNow==='chop'||S.hitNow==='mine')",FX)
open('fact_mum.js','w').write(s);print(len(s))
