import sys
head=open('r3d_head.js').read().split('\n')
defs='\n'.join(l for l in head[2:48] if 'ATLAS' not in l and 'renderer' not in l and not l.startswith('const effect'))
egy=open('egy_r3d.js').read();lab=open('lab_main.js').read()
U=dict(
 embalmer=dict(file='embalmer-lab.html',title='Embalmer Lab',name='Nubian Warrior',role='Embalmer slot · Anubis · new look',
  stats=[('Health','110'),('Damage','7'),('Rate','1/s'),('Range','2.6'),('Speed','1.4')],
  spec='Healing ritual',
  note='Tap the dummy to attack, tap the ground to walk. Her swings throw a crescent wave at range (the Embalmer is a ranged unit). The special plants her spear and kneels inside the game\'s incense ring (2.6 tiles, heals 9/s for 3\u00bd s).',
  cfg="""{f:'embalmer',dmg:7,ps:28,view:3.4,wide:5.2,range:2.6,spd:1.4,rate:1,vref:1,atk:[['whirl',.5,1],['twirl',.46,1],['vault',.56,1]],
  special(){const a=LAB.api;if(a.ritual>0)return;a.ritual=3.5;a.ctl.playG('kneel',1,0);a.ctl.S.hold=true;a.say('Healing ritual')},
  tickSpecial(dt){const a=LAB.api;a.ritual=Math.max(0,a.ritual-dt);const t=3.5-a.ritual,S=a.ctl.S;S.t=t;if(a.ritual<=0){S.hold=false;a.say('Idle')}
    const r=2.6*a.TILE,f=Math.min(1,t/.5,(3.5-t)/.4+.2)*(a.ritual>0?1:0);for(const m of[a.ring,a.ringFill]){m.position.set(a.pos.x,m.position.y,a.pos.z);m.scale.setScalar(r)}a.ring.material.opacity=f*.95;a.ringFill.material.opacity=f*.16},
  onHit(A){const h=new T.Vector3();LAB.api.ctl.U.spearHead.localToWorld(h.set(0,.1,0));const sh=new T.Shape();sh.absarc(0,0,.26,Math.PI*.12,Math.PI*.88,false);sh.absarc(0,-.07,.21,Math.PI*.82,Math.PI*.18,true);
    const geo=new T.ShapeGeometry(sh,16);geo.translate(0,-.16,0);const mat=new T.MeshBasicMaterial({color:A[0]==='vault'?'#ffe6b0':'#cfe6ff',transparent:true,blending:T.AdditiveBlending,depthWrite:false,side:T.DoubleSide});mat.userData=NOOUT;
    const m=new T.Mesh(geo,mat);if(A[0]==='vault')m.scale.setScalar(1.5);LAB.shoot(h,null,null,null,m)}}"""),
 mummy=dict(file='mummy-lab.html',title='Mummy Lab',name='Mummy',role='Holy melee · Anubis',
  stats=[('Health','300'),('Damage','14'),('Rate','0.9/s'),('Range','0.8'),('Speed','1.2')],
  spec='Fall and rise',
  note='Tap the dummy to attack, tap the ground to walk. The special plays what happens the first time it falls in battle: it lies still for 2 seconds, then rises at half health.',
  cfg="""{f:'mummy',dmg:14,ps:38,view:3.4,wide:5.2,range:.8,spd:1.2,rate:.9,vref:1.6,atk:[['whip',.46,1.1],['spin',.5,1.1],['whipR',.46,1.1],['twin',.46,1.1]],
  special(){const a=LAB.api;if(a.ritual>0)return;a.ritual=2.6;a.ctl.playG('down',1,0);a.ctl.S.hold=true;a.say('Lies still\u2026')},
  tickSpecial(dt){const a=LAB.api,S=a.ctl.S;a.ritual=Math.max(0,a.ritual-dt);if(a.ritual<=.6&&S.clip==='down'){S.hold=false;a.ctl.playG('rise',1,0);a.say('Rises again')}if(a.ritual<=0)a.say('Idle')},
  onHit(){}}"""),
 tripo=dict(nospec=1,file='tripo-mummy-lab.html',title='Tripo Mummy Lab',name='Cartoon Mummy',role='Imported model test, Anubis faith',glb='glb/cmrig.glb',
  stats=[('Health','300'),('Damage','14'),('Rate','0.9/s'),('Range','0.8'),('Speed','1.9*')],
  spec='Fall and rise',
  note='Model and skeleton from Tripo; every movement is ours: the walk, idle and whip attacks are driven straight onto its bones. Tap the dummy to attack, tap the ground to walk. The fall-and-rise special is not wired up for it yet. *Lab speed raised from the game\'s 1.2 to test the scurry.',
  cfg="""{f:'tripo',ribbons:1,mh:1.05,tuck:[.3,.62,.17],style:{head:1.15,hand:1.1,foot:1.05},dmg:14,ps:38,view:3.4,wide:5.2,range:.8,spd:1.9,rate:.9,vref:1.6,atk:[['arch',.55,1.1],['spin',.5,1.1],['whipR',.46,1.1],['twin',.46,1.1],['whip',.46,1.1]],
  special(){LAB.api.say('Not wired up for the imported model yet')},onHit(){}}"""),
 cat=dict(nospec=1,fact='fact_cat.js',file='sphynx-lab.html',title='Sphynx Cat Lab',name='Sphynx Cat',role='Imported model, rigged by us',glb='glb/catrig.glb',
  stats=[('Health','160'),('Damage','10'),('Rate','1.2/s'),('Range','1'),('Speed','1.8')],
  spec='',
  note='Your Tripo model with no rig: the skeleton (spine, neck, head, ears, four legs, 12-link tail) and the skin weights were built in code from the mesh. Every motion is ours. Tap the dummy to attack, tap the ground to walk.',
  cfg="""{f:'cat',mh:.8,dmg:10,ps:38,view:3.2,wide:4.8,range:1,spd:1.8,rate:1.2,vref:1.6,atk:[['swipe',.36,1],['pounce',.55,1],['swipeR',.36,1],['flurry',.5,1]],
  special(){},onHit(){}}"""),
 sphynx=dict(nospec=1,fact='fact_cat.js',file='sphynx-scratch-lab.html',title='Sphynx Lab (from scratch)',name='Sphynx Cat',role='Sculpted and rigged from scratch in code',glb='glb/sphynx.glb',
  stats=[('Health','160'),('Damage','10'),('Rate','1.2/s'),('Range','1'),('Speed','1.8')],
  spec='',
  note='No Tripo: the body is sculpted in code from soft-blended shapes, painted, given a skeleton and skinned, then driven by the same cat animation as the Tripo lab, for a side-by-side comparison. Tap the dummy to attack, tap the ground to walk.',
  cfg="""{f:'cat',mh:.8,grad:1,bindStance:1,dmg:10,ps:38,view:3.2,wide:4.8,range:1,spd:1.8,rate:1.2,vref:1.6,atk:[['swipe',.36,1],['pounce',.55,1],['swipeR',.36,1],['flurry',.5,1]],
  special(){},onHit(){}}"""),
 sphinx=dict(fact='fact_sphinx.js',file='sphinx-lab.html',title='Sphinx Lab',name='Sphinx',role='Mythic beast, sculpted and animated from scratch',glb='glb/sphinx.glb',
  stats=[('Health','900'),('Damage','32'),('Rate','1.1/s'),('Range','1.3'),('Speed','2')],
  spec='Skyfall',
  note='Tap the ground and it prowls; tap the dummy and it charges at a gallop, then mauls, rakes, pounces and beats its wings. Skyfall: it takes to the air, hangs over the target and dives into a ground-shaking area slam (2.2x damage).',
  cfg="""{f:'sphinx',mh:1.25,dmg:32,ps:70,view:4.4,wide:6.4,range:1.3,spd:2,chargeMul:1.9,rate:1.1,vref:4,atk:[['maul',.26,1],['swipe',.208,1],['pounce',.343,1],['swipeR',.208,1],['buffet',.286,1]],
  special(){const a=LAB.api;if(a.ritual>0)return;a.setAtk(false);a.ritual=2.1;a.ctl.playG('skyfall',1,0);a.ctl.S.hold=true;a.say('Skyfall')},
  tickSpecial(dt){const a=LAB.api;a.ritual=Math.max(0,a.ritual-dt);if(a.ritual<=0){a.ctl.S.hold=false;a.ctl.playG('idle');a.say('Idle')}},
  onQuake(){LAB.api.hit(32*2.2,1.6)},onHit(){}}"""),
 nubian=dict(fact='empty.js',glb='glb/nubian.glb',file='nubian-lab.html',title='Nubian Warrior Lab',name='Nubian Warrior',role='Embalmer slot, Anubis faith, sculpted body',
  stats=[('Health','110'),('Damage','7'),('Rate','1/s'),('Range','2.6'),('Speed','1.4')],
  spec='Healing ritual',
  note='Tap the dummy to attack, tap the ground to walk. Her swings throw a crescent wave at range (the Embalmer is a ranged unit). The special plants her spear and kneels inside the game\'s incense ring (2.6 tiles, heals 9/s for 3\u00bd s).',
  cfg="""{f:'nubian',dmg:7,ps:28,view:3.4,wide:5.2,range:2.6,spd:1.4,rate:1,vref:1,atk:[['whirl',.5,1],['twirl',.46,1],['vault',.56,1]],
  special(){const a=LAB.api;if(a.ritual>0)return;a.ritual=3.5;a.ctl.playG('kneel',1,0);a.ctl.S.hold=true;a.say('Healing ritual')},
  tickSpecial(dt){const a=LAB.api;a.ritual=Math.max(0,a.ritual-dt);const t=3.5-a.ritual,S=a.ctl.S;S.t=t;if(a.ritual<=0){S.hold=false;a.say('Idle')}
    const r=2.6*a.TILE,f=Math.min(1,t/.5,(3.5-t)/.4+.2)*(a.ritual>0?1:0);for(const m of[a.ring,a.ringFill]){m.position.set(a.pos.x,m.position.y,a.pos.z);m.scale.setScalar(r)}a.ring.material.opacity=f*.95;a.ringFill.material.opacity=f*.16},
  onHit(A){const h=new T.Vector3();LAB.api.ctl.U.spearHead.localToWorld(h.set(0,.1,0));const sh=new T.Shape();sh.absarc(0,0,.26,Math.PI*.12,Math.PI*.88,false);sh.absarc(0,-.07,.21,Math.PI*.82,Math.PI*.18,true);
    const geo=new T.ShapeGeometry(sh,16);geo.translate(0,-.16,0);const mat=new T.MeshBasicMaterial({color:A[0]==='vault'?'#ffe6b0':'#cfe6ff',transparent:true,blending:T.AdditiveBlending,depthWrite:false,side:T.DoubleSide});mat.userData=NOOUT;
    const m=new T.Mesh(geo,mat);if(A[0]==='vault')m.scale.setScalar(1.5);LAB.shoot(h,null,null,null,m)}}"""),
 combo=dict(fact='fact_q.js',file='nubq-test.html',title='Nubian Combo Lab',name='Nubian Warrior',role='Tripo model and rig, full-body motion by us',glb='glb/nubq_lab.glb',
  stats=[('Health','110'),('Damage','9'),('Rate','combo'),('Range','1.05'),('Speed','3.4')],
  spec='Healing ritual',
  note='Special: the healing ritual (blades driven into the ground, kneeling prayer). Tap the dummy for the full combination: dash, spinning slash, butterfly kick, crouch landing, rising cross-slash, hop back to stance. Slow-mo shows the detail.',
  cfg="""{f:'combo',mh:1,dmg:9,ps:38,view:3.9,wide:5.8,camK:.22,camW:.62,range:1.05,spd:3.4,rate:.385,vref:6,atk:[['combo',.47,1]],
  onStrike(k,i){const a=LAB.api;if(a.ritual>0){a.shake(.35);return}if(i>0)a.hit(9*k,k>1)},
  special(){const a=LAB.api;if(a.ritual>0)return;a.setAtk(false);a.ritual=4.4;a.ctl.playG('ritual',1,0);a.ctl.S.hold=true;a.say('Healing ritual')},
  tickSpecial(dt){const a=LAB.api;a.ritual=Math.max(0,a.ritual-dt);const t=4.4-a.ritual,S=a.ctl.S;if(a.ritual<=0){S.hold=false;a.ctl.playG('idle');a.say('Idle')}
    const r=2.6*a.TILE,f=t<.66?0:Math.min(1,(t-.66)/.4,(4.2-t)/.5);for(const m of[a.ring,a.ringFill]){m.position.set(a.pos.x,m.position.y,a.pos.z);m.scale.setScalar(r)}a.ring.material.opacity=Math.max(0,f)*.95;a.ringFill.material.opacity=Math.max(0,f)*.16},onHit(){}}"""),
 archer=dict(fact='fact_archer.js',file='celtic-archer-lab.html',title='Celtic Archer Lab',name='Celtic Archer',role='Tripo model and rig, Cernunnos faith, full-body motion by us',glb='glb/archer_src.glb',
  stats=[('Health','90'),('Damage','12'),('Rate','0.55/s'),('Range','3.2'),('Speed','2')],
  spec='Power Shot',
  note='Tap the dummy for the full shot: poised crouch, lateral leap with a twist, arrow drawn from the quiver and nocked in the air, full draw to the cheek, release at the top, soft one-foot landing, low pivot, hop back to the ready stance. Power Shot: she plants wide and overdraws while the green power of Cernunnos spirals into the arrowhead, then looses a spirit arrow that rocks her back and hits for about four times the damage.',
  cfg="""{f:'archer',mh:1,dmg:12,ps:38,view:4.4,wide:6.6,camK:.22,camW:.55,range:3.2,spd:2,rate:.55,vref:3,atk:[['shot',.7,1]],
  onStrike(k,i,U){const m=U.mkArrow();m.material={opacity:1};const p=U.bow.position.clone();
    if(k>1){m.scale.multiplyScalar(1.7);const g=egSprite(U.GLW,.14,'#b6ff8c');g.position.z=.36;m.add(g);for(let j=1;j<7;j++){const t=egSprite(U.GLW,.11-j*.012,'#4fd84a',false);t.material.opacity=.85-j*.11;t.position.z=.3-j*.09;m.add(t)}m.userData.power=1}
    LAB.shoot(p,null,null,null,m)},
  onLand(o){if(!o.m.userData.power)return;const a=LAB.api;a.ctl.U.burstAt(o.b.clone(),40);a.ctl.U.burstAt(o.b.clone(),16,'#a8f07a');a.shake(.55);a.hit(30,true)},
  special(){const a=LAB.api;if(a.ritual>0)return;a.setAtk(false);const d=a.dum.g.position;a.ctl.S.aimYaw=Math.atan2(d.x-a.pos.x,d.z-a.pos.z);a.ritual=2.7;a.ctl.playG('power',1,0);a.ctl.S.hold=true;a.say('Power Shot')},
  tickSpecial(dt){const a=LAB.api;a.ritual=Math.max(0,a.ritual-dt);if(a.ritual<=0){a.ctl.S.hold=false;a.ctl.S.aimYaw=null;a.ctl.playG('idle');a.say('Idle')}},onHit(){}}"""),
 vdruid=dict(fact='fact_vdruid.js',file='verdant-druid-lab.html',title='Druid Lab',name='Verdant Druid',role='Celtic worker, basic form',glb='glb/elf.glb',glbUp='glb/aged.glb',
  stats=[('Health','40'),('Carries','3'),('Jobs','plant, reap, chop'),('Range','0.8'),('Speed','1.7')],
  spec='Work',
  note='Basic form. Tap Work and he walks to the post and cycles his jobs: Plant, Reap with the golden sickle, Chop with the hatchet.',
  cfg="""{f:'vdruid',form:'basic',mh:1,dmg:0,ps:38,view:3.6,wide:5.4,camK:.22,camW:.6,range:.75,spd:1.7,rate:.4,vref:1.4,atk:[['plant',.95,1],['reap',.42,1],['chop',.44,1]],
  JOBS:[['plant',.95,1],['reap',.42,1],['chop',.44,1]],SPELLS:[['cast',.5,1],['thorns',.6,1],['cast',.5,1]],
  onForm(){const up=this.form==='up',q=s=>document.querySelector(s),set=(s,v)=>{const e=q(s);if(e)e.innerHTML=v};
    set('.card h1',up?'Aged Druid':'Verdant Druid');set('.card .role',up?'Celtic magic warrior, upgraded form (still plants, reaps and chops)':'Celtic worker, basic form');
    const st=up?[['Health','180'],['Damage','16'],['Rate','0.75/s'],['Range','2.8'],['Speed','1.5']]:[['Health','40'],['Carries','3'],['Jobs','plant, reap, chop'],['Range','0.8'],['Speed','1.7']];set('.card dl',st.map(([a,b])=>`<div class="st"><dt>${a}</dt><dd>${b}</dd></div>`).join(''));
    set('.card .note',up?'Upgraded form. Attack: Cast (an orb gathered between his palms and driven at the foe) and Thorns (palm slammed to the earth, spikes burst up under the foe). Work: the same three jobs as the Verdant Druid.':'Basic form. Tap Work and he walks to the post and cycles his jobs: Plant, Reap with the golden sickle, Chop with the hatchet.');
    const ba=q('#b-atk'),bs=q('#b-spec'),bf=q('#b-form');if(ba)ba.textContent=up?'Attack dummy':'Work';if(bs)bs.style.display=up?'':'none';if(bf)bf.textContent=up?'\u2190 Verdant Druid':'Upgrade \u2192 Aged Druid';
    if(!this._w&&ba){this._w=1;ba.addEventListener('click',()=>{if(this._work){this._work=false;return}if(this.form==='up'){this.atk=this.SPELLS;this.range=2.8;this.rate=.75}})}this.atk=up?this.SPELLS:this.JOBS;this.range=up?2.8:.75;this.rate=up?.75:.4;this.dmg=up?16:0;this.spd=up?1.5:1.7;this.mode='atk'},
  special(){if(this.form!=='up')return;const a=LAB.api;this._work=true;this.atk=this.JOBS;this.range=.75;this.rate=.4;document.getElementById('b-atk').click();a.say('Working')},
  onStrike(k,i,U,clip){const a=LAB.api;if(clip==='cast'){const m=new T.Group();const g=egSprite(U.GLW,.22,'#b6ff8c');m.add(g);for(let j=1;j<5;j++){const t=egSprite(U.GLW,.16-j*.025,'#4fd84a',false);t.material.opacity=.8-j*.15;t.position.z=-j*.05;m.add(t)}m.material={opacity:1};m.scale.setScalar(.9);
      const p=U.palmL.getWorldPosition(new T.Vector3()).lerp(U.palmR.getWorldPosition(new T.Vector3()),.5);LAB.shoot(p,null,null,null,m)}
    else if(clip==='thorns'){const d=a.dum.g.position.clone();U.thorns(d);setTimeout(()=>a.hit(22,true),120);a.shake(.3)}},
  onHit(){}}"""),
 ark2=dict(glb2='glb/bearer.glb',fact='fact_ark.js',file='scarab-ark-lab.html',title='Scarab Ark Lab',name='Scarab Ark',role='Siege unit, Anubis faith, sculpted from scratch',glb='glb/ark_nb.glb',
  stats=[('Health','520'),('Brood','12 / 6s'),('Burst','8 each'),('Range','6'),('Speed','0.9')],
  spec='Plague',
  note='Special, Plague: it shakes and blazes, bursts open, and a flying swarm rolls onto the enemy and churns over it for several seconds. Bearers carry it in and hold 6 tiles back. Every 6 seconds the shell swings open and a brood of scarabs pours out, skitters to the enemy, climbs on and bursts (8 each). Up to 30 alive at once. The only way to stop it is to reach it.',
  cfg="""{f:'ark',kite:1,mh:.95,dmg:0,ps:60,view:6.6,wide:9.4,camW:.45,range:6,spd:.9,rate:.167,vref:2,atk:[['open',.6,1]],
  onBurst(){LAB.api.hit(8,false)},onPlague(){LAB.api.hit(3,false)},
  special(){const a=LAB.api;if(a.ritual>0)return;a.setAtk(false);a.ritual=3.6;a.ctl.playG('plague',1,0);a.ctl.S.hold=true;a.say('Plague')},
  tickSpecial(dt){const a=LAB.api;a.ritual=Math.max(0,a.ritual-dt);if(a.ritual<=0){a.ctl.S.hold=false;a.ctl.playG('idle');a.say('Idle')}},onHit(){}}"""),
)
k=sys.argv[1];u=U[k]
stats=''.join(f'<div class="st"><dt>{a}</dt><dd>{b}</dd></div>' for a,b in u['stats'])
import base64
extra='';tripo='';boot='__boot();'
if u.get('glb'):
  extra='\n<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>\n<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/utils/SkeletonUtils.js"></script>'
  tripo=open(u.get('fact','fact_tripo.js')).read()
  b64=base64.b64encode(open(u['glb'],'rb').read()).decode()
  boot="const GLB64='"+b64+"';{const bin=atob(GLB64),buf=new Uint8Array(bin.length);for(let i=0;i<bin.length;i++)buf[i]=bin.charCodeAt(i);new T.GLTFLoader().parse(buf.buffer,'',g=>{window.TRIPO=g;__boot()},e=>{document.getElementById('msg').textContent='Could not load the model: '+e})}"
  if u.get('glbUp'):
    b2=base64.b64encode(open(u['glbUp'],'rb').read()).decode()
    boot="const GLB64='"+b64+"',GLB64B='"+b2+"';{const dec=s=>{const bin=atob(s),buf=new Uint8Array(bin.length);for(let i=0;i<bin.length;i++)buf[i]=bin.charCodeAt(i);return buf.buffer};const L=new T.GLTFLoader(),err=e=>{document.getElementById('msg').textContent='Could not load the model: '+e};L.parse(dec(GLB64),'',g=>{window.TRIPO=g;L.parse(dec(GLB64B),'',g2=>{window.TRIPO2=g2;__boot()},err)},err)}"
  if u.get('glb2'):
    b2=base64.b64encode(open(u['glb2'],'rb').read()).decode()
    boot="const GLB64='"+b64+"',GLB64B='"+b2+"';{const dec=s=>{const bin=atob(s),buf=new Uint8Array(bin.length);for(let i=0;i<bin.length;i++)buf[i]=bin.charCodeAt(i);return buf.buffer};const L=new T.GLTFLoader(),err=e=>{document.getElementById('msg').textContent='Could not load the model: '+e};L.parse(dec(GLB64),'',g=>{window.TRIPO=g;L.parse(dec(GLB64B),'',g2=>{window.BEARER=g2;__boot()},err)},err)}"
html=f'''<title>{u["title"]}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Josefin+Sans:wght@400;600&family=Figtree:wght@400;600;700&display=swap">
<style>
/* layout: the 3D plane fills the screen; a name card top-left and one control bar along the bottom, like the game's HUD */
:root{{--ink:#2b2440;--muted:#6b6385;--card:rgba(250,247,240,.92);--line:rgba(43,36,64,.14);--gold:#c9a23f;--accent:#2b2440;--on-accent:#faf7f0;
  --display:'Josefin Sans',Futura,'Trebuchet MS',sans-serif;--body:Figtree,system-ui,sans-serif;color-scheme:light}}
html,body{{height:100%}}
body{{margin:0;background:#9ccbe0;color:var(--ink);font-family:var(--body);overflow:hidden}}
#gl{{position:fixed;inset:0;touch-action:none;cursor:pointer}}
#gl canvas{{display:block}}
.card{{position:fixed;top:calc(12px + env(safe-area-inset-top,0px));left:max(16px,env(safe-area-inset-left,0px));background:var(--card);border:1px solid var(--line);border-radius:14px;padding:12px 14px;max-width:min(300px,calc(100vw - 32px));backdrop-filter:blur(6px)}}
h1{{font-family:var(--display);font-weight:600;letter-spacing:.14em;text-transform:uppercase;font-size:1.15rem;margin:0}}
.role{{color:var(--muted);font-size:.8rem;margin-top:2px}}
dl{{display:grid;grid-template-columns:repeat(5,auto);gap:2px 12px;margin:10px 0 0}}
.st{{display:flex;flex-direction:column}}dt{{font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}}dd{{margin:0;font-weight:700;font-variant-numeric:tabular-nums}}
.note{{font-size:.78rem;line-height:1.4;color:var(--muted);margin:10px 0 0}}
#msg{{font-size:.78rem;font-weight:600;color:var(--gold);margin-top:6px}}
.bar{{position:fixed;left:0;right:0;bottom:0;padding:10px max(16px,env(safe-area-inset-right,0px)) calc(12px + env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px));display:flex;flex-wrap:wrap;gap:8px;align-items:center;justify-content:center;pointer-events:none}}
.bar>*{{pointer-events:auto}}
button{{font:600 .86rem var(--body);color:var(--ink);background:var(--card);border:1px solid var(--line);border-radius:999px;padding:9px 15px;cursor:pointer}}
button.main{{background:var(--accent);color:var(--on-accent);border-color:var(--accent)}}
button[aria-pressed="true"]{{background:var(--gold);color:var(--on-accent);border-color:var(--gold)}}
button:focus-visible,input:focus-visible{{outline:2px solid var(--gold);outline-offset:2px}}
#dhud{{position:fixed;left:0;top:0;width:52px;height:6px;border-radius:3px;background:rgba(43,36,64,.35);overflow:hidden;pointer-events:none}}#dhpf{{height:100%;width:100%;background:#7fcf6a}}
.dn{{position:fixed;left:0;top:0;font:800 15px var(--body);color:#fffaf0;-webkit-text-stroke:3px #2b2440;paint-order:stroke;pointer-events:none}}.dn.big{{font-size:19px;color:#ffd66a}}
label.z{{display:flex;align-items:center;gap:6px;font-size:.78rem;font-weight:600;background:var(--card);border:1px solid var(--line);border-radius:999px;padding:6px 12px}}
input[type=range]{{width:90px;accent-color:var(--ink)}}
</style>
<div id="gl"></div><div id="dhud"><div id="dhpf"></div></div>
<section class="card"><h1>{u["name"]}</h1><div class="role">{u["role"]}</div><dl>{stats}</dl><p class="note">{u["note"]}</p><div id="msg">Idle</div></section>
<div class="bar"><button id="b-atk" class="main">Attack dummy</button>{'' if u.get('nospec') else '<button id="b-spec" class="main">'+u['spec']+'</button>'}{'<button id="b-form" class="main">Upgrade</button>' if u.get('glbUp') else ''}<button id="b-walk">Walk</button><button id="b-stop">Stop</button>
<button id="b-slow" aria-pressed="false">Slow-mo</button><button id="b-team">Team: red</button><label class="z" for="zoom">Zoom <input id="zoom" type="range" min="0.6" max="2.6" step="0.05" value="1.5"></label></div>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/build/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/effects/OutlineEffect.js"></script>{extra}
<script>
(()=>{{
{defs}
{egy}
window.LABCFG={u["cfg"]};
const LAB=window.LABCFG;window.__lab=LAB;
{tripo}
function __boot(){{
{lab.replace("const LAB=window.LABCFG;","")}
}}
{boot}
}})();
</script>'''
open(u['file'],'w').write(html);print(u['file'],len(html))
