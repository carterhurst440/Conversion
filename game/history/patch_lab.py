import base64,re
F='tidebreak.html';s=open(F).read()
def rep(a,b,n=1):
    global s;c=s.count(a);assert c==n,(c,a[:90]);s=s.replace(a,b)
# 1) models
b64=lambda p:base64.b64encode(open(p,'rb').read()).decode()
rep("'};const L=new THREE.GLTFLoader();","',archer:'"+b64('glb/archer_g.glb')+"',vdruid:'"+b64('glb/elf_g.glb')+"',adruid:'"+b64('glb/aged_g.glb')+"'};const L=new THREE.GLTFLoader();")
# 2) factories (game copies of the lab factories)
fa=open('fact_archer.js').read();fv=open('fact_vdruid.js').read()
fac=fa+"\n"+fv+"\nFACT.adruid=function(){FACT.__up=1;try{return FACT.vdruid()}finally{FACT.__up=0}};\n"
rep("// ----- game driver","// ----- Celtic Archer and the Druid pair (Verdant / Aged), from the character labs\n"+fac+"// ----- game driver")
rep("const GLAB=n=>({mh:{combo:1,sphinx:1.25,ark:.95}[n],","const GLAB=n=>({mh:{combo:1,sphinx:1.25,ark:.95,archer:1,vdruid:1,adruid:1}[n],form:n==='adruid'?'up':'basic',")
# 3) render types
rep("TYPES.g0_0b=TYPES.g0_0;","Object.assign(TYPES,{carcher:{f:'archer',ps:50,vref:2.2,W:3.8,H:3.6,a:.24,cap:200,top:1.1,sh:9,atk:[['shot',.72,1],['shot',.72,1],['spray',.82,1]]},\n  cdruid:{f:'adruid',ps:50,vref:1.65,W:3.2,H:2.7,a:.22,cap:200,top:1.12,sh:9,atk:[['cast',.5,1]]},\n  cdruidb:{f:'vdruid',ps:50,vref:1.85,W:3,H:2.6,a:.22,cap:200,top:1.05,sh:9,atk:[['plant',.95,1],['reap',.42,1],['chop',.44,1]]}});TYPES.carcherb=TYPES.carcher;\nTYPES.g0_0b=TYPES.g0_0;")
# drive: power shot and thorn slam
rep("  if(ty.f==='sphinx'){if(u.skyT>0){",
    "  if(ty.f==='archer'){if(u.pwT>0){special=true;if(S.clip!=='power')c.playG('power',1,Math.max(0,3.0-u.pwT));S.hold=true}else if(S.clip==='power')S.hold=false;if(S.clip==='power')special=true}\n  if(ty.f==='adruid'){if(u.thT>0){special=true;if(S.clip!=='thorns')c.playG('thorns',1,Math.max(0,1.45-u.thT));S.hold=true}else if(S.clip==='thorns')S.hold=false;if(S.clip==='thorns')special=true}\n  if(ty.f==='sphinx'){if(u.skyT>0){")
# 4) units (lab roster for now; the Celtic roster rework will train them for real)
rep("Object.assign(U.g0_0,{bld:'hall',",
    "U.carcher={name:'Celtic Archer',role:'Holy ranged',hp:90,dmg:12,rate:.55,range:3.2,spd:2,house:1,cost:{wheat:6},time:20,bld:'none',lv:1,gu:true,god:8,item:'bow',hat:'none',hitsAir:true,special:'powershot',desc:'Smooth, grounded shots from the quiver to the cheek; every third shot she fans three arrows across the string and sprays up to three enemies. As the Archer Queen, every 12 seconds she springs high and hangs in the air for a Dead Eye shot, overdrawing while the green power of Cernunnos gathers, then looses a spirit arrow for 3\\u00bd\\u00d7 damage.'};\n"
    "U.cdruid={name:'Aged Druid',role:'Holy ranged',hp:180,dmg:16,rate:.75,range:2.8,spd:1.5,house:2,cost:{wheat:14},time:40,bld:'none',lv:1,gu:true,god:8,item:'staff',hat:'wreath',hitsAir:true,special:'thornslam',desc:'The Verdant Druid grown old and powerful, and he still plants, reaps and chops. Casts orbs of green power at range. Every 7 seconds he slams his palm to the earth and thorns burst up under up to 3 enemies, holding them for 2 seconds.'};\n"
    "Object.assign(U.g0_0,{bld:'hall',")
rep("const BATK={","U.carcherb=Object.assign({},U.carcher,{full:'carcher',basic:true,special:null});U.cdruidb=Object.assign({},U.cdruid,{name:'Verdant Druid',role:'Villager',full:'cdruid',basic:true,special:null,hp:40,dmg:2,rate:.4,range:.75,spd:1.7,house:1,hitsAir:false,desc:'The Celtic worker: plants and grows wheat and trees, reaps with a golden sickle and chops with a hatchet. Upgrades into the Aged Druid.'});\nconst LABX={8:['cdruid','carcher']};\nconst BATK={")
rep("GODS.forEach((gd,gi)=>group(`${gd.n} \\u00b7 ${gd.land}`,gd.col,[...(GUK[gi]||[]),'champ'+gi]));group('Basic',null,[...UORDER,...CIV]);\n  {const seen",
    "GODS.forEach((gd,gi)=>group(`${gd.n} \\u00b7 ${gd.land}`,gd.col,[...(LABX[gi]||[]),...(GUK[gi]||[]),'champ'+gi]));group('Basic',null,[...UORDER,...CIV]);\n  {const seen")
rep("const ACTIVE=[8,0,1],","const ACTIVE=[8,0,1],LABONLY=new Set(['carcher','cdruid']),")
# specials
rep("  if(sp==='swarmplague'){",
    "  if(sp==='powershot'){if(u.pwT>0){u.pwT-=dt;if(!u.pwF&&u.pwT<=3.0-2.0){u.pwF=1;const v=u.pwTg&&u.pwTg.hp>0?u.pwTg:null;if(v){G.shots.push({x:u.x,y:u.y,z:hT(u.x,u.y)+1.2,tgt:v,dmg:U[u.type].dmg*3.5,spd:16,kind:'arrow',side:u.side,src:u,col:'#4fd84a',power:1});burst(u.x,u.y,['#4fd84a','#a8f07a','#e9ffd0'],12)}}return true}\n"
    "    u.psT=(u.psT==null?3:u.psT)-dt;if(u.psT>0)return false;let v=null,bd=U[u.type].range+.5;for(const e of G.units){if(!foeOf(u,e))continue;const d=Math.hypot(e.x-u.x,e.y-u.y);if(d<bd){bd=d;v=e}}if(!v){u.psT=.5;return false}\n"
    "    u.psT=12;u.pwT=3.0;u.pwF=0;u.pwTg=v;face(u,v.x,v.y);float(u.x,u.y,'Dead Eye','#3fa83a');ring(u.x,u.y,.7,'#4fd84a');return true}\n"
    "  if(sp==='thornslam'){if(u.thT>0){u.thT-=dt;if(!u.thF&&u.thT<=1.45-.6){u.thF=1;const fs=G.units.filter(e=>foeOf(u,e)&&!U[e.type].air&&Math.hypot(e.x-u.x,e.y-u.y)<3.2).sort((a,b)=>Math.hypot(a.x-u.x,a.y-u.y)-Math.hypot(b.x-u.x,b.y-u.y)).slice(0,3);\n"
    "      for(const e of fs){e.root=2;damageUnit(e,22,u);G.vines.push({x:e.x,y:e.y,t:0,e});G.fx.push({kind:'rootline',flat:true,x:u.x,y:u.y,x2:e.x,y2:e.y,life:0,max:.7});burst(e.x,e.y,['#4f7a2c','#a8f07a','#8a6a48'],8)}if(fs.length){float(u.x,u.y,'Thorns!','#3f8a2c');ring(u.x,u.y,.6,'#6f9e4c')}}return true}\n"
    "    u.tsT=(u.tsT==null?2.5:u.tsT)-dt;if(u.tsT>0)return false;if(!G.units.some(e=>foeOf(u,e)&&!U[e.type].air&&Math.hypot(e.x-u.x,e.y-u.y)<3.2)){u.tsT=.5;return false}u.tsT=7;u.thT=1.45;u.thF=0;return true}\n"
    "  if(sp==='swarmplague'){")
# glowing power arrow
rep("    const[px,py]=pj(s.x,s.y,s.z);if(!onScreen(px,py))continue;\n","    const[px,py]=pj(s.x,s.y,s.z);if(!onScreen(px,py))continue;if(s.power){glow(px,py,15*Z,'#4fd84a',.7);glow(px,py,6*Z,'#e9ffd0',.85)}\n")
# 5) no external labs: the Movement Lab in this file is the master copy
a=s.index('    <details class="rules labs"><summary>Character labs</summary>');e=s.index('</div></details>',a)+len('</div></details>')
s=s[:a]+s[e:]
open(F,'w').write(s);print('lab ok',len(s))
s=open(F).read()
# upgraded units glow softly in their god's colour (aura behind the body + a faint tint on 3D models)
rep("function drawUnit(u,s){\n  let[sx,sy]=unitScreen(u);const fl=scrFl(u.fx,u.fy),t=U[u.type];",
    "const UPG=t=>!!(t&&t.gu&&!t.basic&&U[(t.key||'')+'b'])||!!(t&&t.gu&&!t.basic&&t.awaken);\nfunction drawUnit(u,s){\n  let[sx,sy]=unitScreen(u);const fl=scrFl(u.fx,u.fy),t=U[u.type];\n  if(!u.hid&&!u.leap&&!t.air&&(UPG(t)||(t.gu&&!t.basic&&U[u.type+'b']))&&t.god!=null){const big=t.siege||t.body==='beast'||t.body==='serpent'||(t.scale||1)>1.2||(t.house||1)>=3,pu=.5+.5*Math.sin(time*2.2+(u.ph||0)),rx=(big?15:9.5)*s,ry=(big?6.4:4.2)*s;ctx.save();ctx.globalCompositeOperation='lighter';const gc=GODS[t.god].col;for(const[w,a]of[[7,.18],[4,.3],[1.8,.75]]){ctx.strokeStyle=hexA(gc,a*(.75+.25*pu));ctx.lineWidth=w*Math.max(.7,s);ctx.beginPath();ctx.ellipse(sx,sy,rx,ry,0,0,TAU);ctx.stroke()}ctx.fillStyle=hexA(gc,.12+.06*pu);ctx.beginPath();ctx.ellipse(sx,sy,rx,ry,0,0,TAU);ctx.fill();ctx.restore()}")
rep("try{c.tick(dt,I)}catch(e){console.warn('R3D tick',e);failed=true}}",
    "try{c.tick(dt,I)}catch(e){console.warn('R3D tick',e);failed=true}}")
open(F,'w').write(s);print('glow ok')

s=open(F).read()
rep("SPNAME={swarmplague:'Plague Swarm',","SPNAME={powershot:'Dead Eye',thornslam:'Thorns',swarmplague:'Plague Swarm',")
open(F,'w').write(s);print('names ok')
s=open(F).read()
# the Nubian Warrior's basic form gets its own model; the current model is now the upgraded form
rep("',archer:'","',ewarb:'"+b64('glb/nub_basic_g.glb')+"',archer:'")
rep("const LAB=GLAB('combo');const G0=window.MODELS.ewar;","const LAB=GLAB('combo');const G0=(FACT.__nb===1&&window.MODELS.ewarb)||window.MODELS.ewar;")
rep("FACT.adruid=function(){","FACT.combob=function(){FACT.__nb=1;try{return FACT.combo()}finally{FACT.__nb=0}};\nFACT.adruid=function(){")
rep("TYPES.g0_0b=TYPES.g0_0;","TYPES.g0_0b=Object.assign({},TYPES.g0_0,{f:'combob'});")
rep("const GLAB=n=>({mh:{combo:1,","const GLAB=n=>({mh:{combob:1,combo:1,")
open(F,'w').write(s);print('nubian basic ok')
s=open(F).read()
import re as _re
m=_re.search(r"ewar:'[A-Za-z0-9+/=]+'",s);assert m
s=s[:m.start()]+"ewar:'"+b64('glb/nub_up_g.glb')+"'"+s[m.end():]
open(F,'w').write(s);print('nubian queen ok')

s=open(F).read()
rep("U.carcher={name:'Celtic Archer',role:'Holy ranged',","U.carcher={name:'Celtic Archer',role:'Holy ranged',spray3:1,")
x="else if(t.range>1.2)G.shots.push({x:u.x,y:u.y,z:hT(u.x,u.y)+(t.air?2.4:1.2),tgt:v,"
assert s.count(x)==1
s=s.replace(x,"else if(t.spray3&&((u.shN=(u.shN||0)+1)%3===0)){const fs=G.units.filter(e=>foeOf(u,e)&&Math.hypot(e.x-u.x,e.y-u.y)<t.range+1).sort((a,b)=>Math.hypot(a.x-u.x,a.y-u.y)-Math.hypot(b.x-u.x,b.y-u.y)).slice(0,3);while(fs.length<3)fs.push(v);for(const e of fs)G.shots.push({x:u.x,y:u.y,z:hT(u.x,u.y)+1.2,tgt:e,dmg:t.dmg*.8,spd:11,kind:'arrow',side:u.side,src:u,col:holyCol(t)});float(u.x,u.y,'Spray','#6f9e4c')}\n  "+x)
open(F,'w').write(s);print('spray ok')
