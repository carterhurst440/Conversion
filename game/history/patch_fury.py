import base64
F='tidebreak.html';s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
b64=lambda p:base64.b64encode(open(p,'rb').read()).decode()
# ---------- Electra (the Greek fury): imported Tripo models with added wing bones ----------
rep("',archer:'","',fury:'"+b64('glb/fury_g.glb')+"',furyu:'"+b64('glb/furyu_g.glb')+"',archer:'")
rep("FACT.grkw=function(){",open('fact_fury.js').read()+"\nFACT.furyu=function(){FACT.__fu=1;try{return FACT.fury()}finally{FACT.__fu=0}};\nFACT.grkw=function(){")
rep("const GLAB=n=>({mh:{","const GLAB=n=>({mh:{fury:1.05,furyu:1.12,")
rep("TYPES.champ8b=TYPES.champ8;","TYPES.g1_2={f:'furyu',ps:44,vref:4.8,W:3.6,H:4,a:.12,cap:170,top:1.5,sh:7,atk:[['lash',.42,1],['slash',.4,1],['talon',.4,1],['lash',.42,1]]};TYPES.g1_2b=Object.assign({},TYPES.g1_2,{f:'fury',top:1.42});TYPES.champ8b=TYPES.champ8;")
rep("const TYU=u=>","const TYU=u=>u.type==='g1_2'&&!(window.MODELS&&window.MODELS.furyu)?null:u.type==='g1_2b'&&!(window.MODELS&&window.MODELS.fury)?null:")
rep("name:'Fury',hp:150,dmg:16,rate:1.1,range:1.2,spd:2.4,body:'winged',item:'whip',hat:'snakes',air:true,hitsAir:true,special:'fury',desc:'Hunts the guilty. She flies straight at any enemy that has just killed one of your troops and lashes it for triple damage.'}",
    "name:'Electra',hp:150,dmg:16,rate:1.1,range:1.2,spd:4.8,body:'winged',item:'whip',hat:'snakes',air:true,hitsAir:true,special:'wrath',desc:'A winged fury of the underworld and the fastest thing on the field. She streaks in, hovers over the fight and cracks a burning lash, sweeps it across, or tips forward to rake with her talons. Awakened as the serpent-crowned queen, every 16 seconds she climbs, spreads her wings and shrieks, then dives and cracks her lash into the ground: 60 damage at the heart, 36 around it, and everything caught is slowed.'}")
# Wrath of the Furies: manual-castable dive
rep("  if(sp==='fury'){","""  if(sp==='wrath'){u.wrCd=(u.wrCd==null?5:u.wrCd)-dt;if(u.wrT>0){u.wrT-=dt;u.path=[];u.moving=false;const tg=u.wrTg&&u.wrTg.hp>0?u.wrTg:null;if(tg){const dx=tg.x-u.x,dy=tg.y-u.y,d=Math.hypot(dx,dy)||1;u.fx=dx/d;u.fy=dy/d;if(u.wrT<1.8-.85&&u.wrT>1.8-1.3&&d>.7){const st=Math.min(d-.7,dt*6);u.x+=dx/d*st;u.y+=dy/d*st}}
      if(!u.wrHit&&u.wrT<=1.8-1.32){u.wrHit=1;const cx=tg?tg.x:u.x+(u.fx||0)*1.1,cy=tg?tg.y:u.y+(u.fy==null?1:u.fy)*1.1;
        for(const e of G.units){if(!foeOf(u,e))continue;const d=Math.hypot(e.x-cx,e.y-cy);if(d>1.9)continue;damageUnit(e,d<.8?60:36,u);e.slow=Math.max(e.slow||0,2.5)}
        ring(cx,cy,2,'#ff5a2a');ring(cx,cy,1.1,'#ffc27a');burst(cx,cy,['#ff5a2a','#ffc27a','#3a1010'],26);puff(cx,cy,10);float(cx,cy,'Wrath of the Furies!','#ff5a2a')}return true}
    if(u.wrCd>0)return false;if(u.side===0&&!(u.cast>G.t))return false;const[f]=nearestFoeUnit(u,4.5);if(!f){if(u.side!==0)u.wrCd=.6;return false}
    u.wrT=1.8;u.wrHit=0;u.wrTg=f;u.wrCd=16;u.cast=0;return true}
  if(sp==='fury'){""")
rep("hellgate:{nm:'Gates of Tartarus',","wrath:{nm:'Wrath of the Furies',cd:u=>u.wrCd==null?5:u.wrCd,max:16,col:'#ff5a2a',ic:'\\u2726'},hellgate:{nm:'Gates of Tartarus',")
rep("SPNAME={hellgate:'Gates of Tartarus',","SPNAME={wrath:'Wrath of the Furies',hellgate:'Gates of Tartarus',")
rep("  if(ty.f==='cer'){if(u.hgT>0)","  if(ty.f==='fury'||ty.f==='furyu'){if(u.wrT>0){special=true;if(S.clip!=='wrath')c.playG('wrath',1,Math.max(0,1.8-u.wrT));S.hold=true}else if(S.clip==='wrath'&&S.hold)S.hold=false;if(u.wrT>0)special=true}\n  if(ty.f==='cer'){if(u.hgT>0)")
open(F,'w').write(s);print('electra ok')
