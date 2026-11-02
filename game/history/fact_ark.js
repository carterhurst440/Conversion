// ---------- the Scarab Ark: bearers march it in, it holds back, and every few seconds the scarab's shell swings open and a brood pours out,
// skitters to the enemy, climbs on and bursts. Stop it by reaching it. ----------
FACT.ark=function(){const G=window.TRIPO;const src=T.SkeletonUtils.clone(G.scene);const U={mats:[]};const V=(x,y,z)=>new T.Vector3(x||0,y||0,z||0);
  const root=new T.Group();scene.add(root);root.add(src);U.root=root;const B={};src.traverse(o=>{if(o.isBone)B[o.name]=o});
  src.updateMatrixWorld(true);const box=new T.Box3();src.traverse(o=>{if(o.isMesh){o.geometry.computeBoundingBox();box.union(o.geometry.boundingBox)}});
  const sc=(LAB.mh||.95)/(box.max.y-box.min.y);src.scale.setScalar(sc);
  const grad=(()=>{const d=new Uint8Array([150,150,150,255,214,214,214,255,255,255,255,255]);const t=new T.DataTexture(d,3,1,T.RGBAFormat);t.minFilter=t.magFilter=T.LinearFilter;t.needsUpdate=true;return t})();
  src.traverse(o=>{if(o.isMesh){o.frustumCulled=false;const mat=M('#ffffff',{vertexColors:true,skinning:true,gradientMap:grad,side:T.DoubleSide});mat.userData.outlineParameters={visible:false};U.mats.push(mat);o.material=mat;o.userData.keep=true}});
  const BIND=[];for(const n in B)BIND.push([B[n],B[n].quaternion.clone(),B[n].position.clone()]);
  const E={io:t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2,out:t=>1-Math.pow(1-t,3),in:t=>t*t*t,back:t=>{const c=1.8;return 1+(c+1)*Math.pow(t-1,3)+c*Math.pow(t-1,2)}};
  // the open cycle: shudder, swing the wing cases up and out, hold while the brood pours out, close with a thump
  const OPEN=2.8,SPAWN=[.55,1.75];
  const openAt=t=>t<.25?.06*Math.sin(t/.25*Math.PI*3)*(t/.25):t<.62?E.back((t-.25)/.37):t<2.2?1:t<2.6?1-E.in((t-2.2)/.4):0;
  const S={x:0,z:0,yaw:0,vel:0,wamt:0,clip:'idle',t:0,rate:1,hold:false,open:0,ov:0,ph:0,wheel:0};
  function playG(n,rate,off){S.clip=n==='plague'?'plague':n==='open'||n==='whirl'?'open':'idle';S.t=off||0;S.rate=rate||1;S.spawned=0}
  // plague: rumble and build the glow, burst wide open in a flash, a flying swarm spirals out and sweeps onto the enemy
  const PLAG=3.6,plagueAt=t=>t<.85?.12*(t/.85)+.05*Math.sin(t*70)*(t/.85):t<1.15?.12+1.33*E.out((t-.85)/.3):t<2.7?1.42-.1*Math.min(1,(t-1.15)/.4):t<3.2?1.32*(1-E.in((t-2.7)/.5)):0;
  const wingG=new T.PlaneGeometry(1.1,.55);wingG.translate(.55,0,0);const mW=new T.MeshBasicMaterial({color:'#d9f3ff',transparent:true,opacity:.65,side:T.DoubleSide,depthWrite:false});mW.userData={noflash:true};
  const FLY=[];let cloud=null;
  function mkFlyer(){const g=new T.Group(),b=new T.Mesh(bodyG,mB);g.add(b);const h=new T.Mesh(headG,mG);h.position.set(0,.12,.95);g.add(h);const w1=new T.Mesh(wingG,mW),w2=new T.Mesh(wingG,mW);w1.position.y=.5;w2.position.y=.5;w2.rotation.y=Math.PI;g.add(w1);g.add(w2);g.userData.w=[w1,w2];g.scale.setScalar(.045*sc);return g}
  function startPlague(){if(LAB.noFlyers)return;const o=V();B.beetle.localToWorld(o.set(0,.62,-.02));cloud={t:0,c:o.clone(),o:o.clone(),tick:0};
    for(let i=0;i<90;i++){const g=mkFlyer();g.position.copy(o);scene.add(g);FLY.push({g,born:.04*i,a:Math.random()*TAU,r:(.08+Math.random()*.32)*sc,h:(Math.random()-.5)*.35*sc,w:(2.2+Math.random()*2.5)*(Math.random()<.5?-1:1),ph:Math.random()*TAU})}}
  function tickPlague(dt){if(!cloud)return;cloud.t+=dt;const t=cloud.t,tg=target(),now=performance.now()/1000;
    // the cloud: rises out of the chamber, hangs, then rolls onto the target and churns there before breaking apart
    const up=cloud.o.clone().add(V(0,.55*sc,0));let C;if(t<1.4)C=cloud.o.clone().lerp(up,E.out(Math.min(1,t/1.4)));else if(tg){const k=E.io(Math.min(1,(t-1.4)/1.1));C=up.clone().lerp(V(tg.x,.32*sc,tg.z),k)}else C=up;cloud.c.copy(C);
    const spread=t<1.4?.4+t*.45:1.05,fade=t>6?Math.max(0,1-(t-6)/.8):1;
    for(let i=FLY.length-1;i>=0;i--){const q=FLY[i],g=q.g;if(t<q.born){g.visible=false;continue}g.visible=true;q.a+=q.w*dt;const r=q.r*spread*(t>6?1+(t-6)*3:1);
      const p=V(C.x+Math.cos(q.a)*r,C.y+q.h+Math.sin(now*3+q.ph)*.06*sc+(t-q.born<.5?-(.5-(t-q.born))*.4*sc:0),C.z+Math.sin(q.a)*r);g.position.lerp(p,Math.min(1,dt*8));
      g.rotation.set(.2,q.a+(q.w>0?0:Math.PI),Math.sin(now*6+q.ph)*.3);const fl=Math.sin(now*55+q.ph)*.9;g.userData.w[0].rotation.z=fl;g.userData.w[1].rotation.z=-fl;
      g.children[0].material.opacity=1;g.scale.setScalar(.045*sc*fade);if(fade<=0){scene.remove(g);FLY.splice(i,1)}}
    if(tg&&t>2.3&&t<6.2){cloud.tick-=dt;if(cloud.tick<=0){cloud.tick=.28;if(LAB.onPlague)LAB.onPlague()}}
    if(!FLY.length)cloud=null}
  // glow inside the chamber
  const glow=egSprite(EGT.glow,.55,'#ffcf6a');glow.material.opacity=0;B.beetle.add(glow);glow.position.set(0,.555,-.04);glow.scale.setScalar(.3/sc);
  // ---- the brood: little lapis-and-gold scarabs ----
  const bodyG=new T.SphereGeometry(1,8,6,0,TAU,0,Math.PI*.55);bodyG.scale(.62,.55,1);const headG=new T.SphereGeometry(.42,6,5);const legG=new T.BoxGeometry(1.7,.08,.09);
  const mB=M('#2546b4'),mG=M('#e6b84a'),mK=M('#1a1622');for(const x of[mB,mG,mK]){x.userData.outlineParameters={visible:false};x.userData.noflash=true}
  const seamG=new T.BoxGeometry(.08,.06,1.9);
  function mkScarab(){const g=new T.Group(),b=new T.Mesh(bodyG,mB);g.add(b);const s=new T.Mesh(seamG,mG);s.position.y=.52;s.scale.y=.6;g.add(s);const h=new T.Mesh(headG,mG);h.position.set(0,.12,.95);g.add(h);
    const legs=[];for(const z of[.45,0,-.45]){const l=new T.Mesh(legG,mK);l.position.set(0,.04,z);g.add(l);legs.push(l)}g.userData.legs=legs;g.scale.setScalar(.052*sc);return g}
  const SW=[];const MAXS=30;
  const dustTex=(()=>{const c=document.createElement('canvas');c.width=c.height=64;const g=c.getContext('2d'),gr=g.createRadialGradient(32,32,0,32,32,30);gr.addColorStop(0,'rgba(255,226,140,1)');gr.addColorStop(.4,'rgba(240,190,80,.7)');gr.addColorStop(1,'rgba(240,190,80,0)');g.fillStyle=gr;g.fillRect(0,0,64,64);return new T.CanvasTexture(c)})();
  const PUFF=[];function puff(p,n,sz){for(let i=0;i<n;i++){const m=new T.SpriteMaterial({map:dustTex,transparent:true,depthWrite:false,blending:T.AdditiveBlending});m.userData={noflash:true};const s=new T.Sprite(m);s.position.copy(p);s.scale.setScalar(sz);scene.add(s);
    const a=Math.random()*TAU;PUFF.push({s,v:V(Math.cos(a)*.5,.4+Math.random()*.6,Math.sin(a)*.5).multiplyScalar(sz*3),t:0,L:.45+Math.random()*.25,sz})}}
  const target=()=>{const d=LAB.api&&LAB.api.dum;return d?d.g.position:null};
  function spawnOne(){if(LAB.noSwarm||SW.length>=MAXS)return;const g=mkScarab();const o=V();B.beetle.localToWorld(o.set((Math.random()-.5)*.16,.6,(Math.random()-.5)*.24));g.position.copy(o);scene.add(g);
    const a=Math.random()*TAU,r=(.35+Math.random()*.25)*sc,land=V(o.x+Math.cos(a)*r,0,o.z+Math.sin(a)*r);
    SW.push({g,st:'out',t:0,T:.45+Math.random()*.2,a:o.clone(),b:land,sp:(1.3+Math.random()*.6)*sc,wig:Math.random()*TAU,h:0,hold:0,ang:Math.random()*TAU})}
  function tickSwarm(dt){const tg=target();const now=performance.now()/1000;
    for(let i=SW.length-1;i>=0;i--){const q=SW[i],g=q.g;q.t+=dt;
      if(q.st==='out'){const k=Math.min(1,q.t/q.T);g.position.lerpVectors(q.a,q.b,k);g.position.y+=Math.sin(k*Math.PI)*.25*sc*(1-k*.3);g.rotation.x+=dt*14;if(k>=1){q.st='run';g.rotation.set(0,0,0)}}
      else if(q.st==='run'){if(!tg){q.t=99}else{const dx=tg.x-g.position.x,dz=tg.z-g.position.z,d=Math.hypot(dx,dz);const yaw=Math.atan2(dx,dz)+Math.sin(now*9+q.wig)*.45;
          g.rotation.set(0,yaw,0);const st=Math.min(d,q.sp*dt);g.position.x+=Math.sin(yaw)*st;g.position.z+=Math.cos(yaw)*st;g.position.y=.004*sc;
          if(d<.13*sc+Math.random()*.02){q.st='climb';q.t=0;q.c0=g.position.clone();q.h=(.12+Math.random()*.42)*sc;q.ang=Math.atan2(g.position.x-tg.x,g.position.z-tg.z)+(Math.random()-.5)*.8}}}
      else if(q.st==='climb'){const k=Math.min(1,q.t/.35),R=.1*sc;const pos=V(tg.x+Math.sin(q.ang)*R,q.h*k,tg.z+Math.cos(q.ang)*R);g.position.lerp(pos,.5);g.rotation.set(-Math.PI/2*k,q.ang+Math.PI,0);
        q.ang+=dt*(Math.sin(now*7+q.wig)*1.2);if(q.t>.35+.3+Math.random()*.1){q.st='pop'}}
      if(q.st==='pop'||q.t>8){puff(g.position,3,.07*sc);if(q.st==='pop'&&LAB.onBurst)LAB.onBurst();scene.remove(g);SW.splice(i,1);continue}
      for(let k=0;k<3;k++)q.g.userData.legs[k].rotation.y=Math.sin(now*40+k*2+q.wig)*.5}
    for(let i=PUFF.length-1;i>=0;i--){const p=PUFF[i];p.t+=dt;const k=p.t/p.L;p.s.position.addScaledVector(p.v,dt);p.v.multiplyScalar(Math.exp(-dt*4));p.s.scale.setScalar(p.sz*(1+k*1.5));p.s.material.opacity=1-k;if(k>=1){scene.remove(p.s);PUFF.splice(i,1)}}}
  const _q=new T.Quaternion(),_q2=new T.Quaternion(),X=V(1,0,0),Z=V(0,0,1);
  // ---- Tripo bearers: four copies, poles resting on a shoulder, both fists locked on the moving pole, feet stepping with planted contacts ----
  const PORT=[];
  if(window.BEARER){const BG=window.BEARER.scene;BG.updateMatrixWorld(true);const BQ={},BP={};BG.traverse(b=>{if(b.isBone){BQ[b.name]=b.getWorldQuaternion(new T.Quaternion());BP[b.name]=b.getWorldPosition(V())}});
    const LA=s=>[BP[s+'_Upperarm'].distanceTo(BP[s+'_Forearm']),BP[s+'_Forearm'].distanceTo(BP[s+'_Hand'])],LL=s=>[BP[s+'_Thigh'].distanceTo(BP[s+'_Calf']),BP[s+'_Calf'].distanceTo(BP[s+'_Foot'])];
    const hip0=BP.Hip.clone(),ANK=BP.L_Foot.y,SHY=BP.L_Upperarm.y;
    // size: shoulder tops sit just under the poles
    root.updateMatrixWorld(true);const poleW=V();B.cart.localToWorld(poleW.set(.33,.125,0));root.worldToLocal(poleW);const sp=poleW.y/(SHY+.035);
    const CURL0=[];for(const sd of['L','R'])for(const f of['Index','Mid','Ring','Pinky','Thumb'])for(let k=1;k<=3;k++){const n=sd+'_'+f+k;if(!BP[n])continue;
      const ax=(f==='Thumb'?V(0,1,0):V(0,0,1)).applyQuaternion(BQ[n].clone().invert()).normalize();CURL0.push([n,new T.Quaternion().setFromAxisAngle(ax,(sd==='L'?-1:1)*(f==='Thumb'?.5:k===1?1.2:1.3))])}
    for(const[sx,sz]of[[1,.68],[1,-.68],[-1,.68],[-1,-.68]]){const g=T.SkeletonUtils.clone(BG);g.scale.setScalar(sp);const pb=sx>0?'R':'L';
      g.position.set(sx*.33*sc+(sx>0?1:-1)*Math.abs(BP[pb+'_Upperarm'].x)*sp,0,sz*sc);root.add(g);const bb={};g.traverse(o=>{if(o.isBone)bb[o.name]=o;if(o.isMesh){o.frustumCulled=false;const mp=o.material.map;if(mp){mp.encoding=T.LinearEncoding;mp.needsUpdate=true}
        const mt=M('#ffffff',{map:mp,skinning:true,gradientMap:grad});mt.userData.outlineParameters={visible:false};U.mats.push(mt);o.material=mt;o.userData.keep=true}});
      const bind=[];for(const n in bb)bind.push([bb[n],bb[n].quaternion.clone(),bb[n].position.clone()]);
      PORT.push({g,bb,bind,sx,sz,pb,ph:(sz>0?0:Math.PI)+(sx>0?0:.4),curl:CURL0.map(([n,q])=>[bb[n],q])})}
    const _a=V(),_b=V(),_c=V(),_d=V(),_p=V(),_wq=new T.Quaternion(),_pq=new T.Quaternion(),_r=new T.Quaternion();
    const setWQ=(b,q)=>{b.parent.getWorldQuaternion(_pq).invert();b.quaternion.copy(_pq).multiply(q);b.updateMatrixWorld(true)};
    const aim=(b,c,t)=>{b.getWorldPosition(_a);c.getWorldPosition(_b);_c.subVectors(_b,_a).normalize();_d.subVectors(t,_a).normalize();_r.setFromUnitVectors(_c,_d);b.getWorldQuaternion(_wq);_r.multiply(_wq);setWQ(b,_r)};
    const rotW=(b,ax,an)=>{_r.setFromAxisAngle(ax,an);b.getWorldQuaternion(_wq);_r.multiply(_wq);setWQ(b,_r)};
    const two=(b1,b2,b3,L1,L2,t,pole)=>{b1.getWorldPosition(_a);const D=V().subVectors(t,_a);const d=clamp(D.length(),.02*L1,(L1+L2)*.999);D.normalize();const a=(L1*L1-L2*L2+d*d)/(2*d),h=Math.sqrt(Math.max(0,L1*L1-a*a));
      const P=pole.clone().addScaledVector(D,-pole.dot(D)).normalize();const kn=_a.clone().addScaledVector(D,a).addScaledVector(P,h),end=_a.clone().addScaledVector(D,d);aim(b1,b2,kn);aim(b2,b3,end)};
    U.porters=(dt,dist,wk,open)=>{const STR=.5,DU=.62,A=STR*DU/2;
      for(const P of PORT){const g=P.g,bb=P.bb;for(const[b,q,p]of P.bind){b.quaternion.copy(q);b.position.copy(p)}P.ph+=dist/(STR*sp)*TAU;const ph=P.ph;
        g.updateMatrixWorld(true);const gq=g.getWorldQuaternion(new T.Quaternion()),W=v=>g.localToWorld(v),up=V(0,1,0),rt=V(1,0,0).applyQuaternion(gq),fw=V(0,0,1).applyQuaternion(gq);
        // hips: bob over the standing leg, lean into the load, lean away from the pole a touch
        const mid=TAU*DU/2,cm=Math.cos(ph-mid)*wk;const hp=hip0.clone().add(V(.012*cm,-.025-open*.03+.008*Math.cos(2*(ph-mid))*wk,0));bb.Hip.parent.updateMatrixWorld(true);bb.Hip.position.copy(bb.Hip.parent.worldToLocal(W(hp)));
        rotW(bb.Hip,up,rad(5)*cm);for(const[n,k]of[['Waist',.3],['Spine01',.35],['Spine02',.35]]){rotW(bb[n],rt,rad(7+open*6)*k);rotW(bb[n],up,-rad(7)*cm*k);rotW(bb[n],fw,-P.sx*rad(4)*k)}
        rotW(bb.Head,rt,-rad(6));rotW(bb.Head,fw,P.sx*rad(5));
        // legs: planted feet in stance, lifted arcs in swing
        for(const[sd,off,sg]of[['L',0,1],['R',.5,-1]]){const u=(((ph/TAU+off)%1)+1)%1;let z=0,y=ANK,pt=0;
          if(wk>.01){if(u<DU){z=lerp(A,-A,u/DU)}else{const k=(u-DU)/(1-DU);z=lerp(-A,A,k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2);y+=Math.sin(k*Math.PI)*.05}z*=wk;y=ANK+(y-ANK)*wk}
          const L=LL(sd),pole=V(0,0,1).applyQuaternion(gq);two(bb[sd+'_Thigh'],bb[sd+'_Calf'],bb[sd+'_Foot'],L[0]*sp,L[1]*sp,W(V(sg*.065,y,z+.01)),pole);setWQ(bb[sd+'_Foot'],gq.clone().multiply(BQ[sd+'_Foot']))}
        // arms: the pole-side fist at the shoulder, the other reaching across to grip the pole in front
        const near=P.pb,far=near==='R'?'L':'R';for(const[sd,dz]of[[near,.045],[far,.2]]){const t=V();B.cart.localToWorld(t.set(P.sx*.33,.125,P.sz+dz*Math.sign(P.sz)*0+dz*(P.sz>0?1:1)));
          const L=LA(sd),el=V(sd==='L'?1:-1,-.6,-.5).applyQuaternion(gq).normalize();two(bb[sd+'_Upperarm'],bb[sd+'_Forearm'],bb[sd+'_Hand'],L[0]*sp,L[1]*sp,t.add(V(0,-.012*sc,0)),el)}
        for(const[b,q]of P.curl)b.quaternion.multiply(q);g.updateMatrixWorld(true)}}}
  function tick(dt,I){S.x=I.x;S.z=I.z;let df=I.yaw-S.yaw;df=Math.atan2(Math.sin(df),Math.cos(df));S.yaw+=df*Math.min(1,dt*(S.clip==='open'?1:3));S.vel=I.speed;
    let ot=0;if(S.clip==='open'){const t0=S.t;S.t+=dt*S.rate;ot=openAt(Math.min(S.t,OPEN));
      const n=12;for(let k=0;k<n;k++){const ts=SPAWN[0]+(SPAWN[1]-SPAWN[0])*k/n;if(t0<ts&&S.t>=ts)spawnOne()}if(S.t>=OPEN&&!S.hold)S.clip='idle'}
    let shake=0;if(S.clip==='plague'){const t0=S.t;S.t+=dt*S.rate;ot=plagueAt(Math.min(S.t,PLAG));if(S.t<1.15)shake=Math.min(1,S.t/.85);
      if(t0<.95&&S.t>=.95){startPlague();if(LAB.api&&LAB.api.shake)LAB.api.shake(.7);puff(B.beetle.localToWorld(V(0,.6,0)),14,.16*sc)}if(S.t>=PLAG&&!S.hold)S.clip='idle'}
    S.open+=(ot-S.open)*Math.min(1,dt*30);S.shk=(S.shk||0)+(shake-(S.shk||0))*Math.min(1,dt*10);
    S.wamt+=(clamp(S.vel/.25,0,1)-S.wamt)*Math.min(1,dt*5);const wk=S.wamt;S.ph+=(I.dist||0)/(.34*sc)*TAU;S.wheel+=(I.dist||0)/(.135*sc);
    for(const[b,q,p]of BIND){b.quaternion.copy(q);b.position.copy(p)}
    root.position.set(S.x,0,S.z);root.rotation.set(0,S.yaw,0);
    const now=performance.now()/1000;
    // cart: bobs with the bearers' steps, sways a little; wheels roll with the ground covered
    B.cart.position.y+=wk*.008*Math.abs(Math.sin(S.ph))+.002*Math.sin(now*1.3);B.cart.rotation.z=wk*.012*Math.sin(S.ph)+S.open*.01*Math.sin(now*30);
    for(let i=0;i<4;i++){const w=B['wh'+i];if(w)w.rotation.x=S.wheel}
    // the shell: wing cases lift at the back and swing out like temple doors; the scarab rears its head; the chamber glows
    const o=S.open;_q.setFromAxisAngle(Z,-.78*Math.min(o,1.5));_q2.setFromAxisAngle(X,1.0*o);B.shellL.quaternion.copy(_q.multiply(_q2));_q.setFromAxisAngle(Z,.78*o);_q2.setFromAxisAngle(X,1.0*o);B.shellR.quaternion.copy(_q.multiply(_q2));
    B.bhead.rotation.x=-.25*o+.03*Math.sin(now*2);B.beetle.position.y+=o*.012+(S.clip==='open'&&S.t<.25?.004*Math.sin(S.t*80):0);
    glow.material.opacity=Math.min(1,o*1.1+S.shk*.7)*(.8+.2*Math.sin(now*(9+S.shk*20)));glow.scale.setScalar((.3+S.shk*.25+Math.max(0,o-1)*.6)/sc);
    if(S.shk>.01){B.cart.position.x+=Math.sin(now*61)*.006*S.shk;B.cart.position.z+=Math.cos(now*53)*.004*S.shk;B.cart.rotation.z+=Math.sin(now*47)*.02*S.shk;B.beetle.rotation.y=Math.sin(now*39)*.04*S.shk}
    // bearers: march in step, poles on their shoulders; brace and lean away while the ark opens
    for(let i=0;i<4;i++){const ph=S.ph+(i%2?Math.PI:0)+(i>1?.3:0),h=B['b'+i+'hip'],s=B['b'+i+'sp'];if(!h)continue;
      h.position.y+=wk*.006*Math.abs(Math.cos(ph))-o*.012;s.rotation.x=.08*wk+o*.1;s.rotation.y=wk*.06*Math.sin(ph);
      for(const[sd,off]of[['L',0],['R',Math.PI]]){const t=B['b'+i+'th'+sd],k=B['b'+i+'kn'+sd];const a=Math.sin(ph+off);t.rotation.x=-a*.55*wk+o*.25;k.rotation.x=Math.max(0,Math.cos(ph+off))*.75*wk+o*.3}}
    src.updateMatrixWorld(true);if(U.porters)U.porters(dt,I.dist||0,wk,Math.min(1,S.open));tickSwarm(dt);tickPlague(dt);
    for(const m of U.mats)if(!m.userData.noflash)m.emissive.setHex(I.flash?0xffffff:0)}
  return{U,S,scene,get cur(){return{}},playG,tick,clips:{idle:{},open:{dur:OPEN}}}};
