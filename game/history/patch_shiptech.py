F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
# ---------- transports start unarmed; two Navy researches arm them for battle, then for siege ----------
rep("const TBR=['Sowers','Gathering','Army','Storage','Faith','Defenses']","const TBR=['Sowers','Gathering','Army','Storage','Faith','Defenses','Navy']")
rep("Faith:null,Defenses:null};","Faith:null,Defenses:null,Navy:'#4aa3d8'};")
rep("  sandtrap:{br:'Sowers',","  shipatk:{br:'Navy',name:'Ship Archers',tier:1,cost:{wood:12,stone:8},time:35,desc:''},\n  shipsiege:{br:'Navy',name:'Ship Siege',tier:2,req:'shipatk',cost:{wood:20,stone:16},time:50,desc:''},\n  sandtrap:{br:'Sowers',")
rep("const FSHIP={8:['currach','sweeper'],0:['papyrus','solar'],1:['ferry','trireme']};","const FSHIP={8:['currach','sweeper'],0:['papyrus','solar'],1:['ferry','trireme']};\nconst SHIPTECH={8:['Sling Crews','Fire Arrows'],0:['Bow Crews','Fire Jars'],1:['Marines','Greek Fire']};")
rep("function techName(k,side){const T=TECH[k],g=G.S[side]?G.S[side].god:-1;","function techName(k,side){const T=TECH[k],g=G.S[side]?G.S[side].god:-1;if(k==='shipatk'||k==='shipsiege')return(SHIPTECH[g]||['Ship Archers','Ship Siege'])[k==='shipatk'?0:1];")
rep("function techDesc(k,side){const g=G.S[side]?G.S[side].god:-1;","function techDesc(k,side){const g=G.S[side]?G.S[side].god:-1;if(k==='shipatk'||k==='shipsiege'){const tn=SHIPK[(FSHIP[g]||['currach'])[0]].n,nm=techName(k,side);return k==='shipatk'?`Your ${tn} takes ${nm} aboard. It shoots at enemy troops and ships within 3\\u00bd squares, so it can fight its way to a landing.`:`Your ${tn} carries ${nm}: it bombards enemy buildings near the shore from 4\\u00bd squares for heavy damage. Pair it with a landing to break a rival\\u2019s coast.`}")
rep("function techState(side,k){const S=G.S[side],T=TECH[k];if(k==='cannons')return{hide:true};","function techState(side,k){const S=G.S[side],T=TECH[k];if(k==='cannons')return{hide:true};if((k==='shipatk'||k==='shipsiege')&&!S.tech[k]&&!(S.research&&S.research.k===k)&&!harborOf(side))return{lock:`Needs a ${BNm(side,'harbor')}`};")
rep("case 'cannons':put(","case 'shipatk':case 'shipsiege':case 'cannons':put(")
rep("const AITECH=['mining',","const AITECH=['shipatk','mining',")
rep("'bounty','veins','bmortar']","'bounty','veins','bmortar','shipsiege']")
# the transport's weapons
rep("function updShip(s,dt){\n  s.hurt=Math.max(0,s.hurt-dt);",r"""function updShip(s,dt){
  s.hurt=Math.max(0,s.hurt-dt);
  if(!SK(s).war){s.armed=hasT(s.side,'shipatk');
    if(hasT(s.side,'shipsiege')){s.scd=(s.scd||0)-dt;if(s.scd<=0){let tb=null,bd=4.6;for(const b of G.B){if(b.side===s.side||b.obst||b.type==='wall')continue;const d=distB(s.x,s.y,b);if(d<bd){bd=d;tb=b}}
      if(tb){s.scd=2.8;const g=G.S[s.side]?G.S[s.side].god:-1,col=g===1?'#ff7a2a':g===0?'#ffb04a':'#ff9a3a';const tx=bcx(tb),ty=bcy(tb);G.shots.push({lob:1,x0:s.x,y0:s.y,x1:tx,y1:ty,x:s.x,y:s.y,t:0,dur:1.1,h:2.6,r:.9,dmg:34,side:s.side,air:false,ground:false,bld:true,src:null,col});burst(s.x,s.y,[col,'#ffd27a','#fbf6ee'],6);if(g===1)G.fx.push({kind:'beam',x:s.x,y:s.y,x2:bcx(tb),y2:bcy(tb),z:WL+1,life:0,max:.35,col:'#ff7a2a'})}else s.scd=.5}}}""")
rep("if(s.armed){const WP=SK(s).war||{range:GUN.range,dmg:GUN.dmg,fr:GUN.fr,kind:'ball'};","if(s.armed){const WP=SK(s).war||{range:3.6,dmg:9,fr:1.1,kind:'arrows',noB:1};")
rep("if(!tg)for(const b of G.B){if(b.side===s.side||b.type==='wall')continue;const d=distB(s.x,s.y,b);if(d<bd){bd=d;tg=b}}","if(!tg&&!WP.noB)for(const b of G.B){if(b.side===s.side||b.type==='wall'||b.obst)continue;const d=distB(s.x,s.y,b);if(d<bd){bd=d;tg=b}}")
open(F,'w').write(s);print('ship tech ok')
