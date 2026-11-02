// ---------- imported quadruped (Tripo mesh, skeleton and skin weights built by us): four-leg IK, a trotting gait, spine, tail and ears all driven in code ----------
FACT.cat=function(){const G=window.TRIPO;const src=T.SkeletonUtils.clone(G.scene);const U={mats:[]};
  const root=new T.Group();scene.add(root);root.add(src);U.root=root;const V=()=>new T.Vector3();
  const B={};src.traverse(o=>{if(o.isBone)B[o.name]=o});
  // size: the whole model (ears included) stands LAB.mh tall; author everything below in the model's own units
  src.updateMatrixWorld(true);const box=new T.Box3();src.traverse(o=>{if(o.isMesh){o.geometry.computeBoundingBox();box.union(o.geometry.boundingBox)}});
  const sc=(LAB.mh||.8)/(box.max.y-box.min.y);src.scale.setScalar(sc);
  const soft=(()=>{const d=new Uint8Array([196,196,196,255,226,226,226,255,255,255,255,255]);const t=new T.DataTexture(d,3,1,T.RGBAFormat);t.minFilter=t.magFilter=T.LinearFilter;t.needsUpdate=true;return t})();
  const hard=(()=>{const d=new Uint8Array([160,160,160,255,222,222,222,255,255,255,255,255]);const t=new T.DataTexture(d,3,1,T.RGBAFormat);t.minFilter=t.magFilter=T.LinearFilter;t.needsUpdate=true;return t})();
  src.traverse(o=>{if(o.isMesh){o.frustumCulled=false;const mp=o.material.map;if(mp){mp.encoding=T.LinearEncoding;mp.anisotropy=4;mp.needsUpdate=true}
    const vc=!!o.geometry.attributes.color,mat=M('#ffffff',vc?{vertexColors:true,skinning:true,gradientMap:LAB.grad?hard:soft}:{map:mp,skinning:true,gradientMap:soft});mat.userData.outlineParameters={visible:false};U.mats.push(mat);o.material=mat;o.userData.keep=true}});
  const BIND=[];for(const n in B)BIND.push([B[n],B[n].quaternion.clone(),B[n].position.clone()]);
  // bind measurements, in model units (bones sit straight in model space: no bind rotations)
  const J=n=>{const p=V();let b=B[n];while(b&&b.isBone){p.add(b.position);b=b.parent}return p};
  const LEGS=['FL','FR','HL','HR'],INFO={};
  for(const k of LEGS){const p1=J(k+'1'),p2=J(k+'2'),p3=J(k+'3'),p4=J(k+'4'),s=k[1]==='L'?1:-1,front=k[0]==='F';
    // neutral stance: paws tucked under the body (the model was made mid-stalk with its legs splayed wide)
    const rest=LAB.bindStance?p4.clone():new T.Vector3(p1.x+s*.012,p4.y,p1.z+(front?.075:-.02));
    INFO[k]={s,front,L1:p1.distanceTo(p2),L2:p2.distanceTo(p3),L3:p3.distanceTo(p4),d3:p4.clone().sub(p3).normalize(),rest,toeY:p4.y,pole:new T.Vector3(s*(front?.18:.3),0,front?-1:1).normalize()}}
  const pelvis0=B.pelvis.position.clone(),HLEN=INFO.HL.L1+INFO.HL.L2+INFO.HL.L3;
  // ---- poses: body height and pitch, lunge, jump, spine arch and twist, head, ears, tail, and per-paw offsets from the stance (model units) ----
  const E={io:t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2,out:t=>1-Math.pow(1-t,3),in:t=>t*t*t,lin:t=>t};
  const P0={h:0,pitch:0,fwd:0,jump:0,arch:0,roll:0,twist:0,headP:0,headY:0,ear:0,tail:0,tailUp:0,carry:0,spin:0,FL:[0,0,0],FR:[0,0,0],HL:[0,0,0],HR:[0,0,0],claw:0};
  const P=o=>{const r=Object.assign({},P0,o);for(const k of LEGS)r[k]=(o&&o[k]||[0,0,0]).slice();return r};
  const mixP=(a,b,f)=>{const r={};for(const k in P0){const x=a[k],y=b[k];r[k]=Array.isArray(x)?x.map((v,i)=>v+(y[i]-v)*f):x+(y-x)*f}return r};
  const IDLE=P({});
  const L=(o,ex)=>P(Object.assign({},o,ex||{}));
  const CL={
    idle:{dur:6,loop:true,fn:t=>P({h:Math.sin(t*TAU/3)*.004,arch:Math.sin(t*TAU/3)*1.2,headY:Math.sin(t*TAU/6)*10,headP:Math.sin(t*TAU/4)*3,tail:.35,tailUp:.2})},
    // left claw: rear back onto the haunches, paw cocked high by the face, then a raking slash down and across
    swipe:{dur:.8,keys:[[0,IDLE,'io'],[.17,P({h:.04,pitch:26,fwd:-.03,FL:[.03,.27,-.02],ear:.8,tail:.9,headP:-6,claw:1,twist:-8}),'io'],
      [.36,P({h:-.01,pitch:-6,fwd:.07,FL:[-.08,.02,.2],ear:.9,tail:1,headP:6,claw:1,twist:14,roll:-6}),'out'],[.52,P({pitch:-4,fwd:.05,FL:[-.06,0,.16],ear:.7,tail:.8,claw:1,twist:8}),'io'],[.8,IDLE,'io']]},
    swipeR:{dur:.8,keys:[[0,IDLE,'io'],[.17,P({h:.04,pitch:26,fwd:-.03,FR:[-.03,.27,-.02],ear:.8,tail:.9,headP:-6,claw:1,twist:8}),'io'],
      [.36,P({h:-.01,pitch:-6,fwd:.07,FR:[.08,.02,.2],ear:.9,tail:1,headP:6,claw:1,twist:-14,roll:6}),'out'],[.52,P({pitch:-4,fwd:.05,FR:[.06,0,.16],ear:.7,tail:.8,claw:1,twist:-8}),'io'],[.8,IDLE,'io']]},
    // pounce: sink low with a rump wiggle, spring up and forward, both front paws pin the target, hop back
    pounce:{dur:1.05,keys:[[0,IDLE,'io'],[.14,P({h:-.07,pitch:-4,fwd:-.04,twist:7,ear:.6,tail:.5,tailUp:-.4,HL:[0,0,-.02],HR:[0,0,-.02]}),'io'],[.24,P({h:-.075,pitch:-5,fwd:-.05,twist:-7,ear:.7,tail:.6,tailUp:-.4}),'io'],
      [.32,P({h:-.08,pitch:-4,fwd:-.05,twist:5,ear:.8,tail:.7,tailUp:-.3}),'io'],
      [.44,P({jump:.14,h:.02,pitch:14,fwd:.2,carry:1,FL:[0,.1,.14],FR:[0,.1,.14],HL:[0,.06,-.1],HR:[0,.06,-.1],ear:1,tail:.9,tailUp:.6,claw:1,arch:-6}),'out'],
      [.55,P({jump:0,h:-.04,pitch:-14,fwd:.24,carry:1,FL:[-.02,0,.14],FR:[.02,0,.14],HL:[0,0,.02],HR:[0,0,.02],ear:1,tail:1,claw:1,headP:12,arch:8}),'in'],
      [.72,P({h:-.03,pitch:-10,fwd:.2,carry:1,FL:[-.02,0,.12],FR:[.02,0,.12],ear:.8,tail:.8,claw:1,headP:10,arch:6}),'io'],
      [.84,P({jump:.05,fwd:.08,carry:1,pitch:4,FL:[0,.04,.03],FR:[0,.04,.03],HL:[0,.03,0],HR:[0,.03,0],tail:.6}),'io'],[1.05,IDLE,'io']]},
    // flurry: rear right up onto the hind legs and box, left-right-left
    flurry:{dur:1,fn:t=>{const up=E.io(Math.min(1,t/.2))*E.io(Math.min(1,(1-t)/.22)),s=Math.max(0,Math.min(1,(t-.18)/.62)),ph=s*3*Math.PI;
      const a=Math.sin(ph),b=Math.sin(ph+Math.PI),fl=Math.max(0,a),fr=Math.max(0,b);
      return P({h:.07*up,pitch:46*up,fwd:-.05*up,arch:-10*up,headP:12*up+a*4,twist:(fl-fr)*16*up,roll:(fl-fr)*-5*up,ear:.9*up,tail:1,tailUp:.3,claw:up,
        FL:[(-.06*fl+.02)*up,(.16+.06*fl-.04*fr)*up,(.03+.17*fl)*up],FR:[(.06*fr-.02)*up,(.16+.06*fr-.04*fl)*up,(.03+.17*fr)*up],HL:[0,0,.03*up],HR:[0,0,.03*up]})}},
    kneel:{dur:3.5,keys:[[0,IDLE,'io'],[3.5,IDLE,'io']]}};
  CL.down={dur:2.6,keys:[[0,IDLE,'io'],[2.6,IDLE,'io']]};CL.rise=CL.down;
  const sample=(n,t)=>{const c=CL[n];if(c.fn)return c.fn(t);const k=c.keys;if(t>=k[k.length-1][0])return k[k.length-1][1];for(let i=0;i<k.length-1;i++)if(t<k[i+1][0]){const f=(t-k[i][0])/(k[i+1][0]-k[i][0]);return mixP(k[i][1],k[i+1][1],E[k[i+1][2]](f))}return k[0][1]};
  const S={x:0,z:0,yaw:0,vel:0,wamt:0,clip:'idle',t:0,rate:1,hold:false,prev:null,bl:0,blT:.12};let cur=IDLE;
  function playG(n,rate,off){if(!CL[n])n='idle';S.prev=cur;S.bl=S.blT;S.clip=n;S.rate=rate||1;S.t=off||0}
  // ---- bone helpers ----
  const _q=new T.Quaternion(),_wq=new T.Quaternion(),_pq=new T.Quaternion(),_a=V(),_b=V(),_c=V(),_d=V(),_e=V(),_p=V(),_eu=new T.Euler(),X=new T.Vector3(1,0,0);
  function aim(bone,child,tw){bone.getWorldPosition(_a);child.getWorldPosition(_b);_c.subVectors(_b,_a).normalize();_d.subVectors(tw,_a).normalize();_q.setFromUnitVectors(_c,_d);
    bone.getWorldQuaternion(_wq);_q.multiply(_wq);bone.parent.getWorldQuaternion(_pq).invert();bone.quaternion.copy(_pq.multiply(_q));bone.updateMatrixWorld(true)}
  function loc(bone,x,y,z){_eu.set(x,y,z,'YXZ');_q.setFromEuler(_eu);bone.quaternion.multiply(_q)}
  // one leg: toe on its target, the wrist/hock set back from it along the paw, then hip/shoulder-knee/elbow solved as two bones
  function leg(k,tgt,curl){const I=INFO[k],b1=B[k+'1'],b2=B[k+'2'],b3=B[k+'3'],b4=B[k+'4'];
    const d3=I.d3.clone();if(curl)d3.applyAxisAngle(X,curl*(I.front?1.1:.6)).normalize();
    const toeW=src.localToWorld(tgt.clone()),wrW=src.localToWorld(tgt.clone().addScaledVector(d3,-I.L3));
    b1.getWorldPosition(_a);const L1=I.L1*sc,L2=I.L2*sc;_d.subVectors(wrW,_a);const d=clamp(_d.length(),.02*sc,L1+L2-.002*sc);_d.normalize();
    const a=(L1*L1-L2*L2+d*d)/(2*d),h=Math.sqrt(Math.max(0,L1*L1-a*a));_p.copy(I.pole).transformDirection(src.matrixWorld);_p.addScaledVector(_d,-_p.dot(_d)).normalize();
    const kn=_a.clone().addScaledVector(_d,a).addScaledVector(_p,h);aim(b1,b2,kn);aim(b2,b3,wrW);aim(b3,b4,toeW)}
  // ---- gait: a light trot, diagonal pairs (left-hind with right-fore), paws planted in stance and lifted through the swing ----
  const STRIDE=.62,DUTY=.5,OFF={HL:0,FR:.04,HR:.5,FL:.54};let wph=0,earT=1.5,earK=0,earS=1,tailV=0,lastYaw=0;
  function tick(dt,I){S.x=I.x;S.z=I.z;let df=I.yaw-S.yaw;df=Math.atan2(Math.sin(df),Math.cos(df));S.yaw+=df*Math.min(1,dt*(S.clip==='idle'?9:14));S.vel=I.speed;
    const c=CL[S.clip];S.t+=dt*S.rate;if(!c.loop&&S.t>=c.dur&&!S.hold)playG('idle');const c2=CL[S.clip],tt=c2.loop?S.t%c2.dur:Math.min(S.t,c2.dur);let p=sample(S.clip,tt);
    if(S.bl>0&&S.prev){S.bl-=dt;p=mixP(S.prev,p,1-Math.max(0,S.bl)/S.blT)}cur=p;
    S.wamt+=(clamp(S.vel/.5,0,1)-S.wamt)*Math.min(1,dt*7);const wk=S.clip==='idle'?S.wamt:0;
    wph+=(I.dist||0)/(STRIDE*sc)*TAU;const ph=wph;
    for(const[b,q,ps]of BIND){b.quaternion.copy(q);b.position.copy(ps)}
    root.position.set(S.x,0,S.z);root.rotation.set(0,S.yaw+p.spin*TAU,0);
    // body: height, bob (twice a stride), sway, lunge and jump, all on the pelvis; pitch pivots at the hips
    const bob=wk*(.006+.006*Math.cos(ph*2)),hgt=.012+p.h+p.jump-bob-wk*.004;
    B.pelvis.position.set(pelvis0.x+Math.sin(ph)*.006*wk,pelvis0.y+hgt,pelvis0.z+p.fwd);
    loc(B.pelvis,-rad(p.pitch)+Math.sin(ph*2)*.03*wk,rad(p.twist)*.5+Math.sin(ph)*.06*wk,rad(p.roll)+Math.sin(ph)*.035*wk);
    loc(B.spine,-rad(p.arch)*.5,rad(p.twist)*.4-Math.sin(ph)*.08*wk,0);loc(B.chest,rad(p.arch)*.6+Math.sin(ph*2+.6)*.03*wk,rad(p.twist)*.3,0);
    src.updateMatrixWorld(true);
    // legs
    for(const k of LEGS){const In=INFO[k],o=p[k],t=V().copy(In.rest);t.z+=p.fwd*p.carry;t.x+=o[0];t.y+=o[1];t.z+=o[2];let curl=0;
      if(wk>0){const u=(((ph/TAU+OFF[k])%1)+1)%1,A=STRIDE*DUTY/2;let z,y=0;if(u<DUTY)z=lerp(A,-A,u/DUTY);else{const q=(u-DUTY)/(1-DUTY);z=lerp(-A,A,E.io(q));y=Math.sin(q*Math.PI)*HLEN*(In.front?.26:.2);curl=Math.sin(q*Math.PI)*.9}
        t.z+=z*wk;t.y+=y*wk;curl*=wk}
      if(In.front&&o[1]>.03)curl=Math.max(curl,clamp((o[1]-.03)*7,0,1)*(1-p.claw*.6)-p.claw*.5);
      if(p.jump>0||o[1]>0)curl+=clamp(p.jump*5,0,.8);t.y=Math.max(In.toeY,t.y);leg(k,t,curl)}
    // head and neck: keep the gaze steady against the body's pitch, then add the pose
    const yr=dt>0?df/dt:0;loc(B.neck,rad(p.pitch)*.45+rad(p.headP)*.4-Math.sin(ph*2+.4)*.025*wk,rad(p.headY)*.4,0);loc(B.head,rad(p.pitch)*.25+rad(p.headP)*.6,rad(p.headY)*.6+clamp(yr*.04,-.3,.3),-rad(p.roll)*.5);
    // ears: an idle flick now and then, swept flat back to attack
    earT-=dt;if(earT<=0){earT=1.2+Math.random()*3.5;earK=1;earS=Math.random()<.5?1:-1}earK=Math.max(0,earK-dt*6);const fl=Math.sin(earK*Math.PI)*.35;
    loc(B.earL,-p.ear*.75-(earS>0?fl:0),-p.ear*.45,-p.ear*.25);loc(B.earR,-p.ear*.75-(earS<0?fl:0),p.ear*.45,p.ear*.25);
    // tail: a wave running out along the 12 links, quicker and wider with excitement, swinging out against turns
    tailV+=((clamp(-(S.yaw-lastYaw)/Math.max(dt,1e-3),-6,6))*.05-tailV)*Math.min(1,dt*4);lastYaw=S.yaw;const now=performance.now()/1000,amp=.05+.05*wk+.13*p.tail,spd=1.6+2.2*wk+4*p.tail;
    for(let i=0;i<12;i++){const b=B['tail'+i];if(!b)continue;const u=i/11;loc(b,-p.tailUp*.06*(1-u)-wk*.02,Math.sin(now*spd-i*.55)*amp*(.4+u*.8)+tailV*(1-u*.5),0)}
    src.updateMatrixWorld(true);
    for(const m of U.mats)m.emissive.setHex(I.flash?0xffffff:0)}
  return{U,S,scene,get cur(){return cur},playG,tick,clips:CL}};
