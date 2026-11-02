F='tidebreak.html'
s=open(F).read()
def rep(a,b,n=1):
    global s
    c=s.count(a);assert c==n,(c,a[:100]);s=s.replace(a,b)
# ---------- High Mountains: terraced ground (flat benches broken by sharp cliff bands), hard snowline, rock on the cliffs ----------
rep("hv[vy*VN+vx]=water?.72:bch?.95+n*.12:1.05+clamp((e-.52)*7*amp,0,2.6*amp)+n*.4*(THEME==='moon'?.5:1)}",
    "if(THEME==='mountains'&&!water&&!bch){const raw=clamp((e-.5)*7*amp,0,2.8*amp)+vnoise(vx/7,vy/7,SEED+3)*.9,st=MTN_ST,lv=Math.floor(raw/st),fr=raw/st-lv;hv[vy*VN+vx]=1.05+st*(lv+(fr>.8?(fr-.8)/.2:0))+n*.025}else hv[vy*VN+vx]=water?.72:bch?.95+n*.12:1.05+clamp((e-.52)*7*amp,0,2.6*amp)+n*.4*(THEME==='moon'?.5:1)}")
rep("function tileCol(x,y){","const MTN_ST=.7;\nfunction tileCol(x,y){")
rep("const lit=.6+.56*Math.max(0,nx*LIGHT[0]+ny*LIGHT[1]+nz*LIGHT[2]),hs=hash2(x,y,SEED),dp=dep[i];",
    "const MT=THEME==='mountains',sl=Math.hypot(gx,gy),lit=(MT?.52:.6)+(MT?.7:.56)*Math.max(0,nx*LIGHT[0]+ny*LIGHT[1]+nz*LIGHT[2]),hs=hash2(x,y,SEED),dp=dep[i];")
rep("if(!beachA[i]&&THEME==='mountains'&&elev[i]>.66)base=mixRgb(base,[244,248,252],clamp((elev[i]-.66)*6,0,.85));",
    "if(!beachA[i]&&MT){const hm=Math.min(a,b,c,d),lvl=Math.round((hm-1.05)/MTN_ST);base=shade(base,(lvl%2?.035:-.02)-lvl*.012);"+
    "base=mixRgb(base,mixRgb([240,245,251],[222,231,242],hs*.6),.86);"+
    "if(sl>.22){const k=clamp((sl-.22)*2.6,0,1);base=mixRgb(base,[176,188,204],.4+.45*k)}}if(beachA[i]&&MT)base=mixRgb(base,[238,243,248],.8);")
# no jagged peaks: the mountains are walled by dense snowy pine forest instead
rep("obs:'peak',zt:[.26,.5,.92]","obs:'pines',zt:[.26,.5,.92]")
rep("Long ridges leave only narrow passes.","Dense pine forests leave only narrow passes.")
rep("else if(kind==='peak'){const n=16","else if(kind==='peak'||kind==='pines'){const n=16")
rep("craterrim:1,thicket:1}","craterrim:1,thicket:1,pines:1}")
rep("if(!beachA[i]&&dp==='peak')","if(!beachA[i]&&dp==='pines')base=mixRgb(base,[200,214,222],.35);if(!beachA[i]&&dp==='peak')")
rep("}else if(k==='peak'){const tall",r"""}else if(k==='pines'){ctx.fillStyle='rgba(40,50,70,.18)';ctx.beginPath();ctx.ellipse(sx+2*s,sy+2*s,hw*1.05,hh*1.05,0,0,TAU);ctx.fill();
    for(const[ox,oy,sc2]of[[-9,-1,.95],[8,0,.9],[0,-6,1.15],[-3,5,.85],[6,6,.8]]){const tx=sx+ox*s,ty=sy+oy*s,ss=s*sc2*(.9+r1*.25),Hh=40*ss;ctx.fillStyle='#4a3628';ctx.fillRect(tx-1.6*ss,ty-6*ss,3.2*ss,6*ss);
      for(let t=0;t<3;t++){const yb=ty-5*ss-t*Hh*.26,w=(11-t*2.8)*ss,ht=Hh*.42;ctx.fillStyle=t%2?'#2c5a4c':'#36685a';ctx.beginPath();ctx.moveTo(tx-w,yb);ctx.lineTo(tx,yb-ht);ctx.lineTo(tx+w,yb);ctx.closePath();ctx.fill();
        ctx.fillStyle='#24493f';ctx.beginPath();ctx.moveTo(tx,yb-ht);ctx.lineTo(tx+w,yb);ctx.lineTo(tx+w*.2,yb);ctx.closePath();ctx.fill();
        ctx.fillStyle='#f4f8fc';ctx.beginPath();ctx.moveTo(tx-w*.55,yb-ht*.45);ctx.lineTo(tx,yb-ht);ctx.lineTo(tx+w*.5,yb-ht*.42);ctx.lineTo(tx+w*.2,yb-ht*.5);ctx.lineTo(tx-w*.15,yb-ht*.38);ctx.closePath();ctx.fill()}}
  }else if(k==='peak'){const tall""")
open(F,'w').write(s);print('mountains terraces + pines ok')
