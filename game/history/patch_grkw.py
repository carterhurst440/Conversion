import base64
F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
b64=lambda p:base64.b64encode(open(p,'rb').read()).decode()
# ---------- the Greek worker: the Artisan, a 3D laborer on the shared worker animation set ----------
rep("',archer:'","',grkw:'"+b64('glb/grkw_g.glb')+"',archer:'")
rep("1:{harbor:'Limen',harbors:'Limens',sower:'Shade',sowers:'Shades'}","1:{harbor:'Limen',harbors:'Limens',sower:'Artisan',sowers:'Artisans'}")
rep("FACT.grainb=function(){","FACT.grkw=function(){FACT.__sbm='grkw';try{return FACT.stoneb()}finally{FACT.__sbm=null}};FACT.grainb=function(){")
rep("TYPES.grainb=Object.assign({},TYPES.stoneb,{f:'grainb'});","TYPES.grainb=Object.assign({},TYPES.stoneb,{f:'grainb'});TYPES.grkw=Object.assign({},TYPES.stoneb,{f:'grkw',jobs:u=>{const w=u.work;if(u.tgt&&u.tgt.hp>0&&(!w||u.mode==='attack'))return[['punch',.18,1]];if(w==='farm')return u.wt!=null&&dep[u.wt]==='wheat'?[['reap',.42,1]]:[['plant',.95,1]];if(w==='forest'||w==='chop')return u.wt!=null&&dep[u.wt]==='tree'?[['chop',.44,1]]:[['plant',.95,1]];if(w==='mine'||w==='quarry')return[['mine',.44,1]];return u.tgt?[['punch',.18,1]]:TYPES.stoneb.atk}});")
rep("if(ty.f==='stoneb'||ty.f==='grainb'||ty.f==='waterb')I.sb=","if(ty.f==='stoneb'||ty.f==='grainb'||ty.f==='waterb'||ty.f==='grkw')I.sb=")
rep("const TYU=u=>(u.type==='grainb'||u.type==='waterb')?","const TYU=u=>u.type==='sower'&&(u.side==null?playerGod()===1:G&&G.S&&G.S[u.side]&&G.S[u.side].god===1)?(window.MODELS&&window.MODELS.grkw?TYPES.grkw:null):(u.type==='grainb'||u.type==='waterb')?")
rep("key=k==='sower'?(g===0?'stoneb':g===8?'vdruid':''):","key=k==='sower'?(g===0?'stoneb':g===8?'vdruid':g===1?'grkw':''):")
rep("const GLAB=n=>({mh:{","const GLAB=n=>({mh:{grkw:1,")
open(F,'w').write(s);print('greek worker ok')
