import base64
F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
b64=lambda p:base64.b64encode(open(p,'rb').read()).decode()
# ---------- Egypt's three bearers: each trained for one job, which it does on its own; to change jobs, retire one and train another ----------
rep("',archer:'","',grainb:'"+b64('glb/grainb_g.glb')+"',waterb:'"+b64('glb/waterb_g.glb')+"',archer:'")
rep("const LABX={8:['cdruid','carcher'],","U.grainb=Object.assign({},U.sower,{name:'Grainbearer',egonly:1,desc:'Egypt\\u2019s farmer. Sows and reaps wheat on his own and carries the harvest to a Pyramid. He only farms: to change his work, retire him and train another bearer.'});\nU.waterb=Object.assign({},U.sower,{name:'Waterbearer',egonly:1,desc:'Egypt\\u2019s water carrier. Draws water from the Wells on his own and carries it to a Pyramid. Every Egyptian troop needs water. He only carries water: to change his work, retire him and train another bearer.'});\nconst LABX={8:['cdruid','carcher'],")
rep("CIV=['sower','missionary'];","CIV=['sower','grainb','waterb','missionary'];")
rep("isSow=u=>u.type==='sower'||u.type==='shaper'||u.type==='aged';","isSow=u=>u.type==='sower'||u.type==='shaper'||u.type==='aged'||u.type==='grainb'||u.type==='waterb';")
rep("const CHIPS=['sower','missionary','ram'];","const CHIPS=['sower','grainb','waterb','missionary','ram'];")
rep("return ks.filter(k=>U[k]&&hasT(b.side,U[k].tech)&&S.tier>=U[k].lv)}","return ks.filter(k=>U[k]&&hasT(b.side,U[k].tech)&&S.tier>=U[k].lv&&!(U[k].egonly&&S.god!==0))}")
# each bearer keeps to its job
rep("if(u.type==='sower'&&G.S[u.side]&&G.S[u.side].tech&&G.S[u.side].tech.agedruid&&!G.arena){toAged(u);return}",
    "if(u.type==='sower'&&G.S[u.side]&&G.S[u.side].tech&&G.S[u.side].tech.agedruid&&!G.arena){toAged(u);return}\n  if(!G.arena&&u.mode!=='move'&&u.mode!=='board'&&EGY(u.side)){const ej={sower:'mine',grainb:'farm',waterb:'water'}[u.type];if(ej&&u.work!==ej)setWork(u,ej,u.x,u.y)}")
# Egypt: no job buttons, a Retire button instead
rep("else if(sw){acts.push(`<div class=\"jobs\">","else if(sw&&EGY(0)){acts.push(`<button class=\"big dark sow\" data-c=\"retire\">Retire<small>${sw>1?sw+' bearers':'frees room'}</small></button>`)}else if(sw){acts.push(`<div class=\"jobs\">")
rep("if(us.length===1&&(br||mn||sw)&&!shapeMenu){","if(us.length===1&&(br||mn||sw)&&!shapeMenu&&!EGY(0)){")
rep("if(c==='shaper'){let n=0;","if(c==='retire'){let n=0;for(const u of selUnits()){if(!isSow(u)||u.side!==0)continue;const i=G.units.indexOf(u);if(i>=0)G.units.splice(i,1);puff(u.x,u.y,6);burst(u.x,u.y,['#e8cf9a','#fbf6ee'],8);SEL.delete(u);n++}if(n)toast(`${n} bearer${n>1?'s':''} retired. Train another at a Pyramid.`);renderHUD(true);return}\n   if(c==='shaper'){let n=0;")
# the AI trains the bearer it is shortest of, and leaves their jobs alone
rep("const want=civN('sower')<Math.min(ai.wantSow||4,Math.max(3,cap(k)-2))?'sower':",
    "const eg=EGY(k),tot=eg?civN('sower')+civN('grainb')+civN('waterb'):civN('sower'),pick=eg?[['waterb',1],['grainb',1.6],['sower',1.6]].sort((a,b)=>civN(a[0])/a[1]-civN(b[0])/b[1])[0][0]:'sower';const want=tot<Math.min((ai.wantSow||4)+(eg?2:0),Math.max(3,cap(k)-2))?pick:")
rep("(want==='sower'||S.res.wheat>U[want].cost.wheat+3)","(want!=='missionary'||S.res.wheat>U[want].cost.wheat+3)")
rep("{const P0=mine.filter(isSow),","if(!EGY(k)){const P0=mine.filter(isSow),")
# Egypt starts with one of each bearer
rep("S2.res.water=12}","S2.res.water=12;{const su=G.units.filter(u=>u.side===S2.side&&u.type==='sower');if(su[0])su[0].type='waterb';if(su[1])su[1].type='grainb';const h=S2.hall;if(h){G.units.push(makeUnit('sower',S2.side,h.x+1,h.y+2.6));let ok=0;for(let r=2;r<5&&!ok;r++)for(let k=0;k<16&&!ok;k++){const an=k/16*TAU+.6,x=Math.round(h.x+.5+Math.cos(an)*r),y=Math.round(h.y+.5+Math.sin(an)*r);if(canPlace(S2.side,'well',x,y).ok){const w=place(S2.side,'well',x,y);w.bp=w.bt||0;w.hp=w.max;ok=1}}}}}")
# 3D: the Grainbearer and Waterbearer share the Stonebearer's animation set
rep("FACT.adruid=function(){FACT.__up=1;","FACT.grainb=function(){FACT.__sbm='grainb';try{return FACT.stoneb()}finally{FACT.__sbm=null}};FACT.waterb=function(){FACT.__sbm='waterb';try{return FACT.stoneb()}finally{FACT.__sbm=null}};\nFACT.adruid=function(){FACT.__up=1;")
rep("const TYU=u=>u.type==='aged'?","const TYU=u=>(u.type==='grainb'||u.type==='waterb')?(window.MODELS&&window.MODELS[u.type]?TYPES[u.type]:null):u.type==='aged'?")
rep("return u.tgt?[['punch',.18,1]]:[['reap',.42,1]]}};","return u.tgt?[['punch',.18,1]]:[['reap',.42,1]]}};TYPES.grainb=Object.assign({},TYPES.stoneb,{f:'grainb'});TYPES.waterb=Object.assign({},TYPES.stoneb,{f:'waterb'});")
rep("if(ty.f==='stoneb')I.sb=","if(ty.f==='stoneb'||ty.f==='grainb'||ty.f==='waterb')I.sb=")
rep("if(u.type==='stoneb')return TYPES.stoneb.atk;","if(u.type==='stoneb'||(!u.work&&!u.tgt&&(u.type==='grainb'||u.type==='waterb')))return TYPES.stoneb.atk;")
rep("  if((u.type==='sower'||u.type==='stoneb'||u.type==='aged')&&R3D","  if((u.type==='sower'||u.type==='stoneb'||u.type==='aged'||u.type==='grainb'||u.type==='waterb')&&R3D")
rep("const GLAB=n=>({mh:{","const GLAB=n=>({mh:{grainb:1,waterb:1,")
open(F,'w').write(s);print('bearers ok',len(s))
