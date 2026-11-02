s=open('fact_charon.js').read()
def r(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:80]);s=s.replace(a,b)
r(s[:s.find("FACT.charon=function(){")],"// ---------- Electra (Greek): a winged fury on the shared Tripo rig with two added wing bones a side; she hovers, flaps, and fights with a burning lash; the awakened form is the serpent-crowned queen ----------\n")
r("FACT.charon=function(){const LAB=(typeof GLAB==='function')?GLAB('charon'):window.LABCFG;","FACT.fury=function(){const QU=FACT.__fu===1;const LAB=(typeof GLAB==='function')?GLAB(QU?'furyu':'fury'):window.LABCFG;")
r("const UPC=FACT.__chu===1;const G0=window.MODELS&&window.MODELS[UPC?'charonu':'charon']||window.MODELS.charon||window.MODELS.stoneb;","const UPC=false;const G0=window.MODELS&&window.MODELS[QU?'furyu':'fury']||window.MODELS.fury||window.MODELS.stoneb;")
r("oar.scale.setScalar(sc);SCN.add(oar);U.oar=oar;","oar.scale.setScalar(sc);SCN.add(oar);U.oar=oar;oar.visible=false;")
r("const lanternGlow=egSprite(GLW,.06,'#8fffd0');","const lanternGlow=egSprite(GLW,QU?.07:.05,QU?'#7dffb0':'#ff4a2a');")
r("slide:0,hgL:[0,0,0],hgR:[0,0,0]};","slide:0,hgL:[0,0,0],hgR:[0,0,0],wv:[-.1,-1,.15],wc:.18,wl:1,fa:26,fb:4,fs:8,ff:2.1,fly:1,airL:1,airR:1};")
r("bfL:[.07,-.4,0],bfR:[-.07,-.4,0]","bfL:[.06,-.43,-.05],bfR:[-.06,-.41,-.02]")
NEW=r"""  // ---- Electra's moves (chest frame: +z forward, +x her left). wv = where the lash points, wc = how much it curls, fa/fb/fs/ff = wing flap amount / lift / sweep back / beats per second, fly = hover height ----
  const HOV={hR:[-.15,-.06,.12],hL:[.15,-.02,.08],bR:[0,.2,1],bL:[0,.3,1],eR:[-.8,-.4,-.4],eL:[.8,-.4,-.4],wv:[-.35,-.7,.3],wc:.3};
  const H0=o=>Object.assign({},HOV,o||{});
  // LASH: the arm whips up and back over the shoulder, then cracks the lash straight down onto the target
  const LASH=[K(0,H0()),
    K(.26,{pitch:-10,tw:-24,bend:-6,headP:-8,hR:[-.1,SY+.24,-.1],hL:[.18,.02,.14],bR:[0,1,-.4],eR:[-1,.3,-.4],wv:[0,.4,-1],wc:.32,fa:40,fb:16,fs:-4,ff:2.6}),
    K(.42,{pitch:14,tw:16,bend:10,headP:8,hR:[-.04,SY-.02,.36],hL:[.16,-.06,.04],bR:[0,0,1],eR:[-.8,-.4,-.2],wv:[0,-.25,1],wc:.02,fa:30,fb:-6,fs:16,ff:2.6}),
    K(.56,{pitch:12,tw:12,bend:8,hR:[-.02,-.04,.34],wv:[0,-.6,1],wc:.08}),
    K(.95,H0())];
  // SLASH: a flat backhand sweep, the lash wheeling across in front of her
  const SLASH=[K(0,H0()),
    K(.24,{tw:-36,roll:-6,headY:24,hR:[-.34,SY-.06,.02],hL:[.2,-.02,.12],bR:[-1,.2,.2],eR:[-1,.4,-.3],wv:[-1,-.1,-.3],wc:.22,fa:34,fs:-6}),
    K(.4,{tw:34,roll:8,headY:-16,pitch:8,hR:[.24,SY-.1,.3],hL:[.18,-.06,0],bR:[1,0,.6],eR:[-.6,-.5,-.2],wv:[1,-.12,.55],wc:.05,fa:36,fs:14}),
    K(.56,{tw:40,roll:6,hR:[.3,SY-.16,.18],wv:[1,-.4,.1],wc:.14}),
    K(.92,H0())];
  // TALON: she tips forward and rakes with both feet, wings thrown up behind her
  const TALON=[K(0,H0()),
    K(.22,{pitch:-16,bend:-8,headP:-14,airL:1,airR:1,bfL:[.07,-.3,-.18],bfR:[-.07,-.3,-.16],hR:[-.2,SY-.02,-.08],hL:[.2,SY-.02,-.08],eR:[-1,.2,-.3],eL:[1,.2,-.3],fa:44,fb:22,fs:-10,ff:3,fly:1.25}),
    K(.4,{pitch:30,bend:16,headP:-18,airL:1,airR:1,bfL:[.07,-.28,.34],bfR:[-.07,-.33,.3],hR:[-.22,-.04,-.1],hL:[.22,-.04,-.1],fa:20,fb:30,fs:20,ff:3,fly:.7}),
    K(.56,{pitch:22,bend:12,airL:1,airR:1,bfL:[.07,-.34,.22],bfR:[-.07,-.38,.18],fly:.75}),
    K(.95,H0())];
  // WRATH (special): she climbs, spreads her wings wide and shrieks, then dives and cracks the lash into the ground
  const WRATH=[K(0,H0()),
    K(.5,{pitch:-14,bend:-12,headP:-30,hR:[-.3,SY+.16,.02],hL:[.3,SY+.16,.02],bR:[-1,1,0],bL:[1,1,0],eR:[-1,-.2,-.4],eL:[1,-.2,-.4],wv:[-.3,1,-.3],wc:.35,fa:12,fb:34,fs:-14,ff:1.2,fly:2.1}),
    K(.85,{pitch:-16,bend:-14,headP:-34,hR:[-.32,SY+.2,0],hL:[.32,SY+.2,0],bR:[-1,1,0],bL:[1,1,0],eR:[-1,-.2,-.4],eL:[1,-.2,-.4],wv:[-.3,1,-.4],wc:.4,fa:8,fb:38,fs:-16,ff:1,fly:2.2}),
    K(1.15,{pitch:40,bend:18,headP:10,hR:[-.1,SY+.18,-.06],hL:[.2,-.04,.1],bR:[0,1,-.4],eR:[-1,.3,-.4],wv:[0,.5,-1],wc:.3,fa:6,fb:-24,fs:34,ff:1,fly:1}),
    K(1.32,{pitch:30,bend:14,headP:12,hR:[-.04,-.06,.38],bR:[0,0,1],eR:[-.8,-.4,-.2],wv:[0,-.8,.6],wc:.02,fa:30,fb:0,fs:12,ff:2.6,fly:.45}),
    K(1.8,H0())];
  const STANCE=()=>JSON.parse(JSON.stringify(ST));"""
r("  const STANCE=()=>JSON.parse(JSON.stringify(ST));",NEW)
r("sweep:{dur:1,fn:t=>sampleKeys(SWEEP,t),hits:[[.42,1]]},","sweep:{dur:1,fn:t=>sampleKeys(SWEEP,t),hits:[[.42,1]]},lash:{dur:.95,fn:t=>sampleKeys(LASH,t),hits:[[.42,1]]},slash:{dur:.92,fn:t=>sampleKeys(SLASH,t),hits:[[.4,1]]},talon:{dur:.95,fn:t=>sampleKeys(TALON,t),hits:[[.4,1]]},wrath:{dur:1.8,fn:t=>sampleKeys(WRATH,t),hits:[[1.32,2]]},")
# hover instead of walking: lean into the flight, a slow bob, wings beating faster when she moves
r("    if(wk>0)p=mixP(p,walkPose(wph,S.bank),Math.min(1,wk*1.4));","    const fwk=S.wamt;")
r("    if(S.clip==='idle'){const bob=Math.sin(wph*2)*.006*wk+Math.sin(performance.now()/900)*.004;p=Object.assign({},p,GRIP,{hR:[GRIP.hR[0],GRIP.hR[1]+bob,GRIP.hR[2]],hL:[GRIP.hL[0],GRIP.hL[1]+bob,GRIP.hL[2]],tw:p.tw*.4,headP:p.headP+6})}",
  "    if(S.clip==='idle'){const nw=performance.now()/1000,s1=Math.sin(nw*2.1*TAU/2);p=Object.assign({},p,HOV,{hR:[HOV.hR[0],HOV.hR[1]+s1*.01,HOV.hR[2]],hL:[HOV.hL[0],HOV.hL[1]+s1*.01,HOV.hL[2]],pitch:4+fwk*18,bend:3+fwk*6,headP:-4-fwk*10+Math.sin(nw*.6)*4,headY:Math.sin(nw*.45)*14,roll:S.bank*.8,bfL:[.06,-.43,-.05-fwk*.12],bfR:[-.06,-.41,-.02-fwk*.14],fa:26+fwk*12,ff:2.1+fwk*.7,fs:8+fwk*10,wv:[-.35+Math.sin(nw*1.3)*.08,-.7,.3-fwk*.5]})}")
r("root.position.set(S.x,0,S.z);","S.fph=(S.fph||0)+dt*(p.ff||2)*TAU;root.position.set(S.x,((p.fly==null?1:p.fly)*.42+Math.sin(S.fph)*.025)*(LAB.mh||1),S.z);")
WING=r"""    for(const[b,q]of CURL)b.quaternion.multiply(q);
    // wings: Wing1 beats from the shoulder blade, Wing2 lags behind it so the tips trail and snap
    if(B.L_Wing1){const ph=S.fph,a1=rad(p.fb+p.fa*Math.sin(ph)),a2=rad(p.fa*.7*Math.sin(ph-.9)),sw=rad(p.fs+6*Math.cos(ph));const wq=rootQ.clone().multiply(chestQ),wf=_Z.clone().applyQuaternion(wq),wu=_Y.clone().applyQuaternion(wq);
      rotW(B.L_Wing1,wu,sw);rotW(B.L_Wing1,wf,-a1);rotW(B.L_Wing2,wf,-a2);rotW(B.R_Wing1,wu,-sw);rotW(B.R_Wing1,wf,a1);rotW(B.R_Wing2,wf,a2)}"""
r("    for(const[b,q]of CURL)b.quaternion.multiply(q);",WING)
LASHFX=r"""    // the lash: a chain of segments out of her right fist, aimed by wv and curled by wc, with a ripple running down it
    {const hp=U.palmR.getWorldPosition(V()),wq=rootQ.clone().multiply(chestQ);let dir=V(...p.wv).normalize().applyQuaternion(wq);const upW=_Y,nw=performance.now()/1000;let pt=hp.clone();
      for(let i=0;i<LN;i++){const ax=dir.clone().cross(upW);if(ax.lengthSq()<1e-4)ax.copy(_X.clone().applyQuaternion(wq));ax.normalize();const k=i/LN;dir.applyAxisAngle(ax,-(p.wc||0)*(1+k*1.2)+Math.sin(nw*7-i*.7)*.05*(1-p.wl*0));
        const nx=pt.clone().addScaledVector(dir,SEG*sc);const m=LSEG[i];m.position.copy(pt).lerp(nx,.5);m.quaternion.setFromUnitVectors(_Y,dir);m.scale.set(sc*(1-k*.6),sc,sc*(1-k*.6));LPTS[i+1].copy(nx);pt=nx}
      LPTS[0].copy(hp);U.lashTip=pt;ember.position.copy(pt);ember.material.opacity=.35+.25*Math.sin(nw*9)}
    // props by job"""
r("    // props by job",LASHFX)
PROPS=r"""  const STANCE0=1;
  // ---- the burning lash ----
  const LN=14,SEG=.052,LPTS=[];const lashM=M(QU?'#4fae4a':'#b8321c'),lashH=M(QU?'#ffd85a':'#ffb04a');for(const x of[lashM,lashH]){x.userData.outlineParameters={visible:false};U.mats.push(x)}
  const LSEG=[];for(let i=0;i<LN;i++){const m=new T.Mesh(new T.CylinderGeometry(.009,.011,SEG*1.05,5),i%3===2?lashH:lashM);SCN.add(m);LSEG.push(m);LPTS.push(V())}LPTS.push(V());U.lash=LSEG;
  const ember=egSprite(GLW,.1,QU?'#9dffb0':'#ffb04a');SCN.add(ember);"""
r("  const lanternGlow=",PROPS+"\n  const lanternGlow=")
FX=r"""    if(S.hitNow==='lash'||S.hitNow==='slash'||S.hitNow==='wrath'){const tp=(U.lashTip||U.palmR.getWorldPosition(V())).clone();const n=S.hitNow==='wrath'?26:10;if(S.hitNow==='wrath')tp.y=.01*sc;for(let i=0;i<n;i++)mote(tp.clone(),V((Math.random()-.5)*(S.hitNow==='wrath'?1.3:.5),.15+Math.random()*.5,(Math.random()-.5)*(S.hitNow==='wrath'?1.3:.5)).multiplyScalar(sc),QU?(Math.random()<.5?'#9dffb0':'#e8bf4e'):(Math.random()<.5?'#ff7a2a':'#ffd27a'),.55);shake(S.hitNow==='wrath'?.7:.12)}
    if(S.hitNow==='talon'){const tp=B.L_Foot.getWorldPosition(V());for(let i=0;i<8;i++)mote(tp.clone(),V((Math.random()-.5)*.5,.1+Math.random()*.3,(Math.random()-.5)*.5).multiplyScalar(sc),'#ffd9c0',.4);shake(.1)}
    if(S.clip==='wrath'&&S.t>.4&&S.t<1.05&&Math.random()<dt*24){const hd=B.Head.getWorldPosition(V());mote(hd,V((Math.random()-.5)*.9,(Math.random()-.3)*.5,(Math.random()-.5)*.9).multiplyScalar(sc),QU?'#7dffb0':'#ff4a2a',.5)}
    if(S.hitNow==='chop'||S.hitNow==='mine')"""
r("    if(S.hitNow==='chop'||S.hitNow==='mine')",FX)
open('fact_fury.js','w').write(s);print(len(s))
