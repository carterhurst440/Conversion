L=open('cer/sphinx_game.js').read().split('\n')
def sub(i,a,b):
  assert a in L[i-1],(i,a);L[i-1]=L[i-1].replace(a,b)
sub(1,"FACT.sphinx=function(){const SCN=scene;const LAB=GLAB('sphinx');const G=window.MODELS.sphinx;","// ---------- Cerberus: three hound heads that look about on their own and bite in a rolling volley, a living serpent for a tail, a heavy hound's prowl ----------\nFACT.cer=function(){const SCN=scene;const LAB=GLAB('cer');const CB=FACT.__cb===1;const G=window.MODELS[CB?'cerb':'cer']||window.MODELS.cer;")
sub(3,"if(FACT.__nw===1)for(const n of['wL1','wR1'])if(B[n])B[n].scale.setScalar(.001);","")
sub(5,"const sc=(LAB.mh||1.2)/","const sc=(LAB.mh||1.2)*(CB?.87:1)/")
sub(6,"[138,138,138,255,206,206,206,255,255,255,255,255]","[170,170,170,255,225,225,225,255,255,255,255,255]")
sub(7,"const mat=M('#ffffff',{vertexColors:true,skinning:true,gradientMap:grad,side:T.DoubleSide});","const mp=o.material.map;if(mp){mp.encoding=T.LinearEncoding;mp.anisotropy=4;mp.needsUpdate=true}const mat=M('#ffffff',{map:mp,skinning:true,gradientMap:grad,side:T.DoubleSide});")
sub(13,"const pelvis0=","for(const[a,b]of[['FL','FR'],['HL','HR']]){const z=(INFO[a].rest.z+INFO[b].rest.z)/2;INFO[a].rest.z=INFO[b].rest.z=z}\n  const pelvis0=")
for i in range(14,19):L[i-1]=''
L[14]="  const WING={};"
sub(21,"spread:0,flap:0,","spread:0,flap:0,bL:0,bM:0,bR:0,sn:0,hup:0,")
sub(26,"tail:.25,spread:.02+.02*Math.sin(t*TAU/4)})},","tail:.25})},")
NEW=r"""    // tribite: the three heads strike one after another (right, middle, left), each rearing back before it snaps forward
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
    howl:{dur:1.6,ev:Array.from({length:12},(_,i)=>[.42+i*.07,'pillar']),keys:[[0,IDLE,'io'],[.3,P({hup:1,pitch:10,h:.02,HL:[0,0,.02],HR:[0,0,.02],tail:.8}),'out'],[1.2,P({hup:1,pitch:11,h:.02,HL:[0,0,.02],HR:[0,0,.02],tail:.9}),'io'],[1.6,IDLE,'io']]},"""
L[44]=NEW;L[45]='';L[46]=''
sub(51,"for(const n of['maul','swipe','swipeR','pounce','buffet'])","for(const n of['maul','swipe','swipeR','pounce'])")
i=52
while not L[i-1].lstrip().startswith('const sample='):L[i-1]='';i+=1
sub(69,"'spread','flap'],","'spread','flap','bL','bM','bR','sn','hup'],")
sub(69,"spread:800,flap:1500}","spread:800,flap:1500,bL:1900,bM:1900,bR:1900,sn:900,hup:500}")
sub(69,"ZT={","ZT={bL:.55,bM:.55,bR:.55,sn:.5,")
HEADS=r"""    const yr=dt>0?df/dt:0;const now=performance.now()/1000;
    // three heads: each keeps its own gaze (the outer two watch the flanks), snarls, and lunges on its own beat
    for(const[k,i,out]of[['L',0,-1],['M',1,0],['R',2,1]]){const nk=B['nk'+k],hd=B['hd'+k];if(!nk)continue;const b=s['b'+k],look=Math.sin(now*(.55+i*.17)+i*2.1)*.22+out*.12,sn=Math.sin(now*23+i*5)*.02*(1-wk);
      loc(nk,rad(s.pitch)*.45+rad(s.headP)*.3+rad(s.arch)*-.3+b*.55-s.hup*.55,look*.45-rad(s.twist)*.3+clamp(yr*.03,-.2,.2),out*b*.08);
      loc(hd,rad(s.pitch)*.3+rad(s.headP)*.5-b*.22-s.hup*.5+sn+Math.sin(now*1.3+i)*.04,look*.55+clamp(yr*.03,-.2,.2),-rad(s.roll)*.5+(s.hup?Math.sin(now*9+i)*.06*s.hup:0))}"""
assert L[151].lstrip().startswith('const yr=dt>0?df/dt:0;loc(B.neck');L[151]=HEADS
ln=[j for j,x in enumerate(L) if 'performance.now()/1000;' in x and 'HIST.unshift' in x][0]
L[ln]=L[ln].replace('const now=performance.now()/1000;','')
TAIL=r"""    // serpent tail: a slow S-sway down the coils, the head held level and watching; it rears and strikes on 'sn'
    if(!B.tail8){for(let i=0;i<6;i++){const b=B['tail'+i];if(!b)continue;const uu=i/5,hh=HIST[Math.min(HIST.length-1,i*2)]||[0,0];
      loc(b,-p.tailUp*.08+(i<2?-.12*wk:0)+clamp(hh[1]*.001,-.1,.1),Math.sin(now*(4+5*wk+4*p.tail)-i*.7)*(.12+.1*p.tail)*(.5+uu)-clamp(hh[0]*.03,-.12,.12),0)}}
    else for(let i=0;i<10;i++){const b=B['tail'+i];if(!b)continue;const uu=i/9,hh=HIST[Math.min(HIST.length-1,i*2)]||[0,0];
      const sw=Math.sin(now*(1.5+wk)-i*.55)*(.05+.03*wk)*(.4+uu)-clamp(hh[0]*.025,-.1,.1);
      const pt=(i>=3&&i<=6?s.sn*.34:0)+(i>=7?-s.sn*.36:0)+(i<3?-p.tailUp*.04:0)+clamp(hh[1]*.001,-.1,.1)+(i>=7?Math.sin(now*.9+1)*.06:0);
      loc(b,pt,sw+(i===8?Math.sin(now*.7)*.25:0),i<3?sw*.6:0)}"""
ln=[j for j,x in enumerate(L) if 'for(let i=0;i<12;i++){const b=B[\'tail\'+i]' in x][0]
L[ln]=TAIL;L[ln+1]=''
FIRE=r"""  const fireTex=(()=>{const c=document.createElement('canvas');c.width=c.height=64;const g=c.getContext('2d'),gr=g.createRadialGradient(32,32,0,32,32,30);gr.addColorStop(0,'rgba(255,240,170,1)');gr.addColorStop(.35,'rgba(255,140,40,.9)');gr.addColorStop(1,'rgba(200,30,10,0)');g.fillStyle=gr;g.fillRect(0,0,64,64);return new T.CanvasTexture(c)})();
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
    if(ev==='fang'&&B.tail10){B.tail10.getWorldPosition(pW);bite(pW,0x9cff6a);S.stop=.04;shake(.15)}"""
ln=[j for j,x in enumerate(L) if x.lstrip().startswith('function fire(ev){')][0]
assert L[ln].strip()=="function fire(ev){const pW=V(),fw=V().set(0,0,1).applyQuaternion(root.quaternion);",L[ln]
L[ln]=FIRE
out='\n'.join(x for x in L if x!='')
a='q.v.multiplyScalar(Math.exp(-dt*3))';assert a in out;out=out.replace(a,'q.v.multiplyScalar(Math.exp(-dt*(q.fire?1.2:3)))')
open('fact_cer.js','w').write(out);print(len(out))
