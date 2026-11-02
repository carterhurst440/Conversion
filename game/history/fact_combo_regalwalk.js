// ---------- Tripo humanoid with a full-body pose system: pelvis path, spine twist/bend, head, IK arms with wrists aligned to the blades,
// IK legs to authored foot positions (planted feet locked, moving feet in lifted arcs), finger fists, twin sais and trails ----------
FACT.combo=function(){const G0=window.TRIPO;const src=T.SkeletonUtils.clone(G0.scene);const U={mats:[]};const V=(x,y,z)=>new T.Vector3(x||0,y||0,z||0);
  const root=new T.Group();scene.add(root);root.add(src);U.root=root;const B={};src.traverse(o=>{if(o.isBone)B[o.name]=o});
  src.updateMatrixWorld(true);const box=new T.Box3();src.traverse(o=>{if(o.isMesh){o.geometry.computeBoundingBox();box.union(o.geometry.boundingBox)}});
  const sc=(LAB.mh||1)/(box.max.y-box.min.y);src.scale.setScalar(sc);
  const soft=(()=>{const d=new Uint8Array([176,176,176,255,222,222,222,255,255,255,255,255]);const t=new T.DataTexture(d,3,1,T.RGBAFormat);t.minFilter=t.magFilter=T.LinearFilter;t.needsUpdate=true;return t})();
  src.traverse(o=>{if(o.isMesh){o.frustumCulled=false;const mp=o.material.map;if(mp){mp.encoding=T.LinearEncoding;mp.anisotropy=4;mp.needsUpdate=true}const mat=M('#ffffff',{map:mp,skinning:true,gradientMap:soft});mat.userData.outlineParameters={visible:false};U.mats.push(mat);o.material=mat;o.userData.keep=true}});
  // bind data in model space (root at origin, unscaled units: she is 1 tall)
  root.updateMatrixWorld(true);const BIND=[],BQ={},BP={};const _iv=new T.Matrix4().copy(src.matrixWorld).invert();
  for(const n in B){const b=B[n];BIND.push([b,b.quaternion.clone(),b.position.clone()]);BQ[n]=b.getWorldQuaternion(new T.Quaternion());BP[n]=b.getWorldPosition(V()).applyMatrix4(_iv)}
  const hip0=BP.Hip.clone(),SHL=BP.L_Upperarm.clone().sub(hip0),SHR=BP.R_Upperarm.clone().sub(hip0);
  const LA={L:[BP.L_Upperarm.distanceTo(BP.L_Forearm),BP.L_Forearm.distanceTo(BP.L_Hand)],R:[BP.R_Upperarm.distanceTo(BP.R_Forearm),BP.R_Forearm.distanceTo(BP.R_Hand)]};
  const LL={L:[BP.L_Thigh.distanceTo(BP.L_Calf),BP.L_Calf.distanceTo(BP.L_Foot)],R:[BP.R_Thigh.distanceTo(BP.R_Calf),BP.R_Calf.distanceTo(BP.R_Foot)]};
  const ANK=BP.L_Foot.y;
  // fists: curl every finger joint toward the palm (fixed local rotations, applied after each reset)
  const CURL=[];for(const sd of['L','R'])for(const f of['Index','Mid','Ring','Pinky','Thumb'])for(let k=1;k<=3;k++){const n=sd+'_'+f+k;if(!B[n])continue;
    const ax=(f==='Thumb'?V(0,1,0):V(0,0,1)).applyQuaternion(BQ[n].clone().invert()).normalize();CURL.push([B[n],new T.Quaternion().setFromAxisAngle(ax,(sd==='L'?-1:1)*(f==='Thumb'?.5:k===1?1.25:1.35))])}
  // ---- twin sais, held in the fists with the blade out past the thumb ----
  const gold=M('#e6b84a'),grip=M('#1d1b22'),gemM=M('#2fc6b8');for(const x of[gold,grip,gemM]){x.userData.outlineParameters={visible:false};U.mats.push(x)}
  function sai(sd){const g=new T.Group();const b=new T.Mesh(new T.ConeGeometry(.011,.19,4),gold);b.scale.z=.45;b.position.y=.13;g.add(b);
    for(const sx of[-1,1]){const c=new T.CatmullRomCurve3([V(0,.03,0),V(sx*.034,.04,0),V(sx*.048,.07,0),V(sx*.036,.105,0)]);g.add(new T.Mesh(new T.TubeGeometry(c,10,.0055,5,false),gold))}
    const gd=new T.Mesh(new T.BoxGeometry(.03,.012,.012),gold);gd.position.y=.032;g.add(gd);const gm=new T.Mesh(new T.OctahedronGeometry(.009),gemM);gm.position.set(0,.034,.008);g.add(gm);
    const hd=new T.Mesh(new T.CylinderGeometry(.008,.008,.06,6),grip);g.add(hd);const pm=new T.Mesh(new T.SphereGeometry(.01,6,4),gold);pm.position.y=-.034;g.add(pm);
    const tip=new T.Group();tip.position.y=.22;g.add(tip);const mid=new T.Group();mid.position.y=.06;g.add(mid);g.userData={tip,mid};
    // in the hand's own frame: palm centre, blade along the T-pose forward (thumb) direction, prongs in the plane of the hand
    const hq=BQ[sd+'_Hand'].clone().invert(),fw=V(0,0,1).applyQuaternion(hq).normalize(),len=BP[sd+'_Mid1'].clone().sub(BP[sd+'_Hand']).applyQuaternion(hq).normalize();
    const side=len.clone().sub(fw.clone().multiplyScalar(len.dot(fw))).normalize(),zz=side.clone().cross(fw);g.quaternion.setFromRotationMatrix(new T.Matrix4().makeBasis(side,fw,zz));
    g.position.copy(len).multiplyScalar(BP[sd+'_Mid1'].distanceTo(BP[sd+'_Hand'])*.55).addScaledVector(V(0,-1,0).applyQuaternion(hq),.012);B[sd+'_Hand'].add(g);U['sai'+sd]=g;g.userData.fw=fw;return g}
  sai('L');sai('R');U.spearHead=U.saiR.userData.tip;
  U.halos=['L','R'].map(sd=>{const h=egSprite(EGT.teal,.24,'#c9fff2');h.material.opacity=0;U['sai'+sd].userData.tip.add(h);return h});
  const MOTE=[];function mote(pW){const m=egSprite(EGT.glow,.05,'#ffe7a0');m.position.copy(pW);scene.add(m);MOTE.push({m,t:0,v:V((Math.random()-.5)*.2,.35+Math.random()*.3,(Math.random()-.5)*.2)})}
  const NT=12;function mkTrail(){const tg=new T.BufferGeometry();tg.setAttribute('position',new T.BufferAttribute(new Float32Array(NT*6),3));tg.setAttribute('color',new T.BufferAttribute(new Float32Array(NT*6),3));
    const ti=[];for(let i=0;i<NT-1;i++){const a=i*2;ti.push(a,a+1,a+2,a+1,a+3,a+2)}tg.setIndex(ti);
    const tm=new T.MeshBasicMaterial({vertexColors:true,transparent:true,blending:T.CustomBlending,blendEquation:T.AddEquation,blendSrc:T.OneFactor,blendDst:T.OneFactor,blendSrcAlpha:T.ZeroFactor,blendDstAlpha:T.OneFactor,depthWrite:false,side:T.DoubleSide});tm.userData={noflash:true};
    const m=new T.Mesh(tg,tm);m.frustumCulled=false;scene.add(m);return{m,TR:[]}}
  const TRL={L:mkTrail(),R:mkTrail()};
  // ---- poses ----
  // body-frame values: hands (h) and blade directions (b) ride with the pelvis and its twist; feet (f) are planted points on the ground unless air>0,
  // which blends them to body-frame positions (bf) for flight. p: pelvis offset. Angles in degrees.
  const E={io:t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2,out:t=>1-Math.pow(1-t,3),in:t=>t*t*t,lin:t=>t};
  const ST={p:[0,-.16,0],yaw:-28,pitch:9,roll:0,tw:14,bend:4,side:0,headP:-6,headY:20,
    hL:[.1,.12,.19],hR:[-.13,.19,.07],bL:[.05,.45,1],bR:[.25,.1,1],eL:[1,-.6,-.3],eR:[-1,-.5,-.4],
    fL:[.085,ANK,.13],fR:[-.13,ANK,-.12],fyL:-12,fyR:-62,ptL:0,ptR:0,airL:0,airR:0,bfL:[.1,-.42,0],bfR:[-.1,-.42,0],trL:0,trR:0,hwL:0,hwR:0,hgL:[.17,.2,.15],hgR:[-.17,.2,.15],glow:0};
  const K=(t,o,lf)=>[t,Object.assign(JSON.parse(JSON.stringify(ST)),o||{}),lf||{}];
  const NUM=Object.keys(ST).filter(k=>!['fL','fR','fyL','fyR'].includes(k));
  // the combination: low stance, dash, spinning slash, butterfly kick, deep crouch landing, rising cross-slash, two light hops back to the stance
  const Y0=-28;
  const COMBO=[
    K(0),
    K(.1,{p:[0,-.2,-.015],pitch:3,tw:24,hL:[.12,.08,.12],hR:[-.12,.14,-.02],headY:26}),                                                  // load
    K(.2,{p:[.01,-.1,.16],yaw:-14,pitch:24,tw:6,bend:10,hL:[.15,.02,-.12],hR:[-.16,.02,-.15],bL:[.2,-.5,-1],bR:[-.2,-.5,-1],headP:-18,headY:10,ptR:.6},{fR:[-.03,ANK,.3],fyR:-20,lfR:.06}),   // dash: push off, rear foot strides through
    K(.31,{p:[.03,-.12,.4],yaw:-18,pitch:20,tw:-8,bend:8,hL:[.18,.04,-.08],hR:[-.2,.1,-.08],bL:[.6,-.2,-.6],bR:[-.6,.1,-.5],headP:-14,headY:14,trR:.6},{fL:[.1,ANK,.55],fyL:-18,lfL:.07}), // lead foot lands
    // spinning slash: pivot on the lead foot, a full turn with both arms flung wide, the right blade leading
    K(.4,{p:[.05,-.1,.49],yaw:Y0-110,pitch:6,tw:-26,bend:2,hL:[.3,.17,.06],hR:[-.31,.18,.03],bL:[1,.1,.4],bR:[-1,.15,.35],headP:-4,headY:40,trL:1,trR:1,ptR:.5},{fyL:-128,fR:[-.14,ANK+.05,.44],lfR:.08}),
    K(.5,{p:[.07,-.09,.51],yaw:Y0-235,pitch:4,tw:-22,hL:[.31,.18,.04],hR:[-.31,.18,.04],bL:[1,.1,.3],bR:[-1,.1,.3],headP:-4,headY:-30,trL:1,trR:1,ptR:.5},{fyL:-250,fR:[.02,ANK+.06,.36]}),
    K(.62,{p:[.05,-.14,.5],yaw:Y0-345,pitch:22,tw:18,bend:12,hL:[.25,.1,.16],hR:[-.12,.1,.24],bL:[.5,-.1,1],bR:[.3,-.1,1],headP:-10,headY:10,trL:.8,trR:1},{fyL:-360,fR:[-.09,ANK,.42],fyR:-388,lfR:.03}),
    // butterfly kick: sweep down and through, the body thrown flat, a full turn in the air with the legs scissoring and both blades arcing outward
    K(.72,{p:[.05,-.2,.5],yaw:Y0-380,pitch:58,tw:30,bend:16,side:-6,hL:[.24,-.06,-.04],hR:[-.22,.02,.14],bL:[.6,-.6,.3],bR:[-.5,-.3,.6],headP:-30,headY:-20,trL:.4,trR:.6}),
    K(.8,{p:[.05,.02,.56],yaw:Y0-470,pitch:82,tw:10,bend:4,side:-12,hL:[.3,.14,-.04],hR:[-.3,.14,-.04],bL:[1,.2,-.2],bR:[-1,.2,-.2],headP:-62,headY:0,airL:1,airR:1,bfL:[.2,-.4,.12],bfR:[-.24,-.32,-.14],ptL:1,ptR:1,trL:1,trR:1}),
    K(.9,{p:[.04,.1,.62],yaw:Y0-590,pitch:86,tw:0,side:-8,hL:[.31,.16,0],hR:[-.31,.16,0],bL:[1,.25,-.3],bR:[-1,.25,-.3],headP:-66,airL:1,airR:1,bfL:[.26,-.34,-.1],bfR:[-.2,-.4,.14],ptL:1,ptR:1,trL:1,trR:1}),
    K(.99,{p:[.03,.02,.67],yaw:Y0-680,pitch:62,tw:-6,side:-2,hL:[.28,.12,.06],hR:[-.28,.12,.06],bL:[1,.1,.2],bR:[-1,.1,.2],headP:-40,airL:1,airR:.7,bfL:[.14,-.42,.04],bfR:[-.12,-.4,.06],ptL:.8,ptR:.4,trL:.6,trR:.6},{fR:[-.1,ANK,.68],fyR:-735}),
    // land soft: right foot, then left, sinking into a deep crouch, blades low and wide
    K(1.06,{p:[.02,-.2,.71],yaw:Y0-718,pitch:30,tw:8,bend:14,hL:[.2,.0,.13],hR:[-.19,.0,.15],bL:[.8,-.1,.8],bR:[-.8,-.1,.8],headP:-14,headY:8,airL:0,ptL:0},{fL:[.11,ANK,.8],fyL:-726,lfL:.04}),
    K(1.18,{p:[.02,-.26,.73],yaw:Y0-720,pitch:34,tw:10,bend:16,hL:[.19,.02,.12],hR:[-.19,.02,.12],bL:[.9,-.3,.6],bR:[-.9,-.3,.6],headP:-10,headY:10}),
    // rising cross-slash: spring up through the legs, blades sweep from low outside to high, crossing in front
    K(1.3,{p:[.02,-.12,.75],yaw:Y0-718,pitch:16,tw:4,bend:6,hL:[.12,.12,.2],hR:[-.12,.12,.2],bL:[-.4,.7,.6],bR:[.4,.7,.6],headP:-14,headY:8,trL:1,trR:1}),
    K(1.4,{p:[.02,-.06,.77],yaw:Y0-718,pitch:-6,tw:0,bend:-4,hL:[-.04,.36,.13],hR:[.04,.36,.13],bL:[-.6,.8,.2],bR:[.6,.8,.2],headP:-22,headY:6,trL:1,trR:1,ptL:.3,ptR:.3}),
    K(1.56,{p:[.02,-.08,.76],yaw:Y0-720,pitch:2,tw:4,bend:0,hL:[.02,.3,.16],hR:[-.04,.3,.16],bL:[-.3,.6,.6],bR:[.3,.6,.6],headP:-10,headY:10,trL:.2,trR:.2}),
    // two light hops back into the stance (both feet leave the ground; nothing slides)
    K(1.74,{p:[.01,-.09,.42],yaw:Y0-720,pitch:6,tw:10,hL:[.1,.12,.18],hR:[-.12,.17,.07],headP:-8,headY:18,ptL:.4,ptR:.4},{fL:[.09,ANK,.47],fyL:-732,fR:[-.12,ANK,.3],fyR:-770,lfL:.06,lfR:.06}),
    K(1.94,{p:[0,-.15,.04],yaw:Y0-720,pitch:8,tw:14,hL:[.1,.12,.19],hR:[-.13,.19,.07],headY:20,ptL:.3,ptR:.3},{fL:[.085,ANK,.13],fyL:-732,fR:[-.13,ANK,-.12],fyR:-782,lfL:.05,lfR:.05}),
    K(2.2,{yaw:Y0-720},{fyL:-732,fyR:-782})];
  // feet: carry the last planted spot forward until a key moves them
  {let fL=ST.fL,fR=ST.fR,yL=ST.fyL,yR=ST.fyR;for(const k of COMBO){const m=k[2];if(m.fL)fL=m.fL;if(m.fR)fR=m.fR;if(m.fyL!=null)yL=m.fyL;if(m.fyR!=null)yR=m.fyR;k[1].fL=fL;k[1].fR=fR;k[1].fyL=yL;k[1].fyR=yR;k[1].lfL=m.lfL||0;k[1].lfR=m.lfR||0}}
  const HITS=[[.47,1],[.88,1],[1.38,1.4]];
  // sample: smooth (time-aware Hermite) for body/arms, eased arcs for feet, held exactly while planted
  function hermite(k,i,t,key){const a=k[i][1][key],b=k[i+1][1][key],t0=k[i][0],t1=k[i+1][0],dt=t1-t0,u=(t-t0)/dt;
    const pa=k[Math.max(0,i-1)],pb=k[Math.min(k.length-1,i+2)];const tan=(P0,P1,T0,T1,j)=>{const x0=j==null?P0:P0[j],x1=j==null?P1:P1[j];return(x1-x0)/Math.max(.001,T1-T0)};
    const h00=2*u*u*u-3*u*u+1,h10=u*u*u-2*u*u+u,h01=-2*u*u*u+3*u*u,h11=u*u*u-u*u;
    const f=j=>{const x0=j==null?a:a[j],x1=j==null?b:b[j];const m0=i===0?0:tan(pa[1][key],b,pa[0],t1,j),m1=i+2>=k.length?0:tan(a,pb[1][key],t0,pb[0],j);return h00*x0+h10*m0*dt+h01*x1+h11*m1*dt};
    return Array.isArray(a)?a.map((_,j)=>f(j)):f(null)}
  function sampleKeys(k,t){if(t<=k[0][0])return Object.assign({},k[0][1]);const L=k.length-1;if(t>=k[L][0])return Object.assign({},k[L][1]);let i=0;while(t>k[i+1][0])i++;
    const o={};for(const n of NUM)o[n]=hermite(k,i,t,n);const A=k[i][1],Bk=k[i+1][1],u=(t-k[i][0])/(k[i+1][0]-k[i][0]);
    for(const sd of['L','R']){const fa=A['f'+sd],fb=Bk['f'+sd],same=fa[0]===fb[0]&&fa[2]===fb[2]&&fa[1]===fb[1];const e=same?0:E.io(u);
      o['f'+sd]=fa.map((v,j)=>v+(fb[j]-v)*e);o['f'+sd][1]+=same?0:Math.sin(u*Math.PI)*(Bk['lf'+sd]||0);o['fy'+sd]=A['fy'+sd]+(Bk['fy'+sd]-A['fy'+sd])*(A['fy'+sd]===Bk['fy'+sd]?0:E.io(u))}return o}
  const STANCE=()=>JSON.parse(JSON.stringify(ST));
  // healing ritual: sweep out, tips down, drive both blades into the ground, sink onto the right knee gripping them, bow, breathe,
  // lift the head and open the chest, pull them free and rise to the stance. Hands are locked to the planted blades (hw) from impact to release.
  const GL=[.165,.205,.16],GR=[-.165,.205,.16];
  const RIT=[K(0),
    K(.32,{p:[0,-.11,0],pitch:-4,tw:4,bend:-6,headP:-12,headY:8,hL:[.3,.2,.05],hR:[-.3,.2,.05],bL:[1,.35,.2],bR:[-1,.35,.2],eL:[1,-.2,-.6],eR:[-1,-.2,-.6],trL:1,trR:1,glow:.15}),
    K(.52,{p:[0,-.09,0],pitch:-6,tw:0,bend:-8,headP:-14,headY:0,hL:[.25,.26,.1],hR:[-.25,.26,.1],bL:[.2,-1,.1],bR:[-.2,-1,.1],eL:[1,0,-.5],eR:[-1,0,-.5],trL:.6,trR:.6,glow:.25}),
    K(.66,{p:[0,-.2,.02],pitch:12,tw:0,bend:22,headP:8,headY:0,hL:[.19,.0,.16],hR:[-.19,.0,.16],bL:[.1,-1,.1],bR:[-.1,-1,.1],eL:[1,-.1,-.4],eR:[-1,-.1,-.4],hwL:1,hwR:1,hgL:GL,hgR:GR,trL:1,trR:1,glow:.35},{fyL:-12}),
    K(.8,{p:[0,-.22,0],pitch:10,tw:0,bend:26,headP:14,hwL:1,hwR:1,hgL:GL,hgR:GR,eL:[1,-.2,-.4],eR:[-1,-.2,-.4],glow:.4},{fL:[.085,ANK,.17],fyL:-6,lfL:.02}),
    K(1.22,{p:[.0,-.29,-.03],yaw:-10,pitch:8,tw:0,bend:32,headP:30,hwL:1,hwR:1,hgL:GL,hgR:GR,eL:[1,-.1,-.3],eR:[-1,-.1,-.3],ptR:.95,glow:.55},{fR:[-.075,.075,-.25],fyR:-14,lfR:.04}),
    K(1.55,{p:[0,-.3,-.03],yaw:-10,pitch:10,bend:40,headP:52,hwL:1,hwR:1,hgL:GL,hgR:GR,eL:[1,0,-.3],eR:[-1,0,-.3],ptR:.95,glow:.75}),
    K(3.0,{p:[0,-.3,-.03],yaw:-10,pitch:10,bend:40,headP:52,hwL:1,hwR:1,hgL:GL,hgR:GR,eL:[1,0,-.3],eR:[-1,0,-.3],ptR:.95,glow:1}),
    K(3.45,{p:[0,-.27,-.02],yaw:-10,pitch:2,bend:6,headP:-16,hwL:1,hwR:1,hgL:GL,hgR:GR,eL:[1,-.1,-.4],eR:[-1,-.1,-.4],ptR:.95,glow:1}),
    K(3.75,{p:[0,-.2,0],yaw:-18,pitch:6,bend:8,headP:-8,headY:10,hL:[.15,.1,.15],hR:[-.14,.15,.1],hwL:0,hwR:0,hgL:[GL[0],GL[1]+.12,GL[2]],hgR:[GR[0],GR[1]+.12,GR[2]],ptR:.6,glow:.6}),
    K(4.05,{p:[0,-.17,0],glow:.25},{fR:[-.13,ANK,-.12],fyR:-62,lfR:.06,fL:[.085,ANK,.13],fyL:-12}),
    K(4.4,{glow:0})];
  {let fL=ST.fL,fR=ST.fR,yL=ST.fyL,yR=ST.fyR;for(const k of RIT){const m=k[2];if(m.fL)fL=m.fL;if(m.fR)fR=m.fR;if(m.fyL!=null)yL=m.fyL;if(m.fyR!=null)yR=m.fyR;k[1].fL=fL;k[1].fR=fR;k[1].fyL=yL;k[1].fyR=yR;k[1].lfL=m.lfL||0;k[1].lfR=m.lfR||0}}
  const CL={ritual:{dur:4.4,hits:[[.66,1.2]],fn:t=>{const o=sampleKeys(RIT,t);if(t>1.5&&t<3.3){const b=Math.sin((t-1.5)/1.8*TAU)*Math.min(1,(t-1.5)/.3,(3.3-t)/.3);o.p=[o.p[0],o.p[1]+b*.007,o.p[2]];o.bend+=b*2.5;o.headP+=b*2}return o}},
  idle:{dur:3.2,loop:true,fn:t=>{const o=STANCE(),s=Math.sin(t/3.2*TAU);o.p=[0,-.16+s*.006,0];o.bend+=s*1.5;o.headY+=Math.sin(t/3.2*TAU*.5)*8;o.hL=[.1,.12+s*.006,.19];o.hR=[-.13,.19+s*.006,.07];return o}},
    combo:{dur:2.2,fn:t=>sampleKeys(COMBO,t),hits:HITS}};
  CL.whirl=CL.combo;CL.kneel=CL.ritual;
  const S={x:0,z:0,yaw:0,vel:0,wamt:0,clip:'idle',t:0,rate:1,hold:false,prev:null,bl:0,blT:.18,base:0};let cur=CL.idle.fn(0);
  function playG(n,rate,off){if(!CL[n])n='idle';S.prev=cur;S.bl=S.blT;S.clip=n;S.rate=rate||1;S.t=off||0}
  // blend two poses; yaws wrap to the nearest turn so leaving the combo never unwinds two spins
  function mixP(a,b,f){const o={};for(const k in a){let x=a[k],y=b[k];if(y===undefined){o[k]=x;continue}if(/^(yaw|fyL|fyR)$/.test(k))y=y+360*Math.round((x-y)/360);o[k]=Array.isArray(x)?x.map((v,i)=>v+(y[i]-v)*f):typeof x==='number'?x+(y-x)*f:x}return o}
  // ---- bone helpers ----
  const _q=new T.Quaternion(),_q2=new T.Quaternion(),_wq=new T.Quaternion(),_pq=new T.Quaternion(),_a=V(),_b=V(),_c=V(),_d=V(),_p=V(),_eu=new T.Euler(),rootQ=new T.Quaternion(),bodyQ=new T.Quaternion();
  function setWQ(b,qW){b.parent.getWorldQuaternion(_pq).invert();b.quaternion.copy(_pq).multiply(qW);b.updateMatrixWorld(true)}
  function aim(bone,child,tw){bone.getWorldPosition(_a);child.getWorldPosition(_b);_c.subVectors(_b,_a).normalize();_d.subVectors(tw,_a).normalize();_q.setFromUnitVectors(_c,_d);
    bone.getWorldQuaternion(_wq);_q.multiply(_wq);setWQ(bone,_q)}
  function rotW(bone,axisW,ang){_q2.setFromAxisAngle(axisW,ang);bone.getWorldQuaternion(_wq);_q2.multiply(_wq);setWQ(bone,_q2)}
  const W=v=>src.localToWorld(v);                                   // model space -> world
  const bodyPt=(arr,pel,q)=>V(arr[0],arr[1],arr[2]).applyQuaternion(q).add(pel);
  function twoBone(b1,b2,b3,L1,L2,tgtW,poleW){b1.getWorldPosition(_a);_d.subVectors(tgtW,_a);let d=clamp(_d.length(),.02*sc,(L1+L2)*sc-.002*sc);_d.normalize();const l1=L1*sc,l2=L2*sc;
    const a=(l1*l1-l2*l2+d*d)/(2*d),h=Math.sqrt(Math.max(0,l1*l1-a*a));_p.copy(poleW).addScaledVector(_d,-poleW.dot(_d)).normalize();const kn=_a.clone().addScaledVector(_d,a).addScaledVector(_p,h),end=_a.clone().addScaledVector(_d,d);
    aim(b1,b2,kn);aim(b2,b3,end)}
  // ---- walk: a light fighter's trot, feet planted while they carry weight ----
  let wph=0;const STRIDE=.74,DUTY=.62,_X=V(1,0,0),_Y=V(0,1,0),_Z=V(0,0,1);let fired=-1;
  const shake=v=>LAB.api&&LAB.api.shake&&LAB.api.shake(v);
  // runway walk: tall and level, each foot set down on a centre line heel first and peeled off the toe, hips swaying and dropping over the
  // standing leg while the pelvis turns into each step and the shoulders counter it, arms loose, blades held low, head steady
  // regal walk (Carter's brief): tall, chin up, eyes ahead; deliberate strides with controlled hip rotation and weight shift over the standing leg;
  // the body rises over each standing leg and settles softly into each heel strike; arms swing against the legs, blades low and steady beside the body
  function walkPose(ph,bank){const o=STANCE(),u0=ph/TAU,A=STRIDE*DUTY/2,mid=TAU*DUTY/2,cm=Math.cos(ph-mid),c=Math.cos(ph);
    o.yaw=6*cm;o.tw=-9.5*cm;o.roll=2.2*cm+bank;o.side=-1.5*cm;o.pitch=1;o.bend=-2;o.headP=-6;o.headY=-(o.yaw+o.tw)*.85;
    o.p=[.017*cm,-.03+.009*Math.cos(2*(ph-mid)),0];
    for(const[sd,off,sgn]of[['L',0,1],['R',.5,-1]]){const u=(((u0+off)%1)+1)%1;let z,y=ANK,pt=0;
      if(u<DUTY){const k=u/DUTY;z=lerp(A,-A,k);pt=k<.14?-.28*(1-k/.14):k>.66?.5*Math.pow((k-.66)/.34,1.3):0;y+=k>.66?.04*Math.pow((k-.66)/.34,1.5):0}
      else{const k=(u-DUTY)/(1-DUTY);z=lerp(-A,A,E.io(k));y+=.04*(1-k)*(1-k)+Math.sin(k*Math.PI)*.04;pt=.5*(1-k)*(1-k)-.28*Math.pow(k,3)}
      o['f'+sd]=[sgn*.048,y,z+.01];o['fy'+sd]=sgn*6;o['pt'+sd]=pt;
      const sw=-sgn*c;o['h'+sd]=[sgn*.185,-.065+Math.max(0,sw)*.012,.025+sw*.045];o['b'+sd]=[sgn*.12,-1,.18];o['e'+sd]=[sgn*.6,-.2,-.8]}
    o.trL=0;o.trR=0;return o}
  function tick(dt,I){S.x=I.x;S.z=I.z;let df=I.yaw-S.yaw;df=Math.atan2(Math.sin(df),Math.cos(df));if(S.clip!=='combo')S.yaw+=df*Math.min(1,dt*10);S.vel=I.speed;
    const c=CL[S.clip];const t0=S.t;S.t+=dt*S.rate;if(c.hits)c.hits.forEach(([ht,k],i)=>{if(t0<ht&&S.t>=ht){if(LAB.onStrike)LAB.onStrike(k,i);shake(.18*k)}})
    if(!c.loop&&S.t>=c.dur&&!S.hold)playG('idle');const c2=CL[S.clip],tt=c2.loop?S.t%c2.dur:Math.min(S.t,c2.dur);let p=c2.fn(tt);
    if(S.bl>0&&S.prev){S.bl-=dt;p=mixP(S.prev,p,1-Math.max(0,S.bl)/S.blT)}cur=p;
    S.wamt+=(clamp(S.vel/.5,0,1)-S.wamt)*Math.min(1,dt*7);const wk=S.clip==='idle'?S.wamt:0;wph+=(I.dist||0)/(STRIDE*sc)*TAU;
    S.bank=(S.bank||0)+((clamp(-(dt>0?df/dt:0)*2.2,-9,9))-(S.bank||0))*Math.min(1,dt*4);
    if(wk>0)p=mixP(p,walkPose(wph,S.bank),Math.min(1,wk*1.4));
    for(const[b,q,ps]of BIND){b.quaternion.copy(q);b.position.copy(ps)}
    root.position.set(S.x,0,S.z);root.rotation.set(0,S.yaw,0);rootQ.setFromEuler(root.rotation);root.updateMatrixWorld(true);
    // pelvis: placed and turned in model space
    _eu.set(rad(p.pitch),rad(p.yaw),rad(p.roll),'YXZ');bodyQ.setFromEuler(_eu);const pel=hip0.clone().add(V(...p.p));
    {const wp=W(pel.clone());B.Hip.parent.updateMatrixWorld(true);B.Hip.position.copy(B.Hip.parent.worldToLocal(wp));setWQ(B.Hip,rootQ.clone().multiply(bodyQ).multiply(BQ.Hip))}
    // spine: twist, bend and side-bend shared down the three spine bones
    const qWB=rootQ.clone().multiply(bodyQ),up=_Y.clone().applyQuaternion(qWB),rt=_X.clone().applyQuaternion(qWB),fw=_Z.clone().applyQuaternion(qWB);
    for(const[n,k]of[['Waist',.3],['Spine01',.35],['Spine02',.35]]){rotW(B[n],up,rad(p.tw)*k);rotW(B[n],rt,rad(p.bend)*k);rotW(B[n],fw,rad(p.side)*k)}
    const chestQ=bodyQ.clone().multiply(new T.Quaternion().setFromAxisAngle(_Y,rad(p.tw)));
    rotW(B.NeckTwist01,up,rad(p.headY)*.4);rotW(B.Head,up,rad(p.headY)*.6);const rt2=_X.clone().applyQuaternion(rootQ.clone().multiply(chestQ));rotW(B.NeckTwist01,rt2,rad(p.headP)*.4);rotW(B.Head,rt2,rad(p.headP)*.6);
    // legs: ankle targets (planted points, or body-frame positions in the air), knees toward each foot's facing, feet flat or pointed
    for(const sd of['L','R']){const air=clamp(p['air'+sd],0,1),fy=rad(p['fy'+sd]);const gp=V(...p['f'+sd]),bp=bodyPt(p['bf'+sd],pel,bodyQ);const tgt=gp.lerp(bp,air);tgt.y=Math.max(tgt.y,ANK*.9);
      const fq=new T.Quaternion().setFromAxisAngle(_Y,fy);if(air>0)fq.slerp(bodyQ,air);const pole=V(0,0,1).applyQuaternion(fq).transformDirection(src.matrixWorld);
      twoBone(B[sd+'_Thigh'],B[sd+'_Calf'],B[sd+'_Foot'],LL[sd][0],LL[sd][1],W(tgt.clone()),pole);
      const pt=clamp(p['pt'+sd],-.5,1);_q.setFromAxisAngle(_X,rad(55)*pt);setWQ(B[sd+'_Foot'],rootQ.clone().multiply(fq).multiply(_q).multiply(BQ[sd+'_Foot']))}
    // arms: wrists to body-frame targets, elbows out and down; then the wrist turns so the blade points where the pose says
    for(const sd of['L','R']){const sh=sd==='L'?SHL:SHR,hw=clamp(p['hw'+sd]||0,0,1),hand=bodyPt(p['h'+sd],pel,chestQ).lerp(V(...p['hg'+sd]),hw);const pole=V(...p['e'+sd]).applyQuaternion(chestQ).transformDirection(src.matrixWorld);
      twoBone(B[sd+'_Upperarm'],B[sd+'_Forearm'],B[sd+'_Hand'],LA[sd][0],LA[sd][1],W(hand),pole);
      const s=U['sai'+sd],cw=s.userData.fw.clone().applyQuaternion(B[sd+'_Hand'].getWorldQuaternion(_wq)),des=V(...p['b'+sd]).normalize().applyQuaternion(rootQ.clone().multiply(chestQ)).lerp(V(0,-1,0),hw).normalize();
      cw.normalize();const ang=Math.acos(clamp(cw.dot(des),-1,1));if(ang>1e-3){const ax=cw.clone().cross(des).normalize();rotW(B[sd+'_Hand'],ax,Math.min(ang,rad(85)))}}
    for(const[b,q]of CURL)b.quaternion.multiply(q);
    // flourish: every few steps one sai spins a full turn in the hand
    S.tw0=(S.tw0||0)+dt;for(const sd of['L','R']){const sa=U['sai'+sd];if(!sa.userData.q0)sa.userData.q0=sa.quaternion.clone();const per=3.2,ph0=sd==='L'?0:1.6,k=((S.tw0+ph0)%per)/.42;
      const a=0;sa.quaternion.copy(sa.userData.q0).multiply(_q.setFromAxisAngle(_Z,a*(sd==='L'?1:-1)))}
    src.updateMatrixWorld(true);
    // blade trails
    for(const sd of['L','R']){const s=U['sai'+sd],tr=TRL[sd],on=(p['tr'+sd]||0)>.1;const tp=s.userData.tip.getWorldPosition(V()),md=s.userData.mid.getWorldPosition(V());
      if(on||tr.TR.length){if(on)tr.TR.unshift({a:tp,b:md,l:1});for(const q of tr.TR)q.l-=dt*5.5;while(tr.TR.length>NT||(tr.TR.length&&tr.TR[tr.TR.length-1].l<=0))tr.TR.pop()}
      const pa=tr.m.geometry.attributes.position,ca=tr.m.geometry.attributes.color;for(let i=0;i<NT;i++){const q=tr.TR[Math.min(i,tr.TR.length-1)],f=q?Math.max(0,q.l)*(1-i/NT):0;
        if(q){pa.setXYZ(i*2,q.a.x,q.a.y,q.a.z);pa.setXYZ(i*2+1,q.b.x,q.b.y,q.b.z)}else{pa.setXYZ(i*2,0,-9,0);pa.setXYZ(i*2+1,0,-9,0)}ca.setXYZ(i*2,.5*f,.42*f,.18*f);ca.setXYZ(i*2+1,.18*f,.36*f,.42*f)}
      pa.needsUpdate=true;ca.needsUpdate=true}
    const gl=clamp(p.glow||0,0,1);for(const h of U.halos){h.material.opacity=gl*.8;h.scale.setScalar(.2+gl*.14+Math.sin(performance.now()/260)*.02*gl)}
    if(gl>.3&&Math.random()<gl*dt*14){const sd=Math.random()<.5?'L':'R';mote(U['sai'+sd].userData.tip.getWorldPosition(V()))}
    for(let i=MOTE.length-1;i>=0;i--){const q=MOTE[i];q.t+=dt;q.m.position.addScaledVector(q.v,dt);q.m.material.opacity=Math.max(0,1-q.t/1.1);if(q.t>1.1){scene.remove(q.m);MOTE.splice(i,1)}}
    for(const m of U.mats)m.emissive.setHex(I.flash?0xffffff:0)}
  return{U,S,scene,get cur(){return cur},playG,tick,clips:CL}};
