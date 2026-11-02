import base64
F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
b64=lambda p:base64.b64encode(open(p,'rb').read()).decode()
rep("',archer:'","',stoneb:'"+b64('glb/stoneb_g.glb')+"',archer:'")
rep("FACT.adruid=function(){FACT.__up=1;try{return FACT.vdruid()}finally{FACT.__up=0}};","FACT.adruid=function(){FACT.__up=1;try{return FACT.vdruid()}finally{FACT.__up=0}};\n"+open('fact_stoneb.js').read()+"\n")
rep("vdruid:1,adruid:1}[n]","vdruid:1,adruid:1,stoneb:1}[n]")
rep("TYPES.champ0b=TYPES.champ0;","TYPES.champ0b=TYPES.champ0;TYPES.stoneb={f:'stoneb',ps:50,vref:1.85,W:3,H:2.9,a:.22,cap:200,top:1.05,sh:9,atk:[['plant',.95,1],['reap',.42,1],['mine',.44,1],['punch',.62,1]],\n  jobs:u=>{if(u.type==='stoneb')return TYPES.stoneb.atk;const w=u.work;if(u.tgt&&u.tgt.hp>0&&(!w||u.mode==='attack'))return[['punch',.18,1]];if(w==='mine')return[['mine',.44,1]];if(w==='farm')return u.wt!=null&&dep[u.wt]==='wheat'?[['reap',.42,1]]:[['plant',.95,1]];return u.tgt?[['punch',.18,1]]:[['reap',.42,1]]}};")
rep("if(!special){const A=ty.atk,nx=A[st.combo%A.length];","if(!special){const A=ty.jobs?ty.jobs(u):ty.atk,nx=A[st.combo%A.length];")
rep("const I={x,z,yaw,dist:dist*cad,speed:u.moving?speed:Math.min(speed,.04),flash:(u.hurt||0)>.115};",
    "const I={x,z,yaw,dist:dist*cad,speed:u.moving?speed:Math.min(speed,.04),flash:(u.hurt||0)>.115};if(ty.f==='stoneb')I.sb={drawing:!ov&&G&&u.work==='water'&&G.t-(u.wpT||0)<.25&&!u.dropping,carry:u.carry&&(u.dropping||u.carry.n>=CARRY||u.carry.k==='water')?u.carry.k:null};")
rep("const STATS={tick:0,render:0,n:0,calls:0};","const TYU=u=>u.type==='sower'?((u.side==null?playerGod()===0:G&&G.S&&G.S[u.side]&&G.S[u.side].god===0)&&window.MODELS&&window.MODELS.stoneb?TYPES.stoneb:null):u.type==='stoneb'&&!(window.MODELS&&window.MODELS.stoneb)?null:TYPES[u.type];\nconst STATS={tick:0,render:0,n:0,calls:0};")
rep("for(const u of G.units){const ty=TYPES[u.type];if(!ty)continue;const st=CT.get(u)||create(u,ty);","for(const u of G.units){const ty=TYU(u);if(!ty)continue;const st=CT.get(u)||create(u,ty);")
rep("function drawDemo(u,sx,sy,s,fl){const ty=TYPES[u.type]||(u.type==null&&null);","function drawDemo(u,sx,sy,s,fl){const ty=TYU(u);")
rep("const top=u=>{const ty=TYPES[u.type];return ty?ty.top*ty.ps:46};\nconst owns=u=>!!TYPES[u.type]&&!failed;","const top=u=>{const ty=TYU(u);return ty?ty.top*ty.ps:46};\nconst owns=u=>!!TYU(u)&&!failed;")
rep("  const t=U[u.type];if(t&&t.dummy)return drawDummy(u,sx,sy,s);","  const t=U[u.type];if(t&&t.dummy)return drawDummy(u,sx,sy,s);\n  if((u.type==='sower'||u.type==='stoneb')&&R3D&&R3D.draw(u,sx,sy,s,fl))return sy-R3D.top(u)*s;")
# 3D Stonebearers carry their own loads, so the flat drag/pile is only for the drawn fallback
rep("  if(u.carry&&u.carry.k==='stone'&&EGY(u.side))dragBlock(u,sx,sy,s,0);","  const own3=R3D&&R3D.owns(u);if(u.carry&&u.carry.k==='stone'&&EGY(u.side)&&!own3)dragBlock(u,sx,sy,s,0);")
rep("  if(u.carry&&u.carry.k==='stone'&&EGY(u.side)){dragBlock(u,sx,sy,s,1)}\n  else if(u.carry){","  if(u.carry&&u.carry.k==='stone'&&EGY(u.side)){if(!own3)dragBlock(u,sx,sy,s,1)}\n  else if(u.carry&&!(own3&&u.carry.k==='water')){")
# Movement Lab entry
rep("const LABX={8:['cdruid','carcher']};","U.stoneb=Object.assign({},U.sower,{name:'Stonebearer',role:'Villager',bld:'none',lv:9,desc:'The Egyptian worker: plants and reaps wheat, quarries stone with a maul, draws water from the Wells, and carries every load home.'});const LABX={8:['cdruid','carcher'],0:['stoneb']};")
open(F,'w').write(s);print('stoneb ok',len(s))
