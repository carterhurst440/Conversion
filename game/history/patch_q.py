# last step: repack every embedded model (skin weights, joints, texcoords and colors quantized; unused animation tracks dropped)
import re,base64,sys;sys.path.insert(0,'.')
from glbq import repack
F='tidebreak.html';s=open(F).read();n0=len(s)
def sub(m):
    d=base64.b64decode(m.group(2));return m.group(1)+":'"+base64.b64encode(repack(d)).decode()+"'"
s=re.sub(r"([a-zA-Z0-9_]+):'(Z2xURg[A-Za-z0-9+/=]+)'",sub,s)
open(F,'w').write(s);print('models repacked',n0//1024,'->',len(s)//1024,'KB')
