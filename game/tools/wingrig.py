# add wing bones to a Tripo-rigged winged character: L/R_Wing1 (root, on Spine02) and L/R_Wing2 (mid, child of Wing1); wing vertices re-skinned to them
import sys,json,struct,numpy as np
sys.path.insert(0,'.')
from glbq import parse,read
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
src,out,mode=sys.argv[1],sys.argv[2],sys.argv[3]
d=open(src,'rb').read();j,b0=parse(d);b=bytes(b0)
pr=j['meshes'][0]['primitives'][0];P=read(j,b,pr['attributes']['POSITION']).astype(np.float64);JN=read(j,b,pr['attributes']['JOINTS_0']).astype(np.int64);WT=read(j,b,pr['attributes']['WEIGHTS_0']).astype(np.float64)
sk=j['skins'][0];jn=sk['joints'];names=[j['nodes'][i]['name'] for i in jn]
IBM=read(j,b,sk['inverseBindMatrices']).reshape(-1,4,4).transpose(0,2,1).astype(np.float64)  # column-major -> row matrices
dom=JN[np.arange(len(WT)),WT.argmax(1)]
if mode=='comp':
  I=read(j,b,pr['indices']).ravel();key=np.round(P*1e4).astype(np.int64);_,inv=np.unique(key,axis=0,return_inverse=True);inv=inv.ravel()
  F=inv[I].reshape(-1,3);n=inv.max()+1;r=np.concatenate([F[:,0],F[:,1],F[:,2]]);c=np.concatenate([F[:,1],F[:,2],F[:,0]])
  nc,lab=connected_components(coo_matrix((np.ones(len(r)),(r,c)),shape=(n,n)),directed=False);L=lab[inv];cnt=np.bincount(L)
  wings=[k for k in np.argsort(-cnt)[1:3]];WM=np.isin(L,wings)
else:
  head=names.index('Head');cz=np.median(P[dom==head][:,2]);WM=(dom==head)&((P[:,2]<.24)|(np.abs(P[:,0])>.17))&(P[:,1]>.3)&(np.abs(P[:,0])>.07)
print('wing verts',WM.sum())
sp=names.index('Spine02');SPW=np.linalg.inv(IBM[sp])
newn=[];newIBM=[]
JN2=JN.copy();WT2=WT.copy()
SYM=None
for side,sg in (('L',1),('R',-1)):
  m=WM&(np.sign(P[:,0])==sg);Q=P[m]
  ax=np.abs(Q[:,0]);root=Q[ax<=np.percentile(ax,4)].mean(0);dd=np.linalg.norm(Q-root,axis=1);tip=Q[dd>=np.percentile(dd,96)].mean(0)
  if SYM is None:SYM=(root.copy(),tip.copy())
  else:root=SYM[0]*[-1,1,1];tip=SYM[1]*[-1,1,1]
  mid=root+.42*(tip-root);print(side,'root',root.round(3),'mid',mid.round(3),'tip',tip.round(3))
  i1=len(j['nodes']);i2=i1+1
  # world bind of the new bones: pure translation (axes = model axes)
  M1=np.eye(4);M1[:3,3]=root;M2=np.eye(4);M2[:3,3]=mid
  L1=np.linalg.inv(SPW)@M1;L2=np.linalg.inv(M1)@M2
  def node(nm,Lm):
    t=Lm[:3,3];R=Lm[:3,:3];
    # matrix -> quaternion
    tr=R.trace()
    if tr>0:s=np.sqrt(tr+1)*2;q=[(R[2,1]-R[1,2])/s,(R[0,2]-R[2,0])/s,(R[1,0]-R[0,1])/s,s/4]
    else:
      k=np.argmax(np.diag(R))
      if k==0:s=np.sqrt(1+R[0,0]-R[1,1]-R[2,2])*2;q=[s/4,(R[0,1]+R[1,0])/s,(R[0,2]+R[2,0])/s,(R[2,1]-R[1,2])/s]
      elif k==1:s=np.sqrt(1+R[1,1]-R[0,0]-R[2,2])*2;q=[(R[0,1]+R[1,0])/s,s/4,(R[1,2]+R[2,1])/s,(R[0,2]-R[2,0])/s]
      else:s=np.sqrt(1+R[2,2]-R[0,0]-R[1,1])*2;q=[(R[0,2]+R[2,0])/s,(R[1,2]+R[2,1])/s,s/4,(R[1,0]-R[0,1])/s]
    q=np.array(q);q/=np.linalg.norm(q);return {'name':nm,'translation':t.tolist(),'rotation':q.tolist()}
  j['nodes'].append(node(side+'_Wing1',L1));j['nodes'].append(node(side+'_Wing2',L2));j['nodes'][i1]['children']=[i2]
  spn=jn[sp];j['nodes'][spn].setdefault('children',[]).append(i1)
  k1=len(jn);jn.append(i1);k2=len(jn);jn.append(i2);newIBM+= [np.linalg.inv(M1),np.linalg.inv(M2)]
  # weights: along root->tip, blend wing1 -> wing2; keep a little body weight right at the root
  ab=tip-root;t=np.clip(((Q-root)@ab)/(ab@ab),0,1)
  w2=np.clip((t-.28)/.25,0,1);w2=w2*w2*(3-2*w2);w1=1-w2
  wsp=np.clip(1-t/.08,0,1)*.6;w1*=1-wsp
  idx=np.where(m)[0]
  JN2[idx]=np.stack([np.full(len(idx),k1),np.full(len(idx),k2),np.full(len(idx),sp),np.zeros(len(idx),int)],1)
  WT2[idx]=np.stack([w1*(1-0)*(1),w2*(1-wsp),wsp,np.zeros(len(idx))],1)
  WT2[idx]/=WT2[idx].sum(1,keepdims=True)
b=bytearray(b0)
allIBM=np.concatenate([IBM,np.array(newIBM)],0)
def addacc(arr,ct,typ,target=None):
  while len(b)%4:b.append(0)
  off=len(b);by=arr.tobytes();b.extend(by);bv={'buffer':0,'byteOffset':off,'byteLength':len(by)}
  if target:bv['target']=target
  j['bufferViews'].append(bv);j['accessors'].append({'bufferView':len(j['bufferViews'])-1,'componentType':ct,'count':len(arr),'type':typ});return len(j['accessors'])-1
pr['attributes']['JOINTS_0']=addacc(JN2.astype(np.uint16),5123,'VEC4',34962)
pr['attributes']['WEIGHTS_0']=addacc(WT2.astype(np.float32),5126,'VEC4',34962)
sk['inverseBindMatrices']=addacc(allIBM.transpose(0,2,1).astype(np.float32).reshape(-1,16),5126,'MAT4')
j.pop('animations',None)
j['buffers'][0]['byteLength']=len(b)
js=json.dumps(j,separators=(',',':')).encode();js+=b' '*((-len(js))%4)
while len(b)%4:b.append(0)
o=struct.pack('<III',0x46546C67,2,12+8+len(js)+8+len(b))+struct.pack('<II',len(js),0x4E4F534A)+js+struct.pack('<II',len(b),0x004E4942)+bytes(b)
open(out,'wb').write(o);print('wrote',out,len(o))
