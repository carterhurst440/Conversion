s=open('fact_vdruid.js').read()
def r(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:80]);s=s.replace(a,b)
r(s[:s.find("FACT.vdruid=function(){")],"// ---------- Stonebearer (Egyptian worker): same Tripo rig and pose system as the Verdant Druid; farms with a bronze sickle, quarries with a stone maul,\n// draws water hand over hand from the Well, and carries his loads home: sandstone blocks lifted overhead, water in a jar on the shoulder ----------\n")
r("FACT.vdruid=function(){const LAB=(typeof GLAB==='function')?GLAB('vdruid'):window.LABCFG;const UP=LAB.form==='up'||FACT.__up===1;const G0=UP?(window.MODELS&&window.MODELS.adruid||window.TRIPO2):(window.MODELS&&window.MODELS.vdruid||window.TRIPO);",
  "FACT.stoneb=function(){const LAB=(typeof GLAB==='function')?GLAB('stoneb'):window.LABCFG;const UP=false;const G0=window.MODELS&&window.MODELS[FACT.__sbm||'stoneb']||window.MODELS.stoneb;")
# bronze sickle, stone maul instead of the hatchet
r("const goldM=M('#e2b64e'),goldD=M('#a8822e'),woodM=M('#6e4a2c'),ironM=M('#9aa0aa')","const goldM=M('#c98a3c'),goldD=M('#8a5a26'),woodM=M('#6e4a2c'),ironM=M('#d9b77a')")
r("const hd=new T.Mesh(new T.BoxGeometry(.06,.03,.012),ironM);hd.position.set(.022,.135,0);hatchet.add(hd);",
  "const hd=new T.Mesh(new T.BoxGeometry(.075,.045,.045),ironM);hd.position.set(.0,.15,0);hatchet.add(hd);")
r("const ed=new T.Mesh(new T.CylinderGeometry(.024,.024,.012,10,1,false,0,Math.PI),ironM);ed.rotation.x=Math.PI/2;ed.rotation.z=-Math.PI/2;ed.position.set(.05,.135,0);hatchet.add(ed);const tipH=new T.Group();tipH.position.set(.06,.135,0);",
  "const tipH=new T.Group();tipH.position.set(.04,.15,0);")
r("const m=new T.Mesh(new T.BoxGeometry(.018,.008,.01),i%3?woodM:M('#c9a06a'));","const m=new T.Mesh(new T.BoxGeometry(.016,.012,.012),i%3?M('#e8cf9a'):M('#b98c56'));")
# loads: the sandstone block (carved), a water jar, a bucket on a rope for the well
r("  U.chips=chips;",r"""  U.chips=chips;
  const blockTex=(()=>{const c=document.createElement('canvas');c.width=256;c.height=128;const g=c.getContext('2d');g.fillStyle='#e6c88e';g.fillRect(0,0,256,128);
    for(let i=0;i<260;i++){g.fillStyle=Math.random()<.5?'rgba(190,150,90,.35)':'rgba(255,240,200,.35)';g.fillRect(Math.random()*256,Math.random()*128,2+Math.random()*5,1+Math.random()*3)}
    g.strokeStyle='rgba(150,110,60,.7)';g.lineWidth=3;g.strokeRect(14,14,228,100);g.strokeStyle='rgba(130,92,48,.85)';g.lineWidth=4;
    g.beginPath();g.arc(48,42,9,0,TAU);g.moveTo(48,51);g.lineTo(48,92);g.moveTo(34,62);g.lineTo(62,62);for(const y of[74,84])g.moveTo(40,y),g.lineTo(56,y);
    g.moveTo(90,60);g.quadraticCurveTo(140,26,188,40);g.moveTo(90,60);g.quadraticCurveTo(140,50,188,58);g.moveTo(150,46);g.lineTo(152,96);g.moveTo(140,96);g.lineTo(164,96);g.moveTo(200,70);g.arc(206,72,7,Math.PI,0);g.moveTo(213,74);g.lineTo(206,96);g.stroke();
    g.strokeStyle='rgba(120,84,44,.5)';g.lineWidth=2;g.beginPath();g.moveTo(0,20);g.lineTo(30,34);g.lineTo(18,70);g.moveTo(256,96);g.lineTo(226,108);g.moveTo(120,128);g.lineTo(132,108);g.stroke();const t=new T.CanvasTexture(c);t.encoding=T.LinearEncoding;return t})();
  const sandM=M('#ffffff',{map:blockTex}),sandS=M('#d6b47a'),jarM=M('#b8653a'),jarD=M('#8a4626'),ropeM=M('#a3824f'),waterM=M('#5fb4e6');for(const x of[sandM,sandS,jarM,jarD,ropeM,waterM]){x.userData.outlineParameters={visible:false};U.mats.push(x)}
  const block=new T.Group();{const g=new T.BoxGeometry(.56,.2,.22);const m=new T.Mesh(g,[sandS,sandS,sandS,sandS,sandM,sandM]);block.add(m);for(const[x,y,z]of[[.2,.07,.09],[-.21,-.06,-.08],[.12,-.08,.1]]){const ch=new T.Mesh(new T.BoxGeometry(.04,.03,.03),sandS);ch.position.set(x,y,z);ch.rotation.set(.4,.6,.2);block.add(ch)}}
  block.scale.setScalar(sc);block.visible=false;SCN.add(block);U.block=block;
  const jar=new T.Group();{const pts=[V(0,0),V(.03,.005),V(.05,.04),V(.052,.08),V(.035,.115),V(.02,.13),V(.026,.145)].map(p=>new T.Vector2(p.x,p.y));const m=new T.Mesh(new T.LatheGeometry(pts,14),jarM);jar.add(m);const band=new T.Mesh(new T.TorusGeometry(.051,.005,6,16),jarD);band.rotation.x=Math.PI/2;band.position.y=.07;jar.add(band);const w=new T.Mesh(new T.CircleGeometry(.02,10),waterM);w.rotation.x=-Math.PI/2;w.position.y=.143;jar.add(w)}
  jar.scale.setScalar(sc);jar.visible=false;SCN.add(jar);
  const bucket=new T.Group();{const m=new T.Mesh(new T.CylinderGeometry(.035,.028,.05,12,1,true),woodM);m.material.side=T.DoubleSide;bucket.add(m);const w=new T.Mesh(new T.CircleGeometry(.032,12),waterM);w.rotation.x=-Math.PI/2;w.position.y=.015;bucket.add(w)}
  bucket.scale.setScalar(sc);bucket.visible=false;SCN.add(bucket);
  const rope=new T.Mesh(new T.CylinderGeometry(.004,.004,1,5),ropeM);rope.visible=false;SCN.add(rope);""")
# work clips: MINE (the maul), DRAW (hand over hand at the well), PUNCH (a scrapper's jab-hook)
r("  function hermite(k,i,t,key){",r"""  const DRAW_K=carry([K(0,{p:[0,-.08,.02],pitch:10,bend:8,headP:18,hL:[.06,.1,.22],hR:[-.05,-.04,.22],bL:[0,1,.2],bR:[0,1,.2],eL:[.8,-.4,-.4],eR:[-.8,-.4,-.4]},{fL:[.09,ANK,.1],fyL:-10,fR:[-.08,ANK,-.06],fyR:12}),
    K(.3,{p:[0,-.12,0],pitch:6,bend:6,headP:14,hL:[.06,-.06,.16],hR:[-.05,.12,.24],bL:[0,1,.2],bR:[0,1,.2],eL:[.8,-.4,-.4],eR:[-.8,-.4,-.4]}),
    K(.6,{p:[0,-.08,.02],pitch:10,bend:8,headP:18,hL:[.06,.1,.22],hR:[-.05,-.04,.22],bL:[0,1,.2],bR:[0,1,.2],eL:[.8,-.4,-.4],eR:[-.8,-.4,-.4]})]);
  const PUNCH=carry([K(0,{p:[0,-.06,0],tw:-14,hL:[.08,SY-.02,.14],hR:[-.08,SY-.04,.1],bL:[0,1,.3],bR:[0,1,.3],eL:[.9,-.6,-.2],eR:[-.9,-.6,-.2]},{fL:[.08,ANK,.1],fyL:-14,fR:[-.08,ANK,-.08],fyR:18}),
    K(.18,{p:[0,-.07,.04],tw:22,pitch:8,hL:[.08,SY-.02,.14],hR:[-.0,SY-.02,.36],bR:[0,0,1],eR:[-.9,-.3,-.2]}),
    K(.36,{p:[0,-.06,.02],tw:-26,pitch:6,hL:[.02,SY,.33],bL:[0,0,1],eL:[1,.3,-.2],hR:[-.08,SY-.04,.12]}),
    K(.62,{p:[0,-.06,0],tw:-14,hL:[.08,SY-.02,.14],hR:[-.08,SY-.04,.1],bL:[0,1,.3],bR:[0,1,.3],eL:[.9,-.6,-.2],eR:[-.9,-.6,-.2]})]);
  function hermite(k,i,t,key){""")
r("chop:{dur:1.1,fn:t=>sampleKeys(CHOP,t),hits:[[.44,1]]},","chop:{dur:1.1,fn:t=>sampleKeys(CHOP,t),hits:[[.44,1]]},mine:{dur:1.1,fn:t=>sampleKeys(CHOP,t),hits:[[.44,1]]},draw:{dur:.6,loop:true,fn:t=>sampleKeys(DRAW_K,t)},punch:{dur:.62,fn:t=>sampleKeys(PUNCH,t),hits:[[.18,1],[.36,1]]},")
# tick: drawing at the well is a held loop; loads change the stance
r("function tick(dt,I){S.x=I.x;S.z=I.z;","function tick(dt,I){const SB=I.sb||{};if(SB.drawing&&S.clip!=='draw')playG('draw');else if(!SB.drawing&&S.clip==='draw')playG('idle');S.ld=(S.ld||0)+(((SB.carry==='stone')?1:0)-(S.ld||0))*Math.min(1,dt*6);S.lw=(S.lw||0)+(((SB.carry==='water')?1:0)-(S.lw||0))*Math.min(1,dt*6);\n    S.x=I.x;S.z=I.z;")
r("    if(wk>0)p=mixP(p,walkPose(wph,S.bank),Math.min(1,wk*1.4));",
r"""    if(wk>0)p=mixP(p,walkPose(wph,S.bank),Math.min(1,wk*1.4));
    if(S.ld>.01&&S.clip==='idle'){const L=S.ld,b=Math.sin(wph*2)*.008*wk;p=mixP(p,Object.assign({},p,{p:[p.p[0],p.p[1]-.07+b,p.p[2]],pitch:p.pitch+10,bend:p.bend+8,headP:6,headY:p.headY*.3,hL:[.25,SY+.05+b,-.05],hR:[-.25,SY+.05+b,-.05],bL:[-.3,1,-.2],bR:[.3,1,-.2],eL:[1,-.5,.1],eR:[-1,-.5,.1],tw:p.tw*.3}),L)}
    if(S.lw>.01&&S.clip==='idle'&&S.ld<.5){p=mixP(p,Object.assign({},p,{hR:[-.13,SY+.08,-.01],bR:[0,1,0],eR:[-1,.2,-.3]}),S.lw)}""")
r("    // props by job\n    const job=S.clip==='idle'?(S.lastJob||(UP?'cast':'reap')):S.clip;if(S.clip!=='idle')S.lastJob=S.clip;sickle.visible=job==='reap';hatchet.visible=job==='chop';",
r"""    // props by job; loads ride in the hands
    const job=S.clip==='idle'?(S.lastJob||'reap'):S.clip;if(S.clip!=='idle')S.lastJob=S.clip;const busy=S.ld>.3||S.lw>.3;sickle.visible=!busy&&job==='reap';hatchet.visible=!busy&&(job==='chop'||job==='mine');
    {const pL=U.palmL.getWorldPosition(V()),pR=U.palmR.getWorldPosition(V());block.visible=S.ld>.3;if(block.visible){block.position.copy(pL).lerp(pR,.5);block.position.y+=.08*sc;block.position.add(W(V(0,0,-.04)).sub(W(V(0,0,0))));block.rotation.set(0,S.yaw,-.04)}
     jar.visible=S.lw>.3&&S.ld<.3;if(jar.visible){jar.position.copy(pR);jar.position.y+=.01*sc;jar.rotation.set(0,S.yaw,.25)}
     const dr=S.clip==='draw';bucket.visible=rope.visible=dr;if(dr){const k=(S.t%.6)/.6,front=W(V(0,0,.32)),top=pL.clone().lerp(pR,.5);bucket.position.set(front.x,(.05+.1*k)*sc,front.z);const a=top,b=bucket.position.clone();b.y+=.03*sc;rope.position.copy(a).lerp(b,.5);rope.scale.set(sc,a.distanceTo(b),sc);rope.quaternion.setFromUnitVectors(_Y,b.clone().sub(a).normalize())}}""")
r("if(S.hitNow==='chop'){chips(hatchet.userData.tip.getWorldPosition(V()),12)}","if(S.hitNow==='chop'||S.hitNow==='mine'){chips(hatchet.userData.tip.getWorldPosition(V()),12)}")
open('fact_stoneb.js','w').write(s);print('ok',len(s))
