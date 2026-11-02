// ---------- Cerberus: three hound heads that look about on their own and bite in a rolling volley, a living serpent for a tail, a heavy hound's prowl ----------
FACT.cer=function(){const SCN=scene;const LAB=GLAB('cer');const CB=FACT.__cb===1;const G=window.MODELS[CB?'cerb':'cer']||window.MODELS.cer;const src=T.SkeletonUtils.clone(G.scene);const U={mats:[]};
  const root=new T.Group();SCN.add(root);root.add(src);U.root=root;const V=()=>new T.Vector3();
  const B={};src.traverse(o=>{if(o.isBone)B[o.name]=o});
  src.updateMatrixWorld(true);const box=new T.Box3();src.traverse(o=>{if(o.isMesh){o.geometry.computeBoundingBox();box.union(o.geometry.boundingBox)}});
  const sc=(LAB.mh||1.2)*(CB?.87:1)/(box.max.y-box.min.y);src.scale.setScalar(sc);
  const grad=(()=>{const d=new Uint8Array([170,170,170,255,225,225,225,255,255,255,255,255]);const t=new T.DataTexture(d,3,1,T.RGBAFormat);t.minFilter=t.magFilter=T.LinearFilter;t.needsUpdate=true;return t})();
  src.traverse(o=>{if(o.isMesh){o.frustumCulled=false;const mp=o.material.map;if(mp){mp.encoding=T.LinearEncoding;mp.anisotropy=4;mp.needsUpdate=true}const mat=M('#ffffff',{map:mp,skinning:true,gradientMap:grad,side:T.DoubleSide});mat.userData.outlineParameters={visible:false};U.mats.push(mat);o.material=mat;o.userData.keep=true}});
  const BIND=[];for(const n in B)BIND.push([B[n],B[n].quaternion.clone(),B[n].position.clone()]);
  const J=n=>{const p=V();let b=B[n];while(b&&b.isBone){p.add(b.position);b=b.parent}return p};
  const LEGS=['FL','FR','HL','HR'],INFO={};const X=new T.Vector3(1,0,0),Y=new T.Vector3(0,1,0),Z=new T.Vector3(0,0,1);
  for(const k of LEGS){const p1=J(k+'1'),p2=J(k+'2'),p3=J(k+'3'),p4=J(k+'4'),s=k[1]==='L'?1:-1,front=k[0]==='F';
    INFO[k]={s,front,L1:p1.distanceTo(p2),L2:p2.distanceTo(p3),L3:p3.distanceTo(p4),d3:p4.clone().sub(p3).normalize(),rest:p4.clone(),toeY:p4.y,top:p1,pole:new T.Vector3(s*(front?.12:.22),0,front?-1:1).normalize()}}
  for(const[a,b]of[['FL','FR'],['HL','HR']]){const z=(INFO[a].rest.z+INFO[b].rest.z)/2;INFO[a].rest.z=INFO[b].rest.z=z}
  const pelvis0=B.pelvis.position.clone(),LEG=INFO.HL.L1+INFO.HL.L2+INFO.HL.L3;
  const WING={};
  // ---- poses ----
  const E={io:t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2,out:t=>1-Math.pow(1-t,3),in:t=>t*t*t,lin:t=>t,back:t=>{const c=1.7;return 1+(c+1)*Math.pow(t-1,3)+c*Math.pow(t-1,2)}};
  const P0={h:0,pitch:0,fwd:0,jump:0,arch:0,roll:0,twist:0,headP:0,headY:0,tail:0,tailUp:0,carry:0,claw:0,spread:0,flap:0,bL:0,bM:0,bR:0,sn:0,hup:0,FL:[0,0,0],FR:[0,0,0],HL:[0,0,0],HR:[0,0,0]};
  const P=o=>{const r=Object.assign({},P0,o);for(const k of LEGS)r[k]=(o&&o[k]||[0,0,0]).slice();return r};
  const mixP=(a,b,f)=>{const r={};for(const k in P0){const x=a[k],y=b[k];r[k]=Array.isArray(x)?x.map((v,i)=>v+(y[i]-v)*f):x+(y-x)*f}return r};
  const IDLE=P({});
  const CL={
    idle:{dur:8,loop:true,fn:t=>P({h:Math.sin(t*TAU/4)*.003,arch:Math.sin(t*TAU/4)*1.5,headY:Math.sin(t*TAU/8)*14,headP:Math.sin(t*TAU/5.3)*3,tail:.25})},
    // maul: rear up tall with the wings half open, then crash both forepaws down onto the target
    maul:{dur:1.15,ev:[[.5,'slam']],keys:[[0,IDLE,'io'],
      [.3,P({h:.07,pitch:38,fwd:-.07,arch:-8,FL:[.01,.26,.02],FR:[-.01,.24,.05],HL:[0,0,.03],HR:[0,0,.03],headP:-8,tail:.8,tailUp:.5,claw:1,spread:.55,flap:.7}),'out'],
      [.38,P({h:.08,pitch:42,fwd:-.07,arch:-10,FL:[.01,.28,.03],FR:[-.01,.27,.06],HL:[0,0,.03],HR:[0,0,.03],headP:-10,tail:.9,tailUp:.6,claw:1,spread:.6,flap:.8}),'io'],
      [.5,P({h:-.05,pitch:-12,fwd:.16,arch:10,carry:1,FL:[-.01,0,.12],FR:[.01,0,.14],headP:14,tail:1,tailUp:-.2,claw:1,spread:.5,flap:-.6}),'in'],
      [.7,P({h:-.04,pitch:-9,fwd:.14,arch:8,carry:1,FL:[-.01,0,.12],FR:[.01,0,.14],headP:10,tail:.7,spread:.25,flap:-.2,claw:1}),'io'],[1.15,IDLE,'io']]},
    // swipe: load the shoulder, then a heavy raking blow across the body with the whole torso turning into it
    swipe:{dur:.9,ev:[[.4,'clawL']],keys:[[0,IDLE,'io'],[.22,P({h:-.015,pitch:10,twist:-18,roll:5,fwd:-.03,FL:[.05,.17,-.05],headY:-14,headP:-4,tail:.7,claw:1,spread:.12}),'io'],
      [.4,P({h:-.03,pitch:-4,twist:22,roll:-7,fwd:.08,FL:[-.13,.03,.22],headY:16,headP:6,tail:1,claw:1,spread:.2}),'back'],[.56,P({pitch:-3,twist:14,roll:-4,fwd:.06,FL:[-.1,0,.17],headY:10,tail:.8,claw:1,spread:.1}),'io'],[.9,IDLE,'io']]},
    swipeR:{dur:.9,ev:[[.4,'clawR']],keys:[[0,IDLE,'io'],[.22,P({h:-.015,pitch:10,twist:18,roll:-5,fwd:-.03,FR:[-.05,.17,-.05],headY:14,headP:-4,tail:.7,claw:1,spread:.12}),'io'],
      [.4,P({h:-.03,pitch:-4,twist:-22,roll:7,fwd:.08,FR:[.13,.03,.22],headY:-16,headP:6,tail:1,claw:1,spread:.2}),'back'],[.56,P({pitch:-3,twist:-14,roll:4,fwd:.06,FR:[.1,0,.17],headY:-10,tail:.8,claw:1,spread:.1}),'io'],[.9,IDLE,'io']]},
    // pounce: sink and coil, the tail lashing, explode up with the wings thrown wide, land pinning the target, hop back
    pounce:{dur:1.25,ev:[[.66,'slam']],keys:[[0,IDLE,'io'],[.16,P({h:-.1,pitch:-5,fwd:-.05,twist:6,headP:6,tail:.9,tailUp:-.4,HL:[0,0,.03],HR:[0,0,.03],spread:-.1}),'io'],
      [.28,P({h:-.11,pitch:-6,fwd:-.06,twist:-6,headP:6,tail:1,tailUp:-.4,HL:[0,0,.04],HR:[0,0,.04],spread:-.1}),'io'],[.38,P({h:-.115,pitch:-4,fwd:-.06,headP:5,tail:1,tailUp:-.3,HL:[0,0,.05],HR:[0,0,.05],spread:-.1}),'io'],
      [.52,P({jump:.24,h:.02,pitch:12,fwd:.3,carry:1,arch:-10,FL:[0,.14,.16],FR:[0,.14,.18],HL:[0,.08,-.16],HR:[0,.08,-.16],headP:-6,tail:1,tailUp:.5,claw:1,spread:1,flap:.9}),'out'],
      [.66,P({jump:0,h:-.07,pitch:-14,fwd:.34,carry:1,arch:10,FL:[-.02,0,.12],FR:[.02,0,.14],HL:[0,0,.04],HR:[0,0,.04],headP:14,tail:1,claw:1,spread:.8,flap:-.7}),'in'],
      [.84,P({h:-.05,pitch:-10,fwd:.3,carry:1,arch:8,FL:[-.02,0,.12],FR:[.02,0,.14],headP:10,tail:.8,claw:1,spread:.35,flap:-.2}),'io'],
      [1,P({jump:.06,fwd:.12,carry:1,pitch:4,FL:[0,.05,.03],FR:[0,.05,.03],HL:[0,.04,0],HR:[0,.04,0],tail:.6,spread:.15}),'io'],[1.25,IDLE,'io']]},
    // tribite: the three heads strike one after another (right, middle, left), each rearing back before it snaps forward
    tribite:{dur:.8,ev:[[.2,'biteR'],[.36,'biteM'],[.52,'biteL']],fn:t=>{const bt=t0=>t<t0-.15?-.55*E.io(clamp((t-(t0-.32))/.17,0,1)):t<t0?-.55+1.55*E.in((t-(t0-.15))/.15):Math.max(0,1-E.out((t-t0)/.22));
      const env=Math.sin(clamp(t/.8,0,1)*Math.PI);return P({bR:bt(.2),bM:bt(.36),bL:bt(.52),pitch:-4*env,fwd:.05*env,h:-.012*env,twist:(t<.36?6:-6)*env,tail:.6,claw:.3,FL:[0,0,.03*env],FR:[0,0,.03*env]})}},
    // fang: the serpent tail rears high over the back, then lashes forward past the heads
    fang:{dur:.8,ev:[[.42,'fang']],keys:[[0,IDLE,'io'],[.3,P({sn:-.9,pitch:4,h:-.01,headP:-4,tail:.4}),'io'],[.42,P({sn:1,pitch:-4,fwd:.04,h:-.02,headP:6,tail:.4}),'in'],[.56,P({sn:.85,pitch:-3,fwd:.03,tail:.4}),'io'],[.8,IDLE,'io']]},
    // breath: all three heads thrust forward and pour out hellfire
    breath:{dur:.75,ev:[[.22,'fire'],[.32,'fire'],[.42,'fire'],[.52,'fire']],fn:t=>{const k=t<.18?E.io(t/.18)*-.4:t<.24?-.4+1.0*E.out((t-.18)/.06):t<.58?.6+Math.sin(t*60)*.05:.6*(1-E.io((t-.58)/.17));
      return P({bL:k,bM:k,bR:k,pitch:-3*Math.max(0,k),h:-.01*Math.max(0,k),fwd:-.02*Math.max(0,k),tail:.5})}},
    // inferno (the grown Cerberus): all three heads lock forward and pour out a long roaring stream of hellfire, the body sweeping it left and right
    inferno:{dur:1.5,ev:Array.from({length:20},(_,i)=>[.3+i*.05,'fire2']),fn:t=>{const on=t<.22?-.5*E.io(t/.22):t<.3?-.5+1.05*E.out((t-.22)/.08):t<1.28?.55+Math.sin(t*47)*.04:.55*(1-E.io((t-1.28)/.22));const sw=t>.3&&t<1.28?Math.sin((t-.3)/.98*Math.PI*2)*16:0;
      return P({bL:on,bM:on,bR:on,twist:sw,pitch:-4*Math.max(0,on),h:-.015*Math.max(0,on),fwd:-.03*Math.max(0,on),tail:.8,FL:[0,0,.02],FR:[0,0,.02]})}},
    // howl: all three heads thrown back to the sky
    howl:{dur:1.6,ev:Array.from({length:12},(_,i)=>[.42+i*.07,'pillar']),keys:[[0,IDLE,'io'],[.3,P({hup:1,pitch:10,h:.02,HL:[0,0,.02],HR:[0,0,.02],tail:.8}),'out'],[1.2,P({hup:1,pitch:11,h:.02,HL:[0,0,.02],HR:[0,0,.02],tail:.9}),'io'],[1.6,IDLE,'io']]},
    kneel:{dur:3.5,keys:[[0,IDLE,'io'],[3.5,IDLE,'io']]}};
  CL.down={dur:2.6,keys:[[0,IDLE,'io'],[2.6,IDLE,'io']]};CL.rise=CL.down;
  // everything plays at real big-cat speed: attack timings compressed
  const TS=LAB.ts||.52;for(const n of['maul','swipe','swipeR','pounce']){const c=CL[n];c.dur*=TS;for(const k of c.keys)k[0]*=TS;if(c.ev)for(const e of c.ev)e[0]*=TS}
  const sample=(n,t)=>{const c=CL[n];if(c.fn)return c.fn(t);const k=c.keys;if(t>=k[k.length-1][0])return k[k.length-1][1];for(let i=0;i<k.length-1;i++)if(t<k[i+1][0]){const f=(t-k[i][0])/(k[i+1][0]-k[i][0]);return mixP(k[i][1],k[i+1][1],E[k[i+1][2]](f))}return k[0][1]};
  const S={x:0,z:0,yaw:0,vel:0,wamt:0,gal:0,clip:'idle',t:0,rate:1,hold:false,prev:null,bl:0,blT:.12,lastT:0};let cur=IDLE;
  function playG(n,rate,off){if(!CL[n])n='idle';S.prev=cur;S.bl=S.blT;S.clip=n;S.rate=rate||1;S.t=off||0;S.lastT=S.t}
  // springs: the body follows the pose like something heavy (slight lag, a little overshoot, then settles)
  const SPR=['h','pitch','fwd','jump','arch','roll','twist','headP','headY','spread','flap','bL','bM','bR','sn','hup'],K={h:1500,pitch:1100,fwd:1400,jump:1600,arch:900,roll:900,twist:900,headP:700,headY:500,spread:800,flap:1500,bL:1900,bM:1900,bR:1900,sn:900,hup:500},ZT={bL:.55,bM:.55,bR:.55,sn:.5,flap:.5,spread:.7,headY:.65,headP:.6,pitch:.62,fwd:.6};
  const SP={},SV={};for(const k of SPR){SP[k]=0;SV[k]=0}
  function spring(p,dt){const o=Object.assign({},p);const n=Math.max(1,Math.ceil(dt/.008)),h=dt/n;for(const k of SPR){const kk=K[k],c=2*(ZT[k]||.7)*Math.sqrt(kk);for(let i=0;i<n;i++){SV[k]+=(kk*(p[k]-SP[k])-c*SV[k])*h;SP[k]+=SV[k]*h}o[k]=SP[k]}return o}
  // ---- dust ----
  const dustTex=(()=>{const c=document.createElement('canvas');c.width=c.height=64;const g=c.getContext('2d'),gr=g.createRadialGradient(32,32,0,32,32,30);gr.addColorStop(0,'rgba(236,222,190,.95)');gr.addColorStop(1,'rgba(236,222,190,0)');g.fillStyle=gr;g.fillRect(0,0,64,64);const t=new T.CanvasTexture(c);return t})();
  const PUFF=[];function puff(p,vel,size,life){const m=new T.SpriteMaterial({map:dustTex,transparent:true,depthWrite:false,opacity:.9});m.userData={noflash:true};const sp=new T.Sprite(m);sp.position.copy(p);sp.scale.setScalar(size);SCN.add(sp);PUFF.push({sp,v:vel,t:0,life,size})}
  function burst(cW,n,spd,size,dir){for(let i=0;i<n;i++){const a=i/n*TAU+Math.random()*.4,v=new T.Vector3(Math.cos(a),0,Math.sin(a)).multiplyScalar(spd*(.6+Math.random()*.6));if(dir)v.addScaledVector(dir,spd*1.6);v.y=spd*.35*Math.random();puff(cW.clone().add(new T.Vector3(0,.04,0)),v,size*(.7+Math.random()*.6),.55+Math.random()*.35)}}
  function tickPuff(dt){for(let i=PUFF.length-1;i>=0;i--){const q=PUFF[i];q.t+=dt;const k=q.t/q.life;q.sp.position.addScaledVector(q.v,dt);q.v.multiplyScalar(Math.exp(-dt*(q.fire?1.2:3)));q.sp.scale.setScalar(q.size*(1+k*1.6));q.sp.material.opacity=.85*(1-k);if(k>=1){SCN.remove(q.sp);PUFF.splice(i,1)}}}
  // shockwave rings on the ground and claw streaks in the air
  const FX=[];function addFx(m,life,upd){m.material.userData={noflash:true};SCN.add(m);FX.push({m,t:0,life,upd})}
  function tickFx(dt){for(let i=FX.length-1;i>=0;i--){const f=FX[i];f.t+=dt;const k=Math.min(1,f.t/f.life);f.upd(f.m,k);if(k>=1){SCN.remove(f.m);FX.splice(i,1)}}}
  function ring(pW,R,life,col){const m=new T.Mesh(new T.RingGeometry(.95,1,72),new T.MeshBasicMaterial({color:col||0xfff2c8,transparent:true,depthWrite:false,side:T.DoubleSide,blending:T.AdditiveBlending}));
    m.rotation.x=-Math.PI/2;m.position.set(pW.x,.03,pW.z);addFx(m,life,(m,k)=>{m.scale.setScalar(R*(.2+.8*E.out(k)));m.material.opacity=(1-k)*(1-k)*.45})}
  function claw(side){const fw=V().set(0,0,1).applyQuaternion(root.quaternion),rt=V().set(-1,0,0).applyQuaternion(root.quaternion),c=V();B.chest.getWorldPosition(c);c.addScaledVector(fw,.42*sc);c.y=.34*sc;
    for(let i=0;i<3;i++){const g=new T.RingGeometry(.9,1,40,1,Math.PI*.15,Math.PI*.7);const m=new T.Mesh(g,new T.MeshBasicMaterial({color:i==1?0xffffff:0xffe08a,transparent:true,depthWrite:false,side:T.DoubleSide,blending:T.AdditiveBlending}));
      m.position.copy(c).addScaledVector(rt,(i-1)*.07*sc).addScaledVector(fw,(i-1)*.01);m.lookAt(m.position.clone().addScaledVector(rt,1));m.rotateZ(side*.5+Math.PI*.5);m.scale.setScalar(.28*sc);
      addFx(m,.22,(m,k)=>{m.material.opacity=(1-k);m.scale.setScalar(.28*sc*(1+k*.35))})}}
  // flying debris: dirt clods and rock chips that arc up, tumble, bounce and settle, then sink away
  const CHG=new T.DodecahedronGeometry(1,0),CHM=['#8a6a45','#6f5236','#a5845a','#9a9188','#7c7468'].map(c=>{const m=M(c);m.userData.noflash=true;m.userData.outlineParameters={visible:false};return m});
  const CH=[];function chunks(pW,n,pow,big){for(let i=0;i<n;i++){const a=Math.random()*TAU,sp=(.4+Math.random())*pow*sc,m=new T.Mesh(CHG,CHM[(Math.random()*CHM.length)|0]);
      const r=(.012+Math.random()*.028*(big||1))*sc;m.scale.set(r,r*(.6+Math.random()*.5),r*(.8+Math.random()*.4));m.position.set(pW.x+Math.cos(a)*.05*sc,r,pW.z+Math.sin(a)*.05*sc);m.rotation.set(Math.random()*3,Math.random()*3,0);SCN.add(m);
      CH.push({m,r,v:new T.Vector3(Math.cos(a)*sp,(1.2+Math.random()*1.6)*pow*sc,Math.sin(a)*sp),w:new T.Vector3(Math.random()-.5,Math.random()-.5,Math.random()-.5).multiplyScalar(18),t:0,life:1.3+Math.random()*.6})}}
  function tickChunks(dt){const g=9.8*sc;for(let i=CH.length-1;i>=0;i--){const c=CH[i];c.t+=dt;c.v.y-=g*dt;c.m.position.addScaledVector(c.v,dt);
      if(c.m.position.y<c.r*.6){c.m.position.y=c.r*.6;if(c.v.y<0){c.v.y*=-.32;c.v.x*=.55;c.v.z*=.55;c.w.multiplyScalar(.5)}if(Math.abs(c.v.y)<.15)c.v.y=0}
      c.m.rotation.x+=c.w.x*dt;c.m.rotation.y+=c.w.y*dt;c.m.rotation.z+=c.w.z*dt;const k=(c.t-c.life+.4)/.4;if(k>0){c.m.position.y-=dt*c.r*3;c.m.scale.multiplyScalar(1-dt*2)}
      if(c.t>c.life){SCN.remove(c.m);CH.splice(i,1)}}}
  // ground cracks: a decal of splintering dark lines that fades out
  const crackTex=(()=>{const c=document.createElement('canvas');c.width=c.height=256;const g=c.getContext('2d');g.strokeStyle='rgba(74,54,38,.8)';g.lineCap='round';
    for(let i=0;i<9;i++){let a=i/9*TAU+Math.random()*.5,x=128,y=128,w=5;g.beginPath();g.moveTo(x,y);for(let k=0;k<7;k++){a+=(Math.random()-.5)*.8;const L=10+Math.random()*12;x+=Math.cos(a)*L;y+=Math.sin(a)*L;g.lineWidth=w;g.lineTo(x,y);w=Math.max(1,w*.78)
      if(Math.random()<.3){g.stroke();g.beginPath();const b=a+(Math.random()<.5?1:-1)*.9;g.moveTo(x,y);g.lineTo(x+Math.cos(b)*14,y+Math.sin(b)*14);g.stroke();g.beginPath();g.moveTo(x,y)}}g.stroke()}
    g.fillStyle='rgba(70,52,36,.35)';g.beginPath();g.arc(128,128,16,0,TAU);g.fill();const t=new T.CanvasTexture(c);return t})();
  function crack(pW,R,life){const m=new T.Mesh(new T.PlaneGeometry(2,2),new T.MeshBasicMaterial({map:crackTex,transparent:true,depthWrite:false,opacity:0}));m.rotation.x=-Math.PI/2;m.rotation.z=Math.random()*TAU;m.position.set(pW.x,.012,pW.z);
    addFx(m,life,(m,k)=>{m.scale.setScalar(R*Math.min(1,.4+k*6));m.material.opacity=k<.7?.62:.62*(1-(k-.7)/.3)})}
  const shake=v=>{if(LAB.api&&LAB.api.shake)LAB.api.shake(v)};
  const fireTex=(()=>{const c=document.createElement('canvas');c.width=c.height=64;const g=c.getContext('2d'),gr=g.createRadialGradient(32,32,0,32,32,30);gr.addColorStop(0,'rgba(255,240,170,1)');gr.addColorStop(.35,'rgba(255,140,40,.9)');gr.addColorStop(1,'rgba(200,30,10,0)');g.fillStyle=gr;g.fillRect(0,0,64,64);return new T.CanvasTexture(c)})();
  function flame(p,v,size,life){const m=new T.SpriteMaterial({map:fireTex,transparent:true,depthWrite:false,blending:T.AdditiveBlending});m.userData={noflash:true};const sp=new T.Sprite(m);sp.position.copy(p);sp.scale.setScalar(size);SCN.add(sp);PUFF.push({sp,v,t:0,life,size,fire:1})}
  function bite(pW,col){const fw=V().set(0,0,1).applyQuaternion(root.quaternion),rt=V().set(-1,0,0).applyQuaternion(root.quaternion);
    for(let i=0;i<2;i++){const m=new T.Mesh(new T.RingGeometry(.86,1,32,1,Math.PI*.2,Math.PI*.6),new T.MeshBasicMaterial({color:i?0xffffff:col,transparent:true,depthWrite:false,side:T.DoubleSide,blending:T.AdditiveBlending}));
      m.position.copy(pW).addScaledVector(fw,.04*sc);m.lookAt(m.position.clone().addScaledVector(fw,1));m.rotateZ(i?Math.PI:0);m.scale.setScalar(.09*sc);addFx(m,.18,(m,k)=>{m.material.opacity=1-k;m.scale.setScalar(.09*sc*(1-k*.45))})}}
  function fire(ev){const pW=V(),fw=V().set(0,0,1).applyQuaternion(root.quaternion);
    if((ev==='biteL'||ev==='biteM'||ev==='biteR')&&B['ns'+ev[4]]){B['ns'+ev[4]].getWorldPosition(pW);bite(pW,0xff5a2a);S.stop=.035;shake(.18)}
    const hdir=k=>{const a=V(),b=V();B['hd'+k].getWorldPosition(a);B['ns'+k].getWorldPosition(b);const d=b.sub(a);d.y*=.3;return d.normalize().lerp(fw,.3).normalize()};
    if(ev==='fire2'){for(const k of[...'LMR'].filter(k=>B['ns'+k])){B['ns'+k].getWorldPosition(pW);const d=hdir(k);for(let i=0;i<4;i++){const v=d.clone().multiplyScalar((1.9+Math.random()*.9)*sc).add(V().set((Math.random()-.5)*.35*sc,(Math.random()-.3)*.25*sc,(Math.random()-.5)*.35*sc));flame(pW.clone(),v,(.13+Math.random()*.13)*sc,.45+Math.random()*.3)}}if(Math.random()<.3)shake(.05)}
    if(ev==='pillar'){for(const k of[...'LMR'].filter(k=>B['ns'+k])){B['ns'+k].getWorldPosition(pW);for(let i=0;i<3;i++)flame(pW.clone(),V().set((Math.random()-.5)*.3*sc,(1.6+Math.random()*.8)*sc,(Math.random()-.5)*.3*sc),(.14+Math.random()*.1)*sc,.5+Math.random()*.25)}if(Math.random()<.4)shake(.12)}
    if(ev==='fire'){const hs=[...'LMR'].filter(k=>B['ns'+k]);for(const k of hs){B['ns'+k].getWorldPosition(pW);const hd=hdir(k);for(let i=0;i<(hs.length>1?3:5);i++){const v=hd.clone().multiplyScalar((1.1+Math.random()*.7)*sc).add(V().set((Math.random()-.5)*.4*sc,(Math.random()-.2)*.25*sc,(Math.random()-.5)*.4*sc));flame(pW.clone(),v,(.09+Math.random()*.07)*sc,.38+Math.random()*.2)}}shake(.06)}
    if(ev==='fang'&&B.tail10){B.tail10.getWorldPosition(pW);bite(pW,0x9cff6a);S.stop=.04;shake(.15)}
    if(ev==='slam'){for(const k of['FL','FR']){B[k+'4'].getWorldPosition(pW);pW.y=0;burst(pW,6,1,.22);chunks(pW,6,.9)}B.FL4.getWorldPosition(pW);crack(pW,.32*sc,1.4);ring(pW,.6*sc,.3);S.stop=.08;shake(.45)}
    if(ev==='clawL'||ev==='clawR'){claw(ev==='clawL'?1:-1);S.stop=.07;shake(.3)}
    if(ev==='gust'){root.getWorldPosition(pW);pW.addScaledVector(fw,.6*sc);pW.y=0;burst(pW,16,1.1,.32,fw);ring(pW,.8*sc,.4,0xd8ecff);S.stop=.05;shake(.35)}
    if(ev==='launch'){root.getWorldPosition(pW);pW.y=0;burst(pW,12,1.1,.28);chunks(pW,7,.7)}
    if(ev==='quake'){B.FL4.getWorldPosition(pW);const pR=V();B.FR4.getWorldPosition(pR);pW.add(pR).multiplyScalar(.5);pW.y=0;burst(pW,22,1.5,.34);chunks(pW,26,1.25,1.6);crack(pW,.75*sc,2.2);ring(pW,1.7*sc,.5);S.stop=.12;shake(1);if(LAB.onQuake)LAB.onQuake()}}
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
  const PROWL={stride:.58,duty:.66,off:{HL:0,FL:.25,HR:.5,FR:.75},lift:{F:.085,H:.06}};
  const GALLOP={stride:.66,duty:.36,off:{HL:0,HR:.11,FL:.48,FR:.6},lift:{F:.13,H:.1}};
  let ph=0,earlyY=0;const HIST=[];let lastYaw=0,lastPitch=0;
  function footCycle(g,k,u){const D=g.duty,A=g.stride*D/2;let z,y=0,curl=0;if(u<D)z=lerp(A,-A,u/D);else{const q=(u-D)/(1-D);z=lerp(-A,A,E.io(q));y=Math.sin(q*Math.PI)*g.lift[k[0]];curl=Math.sin(q*Math.PI)}return[z,y,curl]}
  function tick(dt,I){S.x=I.x;S.z=I.z;let df=I.yaw-S.yaw;df=Math.atan2(Math.sin(df),Math.cos(df));S.yaw+=df*Math.min(1,dt*(S.clip==='idle'?6:12));S.vel=I.speed;
    if(S.stop>0){S.stop-=dt;dt*=.06}const c=CL[S.clip];const t0=S.t;S.t+=dt*S.rate;if(c.ev)for(const[et,en]of c.ev)if(t0<et&&S.t>=et)fire(en);
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
    const yr=dt>0?df/dt:0;const now=performance.now()/1000;
    // three heads: each keeps its own gaze (the outer two watch the flanks), snarls, and lunges on its own beat
    for(const[k,i,out]of[['L',0,-1],['M',1,0],['R',2,1]]){const nk=B['nk'+k],hd=B['hd'+k];if(!nk)continue;const b=s['b'+k],look=Math.sin(now*(.55+i*.17)+i*2.1)*.22+out*.12,sn=Math.sin(now*23+i*5)*.02*(1-wk);
      loc(nk,rad(s.pitch)*.45+rad(s.headP)*.3+rad(s.arch)*-.3+b*.55-s.hup*.55,look*.45-rad(s.twist)*.3+clamp(yr*.03,-.2,.2),out*b*.08);
      loc(hd,rad(s.pitch)*.3+rad(s.headP)*.5-b*.22-s.hup*.5+sn+Math.sin(now*1.3+i)*.04,look*.55+clamp(yr*.03,-.2,.2),-rad(s.roll)*.5+(s.hup?Math.sin(now*9+i)*.06*s.hup:0))}
    // wings: fold <-> spread, then beat about the body axis; the inner wing leads, the outer feathers follow
    for(const sd of['L','R']){const W=WING[sd],w1=B['w'+sd+'1'];if(!w1)continue;const sp=clamp(s.spread,-.15,1.1);
      _q2.identity();if(sp>0)_q2.slerp(W.q,Math.min(1,sp));else _q2.setFromAxisAngle(Y,-W.s*sp*.0);
      _q.setFromAxisAngle(Z,W.s*s.flap*.55*Math.max(.25,sp));w1.quaternion.multiply(_q.multiply(_q2));if(sp<0)loc(w1,0,0,W.s*sp*.6);
      loc(B['w'+sd+'2'],0,0,-W.s*SV.flap*.012*sp);loc(B['w'+sd+'3'],0,0,-W.s*SV.flap*.02*sp)}
    // tail: each link replays the body's turning and pitching a moment later, so it whips through every move
    const pr=dt>0?(s.pitch-lastPitch)/dt:0;lastPitch=s.pitch;HIST.unshift([yr,pr]);if(HIST.length>40)HIST.length=40;
    const amp=.05+.05*wk+.1*s.tail*0+.1*p.tail,spd=1.4+2*wk+3*p.tail;
    // serpent tail: a slow S-sway down the coils, the head held level and watching; it rears and strikes on 'sn'
    if(!B.tail8){for(let i=0;i<6;i++){const b=B['tail'+i];if(!b)continue;const uu=i/5,hh=HIST[Math.min(HIST.length-1,i*2)]||[0,0];
      loc(b,-p.tailUp*.08+(i<2?-.12*wk:0)+clamp(hh[1]*.001,-.1,.1),Math.sin(now*(4+5*wk+4*p.tail)-i*.7)*(.12+.1*p.tail)*(.5+uu)-clamp(hh[0]*.03,-.12,.12),0)}}
    else for(let i=0;i<10;i++){const b=B['tail'+i];if(!b)continue;const uu=i/9,hh=HIST[Math.min(HIST.length-1,i*2)]||[0,0];
      const sw=Math.sin(now*(1.5+wk)-i*.55)*(.05+.03*wk)*(.4+uu)-clamp(hh[0]*.025,-.1,.1);
      const pt=(i>=3&&i<=6?s.sn*.34:0)+(i>=7?-s.sn*.36:0)+(i<3?-p.tailUp*.04:0)+clamp(hh[1]*.001,-.1,.1)+(i>=7?Math.sin(now*.9+1)*.06:0);
      loc(b,pt,sw+(i===8?Math.sin(now*.7)*.25:0),i<3?sw*.6:0)}
    src.updateMatrixWorld(true);tickPuff(dt);tickFx(dt);tickChunks(dt);
    // gallop footfalls kick up dust
    if(gl>.5&&wk>.5){for(const k of LEGS){const off=GALLOP.off[k],u=(((u0+off)%1)+1)%1,u1=((((u0-(I.dist||0)/stride)+off)%1)+1)%1;if(u1>u){const pW=V();B[k+'4'].getWorldPosition(pW);pW.y=0;burst(pW,2,.35,.14)}}}
    for(const m of U.mats)m.emissive.setHex(I.flash?0xffffff:0)}
  return{U,S,scene,get cur(){return cur},playG,tick,clips:CL}};