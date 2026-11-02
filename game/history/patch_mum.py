import base64
F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
b64=lambda p:base64.b64encode(open(p,'rb').read()).decode()
# ---------- the Mummy and the Mega Mummy: imported Tripo models ----------
rep("',archer:'","',mumm:'"+b64('glb/mumm_g.glb')+"',mega:'"+b64('glb/mega_g.glb')+"',archer:'")
rep("FACT.grkw=function(){",open('fact_mum.js').read()+"\nFACT.mega=function(){FACT.__mg=1;try{return FACT.mumm()}finally{FACT.__mg=0}};\nFACT.grkw=function(){")
rep("const GLAB=n=>({mh:{","const GLAB=n=>({mh:{mumm:.95,mega:1.45,")
rep("TYPES.megamummy=Object.assign({},TYPES.g0_1,{ps:56,cap:210});","TYPES.g0_1={f:'mumm',ps:44,vref:1.6,W:3.6,H:3.2,a:.24,cap:160,top:1.08,sh:9,atk:[['claw',.46,1],['grab',.42,1],['flail',.3,1]]};TYPES.g0_1b=TYPES.g0_1;TYPES.megamummy={f:'mega',ps:62,vref:1.6,W:4,H:3.4,a:.24,cap:220,top:1.12,sh:12,atk:[['smash',.66,1],['hay',.46,1],['grab',.42,1],['smash',.66,1]]};")
rep("const TYU=u=>","const TYU=u=>(u.type==='g0_1'||u.type==='g0_1b')&&!(window.MODELS&&window.MODELS.mumm)?null:u.type==='megamummy'&&!(window.MODELS&&window.MODELS.mega)?null:")
rep("if(ty.f==='mummy'){if(u.down>0)","if(ty.f==='mummy'||ty.f==='mumm'||ty.f==='mega'){if(u.down>0)")
# the Mega Mummy climbs out at full strength (the half-health return is for a Mummy that lay still)
rep("if(u.down>0){u.down-=dt;if(u.down<=0){u.hp=u.max*.5;","if(u.down>0){u.down-=dt;if(u.down<=0){u.hp=u.type==='megamummy'?u.max:u.max*.5;")
open(F,'w').write(s);print('mummies ok')
