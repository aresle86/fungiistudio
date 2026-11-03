#!/usr/bin/env python3
"""Câu cá dễ hiểu (đợt 1): cần câu tre dựng lại + phao nổi sẵn, icon phao, nút hành động theo từng nhịp,
lần câu đầu có hướng dẫn, nới thời gian giựt, lỡ tay không bị phạt ở 5 con đầu, báo lỗi bằng toast.
Dùng: python3 fishfix.py <nguồn vào> <nguồn ra>. Mỗi chỗ vá phải khớp đúng 1 lần."""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:120])
    s = s.replace(a, b)

# 1. Cần câu tre có đốt, cán quấn dây, chạc tre đỡ, lon mồi giun; phao to hơn
rep("""  stick(root, base.x, base.y, base.z, tip.x, tip.y, tip.z, .011, '#C9A66B'); M(box(.05, .12, .05), '#6B4529', bx - .23, .2, R0 + 1.22, { p: root }); M(cyl(.06, .07, .08, 7), '#8A6A4A', bx - .05, .24, R0 + 1.15, { p: root });""",
"""  const MS0 = c => new T.MeshStandardMaterial({ color: c, flatShading: true, roughness: .8 });
  const RODJ = [], RODT = new T.Object3D(); let RODAX = null;
  { const d = tip.clone().sub(base), up = new T.Vector3(0, 1, 0), dn = d.clone().normalize(), q = new T.Quaternion().setFromUnitVectors(up, dn), at = k => base.clone().addScaledVector(d, k), Ls = d.length() / 6;   /* cần câu tre: 6 lóng nối khớp, thon dần, đốt tre; khúc ngọn võng xuống theo lực cá (rodBend); cán quấn dây, gác trên chạc tre; lon mồi giun cạnh bên */
    RODAX = new T.Vector3().crossVectors(dn, new T.Vector3(0, -1, 0)).normalize().applyQuaternion(q.clone().invert());
    let par = root; for (let i = 0; i < 6; i++){ const j = new T.Group(); if (i === 0){ j.position.copy(base); j.quaternion.copy(q); } else j.position.y = Ls; par.add(j); RODJ.push(j); par = j;
      const r0 = .019 - i * .0022, r1 = .019 - (i + 1) * .0022; M(cyl(r1, r0, Ls, 6), i % 2 ? '#CDAA6E' : '#C49E62', 0, Ls / 2, 0, { p: j }); if (i) M(sph(r0 + .004, 7, 5), '#9C7B42', 0, 0, 0, { p: j, s: [1, .7, 1] }); }
    RODT.position.y = Ls; par.add(RODT);
    M(cyl(.024, .025, d.length() * .17, 6), '#4E3320', 0, d.length() * .085, 0, { p: RODJ[0] }); for (const k of [.03, .085, .14]) M(cyl(.028, .028, d.length() * .012, 6), '#C9A66B', 0, d.length() * k, 0, { p: RODJ[0] });
    const fk = at(.32); stick(root, fk.x, WLR - .06, fk.z, fk.x, fk.y - .02, fk.z, .011, '#8A6A3A'); stick(root, fk.x, fk.y - .03, fk.z, fk.x - .03, fk.y + .04, fk.z - .03, .008, '#8A6A3A'); stick(root, fk.x, fk.y - .03, fk.z, fk.x + .03, fk.y + .04, fk.z + .03, .008, '#8A6A3A');
    const cn = G(bx - .02, .2, R0 + 1.12, 0, root); M(cyl(.045, .045, .08, 10), '#A9B0B2', 0, .04, 0, { p: cn }); M(cyl(.047, .047, .03, 10), '#C24A2E', 0, .04, 0, { p: cn }); M(cyl(.04, .04, .01, 10), '#5A3A22', 0, .081, 0, { p: cn }); for (const [x, z, r] of [[-.014, .01, .4], [.012, -.008, -.5], [.004, .014, 1.2]]) M(new T.TorusGeometry(.012, .005, 4, 8, Math.PI * 1.3), MS0('#E07A86'), x, .088, z, { p: cn, r: [Math.PI / 2, 0, r] }); }""")
rep("""ROOT = pr; const hit = new T.Mesh(new T.SphereGeometry(.35, 8, 6), new T.MeshBasicMaterial({ visible: false })); hit.position.set(bx - .7, .3, R0 + 1.6); S.add(hit); return { root, ph, line, tip, base, hit, rest: new T.Vector3(bx - .98, WLR + .01, R0 + 1.92), ...mkBub() }; })();""",
"""ROOT = pr; ph.scale.setScalar(1.5); const hit = new T.Mesh(new T.SphereGeometry(.35, 8, 6), new T.MeshBasicMaterial({ visible: false })); hit.position.set(bx - .7, .3, R0 + 1.6); S.add(hit); return { root, ph, line, tip, base, hit, rest: new T.Vector3(bx - .98, WLR + .01, R0 + 1.92), RODJ, RODT, RODAX, bend: .07, ...mkBub() }; })();
function rodBend(t, dt){ const C = CAUV, ph = FM.on ? FM.ph : 'idle'; let b = .07 + Math.sin(t * 1.3) * .008;   /* cần cong: nằm yên võng nhẹ, quăng thì bật thẳng, cá rỉa giật nhẹ, phao chìm cong mạnh, kéo cong theo độ căng dây */
  if (ph === 'fly') b = -.06; else if (ph === 'nibble') b = .08 + (FM.t > .3 ? .04 : 0); else if (ph === 'bite') b = .16 + Math.abs(Math.sin(t * 16)) * .04; else if (ph === 'reel'){ const v = FM.vung < 0 && FM.vung > -.55; b = .11 + Math.min(1, FM.ten) * .13 + (v ? Math.sin(t * 30) * .03 : 0); }
  C.bend += (b - C.bend) * Math.min(1, (dt || .016) * (ph === 'fly' ? 18 : 9)); const w = [0, 0, .55, .85, 1.0, 1.1]; for (let i = 2; i < 6; i++) C.RODJ[i].quaternion.setFromAxisAngle(C.RODAX, C.bend * w[i]);
  C.RODT.updateWorldMatrix(true, false); C.RODT.getWorldPosition(C.tip); }""")

# 2. Icon phao đỏ trắng với vòng sóng (không còn thanh chéo như biển cấm)
rep("""  icon('cancau', p => {""",
"""  icon('phao', p => { add(p, new T.TorusGeometry(.36, .022, 4, 30), '#7FB8D0', 0, -.16, 0, [Math.PI / 2, 0, 0]); add(p, new T.TorusGeometry(.24, .02, 4, 26), '#A9D3E3', 0, -.16, 0, [Math.PI / 2, 0, 0]); add(p, new T.SphereGeometry(.17, 14, 8, 0, Math.PI * 2, Math.PI / 2, Math.PI / 2), '#E8453A', 0, -.06, 0); add(p, new T.SphereGeometry(.17, 14, 8, 0, Math.PI * 2, 0, Math.PI / 2), '#FBF7EE', 0, -.06, 0); add(p, new T.CylinderGeometry(.018, .018, .3, 6), '#4A2F1E', 0, .24, 0); add(p, new T.SphereGeometry(.035, 8, 6), '#E8453A', 0, .4, 0); });
  icon('cancau', p => {""")
rep("""try { bubIcon(b, ICON.cancau); } catch (e) {} b.quaternion.copy(cam.quaternion); b.position.set(bx - .7, .75""",
    """try { bubIcon(b, ICON.phao || ICON.cancau); } catch (e) {} b.quaternion.copy(cam.quaternion); b.position.set(bx - .7, .75""")

# 3. Phao nổi dập dềnh dưới ngọn cần cả lúc chưa câu
rep("""  const m = new T.Mesh(new T.SphereGeometry(1, 10, 6), f.tier >= 4 ? FSH.do : f.tier >= 3 ? FSH.tim : f.tier === 2 ? FSH.gold : FSH.mat); m.scale.set(sc * 1.9, .01, sc * .75);""",
"""  const m = new T.Mesh(FSHG.body, f.tier >= 4 ? FSH.do : f.tier >= 3 ? FSH.tim : f.tier === 2 ? FSH.gold : FSH.mat); m.scale.set(sc * 1.9, 1, sc * .75); { const tl = new T.Mesh(FSHG.tail, m.material); tl.position.x = -.7; tl.renderOrder = 4; m.add(tl); }   /* bóng cá có đuôi quẫy, đầu hướng theo chiều bơi */""")
rep("""function fshClear(){ for (const o of FSH.list){ S.remove(o.m); o.m.geometry.dispose(); } FSH.list = []; }""",
"""const FSHG = (() => { const b = new T.Shape(); b.moveTo(1, 0); b.bezierCurveTo(1, .38, .55, .5, .2, .5); b.bezierCurveTo(-.25, .5, -.55, .25, -.72, .12); b.lineTo(-.72, -.12); b.bezierCurveTo(-.55, -.25, -.25, -.5, .2, -.5); b.bezierCurveTo(.55, -.5, 1, -.38, 1, 0);
  const tl = new T.Shape(); tl.moveTo(.04, 0); tl.lineTo(-.34, .5); tl.quadraticCurveTo(-.26, 0, -.34, -.5); tl.lineTo(.04, 0);
  const fl = g => { g.rotateX(-Math.PI / 2); return g; }; return { body: fl(new T.ShapeGeometry(b, 10)), tail: fl(new T.ShapeGeometry(tl, 6)) }; })();
function fshClear(){ for (const o of FSH.list) S.remove(o.m); FSH.list = []; }   /* hình bóng dùng chung, không dispose */""")
rep("""    o.m.rotation.y = -o.a; if (o.m.material !== FSH.mat)""",
"""    o.m.rotation.y = -o.a; { const tl = o.m.children[0]; if (tl){ o.wag = (o.wag || R(0, 6)) + dt * (o === FM.tgt && (FM.ph === 'come' || FM.ph === 'reel') ? 16 : FM.ph === 'bite' && o === FM.tgt ? 22 : 6 + o.sp * 10); tl.rotation.y = Math.sin(o.wag) * .45; } } if (o.m.material !== FSH.mat)""")
rep("""  if (FM.on) return fmTick(t, dt); CAUV.ph.visible = false; CAUV.line.visible = false;""",
"""  if (FM.on) return fmTick(t, dt); { const ph = CAUV.ph, pos = CAUV.line.geometry.attributes.position; ph.visible = true; CAUV.line.visible = true; ph.position.copy(CAUV.rest); ph.position.y += Math.sin(t * 2) * .006; pos.setXYZ(0, CAUV.tip.x, CAUV.tip.y, CAUV.tip.z); pos.setXYZ(1, ph.position.x, ph.position.y + .1, ph.position.z); pos.needsUpdate = true; }""")
rep("""  else showLine = FM.ph !== 'aim' && FM.ph !== 'done';""",
    """  else { ph.position.copy(CAUV.rest); ph.position.y += Math.sin(t * 2) * .006; }
  if (FM.tut && FM.tutF && FSH.list.includes(FM.tutF) && (FM.ph === 'aim' || FM.ph === 'empty')){ const rg = tutRing(), s0 = 1 + .25 * Math.abs(Math.sin(t * 3)); rg.visible = true; rg.position.set(FM.tutF.m.position.x, WLR + .02, FM.tutF.m.position.z); rg.scale.set(s0, s0, s0); } else if (TUTR) TUTR.visible = false;""")
rep("""  ph.visible = showLine; CAUV.line.visible = showLine; if (showLine){ pos.setXYZ(0, CAUV.tip.x, CAUV.tip.y, CAUV.tip.z); pos.setXYZ(1, ph.position.x, ph.position.y + .08, ph.position.z); pos.needsUpdate = true; } }""",
    """  ph.visible = showLine; CAUV.line.visible = showLine; if (showLine){ pos.setXYZ(0, CAUV.tip.x, CAUV.tip.y, CAUV.tip.z); pos.setXYZ(1, ph.position.x, ph.position.y + .1, ph.position.z); pos.needsUpdate = true; } }""")

# 4. Nút hành động một chỗ, đổi theo nhịp: Quăng câu · Chờ cá · GIỰT! · Giữ để kéo
rep("""else if (b.dataset.f === 'ok'){ FM.ph = 'aim'; fuiAim(); }""",
    """else if (b.dataset.f === 'ok'){ FM.ph = 'aim'; fuiAim(); } else if (b.dataset.f === 'cast'){ fmCastBtn(); } else if (b.dataset.f === 'giut'){ if (FM.ph === 'bite') fmTap(0, 0); }""")
rep("""<small>${cauLeft() > 0 ? `Chạm hay kéo thả tới bóng cá để quăng · còn ${cauLeft()} con hôm nay` : `Hôm nay câu đủ ${cauCap()} con rồi`}</small></span><button class="x" data-f="x" aria-label="Thôi câu">×</button></div><div class="fmois">${chip('', 1)}${chip('trun', moiHas('trun'), 'trun')}${chip('com', moiHas('com'), 'com')}${chip('tep', moiHas('tep'), 'tep')}${moiHas('sau') || FM.bait === 'sau' ? chip('sau', moiHas('sau'), 'sau') : ''}</div>`); };""",
    """<small>${cauLeft() > 0 ? (FM.tut ? 'Chạm vào bóng cá có vòng sáng để quăng câu' : `Chạm vào bóng cá dưới nước để quăng · còn ${cauLeft()} con hôm nay`) : `Hôm nay câu đủ ${cauCap()} con rồi`}</small></span><button class="x" data-f="x" aria-label="Thôi câu">×</button></div>${FM.tut ? '' : `<div class="fmois">${chip('', 1)}${chip('trun', moiHas('trun'), 'trun')}${chip('com', moiHas('com'), 'com')}${chip('tep', moiHas('tep'), 'tep')}${moiHas('sau') || FM.bait === 'sau' ? chip('sau', moiHas('sau'), 'sau') : ''}</div>`}<button class="fact cast" data-f="cast" ${cauLeft() > 0 ? '' : 'disabled'}><i class="fic"><img src="${ICON.phao || ICON.cancau}" alt=""></i><span>Quăng câu</span></button>`); };
const fuiWait = nib => fuiSet(`<div class="fbar"><img src="${ICON.phao || ICON.cancau}" alt=""><span><b>${nib ? 'Cá đang rỉa mồi…' : 'Chờ cá ăn mồi…'}</b><small>${nib ? 'Phao rung là cá thử mồi, chìm hẳn mới giựt' : 'Ngồi yên, phao chìm là giựt liền'}</small></span><button class="x" data-f="x" aria-label="Thôi câu">×</button></div><button class="fact wait${nib ? ' nib' : ''}" disabled><i class="fic"><img src="${ICON.phao || ICON.cancau}" alt=""></i><span>${nib ? 'Cá rỉa mồi' : 'Chờ cá'}<em class="fdots"><b></b><b></b><b></b></em></span></button>`);
const fuiBite = () => fuiSet(`<div class="fbar"><img src="${ICON.phao || ICON.cancau}" alt=""><span><b>Phao chìm rồi!</b><small>Chạm liền để giựt cần</small></span><button class="x" data-f="x" aria-label="Thôi câu">×</button></div><button class="fact giut" data-f="giut"><i class="fic bang">!</i><span>GIỰT!</span></button>`);
let TUTR = null; const tutRing = () => { if (!TUTR){ TUTR = new T.Mesh(new T.RingGeometry(.2, .26, 36), new T.MeshBasicMaterial({ color: '#FFE36A', transparent: true, opacity: .9, depthWrite: false })); TUTR.rotation.x = -Math.PI / 2; TUTR.renderOrder = 5; TUTR.userData.keep = true; S.add(TUTR); } return TUTR; };
function tutSpawn(){ if (FM.tutF && FSH.list.includes(FM.tutF)) return; const o = fshSpawn('rophi', { x: bx - 1.3, z: R0 + 1.05 }); o.sp = .03; o.life = 1e6; FM.tutF = o; }
function fmCastBtn(){ if (FM.ph !== 'aim' && FM.ph !== 'empty') return; let o = FM.tut && FM.tutF && FSH.list.includes(FM.tutF) ? FM.tutF : null; if (!o){ let bd = 1e9; for (const f of FSH.list){ const d = Math.hypot(f.m.position.x - CAUV.rest.x, f.m.position.z - CAUV.rest.z); if (d < bd){ bd = d; o = f; } } } if (o) fmCast(o.m.position.x + .05, o.m.position.z); else fmCast(bx - 1.2, R0 + 1.4); }""")
rep("""const fuiReel = () => fuiSet(`<div class="freel"><b>Giữ tay để kéo · cá vùng thì buông</b><div class="ften"><i></i><u></u></div><div class="fprog"><i></i></div><button class="fauto${ST.autoReel ? ' on' : ''}" data-f="auto">${ST.autoReel ? 'Tự kéo: bật' : 'Tự kéo: tắt'}</button><button class="x" data-f="x" aria-label="Thôi câu">×</button></div>`);""",
    """const fuiReel = () => fuiSet(`<div class="freel"><b>Kéo cá vô bờ</b><div class="frow"><small>Dây</small><div class="ften"><i></i><u></u></div></div><div class="frow"><small>Cá</small><div class="fprog"><i></i><img class="fpf" src="${ICON[FM.tgt && FM.tgt.k] || ICON.caro}" alt=""></div></div>${FM.tut ? '' : `<button class="fauto${ST.autoReel ? ' on' : ''}" data-f="auto">${ST.autoReel ? 'Tự kéo: bật' : 'Tự kéo: tắt'}</button>`}<button class="x" data-f="x" aria-label="Thôi câu">×</button></div><div class="fact hold"><i class="fic"><img src="${ICON.cancau}" alt=""></i><span>Giữ để kéo</span></div>`);""")
rep("""if (hd) hd.textContent = ST.autoReel ? (v ? 'Cá vùng, dây tự chùng…' : 'Đang tự kéo…') : v ? 'Cá vùng! Buông tay ra' : FM.hold ? 'Đang kéo…' : 'Giữ tay để kéo'; FUI.classList.toggle('vung', v); }""",
    """if (hd) hd.textContent = v ? 'Cá vùng! Dây căng quá' : 'Kéo cá vô bờ'; { const fa = FUI.querySelector('.fact.hold span'); if (fa) fa.textContent = ST.autoReel ? 'Đang tự kéo…' : v ? 'Buông tay!' : FM.hold ? 'Đang kéo…' : 'Giữ để kéo'; const fh = FUI.querySelector('.fact.hold'); if (fh) fh.classList.toggle('down', !!FM.hold && !v); } FUI.classList.toggle('vung', v); }""")
rep(""".fbtns{display:flex;gap:8px;justify-content:center;margin-top:6px}""",
    """.fui .fact{box-sizing:border-box;position:relative;display:flex;align-items:center;justify-content:center;gap:12px;width:100%;margin-top:10px;min-height:64px;padding:0 18px 0 10px;border:0;border-radius:22px;font:400 25px var(--f-game);letter-spacing:.3px;color:#fff;text-shadow:0 2px 0 rgba(40,60,30,.45);--c1:#8CC46A;--c2:#5E9446;--c3:#3F6E2E;background:linear-gradient(180deg,var(--c1) 0%,var(--c2) 70%);box-shadow:inset 0 3px 0 rgba(255,255,255,.35),inset 0 -4px 0 rgba(0,0,0,.12),0 0 0 3px #FFFBF2,0 0 0 5px var(--c3),0 7px 0 2px var(--c3),0 12px 22px rgba(43,52,70,.28);cursor:pointer;user-select:none;-webkit-user-select:none;pointer-events:auto;overflow:hidden;transition:transform .08s}
.fui .fact::after{content:'';position:absolute;top:0;left:-60%;width:40%;height:100%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.4),transparent);transform:skewX(-20deg);animation:fShine 2.6s ease-in-out infinite}@keyframes fShine{0%,60%{left:-60%}100%{left:130%}}
.fui .fact:active,.fui .fact.down{transform:translateY(4px);box-shadow:inset 0 3px 0 rgba(255,255,255,.3),0 0 0 3px #FFFBF2,0 0 0 5px var(--c3),0 3px 0 2px var(--c3),0 6px 12px rgba(43,52,70,.25)}
.fui .fact .fic{flex:none;display:grid;place-items:center;width:48px;height:48px;border-radius:50%;background:#FFFBF2;box-shadow:inset 0 -3px 0 rgba(0,0,0,.08),0 2px 0 var(--c3)}.fui .fact .fic img{width:40px;height:40px}
.fui .fact.cast .fic{animation:fBob 1.4s ease-in-out infinite}@keyframes fBob{50%{transform:translateY(-4px) rotate(-6deg)}}
.fui .fact:disabled{opacity:1;cursor:default}
.fui .fact.wait{--c1:#D8CDB6;--c2:#BEB198;--c3:#978B74;color:#FFFBF2;text-shadow:0 2px 0 rgba(90,70,40,.35)}.fui .fact.wait::after{display:none}.fui .fact.wait .fic img{animation:fFloat 1.8s ease-in-out infinite}@keyframes fFloat{50%{transform:translateY(3px)}}.fui .fact.wait.nib .fic img{animation:fNib .22s ease-in-out infinite}@keyframes fNib{50%{transform:translateY(4px) rotate(4deg)}}
.fui .fdots{display:inline-flex;gap:4px;margin-left:6px;vertical-align:middle}.fui .fdots b{width:7px;height:7px;border-radius:50%;background:#FFFBF2;animation:fDot 1.2s infinite}.fui .fdots b:nth-child(2){animation-delay:.2s}.fui .fdots b:nth-child(3){animation-delay:.4s}@keyframes fDot{0%,60%,100%{transform:none;opacity:.5}30%{transform:translateY(-6px);opacity:1}}
.fui .fact.giut{--c1:#F2805C;--c2:#D9573A;--c3:#9C3620;font-size:31px;animation:fG .42s ease-in-out infinite}.fui .fact.giut .fic.bang{font:400 38px var(--f-game);color:#D9573A;text-shadow:none;animation:fBang .42s ease-in-out infinite}@keyframes fG{0%,100%{transform:translateX(0)}25%{transform:translateX(-4px)}75%{transform:translateX(4px)}}.fui .fact.giut{box-shadow:inset 0 3px 0 rgba(255,255,255,.35),inset 0 -4px 0 rgba(0,0,0,.12),0 0 0 3px #FFFBF2,0 0 0 5px var(--c3),0 7px 0 2px var(--c3),0 0 26px 6px rgba(242,128,92,.55)}@keyframes fBang{50%{transform:scale(1.2) rotate(8deg)}}
.fui .fact.hold{--c1:#7FB0DE;--c2:#5E8FC0;--c3:#3D6890}.fui.vung .fact.hold{--c1:#F2805C;--c2:#D9573A;--c3:#9C3620;animation:fG .3s infinite}.fui .fact.hold .fic img{transition:transform .2s}.fui .fact.hold.down .fic img{animation:fReel .5s linear infinite}@keyframes fReel{50%{transform:rotate(-14deg)}}
.fui .frow{display:flex;align-items:center;gap:8px;margin-top:8px}.fui .frow small{width:28px;font:700 12px var(--f-body);color:#8A5D3B}.fui .frow .ften,.fui .frow .fprog{flex:1;margin-top:0}.fui .fprog{overflow:visible}.fui .fpf{position:absolute;top:50%;left:0;width:34px;height:34px;transform:translate(-50%,-50%) scaleX(-1);transition:left .08s;filter:drop-shadow(0 2px 0 rgba(0,0,0,.15))}
.fbang{position:fixed;z-index:11;transform:translate(-50%,-100%);font:400 54px var(--f-game);color:#FFE36A;-webkit-text-stroke:3px #A83E26;text-shadow:0 4px 0 #A83E26;pointer-events:none;animation:fB 1.2s ease-out forwards}@keyframes fB{0%{transform:translate(-50%,-60%) scale(.3)}20%{transform:translate(-50%,-110%) scale(1.25)}35%{transform:translate(-50%,-100%) scale(1)}80%{opacity:1}100%{opacity:0;transform:translate(-50%,-130%)}}
.fbtns{display:flex;gap:8px;justify-content:center;margin-top:6px}""")

rep("""if (pg) pg.style.width = Math.min(100, FM.prog * 100) + '%';""", """if (pg) pg.style.width = Math.min(100, FM.prog * 100) + '%'; { const pf = FUI.querySelector('.fpf'); if (pf) pf.style.left = Math.min(100, FM.prog * 100) + '%'; }""")
rep("""function cauTick(t, dt){ const on = cauOn() && !VISIT; CAUV.root.visible = on; CAUV.b.visible = false; CAUV.hit.visible = on; if (!on){ if (FM.on) fmExit(); return; }""",
    """function cauTick(t, dt){ const on = cauOn() && !VISIT; CAUV.root.visible = on; CAUV.b.visible = false; CAUV.hit.visible = on; if (!on){ if (FM.on) fmExit(); return; } rodBend(t, dt);""")
# 5. Nhịp câu: hiện nút theo nhịp, nới thời gian giựt, lần đầu dễ, lỡ tay không phạt ở 5 con đầu, lỗi là toast
rep("""if (FM.t <= 0){ FM.ph = FM.tgt ? 'come' : 'wait'; FM.t = FM.tgt ? 0 : FM.wait; for (let i = 0; i < 6; i++)""",
    """if (FM.t <= 0){ FM.ph = FM.tgt ? 'come' : 'wait'; FM.t = FM.tgt ? 0 : FM.wait; fuiWait(0); for (let i = 0; i < 6; i++)""")
rep("""FM.ph = 'nibble'; FM.nib = 1 + Math.floor(Math.random() * 3); FM.t = R(.5, .9);""",
    """FM.ph = 'nibble'; FM.nib = FM.tut ? 1 : 1 + Math.floor(Math.random() * 3); FM.t = R(.5, .9); fuiWait(1);""")
rep("""if (FM.nib <= 0){ FM.ph = 'bite'; FM.t = FISHK[FM.tgt.k].tier ? .75 : .95; sfx('pop'); buzz(25);""",
    """if (FM.nib <= 0){ FM.ph = 'bite'; FM.t = FM.tut ? 3 : FISHK[FM.tgt.k].tier ? 1.3 : 1.5; fuiBite(); { pv.set(FM.bob.x, .35, FM.bob.z).project(cam); const d = document.createElement('div'); d.className = 'fbang'; d.textContent = '!'; d.style.left = ((pv.x + 1) / 2 * innerWidth) + 'px'; d.style.top = ((1 - pv.y) / 2 * innerHeight) + 'px'; document.body.appendChild(d); setTimeout(() => d.remove(), 1200); } sfx('pop'); buzz(25);""")
rep("""  if (FM.ph === 'nibble'){ fmLose('Giựt sớm quá, cá giựt mình bỏ đi rồi. Đợi phao chìm hẳn nghe.'); return; } if (FM.ph === 'come' || FM.ph === 'wait'){ fmLose('Chưa có cá ăn mồi mà. Ngồi im chờ chút.'); return; }""",
    """  if (FM.ph === 'nibble'){ if (FM.tut || (ST.cau.tot || 0) < 5) return toast('Cá mới rỉa thôi, đợi phao chìm hẳn rồi giựt nghe.'); fmLose('Giựt sớm quá, cá giựt mình bỏ đi rồi. Đợi phao chìm hẳn nghe.'); return; } if (FM.ph === 'come' || FM.ph === 'wait'){ toast('Chưa có cá ăn mồi, ngồi yên chờ chút nghe.'); return; }""")
rep("""else bark('Chạm xuống mặt sông mới quăng câu được.'); return; }""",
    """else toast('Chạm xuống mặt sông mới quăng câu được.'); return; }""")
rep("""function fmLose(msg){ if (FM.tgt){ FM.tgt.a += Math.PI; FM.tgt.sp = .9; FM.tgt.life = 2; } FM.tgt = null; FM.ph = 'aim'; bark(msg); fuiAim(); }""",
    """function fmLose(msg){ if (FM.tgt){ FM.tgt.a += Math.PI; FM.tgt.sp = .9; FM.tgt.life = 2; } FM.tgt = null; FM.ph = 'aim'; toast(msg); if (FM.tut){ FM.tutF = null; tutSpawn(); } fuiAim(); }""")
rep("""FM.ph = 'aim'; bark('Chỗ này vắng cá. Quăng gần bóng cá thử coi.'); fuiAim(); }""",
    """FM.ph = 'aim'; toast('Chỗ này vắng cá. Quăng gần bóng cá thử coi.'); fuiAim(); }""")
rep("""if (FM.hold){ FM.prog += dt * (.24 - f.str * .1) * (ST.autoReel ? .8 : 1); FM.ten += dt * (.35 + f.str * .5) + (v ? dt * (1.1 + f.str * 1.4) : 0); }""",
    """if (FM.hold){ FM.prog += dt * (.24 - f.str * .1) * (ST.autoReel ? .8 : 1) * (FM.tut ? 1.4 : 1); FM.ten += (dt * (.35 + f.str * .5) + (v ? dt * (1.1 + f.str * 1.4) : 0)) * (FM.tut ? .5 : 1); }""")
rep("""function fmCatch(k, junk){ FM.ph = 'done';""",
    """function fmCatch(k, junk){ FM.ph = 'done'; if (FM.tut && !junk){ FM.tut = 0; FM.tutF = null; ST.seen.cauTut = 1; }""")
# lần đầu vào câu: bóng cá chắc chắn ở sát cầu, vòng sáng chỉ chỗ; bỏ đoạn Ngoại giảng luật (giao diện tự dẫn)
rep("""FM.on = true; FM.ph = 'aim'; document.body.classList.add('fishing');""",
    """FM.on = true; FM.ph = 'aim'; FM.tut = ST.seen.cauTut ? 0 : 1; if (FM.tut){ FM.bait = ''; tutSpawn(); } document.body.classList.add('fishing');""")
rep("""  sayOnce('cau2', 'Thấy bóng cá dưới nước hông? Bóng to là cá bự. Quăng câu gần nó, phao rỉa lăn tăn là cá thử mồi, chìm hẳn mới giựt.', 'vui'); stepMark('fish0'); }""",
    """  stepMark('fish0'); }""")
rep("""function fmExit(){ FM.on = false; FM.ph = 'aim'; FM.tgt = null;""",
    """function fmExit(){ FM.on = false; FM.ph = 'aim'; FM.tgt = null; FM.tutF = null; if (TUTR) TUTR.visible = false;""")
rep("""const FM = { bait: '', used: '', on: false, ph: 'aim',""",
    """const FM = { tut: 0, tutF: null, bait: '', used: '', on: false, ph: 'aim',""")

# 6. Thẻ "Về vườn ngày N/7" không bật đè lúc đang câu hay đang mở bảng: chờ rảnh rồi mới hiện
rep("""function ddShow(extra = ''){ const D = ST.dd; if (!D) return;""", """function ddShow(extra = ''){ const D = ST.dd; if (!D) return; if (FM.on || busy()) return setTimeout(() => ddShow(extra), 2500);""")
open(dst, 'w', encoding='utf8').write(s)
print('ok', dst)
