F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
# ---------- no Missionary for Egypt (each unit will level up its own way) ----------
rep("&&!(U[k].egonly&&S.god!==0))}","&&!(U[k].egonly&&S.god!==0)&&!(k==='missionary'&&S.god===0))}")
rep("cap(k)>=15&&civN('missionary')<1&&G.t>200?'missionary'","!eg&&cap(k)>=15&&civN('missionary')<1&&G.t>200?'missionary'")
# ---------- worker icons (Train menu and bottom bar) use the 3D rigs ----------
rep("  if(k==='ram')drawRam(u,w/2,h-12*sc,.95*sc,1,0);","  if(['sower','grainb','waterb','aged','stoneb'].includes(k)&&R3D&&R3D.draw(u,w/2,h-3,sc*1.05,1))return;\n  if(k==='ram')drawRam(u,w/2,h-12*sc,.95*sc,1,0);")
rep("function uIconURL(k){return UIURL[k]||(UIURL[k]=unitIcon(k,44,48).toDataURL())}",
    "const iconVer=k=>{const g=playerGod(),m=window.MODELS||{},key=k==='sower'?(g===0?'stoneb':g===8?'vdruid':''):k==='aged'?'adruid':(k==='grainb'||k==='waterb')?k:'';return key&&m[key]?'3'+g:'2'+g};\nfunction uIconURL(k){const v=k+iconVer(k);return UIURL[v]||(UIURL[v]=unitIcon(k,44,48).toDataURL())}")
rep("  for(const k of CHIPS){const n=mine.filter(u=>baseOf(u.type)===k).length,el=$('cn-'+k);",
    "  for(const k of CHIPS){const n=mine.filter(u=>baseOf(u.type)===k).length,el=$('cn-'+k);{const bt=el.parentElement,v=iconVer(k);if(n&&bt.dataset.v!==v){bt.dataset.v=v;const cv=bt.querySelector('canvas');if(cv)bt.replaceChild(unitIcon(k,42,50),cv)}}")
open(F,'w').write(s);print('icons ok')
s=open(F).read()
rep("if(!wild)list0.push(...CIV.filter(k=>U[k].bld!=='upgrade'));","if(!wild)list0.push(...CIV.filter(k=>U[k].bld!=='upgrade'&&!(U[k].egonly&&S.god!==0)&&!(k==='missionary'&&S.god===0)));")
rep("  if(['sower','grainb','waterb','aged','stoneb'].includes(k)&&R3D&&R3D.draw(u,w/2,h-3,sc*1.05,1))return;",
    "  if(['sower','grainb','waterb','aged','stoneb'].includes(k)&&R3D&&iconVer(k)[0]==='3'){R3D.draw(u,w/2,h-3,sc*1.05,1);ctx.clearRect(0,0,w,h);if(R3D.draw(u,w/2,h-3,sc*1.05,1))return}")
open(F,'w').write(s);print('train list ok')
s=open(F).read()
rep("const tt=c.firstChild;tt.appendChild(unitIcon(k));","const tt=c.firstChild;tt.appendChild(unitIcon(k));if(['sower','grainb','waterb','aged'].includes(k))for(const ms of[250,900])setTimeout(()=>{const cv=tt.querySelector('canvas');if(cv&&cv.isConnected)tt.replaceChild(unitIcon(k),cv)},ms);")
open(F,'w').write(s);print('icon retry ok')
