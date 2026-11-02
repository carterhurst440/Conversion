F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a)
    assert c==n,(c,a[:90])
    s=s.replace(a,b)

# ---------- Warriors and Archers are gone; each faith's first troop trains at its barracks ----------
rep("const UORDER=['warrior','archer','ram'],","const UORDER=['ram'],")
rep("const CHIPS=['sower','missionary','warrior','archer','ram'];","const CHIPS=['sower','missionary','ram'];")
rep("Object.assign(U.g0_0,{bld:'hall',","U.g8_0.bld='barracks';U.g1_0.bld='barracks';Object.assign(U.g0_0,{bld:'hall',")
rep("b.type==='barracks'?UORDER.filter(k=>U[k].bld==='barracks'||U[k].alt==='barracks'):b.type==='altar'?gk('altar')",
    "b.type==='barracks'?[...gk('barracks'),...UORDER.filter(k=>U[k].bld==='barracks'||U[k].alt==='barracks')]:b.type==='altar'?gk('altar')")
rep("barracks:{name:'Barracks',hp:340,cost:{wood:60},desc:'Trains Warriors, Archers and Rams, one at a time. More ",
    "barracks:{name:'Barracks',hp:340,cost:{wood:60},desc:'Trains your faith\\u2019s frontline troop and Rams, one at a time. More ")
# army research now speeds every troop; archery research removed
rep("drill:{br:'Warriors',","drill:{br:'Army',")
rep("march:{br:'Warriors',","march:{br:'Army',")
rep("desc:'Warriors move 20% faster.'","desc:'Every troop moves 20% faster.'")
rep("desc:'Warriors move another 20% faster.'","desc:'Every troop moves another 20% faster.'")
rep("const TBR=['Sowers','Gathering','Warriors','Archers','Storage','Faith','Defenses'","const TBR=['Sowers','Gathering','Army','Storage','Faith','Defenses'")
rep("Warriors:'#e8735a',Archers:'#f2c14e',","Army:'#e8735a',")
rep("'drill','longbow','rite1',","'drill','rite1',")
rep("'march','eagle','vaults',","'march','vaults',")
rep("(u.type==='warrior'?1+.2*((G.S[u.side]&&G.S[u.side].drill)||0):1)","(!U[u.type].civ?1+.2*((G.S[u.side]&&G.S[u.side].drill)||0):1)")
# codex / mechanics lists
rep("{key:'base',title:'Common troops',sub:'Warriors, Archers and Rams train at the Barracks.',units:['warrior','archer','ram']}",
    "{key:'base',title:'Common troops',sub:'Rams train at the Barracks, beside each faith\\u2019s frontline troop. Rams are the only troop that breaks walls.',units:['ram']}")
rep("barracks:['warrior','archer','ram'],altar:GUK[g],","barracks:[...GUK[g].filter(k=>U[k].bld==='barracks'),'ram'],altar:GUK[g].filter(k=>U[k].bld==='altar'),")
rep("['warrior','barracks'],['archer','barracks'],['ram','barracks'],...GUK[g].map(k=>[k,'altar'])","['ram','barracks'],...GUK[g].map(k=>[k,U[k].bld])")
rep("Barracks (any time) train Warriors, Archers and Rams.","Barracks (any time) train your faith’s frontline troop and Rams.")
rep("UP={sower:['mining','tools','veins','shape','quarry','swift','bounty'],warrior:['drill','march'],archer:['longbow','eagle'],",
    "UP={sower:['mining','tools','veins','shape','quarry','swift','bounty'],ram:['drill','march'],")

# ---------- faith names ----------
rep("const EGY=side=>",
r"""const FNAMES={
 8:{hall:'Nemeton',halls:'Nemetons',temple:'Great Nemeton',temples:'Great Nemetons',barracks:'Dún',storehouse:'Souterrain',storehouses:'Souterrains',altar:'Dolmen',altars:'Dolmens',veil:'Sídhe Mound',sower:'Crofter',sowers:'Crofters'},
 0:{hall:'Pyramid',halls:'Pyramids',temple:'Great Pyramid',temples:'Great Pyramids',sower:'Stonebearer',sowers:'Stonebearers'},
 1:{sower:'Shade',sowers:'Shades'}};
const FDEF={hall:'Church',halls:'Churches',temple:'Temple',temples:'Temples',barracks:'Barracks',storehouse:'Storehouse',storehouses:'Storehouses',altar:'Altar',altars:'Altars',veil:'Veil',sower:'Sower',sowers:'Sowers'};
const FN=(g,k)=>(FNAMES[g]&&FNAMES[g][k])||FDEF[k];
const FWORDS=[['Churches','halls'],['Church','hall'],['Temples','temples'],['Temple','temple'],['Storehouses','storehouses'],['Storehouse','storehouse'],['Barracks','barracks'],['Altars','altars'],['Altar','altar'],['Veil','veil'],['Sowers','sowers'],['Sower','sower']];
const FRX=FWORDS.map(([w,k])=>[new RegExp('\\b'+w+'\\b','g'),k]);
function FXg(g,str){if(!FNAMES[g]||typeof str!=='string')return str;const ph=[];let o=str;FRX.forEach(([rx,k],i)=>{o=o.replace(rx,()=>{ph.push(FN(g,k));return'\u0001'+(ph.length-1)+'\u0002'})});return o.replace(/\u0001(\d+)\u0002/g,(m,i)=>ph[+i])}
const playerGod=()=>typeof G!=='undefined'&&G&&G.S&&G.S[0]?G.S[0].god:PICKGOD;
const FX=str=>FXg(playerGod(),str);
let NAMEG=null,FORIG=null;
function applyNames(g){if(!FORIG){FORIG={B:{},U:{},T:{}};for(const k in B)FORIG.B[k]={name:B[k].name,desc:B[k].desc};for(const k in U)FORIG.U[k]={name:U[k].name,desc:U[k].desc};for(const k in TECH)FORIG.T[k]={name:TECH[k].name,desc:TECH[k].desc}}
  NAMEG=g;for(const k in FORIG.B){B[k].name=FXg(g,FORIG.B[k].name);B[k].desc=FXg(g,FORIG.B[k].desc)}for(const k in FORIG.U){if(!U[k])continue;U[k].name=FXg(g,FORIG.U[k].name);U[k].desc=FXg(g,FORIG.U[k].desc)}for(const k in FORIG.T){TECH[k].name=FXg(g,FORIG.T[k].name);TECH[k].desc=FXg(g,FORIG.T[k].desc)}
  const nm=FN(g,'hall');B.hall.name=nm;B.chapel.name=nm;
  if(g===8){B.barracks.desc='The war-hall of the clan. Trains Rootbound Druids and Rams, one at a time. More Dún train more at once. Build it any time.';B.storehouse.desc='An earth-cut store under the turf. A drop-off and a new farm ring: Crofters can work within 4½ squares of it and bring their goods here, so dig them out where the resources are. Goods stored here are lost to raiders if it falls.'}
  {const el=document.querySelector('#ch-sower b');if(el)el.textContent=U.sower.name;const e2=document.getElementById('ch-sower');if(e2)e2.setAttribute('aria-label',U.sower.name)}}
const BNm=(side,k)=>{const g=G.S[side]?G.S[side].god:-1;if(k==='hall'||k==='chapel')return FN(g,'hall');return FORIG&&FORIG.B[k]?FXg(g,FORIG.B[k].name):B[k].name};
const EGY=side=>""")
# keep names in sync with the player's faith
rep("function toast(m,bad){const t=$('toast');t.textContent=m;","function toast(m,bad){m=FX(m);const t=$('toast');t.textContent=m;")
rep("  {const cw=$('c-wood');","  if(G&&G.S&&G.S[0]&&NAMEG!==G.S[0].god)applyNames(G.S[0].god);\n  {const cw=$('c-wood');")
rep("function renderGodPick(){const el=$('gpick');if(!el)return;","function renderGodPick(){const el=$('gpick');if(!el)return;applyNames(PICKGOD);")
# panel funnel
import re
m=re.search(r"function setPanel\((\w+)\)\{",s);assert m
s=s.replace(m.group(0),m.group(0)+m.group(1)+"=FX("+m.group(1)+");",1)
# hall / temple names
rep("function hallName(k){const S=G.S[k];if(S.god===0)return S.tier>=2?'Great Pyramid of Anubis':'Pyramid of Anubis';return ",
    "function hallName(k){const S=G.S[k];if(FNAMES[S.god]&&FNAMES[S.god].hall)return `${S.tier>=2?FN(S.god,'temple'):FN(S.god,'hall')} of ${GODS[S.god].n}`;return ")
rep("${EGY(0)?(S.tier>=2?'Great Pyramid':'Pyramid'):S.tier>=2?'Temple':'Church'} \\u00b7 army",
    "${S.tier>=2?FN(S.god,'temple'):FN(S.god,'hall')} \\u00b7 army")
rep("<span>\\u2191 ${EGY(0)?'Gold cap':'Temple'}</span>","<span>\\u2191 ${EGY(0)?'Gold cap':FN(G.S[0].god,'temple')}</span>")
rep("b.type==='chapel'&&b.temple?'Temple':D.name}","b.type==='chapel'&&b.temple?FN(G.S[b.side].god,'temple'):mine?D.name:BNm(b.side,b.type)}")
# welcome screen: per-faith building chips and a names line
rep("<i>${{hall:EGY(0)||k===0?'Pyramid':'Church',wabet:'Wabet',altar:'Altar'}[U[key].bld]||'Altar'}</i>",
    "<i>${{hall:FN(k,'hall'),wabet:'Wabet',altar:FN(k,'altar'),barracks:FN(k,'barracks')}[U[key].bld]||FN(k,'altar')}</i>")
rep("      d.insertAdjacentHTML('beforeend','<h4>Faith troops</h4>');",
    "      d.insertAdjacentHTML('beforeend',`<p class=\"eco\"><b>Workers:</b> ${FN(k,'sowers')} \\u00b7 <b>House of faith:</b> ${FN(k,'hall')} \\u2192 ${FN(k,'temple')}${k===0?'':` \\u00b7 <b>War-hall:</b> ${FN(k,'barracks')} \\u00b7 <b>Store:</b> ${FN(k,'storehouse')}`} \\u00b7 <b>Altar:</b> ${FN(k,'altar')} \\u00b7 <b>Gate:</b> ${FN(k,'veil')}</p>`);\n      d.insertAdjacentHTML('beforeend','<h4>Faith troops</h4>');")
# Egypt's own text used 'Sowers'
rep("Sowers farm wheat, forage berries in the woods and quarry stone from day one.","Stonebearers farm wheat, forage berries in the woods and quarry stone from day one.")
open(F,'w').write(s);print('names ok',len(s))
s=open(F).read()
rep("${locked?(k==='veil'?'Needs Altar':EGY(0)?'Needs Great Pyramid':'Needs Temple')","${locked?'Needs '+(k==='veil'?FN(S.god,'altar'):FN(S.god,'temple'))")
open(F,'w').write(s);print('needs ok')
s=open(F).read()
rep("const want=civN('sower')<(ai.wantSow||4)?'sower':","const want=civN('sower')<Math.min(ai.wantSow||4,Math.max(3,cap(k)-2))?'sower':")
open(F,'w').write(s);print('ai ok')
