import sys,io;sys.path.insert(0,'.')
from glbw import *
from PIL import Image
def shrink(src,out,size=512,q=82):
    j,b=load(src)
    bvs=j['bufferViews'];imgs={im['bufferView'] for im in j.get('images',[])}
    new=bytearray()
    for i,bv in enumerate(bvs):
        o=bv.get('byteOffset',0);data=bytes(b[o:o+bv['byteLength']])
        if i in imgs:
            I=Image.open(io.BytesIO(data)).convert('RGB');I=I.resize((size,size),Image.LANCZOS);buf=io.BytesIO();I.save(buf,'JPEG',quality=q);data=buf.getvalue()
        while len(new)%4:new.append(0)
        bv['byteOffset']=len(new);bv['byteLength']=len(data);new+=data
    for im in j.get('images',[]):im['mimeType']='image/jpeg'
    j['buffers'][0]['byteLength']=len(new)
    save(out,j,new)
