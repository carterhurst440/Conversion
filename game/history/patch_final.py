F='tidebreak.html'
s=open(F).read()
s=s.replace("setHex(I.flash?0xffffff:0)","setHex(I.flash?0x5a2418:0)")
open(F,'w').write(s);print('final ok',s.count('0x5a2418'))
