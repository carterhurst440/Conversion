import base64
F='tidebreak.html';s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
b64=lambda p:base64.b64encode(open(p,'rb').read()).decode()
# ---------- the Sobek Guard: a fifth Egyptian holy unit, crocodile warrior ----------
rep("',archer:'","',croc:'"+b64('glb/croc_g.glb')+"',crocu:'"+b64('glb/crocu_g.glb')+"',archer:'")
rep("FACT.grkw=function(){",open('fact_croc.js').read()+"\nFACT.crocu=function(){FACT.__cu=1;try{return FACT.croc()}finally{FACT.__cu=0}};\nFACT.grkw=function(){")
rep("const GLAB=n=>({mh:{","const GLAB=n=>({mh:{croc:1.18,crocu:1.24,")
rep("for 1.8\\u00d7 damage.'}],","for 1.8\\u00d7 damage.'},\n  {name:'Sobek Guard',hp:380,dmg:22,rate:.8,range:.9,spd:1.7,house:2,lv:2,cost:{wheat:14},time:110,awaken:'rite2',item:'none',special:'deathroll',desc:'A crocodile warrior of Sobek. He hacks and hooks with a bronze khopesh, lunges in jaws-first, and spins on the spot so his heavy tail sweeps everything around him. Awakened in Sobek\\u2019s gold, every 14 seconds he clamps onto an enemy and drags it into a death roll: three wrenching hits of 24, and the victim is left stunned for 2 seconds.'}],")
rep("TYPES.champ8b=TYPES.champ8;","TYPES.g0_4={f:'crocu',ps:46,vref:1.7,W:4,H:3.4,a:.24,cap:170,top:1.22,sh:10,atk:[['hack',.44,1],['hook',.42,1],['chomp',.4,1],['spin',.42,1]]};TYPES.g0_4b=Object.assign({},TYPES.g0_4,{f:'croc',top:1.16});TYPES.champ8b=TYPES.champ8;")
rep("const TYU=u=>","const TYU=u=>u.type==='g0_4'&&!(window.MODELS&&window.MODELS.crocu)?null:u.type==='g0_4b'&&!(window.MODELS&&window.MODELS.croc)?null:")
rep("  if(sp==='wrath'){","""  if(sp==='deathroll'){u.drCd=(u.drCd==null?5:u.drCd)-dt;if(u.drT>0){u.drT-=dt;u.path=[];u.moving=false;const tg=u.drTg&&u.drTg.hp>0?u.drTg:null;
      if(tg){const dx=tg.x-u.x,dy=tg.y-u.y,d=Math.hypot(dx,dy)||1;u.fx=dx/d;u.fy=dy/d;if(u.drT>1.95-.42&&d>.6){const st=Math.min(d-.6,dt*5);u.x+=dx/d*st;u.y+=dy/d*st}if(u.drT<1.95-.42)tg.stun=Math.max(tg.stun||0,.2)}
      const el=1.95-u.drT;for(const[k,ht]of[[1,.7],[2,1.15],[3,1.6]])if((u.drHit||0)<k&&el>=ht){u.drHit=k;if(tg&&Math.hypot(tg.x-u.x,tg.y-u.y)<1.6){damageUnit(tg,24,u);burst(tg.x,tg.y,['#8fd0e0','#d9c49a','#ffffff'],10);if(k===3){tg.stun=Math.max(tg.stun||0,U[tg.type].champ!=null?1.2:2);float(tg.x,tg.y,'Death Roll!','#3f8f9a')}}}
      return true}
    if(u.drCd>0)return false;if(u.side===0&&!(u.cast>G.t))return false;const[f]=nearestFoeUnit(u,3);if(!f||U[f.type].air){if(u.side!==0)u.drCd=.6;return false}
    u.drT=1.95;u.drHit=0;u.drTg=f;u.drCd=14;u.cast=0;ring(u.x,u.y,1.2,'#3f8f9a');return true}
  if(sp==='wrath'){""")
rep("wrath:{nm:'Wrath of the Furies',","deathroll:{nm:'Death Roll',cd:u=>u.drCd==null?5:u.drCd,max:14,col:'#3f8f9a',ic:'\\u21bb'},wrath:{nm:'Wrath of the Furies',")
rep("SPNAME={wrath:","SPNAME={deathroll:'Death Roll',wrath:")
rep("  if(ty.f==='fury'||ty.f==='furyu'){","  if(ty.f==='croc'||ty.f==='crocu'){if(u.drT>0){special=true;if(S.clip!=='roll')c.playG('roll',1,Math.max(0,1.95-u.drT));S.hold=true}else if(S.clip==='roll'&&S.hold)S.hold=false;if(u.drT>0)special=true}\n  if(ty.f==='fury'||ty.f==='furyu'){")
open(F,'w').write(s);print('croc ok')
