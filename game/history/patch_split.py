# models move out of the page into m/<key>.js, each loaded with a script tag (works on file:// too); frees the page from the 16MB cap
import os,sys,time
F='tidebreak.html';s=open(F).read()
a="window.MODELS={};(function(){if(typeof THREE==='undefined'||!THREE.GLTFLoader)return;const D={"
i=s.index(a);j=i+len(a);end=s.index("};const L=new THREE.GLTFLoader();",j)
body=s[j:end];keys=[];pos=0
os.makedirs('m',exist_ok=True)
for f in os.listdir('m'):os.remove('m/'+f)
while pos<len(body):
  c=body.index(":'",pos);k=body[pos:c].strip(', ');q=body.index("'",c+2);b64=body[c+2:q];pos=q+1
  keys.append(k);open('m/%s.js'%k,'w').write("(window.__MD=window.__MD||{})['%s']='%s';"%(k,b64))
tail_end=s.index("})();",end)+5
V=str(int(time.time()))
new=("window.MODELS={};(function(){if(typeof THREE==='undefined'||!THREE.GLTFLoader)return;const KS=%s;const L=new THREE.GLTFLoader();"
 "const go=k=>{try{const M=window.__MD||{},s64=M[k];if(!s64)return;delete M[k];const bin=atob(s64),buf=new Uint8Array(bin.length);for(let i=0;i<bin.length;i++)buf[i]=bin.charCodeAt(i);L.parse(buf.buffer,'',g=>{window.MODELS[k]=g},e=>console.warn('model',k,e))}catch(e){console.warn('model',k,e)}};"
 "for(const k of KS){const sc=document.createElement('script');sc.src='m/'+k+'.js?v=%s';sc.onload=()=>go(k);sc.onerror=()=>console.warn('model file',k);document.head.appendChild(sc)}})();")%(str(keys).replace(' ',''),V)
s=s[:i]+new+s[tail_end:]
open(F,'w').write(s)
print('split',len(keys),'models; page',len(s)//1024,'KB; m/',sum(os.path.getsize('m/'+f) for f in os.listdir('m'))//1024,'KB')
