F='tidebreak.html';s=open(F).read()
a=s.index("FACT.combo=function(){");e=s.index("FACT.sphinx=",a) if s.find("FACT.sphinx=",a)>0 else a+40000
seg=s[a:e]
def rep(x,y):
    global seg;assert seg.count(x)==1,x[:70];seg=seg.replace(x,y)
# trident for the queen (upgraded form); the basic form keeps the sais
rep("sai('L');sai('R');U.spearHead=U.saiR.userData.tip;",r"""sai('L');sai('R');U.spearHead=U.saiR.userData.tip;
  const QN=FACT.__nb!==1;let TRI=null;
  if(QN){U.saiL.visible=false;U.saiR.visible=false;const steel=M('#d9dde6'),shaftM=M('#3a2a20');for(const x of[steel,shaftM]){x.userData.outlineParameters={visible:false};U.mats.push(x)}
    const sp=new T.Group();const sh=new T.Mesh(new T.CylinderGeometry(.009,.009,.92,6),shaftM);sh.position.y=.1;sp.add(sh);
    const butt=new T.Mesh(new T.ConeGeometry(.014,.045,6),gold);butt.rotation.x=Math.PI;butt.position.y=-.38;sp.add(butt);
    for(const y of[-.03,.17]){const w=new T.Mesh(new T.CylinderGeometry(.013,.013,.026,8),gold);w.position.y=y;sp.add(w)}
    const hd=new T.Group();hd.position.y=.56;sp.add(hd);const col=new T.Mesh(new T.CylinderGeometry(.018,.014,.045,8),gold);hd.add(col);
    const ring=new T.Mesh(new T.TorusGeometry(.036,.008,6,16),gold);ring.position.y=.055;hd.add(ring);const gm=new T.Mesh(new T.OctahedronGeometry(.012),gemM);gm.position.set(0,.03,.016);hd.add(gm);
    const bl=new T.Mesh(new T.ConeGeometry(.02,.16,4),steel);bl.scale.z=.35;bl.position.y=.14;hd.add(bl);
    for(const sx of[-1,1]){const pts=[V(sx*.027,.045,0),V(sx*.068,.075,0),V(sx*.064,.13,0),V(sx*.041,.175,0)];hd.add(new T.Mesh(new T.TubeGeometry(new T.CatmullRomCurve3(pts),10,.007,5,false),steel));const tc=new T.Mesh(new T.ConeGeometry(.008,.028,5),steel);tc.position.set(sx*.039,.186,0);hd.add(tc)}
    const tip=new T.Group();tip.position.y=.22;hd.add(tip);const mid=new T.Group();mid.position.y=-.12;hd.add(mid);
    sp.scale.setScalar(sc);SCN.add(sp);TRI=sp;U.trident=sp;U.saiR.userData.tip=tip;U.saiR.userData.mid=mid;U.saiL.userData.tip=tip;U.saiL.userData.mid=mid;U.spearHead=tip}""")
rep("const ST={p:[0,-.16,0],","const ST={sp:[.25,.45,.85],lh:0,wh:0,wk:0,p:[0,-.16,0],")
# the queen's spear combination, ported from her old spear: pirouette, wheel-and-thrust, leap-and-slam
rep("  const HITS=",r"""  const QS={hL:[.1,.1,.2],hR:[-.14,.04,.06],sp:[.28,.42,.86],lh:1,bR:[.28,.42,.86]};
  const KQ=(t,o,lf)=>[t,Object.assign(JSON.parse(JSON.stringify(ST)),QS,o||{}),lf||{}];
  const QCOMBO=[
    KQ(0),
    KQ(.12,{p:[0,-.22,-.01],pitch:6,tw:26,headY:30,hR:[-.2,.02,-.04],sp:[-.7,.15,-.6],bR:[-.7,.15,-.6],lh:0,hL:[.14,.06,.14]}),                       // load the pirouette
    KQ(.22,{p:[.02,-.1,.04],yaw:Y0-90,pitch:2,tw:-10,hR:[-.32,.18,.04],sp:[-1,.06,.25],bR:[-1,.06,.25],lh:0,hL:[.26,.16,.05],headY:40,trR:1,airR:1,bfR:[-.14,-.32,-.05],ptR:.6},{fyL:-100}),
    KQ(.34,{p:[.03,-.09,.06],yaw:Y0-230,tw:-14,hR:[-.33,.18,.04],sp:[-1,.04,.2],bR:[-1,.04,.2],lh:0,hL:[.27,.17,.04],headY:-20,trR:1,airR:1,bfR:[-.14,-.33,-.06],ptR:.6},{fyL:-235}),
    KQ(.47,{p:[.03,-.15,.14],yaw:Y0-360,pitch:14,tw:10,bend:8,hR:[-.1,.14,.28],sp:[.35,-.02,1],bR:[.35,-.02,1],lh:.5,hL:[.12,.1,.22],headY:14,trR:1,airR:0,ptR:0},{fyL:-370,fR:[-.12,ANK,.18],fyR:-420,lfR:.05}),   // strike as she comes round
    // wheel: the spear spins twice like a wheel before her
    KQ(.58,{p:[.02,-.13,.16],yaw:Y0-360,pitch:4,tw:0,hR:[-.02,.18,.22],lh:0,hL:[.16,.08,.14],wk:1,wh:0,trR:1}),
    KQ(.84,{p:[.02,-.12,.16],yaw:Y0-360,pitch:4,tw:0,hR:[-.02,.18,.22],lh:0,hL:[.16,.08,.14],wk:1,wh:4*Math.PI,trR:1}),
    // thrust: lunge through, both hands driving the trident
    KQ(.98,{p:[.02,-.2,.42],yaw:Y0-350,pitch:22,tw:-8,bend:10,hR:[-.06,.14,.36],sp:[.04,-.05,1],bR:[.04,-.05,1],lh:.85,hL:[.06,.13,.5],headP:-14,headY:6,trR:1,wk:0},{fL:[.1,ANK,.6],fyL:-366,lfL:.06}),
    KQ(1.1,{p:[.02,-.26,.44],yaw:Y0-358,pitch:26,tw:10,bend:16,hR:[-.14,.0,.1],sp:[.1,-.35,-1],bR:[.1,-.35,-1],lh:0,hL:[.16,.0,.16],headP:-8,trR:0}),   // crouch, spear swept low behind
    // leap, spear overhead, and slam down on landing
    KQ(1.24,{p:[.02,.12,.58],yaw:Y0-360,pitch:-8,tw:0,bend:-6,hR:[-.06,.36,.02],sp:[0,.85,-.5],bR:[0,.85,-.5],lh:.8,hL:[-.02,.3,.1],headP:-18,airL:1,airR:1,bfL:[.09,-.32,.1],bfR:[-.09,-.36,-.06],ptL:.6,ptR:.6}),
    KQ(1.4,{p:[.02,.06,.68],yaw:Y0-360,pitch:4,hR:[-.04,.32,.12],sp:[0,.75,.6],bR:[0,.75,.6],lh:.8,hL:[.0,.32,.22],headP:-12,airL:1,airR:1,bfL:[.1,-.34,.14],bfR:[-.08,-.38,-.04],ptL:.5,ptR:.5,trR:1}),
    KQ(1.5,{p:[.02,-.24,.74],yaw:Y0-360,pitch:32,tw:4,bend:16,hR:[-.06,-.06,.38],sp:[0,-.72,.7],bR:[0,-.72,.7],lh:1,headP:-6,airL:0,airR:0,ptL:0,ptR:0,trR:1},{fL:[.1,ANK,.82],fyL:-366,lfL:.04,fR:[-.12,ANK,.58],fyR:-418,lfR:.04}),
    KQ(1.72,{p:[.02,-.2,.74],yaw:Y0-360,pitch:24,bend:12,hR:[-.06,-.04,.36],sp:[0,-.6,.8],bR:[0,-.6,.8],lh:1,trR:0}),
    KQ(1.92,{p:[.01,-.12,.4],yaw:Y0-360,pitch:10,ptL:.4,ptR:.4},{fL:[.09,ANK,.47],fyL:-372,fR:[-.12,ANK,.25],fyR:-410,lfL:.06,lfR:.06}),
    KQ(2.2,{p:[0,-.16,0],yaw:Y0-360},{fL:[.085,ANK,.13],fyL:-372,fR:[-.13,ANK,-.12],fyR:-422,lfL:.05,lfR:.05})];
  {let fL=ST.fL,fR=ST.fR,yL=ST.fyL,yR=ST.fyR;for(const k of QCOMBO){const m=k[2];if(m.fL)fL=m.fL;if(m.fR)fR=m.fR;if(m.fyL!=null)yL=m.fyL;if(m.fyR!=null)yR=m.fyR;k[1].fL=fL;k[1].fR=fR;k[1].fyL=yL;k[1].fyR=yR;k[1].lfL=m.lfL||0;k[1].lfR=m.lfR||0}}
  const QHITS=[[.47,1],[.98,1],[1.5,1.4]];
  const HITS=""")
rep("combo:{dur:2.2,fn:t=>sampleKeys(COMBO,t),hits:HITS}};","combo:{dur:2.2,fn:t=>sampleKeys(QN?QCOMBO:COMBO,t),hits:QN?QHITS:HITS}};")
rep("o.hL=[.1,.12+s*.006,.19];o.hR=[-.13,.19+s*.006,.07];return o}},","if(QN){Object.assign(o,JSON.parse(JSON.stringify(QS)));o.hR=[-.14,.04+s*.006,.06];o.hL=[.1,.1+s*.006,.2]}else{o.hL=[.1,.12+s*.006,.19];o.hR=[-.13,.19+s*.006,.07]}return o}},")
rep("o.trL=0;o.trR=0;return o}","o.trL=0;o.trR=0;if(QN){o.hR=[-.15,.03+Math.max(0,c)*.03,.02+c*.05];o.sp=[.12,.3,1];o.bR=[.12,.3,1];o.lh=0}return o}")
# spear pose: wheel spin and the left hand on the shaft
rep("if(wk>0)p=mixP(p,walkPose(wph,S.bank),Math.min(1,wk*1.4));",
    "if(wk>0)p=mixP(p,walkPose(wph,S.bank),Math.min(1,wk*1.4));\n    if(QN){let d=V(...p.sp);if(p.wk>0){d.lerp(V(Math.cos(p.wh+Math.PI/2),Math.sin(p.wh+Math.PI/2),.15),clamp(p.wk,0,1))}d.normalize();p.sp=d.toArray();p.bR=p.sp;const lh=clamp(p.lh||0,0,1);if(lh>0)p.hL=p.hL.map((v,i)=>v+(p.hR[i]+p.sp[i]*.22-v)*lh)}")
rep("for(const[b,q]of CURL)b.quaternion.multiply(q);",
    "for(const[b,q]of CURL)b.quaternion.multiply(q);\n    if(TRI){src.updateMatrixWorld(true);const hw=clamp(((p.hwL||0)+(p.hwR||0))/2,0,1),gp=U.saiR.getWorldPosition(V());let dW=V(...p.sp).normalize().applyQuaternion(rootQ.clone().multiply(chestQ));\n      if(hw>.01){const gl=U.saiL.getWorldPosition(V());gp.lerp(gl,.5*hw);dW.lerp(V(0,-1,0),hw).normalize();gp.y+=hw*.2*sc}TRI.position.copy(gp);TRI.quaternion.setFromUnitVectors(V(0,1,0),dW);TRI.updateMatrixWorld(true)}")
s=s[:a]+seg+s[e:]
open(F,'w').write(s);print('queen ok')
s=open(F).read()
a=s.index("FACT.sphinx=function(){");k="const B={};src.traverse(o=>{if(o.isBone)B[o.name]=o});";i=s.index(k,a)
assert i-a<3000
s=s[:i+len(k)]+"if(FACT.__nw===1)for(const n of['wL1','wR1'])if(B[n])B[n].scale.setScalar(.001);"+s[i+len(k):]
x="FACT.combob=function(){";assert s.count(x)==1
s=s.replace(x,"FACT.sphinxb=function(){FACT.__nw=1;try{return FACT.sphinx()}finally{FACT.__nw=0}};\n"+x)
x="TYPES.g0_3b=TYPES.g0_3;";assert s.count(x)==1
s=s.replace(x,"TYPES.g0_3b=Object.assign({},TYPES.g0_3,{f:'sphinxb',atk:TYPES.g0_3.atk.filter(a=>a[0]!=='buffet')});")
open(F,'w').write(s);print('sphinx wings ok')
s=open(F).read()
# Celtic Archer: basic and Archer Queen models
x="',archer:'";assert s.count(x)==1
s=s.replace(x,"',archerb:'"+__import__('base64').b64encode(open('glb/archerb_g.glb','rb').read()).decode()+"',archer:'")
x="const G0=window.MODELS&&window.MODELS.archer||window.TRIPO;";assert s.count(x)==1
s=s.replace(x,"const G0=(FACT.__ab===1&&window.MODELS&&window.MODELS.archerb)||window.MODELS&&window.MODELS.archer||window.TRIPO;")
x="FACT.sphinxb=function(){";s=s.replace(x,"FACT.archerb=function(){FACT.__ab=1;try{return FACT.archer()}finally{FACT.__ab=0}};\n"+x)
x="TYPES.carcherb=TYPES.carcher;";assert s.count(x)==1
s=s.replace(x,"TYPES.carcherb=Object.assign({},TYPES.carcher,{f:'archerb'});")
s=s.replace("U.carcher={name:'Celtic Archer',","U.carcher={name:'Archer Queen',")
s=s.replace("U.carcherb=Object.assign({},U.carcher,{full:'carcher',basic:true,special:null});","U.carcherb=Object.assign({},U.carcher,{name:'Celtic Archer',full:'carcher',basic:true,special:null});")
open(F,'w').write(s);print('archer pair ok')
