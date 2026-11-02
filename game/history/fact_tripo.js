// ---------- imported Tripo model: its own mesh and skeleton, its walk clip, and our moves layered on top by aiming its arm bones (two-bone IK) ----------
FACT.tripo=function(){const G=window.TRIPO;const src=T.SkeletonUtils.clone(G.scene);const U={mats:[]};
  const root=new T.Group();scene.add(root);const fall=new T.Group();root.add(fall);fall.add(src);U.root=root;
  const B={};src.traverse(o=>{if(o.isBone)B[o.name]=o});
  // stand it on the ground at the game height and give it the game's cartoon shading (its texture kept)
  src.updateMatrixWorld(true);const box=new T.Box3();src.traverse(o=>{if(o.isMesh){o.geometry.computeBoundingBox();const b=o.geometry.boundingBox.clone().applyMatrix4(o.matrixWorld);box.union(b)}});
  // tuck in loose pieces that stick far out from the hips (a stiff bandage 'tail' on this model): pull them back to the body's edge
  if(LAB.tuck)src.traverse(o=>{if(!o.isMesh)return;const pa=o.geometry.attributes.position;o.geometry.computeBoundingBox();const bb=o.geometry.boundingBox,h=bb.max.y-bb.min.y;let cx=0,cz=0,n=0;
    for(let i=0;i<pa.count;i++){const y=(pa.getY(i)-bb.min.y)/h;if(y>.4&&y<.5){cx+=pa.getX(i);cz+=pa.getZ(i);n++}}cx/=n||1;cz/=n||1;
    for(let i=0;i<pa.count;i++){const y=(pa.getY(i)-bb.min.y)/h;if(y<LAB.tuck[0]||y>LAB.tuck[1])continue;const dx=pa.getX(i)-cx,dz=pa.getZ(i)-cz,r=Math.hypot(dx,dz),lim=LAB.tuck[2]*h;if(r>lim){pa.setX(i,cx+dx/r*lim);pa.setZ(i,cz+dz/r*lim)}}
    pa.needsUpdate=true;o.geometry.computeVertexNormals()});
  const H=box.max.y-box.min.y,sc=(LAB.mh||1.05)/H;src.scale.multiplyScalar(sc);src.position.y=-box.min.y*sc;
  const soft=(()=>{const d=new Uint8Array([200,200,200,255,228,228,228,255,255,255,255,255]);const t=new T.DataTexture(d,3,1,T.RGBAFormat);t.minFilter=t.magFilter=T.LinearFilter;t.needsUpdate=true;return t})();
  src.traverse(o=>{if(o.isMesh){o.frustumCulled=false;const mp=o.material.map;if(mp){mp.encoding=T.LinearEncoding;mp.anisotropy=4;mp.needsUpdate=true}const mat=M('#ffffff',{map:mp,skinning:!!o.isSkinnedMesh,gradientMap:soft});mat.userData.outlineParameters={visible:false};U.mats.push(mat);o.material=mat;o.userData.keep=true}});
  // game-style proportions, Fire Emblem-ish: a bigger head, bigger hands and feet, so the figure reads at a glance at game size
  const STY=LAB.style||{head:1.42,hand:1.3,foot:1.2};for(const[n,k]of[['Head',STY.head],['L_Hand',STY.hand],['R_Hand',STY.hand],['L_Foot',STY.foot],['R_Foot',STY.foot]])if(B[n])B[n].scale.setScalar(k);
  // ---- regalia from the reference art, built in 3D and pinned to its bones: teal-and-gold collar with a gem, pauldrons, gold belt and gem buckle,
  // a ragged teal kilt with a long gold-trimmed front panel, teal bracers and anklets banded in gold, and two long flowing ribbons ----
  const ADORN=[];if(LAB.adorn){const V=()=>new T.Vector3();root.updateMatrixWorld(true);
    const TL='#1d6a6e',TLD='#164f53',GD='#e8bd52',GM='#3ee0d6';const tm=c=>{const x=M(c);x.userData.outlineParameters={visible:false};U.mats.push(x);return x};const teal=tm(TL),tealD=tm(TLD),gold=tm(GD),gem=M(GM,{emissive:new T.Color('#0f6f6a')});gem.userData.outlineParameters={visible:false};
    // body measurements from the mesh itself, so the pieces fit whatever model is loaded
    const VS=[];src.traverse(o=>{if(o.isMesh){const pa=o.geometry.attributes.position;for(let i=0;i<pa.count;i+=2){VS.push(root.worldToLocal(new T.Vector3().fromBufferAttribute(pa,i).applyMatrix4(o.matrixWorld)))}}});
    const segR=(a,b,t0,t1,q)=>{const A=root.worldToLocal(a.getWorldPosition(V())),Bq=root.worldToLocal(b.getWorldPosition(V())),ab=V().subVectors(Bq,A),L2=ab.lengthSq(),ds=[];
      for(const v of VS){const t=V().subVectors(v,A).dot(ab)/L2;if(t<t0||t>t1)continue;const c=A.clone().addScaledVector(ab,t),d=v.distanceTo(c);if(d<Math.sqrt(L2)*.9)ds.push(d)}ds.sort((x,y)=>x-y);return ds.length?ds[Math.floor(ds.length*(q||.85))]:.03};
    const band=(y0,y1)=>{let rx=0,rz=0,cz=0,n=0;for(const v of VS)if(v.y>y0&&v.y<y1&&Math.abs(v.x)<.16){rx=Math.max(rx,Math.abs(v.x));rz=Math.max(rz,Math.abs(v.z));cz+=v.z;n++}return{rx,rz,cz:n?cz/n:0}};
    const M4=new T.Matrix4(),IQ=new T.Quaternion();
    const pin=(bone,obj,posRoot,quat)=>{const w=new T.Matrix4().compose(posRoot,quat||IQ,new T.Vector3(1,1,1));w.premultiply(root.matrixWorld);M4.copy(bone.matrixWorld).invert().multiply(w);M4.decompose(obj.position,obj.quaternion,obj.scale);bone.add(obj);ADORN.push(obj);obj.traverse(o=>{if(o.isMesh){o.frustumCulled=false;o.userData.keep=true}})};
    const at=b=>root.worldToLocal(b.getWorldPosition(V()));
    const neck=at(B.Head),chestY=at(B.Spine02).y,hip=at(B.Pelvis),waist=at(B.Spine01).clone();waist.y=lerp(hip.y,waist.y,.75);
    // collar: a flared teal yoke edged in gold, gold bars, and a gem pendant on the chest
    {const sb=band(neck.y-.1,neck.y-.05),r0=Math.max(.05,sb.rx*.62),g=new T.Group(),h=.05;
      const yoke=new T.Mesh(new T.CylinderGeometry(r0*.75,r0*1.25,h,24,1,true),teal);yoke.material.side=T.DoubleSide;g.add(yoke);
      for(const[yy,rr]of[[h/2,r0*.75],[-h/2,r0*1.25]]){const t=new T.Mesh(new T.TorusGeometry(rr,.006,5,24),gold);t.rotation.x=Math.PI/2;t.position.y=yy;g.add(t)}
      for(let i=0;i<9;i++){const a=(i/8-.5)*2.3,bar=new T.Mesh(new T.BoxGeometry(.008,h*.8,.004),gold);bar.position.set(Math.sin(a)*r0*1.02,0,Math.cos(a)*r0*1.02);bar.rotation.set(-.42*Math.cos(a),a,.42*Math.sin(a)*0);g.add(bar)}
      const pend=new T.Mesh(new T.OctahedronGeometry(.016),gem);pend.scale.set(.8,1.2,.5);pend.position.set(0,-h*.7,r0*1.28);g.add(pend);const pf=new T.Mesh(new T.OctahedronGeometry(.022),gold);pf.scale.set(.8,1.2,.3);pf.position.set(0,-h*.7,r0*1.24);g.add(pf);
      g.scale.z=Math.max(.7,sb.rz/sb.rx);pin(B.Spine02,g,V().set(0,neck.y-.05,sb.cz))}
    // pauldrons: teal shells with gold rims and a gold point, riding the upper arms
    for(const sd of['L','R']){const sx=sd==='L'?1:-1,up=B[sd+'_Upperarm'],r=segR(up,B[sd+'_Forearm'],0,.3)*1.35,g=new T.Group();
      const sh=new T.Mesh(new T.SphereGeometry(r,14,8,0,TAU,0,Math.PI*.55),teal);sh.scale.set(1,.8,1.1);g.add(sh);const rim=new T.Mesh(new T.TorusGeometry(r*.98,.006,4,18),gold);rim.rotation.x=Math.PI/2;rim.position.y=r*.12;g.add(rim);
      const pt=new T.Mesh(new T.ConeGeometry(r*.32,r*.7,4),gold);pt.position.set(0,r*.7,0);g.add(pt);const p0=at(up);pin(up,g,V().set(p0.x+sx*r*.25,p0.y+r*.25,p0.z),new T.Quaternion().setFromAxisAngle(V().set(0,0,1),-sx*.5))}
    // gold belt with a gem buckle
    {const wb=band(waist.y-.02,waist.y+.02),g=new T.Group();
      const bk=new T.Mesh(new T.BoxGeometry(.05,.04,.012),gold);bk.rotation.z=Math.PI/4;bk.position.set(0,0,wb.rz*1.02);g.add(bk);const bg=new T.Mesh(new T.OctahedronGeometry(.014),gem);bg.position.set(0,0,wb.rz*1.06);bg.scale.set(.8,1.1,.5);g.add(bg);pin(B.Pelvis,g,V().set(0,waist.y,wb.cz))}
    // kilt: a long front panel with gold border and gold chevrons, and ragged teal side and back panels that swing with the thighs
    {const wb=band(waist.y-.03,waist.y+.01),knee=at(B.L_Calf).y,len=(waist.y-knee)*1.02;
      const panel=(w,L,mat,trim,rag)=>{const g=new T.Group(),sh=new T.Shape();sh.moveTo(-w/2,0);sh.lineTo(w/2,0);sh.lineTo(w/2*.86,-L*(rag?.82:1));if(rag){for(let i=0;i<=4;i++){const x=w/2*.86-i*(w*.86/4);sh.lineTo(x,-L*(i%2?1:.86))}}else sh.lineTo(0,-L*1.08);sh.lineTo(-w/2*.86,-L*(rag?.82:1));sh.lineTo(-w/2,0);
        const m=new T.Mesh(new T.ShapeGeometry(sh),mat);m.material.side=T.DoubleSide;g.add(m);if(trim){for(const sx of[-1,1]){const tb=new T.Mesh(new T.BoxGeometry(.008,L*.95,.004),gold);tb.position.set(sx*w*.44,-L*.47,.003);tb.rotation.z=sx*.07;g.add(tb)}
          for(let k=0;k<2;k++){const ch=new T.Mesh(new T.OctahedronGeometry(w*.16),gold);ch.scale.set(1,1.3,.15);ch.position.set(0,-L*(.45+k*.28),.004);g.add(ch)}}return g};
      const fr=panel(Math.max(.07,wb.rx*.85),len,teal,true,false);pin(B.Pelvis,fr,V().set(0,waist.y-.01,wb.cz+wb.rz*1.06),new T.Quaternion().setFromAxisAngle(V().set(1,0,0),-.06));
      const bk=panel(Math.max(.08,wb.rx*1.1),len*.9,tealD,false,true);pin(B.Pelvis,bk,V().set(0,waist.y-.01,wb.cz-wb.rz*1.06),new T.Quaternion().setFromAxisAngle(V().set(0,1,0),Math.PI).multiply(new T.Quaternion().setFromAxisAngle(V().set(1,0,0),-.08)));
      for(const sd of['L','R']){const sx=sd==='L'?1:-1,th=B[sd+'_Thigh'];for(const[ang,mat]of[[.55,teal],[1.25,tealD]]){const pnl=panel(.075,len*.82,mat,mat===teal,true);
        pin(th,pnl,V().set(sx*Math.sin(ang)*wb.rx*1.08,waist.y-.02,wb.cz+Math.cos(ang)*wb.rz*1.08),new T.Quaternion().setFromAxisAngle(V().set(0,1,0),sx*ang).multiply(new T.Quaternion().setFromAxisAngle(V().set(1,0,0),-.1)))}}}
    // bracers and anklets: teal cuffs with gold bands
    const cuff=(b0,b1,t,len)=>{const r=Math.min(segR(b0,b1,t-.1,t+.1,.8)*1.25,at(b0).distanceTo(at(b1))*.3),g=new T.Group();const c=new T.Mesh(new T.CylinderGeometry(r,r*1.04,len,14,1,true),teal);c.material.side=T.DoubleSide;g.add(c);
      for(const yy of[-len/2,len/2,0]){const tr=new T.Mesh(new T.TorusGeometry(r*1.03,yy?.006:.004,4,16),gold);tr.rotation.x=Math.PI/2;tr.position.y=yy;g.add(tr)}
      const A=at(b0),Bq=at(b1),ctr=A.clone().lerp(Bq,t),q=new T.Quaternion().setFromUnitVectors(V().set(0,1,0),V().subVectors(Bq,A).normalize());pin(b0,g,ctr,q)};
    for(const sd of['L','R'])cuff(B[sd+'_Forearm'],B[sd+'_Hand'],.72,.07);
  }
  const ribbons=(LAB.adorn||LAB.ribbons)?[makeCloth(2,12,'#efe4cc',.07,.62),makeCloth(2,11,'#e6d9bd',.065,.56)]:[];
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
  const LEG=B.R_Thigh.getWorldPosition(V()).distanceTo(B.R_Calf.getWorldPosition(V()))+B.R_Calf.getWorldPosition(V()).distanceTo(B.R_Foot.getWorldPosition(V()));
  const foot0={R:root.worldToLocal(B.R_Foot.getWorldPosition(V())),L:root.worldToLocal(B.L_Foot.getWorldPosition(V()))};
  const rq0=root.getWorldQuaternion(new T.Quaternion()).invert(),footRel={R:rq0.clone().multiply(B.R_Foot.getWorldQuaternion(new T.Quaternion())),L:rq0.clone().multiply(B.L_Foot.getWorldQuaternion(new T.Quaternion()))};
  const STRIDE=LEG*1.45,DUTY=.58;
  const armL=B.R_Upperarm.getWorldPosition(V()).distanceTo(B.R_Forearm.getWorldPosition(V()))+B.R_Forearm.getWorldPosition(V()).distanceTo(B.R_Hand.getWorldPosition(V())),K=armL/.46;
  // the same whip moves the hand-built mummy uses; hand targets are written as the hand-built rig's, then mapped onto this body
  const OURSH=[.13,.795,0];
  const P=o=>Object.assign({hR:[-.2,.52,.2],hL:[.17,.6,.3],twist:0,lean:6,spin:0,fwd:0,sway:0,crouch:0,headT:0,lash:0,coil:0,lashR:0,coilR:0,rad:0,w:1},o);
  const mixP=(a,b,t)=>{const o={};for(const k in a){const x=a[k];let y=b[k]===undefined?x:b[k];if(k==='spin')y=y+Math.round(x-y);o[k]=Array.isArray(x)?x.map((v,i)=>lerp(v,y[i],t)):lerp(x,y,t)}return o};
  const E={io:t=>t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2,out:t=>1-Math.pow(1-t,3),lin:t=>t,in:t=>t*t*t};
  const IDLE=P({hR:[-.22,.44,.12],hL:[.22,.46,.14],lean:6,crouch:.03});
  const CL={
    // a warrior's ready stance: weight low and balanced, hands loose and open at the sides, a slow breath and a weight shift
    idle:{dur:3.6,loop:true,fn:t=>{const u=t/3.6*TAU,s=Math.sin(u),s2=Math.sin(u*.5);return P({hR:[-.22,.44+s*.012,.12],hL:[.22,.46+s*.012,.14],lean:6+s*1.5,crouch:.03,twist:s2*6,sway:s2*.35,headT:s2*4})}},
    // back-arch sling: rear far back with both wraps coiled overhead, then whip the whole body forward and crack both down
    arch:{dur:1.15,keys:[[0,IDLE,'io'],[.12,P({lean:-8,crouch:.08,hR:[-.2,.8,0],hL:[.2,.8,0],coil:.6,coilR:.6,headT:-10}),'io'],
      [.34,P({lean:-48,crouch:.06,hR:[-.2,1.06,-.24],hL:[.2,1.06,-.24],coil:1,coilR:1,lash:.1,lashR:.1,headT:-20}),'out'],
      [.55,P({fwd:.32,lean:46,crouch:.14,hR:[-.1,.46,.5],hL:[.1,.46,.5],lash:1,lashR:1,headT:10}),'in'],
      [.76,P({fwd:.24,lean:38,crouch:.12,hR:[-.1,.44,.46],hL:[.1,.44,.46],lash:.8,lashR:.8}),'out'],[1.15,IDLE,'io']]},
    // frenzy: lurching side to side, three frantic swings, the last one landing with the right wrap
    frenzy:{dur:1.05,keys:[[0,IDLE,'io'],[.1,P({lean:20,crouch:.1,sway:-1,twist:-34,hR:[-.34,.86,-.06],hL:[.2,.5,.3],headT:-14}),'out'],
      [.2,P({fwd:.1,lean:34,crouch:.12,sway:1,twist:30,hR:[.12,.5,.44],hL:[.3,.8,-.06],lashR:.6,headT:14}),'out'],
      [.3,P({fwd:.16,lean:24,crouch:.1,sway:-1,twist:-30,hR:[-.3,.8,-.04],hL:[-.1,.5,.44],lash:.6,lashR:.2,headT:-14}),'out'],
      [.5,P({fwd:.3,lean:40,crouch:.14,sway:.6,twist:34,hR:[.08,.5,.48],hL:[.32,.7,0],lashR:1,lash:.2,headT:10}),'out'],
      [.74,P({fwd:.22,lean:30,crouch:.12,twist:22,hR:[.06,.5,.44],hL:[.28,.62,.08],lashR:.6}),'io'],[1.05,IDLE,'io']]},
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
  function leg(side,tgtRoot){const th=B[side+'_Thigh'],ca=B[side+'_Calf'],ft=B[side+'_Foot'];const Sx=th.getWorldPosition(V()),L1=Sx.distanceTo(ca.getWorldPosition(V())),L2=ca.getWorldPosition(V()).distanceTo(ft.getWorldPosition(V()));
    const Tw=root.localToWorld(tgtRoot.clone());_d.subVectors(Tw,Sx);let d=clamp(_d.length(),.01,L1+L2-.001);_d.normalize();const a=(L1*L1-L2*L2+d*d)/(2*d),h=Math.sqrt(Math.max(0,L1*L1-a*a));
    _p.set(side==='R'?-.15:.15,0,1).transformDirection(root.matrixWorld);_p.addScaledVector(_d,-_p.dot(_d)).normalize();const Kn=Sx.clone().addScaledVector(_d,a).addScaledVector(_p,h);aim(th,ca,Kn);aim(ca,ft,Tw);
    // keep the foot flat to the ground (as it was at bind), with a little toe-up while it swings
    _q.copy(rootQ).multiply(footRel[side]);ft.parent.getWorldQuaternion(_pq).invert();ft.quaternion.copy(_pq.multiply(_q));ft.updateMatrixWorld(true)}
  function moveHip(dW){const par=B.Hip.parent;par.getWorldQuaternion(_pq).invert();const sc2=par.getWorldScale(_e).x;B.Hip.position.add(dW.clone().applyQuaternion(_pq).divideScalar(sc2))}
  function turnHip(ang){rotWorld(B.Hip,UPW,ang)}
  const UPW=new T.Vector3(0,1,0),RT=V();let wph=0;
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
    // our own gait: a low gliding prowl; feet stay planted on the ground in stance and lift through the swing, the pelvis bobs, sways and turns into each step
    wph+=(I.dist||0)/STRIDE*TAU;const ph=wph,wk=walking,cph=Math.cos(ph),sph=Math.sin(ph);
    root.updateMatrixWorld(true);const FW=V().set(0,0,1).applyQuaternion(rootQ),SDW=V().set(1,0,0).applyQuaternion(rootQ);
    // the scurry: low and pitched forward, quick short steps, the body lurching hard side to side
    const crouch=LEG*(.035+(p.crouch||0)+.03*wk),bob=LEG*(.02+.02*Math.cos(ph*2))*wk;moveHip(V().set(0,-(crouch+bob),0).addScaledVector(SDW,(-sph*.022*wk+(p.sway||0)*.05)*LEG).addScaledVector(FW,LEG*.02*wk));root.updateMatrixWorld(true);
    turnHip(cph*rad(10)*wk);const leanT=(p.lean||0)+7*wk;rotWorld(B.Hip,RT.set(1,0,0).applyQuaternion(rootQ),rad(leanT)*.22);
    root.updateMatrixWorld(true);
    // our layer: lean and twist through the spine, then the arms aimed at their hand targets
    RT.set(1,0,0).applyQuaternion(rootQ);const wa=1-walking;
    for(const sd of['R','L']){const u=(((ph/TAU+(sd==='L'?.5:0))%1)+1)%1,A=STRIDE*DUTY/2;let z,y=0;if(u<DUTY)z=lerp(A,-A,u/DUTY);else{const k=(u-DUTY)/(1-DUTY);z=lerp(-A,A,E.io(k));y=Math.sin(k*Math.PI)*LEG*.15}
      leg(sd,V().copy(foot0[sd]).add(V().set(0,y*wk,z*wk)))}
    const tw=(p.twist||0)-cph*11*wk;rotWorld(B.Spine01,UPW,rad(tw)*.5);rotWorld(B.Spine02,UPW,rad(tw)*.5);RT.set(1,0,0).applyQuaternion(rootQ);rotWorld(B.Spine01,RT,rad(leanT)*.42);rotWorld(B.Spine02,RT,rad(leanT)*.36);
    if(B.Head){const ht=(p.headT||0);rotWorld(B.Head,V().set(0,0,1).applyQuaternion(rootQ),rad(ht)*.6);rotWorld(B.Head,RT,-rad(leanT)*.3)}
    // arms: our pose, swinging opposite the legs while walking
    // walking: a confident stride with the arms swinging long and loose against the legs
    const fl=wk;const hr=[lerp(p.hR[0],-.21,fl),lerp(p.hR[1],.46+Math.max(0,-cph)*.05,fl),lerp(p.hR[2],.1-cph*.2,fl)],hl=[lerp(p.hL[0],.21,fl),lerp(p.hL[1],.46+Math.max(0,cph)*.05,fl),lerp(p.hL[2],.1+cph*.2,fl)];
    arm('R',fr(hr,'R'),1);arm('L',fr(hl,'L'),1);
    whips(p,dt);
    if(ribbons.length){const sp=B.Spine02;const body=[{a:B.Spine01.getWorldPosition(V()),b:B.Head.getWorldPosition(V()),r:LEG*.22},{a:B.Hip.getWorldPosition(V()),r:LEG*.25}];
      const an=(x)=>{const w=V().set(x,0,0);return root.localToWorld(root.worldToLocal(sp.getWorldPosition(V())).add(V().set(x,.03,-.06)))};
      stepCloth(ribbons[0],dt,[an(.05),an(.09)],body,null);stepCloth(ribbons[1],dt,[an(-.09),an(-.05)],body,null)}
    for(const m of U.mats)m.emissive.setHex(I.flash?0xffffff:0)}
  return{U,S,scene,get cur(){return cur},playG,tick,clips:CL}};
