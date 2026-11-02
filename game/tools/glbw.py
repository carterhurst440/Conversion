import json,struct,numpy as np
def load(p):
    b=open(p,'rb').read();n=struct.unpack('<I',b[12:16])[0];j=json.loads(b[20:20+n]);o=20+n;bl=struct.unpack('<I',b[o:o+4])[0];bin_=bytearray(b[o+8:o+8+bl]);return j,bin_
CT={5126:np.float32,5125:np.uint32,5123:np.uint16,5121:np.uint8}
NC={'SCALAR':1,'VEC2':2,'VEC3':3,'VEC4':4,'MAT4':16}
def acc(j,bin_,i):
    a=j['accessors'][i];bv=j['bufferViews'][a['bufferView']];dt=np.dtype(CT[a['componentType']]);n=NC[a['type']]
    off=bv.get('byteOffset',0)+a.get('byteOffset',0);st=bv.get('byteStride',dt.itemsize*n)
    arr=np.ndarray((a['count'],n),dtype=dt,buffer=bin_,offset=off,strides=(st,dt.itemsize));return arr
def save(p,j,bin_):
    js=json.dumps(j,separators=(',',':')).encode();js+=b' '*((4-len(js)%4)%4);bb=bytes(bin_)+b'\0'*((4-len(bin_)%4)%4)
    out=struct.pack('<III',0x46546C67,2,12+8+len(js)+8+len(bb))+struct.pack('<II',len(js),0x4E4F534A)+js+struct.pack('<II',len(bb),0x004E4942)+bb;open(p,'wb').write(out)
