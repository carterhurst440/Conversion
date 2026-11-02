#!/usr/bin/env python3
"""Turn a .glb into a game model file:  python3 tools/add_model.py path/to/model.glb key
 - shrinks textures to 512px JPEG, repacks (quantized skin weights/normals, drops animations)
 - writes m/<key>.js, which index.html loads with a <script> tag
Then add 'key' to the KS=[...] list in the window.MODELS loader in index.html (search for "const KS=")."""
import sys,os,base64,tempfile
sys.path.insert(0,os.path.dirname(__file__))
from shrinktex import shrink
from glbq import repack
src,key=sys.argv[1],sys.argv[2]
tmp=tempfile.mktemp(suffix='.glb');shrink(src,tmp)
d=repack(open(tmp,'rb').read());os.remove(tmp)
os.makedirs('m',exist_ok=True)
open('m/%s.js'%key,'w').write("(window.__MD=window.__MD||{})['%s']='%s';"%(key,base64.b64encode(d).decode()))
print('wrote m/%s.js'%key,len(d)//1024,'KB glb')
