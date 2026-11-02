// ---------- Electra (Greek): a winged fury on the shared Tripo rig with two added wing bones a side; she hovers, flaps, and fights with a burning lash; the awakened form is the serpent-crowned queen ----------
FACT.fury=function(){const QU=FACT.__fu===1;const LAB=(typeof GLAB==='function')?GLAB(QU?'furyu':'fury'):window.LABCFG;const UP=false;const UPC=false;const G0=window.MODELS&&window.MODELS[QU?'furyu':'fury']||window.MODELS.fury||window.MODELS.stoneb;const src=T.SkeletonUtils.clone(G0.scene);const U={mats:[]};const V=(x,y,z)=>new T.Vector3(x||0,y||0,z||0);const SCN=scene;
  const root=new T.Group();SCN.add(root);root.add(src);U.root=root;const B={};src.traverse(o=>{if(o.isBone)B[o.name]=o});
  src.updateMatrixWorld(true);const box=new T.Box3();src.traverse(o=>{if(o.isMesh){o.geometry.computeBoundingBox();box.union(o.geometry.boundingBox)}});
  const sc=(LAB.mh||1)/(box.max.y-box.min.y);src.scale.setScalar(sc);
  const soft=(()=>{const d=new Uint8Array([176,176,176,255,222,222,222,255,255,255,255,255]);const t=new T.DataTexture(d,3,1,T.RGBAFormat);t.minFilter=t.magFilter=T.LinearFilter;t.needsUpdate=true;return t})();
  src.traverse(o=>{if(o.isMesh){o.frustumCulled=false;const mp=o.material.map;if(mp){mp.encoding=T.LinearEncoding;mp.anisotropy=4;mp.needsUpdate=true}const mat=M('#ffffff',{map:mp,skinning:true,gradientMap:soft});mat.userData.outlineParameters={visible:false};U.mats.push(mat);o.material=mat;o.userData.keep=true}});
  root.updateMatrixWorld(true);const BIND=[],BQ={},BP={};const _iv=new T.Matrix4().copy(src.matrixWorld).invert();
  for(const n in B){const b=B[n];BIND.push([b,b.quaternion.clone(),b.position.clone()]);BQ[n]=b.getWorldQuaternion(new T.Quaternion());BP[n]=b.getWorldPosition(V()).applyMatrix4(_iv)}
  const hip0=BP.Hip.clone(),SHL=BP.L_Upperarm.clone().sub(hip0),SHR=BP.R_Upperarm.clone().sub(hip0);
  const LA={L:[BP.L_Upperarm.distanceTo(BP.L_Forearm),BP.L_Forearm.distanceTo(BP.L_Hand)],R:[BP.R_Upperarm.distanceTo(BP.R_Forearm),BP.R_Forearm.distanceTo(BP.R_Hand)]};
  const LL={L:[BP.L_Thigh.distanceTo(BP.L_Calf),BP.L_Calf.distanceTo(BP.L_Foot)],R:[BP.R_Thigh.distanceTo(BP.R_Calf),BP.R_Calf.distanceTo(BP.R_Foot)]};
  const ANK=BP.L_Foot.y;const FOFF=V((BP.L_Foot.x+BP.R_Foot.x)/2-.004,0,(BP.L_Foot.z+BP.R_Foot.z)/2);
  // left hand closed round the grip; right hand in a draw hook (index, middle, ring curled at the tips, thumb tucked)
  const CURL=[];for(const sd of['L','R'])for(const f of['Index','Mid','Ring','Pinky','Thumb'])for(let k=1;k<=3;k++){const n=sd+'_'+f+k;if(!B[n])continue;
    const ax=(f==='Thumb'?V(0,1,0):V(0,0,1)).applyQuaternion(BQ[n].clone().invert()).normalize();const a=f==='Thumb'?.5:k===1?1.2:1.3;CURL.push([B[n],new T.Quaternion().setFromAxisAngle(ax,(sd==='L'?-1:1)*a)])}
  // palm anchors (no mesh): where the fist closes, with the thumb direction kept for wrist alignment
  function anchor(sd){const g=new T.Group();const hq=BQ[sd+'_Hand'].clone().invert(),fw=V(0,0,1).applyQuaternion(hq).normalize(),len=BP[sd+'_Mid1'].clone().sub(BP[sd+'_Hand']).applyQuaternion(hq).normalize();
    g.position.copy(len).multiplyScalar(BP[sd+'_Mid1'].distanceTo(BP[sd+'_Hand'])*.6).addScaledVector(V(0,-1,0).applyQuaternion(hq),.012);B[sd+'_Hand'].add(g);g.userData.fw=fw;return g}
  U.palmL=anchor('L');U.palmR=anchor('R');
  const E={io:t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2,out:t=>1-Math.pow(1-t,3),in:t=>t*t*t,lin:t=>t};
  // ---- props: golden druid's sickle and a hatchet (swapped per job), a seed glow, a sprout that grows from the soil, wood chips ----
  const goldM=M('#c98a3c'),goldD=M('#8a5a26'),woodM=M('#6e4a2c'),ironM=M('#d9b77a'),leafM=M('#5fae3e'),leafD=M('#3f8a2c'),stemM=M('#7cc04a');
  for(const x of[goldM,goldD,woodM,ironM,leafM,leafD,stemM]){x.userData.outlineParameters={visible:false};U.mats.push(x)}
  function inHand(sd,g,along){const an=U['palm'+sd],fw=an.userData.fw.clone(),hq=BQ[sd+'_Hand'].clone().invert();const len=BP[sd+'_Mid1'].clone().sub(BP[sd+'_Hand']).applyQuaternion(hq).normalize();
    const side=len.clone().sub(fw.clone().multiplyScalar(len.dot(fw))).normalize(),zz=side.clone().cross(fw);g.quaternion.setFromRotationMatrix(new T.Matrix4().makeBasis(side,fw,zz));an.add(g);return g}
  // sickle: short handle along the thumb axis, a crescent blade sweeping out to the side
  const sickle=new T.Group();{const h=new T.Mesh(new T.CylinderGeometry(.008,.009,.09,6),woodM);h.position.y=.01;sickle.add(h);const fr=new T.Mesh(new T.CylinderGeometry(.011,.011,.012,8),goldD);fr.position.y=.057;sickle.add(fr);
    const pts=[];for(let i=0;i<=14;i++){const a=i/14*Math.PI*.95;pts.push(V(Math.sin(a)*.075-0,.06+(1-Math.cos(a))*.0+Math.sin(a)*.0+Math.cos(a)*-.0+ (1-Math.cos(a))*.075*0+ Math.sin(a)*.0,0))}
    const cv=new T.CatmullRomCurve3(Array.from({length:15},(_,i)=>{const a=i/14*Math.PI*.9;return V(.075*(1-Math.cos(a))*.0+.075*Math.sin(a)*1.0,.06+.075*(1-Math.cos(a)),0)}));
    const bl=new T.Mesh(new T.TubeGeometry(cv,24,.0055,5,false),goldM);bl.scale.z=.45;sickle.add(bl);const tipS=new T.Group();tipS.position.copy(cv.getPoint(1));sickle.add(tipS);sickle.userData.tip=tipS}
  inHand('R',sickle);U.sickle=sickle;
  // hatchet: handle along the thumb axis, iron head at the top with the edge forward
  const hatchet=new T.Group();{const h=new T.Mesh(new T.CylinderGeometry(.008,.009,.2,6),woodM);h.position.y=.05;hatchet.add(h);const hd=new T.Mesh(new T.BoxGeometry(.075,.045,.045),ironM);hd.position.set(.0,.15,0);hatchet.add(hd);
    const tipH=new T.Group();tipH.position.set(.04,.15,0);hatchet.add(tipH);hatchet.userData.tip=tipH}
  inHand('R',hatchet);U.hatchet=hatchet;hatchet.visible=false;
  const GLW=(()=>{const c=document.createElement('canvas');c.width=c.height=64;const g=c.getContext('2d'),gr=g.createRadialGradient(32,32,0,32,32,31);gr.addColorStop(0,'rgba(255,255,255,1)');gr.addColorStop(.35,'rgba(255,255,255,.7)');gr.addColorStop(1,'rgba(255,255,255,0)');g.fillStyle=gr;g.fillRect(0,0,64,64);return new T.CanvasTexture(c)})();
  const seedGlow=egSprite(GLW,.08,'#b6ff8c');seedGlow.material.opacity=0;SCN.add(seedGlow);
  // sprout: a curling stem with leaves unfolding, grown at the spot he planted
  const sprout=new T.Group();{const cv=new T.CatmullRomCurve3([V(0,0,0),V(.004,.03,0),V(-.006,.06,.004),V(.002,.09,0)]);const st=new T.Mesh(new T.TubeGeometry(cv,12,.004,5,false),stemM);sprout.add(st);
    const leaf=(y,a,s)=>{const sh=new T.Shape();sh.moveTo(0,0);sh.quadraticCurveTo(.02*s,.012*s,.042*s,0);sh.quadraticCurveTo(.02*s,-.012*s,0,0);const m=new T.Mesh(new T.ShapeGeometry(sh,6),leafM);m.material.side=T.DoubleSide;const g=new T.Group();g.position.y=y;g.rotation.y=a;m.rotation.z=.5;g.add(m);sprout.add(g);return m};
    sprout.userData.leaves=[leaf(.05,0,1),leaf(.065,Math.PI,1),leaf(.088,Math.PI/2,1.25),leaf(.09,-Math.PI/2,1.1)]}
  sprout.scale.setScalar(0.0001);SCN.add(sprout);U.sprout=sprout;
  const MOTE=[];function mote(from,v,col,life){const m=egSprite(GLW,.035,col||'#5fd84a',false);m.position.copy(from);SCN.add(m);MOTE.push({m,v,t:0,L:life||.8})}
  const CHIP=[];function chips(p,n){for(let i=0;i<n;i++){const m=new T.Mesh(new T.BoxGeometry(.016,.012,.012),i%3?M('#e8cf9a'):M('#b98c56'));m.scale.setScalar(sc);m.position.copy(p);SCN.add(m);const a=Math.random()*TAU;CHIP.push({m,v:V(Math.cos(a)*.6,.8+Math.random()*.6,Math.sin(a)*.6).multiplyScalar(sc),r:V(Math.random()*9,Math.random()*9,0),t:0})}}
  U.chips=chips;
  const oarW=M(UPC?'#e8bf4e':'#7a5634'),oarD=M(UPC?'#d4a23a':'#5a3e24'),oarT=M(UPC?'#9a1f2a':'#3f8f86');for(const x of[oarW,oarD,oarT]){x.userData.outlineParameters={visible:false};U.mats.push(x)}
  const oar=new T.Group();{const sh=new T.Mesh(new T.CylinderGeometry(.011,.013,1,7),oarW);sh.position.y=.5;oar.add(sh);const bl=new T.Mesh(new T.BoxGeometry(.075,.24,.014),oarD);bl.position.y=1.08;oar.add(bl);const st=new T.Mesh(new T.BoxGeometry(.05,.13,.016),oarT);st.position.set(.006,1.1,.001);oar.add(st);const nk=new T.Mesh(new T.CylinderGeometry(.016,.011,.06,7),oarD);nk.position.y=.95;oar.add(nk);if(UPC){const tip=new T.Mesh(new T.ConeGeometry(.016,.06,6),oarD);tip.rotation.x=Math.PI;tip.position.y=-.03;oar.add(tip);for(const y of[.62,.8]){const rg=new T.Mesh(new T.CylinderGeometry(.017,.017,.02,8),oarD);rg.position.y=y;oar.add(rg)}const tr=new T.Group();tr.position.set(.006,1.1,.009);for(const x of[-.016,0,.016]){const p=new T.Mesh(new T.BoxGeometry(.006,.07,.004),oarD);p.position.x=x;p.position.y=x?0:.008;tr.add(p)}const bar=new T.Mesh(new T.BoxGeometry(.04,.006,.004),oarD);bar.position.y=-.03;tr.add(bar);oar.add(tr)}}
  oar.scale.setScalar(sc);SCN.add(oar);U.oar=oar;oar.visible=false;
  const STANCE0=1;
  // ---- the burning lash ----
  const LN=14,SEG=.052,LPTS=[];const lashM=M(QU?'#4fae4a':'#b8321c'),lashH=M(QU?'#ffd85a':'#ffb04a');for(const x of[lashM,lashH]){x.userData.outlineParameters={visible:false};U.mats.push(x)}
  const LSEG=[];for(let i=0;i<LN;i++){const m=new T.Mesh(new T.CylinderGeometry(.009,.011,SEG*1.05,5),i%3===2?lashH:lashM);SCN.add(m);LSEG.push(m);LPTS.push(V())}LPTS.push(V());U.lash=LSEG;
  const ember=egSprite(GLW,.1,QU?'#9dffb0':'#ffb04a');SCN.add(ember);
  const lanternGlow=egSprite(GLW,QU?.07:.05,QU?'#7dffb0':'#ff4a2a');SCN.add(lanternGlow);U.eyeGlow=lanternGlow;
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
  const rope=new T.Mesh(new T.CylinderGeometry(.004,.004,1,5),ropeM);rope.visible=false;SCN.add(rope);
  // ---- poses (chest frame: +z out of the chest toward his work, +x to his left) ----
  const SY=SHL.y,POUCH=[-.11,-.04,.07],GRD=-(hip0.y-ANK)-.0;
  const ST={p:[0,-.02,0],yaw:0,pitch:3,roll:0,tw:0,bend:2,side:0,headP:-2,headY:0,
    hL:[.14,-.12,.03],hR:[-.14,-.11,.03],bL:[0,-.3,1],bR:[0,.2,1],eL:[.6,-.3,-1],eR:[-.6,-.3,-1],
    fL:[.075,ANK,.03],fR:[-.075,ANK,-.03],fyL:-8,fyR:8,ptL:0,ptR:0,airL:0,airR:0,bfL:[.06,-.43,-.05],bfR:[-.06,-.41,-.02],tool:0,glow:0,grow:0,trl:0,hwL:0,hwR:0,slide:0,hgL:[0,0,0],hgR:[0,0,0],wv:[-.1,-1,.15],wc:.18,wl:1,fa:26,fb:4,fs:8,ff:2.1,fly:1,airL:1,airR:1};
  const K=(t,o,lf)=>[t,Object.assign(JSON.parse(JSON.stringify(ST)),o||{}),lf||{}];
  const NUM=Object.keys(ST).filter(k=>!['fL','fR','fyL','fyR'].includes(k));
  const carry=keys=>{let fL=ST.fL,fR=ST.fR,yL=ST.fyL,yR=ST.fyR;for(const k of keys){const m=k[2];if(m.fL)fL=m.fL;if(m.fR)fR=m.fR;if(m.fyL!=null)yL=m.fyL;if(m.fyR!=null)yR=m.fyR;k[1].fL=fL;k[1].fR=fR;k[1].fyL=yL;k[1].fyR=yR;k[1].lfL=m.lfL||0;k[1].lfR=m.lfR||0}return keys};
  // PLANT: step in, sink onto the right knee, a seed from the pouch, pressed into the soil with both hands; the sprout curls up under his cupped palms
  const PLANT=carry([K(0,{tool:0}),
    K(.3,{p:[0,-.16,.02],pitch:6,bend:6,headP:16,hR:POUCH,hL:[.12,-.08,.1],tool:0},{fL:[.08,ANK,.17],fyL:-6,lfL:.05}),
    K(.62,{p:[0,-.3,-.02],pitch:6,bend:10,headP:26,hR:[-.05,-.08,.15],hL:[.07,-.1,.17],eR:[-.6,-.6,-.4],ptR:.95,glow:.3,tool:0},{fR:[-.075,.075,-.23],fyR:4,lfR:.03}),
    K(.92,{p:[0,-.32,.02],pitch:12,bend:16,headP:34,hR:[-.025,-.28,.24],hL:[.03,-.28,.25],eR:[-.7,-.4,-.5],eL:[.7,-.4,-.5],bR:[0,-1,.3],bL:[0,-1,.3],ptR:.95,glow:.9,tool:0}),
    K(1.45,{p:[0,-.31,0],pitch:9,bend:12,headP:28,hR:[-.035,-.18,.24],hL:[.04,-.18,.25],eR:[-.7,-.4,-.5],eL:[.7,-.4,-.5],bR:[0,-.6,.5],bL:[0,-.6,.5],ptR:.95,glow:1,grow:1,tool:0}),
    K(1.7,{p:[0,-.24,-.01],pitch:10,bend:14,headP:12,hR:[-.1,-.1,.12],hL:[.1,-.1,.13],ptR:.6,glow:.2,grow:1,tool:0}),
    K(2.0,{p:[0,-.06,0],grow:1,tool:0},{fR:[-.075,ANK,-.03],fyR:8,lfR:.05,fL:[.075,ANK,.03],fyL:-8,lfL:.04}),
    K(2.3,{grow:1,tool:0})]);
  // REAP: stoop, the left hand gathers a sheaf low, the golden sickle sweeps through under it, the cut sheaf lifted and set aside
  const REAP=carry([K(0),
    K(.22,{p:[0,-.22,.0],pitch:12,bend:8,tw:-14,headP:26,hL:[.1,-.22,.26],bL:[.3,-.3,1],hR:[-.22,-.08,.08],bR:[-.6,.4,.6],eR:[-1,.3,-.3]},{fL:[.09,ANK,.13],fyL:-14,lfL:.04}),
    K(.42,{p:[0,-.24,.01],pitch:14,bend:10,tw:16,headP:28,hL:[.1,-.25,.25],bL:[.3,-.3,1],hR:[.12,-.27,.22],bR:[1,-.2,.4],eR:[-.6,-.2,-.6],trl:1}),
    K(.62,{p:[0,-.16,.0],pitch:10,bend:6,tw:8,headP:16,hL:[.12,-.1,.2],bL:[0,1,.3],hR:[.0,-.18,.2],bR:[.6,-.3,.6],trl:.2}),
    K(.9,{p:[0,-.06,0],pitch:8,bend:6,tw:-18,hL:[.22,-.04,.06],hR:[-.14,-.1,.05]}),
    K(1.25,{},{fL:[.075,ANK,.03],fyL:-8,lfL:.04})]);
  // CHOP: square up, the hatchet swung high over the right shoulder, driven down and across into the trunk at waist height, worked free
  const CHOP=carry([K(0,{tool:1}),
    K(.28,{p:[0,-.06,-.02],pitch:-6,bend:-8,tw:-26,headP:-6,hR:[-.1,SY+.06,-.04],bR:[-.2,.4,-1],eR:[-1,.6,-.2],hL:[.12,.08,.16],eL:[.8,-.4,-.4],tool:1},{fR:[-.09,ANK,-.08],fyR:20,lfR:.04}),
    K(.44,{p:[0,-.17,.04],pitch:12,bend:10,tw:14,headP:14,hR:[.03,.02,.3],bR:[.1,-.2,1],eR:[-.6,-.6,-.4],hL:[.1,-.04,.14],tool:1,trl:1}),
    K(.62,{p:[0,-.15,.03],pitch:10,bend:8,tw:10,headP:12,hR:[.0,.03,.27],bR:[.1,.0,1],tool:1,trl:0}),
    K(.85,{p:[0,-.05,0],pitch:6,bend:4,tw:-6,hR:[-.15,-.06,.06],bR:[0,.4,1],hL:[.14,-.1,.04],tool:1}),
    K(1.1,{tool:1},{fR:[-.075,ANK,-.03],fyR:8,lfR:.04})]);
  const DRAW_K=carry([K(0,{p:[0,-.08,.02],pitch:10,bend:8,headP:18,hL:[.06,.1,.22],hR:[-.05,-.04,.22],bL:[0,1,.2],bR:[0,1,.2],eL:[.8,-.4,-.4],eR:[-.8,-.4,-.4]},{fL:[.09,ANK,.1],fyL:-10,fR:[-.08,ANK,-.06],fyR:12}),
    K(.3,{p:[0,-.12,0],pitch:6,bend:6,headP:14,hL:[.06,-.06,.16],hR:[-.05,.12,.24],bL:[0,1,.2],bR:[0,1,.2],eL:[.8,-.4,-.4],eR:[-.8,-.4,-.4]}),
    K(.6,{p:[0,-.08,.02],pitch:10,bend:8,headP:18,hL:[.06,.1,.22],hR:[-.05,-.04,.22],bL:[0,1,.2],bR:[0,1,.2],eL:[.8,-.4,-.4],eR:[-.8,-.4,-.4]})]);
  const PUNCH=carry([K(0,{p:[0,-.06,0],tw:-14,hL:[.08,SY-.02,.14],hR:[-.08,SY-.04,.1],bL:[0,1,.3],bR:[0,1,.3],eL:[.9,-.6,-.2],eR:[-.9,-.6,-.2]},{fL:[.08,ANK,.1],fyL:-14,fR:[-.08,ANK,-.08],fyR:18}),
    K(.18,{p:[0,-.07,.04],tw:22,pitch:8,hL:[.08,SY-.02,.14],hR:[-.0,SY-.02,.36],bR:[0,0,1],eR:[-.9,-.3,-.2]}),
    K(.36,{p:[0,-.06,.02],tw:-26,pitch:6,hL:[.02,SY,.33],bL:[0,0,1],eL:[1,.3,-.2],hR:[-.08,SY-.04,.12]}),
    K(.62,{p:[0,-.06,0],tw:-14,hL:[.08,SY-.02,.14],hR:[-.08,SY-.04,.1],bL:[0,1,.3],bR:[0,1,.3],eL:[.9,-.6,-.2],eR:[-.9,-.6,-.2]})]);
  function hermite(k,i,t,key){const a=k[i][1][key],b=k[i+1][1][key],t0=k[i][0],t1=k[i+1][0],dt=t1-t0,u=(t-t0)/dt;
    const pa=k[Math.max(0,i-1)],pb=k[Math.min(k.length-1,i+2)];const tan=(P0,P1,T0,T1,j)=>{const x0=j==null?P0:P0[j],x1=j==null?P1:P1[j];return(x1-x0)/Math.max(.001,T1-T0)};
    const h00=2*u*u*u-3*u*u+1,h10=u*u*u-2*u*u+u,h01=-2*u*u*u+3*u*u,h11=u*u*u-u*u;
    const f=j=>{const x0=j==null?a:a[j],x1=j==null?b:b[j];const m0=i===0?0:tan(pa[1][key],b,pa[0],t1,j),m1=i+2>=k.length?0:tan(a,pb[1][key],t0,pb[0],j);return h00*x0+h10*m0*dt+h01*x1+h11*m1*dt};
    return Array.isArray(a)?a.map((_,j)=>f(j)):f(null)}
  function sampleKeys(k,t){if(t<=k[0][0])return Object.assign({},k[0][1]);const L=k.length-1;if(t>=k[L][0])return Object.assign({},k[L][1]);let i=0;while(t>k[i+1][0])i++;
    const o={};for(const n of NUM)o[n]=hermite(k,i,t,n);const A=k[i][1],Bk=k[i+1][1],u=(t-k[i][0])/(k[i+1][0]-k[i][0]);
    // snap values: the draw and the arrow change hands instantly at the release
    for(const n of['draw','arw','charge'])o[n]=(A[n]>Bk[n]&&t>=k[i][0])?(u<.15?A[n]*(1-u/.15):0):A[n]+(Bk[n]-A[n])*E.io(u);
    for(const sd of['L','R']){const fa=A['f'+sd],fb=Bk['f'+sd],same=fa[0]===fb[0]&&fa[2]===fb[2]&&fa[1]===fb[1];const e=same?0:E.io(u);
      o['f'+sd]=fa.map((v,j)=>v+(fb[j]-v)*e);o['f'+sd][1]+=same?0:Math.sin(u*Math.PI)*(Bk['lf'+sd]||0);o['fy'+sd]=A['fy'+sd]+(Bk['fy'+sd]-A['fy'+sd])*(A['fy'+sd]===Bk['fy'+sd]?0:E.io(u))}return o}
  // ---- the Aged Druid's magic ----
  // CAST: coil, both palms cupped at the chest while a green orb swells between them, then a step and a two-handed thrust that drives it at the foe
  const CAST=carry([K(0,{tool:2}),
    K(.32,{p:[0,-.08,-.02],pitch:-2,tw:-20,bend:-2,headP:4,hL:[.05,.05,.15],hR:[-.05,.05,.15],bL:[.2,1,.3],bR:[-.2,1,.3],eL:[.9,-.5,-.3],eR:[-.9,-.5,-.3],glow:1,tool:2},{fR:[-.09,ANK,-.09],fyR:22,lfR:.04}),
    K(.5,{p:[0,-.12,.06],pitch:12,tw:8,bend:8,headP:-4,hL:[.04,.13,.33],hR:[-.04,.13,.33],bL:[.1,1,.6],bR:[-.1,1,.6],eL:[.8,-.6,-.2],eR:[-.8,-.6,-.2],glow:0,tool:2},{fL:[.08,ANK,.16],fyL:-10,lfL:.05}),
    K(.75,{p:[0,-.1,.04],pitch:8,tw:4,bend:5,hL:[.07,.08,.27],hR:[-.07,.08,.27],tool:2}),
    K(1.3,{tool:2},{fL:[.075,ANK,.03],fyL:-8,lfL:.04,fR:[-.075,ANK,-.03],fyR:8,lfR:.04})]);
  // THORNS: the right arm rises, power gathering in the palm, then he drops and slams it flat to the earth; spikes erupt under the foe
  const THORN=carry([K(0,{tool:2}),
    K(.38,{p:[0,-.02,-.02],pitch:-6,tw:-14,bend:-6,headP:-8,hR:[-.08,SY+.1,.16],bR:[0,1,.5],eR:[-1,-.2,-.4],hL:[.15,.0,.12],glow:.9,tool:2},{fR:[-.1,ANK,-.08],fyR:20,lfR:.04}),
    K(.6,{p:[0,-.26,.06],pitch:20,tw:6,bend:14,headP:10,hR:[-.04,-.3,.27],bR:[0,-.2,1],eR:[-.7,.2,-.4],hL:[.16,-.08,.14],glow:0,ptR:.6,tool:2},{fL:[.09,ANK,.17],fyL:-8,lfL:.05}),
    K(.85,{p:[0,-.24,.05],pitch:16,tw:4,bend:12,headP:6,hR:[-.05,-.27,.26],bR:[0,-.2,1],hL:[.16,-.06,.13],ptR:.6,tool:2}),
    K(1.45,{tool:2},{fL:[.075,ANK,.03],fyL:-8,lfL:.04,fR:[-.075,ANK,-.03],fyR:8,lfR:.04})]);
  const spikeM=M('#4f7a2c'),spikeD=M('#2f5a22');for(const x of[spikeM,spikeD]){x.userData.outlineParameters={visible:false};U.mats.push(x)}
  const SPK=[];U.thorns=p=>{for(let i=0;i<9;i++){const a=i/9*TAU+Math.random()*.5,r=(i===0?.12:.12+Math.random()*.2)*sc;const m=new T.Mesh(new T.ConeGeometry(.024,.24+Math.random()*.14,5),i%2?spikeM:spikeD);m.scale.setScalar(sc);m.position.set(p.x+Math.cos(a)*r,0,p.z+Math.sin(a)*r);m.rotation.set((Math.random()-.5)*.6,0,(Math.random()-.5)*.6);m.userData.h=m.geometry.parameters.height*sc;SCN.add(m);SPK.push({m,t:-i*.025})}
    for(let i=0;i<12;i++)mote(V(p.x,.02*sc,p.z),V((Math.random()-.5)*.8,.6+Math.random()*.5,(Math.random()-.5)*.8).multiplyScalar(sc),Math.random()<.5?'#a8f07a':'#5fd84a',.7)};
  U.GLW=GLW;
  const GRIP={hR:[-.11,SY-.03,.13],hL:[.05,-.13,.17],bR:[.2,1,.4],bL:[.2,1,.4],eR:[-1,-.3,-.3],eL:[.8,-.5,-.3]};
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
  // ---- Electra's moves (chest frame: +z forward, +x her left). wv = where the lash points, wc = how much it curls, fa/fb/fs/ff = wing flap amount / lift / sweep back / beats per second, fly = hover height ----
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
  const STANCE=()=>JSON.parse(JSON.stringify(ST));
  const CL={idle:{dur:4,loop:true,fn:t=>{const o=STANCE(),s=Math.sin(t/4*TAU);o.p=[0,-.02+s*.004,0];o.bend+=s*1.5;o.headY=Math.sin(t/4*TAU*.5)*10;o.hL=[.14,-.12+s*.004,.03];o.hR=[-.14,-.11+s*.004,.03];return o}},
    plant:{dur:2.3,fn:t=>sampleKeys(PLANT,t),hits:[[.95,1]]},reap:{dur:1.25,fn:t=>sampleKeys(REAP,t),hits:[[.42,1]]},chop:{dur:1.1,fn:t=>sampleKeys(CHOP,t),hits:[[.44,1]]},mine:{dur:1.1,fn:t=>sampleKeys(CHOP,t),hits:[[.44,1]]},draw:{dur:.6,loop:true,fn:t=>sampleKeys(DRAW_K,t)},punch:{dur:.62,fn:t=>sampleKeys(PUNCH,t),hits:[[.18,1],[.36,1]]},sweep:{dur:1,fn:t=>sampleKeys(SWEEP,t),hits:[[.42,1]]},lash:{dur:.95,fn:t=>sampleKeys(LASH,t),hits:[[.42,1]]},slash:{dur:.92,fn:t=>sampleKeys(SLASH,t),hits:[[.4,1]]},talon:{dur:.95,fn:t=>sampleKeys(TALON,t),hits:[[.4,1]]},wrath:{dur:1.8,fn:t=>sampleKeys(WRATH,t),hits:[[1.32,2]]},thrust:{dur:.85,fn:t=>sampleKeys(THRUST,t),hits:[[.38,1]]},rise:{dur:.95,fn:t=>sampleKeys(RISE,t),hits:[[.45,1]]},pound:{dur:1.1,fn:t=>sampleKeys(POUND,t),hits:[[.62,1.6]]},
    cast:{dur:1.3,fn:t=>sampleKeys(CAST,t),hits:[[.5,1]]},thorns:{dur:1.45,fn:t=>sampleKeys(THORN,t),hits:[[.6,1.4]]}};CL.bolt=CL.cast;
  CL.work=CL.plant;
  const S={x:0,z:0,yaw:0,vel:0,wamt:0,clip:'idle',t:0,rate:1,hold:false,prev:null,bl:0,blT:.2,base:0};let cur=CL.idle.fn(0);
  function playG(n,rate,off){if(!CL[n])n='idle';S.prev=cur;S.bl=S.blT;S.clip=n;S.rate=rate||1;S.t=off||0}
  function mixP(a,b,f){const o={};for(const k in a){let x=a[k],y=b[k];if(y===undefined){o[k]=x;continue}if(/^(yaw|fyL|fyR)$/.test(k))y=y+360*Math.round((x-y)/360);o[k]=Array.isArray(x)?x.map((v,i)=>v+(y[i]-v)*f):typeof x==='number'?x+(y-x)*f:x}return o}
  const _q=new T.Quaternion(),_q2=new T.Quaternion(),_wq=new T.Quaternion(),_pq=new T.Quaternion(),_a=V(),_b=V(),_c=V(),_d=V(),_p=V(),_eu=new T.Euler(),rootQ=new T.Quaternion(),bodyQ=new T.Quaternion();
  function setWQ(b,qW){b.parent.getWorldQuaternion(_pq).invert();b.quaternion.copy(_pq).multiply(qW);b.updateMatrixWorld(true)}
  function aim(bone,child,tw){bone.getWorldPosition(_a);child.getWorldPosition(_b);_c.subVectors(_b,_a).normalize();_d.subVectors(tw,_a).normalize();_q.setFromUnitVectors(_c,_d);
    bone.getWorldQuaternion(_wq);_q.multiply(_wq);setWQ(bone,_q)}
  function rotW(bone,axisW,ang){_q2.setFromAxisAngle(axisW,ang);bone.getWorldQuaternion(_wq);_q2.multiply(_wq);setWQ(bone,_q2)}
  const W=v=>src.localToWorld(v);
  const bodyPt=(arr,pel,q)=>V(arr[0],arr[1],arr[2]).applyQuaternion(q).add(pel);
  function twoBone(b1,b2,b3,L1,L2,tgtW,poleW){b1.getWorldPosition(_a);_d.subVectors(tgtW,_a);let d=clamp(_d.length(),.02*sc,(L1+L2)*sc-.002*sc);_d.normalize();const l1=L1*sc,l2=L2*sc;
    const a=(l1*l1-l2*l2+d*d)/(2*d),h=Math.sqrt(Math.max(0,l1*l1-a*a));_p.copy(poleW).addScaledVector(_d,-poleW.dot(_d)).normalize();const kn=_a.clone().addScaledVector(_d,a).addScaledVector(_p,h),end=_a.clone().addScaledVector(_d,d);
    aim(b1,b2,kn);aim(b2,b3,end)}

  // ---- walk: an unhurried, grounded stride; cloak-heavy shoulders, hands loose ----
  let wph=0;const STRIDE=1.12,DUTY=.6,_X=V(1,0,0),_Y=V(0,1,0),_Z=V(0,0,1);
  const shake=v=>LAB.api&&LAB.api.shake&&LAB.api.shake(v);
  function walkPose(ph,bank){const o=STANCE(),u0=ph/TAU,A=STRIDE*DUTY/2,c=Math.cos(ph),s2=Math.sin(ph),c2=Math.cos(2*ph);
    // pelvis turns into each stride, shoulders counter it; weight shifts over the standing leg; the body dips at contact and rises at mid-stance
    o.yaw=9*c;o.tw=-22*c;o.roll=3.2*c+bank;o.side=-2.5*c;o.pitch=6;o.bend=4+1.2*c2;o.headP=-5+1.5*c2;o.headY=-(o.yaw+o.tw)*.85;
    o.p=[.016*c,-.04+.014*c2,.012];
    for(const[sd,off,sgn]of[['L',0,1],['R',.5,-1]]){const u=(((u0+off)%1)+1)%1;let z,y=ANK,pt=0;
      if(u<DUTY){const k=u/DUTY;z=lerp(A,-A,k);pt=k<.15?-.25*(1-k/.15):k>.7?.6*Math.pow((k-.7)/.3,1.2):0;y+=k>.7?.03*Math.pow((k-.7)/.3,1.3):0}
      else{const k=(u-DUTY)/(1-DUTY);z=lerp(-A,A,E.io(k));y+=.042*Math.sin(Math.min(1,k*1.15)*Math.PI)+(k<.25?.012*(1-k/.25):0);pt=k<.3?.45:.45*(1-(k-.3)/.7)-.18*(k>.78?(k-.78)/.22:0)}
      o['f'+sd]=[sgn*.07,y,z+.01];o['fy'+sd]=sgn*-6;o['pt'+sd]=pt;
      // arms swing opposite the legs from the shoulder; the forward hand rises and the elbow bends, the back hand trails long
      const sw=-sgn*c,fwd=Math.max(0,sw),bk=Math.max(0,-sw);
      o['h'+sd]=[sgn*(.135-.02*fwd),-.13+.05*fwd*fwd+.012*bk,.02+sw*.15+.03*fwd];o['e'+sd]=[sgn*.45,-.25+.35*fwd,-1];o['b'+sd]=[sgn*.1,-.2+.6*fwd,1]}
    return o}
  function tick(dt,I){const SB=I.sb||{};if(SB.drawing&&S.clip!=='draw')playG('draw');else if(!SB.drawing&&S.clip==='draw')playG('idle');S.ld=(S.ld||0)+(((SB.carry==='stone')?1:0)-(S.ld||0))*Math.min(1,dt*6);S.lw=(S.lw||0)+(((SB.carry==='water')?1:0)-(S.lw||0))*Math.min(1,dt*6);
    S.x=I.x;S.z=I.z;let df=I.yaw-S.yaw;df=Math.atan2(Math.sin(df),Math.cos(df));S.yaw+=df*Math.min(1,dt*10);S.vel=I.speed;
    const c=CL[S.clip];const t0=S.t;S.t+=dt*S.rate;if(c.hits)c.hits.forEach(([ht,k],i)=>{if(t0<ht&&S.t>=ht){S.hitNow=S.clip;if(LAB.onStrike)LAB.onStrike(k,i,U,S.clip);shake(S.clip==='chop'?.15:.05)}})
    if(!c.loop&&S.t>=c.dur&&!S.hold)playG('idle');const c2=CL[S.clip],tt=c2.loop?S.t%c2.dur:Math.min(S.t,c2.dur);let p=c2.fn(tt);
    if(S.bl>0&&S.prev){S.bl-=dt;p=mixP(S.prev,p,1-Math.max(0,S.bl)/S.blT)}cur=p;
    S.wamt+=(clamp(S.vel/.4,0,1)-S.wamt)*Math.min(1,dt*7);const wk=S.clip==='idle'?S.wamt:0;wph+=(I.dist||0)/(STRIDE*sc)*TAU;
    S.bank=(S.bank||0)+((clamp(-(dt>0?df/dt:0)*2.2,-9,9))-(S.bank||0))*Math.min(1,dt*4);
    const fwk=S.wamt;
    if(S.clip==='idle'){const nw=performance.now()/1000,s1=Math.sin(nw*2.1*TAU/2);p=Object.assign({},p,HOV,{hR:[HOV.hR[0],HOV.hR[1]+s1*.01,HOV.hR[2]],hL:[HOV.hL[0],HOV.hL[1]+s1*.01,HOV.hL[2]],pitch:4+fwk*18,bend:3+fwk*6,headP:-4-fwk*10+Math.sin(nw*.6)*4,headY:Math.sin(nw*.45)*14,roll:S.bank*.8,bfL:[.06,-.43,-.05-fwk*.12],bfR:[-.06,-.41,-.02-fwk*.14],fa:26+fwk*12,ff:2.1+fwk*.7,fs:8+fwk*10,wv:[-.35+Math.sin(nw*1.3)*.08,-.7,.3-fwk*.5]})}
    if(S.ld>.01&&S.clip==='idle'){const L=S.ld,b=Math.sin(wph*2)*.008*wk;p=mixP(p,Object.assign({},p,{p:[p.p[0],p.p[1]-.07+b,p.p[2]],pitch:p.pitch+10,bend:p.bend+8,headP:6,headY:p.headY*.3,hL:[.25,SY+.05+b,-.05],hR:[-.25,SY+.05+b,-.05],bL:[-.3,1,-.2],bR:[.3,1,-.2],eL:[1,-.5,.1],eR:[-1,-.5,.1],tw:p.tw*.3}),L)}
    if(S.lw>.01&&S.clip==='idle'&&S.ld<.5){p=mixP(p,Object.assign({},p,{hR:[-.13,SY+.08,-.01],bR:[0,1,0],eR:[-1,.2,-.3]}),S.lw)}
    for(const[b,q,ps]of BIND){b.quaternion.copy(q);b.position.copy(ps)}
    S.fph=(S.fph||0)+dt*(p.ff||2)*TAU;root.position.set(S.x,((p.fly==null?1:p.fly)*.42+Math.sin(S.fph)*.025)*(LAB.mh||1),S.z);root.rotation.set(0,S.yaw,0);rootQ.setFromEuler(root.rotation);root.updateMatrixWorld(true);
    _eu.set(rad(p.pitch),rad(p.yaw),rad(p.roll),'YXZ');bodyQ.setFromEuler(_eu);const pel=hip0.clone().add(V(...p.p));
    {const wp=W(pel.clone());B.Hip.parent.updateMatrixWorld(true);B.Hip.position.copy(B.Hip.parent.worldToLocal(wp));setWQ(B.Hip,rootQ.clone().multiply(bodyQ).multiply(BQ.Hip))}
    const qWB=rootQ.clone().multiply(bodyQ),up=_Y.clone().applyQuaternion(qWB),rt=_X.clone().applyQuaternion(qWB),fw=_Z.clone().applyQuaternion(qWB);
    for(const[n,k]of[['Waist',.3],['Spine01',.35],['Spine02',.35]]){rotW(B[n],up,rad(p.tw)*k);rotW(B[n],rt,rad(p.bend)*k);rotW(B[n],fw,rad(p.side)*k)}
    const chestQ=bodyQ.clone().multiply(new T.Quaternion().setFromAxisAngle(_Y,rad(p.tw)));
    rotW(B.NeckTwist01,up,rad(p.headY)*.4);rotW(B.Head,up,rad(p.headY)*.6);const rt2=_X.clone().applyQuaternion(rootQ.clone().multiply(chestQ));rotW(B.NeckTwist01,rt2,rad(p.headP)*.4);rotW(B.Head,rt2,rad(p.headP)*.6);
    for(const sd of['L','R']){const air=clamp(p['air'+sd],0,1),fy=rad(p['fy'+sd]);const gp=V(...p['f'+sd]).add(FOFF),bp=bodyPt(p['bf'+sd],pel,bodyQ);const tgt=gp.lerp(bp,air);tgt.y=Math.max(tgt.y,ANK*.9);
      const fq=new T.Quaternion().setFromAxisAngle(_Y,fy);if(air>0)fq.slerp(bodyQ,air);const pole=V(0,0,1).applyQuaternion(fq).transformDirection(src.matrixWorld);
      twoBone(B[sd+'_Thigh'],B[sd+'_Calf'],B[sd+'_Foot'],LL[sd][0],LL[sd][1],W(tgt.clone()),pole);
      const pt=clamp(p['pt'+sd],-.5,1);_q.setFromAxisAngle(_X,rad(55)*pt);setWQ(B[sd+'_Foot'],rootQ.clone().multiply(fq).multiply(_q).multiply(BQ[sd+'_Foot']))}
    const cq=rootQ.clone().multiply(chestQ);
    for(const sd of['L','R']){const hand=bodyPt(p['h'+sd],pel,chestQ);const pole=V(...p['e'+sd]).applyQuaternion(chestQ).transformDirection(src.matrixWorld);
      twoBone(B[sd+'_Upperarm'],B[sd+'_Forearm'],B[sd+'_Hand'],LA[sd][0],LA[sd][1],W(hand),pole);
      const an=U['palm'+sd],cw=an.userData.fw.clone().applyQuaternion(B[sd+'_Hand'].getWorldQuaternion(_wq)),des=V(...p['b'+sd]).normalize().applyQuaternion(cq).normalize();
      cw.normalize();const ang=Math.acos(clamp(cw.dot(des),-1,1));if(ang>1e-3){const ax=cw.clone().cross(des).normalize();rotW(B[sd+'_Hand'],ax,Math.min(ang,rad(85)))}}
    for(const[b,q]of CURL)b.quaternion.multiply(q);
    // wings: Wing1 beats from the shoulder blade, Wing2 lags behind it so the tips trail and snap
    if(B.L_Wing1){const ph=S.fph,a1=rad(p.fb+p.fa*Math.sin(ph)),a2=rad(p.fa*.7*Math.sin(ph-.9)),sw=rad(p.fs+6*Math.cos(ph));const wq=rootQ.clone().multiply(chestQ),wf=_Z.clone().applyQuaternion(wq),wu=_Y.clone().applyQuaternion(wq);
      rotW(B.L_Wing1,wu,sw);rotW(B.L_Wing1,wf,-a1);rotW(B.L_Wing2,wf,-a2);rotW(B.R_Wing1,wu,-sw);rotW(B.R_Wing1,wf,a1);rotW(B.R_Wing2,wf,a2)}
    src.updateMatrixWorld(true);
    // the lash: a chain of segments out of her right fist, aimed by wv and curled by wc, with a ripple running down it
    {const hp=U.palmR.getWorldPosition(V()),wq=rootQ.clone().multiply(chestQ);let dir=V(...p.wv).normalize().applyQuaternion(wq);const upW=_Y,nw=performance.now()/1000;let pt=hp.clone();
      for(let i=0;i<LN;i++){const ax=dir.clone().cross(upW);if(ax.lengthSq()<1e-4)ax.copy(_X.clone().applyQuaternion(wq));ax.normalize();const k=i/LN;dir.applyAxisAngle(ax,-(p.wc||0)*(1+k*1.2)+Math.sin(nw*7-i*.7)*.05*(1-p.wl*0));
        const nx=pt.clone().addScaledVector(dir,SEG*sc);const m=LSEG[i];m.position.copy(pt).lerp(nx,.5);m.quaternion.setFromUnitVectors(_Y,dir);m.scale.set(sc*(1-k*.6),sc,sc*(1-k*.6));LPTS[i+1].copy(nx);pt=nx}
      LPTS[0].copy(hp);U.lashTip=pt;ember.position.copy(pt);ember.material.opacity=.35+.25*Math.sin(nw*9)}
    // props by job; loads ride in the hands
    sickle.visible=false;hatchet.visible=false;{const pL=U.palmL.getWorldPosition(V()),pR=U.palmR.getWorldPosition(V()),d=pR.clone().sub(pL),L=d.length()||1;d.multiplyScalar(1/L);oar.position.copy(pL).addScaledVector(d,(-.32+(p.slide||0))*sc);oar.quaternion.setFromUnitVectors(_Y,d);const hd=B.Head.getWorldPosition(V());U.eyeGlow.position.copy(hd).add(W(V(0,0,.05)).sub(W(V(0,0,0))));U.eyeGlow.material.opacity=.55+.25*Math.sin(performance.now()/300)}
    {const pL=U.palmL.getWorldPosition(V()),pR=U.palmR.getWorldPosition(V());block.visible=S.ld>.3;if(block.visible){block.position.copy(pL).lerp(pR,.5);block.position.y+=.08*sc;block.position.add(W(V(0,0,-.04)).sub(W(V(0,0,0))));block.rotation.set(0,S.yaw,-.04)}
     jar.visible=S.lw>.3&&S.ld<.3;if(jar.visible){jar.position.copy(pR);jar.position.y+=.01*sc;jar.rotation.set(0,S.yaw,.25)}
     const dr=S.clip==='draw';bucket.visible=rope.visible=dr;if(dr){const k=(S.t%.6)/.6,front=W(V(0,0,.32)),top=pL.clone().lerp(pR,.5);bucket.position.set(front.x,(.05+.1*k)*sc,front.z);const a=top,b=bucket.position.clone();b.y+=.03*sc;rope.position.copy(a).lerp(b,.5);rope.scale.set(sc,a.distanceTo(b),sc);rope.quaternion.setFromUnitVectors(_Y,b.clone().sub(a).normalize())}}
    const gL=U.palmL.getWorldPosition(V()),gR=U.palmR.getWorldPosition(V());
    const gl=clamp(p.glow||0,0,1);seedGlow.position.copy(gR).lerp(gL,.5);seedGlow.material.opacity=gl*.9;seedGlow.scale.setScalar(((S.clip==='cast'||S.clip==='thorns'?.08+gl*.12:.05+gl*.07)+Math.sin(performance.now()/120)*.008*gl)*sc);
    if(gl>.3&&Math.random()<gl*dt*16)mote(seedGlow.position.clone(),V((Math.random()-.5)*.25,.3+Math.random()*.3,(Math.random()-.5)*.25).multiplyScalar(sc),Math.random()<.4?'#c8ff9a':'#5fd84a',.8);
    // the sprout grows where he pressed the seed, and stays until his next planting
    if(S.clip==='plant'&&S.t<.5){S.sp=W(V(0,0,.25+.0));S.spg=0}const gw=clamp(p.grow||0,0,1);if(S.sp){S.spg=S.clip==='plant'?gw:S.spg;sprout.position.set(S.sp.x,0,S.sp.z);const e=E.out(S.spg);sprout.scale.setScalar(Math.max(.0001,e*sc*1.3));sprout.rotation.y=S.yaw;sprout.userData.leaves.forEach((l,i)=>{l.rotation.z=.5+(1-clamp(S.spg*1.6-i*.15,0,1))*1.2})}
    if(S.hitNow==='thorns'){const hp=U.palmR.getWorldPosition(V());hp.y=.01*sc;for(let i=0;i<14;i++)mote(hp.clone(),V((Math.random()-.5)*.7,.3+Math.random()*.4,(Math.random()-.5)*.7).multiplyScalar(sc),Math.random()<.5?'#8a6a48':'#5fd84a',.6)}
    if(S.hitNow==='pound'){const tp=oar.localToWorld(V(0,1.08,0));tp.y=.01*sc;for(let i=0;i<18;i++)mote(tp.clone(),V((Math.random()-.5)*1.1,.2+Math.random()*.5,(Math.random()-.5)*1.1).multiplyScalar(sc),Math.random()<.5?'#7fe0d0':'#c9b38a',.6);shake(.6)}
    if(S.hitNow==='thrust'||S.hitNow==='rise'){const tp=oar.localToWorld(V(0,1.08,0));for(let i=0;i<8;i++)mote(tp.clone(),V((Math.random()-.5)*.5,.1+Math.random()*.3,(Math.random()-.5)*.5).multiplyScalar(sc),'#bff4ec',.45)}
    if(S.hitNow==='sweep'){const tp=oar.localToWorld(V(0,1.08,0));for(let i=0;i<10;i++)mote(tp.clone(),V((Math.random()-.5)*.6,.15+Math.random()*.4,(Math.random()-.5)*.6).multiplyScalar(sc),Math.random()<.5?'#7fe0d0':'#bff4ec',.5)}
    if(S.hitNow==='lash'||S.hitNow==='slash'||S.hitNow==='wrath'){const tp=(U.lashTip||U.palmR.getWorldPosition(V())).clone();const n=S.hitNow==='wrath'?26:10;if(S.hitNow==='wrath')tp.y=.01*sc;for(let i=0;i<n;i++)mote(tp.clone(),V((Math.random()-.5)*(S.hitNow==='wrath'?1.3:.5),.15+Math.random()*.5,(Math.random()-.5)*(S.hitNow==='wrath'?1.3:.5)).multiplyScalar(sc),QU?(Math.random()<.5?'#9dffb0':'#e8bf4e'):(Math.random()<.5?'#ff7a2a':'#ffd27a'),.55);shake(S.hitNow==='wrath'?.7:.12)}
    if(S.hitNow==='talon'){const tp=B.L_Foot.getWorldPosition(V());for(let i=0;i<8;i++)mote(tp.clone(),V((Math.random()-.5)*.5,.1+Math.random()*.3,(Math.random()-.5)*.5).multiplyScalar(sc),'#ffd9c0',.4);shake(.1)}
    if(S.clip==='wrath'&&S.t>.4&&S.t<1.05&&Math.random()<dt*24){const hd=B.Head.getWorldPosition(V());mote(hd,V((Math.random()-.5)*.9,(Math.random()-.3)*.5,(Math.random()-.5)*.9).multiplyScalar(sc),QU?'#7dffb0':'#ff4a2a',.5)}
    if(S.hitNow==='chop'||S.hitNow==='mine'){chips(hatchet.userData.tip.getWorldPosition(V()),12)}else if(S.hitNow==='reap'){for(let i=0;i<10;i++)mote(sickle.userData.tip.getWorldPosition(V()),V((Math.random()-.5)*.6,.2+Math.random()*.5,(Math.random()-.5)*.6).multiplyScalar(sc),Math.random()<.5?'#e8cf82':'#d9b44e',.6)}S.hitNow=null;
    for(let i=MOTE.length-1;i>=0;i--){const q=MOTE[i];q.t+=dt;q.m.position.addScaledVector(q.v,dt);q.v.y-=dt*.15*sc;q.m.material.opacity=Math.max(0,1-q.t/q.L);if(q.t>q.L){SCN.remove(q.m);MOTE.splice(i,1)}}
    for(let i=SPK.length-1;i>=0;i--){const q=SPK[i];q.t+=dt;if(q.t<0){q.m.visible=false;continue}q.m.visible=true;const k=q.t<.12?E.out(q.t/.12):q.t>1.1?Math.max(0,1-(q.t-1.1)/.35):1;q.m.position.y=q.m.userData.h*(k-1)*.5+q.m.userData.h*.5*k;q.m.scale.setScalar(sc*Math.max(.01,k));if(q.t>1.45){SCN.remove(q.m);SPK.splice(i,1)}}
    for(let i=CHIP.length-1;i>=0;i--){const q=CHIP[i];q.t+=dt;q.v.y-=dt*3*sc;q.m.position.addScaledVector(q.v,dt);if(q.m.position.y<.003){q.m.position.y=.003;q.v.multiplyScalar(.3)}q.m.rotation.x+=q.r.x*dt;q.m.rotation.y+=q.r.y*dt;if(q.t>1.4){SCN.remove(q.m);CHIP.splice(i,1)}}
    for(const m of U.mats)m.emissive&&m.emissive.setHex(I.flash?0xffffff:0)}
  return{U,S,scene:SCN,get cur(){return cur},playG,tick,clips:CL}};
