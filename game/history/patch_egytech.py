F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
# ---------- Egypt's own tech tree: bearers, stone & grain, water; no Mining (Stonebearers cut stone from the start) ----------
rep("  btower:{br:'Defenses',","  shaduf:{br:'Water',egy:1,name:'Shaduf',tier:1,cost:{wheat:8,stone:6},time:25,desc:'Waterbearers lift water with a counterweighted shaduf pole and fill their jars twice as fast.'},\n  cistern:{br:'Water',egy:1,name:'Cisterns',tier:2,req:'shaduf',cost:{stone:14,wheat:10},time:40,desc:'Every Pyramid and Temple allows 2 more Wells, so your people can grow larger.'},\n  btower:{br:'Defenses',")
rep("const TBR=['Sowers','Gathering','Army','Storage','Faith','Defenses','Navy'];","const TBR=['Sowers','Gathering','Water','Army','Storage','Faith','Defenses','Navy'];\nconst EREQ={tools:'quarry',quarry:null};const treq=(k,side)=>{const g=G&&G.S[side]?G.S[side].god:-1;return g===0&&k in EREQ?EREQ[k]:TECH[k].req};\nconst EBR={quarry:'Gathering',sandtrap:'Gathering'},tbr=(k,side)=>{const g=G&&G.S[side]?G.S[side].god:-1;return g===0&&EBR[k]?EBR[k]:TECH[k].br};\nconst brName=(br,side)=>{const g=G&&G.S[side]?G.S[side].god:-1;return g===0?({Sowers:'Bearers',Gathering:'Stone & Grain'}[br]||br):br};\nconst ETN={shape:['Flood Plains','When a Grainbearer has no wheat left to tend, it turns open land inside your farm rings into crop land and plants it.'],quarry:['Quarrying','Stonebearers raise fresh rock from open ground and spent rubble near your Pyramid and Temples, so the stone never runs out.'],swift:['Bearer\\u2019s Stride','All three bearers work twice as fast and walk 20% quicker.'],tools:['Copper Chisels','Stonebearers and Grainbearers cut stone and reap wheat 40% faster.'],veins:['Rich Veins','Every block of stone or sheaf of wheat a bearer takes has a 1 in 3 chance to give 2.'],bounty:['Gift of the Nile','The river\\u2019s silt feeds the fields: wheat ripens 40% faster.']};")
rep("const BRCOL={Sowers:'#8fdc6a',","const BRCOL={Water:'#5fb4e6',Sowers:'#8fdc6a',")
rep("if(S.tech[k]||(k==='mining'&&S.god===0))return{done:true};","if(k==='mining'&&S.god===0)return{hide:true};if(TECH[k].egy&&S.god!==0)return{hide:true};if(S.tech[k])return{done:true};")
rep("if(T.req&&!(k==='quarry'&&S.god===0)&&!S.tech[T.req])return{lock:`After ${techName(T.req,side)}`};","{const rq=treq(k,side);if(rq&&!S.tech[rq])return{lock:`After ${techName(rq,side)}`}}")
rep("function techName(k,side){const T=TECH[k],g=G.S[side]?G.S[side].god:-1;","function techName(k,side){const T=TECH[k],g=G.S[side]?G.S[side].god:-1;if(g===0&&ETN[k])return ETN[k][0];")
rep("function techDesc(k,side){const g=G.S[side]?G.S[side].god:-1;","function techDesc(k,side){const g=G.S[side]?G.S[side].god:-1;if(g===0&&ETN[k])return ETN[k][1];")
# the tree layout follows the per-faith prerequisites
i=s.index("function openTech(");j=s.index("\nfunction ",i+20);t=s[i:j]
t=t.replace("TECH[k].req?depth(TECH[k].req)+1:1","treq(k,0)?depth(treq(k,0))+1:1").replace("ks.filter(c=>TECH[c].req===k)","ks.filter(c=>treq(c,0)===k)").replace("ks.filter(k=>!TECH[k].req)","ks.filter(k=>!treq(k,0))").replace("q=TECH[k].req?pos[TECH[k].req]:{x:C,y:C}","q=treq(k,0)&&pos[treq(k,0)]?pos[treq(k,0)]:{x:C,y:C}").replace("${T.br} · Tier","${brName(tbr(k,0),0)} · Tier").replace("TECH[k].br===br","tbr(k,0)===br").replace("BRCOL[TECH[k].br]","BRCOL[tbr(k,0)]")
assert t.count("TECH[k].req")==0,t.count("TECH[k].req")
s=s[:i]+t+s[j:]
# effects
rep("u.wneed=2;u.wpT=G.t;u.dig=.3;","u.wneed=hasT(u.side,'shaduf')?1:2;u.wpT=G.t;u.dig=.3;")
rep("if(u.wp>=2){u.wp=0;u.carry={k:'water'","if(u.wp>=(hasT(u.side,'shaduf')?1:2)){u.wp=0;u.carry={k:'water'")
rep("let n=S&&S.hall?(S.tier>=2?6:4):0;for(const b of G.B)if(b.side===side&&b.type==='chapel'&&built(b))n+=b.temple?6:4;return n}","const cs=hasT(side,'cistern')?2:0;let n=S&&S.hall?(S.tier>=2?6:4)+cs:0;for(const b of G.B)if(b.side===side&&b.type==='chapel'&&built(b))n+=(b.temple?6:4)+cs;return n}")
# Egypt's AI studies in its own order
rep("for(const t of EGY(k)?['quarry','btower','bmortar',...AITECH]:AITECH)","for(const t of EGY(k)?['quarry','btower','shaduf','bmortar','shape','tools','cistern','granary','swift','rite1','drill','veins','bounty',...AITECH]:AITECH)")
open(F,'w').write(s);print('egypt tech ok')
s=open(F).read()
rep("      case 'shipatk':case 'shipsiege':case 'cannons':",r"""      case 'shaduf':{ctx.strokeStyle='#7a5634';ctx.lineWidth=2.4;ctx.lineCap='round';line(w/2-4,h-6,w/2-1,h-24);line(w/2-16,h-28,w/2+14,h-16);ctx.fillStyle='#8a7a68';ctx.beginPath();ctx.arc(w/2-15,h-27,3.4,0,TAU);ctx.fill();ctx.strokeStyle='#a3824f';ctx.lineWidth=1;line(w/2+13,h-16,w/2+13,h-9);ctx.fillStyle='#b8653a';ctx.fillRect(w/2+9,h-10,8,6);ctx.fillStyle='#5fb4e6';ctx.beginPath();ctx.ellipse(w/2+6,h-4,11,3,0,0,TAU);ctx.fill();break}
      case 'cistern':{ctx.fillStyle='#c9b38a';ctx.beginPath();ctx.ellipse(w/2,h-12,14,6,0,0,TAU);ctx.fill();ctx.fillRect(w/2-14,h-22,28,10);ctx.fillStyle='#dcc89e';ctx.beginPath();ctx.ellipse(w/2,h-22,14,6,0,0,TAU);ctx.fill();ctx.fillStyle='#4aa3d8';ctx.beginPath();ctx.ellipse(w/2,h-22,10,4,0,0,TAU);ctx.fill();ctx.fillStyle='#bfe6ff';ctx.beginPath();ctx.ellipse(w/2-3,h-23,4,1.4,0,0,TAU);ctx.fill();break}
      case 'quarry':{drawDep('rock',w/2,h-9,.5,40,0,0,0);ctx.strokeStyle='#5a4a3a';ctx.lineWidth=2;line(w/2+4,h-30,w/2+14,h-14);ctx.fillStyle='#c9c3bb';ctx.beginPath();ctx.moveTo(w/2,h-31);ctx.lineTo(w/2+10,h-29);ctx.lineTo(w/2+6,h-27);ctx.closePath();ctx.fill();break}
      case 'sandtrap':{ctx.fillStyle='#e0c58e';ctx.beginPath();ctx.ellipse(w/2,h/2+4,15,7,0,0,TAU);ctx.fill();ctx.fillStyle='#8a6a42';ctx.beginPath();ctx.ellipse(w/2,h/2+5,9,3.6,0,0,TAU);ctx.fill();ctx.strokeStyle='rgba(120,90,50,.6)';ctx.lineWidth=1;for(let i=0;i<3;i++){ctx.beginPath();ctx.ellipse(w/2,h/2+5,11+i*2,4.6+i,0,Math.PI*1.1,Math.PI*1.9);ctx.stroke()}break}
      case 'shipatk':case 'shipsiege':case 'cannons':""")
open(F,'w').write(s);print('tech icons ok')
