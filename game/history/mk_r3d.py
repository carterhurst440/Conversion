import re
def lines(f): return open(f).read().split('\n')
def upto(f,marker):
    s=open(f).read();i=s.index(marker);return s[:i]
def block(f,a,b):
    L=lines(f);ia=next(i for i,l in enumerate(L) if a in l);ib=next(i for i in range(ia+1,len(L)) if b in L[i]);return '\n'.join(L[ia:ib])

# shared per-frame tail of every controller
COMMON_HEAD="""
  S.x=0;S.z=0;S.rate=1;S.hold=false;const _play0=play;
  function playG(n,rate,off){_play0(n);S.rate=rate||1;S.t=off||0;S.firedT=S.t}
  function clipStep(dt){const c=CLIPS[S.clip];S.t+=dt*(S.rate||1);if(!c.loop&&S.t>=c.dur&&!S.hold){playG('idle');}const c2=CLIPS[S.clip];const tt=c2.loop?S.t%c2.dur:Math.min(S.t,c2.dur);
    let p=sample(S.clip,tt);if(S.bl>0&&S.prev){S.bl-=dt;p=mix(S.prev,p,1-Math.max(0,S.bl)/S.blT)}return p}
  function face(I,dt,k){let df=I.yaw-S.yaw;df=Math.atan2(Math.sin(df),Math.cos(df));S.yaw+=df*Math.min(1,dt*(k||9))}
  function flash(on){for(const m of U.mats)if(m!==U.gold)m.emissive.setHex(on?0xffffff:0)}
"""

druid_tick="""
  CLIPS.sinkG={dur:.42,keys:[[0,P({}),'io'],[.12,P(DIG),'snap'],[.42,X(DIG,{sink:1.15,spin:200,ry:12}),'in']]};
  CLIPS.riseG={dur:.7,keys:[[0,X(DIG,{sink:1.15,spin:200}),'lin'],[.38,X(REAR,{sink:-.05,spin:0,glow:1.3}),'back'],[.7,P({}),'io']]};
  function tick(dt,I){S.x=I.x;S.z=I.z;face(I,dt,7);S.vel=I.speed;S.wph+=I.dist/.62*TAU;
    let p=clipStep(dt);S.wamt+=(clamp(S.vel/.5,0,1)-S.wamt)*Math.min(1,dt*5);if(S.clip==='idle'&&S.wamt>.01){const w=walkPose(S.wph,Math.min(1,S.wamt*1.15));p=mix(p,w,Math.min(1,S.wamt*2))}
    cur=springPose(p,dt);applyPose(cur);flash(I.flash);
%s
  }
"""%block('druid_main.js','// beard and moss mantle are cloth','for(const d of DUM){if')

stag_tick="""
  function tick(dt,I){S.x=I.x;S.z=I.z;face(I,dt,I.run?20:8);S.vel=I.speed;const g=clamp((S.vel-.9)/1.2,0,1);S.gait+=((I.run?1:g)-S.gait)*Math.min(1,dt*4);S.wph+=I.dist/lerp(.72,1.75,S.gait)*TAU;
    let p=clipStep(dt);S.wamt+=(clamp(S.vel/.8,0,1)-S.wamt)*Math.min(1,dt*7);
    if(I.run){p=mix(p,gaitPose(S.wph,1,1),.85);p.neck=lerp(p.neck,80,.7);p.headP=lerp(p.headP,36,.7);p.ear=-60;p.brow=1}
    else if(S.clip==='idle'&&S.wamt>.01){const w=gaitPose(S.wph,Math.min(1,S.wamt*1.15),S.gait);p=mix(p,w,Math.min(1,S.wamt*2.2))}
    cur=springPose(p,dt);applyPose(cur,dt);flash(I.flash);
%s
  }
"""%block('stag_main.js','// ribbons tied to the antlers','for(const d of DUM){if')

serp_tick="""
  initTrail();
  function tick(dt,I){S.x=I.x;S.z=I.z;face(I,dt,6);S.vel=I.speed;S.wph+=I.dist/.55*TAU;S.under=!!I.under;
    let p=clipStep(dt);
    if(S.under)S.depth=-.4;else if(S.clip==='dive')S.depth=Math.min(0,cur.dep);else if(S.clip==='erupt'&&S.t<.3)S.depth=Math.min(0,cur.dep);else S.depth=0;
    S.wamt+=(clamp(S.vel/.8,0,1)-S.wamt)*Math.min(1,dt*6);if(S.clip==='idle'&&S.wamt>.01){const k=Math.min(1,S.wamt*1.5);p=mix(p,P({lift:S.under?-.1:.07,hp:.12,hy:0,sway:0,tongue:0,dep:0}),k)}
    if(S.under)p.lift=-.05;
    cur=springPose(p,dt);
    if(S.clip==='erupt'||S.clip==='dive'||S.under||S.vel>.01)pushTrail(headGround());
    if(!S.under&&S.clip!=='dive'&&!(S.clip==='erupt'&&S.t<.3)){for(let i=1;i<TRAIL.length;i++){const q=TRAIL[i];if(q.y<0)q.y=Math.min(0,q.y+dt*.32)}}
    applyPose(cur);flash(I.flash);
  }
  function teleport(){initTrail()}
"""

cern_tick="""
  function tick(dt,I){S.x=I.x;S.z=I.z;face(I,dt,8);S.vel=I.speed;S.wph+=I.dist/1.25*TAU;
    let p=clipStep(dt);S.wamt+=(clamp(S.vel/.8,0,1)-S.wamt)*Math.min(1,dt*6);if(S.clip==='idle'&&S.wamt>.01){const w=walkPose(S.wph,Math.min(1,S.wamt*1.15));p=mix(p,w,Math.min(1,S.wamt*2.2))}
    cur=springPose(p,dt);applyPose(cur,dt);U.torc.visible=!I.torcAway;flash(I.flash);
    S.eyeT-=dt;if(S.eyeT<=0){S.blink=.12;S.eyeT=3+R()*3}if(S.blink>0)S.blink-=dt;
    {const eg=Math.max(0,cur.eyeG||0);for(const g of U.eyeGlow){g.material.opacity=S.blink>0&&eg<.3||cur.eye>.5?.1:Math.min(1,.75+eg*.25+Math.sin(performance.now()*.004)*.2);g.scale.setScalar(.07+eg*.1)}for(const e of U.eyes)e.scale.x=1.35+eg*.5}
%s
  }
"""%block('cern_main.js','// leaf cape from the shoulders','// smear behind')

def factory(name,parts,tick,extra_ret=''):
    body='\n'.join(parts)
    # strip things that only make sense on the test page
    return "FACT.%s=function(){\n%s\n%s\n%s\n  return{U,S,scene,get cur(){return cur},playG,tick,clips:CLIPS%s};};\n"%(name,body,COMMON_HEAD,tick,extra_ret)

out=open('r3d_head.js').read()
out+=factory('druid',[open('druid_build.js').read(),upto('druid_main.js','function addNum')],druid_tick)
out+=factory('stag',[open('stag_build.js').read(),upto('stag_main.js','function addNum')],stag_tick)
out+=factory('serpent',[upto('serpent_main.js','function addNum')],serp_tick,',teleport')
out+=factory('cern',[open('cern_build.js').read(),upto('cern_main.js','function addNum')],cern_tick)
out+=open('r3d_driver.js').read()
open('r3d.js','w').write(out)
print(len(out))
