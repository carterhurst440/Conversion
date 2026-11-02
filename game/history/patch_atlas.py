F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
# ---------- 3D troops never drop to the flat fallback when zoomed in: the atlas shares its space out, and repacks when it fragments ----------
rep("  if(Math.abs(Z-slotZ)/slotZ>.08){slots.clear();shelves=[];slotZ=Z;for(const ds of DEMO.values())ds.lsx=null}",
    "  {let need=0;for(const it of list)need+=it.w*(it.h+2);const bud=ATLAS*ATLAS*.5;const k=need>bud?Math.sqrt(bud/need):1;atlK+=(k-atlK)*(k<atlK?1:.05);if(atlK<.999)for(const it of list){it.P*=atlK;it.w=Math.ceil(it.st.ty.W*it.P);it.h=Math.ceil(it.st.ty.H*it.P)}}\n  if(Math.abs(Z-slotZ)/slotZ>.08||repackNext){repackNext=false;slots.clear();shelves=[];slotZ=Z;for(const ds of DEMO.values())ds.lsx=null}")
rep("if(!sl){sl=allocSlot(it.w,it.h);if(!sl)continue;slots.set(it.u,sl);sl.fresh=true}","if(!sl){sl=allocSlot(it.w,it.h);if(!sl){repackNext=true;STATS.miss=(STATS.miss||0)+1;continue}slots.set(it.u,sl);sl.fresh=true}")
rep("let cells=new Map(),lastGT=null,frameNo=0,failed=false;","let cells=new Map(),lastGT=null,frameNo=0,failed=false,atlK=1,repackNext=false;")
open(F,'w').write(s);print('atlas ok')
