import base64
F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
b64=lambda p:base64.b64encode(open(p,'rb').read()).decode()
# ---------- Charon: the Ferryman's 3D model (stands in for the basic Ferryman too until its own model arrives) ----------
rep("',archer:'","',charon:'"+b64('glb/charon_g.glb')+"',archer:'")
rep("FACT.grkw=function(){",open('fact_charon.js').read()+"\nFACT.grkw=function(){")
rep("const GLAB=n=>({mh:{","const GLAB=n=>({mh:{charon:1,")
rep("TYPES.champ0b=TYPES.champ0;","TYPES.champ0b=TYPES.champ0;TYPES.g1_0={f:'charon',ps:50,vref:1.6,W:3.8,H:3.2,a:.22,cap:200,top:1.12,sh:9,atk:[['sweep',.42,1]]};TYPES.g1_0b=TYPES.g1_0;")
open(F,'w').write(s);print('charon ok')
s=open(F).read()
rep("',archer:'","',charonu:'"+b64('glb/charonu_g.glb')+"',archer:'")
rep("FACT.grkw=function(){","FACT.charonu=function(){FACT.__chu=1;try{return FACT.charon()}finally{FACT.__chu=0}};\nFACT.grkw=function(){")
rep("TYPES.g1_0={f:'charon',ps:50,vref:1.6,W:3.8,H:3.2,a:.22,cap:200,top:1.12,sh:9,atk:[['sweep',.42,1]]};TYPES.g1_0b=TYPES.g1_0;","TYPES.g1_0={f:'charonu',ps:50,vref:1.6,W:3.8,H:3.2,a:.22,cap:200,top:1.12,sh:9,atk:[['sweep',.42,1]]};TYPES.g1_0b=Object.assign({},TYPES.g1_0,{f:'charon'});")
rep("const GLAB=n=>({mh:{charon:1,","const GLAB=n=>({mh:{charon:1,charonu:1,")
open(F,'w').write(s);print('charon upgrade ok')
s=open(F).read()
# the three-hit oar combo
rep("TYPES.g1_0={f:'charonu',ps:50,vref:1.6,W:3.8,H:3.2,a:.22,cap:200,top:1.12,sh:9,atk:[['sweep',.42,1]]};","TYPES.g1_0={f:'charonu',ps:50,vref:1.6,W:4.2,H:3.4,a:.24,cap:200,top:1.12,sh:9,atk:[['thrust',.38,1],['rise',.45,1],['pound',.62,1]]};")
# Styx Surge: the upgraded Charon's chosen special; the toll stays on every Ferryman
rep("U[f.type].special!=='toll'||Math.hypot(f.x-u.x,f.y-u.y)>3)continue;","!(U[f.type].special==='toll'||U[f.type].toll)||Math.hypot(f.x-u.x,f.y-u.y)>3)continue;")
rep("const isHoly=u=>U[u.type].champ!=null||!!U[u.type].gu;","const isHoly=u=>U[u.type].champ!=null||!!U[u.type].gu;\nif(U.g1_0){U.g1_0.toll=true;if(U.g1_0b)U.g1_0b.toll=true;U.g1_0.special='styx';U.g1_0.desc='Charon takes his toll: every enemy that dies within 3 squares of him pays you 6 wood and 6 wheat. He fights with a three-blow oar combo: a long spear thrust, a great rising sweep and a ground-shaking pound. Awakened, he can call a Styx Surge: he slams the oar down and the river of the dead floods out around him, battering, slowing and drowning every enemy caught in it. He wades through rivers and sea as if they were roads.';if(U.g1_0b)U.g1_0b.desc='The young ferryman of the dead. Every enemy that dies within 3 squares of him pays you 6 wood and 6 wheat, and his oar strikes in a three-blow combo. He wades through rivers and sea as if they were roads.'}")
rep("const SPNAME={","const SPNAME={styx:'Styx Surge',")
rep("  if(sp==='skyfall'){",r"""  if(sp==='styx'){u.styCd=(u.styCd==null?5:u.styCd)-dt;if(u.styT>0){u.styT-=dt;u.path=[];u.moving=false;
      if(!u.styHit&&u.styT<=1.1-.62){u.styHit=1;const fx=u.fx||0,fy=u.fy==null?1:u.fy,cx=u.x+fx*1.1,cy=u.y+fy*1.1;
        for(const e of G.units){if(!foeOf(u,e)||U[e.type].air)continue;const d=Math.hypot(e.x-cx,e.y-cy);if(d>3)continue;damageUnit(e,32,u);e.slow=Math.max(e.slow||0,3);const k=(3-d)/3*.7,nx=e.x+(e.x-cx)/(d||1)*k,ny=e.y+(e.y-cy)/(d||1)*k;if(landAt(nx,ny)){e.x=nx;e.y=ny}}
        G.pools.push({x:cx,y:cy,r:2.4,t:4,side:u.side,styx:1});ring(cx,cy,3,'#3fb8a8');ring(cx,cy,2,'#bff4ec');burst(cx,cy,['#2a7a72','#7fe0d0','#1d2e3a'],24);puff(cx,cy,12);float(u.x,u.y,'Styx Surge!','#3fb8a8')}return true}
    if(u.styCd>0)return false;if(u.side===0&&!(u.cast>G.t))return false;const[f]=nearestFoeUnit(u,4);if(!f&&u.side!==0){u.styCd=.6;return false}if(f)face(u,f.x,f.y);
    u.styT=1.1;u.styHit=0;u.styCd=14;u.cast=0;return true}
  if(sp==='skyfall'){""")
rep("if(ty.f==='sphinx'){if(u.skyT>0){","if(ty.f==='charonu'){if(u.styT>0){special=true;if(S.clip!=='pound')c.playG('pound',.9,Math.max(0,1.1-u.styT));S.hold=true}else if(S.clip==='pound'&&S.hold)S.hold=false;if(u.styT>0)special=true}\n  if(ty.f==='sphinx'){if(u.skyT>0){")
rep("swarmplague:{nm:'Plague',","styx:{nm:'Styx Surge',cd:u=>u.styCd==null?5:u.styCd,max:14,col:'#3fb8a8',ic:'\\u224b'},swarmplague:{nm:'Plague',")
open(F,'w').write(s);print('ferryman combo + styx ok')
