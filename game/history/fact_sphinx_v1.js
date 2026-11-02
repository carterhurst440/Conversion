// ---------- the sphinx: lion body, pharaoh head, Egyptian wings; everything driven in code ----------
// weight comes from springs on the body (it lags, overshoots and settles), a prowl with rolling shoulder blades,
// a rotary gallop for charges, wings that fold, spread and beat, a tail that whips behind every move, and dust on impacts
FACT.sphinx=function(){const G=window.TRIPO;const src=T.SkeletonUtils.clone(G.scene);const U={mats:[]};
  const root=new T.Group();scene.add(root);root.add(src);U.root=root;const V=()=>new T.Vector3();
  const B={};src.traverse(o=>{if(o.isBone)B[o.name]=o});
  src.updateMatrixWorld(true);const box=new T.Box3();src.traverse(o=>{if(o.isMesh){o.geometry.computeBoundingBox();box.union(o.geometry.boundingBox)}});
  const sc=(LAB.mh||1.2)/(box.max.y-box.min.y);src.scale.setScalar(sc);
  const grad=(()=>{const d=new Uint8Array([138,138,138,255,206,206,206,255,255,255,255,255]);const t=new T.DataTexture(d,3,1,T.RGBAFormat);t.minFilter=t.magFilter=T.LinearFilter;t.needsUpdate=true;return t})();
  src.traverse(o=>{if(o.isMesh){o.frustumCulled=false;const mat=M('#ffffff',{vertexColors:true,skinning:true,gradientMap:grad,side:T.DoubleSide});mat.userData.outlineParameters={visible:false};U.mats.push(mat);o.material=mat;o.userData.keep=true}});
  const BIND=[];for(const n in B)BIND.push([B[n],B[n].quaternion.clone(),B[n].position.clone()]);
  const J=n=>{const p=V();let b=B[n];while(b&&b.isBone){p.add(b.position);b=b.parent}return p};
  const LEGS=['FL','FR','HL','HR'],INFO={};const X=new T.Vector3(1,0,0),Y=new T.Vector3(0,1,0),Z=new T.Vector3(0,0,1);
  for(const k of LEGS){const p1=J(k+'1'),p2=J(k+'2'),p3=J(k+'3'),p4=J(k+'4'),s=k[1]==='L'?1:-1,front=k[0]==='F';
    INFO[k]={s,front,L1:p1.distanceTo(p2),L2:p2.distanceTo(p3),L3:p3.distanceTo(p4),d3:p4.clone().sub(p3).normalize(),rest:p4.clone(),toeY:p4.y,top:p1,pole:new T.Vector3(s*(front?.12:.22),0,front?-1:1).normalize()}}
  const pelvis0=B.pelvis.position.clone(),LEG=INFO.HL.L1+INFO.HL.L2+INFO.HL.L3;
  // wing spread: the folded wing (pointing back, feathers hanging down) turned to point out sideways with feathers trailing back
  const WING={};for(const sd of['L','R']){const s=sd==='L'?1:-1,bf=J('w'+sd+'4').sub(J('w'+sd+'1')).normalize(),tf=new T.Vector3(0,-1,0);tf.addScaledVector(bf,-tf.dot(bf)).normalize();
    const bs=new T.Vector3(s,.18,-.12).normalize(),ts=new T.Vector3(0,-.15,-1);ts.addScaledVector(bs,-ts.dot(bs)).normalize();
    const Mf=new T.Matrix4().makeBasis(bf,tf,bf.clone().cross(tf)),Ms=new T.Matrix4().makeBasis(bs,ts,bs.clone().cross(ts));
    const R=Ms.multiply(Mf.transpose());WING[sd]={s,q:new T.Quaternion().setFromRotationMatrix(R)}}
  // ---- poses ----
  const E={io:t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2,out:t=>1-Math.pow(1-t,3),in:t=>t*t*t,lin:t=>t,back:t=>{const c=1.7;return 1+(c+1)*Math.pow(t-1,3)+c*Math.pow(t-1,2)}};
  const P0={h:0,pitch:0,fwd:0,jump:0,arch:0,roll:0,twist:0,headP:0,headY:0,tail:0,tailUp:0,carry:0,claw:0,spread:0,flap:0,FL:[0,0,0],FR:[0,0,0],HL:[0,0,0],HR:[0,0,0]};
  const P=o=>{const r=Object.assign({},P0,o);for(const k of LEGS)r[k]=(o&&o[k]||[0,0,0]).slice();return r};
  const mixP=(a,b,f)=>{const r={};for(const k in P0){const x=a[k],y=b[k];r[k]=Array.isArray(x)?x.map((v,i)=>v+(y[i]-v)*f):x+(y-x)*f}return r};
  const IDLE=P({});
  const CL={
    idle:{dur:8,loop:true,fn:t=>P({h:Math.sin(t*TAU/4)*.003,arch:Math.sin(t*TAU/4)*1.5,headY:Math.sin(t*TAU/8)*14,headP:Math.sin(t*TAU/5.3)*3,tail:.25,spread:.02+.02*Math.sin(t*TAU/4)})},
    // maul: rear up tall with the wings half open, then crash both forepaws down onto the target
    maul:{dur:1.15,ev:[[.5,'slam']],keys:[[0,IDLE,'io'],
      [.3,P({h:.07,pitch:38,fwd:-.07,arch:-8,FL:[.01,.26,.02],FR:[-.01,.24,.05],HL:[0,0,.03],HR:[0,0,.03],headP:-8,tail:.8,tailUp:.5,claw:1,spread:.55,flap:.7}),'out'],
      [.38,P({h:.08,pitch:42,fwd:-.07,arch:-10,FL:[.01,.28,.03],FR:[-.01,.27,.06],HL:[0,0,.03],HR:[0,0,.03],headP:-10,tail:.9,tailUp:.6,claw:1,spread:.6,flap:.8}),'io'],
      [.5,P({h:-.05,pitch:-12,fwd:.16,arch:10,carry:1,FL:[-.01,0,.12],FR:[.01,0,.14],headP:14,tail:1,tailUp:-.2,claw:1,spread:.5,flap:-.6}),'in'],
      [.7,P({h:-.04,pitch:-9,fwd:.14,arch:8,carry:1,FL:[-.01,0,.12],FR:[.01,0,.14],headP:10,tail:.7,spread:.25,flap:-.2,claw:1}),'io'],[1.15,IDLE,'io']]},
    // swipe: load the shoulder, then a heavy raking blow across the body with the whole torso turning into it
    swipe:{dur:.9,keys:[[0,IDLE,'io'],[.22,P({h:-.015,pitch:10,twist:-18,roll:5,fwd:-.03,FL:[.05,.17,-.05],headY:-14,headP:-4,tail:.7,claw:1,spread:.12}),'io'],
      [.4,P({h:-.03,pitch:-4,twist:22,roll:-7,fwd:.08,FL:[-.13,.03,.22],headY:16,headP:6,tail:1,claw:1,spread:.2}),'back'],[.56,P({pitch:-3,twist:14,roll:-4,fwd:.06,FL:[-.1,0,.17],headY:10,tail:.8,claw:1,spread:.1}),'io'],[.9,IDLE,'io']]},
    swipeR:{dur:.9,keys:[[0,IDLE,'io'],[.22,P({h:-.015,pitch:10,twist:18,roll:-5,fwd:-.03,FR:[-.05,.17,-.05],headY:14,headP:-4,tail:.7,claw:1,spread:.12}),'io'],
      [.4,P({h:-.03,pitch:-4,twist:-22,roll:7,fwd:.08,FR:[.13,.03,.22],headY:-16,headP:6,tail:1,claw:1,spread:.2}),'back'],[.56,P({pitch:-3,twist:-14,roll:4,fwd:.06,FR:[.1,0,.17],headY:-10,tail:.8,claw:1,spread:.1}),'io'],[.9,IDLE,'io']]},
    // pounce: sink and coil, the tail lashing, explode up with the wings thrown wide, land pinning the target, hop back
    pounce:{dur:1.25,ev:[[.66,'slam']],keys:[[0,IDLE,'io'],[.16,P({h:-.1,pitch:-5,fwd:-.05,twist:6,headP:6,tail:.9,tailUp:-.4,HL:[0,0,.03],HR:[0,0,.03],spread:-.1}),'io'],
      [.28,P({h:-.11,pitch:-6,fwd:-.06,twist:-6,headP:6,tail:1,tailUp:-.4,HL:[0,0,.04],HR:[0,0,.04],spread:-.1}),'io'],[.38,P({h:-.115,pitch:-4,fwd:-.06,headP:5,tail:1,tailUp:-.3,HL:[0,0,.05],HR:[0,0,.05],spread:-.1}),'io'],
      [.52,P({jump:.24,h:.02,pitch:12,fwd:.3,carry:1,arch:-10,FL:[0,.14,.16],FR:[0,.14,.18],HL:[0,.08,-.16],HR:[0,.08,-.16],headP:-6,tail:1,tailUp:.5,claw:1,spread:1,flap:.9}),'out'],
      [.66,P({jump:0,h:-.07,pitch:-14,fwd:.34,carry:1,arch:10,FL:[-.02,0,.12],FR:[.02,0,.14],HL:[0,0,.04],HR:[0,0,.04],headP:14,tail:1,claw:1,spread:.8,flap:-.7}),'in'],
      [.84,P({h:-.05,pitch:-10,fwd:.3,carry:1,arch:8,FL:[-.02,0,.12],FR:[.02,0,.14],headP:10,tail:.8,claw:1,spread:.35,flap:-.2}),'io'],
      [1,P({jump:.06,fwd:.12,carry:1,pitch:4,FL:[0,.05,.03],FR:[0,.05,.03],HL:[0,.04,0],HR:[0,.04,0],tail:.6,spread:.15}),'io'],[1.25,IDLE,'io']]},
    // buffet: wings flung wide and high, the body rearing into it, then one huge downbeat that throws a gust forward
    buffet:{dur:1.15,ev:[[.55,'gust']],keys:[[0,IDLE,'io'],[.3,P({h:.03,pitch:16,fwd:-.05,arch:-6,headP:-12,tail:.6,tailUp:.4,spread:1,flap:1}),'out'],[.42,P({h:.04,pitch:18,fwd:-.05,arch:-7,headP:-14,tail:.7,tailUp:.4,spread:1,flap:1.1}),'io'],
      [.55,P({h:-.03,pitch:-6,fwd:.06,arch:6,headP:10,tail:1,spread:1,flap:-1}),'in'],[.75,P({h:-.02,pitch:-4,fwd:.04,headP:6,tail:.7,spread:.8,flap:-.5}),'io'],[1.15,IDLE,'io']]},
    kneel:{dur:3.5,keys:[[0,IDLE,'io'],[3.5,IDLE,'io']]}};
  CL.down={dur:2.6,keys:[[0,IDLE,'io'],[2.6,IDLE,'io']]};CL.rise=CL.down;
  const sample=(n,t)=>{const c=CL[n];if(c.fn)return c.fn(t);const k=c.keys;if(t>=k[k.length-1][0])return k[k.length-1][1];for(let i=0;i<k.length-1;i++)if(t<k[i+1][0]){const f=(t-k[i][0])/(k[i+1][0]-k[i][0]);return mixP(k[i][1],k[i+1][1],E[k[i+1][2]](f))}return k[0][1]};
  const S={x:0,z:0,yaw:0,vel:0,wamt:0,gal:0,clip:'idle',t:0,rate:1,hold:false,prev:null,bl:0,blT:.12,lastT:0};let cur=IDLE;
  function playG(n,rate,off){if(!CL[n])n='idle';S.prev=cur;S.bl=S.blT;S.clip=n;S.rate=rate||1;S.t=off||0;S.lastT=S.t}
  // springs: the body follows the pose like something heavy (slight lag, a little overshoot, then settles)
  const SPR=['h','pitch','fwd','jump','arch','roll','twist','headP','headY','spread','flap'],K={h:420,pitch:300,fwd:360,jump:700,arch:260,roll:260,twist:260,headP:200,headY:160,spread:220,flap:420},ZT={flap:.5,spread:.75,headY:.65,headP:.6};
  const SP={},SV={};for(const k of SPR){SP[k]=0;SV[k]=0}
  function spring(p,dt){const o=Object.assign({},p);const n=Math.max(1,Math.ceil(dt/.008)),h=dt/n;for(const k of SPR){const kk=K[k],c=2*(ZT[k]||.7)*Math.sqrt(kk);for(let i=0;i<n;i++){SV[k]+=(kk*(p[k]-SP[k])-c*SV[k])*h;SP[k]+=SV[k]*h}o[k]=SP[k]}return o}
  // ---- dust ----
  const dustTex=(()=>{const c=document.createElement('canvas');c.width=c.height=64;const g=c.getContext('2d'),gr=g.createRadialGradient(32,32,0,32,32,30);gr.addColorStop(0,'rgba(236,222,190,.95)');gr.addColorStop(1,'rgba(236,222,190,0)');g.fillStyle=gr;g.fillRect(0,0,64,64);const t=new T.CanvasTexture(c);return t})();
  const PUFF=[];function puff(p,vel,size,life){const m=new T.SpriteMaterial({map:dustTex,transparent:true,depthWrite:false,opacity:.9});m.userData={noflash:true};const sp=new T.Sprite(m);sp.position.copy(p);sp.scale.setScalar(size);scene.add(sp);PUFF.push({sp,v:vel,t:0,life,size})}
  function burst(cW,n,spd,size,dir){for(let i=0;i<n;i++){const a=i/n*TAU+Math.random()*.4,v=new T.Vector3(Math.cos(a),0,Math.sin(a)).multiplyScalar(spd*(.6+Math.random()*.6));if(dir)v.addScaledVector(dir,spd*1.6);v.y=spd*.35*Math.random();puff(cW.clone().add(new T.Vector3(0,.04,0)),v,size*(.7+Math.random()*.6),.55+Math.random()*.35)}}
  function tickPuff(dt){for(let i=PUFF.length-1;i>=0;i--){const q=PUFF[i];q.t+=dt;const k=q.t/q.life;q.sp.position.addScaledVector(q.v,dt);q.v.multiplyScalar(Math.exp(-dt*3));q.sp.scale.setScalar(q.size*(1+k*1.6));q.sp.material.opacity=.85*(1-k);if(k>=1){scene.remove(q.sp);PUFF.splice(i,1)}}}
  function fire(ev){const pW=V();if(ev==='slam'){for(const k of['FL','FR']){B[k+'4'].getWorldPosition(pW);pW.y=0;burst(pW,7,.9,.22)}}
    if(ev==='gust'){const fw=V().set(0,0,1).applyQuaternion(root.quaternion);root.getWorldPosition(pW);pW.addScaledVector(fw,.5*sc);pW.y=0;burst(pW,12,.7,.3,fw)}}
  // ---- bones ----
  const _q=new T.Quaternion(),_q2=new T.Quaternion(),_wq=new T.Quaternion(),_pq=new T.Quaternion(),_a=V(),_b=V(),_c=V(),_d=V(),_p=V(),_eu=new T.Euler();
  function aim(bone,child,tw){bone.getWorldPosition(_a);child.getWorldPosition(_b);_c.subVectors(_b,_a).normalize();_d.subVectors(tw,_a).normalize();_q.setFromUnitVectors(_c,_d);
    bone.getWorldQuaternion(_wq);_q.multiply(_wq);bone.parent.getWorldQuaternion(_pq).invert();bone.quaternion.copy(_pq.multiply(_q));bone.updateMatrixWorld(true)}
  function loc(bone,x,y,z){if(!bone)return;_eu.set(x,y,z,'YXZ');_q.setFromEuler(_eu);bone.quaternion.multiply(_q)}
  function leg(k,tgt,curl){const I=INFO[k],b1=B[k+'1'],b2=B[k+'2'],b3=B[k+'3'],b4=B[k+'4'];
    const d3=I.d3.clone();if(curl)d3.applyAxisAngle(X,curl*(I.front?1.15:.7)).normalize();
    const toeW=src.localToWorld(tgt.clone()),wrW=src.localToWorld(tgt.clone().addScaledVector(d3,-I.L3));
    b1.getWorldPosition(_a);const L1=I.L1*sc,L2=I.L2*sc;_d.subVectors(wrW,_a);const d=clamp(_d.length(),.02*sc,L1+L2-.003*sc);_d.normalize();
    const a=(L1*L1-L2*L2+d*d)/(2*d),h=Math.sqrt(Math.max(0,L1*L1-a*a));_p.copy(I.pole).transformDirection(src.matrixWorld);_p.addScaledVector(_d,-_p.dot(_d)).normalize();
    const kn=_a.clone().addScaledVector(_d,a).addScaledVector(_p,h);aim(b1,b2,kn);aim(b2,b3,wrW);aim(b3,b4,toeW)}
  // ---- gaits: a prowl (lateral walk, shoulders rolling) and a rotary gallop for charges ----
  const PROWL={stride:.62,duty:.66,off:{HL:0,FL:.25,HR:.5,FR:.75},lift:{F:.085,H:.06}};
  const GALLOP={stride:1.25,duty:.36,off:{HL:0,HR:.11,FL:.48,FR:.6},lift:{F:.13,H:.1}};
  let ph=0,earlyY=0;const HIST=[];let lastYaw=0,lastPitch=0;
  function footCycle(g,k,u){const D=g.duty,A=g.stride*D/2;let z,y=0,curl=0;if(u<D)z=lerp(A,-A,u/D);else{const q=(u-D)/(1-D);z=lerp(-A,A,E.io(q));y=Math.sin(q*Math.PI)*g.lift[k[0]];curl=Math.sin(q*Math.PI)}return[z,y,curl]}
  function tick(dt,I){S.x=I.x;S.z=I.z;let df=I.yaw-S.yaw;df=Math.atan2(Math.sin(df),Math.cos(df));S.yaw+=df*Math.min(1,dt*(S.clip==='idle'?6:12));S.vel=I.speed;
    const c=CL[S.clip];const t0=S.t;S.t+=dt*S.rate;if(c.ev)for(const[et,en]of c.ev)if(t0<et&&S.t>=et)fire(en);
    if(!c.loop&&S.t>=c.dur&&!S.hold)playG('idle');const c2=CL[S.clip],tt=c2.loop?S.t%c2.dur:Math.min(S.t,c2.dur);let p=sample(S.clip,tt);
    if(S.bl>0&&S.prev){S.bl-=dt;p=mixP(S.prev,p,1-Math.max(0,S.bl)/S.blT)}cur=p;
    S.wamt+=(clamp(S.vel/.4,0,1)-S.wamt)*Math.min(1,dt*5);const wk=S.clip==='idle'?S.wamt:0;S.gal+=((I.charge&&wk>.5?1:0)-S.gal)*Math.min(1,dt*4);const gl=S.gal;
    const stride=lerp(PROWL.stride,GALLOP.stride,gl)*sc;ph+=(I.dist||0)/stride*TAU;const u0=ph/TAU;
    // gait-driven body motion, folded into the pose before the springs
    const q=P(p);const cph=Math.cos(ph),sph=Math.sin(ph);
    if(wk>0){q.h+=wk*((1-gl)*(-.012+.006*Math.cos(ph*2))+gl*(.012+.035*Math.max(0,Math.sin(ph*TAU/TAU+1.2))));
      q.pitch+=wk*(gl*7*Math.sin(ph+.6)-(1-gl)*3);q.arch+=wk*gl*14*Math.sin(ph+2.2);q.roll+=wk*(1-gl)*3*sph;q.twist+=wk*(1-gl)*5*Math.sin(ph+.5);
      q.headP+=wk*((1-gl)*6-gl*4*Math.sin(ph+.6));q.tail=Math.max(q.tail,.35*wk+.4*gl);q.tailUp+=gl*-.3;q.spread=Math.max(q.spread,gl*.28);q.flap+=gl*.35*Math.sin(ph+1)}
    const s=spring(q,dt);
    for(const[b,qq,ps]of BIND){b.quaternion.copy(qq);b.position.copy(ps)}
    root.position.set(S.x,0,S.z);root.rotation.set(0,S.yaw,0);
    B.pelvis.position.set(pelvis0.x+(1-gl)*Math.sin(ph)*.006*wk,pelvis0.y+.004+s.h+s.jump,pelvis0.z+s.fwd);
    loc(B.pelvis,-rad(s.pitch),rad(s.twist)*.45,rad(s.roll));
    loc(B.spine,-rad(s.arch)*.55,rad(s.twist)*.35,rad(s.roll)*.3);loc(B.chest,rad(s.arch)*.65,rad(s.twist)*.3,0);
    // shoulder blades: each rides up as its leg takes the weight (the prowl's signature roll)
    for(const k of['FL','FR']){const u=(((u0+lerp(PROWL.off[k],GALLOP.off[k],gl))%1)+1)%1,D=lerp(PROWL.duty,GALLOP.duty,gl),st=u<D?Math.sin(u/D*Math.PI):-.4*Math.sin((u-D)/(1-D)*Math.PI);
      B[k+'1'].position.y+=wk*st*.022*(1-gl*.5)}
    src.updateMatrixWorld(true);
    for(const k of LEGS){const In=INFO[k],o=p[k],t=V().copy(In.rest);t.z+=s.fwd*p.carry;t.x+=o[0];t.y+=o[1];t.z+=o[2];let curl=0;
      if(wk>0){const off=lerp(PROWL.off[k],GALLOP.off[k],gl),u=(((u0+off)%1)+1)%1;const a=footCycle(PROWL,k,u),b=footCycle(GALLOP,k,u);
        t.z+=lerp(a[0],b[0],gl)*wk;t.y+=lerp(a[1],b[1],gl)*wk;curl=lerp(a[2],b[2],gl)*wk;if(gl>.3)t.z+=(In.front?.05:-.04)*gl*wk}
      if(In.front&&o[1]>.03)curl=Math.max(curl,clamp((o[1]-.03)*6,0,1)*(1-p.claw*.7)-p.claw*.45);
      if(s.jump>0)curl+=clamp(s.jump*4,0,.8);t.y=Math.max(In.toeY,t.y);leg(k,t,curl)}
    // head: steady gaze against the body's pitch and bob, then the pose's own look
    const yr=dt>0?df/dt:0;loc(B.neck,rad(s.pitch)*.5+rad(s.headP)*.4+rad(s.arch)*-.3,rad(s.headY)*.4-rad(s.twist)*.3,0);loc(B.head,rad(s.pitch)*.3+rad(s.headP)*.6,rad(s.headY)*.6+clamp(yr*.05,-.35,.35)-rad(s.twist)*.2,-rad(s.roll)*.6);
    // wings: fold <-> spread, then beat about the body axis; the inner wing leads, the outer feathers follow
    for(const sd of['L','R']){const W=WING[sd],w1=B['w'+sd+'1'];if(!w1)continue;const sp=clamp(s.spread,-.15,1.1);
      _q2.identity();if(sp>0)_q2.slerp(W.q,Math.min(1,sp));else _q2.setFromAxisAngle(Y,-W.s*sp*.0);
      _q.setFromAxisAngle(Z,W.s*s.flap*.55*Math.max(.25,sp));w1.quaternion.multiply(_q.multiply(_q2));if(sp<0)loc(w1,0,0,W.s*sp*.6);
      loc(B['w'+sd+'2'],0,0,-W.s*SV.flap*.012*sp);loc(B['w'+sd+'3'],0,0,-W.s*SV.flap*.02*sp)}
    // tail: each link replays the body's turning and pitching a moment later, so it whips through every move
    const pr=dt>0?(s.pitch-lastPitch)/dt:0;lastPitch=s.pitch;HIST.unshift([yr,pr]);if(HIST.length>40)HIST.length=40;const now=performance.now()/1000;
    const amp=.05+.05*wk+.1*s.tail*0+.1*p.tail,spd=1.4+2*wk+3*p.tail;
    for(let i=0;i<12;i++){const b=B['tail'+i];if(!b)continue;const uu=i/11,hh=HIST[Math.min(HIST.length-1,i*2)]||[0,0];
      loc(b,-p.tailUp*.05*(1-uu)+clamp(hh[1]*.0012,-.12,.12),Math.sin(now*spd-i*.5)*amp*(.4+uu*.9)-clamp(hh[0]*.03,-.12,.12),0)}
    src.updateMatrixWorld(true);tickPuff(dt);
    // gallop footfalls kick up dust
    if(gl>.5&&wk>.5){for(const k of LEGS){const off=GALLOP.off[k],u=(((u0+off)%1)+1)%1,u1=((((u0-(I.dist||0)/stride)+off)%1)+1)%1;if(u1>u){const pW=V();B[k+'4'].getWorldPosition(pW);pW.y=0;burst(pW,2,.35,.14)}}}
    for(const m of U.mats)m.emissive.setHex(I.flash?0xffffff:0)}
  return{U,S,scene,get cur(){return cur},playG,tick,clips:CL}};
