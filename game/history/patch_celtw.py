F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
# ---------- Celtic workers: the Verdant Druid, researched up into the Aged Druid who labors and fights ----------
rep("8:{hall:'Nemeton',","8:{sower:'Verdant Druid',sowers:'Verdant Druids',aged:1,hall:'Nemeton',")
rep("sower:'Crofter',sowers:'Crofters'},","},")
rep("const LABX={8:['cdruid','carcher'],","U.aged=Object.assign({},U.cdruid,{name:'Aged Druid',role:'Villager \\u00b7 Ranged',civ:true,fights:true,base:'sower',house:1,bld:'upgrade',cost:{wheat:3},desc:'The Verdant Druid grown old and powerful. He still plants, reaps and chops, and when enemies come near he fights back, casting orbs of green power at range. His Thorns pin up to 3 enemies for 2 seconds.'});delete U.aged.gu;delete U.aged.god;\nconst LABX={8:['cdruid','carcher'],")
rep("isSow=u=>u.type==='sower'||u.type==='shaper';","isSow=u=>u.type==='sower'||u.type==='shaper'||u.type==='aged';")
rep("  sandtrap:{br:'Sowers',","  agedruid:{br:'Sowers',name:'Aged Druids',tier:2,cost:{wheat:20,wood:24},time:40,desc:'Every Verdant Druid, now and later, grows into an Aged Druid: three times the health, and he fights back with ranged green magic and Thorns while still planting, reaping and chopping.'},\n  sandtrap:{br:'Sowers',")
rep("||(k==='sandtrap'&&S.god!==0))return{hide:true};","||(k==='sandtrap'&&S.god!==0)||(k==='agedruid'&&S.god!==8))return{hide:true};")
rep("&&!(k==='sandtrap'&&g!==0))","&&!(k==='sandtrap'&&g!==0)&&!(k==='agedruid'&&g!==8))")
rep("function applyTech(side,k){const S=G.S[side];","function toAged(u){const f=u.hp/u.max;u.type='aged';u.max=U.aged.hp*(1+.2*(u.rank||0));u.hp=u.max*f;burst(u.x,u.y,['#8fdc6a','#c8ff9a','#fbf6ee'],12);ring(u.x,u.y,.7,'#8fdc6a');if(u.side===0)float(u.x,u.y,'Aged Druid','#3f8a2c')}\nfunction agedFight(u,dt){if(u.mode==='attack'&&u.tgt&&u.tgt.hp>0&&!u.autoF)return true;\n  if(u.autoF&&u.mode==='attack'){const v=u.tgt;if(v&&v.hp>0&&Math.hypot(v.x-u.x,v.y-u.y)<5.5)return true;u.autoF=0;u.mode='idle';u.tgt=null;u.path=[];return false}\n  if((u.afT=(u.afT||0)-dt)>0)return false;u.afT=.4;let f=null,bd=3.4;for(const e of G.units){if(!foeOf(u,e)||e.hp<=0||e.hid||e.leap)continue;const d=Math.hypot(e.x-u.x,e.y-u.y);if(d<bd){bd=d;f=e}}\n  if(!f)return false;u.autoF=1;u.tgt=f;u.mode='attack';u.plan=0;u.path=[];return true}\nfunction applyTech(side,k){const S=G.S[side];if(k==='agedruid')for(const u of G.units)if(u.side===side&&u.type==='sower')toAged(u);")
rep("if(t.civ&&u.mode!=='move'&&u.mode!=='board'){civTick(u,dt);","if(u.type==='sower'&&G.S[u.side]&&G.S[u.side].tech&&G.S[u.side].tech.agedruid&&!G.arena){toAged(u);return}\n  if(t.civ&&u.mode!=='move'&&u.mode!=='board'&&!(t.fights&&agedFight(u,dt))){u.autoF=0;civTick(u,dt);")
# 3D: Celtic workers drawn as the Verdant / Aged Druid, animated by their job
rep("const TYU=u=>u.type==='sower'?(","const TYU=u=>u.type==='aged'?(window.MODELS&&window.MODELS.adruid?TYPES.aged:null):u.type==='sower'&&(u.side==null?playerGod()===8:G&&G.S&&G.S[u.side]&&G.S[u.side].god===8)?(window.MODELS&&window.MODELS.vdruid?TYPES.cdruidb:null):u.type==='sower'?(")
rep("TYPES.champ0b=TYPES.champ0;","TYPES.champ0b=TYPES.champ0;{const dj=(u,fight)=>{const w=u.work;if(u.mode==='attack'&&u.tgt&&u.tgt.hp>0)return fight;if(w==='farm')return u.wt!=null&&dep[u.wt]==='wheat'?[['reap',.42,1]]:[['plant',.95,1]];if(w==='forest'||w==='chop'||w==='mine')return u.wt!=null&&dep[u.wt]==='tree'||w!=='forest'?[['chop',.44,1]]:[['plant',.95,1]];if(w==='reap')return[['reap',.42,1]];return null};\n  TYPES.cdruidb.jobs=u=>u.type==='cdruidb'?TYPES.cdruidb.atk:dj(u,[['reap',.42,1]])||TYPES.cdruidb.atk;TYPES.aged=Object.assign({},TYPES.cdruid,{atk:[['cast',.5,1]],jobs:u=>dj(u,[['cast',.5,1]])||[['cast',.5,1]]})}")
rep("  if((u.type==='sower'||u.type==='stoneb')&&R3D&&R3D.draw(u,sx,sy,s,fl))","  if((u.type==='sower'||u.type==='stoneb'||u.type==='aged')&&R3D&&R3D.draw(u,sx,sy,s,fl))")
rep("TYPES.cdruidb={","TYPES.cdruidb={",0) if False else None
open(F,'w').write(s);print('celtic workers ok',len(s))
s=open(F).read()
rep("for(const u of G.units){const ty=TYU(u);if(!ty)continue;const st=CT.get(u)||create(u,ty);","for(const u of G.units){const ty=TYU(u);if(!ty)continue;let st=CT.get(u);if(st&&st.ty!==ty){dispose(st);CT.delete(u);st=null}if(!st)st=create(u,ty);")
open(F,'w').write(s);print('rig swap ok')
