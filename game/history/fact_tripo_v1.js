// ---------- imported Tripo model: its own mesh and skeleton, its walk clip, and our moves layered on top by aiming its arm bones (two-bone IK) ----------
FACT.tripo=function(){const G=window.TRIPO;const src=T.SkeletonUtils.clone(G.scene);const U={mats:[]};
  const root=new T.Group();scene.add(root);const fall=new T.Group();root.add(fall);fall.add(src);U.root=root;
  const B={};src.traverse(o=>{if(o.isBone)B[o.name]=o});
  // stand it on the ground at the game height and give it the game's cartoon shading (its texture kept)
  src.updateMatrixWorld(true);const box=new T.Box3();src.traverse(o=>{if(o.isMesh){o.geometry.computeBoundingBox();const b=o.geometry.boundingBox.clone().applyMatrix4(o.matrixWorld);box.union(b)}});
  const H=box.max.y-box.min.y,sc=(LAB.mh||1.05)/H;src.scale.multiplyScalar(sc);src.position.y=-box.min.y*sc;
  const soft=(()=>{const d=new Uint8Array([178,178,178,255,255,255,255,255]);const t=new T.DataTexture(d,2,1,T.RGBAFormat);t.minFilter=t.magFilter=T.NearestFilter;t.needsUpdate=true;return t})();
  src.traverse(o=>{if(o.isMesh){o.frustumCulled=false;const mp=o.material.map;if(mp){mp.encoding=T.LinearEncoding;mp.anisotropy=4;mp.needsUpdate=true}const mat=M('#ffffff',{map:mp,skinning:!!o.isSkinnedMesh,gradientMap:soft});mat.userData.outlineParameters={thickness:.009,color:[.17,.14,.25],alpha:1,visible:true};U.mats.push(mat);o.material=mat;o.userData.keep=true}});
  // game-style proportions, Fire Emblem-ish: a bigger head, bigger hands and feet, so the figure reads at a glance at game size
  const STY=LAB.style||{head:1.42,hand:1.3,foot:1.2};for(const[n,k]of[['Head',STY.head],['L_Hand',STY.hand],['R_Hand',STY.hand],['L_Foot',STY.foot],['R_Foot',STY.foot]])if(B[n])B[n].scale.setScalar(k);
  const BIND=[];src.traverse(o=>{if(o.isBone)BIND.push([o,o.quaternion.clone(),o.position.clone()])});
  // the walk clip carries the body forward (root motion) and then snaps it back each loop: take the forward travel out of the hip track so the cycle loops in place
  // (the game moves the unit itself), and drop the do-nothing two-key position and scale tracks
  let wclip=null;if(G.animations.length){const c0=G.animations[0];if(!G.__fixed){for(const t of c0.tracks){if(t.name==='Hip.position'){const n=t.times.length,t0=t.times[0],t1=t.times[n-1],v=t.values,f=v.slice(0,3),l=v.slice(v.length-3);
        for(let i=0;i<n;i++){const k=(t.times[i]-t0)/(t1-t0);for(let j=0;j<3;j++)v[i*3+j]-=(l[j]-f[j])*k}
        G.__travel=Math.hypot(l[0]-f[0],l[1]-f[1],l[2]-f[2]);G.__dur=t1-t0;
        const par=B.Hip.parent;par.updateMatrixWorld(true);const up=new T.Vector3(0,1,0).applyQuaternion(par.getWorldQuaternion(new T.Quaternion()).invert());let vj=0;for(let j=1;j<3;j++)if(Math.abs(up.getComponent(j))>Math.abs(up.getComponent(vj)))vj=j;
        const mean=[0,0,0];for(let i=0;i<n;i++)for(let j=0;j<3;j++)mean[j]+=v[i*3+j]/n;for(let i=0;i<n;i++)for(let j=0;j<3;j++)if(j!==vj)v[i*3+j]=mean[j]+(v[i*3+j]-mean[j])*.25}}G.__fixed=true}
    wclip=new T.AnimationClip('walk',c0.duration,c0.tracks.filter(t=>t.name.endsWith('.quaternion')||t.name==='Hip.position'))}
  const mixer=new T.AnimationMixer(src);const walk=wclip?mixer.clipAction(wclip):null;if(walk){walk.play();walk.setEffectiveWeight(0)}
  const S={x:0,z:0,yaw:0,vel:0,wamt:0,clip:'idle',t:0,rate:1,hold:false,prev:null,bl:0,blT:.15};
  // shoulders and arm length, measured from the model so our moves fit its proportions
  root.updateMatrixWorld(true);const V=()=>new T.Vector3();const sh={R:root.worldToLocal(B.R_Upperarm.getWorldPosition(V())),L:root.worldToLocal(B.L_Upperarm.getWorldPosition(V()))};
  const armL=B.R_Upperarm.getWorldPosition(V()).distanceTo(B.R_Forearm.getWorldPosition(V()))+B.R_Forearm.getWorldPosition(V()).distanceTo(B.R_Hand.getWorldPosition(V())),K=armL/.46;
  // the same whip moves the hand-built mummy uses; hand targets are written as the hand-built rig's, then mapped onto this body
  const OURSH=[.13,.795,0];
  const P=o=>Object.assign({hR:[-.2,.52,.2],hL:[.17,.6,.3],twist:0,lean:6,spin:0,fwd:0,lash:0,coil:0,lashR:0,coilR:0,rad:0,w:1},o);
  const mixP=(a,b,t)=>{const o={};for(const k in a){const x=a[k];let y=b[k]===undefined?x:b[k];if(k==='spin')y=y+Math.round(x-y);o[k]=Array.isArray(x)?x.map((v,i)=>lerp(v,y[i],t)):lerp(x,y,t)}return o};
  const E={io:t=>t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2,out:t=>1-Math.pow(1-t,3),lin:t=>t};
  const IDLE=P({hR:[-.17,.4,.08],hL:[.17,.4,.08],lean:4});
  const CL={
    idle:{dur:4,loop:true,fn:t=>{const s=Math.sin(t/4*TAU);return P({hR:[-.17,.4+s*.01,.08],hL:[.17,.4+s*.01,.08],lean:4+s*1.5,twist:Math.sin(t/4*Math.PI)*5})}},
    whip:{dur:1.1,keys:[[0,IDLE,'io'],[.12,P({lean:6,twist:20,hL:[.24,.86,0],coil:1}),'io'],[.3,P({lean:-4,twist:30,hL:[.22,1.0,-.1],coil:1,lash:.15}),'io'],
      [.46,P({fwd:.18,lean:20,twist:-26,hL:[.04,.64,.46],lash:1}),'out'],[.66,P({fwd:.12,lean:18,twist:-20,hL:[.06,.62,.42],lash:.9}),'io'],[.92,P({lash:.2}),'io'],[1.1,IDLE,'io']]},
    whipR:{dur:1.1,keys:[[0,IDLE,'io'],[.12,P({lean:8,twist:-24,hR:[-.3,.7,-.06],coilR:1}),'io'],[.3,P({lean:2,twist:-40,hR:[-.42,.78,-.14],coilR:1,lashR:.15}),'io'],
      [.46,P({fwd:.18,lean:18,twist:30,hR:[-.02,.62,.46],lashR:1}),'out'],[.66,P({fwd:.12,lean:16,twist:22,hR:[-.04,.6,.42],lashR:.9}),'io'],[.92,P({lashR:.2}),'io'],[1.1,IDLE,'io']]},
    twin:{dur:1.1,keys:[[0,IDLE,'io'],[.14,P({lean:4,hR:[-.24,.92,-.02],hL:[.24,.92,-.02],coil:1,coilR:1}),'io'],[.32,P({lean:-8,hR:[-.2,1.04,-.1],hL:[.2,1.04,-.1],coil:1,coilR:1,lash:.15,lashR:.15}),'io'],
      [.46,P({fwd:.2,lean:28,hR:[-.1,.56,.46],hL:[.1,.56,.46],lash:1,lashR:1}),'out'],[.68,P({fwd:.12,lean:24,hR:[-.1,.56,.42],hL:[.1,.56,.42],lash:.9,lashR:.9}),'io'],[.94,P({lash:.2,lashR:.2}),'io'],[1.1,IDLE,'io']]},
    spin:{dur:1.1,keys:[[0,IDLE,'io'],[.14,P({lean:16,twist:-36,hR:[-.3,.5,.1],hL:[.24,.6,.24]}),'io'],[.24,P({spin:.22,lean:2,hR:[-.52,.72,.04],hL:[.46,.74,0],rad:1,lash:.75,lashR:.75}),'lin'],
      [.38,P({spin:.66,lean:0,hR:[-.52,.74,0],hL:[.46,.76,-.02],rad:1,lash:.85,lashR:.85}),'lin'],[.5,P({fwd:.3,spin:1,lean:22,hR:[-.1,.58,.46],hL:[.1,.58,.46],lash:1,lashR:1}),'out'],
      [.76,P({fwd:.2,spin:1,lean:16,hR:[-.1,.56,.4],hL:[.1,.56,.4],lash:.6,lashR:.6}),'io'],[1.1,P(Object.assign({},IDLE,{spin:1})),'io']]},
    kneel:{dur:3.5,keys:[[0,IDLE,'io'],[3.5,IDLE,'io']]}};
  CL.down={dur:2.6,keys:[[0,IDLE,'io'],[2.6,IDLE,'io']]};CL.rise=CL.down;
  const sample=(n,t)=>{const c=CL[n];if(c.fn)return c.fn(t);const k=c.keys;if(t>=k[k.length-1][0])return k[k.length-1][1];for(let i=0;i<k.length-1;i++)if(t<k[i+1][0]){const f=(t-k[i][0])/(k[i+1][0]-k[i][0]);return mixP(k[i][1],k[i+1][1],E[k[i+1][2]](f))}return k[0][1]};
  let cur=IDLE;
  function playG(n,rate,off){if(!CL[n])n='idle';S.prev=cur;S.bl=S.blT;S.clip=n;S.rate=rate||1;S.t=off||0}
  // bone aiming: turn a bone (in world space) so its child points at a target, then store it back in the bone's own space
  const _q=new T.Quaternion(),_wq=new T.Quaternion(),_pq=new T.Quaternion(),_a=V(),_b=V(),_c=V(),_d=V(),_e=V(),_p=V();
  function aim(bone,child,tw){bone.getWorldPosition(_a);child.getWorldPosition(_b);_c.subVectors(_b,_a).normalize();_d.subVectors(tw,_a).normalize();_q.setFromUnitVectors(_c,_d);
    bone.getWorldQuaternion(_wq);_q.multiply(_wq);bone.parent.getWorldQuaternion(_pq).invert();bone.quaternion.copy(_pq.multiply(_q));bone.updateMatrixWorld(true)}
  function rotWorld(bone,axisW,ang){_q.setFromAxisAngle(axisW,ang);bone.getWorldQuaternion(_wq);_q.multiply(_wq);bone.parent.getWorldQuaternion(_pq).invert();bone.quaternion.copy(_pq.multiply(_q));bone.updateMatrixWorld(true)}
  function arm(side,tgtRoot,w){const up=B[side+'_Upperarm'],fo=B[side+'_Forearm'],hd=B[side+'_Hand'];if(w<=0)return;
    const Sx=up.getWorldPosition(V()),L1=Sx.distanceTo(fo.getWorldPosition(V())),L2=fo.getWorldPosition(V()).distanceTo(hd.getWorldPosition(V()));
    const Tw=root.localToWorld(tgtRoot.clone());hd.getWorldPosition(_e);Tw.lerp(_e,1-w);_d.subVectors(Tw,Sx);let d=clamp(_d.length(),.01,L1+L2-.002);_d.normalize();
    const a=(L1*L1-L2*L2+d*d)/(2*d),h=Math.sqrt(Math.max(0,L1*L1-a*a));_p.set(side==='R'?-1:1,-.4,-.7).transformDirection(root.matrixWorld);_p.addScaledVector(_d,-_p.dot(_d)).normalize();
    const El=Sx.clone().addScaledVector(_d,a).addScaledVector(_p,h);aim(up,fo,El);aim(fo,hd,Tw)}
  const UPW=new T.Vector3(0,1,0),RT=V();
  // whips torn from its wraps, one per hand
  const NW=24;function mkWhip(){const g=new T.BufferGeometry();g.setAttribute('position',new T.BufferAttribute(new Float32Array(NW*2*3),3));const ix=[];for(let i=0;i<NW-1;i++){const a=i*2;ix.push(a,a+1,a+2,a+1,a+3,a+2)}g.setIndex(ix);
    const mt=M('#e6dcc4',{side:T.DoubleSide});mt.userData=NOOUT;const w=new T.Mesh(g,mt);w.frustumCulled=false;w.userData.keep=true;scene.add(w);return{w,g,t:0}}
  const WH=[mkWhip(),mkWhip()],_H=V(),_Fw=V(),_Sd=V(),_P=V(),_Q=V(),_hp=V(),_Dw=V(),rootQ=new T.Quaternion();
  function whips(p,dt){_Fw.set(0,0,1).applyQuaternion(rootQ);B.Hip.getWorldPosition(_hp);
    for(let k=0;k<2;k++){const W=WH[k],ls=clamp(k?p.lashR:p.lash,0,1.2),co=clamp(k?p.coilR:p.coil,0,1),rd=clamp(p.rad||0,0,1);W.w.visible=ls>.03||co>.05;W.t+=dt*(8+co*10)*(k?-1:1);if(!W.w.visible)continue;
      B[k?'R_Hand':'L_Hand'].getWorldPosition(_H);_Dw.set(_H.x-_hp.x,0,_H.z-_hp.z);if(_Dw.lengthSq()<1e-6)_Dw.copy(_Fw);_Dw.normalize().lerp(_Fw,1-rd).normalize();_Sd.crossVectors(UPW,_Dw).normalize();
      const L=.15+ls*1.25,pa=W.g.attributes.position,wt=W.t,kk=Math.min(1,ls/.6);
      for(let i=0;i<NW;i++){const u=i/(NW-1),ca=wt+u*5,cr=.06+u*.14,wv=Math.sin(u*10-wt*1.3)*.07*u;const lx=_Dw.x*L*u+_Sd.x*wv,ly=Math.sin(u*Math.PI)*.12*(1-u*.5)-u*(_H.y-.45)*.9*(1-rd*.8),lz=_Dw.z*L*u+_Sd.z*wv;
        _P.set(_H.x+lerp(Math.cos(ca)*cr,lx,kk),_H.y+lerp(.04+u*.05,ly,kk),_H.z+lerp(Math.sin(ca)*cr,lz,kk));const w=.028*(1-u*.4);if(kk>.5)_Q.copy(_Sd).multiplyScalar(w);else _Q.set(0,w,0);
        pa.setXYZ(i*2,_P.x-_Q.x,_P.y-_Q.y,_P.z-_Q.z);pa.setXYZ(i*2+1,_P.x+_Q.x,_P.y+_Q.y,_P.z+_Q.z)}pa.needsUpdate=true;W.g.computeVertexNormals()}}
  const fr=(a,s)=>{const o=OURSH,b=s==='R'?sh.R:sh.L,sx=s==='R'?-1:1;return new T.Vector3(b.x+(a[0]-sx*o[0])*K,b.y+(a[1]-o[1])*K,b.z+(a[2]-o[2])*K)};
  function tick(dt,I){S.x=I.x;S.z=I.z;let df=I.yaw-S.yaw;df=Math.atan2(Math.sin(df),Math.cos(df));S.yaw+=df*Math.min(1,dt*(S.clip==='idle'?8:14));S.vel=I.speed;
    const c=CL[S.clip];S.t+=dt*S.rate;if(!c.loop&&S.t>=c.dur&&!S.hold)playG('idle');const c2=CL[S.clip],tt=c2.loop?S.t%c2.dur:Math.min(S.t,c2.dur);let p=sample(S.clip,tt);
    if(S.bl>0&&S.prev){S.bl-=dt;p=mixP(S.prev,p,1-Math.max(0,S.bl)/S.blT)}cur=p;
    S.wamt+=(clamp(S.vel/.6,0,1)-S.wamt)*Math.min(1,dt*6);const walking=S.clip==='idle'?S.wamt:0;
    root.position.set(S.x,0,S.z);root.rotation.set(0,S.yaw+(p.spin||0)*TAU,0);rootQ.setFromEuler(root.rotation);fall.position.set(0,0,p.fwd||0);
    for(const[b,q,ps]of BIND){b.quaternion.copy(q);b.position.copy(ps)}
    if(walk){walk.setEffectiveWeight(walking);const v0=(G.__travel||1)*B.Hip.parent.getWorldScale(_e).x/(G.__dur||1);walk.timeScale=clamp(S.vel/Math.max(.05,v0),.5,3);mixer.update(dt)}
    root.updateMatrixWorld(true);
    // our layer: lean and twist through the spine, then the arms aimed at their hand targets
    RT.set(1,0,0).applyQuaternion(rootQ);const wa=1-walking;
    rotWorld(B.Spine01,UPW,rad(p.twist||0)*.5*wa);rotWorld(B.Spine02,UPW,rad(p.twist||0)*.5*wa);rotWorld(B.Spine01,RT,rad(p.lean||0)*.6*wa);
    arm('R',fr(p.hR,'R'),wa);arm('L',fr(p.hL,'L'),wa);
    whips(p,dt);for(const m of U.mats)m.emissive.setHex(I.flash?0xffffff:0)}
  return{U,S,scene,get cur(){return cur},playG,tick,clips:CL}};
