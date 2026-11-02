// ---------- Celtic archer: Tripo humanoid on the same full-body pose system as the Nubian (pelvis path, spine, head, IK arms and legs),
// plus a bow placed in the left fist every frame, a live bowstring, an arrow carried from the quiver to the nock, and a back quiver ----------
FACT.archer=function(){const LAB=(typeof GLAB==='function')?GLAB('archer'):window.LABCFG;const G0=window.MODELS&&window.MODELS.archer||window.TRIPO;const src=T.SkeletonUtils.clone(G0.scene);const U={mats:[]};const V=(x,y,z)=>new T.Vector3(x||0,y||0,z||0);const SCN=scene;
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
  const ANK=BP.L_Foot.y;const FOFF=V((BP.L_Foot.x+BP.R_Foot.x)/2-.004,0,(BP.L_Foot.z+BP.R_Foot.z)/2-.033);
  // left hand closed round the grip; right hand in a draw hook (index, middle, ring curled at the tips, thumb tucked)
  const CURL=[];for(const sd of['L','R'])for(const f of['Index','Mid','Ring','Pinky','Thumb'])for(let k=1;k<=3;k++){const n=sd+'_'+f+k;if(!B[n])continue;
    const ax=(f==='Thumb'?V(0,1,0):V(0,0,1)).applyQuaternion(BQ[n].clone().invert()).normalize();const a=sd==='L'?(f==='Thumb'?.5:k===1?1.25:1.35):(f==='Thumb'?.7:f==='Pinky'?(k===1?1.2:1.3):(k===1?.35:1.1));CURL.push([B[n],new T.Quaternion().setFromAxisAngle(ax,(sd==='L'?-1:1)*a)])}
  // palm anchors (no mesh): where the fist closes, with the thumb direction kept for wrist alignment
  function anchor(sd){const g=new T.Group();const hq=BQ[sd+'_Hand'].clone().invert(),fw=V(0,0,1).applyQuaternion(hq).normalize(),len=BP[sd+'_Mid1'].clone().sub(BP[sd+'_Hand']).applyQuaternion(hq).normalize();
    g.position.copy(len).multiplyScalar(BP[sd+'_Mid1'].distanceTo(BP[sd+'_Hand'])*.6).addScaledVector(V(0,-1,0).applyQuaternion(hq),.012);B[sd+'_Hand'].add(g);g.userData.fw=fw;return g}
  U.palmL=anchor('L');U.palmR=anchor('R');
  // ---- props ----
  const woodM=M('#7a5232'),woodD=M('#5a3a22'),wrapM=M('#2f5a3a'),goldM=M('#d8aa48'),featherM=M('#e8e0cc'),featherR=M('#b8402e'),leatherM=M('#6b4428'),strM=new T.LineBasicMaterial({color:'#f4ead2'}),headM=M('#c9ccd6');
  for(const x of[woodM,woodD,wrapM,goldM,featherM,featherR,leatherM,headM]){x.userData.outlineParameters={visible:false};U.mats.push(x)}
  // bow: a short recurve, belly toward the archer (-x), back toward the target (+x), limbs along y. Unscaled model units (she is 1 tall).
  const BH=.27,bowPts=[];for(let i=0;i<=16;i++){const y=-BH+2*BH*i/16,u=Math.abs(y)/BH;const x=-.075*u*u+.03*Math.max(0,(u-.82)/.18)**2;bowPts.push(V(x,y,0))}
  const bowCurve=new T.CatmullRomCurve3(bowPts);const bow=new T.Group();const limb=new T.Mesh(new T.TubeGeometry(bowCurve,40,.0075,6,false),woodM);bow.add(limb);
  {const gr=new T.Mesh(new T.CylinderGeometry(.011,.011,.07,8),wrapM);bow.add(gr);for(const y of[-.04,.04]){const r=new T.Mesh(new T.CylinderGeometry(.0125,.0125,.008,8),goldM);r.position.y=y;bow.add(r)}
    for(const s of[-1,1]){const t=new T.Mesh(new T.SphereGeometry(.009,6,4),goldM);t.position.copy(bowPts[s<0?0:16]);bow.add(t)}}
  const tipT=bowPts[16].clone(),tipB=bowPts[0].clone(),REST=V(-.075*1.0+.004,0,0);  // string rest point at the grip height
  bow.scale.setScalar(sc);SCN.add(bow);U.bow=bow;
  const sGeo=new T.BufferGeometry().setFromPoints([V(),V(),V()]);const string=new T.Line(sGeo,strM);string.frustumCulled=false;SCN.add(string);U.string=string;
  // arrow: shaft along +z from the nock (z=0) to the head (z=AL)
  const AL=.34;function mkArrow(){const g=new T.Group();const sh=new T.Mesh(new T.CylinderGeometry(.0035,.0035,AL,5),woodD);sh.rotation.x=Math.PI/2;sh.position.z=AL/2;g.add(sh);
    const hd=new T.Mesh(new T.ConeGeometry(.009,.035,4),headM);hd.rotation.x=Math.PI/2;hd.position.z=AL+.012;g.add(hd);
    for(let i=0;i<3;i++){const f=new T.Mesh(new T.PlaneGeometry(.018,.055),i?featherM:featherR);f.position.z=.04;f.rotation.z=i*TAU/3;f.position.x=Math.cos(i*TAU/3+Math.PI/2)*.008;f.position.y=Math.sin(i*TAU/3+Math.PI/2)*.008;f.rotation.y=Math.PI/2;f.material.side=T.DoubleSide;g.add(f)}
    g.scale.setScalar(sc);return g}
  const arrow=mkArrow();SCN.add(arrow);U.arrow=arrow;U.mkArrow=mkArrow;
  // quiver on the back, mouth over the right shoulder, fletchings showing
  const quiver=new T.Group();{const q=new T.Mesh(new T.CylinderGeometry(.03,.024,.23,10,1,true),leatherM);q.material.side=T.DoubleSide;quiver.add(q);
    const bt=new T.Mesh(new T.CircleGeometry(.024,10),leatherM);bt.rotation.x=Math.PI/2;bt.position.y=-.115;quiver.add(bt);
    for(const y of[.1,-.08]){const r=new T.Mesh(new T.TorusGeometry(.03,.004,4,12),goldM);r.rotation.x=Math.PI/2;r.position.y=y;quiver.add(r)}
    for(let i=0;i<5;i++){const a=mkArrow();a.scale.setScalar(1);a.rotation.x=-Math.PI/2;a.position.set(Math.cos(i*1.3)*.012,.115-AL+.03+((i*7)%3)*.008,Math.sin(i*1.3)*.012);quiver.add(a)}
    const strap=new T.Mesh(new T.TorusGeometry(.2,.005,4,24,Math.PI*.9),leatherM);strap.rotation.z=Math.PI*.55;strap.position.set(.05,-.02,.0);}
  {const sp=B.Spine02;const at=V(-.05,.8,hip0.z-.13).applyMatrix4(src.matrixWorld);const tilt=new T.Quaternion().setFromEuler(new T.Euler(-.12,0,.55));
    SCN.add(quiver);quiver.scale.setScalar(sc);const sq0=sp.getWorldQuaternion(new T.Quaternion()),sp0=sp.getWorldPosition(V()),qw0=root.getWorldQuaternion(new T.Quaternion()).multiply(tilt);U.qOff=at.clone().sub(sp0).applyQuaternion(sq0.clone().invert());U.qRot=sq0.clone().invert().multiply(qw0)}
  U.quiver=quiver;
  const GC='#4fd84a';const GLW=(()=>{const c=document.createElement('canvas');c.width=c.height=64;const g=c.getContext('2d'),gr=g.createRadialGradient(32,32,0,32,32,31);gr.addColorStop(0,'rgba(255,255,255,1)');gr.addColorStop(.35,'rgba(255,255,255,.7)');gr.addColorStop(1,'rgba(255,255,255,0)');g.fillStyle=gr;g.fillRect(0,0,64,64);return new T.CanvasTexture(c)})();U.GLW=GLW;
  const tipGlow=egSprite(GLW,.12,'#b6ff8c');tipGlow.material.opacity=0;SCN.add(tipGlow);
  const bowGlow=egSprite(GLW,.3,'#8dff6a');bowGlow.material.opacity=0;SCN.add(bowGlow);
  const runeM=new T.MeshBasicMaterial({color:'#3fbf3a',transparent:true,opacity:0,depthWrite:false,side:T.DoubleSide});runeM.userData={noflash:true};
  const rune=new T.Group();{const r1=new T.Mesh(new T.RingGeometry(.3,.33,48),runeM);r1.rotation.x=-Math.PI/2;rune.add(r1);const r2=new T.Mesh(new T.RingGeometry(.2,.215,36),runeM);r2.rotation.x=-Math.PI/2;rune.add(r2);
    for(let i=0;i<6;i++){const a=i/6*TAU;const sp=new T.Mesh(new T.PlaneGeometry(.022,.07),runeM);sp.rotation.x=-Math.PI/2;sp.rotation.z=a;sp.position.set(Math.sin(a)*.26,0,Math.cos(a)*.26);rune.add(sp)}}
  rune.scale.setScalar(sc);rune.position.y=.004;SCN.add(rune);
  const MOTE=[];function mote(from,to,col,life){const m=egSprite(GLW,.04,col||GC,false);m.position.copy(from);SCN.add(m);MOTE.push({m,a:from.clone(),b:to,t:0,L:life||.7,sw:Math.random()*TAU})}
  const BURST=[];function burstAt(p,n,col){for(let i=0;i<n;i++){const m=egSprite(GLW,.045,col||GC,false);m.position.copy(p);SCN.add(m);const a=Math.random()*TAU,e=(Math.random()-.3)*1.2;BURST.push({m,v:V(Math.cos(a)*Math.cos(e),Math.sin(e)+.3,Math.sin(a)*Math.cos(e)).multiplyScalar((.5+Math.random()*.7)*sc),t:0,L:.45+Math.random()*.25})}}
  U.burstAt=burstAt;U.GC=GC;
  // ---- poses (chest frame: +x points at the target, +z out of the chest; feet are planted model-space points unless air>0) ----
  const E={io:t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2,out:t=>1-Math.pow(1-t,3),in:t=>t*t*t,lin:t=>t};
  const SY=SHL.y;
  const ST={p:[0,-.07,0],yaw:-55,pitch:6,roll:0,tw:-28,bend:4,side:0,headP:-4,headY:76,
    hL:[.17,.04,.12],hR:[.06,.07,.13],bL:[.35,1,.15],bR:[.3,.1,1],eL:[.3,-1,.1],eR:[-.6,-.8,.2],
    fL:[.05,ANK,.13],fR:[-.07,ANK,-.13],fyL:-25,fyR:-80,ptL:0,ptR:0,airL:0,airR:0,bfL:[.07,-.36,.08],bfR:[-.08,-.38,-.06],draw:0,arw:0,charge:0,hwL:0,hwR:0,hgL:[0,0,0],hgR:[0,0,0]};
  const K=(t,o,lf)=>[t,Object.assign(JSON.parse(JSON.stringify(ST)),o||{}),lf||{}];
  const NUM=Object.keys(ST).filter(k=>!['fL','fR','fyL','fyR'].includes(k));
  const QV=[SHR.x+.03,SY+.09,-.09],AIM_L=[SHL.x+.255,SY+.01,.0],ANCH=[.025,SY+.045,.03];
  // the attack: poised crouch, lateral leap with a twist, draw from the quiver, nock, full draw to the cheek, release at the top,
  // soft landing on one foot, absorb through the knee, low pivot, hop back into the ready stance
  const SHOT=[
    K(0),
    K(.14,{p:[.02,-.2,0],pitch:14,bend:10,headP:-10,hL:[.15,-.02,.12],hR:[.05,.02,.12],eL:[.3,-1,.2]}),                                   // poised crouch
    K(.24,{p:[-.1,-.13,0],yaw:-40,pitch:10,roll:-10,tw:-36,bend:6,hL:[.18,.05,.1],hR:[QV[0]+.06,QV[1]-.08,QV[2]+.08],eR:[-.3,.6,-.4]},{fR:[-.12,ANK+.03,-.15],lfR:.03}),   // drive off: weight thrown sideways, right hand starts up
    K(.34,{p:[-.24,.06,0],yaw:-12,pitch:2,roll:-22,tw:-48,bend:0,side:-6,headY:60,hL:[.24,.12,.06],bL:[.6,1,.1],hR:QV,eR:[-.2,1,-.3],arw:1,airL:1,airR:1,bfL:[.1,-.3,.12],bfR:[-.06,-.34,-.1],ptL:.7,ptR:.6}),  // airborne, twisting, hand at the quiver
    K(.46,{p:[-.36,.14,0],yaw:-34,pitch:0,roll:-16,tw:-48,side:-4,headY:78,hL:[.3,.2,.03],bL:[.15,1,.05],hR:[.16,.2,.06],eR:[-1,.2,0],arw:1,airL:1,airR:1,bfL:[.09,-.27,.16],bfR:[-.04,-.33,-.12],ptL:.7,ptR:.7}), // arrow comes over, nocked
    K(.58,{p:[-.44,.16,0],yaw:-48,pitch:-2,roll:-10,tw:-40,side:-2,headP:-2,headY:84,hL:AIM_L,bL:[.04,1,.02],hR:ANCH,eR:[-1,.35,0],eL:[0,-1,-.3],draw:1,arw:1,airL:1,airR:1,bfL:[.1,-.25,.15],bfR:[-.03,-.31,-.13],ptL:.7,ptR:.7}), // full draw at the top
    K(.66,{p:[-.48,.13,0],yaw:-50,pitch:-2,roll:-8,tw:-40,headY:84,hL:AIM_L,bL:[.04,1,.02],hR:ANCH,eR:[-1,.35,0],eL:[0,-1,-.3],draw:1,arw:1,airL:1,airR:1,bfL:[.1,-.27,.14],bfR:[-.03,-.33,-.12],ptL:.6,ptR:.7}),  // hold
    K(.7,{p:[-.5,.1,0],yaw:-50,pitch:-3,roll:-8,tw:-42,headY:84,hL:[AIM_L[0]+.01,AIM_L[1],AIM_L[2]],bL:[.1,1,.05],hR:[-.07,SY+.09,-.03],eR:[-1,.5,-.2],eL:[0,-1,-.3],draw:0,arw:0,airL:1,airR:.8,bfL:[.09,-.3,.13],bfR:[-.04,-.36,-.08],ptL:.6,ptR:.5}),  // release: string snaps, hand flies back
    K(.82,{p:[-.54,-.02,0],yaw:-52,pitch:4,roll:-4,tw:-36,headY:80,hL:[.28,.12,.06],bL:[.3,1,.1],hR:[-.04,.13,.04],eR:[-.8,-.3,-.2],airL:.55,airR:.9,bfL:[.07,-.4,.1],bfR:[-.05,-.35,-.06],ptL:.3,ptR:.5},{fL:[-.5,ANK,.12],fyL:-30}), // reaching for the ground
    K(.9,{p:[-.53,-.12,0],yaw:-54,pitch:14,roll:4,tw:-32,bend:10,headY:78,hL:[.24,.06,.1],bL:[.35,1,.15],hR:[.02,.08,.1],airL:0,airR:.8,bfR:[-.05,-.32,-.08],ptL:0,ptR:.5}),   // lands soft on the left foot
    K(1.0,{p:[-.5,-.24,0],yaw:-54,pitch:20,roll:2,tw:-30,bend:16,headP:-12,headY:76,hL:[.2,.0,.12],hR:[.04,.03,.12],airR:.6,bfR:[-.06,-.3,-.1],ptR:.4}),               // absorbs through the bent knee
    K(1.1,{p:[-.44,-.25,0],yaw:-50,pitch:18,tw:-26,bend:14,airR:0,ptR:0},{fR:[-.48,ANK,-.15],fyR:-80,lfR:.02}),                                                             // other foot down
    K(1.26,{p:[-.38,-.24,0],yaw:-22,pitch:16,tw:-50,bend:12,headY:70,hL:[.22,.02,.12],hR:[.05,.04,.12]},{fyL:-6}),                                                            // low pivot on the front foot
    K(1.42,{p:[-.24,-.16,0],yaw:-48,pitch:10,tw:-30,bend:8,headY:76,ptL:.35,ptR:.35},{fL:[-.16,ANK,.13],fyL:-22,lfL:.06,fR:[-.25,ANK,-.13],fyR:-80,lfR:.06}),            // hop back
    K(1.6,{p:[-.02,-.1,0],yaw:-55,pitch:6,ptL:.3,ptR:.3},{fL:[.05,ANK,.13],fyL:-25,lfL:.06,fR:[-.07,ANK,-.13],fyR:-80,lfR:.06}),
    K(1.8,{})];
  {let fL=ST.fL,fR=ST.fR,yL=ST.fyL,yR=ST.fyR;for(const k of SHOT){const m=k[2];if(m.fL)fL=m.fL;if(m.fR)fR=m.fR;if(m.fyL!=null)yL=m.fyL;if(m.fyR!=null)yR=m.fyR;k[1].fL=fL;k[1].fR=fR;k[1].fyL=yL;k[1].fyR=yR;k[1].lfL=m.lfL||0;k[1].lfR=m.lfR||0}}
  const REL=.7;
  // POWER SHOT: plant a wide stance, nock, a long trembling overdraw while the god's green power spirals into the arrowhead, then a release that rocks her back
  const PW=[
    K(0),
    K(.25,{p:[0,-.16,-.02],pitch:8,bend:6,headP:-6,hL:[.16,0,.12],hR:[.05,.03,.12]},{fL:[.03,ANK,.21],fyL:-15,lfL:.05,fR:[-.06,ANK,-.21],fyR:-86,lfR:.04}),
    K(.5,{p:[0,-.18,-.02],pitch:6,tw:-34,headY:80,hL:[.18,.04,.1],hR:QV,eR:[-.2,1,-.3],arw:1}),
    K(.78,{p:[0,-.18,0],tw:-38,headY:82,hL:[.3,.18,.04],bL:[.1,1,.05],hR:[.17,.19,.06],eR:[-1,.2,0],arw:1}),
    K(1.0,{p:[0,-.19,-.01],tw:-40,headY:84,hL:AIM_L,bL:[.04,1,.02],hR:[.1,SY+.03,.04],eR:[-1,.35,0],eL:[0,-1,-.3],draw:.5,arw:1,charge:.12}),
    K(1.75,{p:[0,-.215,-.035],pitch:1,tw:-43,bend:-3,headP:-3,headY:86,hL:[AIM_L[0]+.005,AIM_L[1]+.005,0],bL:[.04,1,.02],hR:[-.035,SY+.05,.025],eR:[-1,.45,0],eL:[0,-1,-.3],draw:1,arw:1,charge:1}),
    K(1.92,{p:[0,-.22,-.04],pitch:1,tw:-43,bend:-3,headP:-3,headY:86,hL:[AIM_L[0]+.005,AIM_L[1]+.005,0],bL:[.04,1,.02],hR:[-.04,SY+.05,.025],eR:[-1,.45,0],eL:[0,-1,-.3],draw:1,arw:1,charge:1}),
    K(1.98,{p:[0,-.2,-.1],pitch:-7,tw:-44,bend:-6,headP:-8,headY:84,hL:[AIM_L[0]-.03,AIM_L[1]+.06,.01],bL:[.35,1,0],hR:[-.15,SY+.1,-.05],eR:[-1,.6,-.2],eL:[0,-1,-.3],draw:0,arw:0,charge:0}),
    K(2.18,{p:[0,-.18,-.08],pitch:-2,tw:-38,bend:0,headY:82,hL:[.27,.15,.06],bL:[.3,1,.1],hR:[-.06,.13,.02],eR:[-.8,-.3,-.2]}),
    K(2.45,{p:[0,-.11,-.02]},{fL:[.05,ANK,.13],fyL:-25,lfL:.04,fR:[-.07,ANK,-.13],fyR:-80,lfR:.04}),
    K(2.7,{})];
  {let fL=ST.fL,fR=ST.fR,yL=ST.fyL,yR=ST.fyR;for(const k of PW){const m=k[2];if(m.fL)fL=m.fL;if(m.fR)fR=m.fR;if(m.fyL!=null)yL=m.fyL;if(m.fyR!=null)yR=m.fyR;k[1].fL=fL;k[1].fR=fR;k[1].fyL=yL;k[1].fyR=yR;k[1].lfL=m.lfL||0;k[1].lfR=m.lfR||0}}
  const PREL=1.96;
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
  const STANCE=()=>JSON.parse(JSON.stringify(ST));
  const CL={idle:{dur:3.4,loop:true,fn:t=>{const o=STANCE(),s=Math.sin(t/3.4*TAU);o.p=[0,-.07+s*.005,0];o.bend+=s*1.5;o.headY+=Math.sin(t/3.4*TAU*.5)*6;o.hL=[.17,.04+s*.005,.12];o.hR=[.06,.07+s*.005,.13];return o}},
    shot:{dur:1.8,fn:t=>sampleKeys(SHOT,t),hits:[[REL,1]]},
    power:{dur:2.7,fn:t=>{const o=sampleKeys(PW,t);if(t>1&&t<1.95){const a=.0035*o.charge,n=performance.now()/1000;o.hR=[o.hR[0]+Math.sin(n*61)*a,o.hR[1]+Math.sin(n*47+1)*a,o.hR[2]];o.hL=[o.hL[0],o.hL[1]+Math.sin(n*53+2)*a*.6,o.hL[2]]}return o},hits:[[PREL,2.5]]}};
  CL.combo=CL.shot;CL.bolt=CL.shot;CL.special=CL.power;
  const S={x:0,z:0,yaw:0,vel:0,wamt:0,clip:'idle',t:0,rate:1,hold:false,prev:null,bl:0,blT:.18,base:0};let cur=CL.idle.fn(0);
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
  // ---- run: light and quick, bow carried low in the left hand, right arm pumping ----
  let wph=0;const STRIDE=1.3,DUTY=.36,_X=V(1,0,0),_Y=V(0,1,0),_Z=V(0,0,1);
  const shake=v=>LAB.api&&LAB.api.shake&&LAB.api.shake(v);
  function walkPose(ph,bank){const o=STANCE(),u0=ph/TAU,A=STRIDE*DUTY/2,mid=TAU*DUTY/2,cm=Math.cos(ph-mid),c=Math.cos(ph);
    o.yaw=8*cm;o.tw=-12*cm;o.roll=1.5*cm+bank;o.side=0;o.pitch=14;o.bend=4;o.headP=-14;o.headY=-(o.yaw+o.tw)*.8;
    o.p=[.008*cm,-.04-.02*Math.cos(2*(ph-mid)),.025];
    for(const[sd,off,sgn]of[['L',0,1],['R',.5,-1]]){const u=(((u0+off)%1)+1)%1;let z,y=ANK,pt=0;
      if(u<DUTY){const k=u/DUTY;z=lerp(A,-A,k);pt=k<.25?.15:k>.55?.7*Math.pow((k-.55)/.45,1.1):0;y+=k>.55?.04*Math.pow((k-.55)/.45,1.4):0}
      else{const k=(u-DUTY)/(1-DUTY);const kz=k<.35?k*.25/.35:.25+.75*E.io((k-.35)/.65);z=lerp(-A*1.2,A*1.06,kz);
        y+=k<.45?.04+.16*Math.sin(k/.45*Math.PI/2):.2*Math.pow(1-(k-.45)/.55,1.6)*.92;pt=k<.4?.7:.7*(1-(k-.4)/.6)+.1}
      o['f'+sd]=[sgn*.05,y,z+.04];o['fy'+sd]=sgn*4;o['pt'+sd]=pt;
      const sw=-sgn*c;o['h'+sd]=[sgn*.14,.06+Math.max(0,sw)*.03,.04+sw*(sd==='L'?.04:.07)];o['e'+sd]=[sgn*.3,-.4,-1]}
    o.bL=[.2,1,.35];o.bR=[.2,.1,1];o.draw=0;o.arw=0;return o}
  function tick(dt,I){S.x=I.x;S.z=I.z;let df=((S.clip==='power'&&S.aimYaw!=null)?S.aimYaw:I.yaw)-S.yaw;df=Math.atan2(Math.sin(df),Math.cos(df));S.yaw+=df*Math.min(1,dt*(S.clip==='shot'||S.clip==='power'?14:10));S.vel=I.speed;
    const c=CL[S.clip];const t0=S.t;S.t+=dt*S.rate;if(c.hits)c.hits.forEach(([ht,k],i)=>{if(t0<ht&&S.t>=ht){if(LAB.onStrike)LAB.onStrike(k,i,U);shake(.06)}})
    if(!c.loop&&S.t>=c.dur&&!S.hold)playG('idle');const c2=CL[S.clip],tt=c2.loop?S.t%c2.dur:Math.min(S.t,c2.dur);let p=c2.fn(tt);
    if(S.bl>0&&S.prev){S.bl-=dt;p=mixP(S.prev,p,1-Math.max(0,S.bl)/S.blT)}cur=p;
    S.wamt+=(clamp(S.vel/.5,0,1)-S.wamt)*Math.min(1,dt*7);const wk=S.clip==='idle'?S.wamt:0;wph+=(I.dist||0)/(STRIDE*sc)*TAU;
    S.bank=(S.bank||0)+((clamp(-(dt>0?df/dt:0)*2.2,-9,9))-(S.bank||0))*Math.min(1,dt*4);
    if(wk>0)p=mixP(p,walkPose(wph,S.bank),Math.min(1,wk*1.4));
    for(const[b,q,ps]of BIND){b.quaternion.copy(q);b.position.copy(ps)}
    root.position.set(S.x,0,S.z);root.rotation.set(0,S.yaw,0);rootQ.setFromEuler(root.rotation);root.updateMatrixWorld(true);
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
    src.updateMatrixWorld(true);
    // bow in the left fist: limbs along the pose's bow axis, back facing the target (chest +x), belly toward the archer
    {const sp=B.Spine02,q=sp.getWorldQuaternion(new T.Quaternion());quiver.position.copy(sp.getWorldPosition(V())).add(U.qOff.clone().applyQuaternion(q));quiver.quaternion.copy(q).multiply(U.qRot)}
    const gL=U.palmL.getWorldPosition(V()),gR=U.palmR.getWorldPosition(V());
    const bup=V(...p.bL).normalize().applyQuaternion(cq).normalize();let bfw=V(1,0,0).applyQuaternion(cq);bfw.addScaledVector(bup,-bfw.dot(bup)).normalize();const bz=V().crossVectors(bfw,bup);
    bow.quaternion.setFromRotationMatrix(new T.Matrix4().makeBasis(bfw,bup,bz));bow.position.copy(gL);bow.updateMatrixWorld(true);
    // string: tips to the nock point; pulled to the right hand by the draw, and it twangs for a moment after the release
    const tT=tipT.clone().applyMatrix4(bow.matrixWorld),tB=tipB.clone().applyMatrix4(bow.matrixWorld),rest=REST.clone().applyMatrix4(bow.matrixWorld);
    const dr=clamp(p.draw||0,0,1);S.twang=Math.max(0,(S.twang||0)-dt);if(S.lastDraw>.6&&dr<.3)S.twang=.25;S.lastDraw=dr;
    const nock=rest.clone().lerp(gR,dr);if(S.twang>0)nock.addScaledVector(bfw,Math.sin(S.twang*90)*S.twang*.06*sc);
    const ps=sGeo.attributes.position;ps.setXYZ(0,tT.x,tT.y,tT.z);ps.setXYZ(1,nock.x,nock.y,nock.z);ps.setXYZ(2,tB.x,tB.y,tB.z);ps.needsUpdate=true;sGeo.computeBoundingSphere();
    // arrow: held in the right hand from the quiver, laid on the string and pointed through the grip
    const aw=clamp(p.arw||0,0,1);arrow.visible=aw>.5;if(arrow.visible){const from=dr>.05?nock:gR,dir=V().subVectors(gL,from);if(dir.lengthSq()<1e-6)dir.copy(bfw);dir.normalize();
      arrow.position.copy(from);arrow.quaternion.setFromUnitVectors(_Z,dir);U.arrowDir=dir;U.arrowPos=from.clone()}
    // power shot: charge glow on the arrowhead and bow, rune ring at her feet, motes spiralling in; a flash and burst on release
    const ch=clamp(p.charge||0,0,1);const head=arrow.visible?arrow.localToWorld(V(0,0,AL+.02)):gL;
    tipGlow.position.copy(head);tipGlow.material.opacity=ch;tipGlow.scale.setScalar((.04+ch*.08+Math.sin(performance.now()/90)*.012*ch)*sc*1.2);
    rune.position.x=S.x;rune.position.z=S.z;rune.rotation.y+=dt*(.6+ch*2.5);runeM.opacity=Math.min(.85,ch*1.1);rune.scale.setScalar(sc*(.85+ch*.35));
    if(ch>.05&&Math.random()<ch*dt*40){const a=Math.random()*TAU,r=(.35+Math.random()*.25)*sc;mote(V(S.x+Math.cos(a)*r,(.1+Math.random()*.7)*sc,S.z+Math.sin(a)*r),head,Math.random()<.3?'#a8f07a':GC,.55)}
    if(S.lastCh>.7&&ch<.2){S.flash=.35;burstAt(gL,26);burstAt(head,14,'#a8f07a');shake(.4)}S.lastCh=ch;
    S.flash=Math.max(0,(S.flash||0)-dt);bowGlow.position.copy(gL);bowGlow.material.opacity=Math.max(ch*.25,S.flash/.35*.8);bowGlow.scale.setScalar((.12+ch*.06+(S.flash>0?(.35-S.flash)*.8:0))*sc);
    for(let i=MOTE.length-1;i>=0;i--){const q=MOTE[i];q.t+=dt;const k=Math.min(1,q.t/q.L),e=k*k;const bb=q.b;q.m.position.lerpVectors(q.a,bb,e);q.m.position.x+=Math.cos(q.sw+k*6)*(1-k)*.08*sc;q.m.position.z+=Math.sin(q.sw+k*6)*(1-k)*.08*sc;q.m.material.opacity=Math.sin(k*Math.PI);if(k>=1){SCN.remove(q.m);MOTE.splice(i,1)}}
    for(let i=BURST.length-1;i>=0;i--){const q=BURST[i];q.t+=dt;q.m.position.addScaledVector(q.v,dt);q.v.multiplyScalar(Math.exp(-dt*3));q.m.material.opacity=Math.max(0,1-q.t/q.L);if(q.t>q.L){SCN.remove(q.m);BURST.splice(i,1)}}
    for(const m of U.mats)m.emissive&&m.emissive.setHex(I.flash?0xffffff:0)}
  return{U,S,scene:SCN,get cur(){return cur},playG,tick,clips:CL}};
