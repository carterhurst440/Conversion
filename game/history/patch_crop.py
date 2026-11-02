# tight atlas cells: each unit type learns how much of its camera box its body actually fills,
# so a mummy no longer reserves a cell eight times bigger than itself (that waste made units blurry, slow and drop out)
s=open('tidebreak.html').read()
def R(a,b,n=1):
  global s
  c=s.count(a);assert c==n,(a[:70],c);s=s.replace(a,b)
R("const P=Math.min(st.ty.ps*Z*DPR,st.ty.cap,ATLAS*.45/st.ty.W,ATLAS*.45/st.ty.H);list.push({u,st,P,w:Math.ceil(st.ty.W*P),h:Math.ceil(st.ty.H*P)})}",
  "const C=cropOf(st.ty),P=Math.min(st.ty.ps*Z*DPR,st.ty.cap*(C.full?1:2),ATLAS*.45/(st.ty.W*(C.x1-C.x0)),ATLAS*.45/(st.ty.H*(C.y1-C.y0)));list.push({u,st,P,C,w:Math.ceil(st.ty.W*(C.x1-C.x0)*P),h:Math.ceil(st.ty.H*(C.y1-C.y0)*P)})}")
R("if(atlK<.999)for(const it of list){it.P*=atlK;it.w=Math.ceil(it.st.ty.W*it.P);it.h=Math.ceil(it.st.ty.H*it.P)}}",
  "if(atlK<.999)for(const it of list){it.P*=atlK;it.w=Math.ceil(it.st.ty.W*(it.C.x1-it.C.x0)*it.P);it.h=Math.ceil(it.st.ty.H*(it.C.y1-it.C.y0)*it.P)}}")
R("if(due){sl.fresh=false;cam.left=-ty.W/2;cam.right=ty.W/2;cam.top=ty.H*(1-ty.a);cam.bottom=-ty.H*ty.a;cam.updateProjectionMatrix();",
  "if(due){sl.fresh=false;const C=it.C;sl.C=C;sl.cw=it.w;sl.ch=it.h;cam.left=-ty.W/2+C.x0*ty.W;cam.right=-ty.W/2+C.x1*ty.W;cam.top=ty.H*(1-ty.a)-C.y0*ty.H;cam.bottom=ty.H*(1-ty.a)-C.y1*ty.H;cam.updateProjectionMatrix();")
# sample one freshly rendered cell per frame to learn the type's extents
R("n++;if(!SNAP[ty.f]&&S.clip==='idle'&&(st.slotN||0)>20){",
  "n++;if((!smp||window.__cropAll)&&cropNeeds(ty,frameNo)){smp=1;cropSample(ty,C,sl.x,ATLAS-sl.y-it.h,it.w,it.h)}if(!SNAP[ty.f]&&S.clip==='idle'&&(st.slotN||0)>20){")
R("renderer.setScissorTest(true);const useOutline=effect&&list.length<=10;let n=0;","renderer.setScissorTest(true);const useOutline=effect&&list.length<=10;let n=0,smp=0;")
R("cells.set(it.u,{x:sl.x,y:sl.y,w:it.w,h:it.h,ty,Ps:ty.ps*Z})}","cells.set(it.u,{x:sl.x,y:sl.y,w:sl.cw||it.w,h:sl.ch||it.h,ty,Ps:ty.ps*Z,C:sl.C||CROPFULL})}")
R("const dw=ty.W*Ps,dh=ty.H*Ps;ctx.drawImage(glc,c.x,c.y,c.w,c.h,sx-dw/2,sy-dh*(1-ty.a),dw,dh);return true}",
  "const dw=ty.W*Ps,dh=ty.H*Ps,C=c.C,ox=sx-dw/2,oy=sy-dh*(1-ty.a);ctx.drawImage(glc,c.x,c.y,c.w,c.h,ox+C.x0*dw,oy+C.y0*dh,dw*(C.x1-C.x0),dh*(C.y1-C.y0));return true}")
R("function setEL(d){elDeg=clamp(d,5,45);","function setEL(d){CROP.clear();elDeg=clamp(d,5,45);")
R("const CT=new Map();let slots=new Map(),",r"""const CROPFULL={x0:0,x1:1,y0:0,y1:1,full:1},CROP=new Map();let CROPSV=Object.assign({},window.CROPBAKE||{});try{const sv=JSON.parse(localStorage.getItem('tb-crop2')||'{}')||{};for(const k in sv){const a=CROPSV[k],b=sv[k];CROPSV[k]=a?{x0:Math.min(a.x0,b.x0),x1:Math.max(a.x1,b.x1),y0:Math.min(a.y0,b.y0),y1:Math.max(a.y1,b.y1)}:b}}catch(e){}window.__cropDump=()=>JSON.stringify(CROPSV);let cropSvT=0;
function cropKey(ty){return ty.f+(ty.flat?'f':'')+'@'+elDeg}
function cropFix(E){const q=v=>Math.round(v*20)/20,m=.16;return{x0:Math.max(0,q(E.x0-m)),x1:Math.min(1,q(E.x1+m)),y0:Math.max(0,q(E.y0-m)),y1:Math.min(1,q(E.y1+m*.6))}}
function cropOf(ty){let c=CROP.get(ty);if(!c){const E=CROPSV[cropKey(ty)];if(E){c={n:3,E,C:cropFix(E)};CROP.set(ty,c)}}return c&&c.C||CROPFULL}
function cropNeeds(ty,f){if(window.__cropAll)return true;const c=CROP.get(ty);return !c||c.n<8||f%8===0}
let cropBuf=new Uint8Array(4096);
function cropSample(ty,C,x,y,w,h){if(w<8||h<8)return;const gl=renderer.getContext();if(cropBuf.length<w*h*4)cropBuf=new Uint8Array(w*h*4);try{gl.readPixels(x,y,w,h,gl.RGBA,gl.UNSIGNED_BYTE,cropBuf)}catch(e){return}
  let bx0=w,bx1=-1,by0=h,by1=-1;for(let r=0;r<h;r++){const row=r*w*4;for(let i=0;i<w;i++)if(cropBuf[row+i*4+3]>12){const yy=h-1-r;if(i<bx0)bx0=i;if(i>bx1)bx1=i;if(yy<by0)by0=yy;if(yy>by1)by1=yy}}
  let c=CROP.get(ty);if(!c){c={n:0,E:null,C:null};CROP.set(ty,c)}c.n++;if(bx1<0)return;
  const sw=C.x1-C.x0,sh=C.y1-C.y0,o={x0:C.x0+bx0/w*sw,x1:C.x0+(bx1+1)/w*sw,y0:C.y0+by0/h*sh,y1:C.y0+(by1+1)/h*sh};
  // touching the cell edge means a swing or lunge is spilling out: open that side well up
  if(!C.full){if(bx0<=1)o.x0-=.25;if(bx1>=w-2)o.x1+=.25;if(by0<=1)o.y0-=.25;if(by1>=h-2)o.y1+=.25}
  const E=c.E=c.E?{x0:Math.min(c.E.x0,o.x0),x1:Math.max(c.E.x1,o.x1),y0:Math.min(c.E.y0,o.y0),y1:Math.max(c.E.y1,o.y1)}:o;
  const N=cropFix(E);if(!c.C||N.x0!==c.C.x0||N.x1!==c.C.x1||N.y0!==c.C.y0||N.y1!==c.C.y1){c.C=N;CROPSV[cropKey(ty)]=E;const now=performance.now();if(now-cropSvT>3000){cropSvT=now;try{localStorage.setItem('tb-crop2',JSON.stringify(CROPSV))}catch(e){}}}}
const CT=new Map();let slots=new Map(),""")
R("cv.getContext('2d').drawImage(glc,sl.x,sl.y,it.w,it.h,0,0,it.w,it.h);SNAP[ty.f]=cv}","cv.getContext('2d').drawImage(glc,sl.x,sl.y,it.w,it.h,0,0,it.w,it.h);cv.C=C;SNAP[ty.f]=cv}")
R("const Ps=ty.ps*VW.Z,dw=ty.W*Ps,dh=ty.H*Ps;ctx.save();if((u.fx||0)-(u.fy||0)<0){ctx.translate(sx,0);ctx.scale(-1,1);ctx.translate(-sx,0)}ctx.drawImage(sn,sx-dw/2,sy-dh*(1-ty.a),dw,dh);",
  "const Ps=ty.ps*VW.Z,dw=ty.W*Ps,dh=ty.H*Ps,C=sn.C||CROPFULL;ctx.save();if((u.fx||0)-(u.fy||0)<0){ctx.translate(sx,0);ctx.scale(-1,1);ctx.translate(-sx,0)}ctx.drawImage(sn,sx-dw/2+C.x0*dw,sy-dh*(1-ty.a)+C.y0*dh,dw*(C.x1-C.x0),dh*(C.y1-C.y0));")
R("Ps=ty.ps*ss,dw=ty.W*Ps,dh=ty.H*Ps;ctx.drawImage(sn,sx-dw/2,sy-dh*(1-ty.a),dw,dh);return true}",
  "Ps=ty.ps*ss,dw=ty.W*Ps,dh=ty.H*Ps,C=sn.C||CROPFULL;ctx.drawImage(sn,sx-dw/2+C.x0*dw,sy-dh*(1-ty.a)+C.y0*dh,dw*(C.x1-C.x0),dh*(C.y1-C.y0));return true}")
# a one-pixel clear gutter round every cell so scaling a tight cell never picks up its neighbour's edge
R("let sl=slots.get(it.u);if(sl&&(sl.w<it.w||sl.h<it.h)){freeSlot(sl);slots.delete(it.u);sl=null}if(!sl){sl=allocSlot(it.w,it.h);",
  "let sl=slots.get(it.u);if(sl&&(sl.w<it.w+2||sl.h<it.h+2)){freeSlot(sl);slots.delete(it.u);sl=null}if(!sl){sl=allocSlot(Math.ceil((it.w+2)/16)*16,Math.ceil((it.h+2)/16)*16);")
# a miss first triggers a clean repack; only a miss straight after a repack means the sheet is truly full and units must shrink
R("if(!sl){repackNext=true;STATS.miss=(STATS.miss||0)+1;atlCap=Math.max(.3,Math.min(atlCap,atlK)*.85);continue}","if(!sl){STATS.miss=(STATS.miss||0)+1;if(frameNo-lastRepack<3)atlCap=Math.max(.3,Math.min(atlCap,atlK)*.9);repackNext=true;continue}")
R("if(Math.abs(Z-slotZ)/slotZ>.08||repackNext){repackNext=false;","if(Math.abs(Z-slotZ)/slotZ>.08||repackNext){repackNext=false;lastRepack=frameNo;")
R("let cells=new Map(),lastGT=null,","let lastRepack=-99,cells=new Map(),lastGT=null,")
R("renderer.setViewport(sl.x,ATLAS-sl.y-it.h,it.w,it.h);renderer.setScissor(sl.x,ATLAS-sl.y-it.h,it.w,it.h);renderer.clear();\n      try{(useOutline?effect:renderer).render(st.scene,cam)}",
  "renderer.setScissor(sl.x,ATLAS-sl.y-sl.h,sl.w,sl.h);renderer.clear();renderer.setViewport(sl.x+1,ATLAS-sl.y-1-it.h,it.w,it.h);renderer.setScissor(sl.x+1,ATLAS-sl.y-1-it.h,it.w,it.h);\n      try{(useOutline?effect:renderer).render(st.scene,cam)}")
R("cropSample(ty,C,sl.x,ATLAS-sl.y-it.h,it.w,it.h)","cropSample(ty,C,sl.x+1,ATLAS-sl.y-1-it.h,it.w,it.h)")
R("cv.getContext('2d').drawImage(glc,sl.x,sl.y,it.w,it.h,0,0,it.w,it.h);cv.C=C;","cv.getContext('2d').drawImage(glc,sl.x+1,sl.y+1,it.w,it.h,0,0,it.w,it.h);cv.C=C;")
R("cells.set(it.u,{x:sl.x,y:sl.y,w:sl.cw||it.w,","cells.set(it.u,{x:sl.x+1,y:sl.y+1,w:sl.cw||it.w,")
# menu icons and cards use the same learned crop, so the icon strip stops overflowing and wiping icons
R("const P=Math.min(ty.ps*s*2,ty.cap),w=Math.ceil(ty.W*P),h=Math.ceil(ty.H*P);let sl=slots.get(u);if(sl&&(sl.w<w||sl.h<h)){freeSlot(sl);slots.delete(u);sl=null}if(!sl){sl=allocSlotD(w,h)||allocSlotD(w,h);if(!sl)return false;slots.set(u,sl)}",
  "const C=cropOf(ty),P=Math.min(ty.ps*s*2,ty.cap*(C.full?1:1.6)),w=Math.ceil(ty.W*(C.x1-C.x0)*P),h=Math.ceil(ty.H*(C.y1-C.y0)*P);let sl=slots.get(u);if(sl&&(sl.w<w+2||sl.h<h+2)){freeSlot(sl);slots.delete(u);sl=null}if(!sl){sl=allocSlotD(w+2,h+2)||allocSlotD(w+2,h+2);if(!sl)return false;slots.set(u,sl)}")
R("const S=st.ctl.S,cam=st.cam;cam.left=-ty.W/2;cam.right=ty.W/2;cam.top=ty.H*(1-ty.a);cam.bottom=-ty.H*ty.a;cam.updateProjectionMatrix();",
  "const S=st.ctl.S,cam=st.cam;cam.left=-ty.W/2+C.x0*ty.W;cam.right=-ty.W/2+C.x1*ty.W;cam.top=ty.H*(1-ty.a)-C.y0*ty.H;cam.bottom=ty.H*(1-ty.a)-C.y1*ty.H;cam.updateProjectionMatrix();")
R("renderer.setScissorTest(true);renderer.setViewport(sl.x,ATLAS-sl.y-h,w,h);renderer.setScissor(sl.x,ATLAS-sl.y-h,w,h);renderer.clear();",
  "renderer.setScissorTest(true);renderer.setScissor(sl.x,ATLAS-sl.y-sl.h,sl.w,sl.h);renderer.clear();renderer.setViewport(sl.x+1,ATLAS-sl.y-1-h,w,h);renderer.setScissor(sl.x+1,ATLAS-sl.y-1-h,w,h);")
R("const Ps=ty.ps*s,dw=ty.W*Ps,dh=ty.H*Ps;ctx.drawImage(glc,sl.x,sl.y,w,h,sx-dw/2,sy-dh*(1-ty.a),dw,dh);",
  "const Ps=ty.ps*s,dw=ty.W*Ps,dh=ty.H*Ps;ctx.drawImage(glc,sl.x+1,sl.y+1,w,h,sx-dw/2+C.x0*dw,sy-dh*(1-ty.a)+C.y0*dh,dw*(C.x1-C.x0),dh*(C.y1-C.y0));if(cropNeeds(ty,1)&&w>16)cropSample(ty,C,sl.x+1,ATLAS-sl.y-1-h,w,h);")
# a unit that could not get an atlas cell this frame shows its last snapshot instead of dropping to the flat 2D figure
R("function draw(u,sx,sy,s,fl){if(failed){","function draw(u,sx,sy,s,fl){if(failed||(!cells.has(u)&&!u.hid&&CT.has(u)&&!CT.get(u).hidden&&!CT.get(u).ty.noSnap&&G&&G.units&&G.units.includes(u)&&TYU(u)&&SNAP[TYU(u).f])){")
# extents learned offline from every unit's attacks and specials, so cells start the right size
import json
R("var R3D=(()=>{if(typeof THREE==='undefined')return null;","window.CROPBAKE="+json.dumps(json.load(open('cropbake2.json')),separators=(',',':'))+";\nvar R3D=(()=>{if(typeof THREE==='undefined')return null;")
open('tidebreak.html','w').write(s)
print('crop ok')
