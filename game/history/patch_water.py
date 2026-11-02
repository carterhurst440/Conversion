F='tidebreak.html';s=open(F).read()
def rep(a,b,n=1):
    global s;c=s.count(a);assert c==n,(c,a[:90]);s=s.replace(a,b)
# ---------- three faiths only: Cernunnos (Celtic), Anubis (Egypt), Hades (Greece) ----------
rep("const GUK=[];GU.forEach(","for(let g=0;g<GU.length;g++)if(![0,1,8].includes(g))GU[g]=[];\nconst GUK=[];GU.forEach(")
rep("const BLESS={","const BLESS0={")
i=s.index("const BLESS0={");j=s.index("\n};",i)+3
s=s[:j]+"\nconst BLESS={};for(const g of[0,1,8])if(BLESS0[g])BLESS[g]=BLESS0[g];"+s[j:]
s=s.replace("GODS.forEach((gd,gi)=>group(","GACT((gd,gi)=>group(")
rep("  GODS.forEach((g,k)=>{const taken=","  GACT((g,k)=>{const taken=")
# ---------- water: Egypt's third resource, drawn from Wells, needed to train every Egyptian unit ----------
rep("const RES=['wood','stone','wheat','souls'];","const RES=['wood','stone','wheat','water','souls'];")
rep("const MATCOL={wood:'#a87650',","const MATCOL={water:'#4aa3d8',wood:'#a87650',")
rep("const RESLV={wood:1,","const RESLV={water:1,wood:1,")
s=s.replace("res:{wood:4,stone:0,clay:0,wheat:6,souls:0}","res:{wood:4,stone:0,clay:0,wheat:6,water:0,souls:0}")
s=s.replace("res:{wood:0,stone:0,clay:0,wheat:0,souls:0}","res:{wood:0,stone:0,clay:0,wheat:0,water:0,souls:0}")
rep("  {const cw=$('c-wood');if(cw){const hd=EGY(0)?'none':'';if(cw.style.display!==hd)cw.style.display=hd}}",
    "  {const cw=$('c-wood');if(cw){const hd=EGY(0)?'none':'';if(cw.style.display!==hd)cw.style.display=hd}const cq=$('c-water');if(cq){const hd=EGY(0)?'':'none';if(cq.style.display!==hd)cq.style.display=hd}}")
rep("U.g0_2.cost={wheat:30};U.g0_3.cost={wheat:50};","U.g0_2.cost={wheat:30,water:12};U.g0_3.cost={wheat:50,water:20};")
rep("Object.assign(U.g0_0,{bld:'hall',cost:{wheat:10},","Object.assign(U.g0_0,{bld:'hall',cost:{wheat:10,water:4},")
rep("Object.assign(U.g0_1,{bld:'wabet',time:50,cost:{wheat:22}});","Object.assign(U.g0_1,{bld:'wabet',time:50,cost:{wheat:22,water:8}});")
rep("if(c.egw&&o.wheat)o.wheat=Math.round(o.wheat*c.egw);","if(c.egw&&o.wheat){o.wheat=Math.round(o.wheat*c.egw);o.water=Math.max(1,Math.round(o.wheat*.4))}")
# the job
rep("function walkTo(u,j,dt){",r"""function waterTick(u,dt){
  if(u.carry&&(u.carry.k!=='water'||u.carry.n>=CARRY||u.dropping)){u.dropping=true;if(deliver(u,dt))return true;u.dropping=false}
  if(!u.carry)u.dropping=false;let w=u.wellB;
  if(!w||!G.B.includes(w)||!built(w)){w=null;let bd=1e9;const i0=isl[cellAt(u.x,u.y)];for(const b of G.B){if(b.side!==u.side||b.type!=='well'||!built(b)||isl[idx(b.x,b.y)]!==i0)continue;const n=G.units.filter(v=>v!==u&&v.wellB===b).length,d=Math.hypot(b.x+.5-u.x,b.y+.5-u.y)+n*2;if(d<bd){bd=d;w=b}}u.wellB=w;u.wt=null;
    if(!w){if(u.carry){u.dropping=true;return true}if(!u.wWarn&&u.side===0){u.wWarn=1;float(u.x,u.y,'Dig a Well first','#3d7fa8')}return false}}
  if(u.wt==null){let best=-1,bd=1e9;for(const[a,c]of[[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]){const x=w.x+a,y=w.y+c;if(!inb(x,y))continue;const i=idx(x,y);if(!land[i]||cells[i])continue;const d=Math.hypot(x+.5-u.x,y+.5-u.y);if(d<bd){bd=d;best=i}}if(best<0)return false;u.wt=best;u.wp=0;u.path=[];u.plan=0}
  if(!walkTo(u,u.wt,dt))return true;face(u,w.x+.5,w.y+.5);u.wp+=dt;u.wneed=2;u.wpT=G.t;u.dig=.3;if((u.dg=(u.dg||0)-dt)<=0){u.dg=.6;u.sw=1;burst(w.x+.5,w.y+.5,['#7fc4ea','#bfe6ff','#4aa3d8'],3)}
  if(u.wp>=2){u.wp=0;u.carry={k:'water',n:(u.carry&&u.carry.k==='water'?u.carry.n:0)+1};if(u.carry.n>=CARRY)u.dropping=true}return true}
function walkTo(u,j,dt){""")
rep("  if(u.work==='farm'||u.work==='forest'||u.work==='mine'){if(comboTick(u,dt))return}","  if(u.work==='water'){if(waterTick(u,dt))return}else if(u.work==='farm'||u.work==='forest'||u.work==='mine'){if(comboTick(u,dt))return}")
rep("function setWork(u,w,x,y,shape){u.sect=null;","function setWork(u,w,x,y,shape){u.sect=null;u.wellB=null;")
rep("[['farm','Farm'],['forest',EGY(0)?'Forage':'Forest'],...(hasT(0,'mining')?[['mine','Mine']]:[])]",
    "(EGY(0)?[['farm','Farm'],['water','Water'],['mine','Stone']]:[['farm','Farm'],['forest','Forest'],...(hasT(0,'mining')?[['mine','Mine']]:[])])",2)
rep("if(c==='chop'||c==='reap'||c==='mine'||c==='farm'||c==='forest'||c==='quarry'){","if(c==='chop'||c==='reap'||c==='mine'||c==='farm'||c==='forest'||c==='quarry'||c==='water'){")
rep("forest:'Forestry: chopping trees and planting new ones.',","forest:'Forestry: chopping trees and planting new ones.',water:'Drawing water from the Wells and carrying it to the Pyramid.',")
rep("{chop:'Chop',reap:'Reap',mine:'Mine',farm:'Farm',forest:'Forest',quarry:'Quarry'}[j]","{chop:'Chop',reap:'Reap',mine:'Mine',farm:'Farm',forest:'Forest',quarry:'Quarry',water:'Water'}[j]")
# AI
rep("const want=EGY(k)?{farm:2+Math.floor(lv/2),forest:1+Math.floor(lv/3),mine:2+Math.floor(lv/2)}:","const want=EGY(k)?{farm:2+Math.floor(lv/2),forest:0,mine:2+Math.floor(lv/2),water:1+Math.floor(lv/2)}:")
rep("for(const j of S.res.stone<12&&want.mine?['farm','mine','forest']:['farm','forest','mine']){","for(const j of S.res.stone<12&&want.mine?['farm','mine','forest','water']:['farm','forest','mine','water']){if(!want[j])continue;")
# Egypt's rule text
rep("Every Egyptian troop costs about twice the wheat.","Every Egyptian troop costs about twice the wheat, plus water drawn from the Wells.")
rep("Stonebearers farm wheat, forage berries in the woods and quarry stone from day one.","Stonebearers farm wheat, quarry stone and draw water from the Wells.")
# ---------- canals: a thin blue channel winding from every Well to its nearest Pyramid ----------
rep("  for(const pl of G.pools){if(!seeAt(pl.x,pl.y))continue;",r"""  for(const b of G.B){if(b.type!=='well'||!built(b)||!(b.side===0||b.seen))continue;let py=null,bd=1e9;for(const h of G.B){if(h.side!==b.side||(h.type!=='hall'&&h.type!=='chapel'))continue;const hx=h.x+(h.type==='hall'?1:.5),hy=h.y+(h.type==='hall'?1:.5),d=Math.hypot(hx-b.x-.5,hy-b.y-.5);if(d<bd){bd=d;py=[hx,hy]}}if(!py)continue;
    const x0=b.x+.5,y0=b.y+.5,dx=py[0]-x0,dy=py[1]-y0,L=Math.hypot(dx,dy)||1,nx=-dy/L,ny=dx/L,sd=(b.seed||.3)*9,pts=[];for(let k=0;k<=18;k++){const t=k/18,e=Math.min(t,.86)/.86,w=Math.sin(t*Math.PI*2.2+sd)*.28*Math.sin(Math.PI*Math.min(1,e)),x=x0+dx*e+nx*w,y=y0+dy*e+ny*w;pts.push(pj(x,y,hT(x,y)))}
    if(!pts.some(p=>onScreen(p[0],p[1])))continue;ctx.save();ctx.lineCap='round';ctx.lineJoin='round';const path=()=>{ctx.beginPath();ctx.moveTo(pts[0][0],pts[0][1]);for(let k=1;k<pts.length;k++)ctx.lineTo(pts[k][0],pts[k][1])};
    path();ctx.strokeStyle='rgba(122,92,52,.45)';ctx.lineWidth=4.6*Z;ctx.stroke();path();ctx.strokeStyle='#3d8fc4';ctx.lineWidth=2.8*Z;ctx.stroke();path();ctx.strokeStyle='rgba(190,235,255,.85)';ctx.lineWidth=1*Z;ctx.setLineDash([3*Z,7*Z]);ctx.lineDashOffset=-time*14*Z;ctx.stroke();ctx.restore()}
  for(const pl of G.pools){if(!seeAt(pl.x,pl.y))continue;""")
open(F,'w').write(s);print('water ok',len(s))
s=open(F).read()
rep("for(const S2 of G.S)if(S2.god===0){S2.res.stone+=S2.res.wood+4;S2.res.wood=0}","for(const S2 of G.S)if(S2.god===0){S2.res.stone+=S2.res.wood+4;S2.res.wood=0;S2.res.water=12}")
rep("for(const j of S.res.stone<12&&want.mine?['farm','mine','forest','water']:['farm','forest','mine','water']){","for(const j of EGY(k)?['water','farm','mine']:S.res.stone<12&&want.mine?['farm','mine','forest','water']:['farm','forest','mine','water']){")
open(F,'w').write(s);print('water2 ok')
s=open(F).read()
# ---------- two defenses per faith: a long-range single-target tower and a short-range splash ----------
rep("if(!S||b.bless!=null||!S.tech||!S.tech['b'+b.type]||","if(!S||b.bless!=null||!S.tech||!(S.tech['b'+b.type]||b.type==='tower'||b.type==='mortar')||")
rep("const BLESS={};for(const g of[0,1,8])if(BLESS0[g])BLESS[g]=BLESS0[g];",
    "const BLESS={};for(const g of[0,1,8])if(BLESS0[g])BLESS[g]=BLESS0[g];for(const g of[0,1,8]){BLESS[g].tower.desc+=' Long range: picks off one target at a time.';BLESS[g].mortar.desc+=' Short range: hits everything in the blast.'}")
rep("tower:[2,4,4,4,4],cannon:[1,2,2,2,2],mortar:[0,1,1,1,1]","tower:[2,4,4,4,4],cannon:[0,0,0,0,0],mortar:[1,2,3,3,3]")
rep("['Defend',['tower','cannon','mortar','wall']]","['Defend',['tower','mortar','wall']]",2)
rep("function BD(side,k){const D=B[k];","function BD(side,k){const D=B[k];{const g=G.S[side]?G.S[side].god:-1;if((k==='tower'||k==='mortar')&&BLESS[g]&&BLESS[g][k])return Object.assign({},D,BLESS[g][k])}")
rep("t.appendChild(bldIcon(k));","t.appendChild(bldIcon(k,(k==='tower'||k==='mortar')&&BLESS[S.god]&&BLESS[S.god][k]?S.god:undefined));")
rep("const GUN={range:4.6,","B.tower.range=6;B.tower.fr=1;B.mortar.range=3.4;B.mortar.min=0;B.mortar.fr=.45;B.mortar.splash=1.4;\nconst GUN={range:4.6,")
open(F,'w').write(s);print('defenses ok')
