# repack a GLB: drop unused animations, quantize skin weights/joints, texcoords and vertex colors (positions and normals stay float)
import json,struct,numpy as np,sys
CT={5120:np.int8,5121:np.uint8,5122:np.int16,5123:np.uint16,5125:np.uint32,5126:np.float32}
NC={'SCALAR':1,'VEC2':2,'VEC3':3,'VEC4':4,'MAT4':16}
def parse(d):
    n=struct.unpack('<I',d[12:16])[0];j=json.loads(d[20:20+n]);o=20+n;bl=struct.unpack('<I',d[o:o+4])[0];b=d[o+8:o+8+bl];return j,b
def read(j,b,ai):
    a=j['accessors'][ai];bv=j['bufferViews'][a['bufferView']];dt=CT[a['componentType']];nc=NC[a['type']];off=bv.get('byteOffset',0)+a.get('byteOffset',0);st=bv.get('byteStride')
    isz=np.dtype(dt).itemsize*nc
    if st and st!=isz:
        raw=np.frombuffer(b,np.uint8,count=st*(a['count']-1)+isz,offset=off);arr=np.stack([np.frombuffer(raw[i*st:i*st+isz].tobytes(),dt) for i in range(a['count'])])
    else: arr=np.frombuffer(b,dt,count=a['count']*nc,offset=off).reshape(a['count'],nc)
    if a.get('normalized'):
        arr=arr.astype(np.float32)/{np.uint8:255.,np.uint16:65535.,np.int8:127.,np.int16:32767.}[dt]
    return arr
def repack(d):
    j,b=parse(d);j.pop('animations',None)
    new=bytearray();bvs=[];accs=[]
    def put(data,target=None,stride=None):
        while len(new)%4:new.append(0)
        bv={'buffer':0,'byteOffset':len(new),'byteLength':len(data)}
        if target:bv['target']=target
        if stride:bv['byteStride']=stride
        new.extend(data);bvs.append(bv);return len(bvs)-1
    amap={}
    def acc(ai,kind=None):
        if (ai,kind) in amap:return amap[(ai,kind)]
        a=j['accessors'][ai];arr=read(j,b,ai);na={'count':a['count'],'type':a['type']}
        if kind=='W':
            w=np.clip(arr,0,None);s=w.sum(1,keepdims=True);s[s==0]=1;w=w/s;q=np.floor(w*255+.5).astype(np.int32)
            for i in np.where(q.sum(1)!=255)[0]:q[i,np.argmax(q[i])]+=255-q[i].sum()
            data=q.astype(np.uint8);na.update(componentType=5121,normalized=True)
        elif kind=='J' and arr.max()<256:data=arr.astype(np.uint8);na['componentType']=5121
        elif kind=='UV' and arr.min()>=0 and arr.max()<=1:data=np.floor(arr*65535+.5).astype(np.uint16);na.update(componentType=5123,normalized=True)
        elif kind=='IDX' and arr.max()<65536:data=arr.astype(np.uint16);na['componentType']=5123
        elif kind=='N':
            n=arr/np.maximum(np.linalg.norm(arr,axis=1,keepdims=True),1e-9);q=np.zeros((len(n),4),np.int8);q[:,:3]=np.round(n*127).astype(np.int8)
            data=q;na.update(componentType=5120,normalized=True);na['bufferView']=put(q.tobytes(),34962,4);accs.append(na);amap[(ai,kind)]=len(accs)-1;return len(accs)-1
        elif kind=='C':
            if arr.shape[1]==3:arr=np.concatenate([arr,np.ones((len(arr),1),np.float32)],1);na['type']='VEC4'
            data=np.floor(np.clip(arr,0,1)*255+.5).astype(np.uint8);na.update(componentType=5121,normalized=True)
        else:
            data=arr.astype(CT[a['componentType']]) if not a.get('normalized') else np.frombuffer(b,CT[a['componentType']],count=a['count']*NC[a['type']],offset=j['bufferViews'][a['bufferView']].get('byteOffset',0)+a.get('byteOffset',0));na['componentType']=a['componentType']
            if a.get('normalized'):na['normalized']=True
        for k in('min','max'):
            if k in a and kind is None:na[k]=a[k]
        tgt=34963 if kind=='IDX' else (34962 if kind!='M' else None)
        na['bufferView']=put(np.ascontiguousarray(data).tobytes(),tgt);accs.append(na);amap[(ai,kind)]=len(accs)-1;return len(accs)-1
    for me in j['meshes']:
        for p in me['primitives']:
            at={}
            for k,ai in p['attributes'].items():
                kind='N' if k=='NORMAL' else 'W' if k.startswith('WEIGHTS') else 'J' if k.startswith('JOINTS') else 'UV' if k.startswith('TEXCOORD') else 'C' if k.startswith('COLOR') else None
                at[k]=acc(ai,kind)
            p['attributes']=at
            if 'indices' in p:p['indices']=acc(p['indices'],'IDX')
            p.pop('targets',None)
    for sk in j.get('skins',[]):
        if 'inverseBindMatrices' in sk:sk['inverseBindMatrices']=acc(sk['inverseBindMatrices'],'M')
    for im in j.get('images',[]):
        bv=j['bufferViews'][im['bufferView']];o=bv.get('byteOffset',0);im['bufferView']=put(b[o:o+bv['byteLength']])
    if any(k=='N' for(_,k) in amap):
        for f in('extensionsUsed','extensionsRequired'):
            l=j.setdefault(f,[])
            if 'KHR_mesh_quantization' not in l:l.append('KHR_mesh_quantization')
    j['bufferViews']=bvs;j['accessors']=accs;j['buffers']=[{'byteLength':len(new)}]
    js=json.dumps(j,separators=(',',':')).encode();
    while len(js)%4:js+=b' '
    while len(new)%4:new.append(0)
    out=struct.pack('<III',0x46546C67,2,12+8+len(js)+8+len(new))+struct.pack('<II',len(js),0x4E4F534A)+js+struct.pack('<II',len(new),0x004E4942)+bytes(new)
    return out
if __name__=='__main__':
    d=open(sys.argv[1],'rb').read();o=repack(d);open(sys.argv[2],'wb').write(o);print(len(d)//1024,'->',len(o)//1024)
