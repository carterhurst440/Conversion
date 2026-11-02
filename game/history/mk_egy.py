kit=open('hkit.js').read();tail=open('hkit_tail.js').read()
def fac(name,f):
    s=open(f).read();head,clips=s.split('//@@CLIPS')
    return "FACT.%s=function(){\n%s\n%s\n%s\n%s\n  return{U,S,scene,get cur(){return cur},playG,tick,clips:CLIPS};};\n"%(name,head,kit,clips,tail)
out=open('egy_common.js').read()
for n,f in [('embalmer','ch_embalmer.js'),('mummy','ch_mummy.js'),('scarab','ch_scarab.js'),('anubis','ch_anubis.js'),('nubian','ch_nubian.js')]:out+=fac(n,f)
open('egy_r3d.js','w').write(out);print(len(out))
head=open('r3d_head.js').read().split('\n');defs='\n'.join(head[2:48])
html=open('egy_test.html').read()
i=html.index('(()=>{\n')+7;j=html.index("const cv=document.getElementById('c')")
html=html[:i]+defs+'\n'+out+'\n'+html[j:]
open('egy_test.html','w').write(html)
