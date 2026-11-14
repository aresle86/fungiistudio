# v149d: săn cá hiếm bằng lời đồn (Ares duyệt 14/11/2026: "Ok")
# - Sổ cá giấu 4 mảnh của cá rất hiếm / cá hô: chỗ, giờ, trời, mồi; nghe đồn mỗi lần một mảnh
# - nghe đồn: giao đơn nhà bên (1 lần/ngày), chợ huyện (1 lần/ngày), cá đớp rồi nhả khi sai mồi
# - bọt nước sủi ở chỗ cá hiếm nằm khi đủ trời + giờ
# - tỉ lệ: đúng hết 6% (cá hô 2%), chắc chắn sau 12 lần đúng (cá hô 25); sai mồi vẫn 1%
# - con đầu tiên: +500 xu + Ngoại kể chuyện con cá
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)

rep("BUILD = 'v149c'", "BUILD = 'v149d'")

# --- lời đồn: dữ liệu, sổ cá ---
rep("const fHint = (f, got) => {", """const DONX = ['cho', 'gio', 'troi', 'moi'];
for (const k in FISHK) FISHK[k].k = k;
const donTroi = f => [f.mua ? MUAN[f.mua] : '', f.tide ? NUOCN[f.tide] : '', f.moon ? TRANGN[f.moon] : ''].filter(Boolean).join(', ') || 'trời nào cũng được';
const donLab = (f, x) => x === 'cho' ? SPOTN[f.sp] : x === 'gio' ? (f.gio ? f.gio.map(g => GION[g]).join(', ') : 'cả ngày') : x === 'moi' ? 'mồi ' + BAITN[f.bait] : donTroi(f);
const donHas = (k, x) => ((ST.don || {})[k] || '').includes(x[0]) || !!(ST.fishLog[k] || {}).n;
const donHint = f => DONX.map(x => donHas(f.k, x) ? donLab(f, x) : '???').join(' · ');
const donTxt = (f, x) => { const n = f.name.toLowerCase(); return x === 'cho' ? `Nghe nói con ${n} hay nằm ${SPOTN[f.sp]}.` : x === 'gio' ? `Người ta đồn con ${n} chỉ ăn lúc ${donLab(f, 'gio')}.` : x === 'moi' ? `Dân câu nói con ${n} mê ${donLab(f, 'moi')} lắm.` : `Nghe nói phải ${donTroi(f)} mới gặp con ${n}.`; };
function donLearn(k, x){ ST.don = ST.don || {}; if (donHas(k, x)) return 0; ST.don[k] = (ST.don[k] || '') + x[0]; save(); return 1; }
function donGive(){ const ks = Object.keys(FISHK).filter(k => FISHK[k].tier >= 3 && !(ST.fishLog[k] || {}).n && DONX.some(x => !donHas(k, x))); if (!ks.length) return null;
  const ss = ks.filter(k => { const f = FISHK[k]; return !f.mua || (f.mua === 'nn' ? nnOn() : f.mua === muaSong()); }), k = pick(ss.length ? ss : ks), x = pick(DONX.filter(x => !donHas(k, x))); donLearn(k, x); return { k, x, txt: donTxt(FISHK[k], x) }; }
const DONS = { rodauvang: 'Hồi Ngoại mười tuổi, ông cố câu được con rô đầu vàng, năm đó lúa trúng mùa. Giờ tới lượt con rồi đó.', locbong: 'Con lóc bông này chắc là cháu con Ngoại thấy hồi con gái. Nó canh dưới bến cả đời, giờ mới chịu lên gặp con.', hu: 'Ông ngoại con câu được con cá hu một đêm tối trời, về kể cả năm không chán. Giờ con cũng có chuyện để kể rồi.', cadua: 'Mùa khô nước mặn lên, cá dứa theo con nước vô tận bến mình. Khô cá dứa hồi xưa là quà biếu quý nhất xóm.', caho: 'Cá hô là ông hoàng sông Tiền. Con chụp hình rồi thả nó về, để con cháu sau này còn thấy.' };
const fHint = (f, got) => {""")
rep("""  if (f.tier >= 4) return got ? 'Đã chụp hình, thả về sông' : `${s2} · ${TRANGN[f.moon]} · mồi gì Ngoại quên rồi`;""",
    """  if (f.tier >= 3 && !got) return donHint(f);
  if (f.tier >= 4) return 'Đã chụp hình, thả về sông';""")
rep("""  if (f.tier >= 3 && !got) return `${s2} · ${g}${f.mua ? ' · ' + MUAN[f.mua] : ''}${f.tide ? ' · ' + NUOCN[f.tide] : ''}${f.moon ? ' · ' + TRANGN[f.moon] : ''} · mồi gì Ngoại quên rồi`;\n""", "")

# --- nghe đồn khi giao đơn nhà bên ---
rep("bump('ord'); ordAfter();", """bump('ord'); ordAfter(); try { if (cauOn() && ST.donD !== dayKey()){ const r = donGive(); if (r){ ST.donD = dayKey(); setTimeout(() => say(`${o.who} kể: ${r.txt}`, 'vui', { idle: true }), 2600); } } } catch (e) {}""")

# --- nghe đồn ở chợ huyện ---
rep("""CHM.tx = CHM.tx0; ctl.enabled = false; document.body.classList.add('chon'); $('#chUi').hidden = false;""",
    """CHM.tx = CHM.tx0; ctl.enabled = false; document.body.classList.add('chon'); $('#chUi').hidden = false;
    try { if (cauOn() && ST.donC !== dayKey()){ const r = donGive(); if (r){ ST.donC = dayKey(); setTimeout(() => chSay(r.txt, 'Ông Tám bán cần câu'), ST.seen.ch1 ? 900 : 6500); } } } catch (e) {}""")

# --- tỉ lệ mới + cá đớp rồi nhả khi sai mồi ---
rep("""  if (rc.length){ const C = ST.cau; C.pity = (C.pity || 0) + 1; const r4 = rc.some(k => FISHK[k].tier === 4); if (Math.random() < (r4 ? .04 : .015) + Math.max(0, C.pity - 30) * .015){ const a = R(0, 6.28); FM.tgt = fshSpawn(pick(rc), { x: FM.bob.x + Math.cos(a) * .7, z: Math.max(FAREA.z0, Math.min(FAREA.z1, FM.bob.z + Math.sin(a) * .5)) }); FM.wait = 0; } } }""",
    """  const rn = Object.keys(FISHK).filter(k => { const f = FISHK[k]; return f.tier >= 3 && f.sp === sp && f.bait !== FM.bait && fAvail(f); }), hook = k => { const a = R(0, 6.28); FM.tgt = fshSpawn(k, { x: FM.bob.x + Math.cos(a) * .7, z: Math.max(FAREA.z0, Math.min(FAREA.z1, FM.bob.z + Math.sin(a) * .5)) }); FM.wait = 0; };
  if (rc.length){ const C = ST.cau; C.pity = (C.pity || 0) + 1; const t3 = rc.filter(k => FISHK[k].tier === 3); if (C.pity >= (t3.length ? 12 : 25) || Math.random() < (t3.length ? .06 : .02)) hook(pick(t3.length ? t3 : rc)); }   // đúng hết: 6% (cá hô 2%), chắc chắn sau 12 (25) lần
  else if (rn.length){ if (Math.random() < .01) hook(pick(rn));   // sai mồi vẫn 1%
    else { const k = pick(rn), dk = dayKey() + k; if (ST.donM !== dk && Math.random() < .15){ ST.donM = dk; const f = FISHK[k], xs = DONX.filter(x => x !== 'moi' && !donHas(k, x)); if (xs.length) donLearn(k, pick(xs)); const bt = BAITN[FM.bait];
      setTimeout(() => { if (!FM.on) return; for (let i = 0; i < 14; i++) puff('drop', FM.bob.x, .05, FM.bob.z, 1, '#9cc6e0', 1); buzz(25); say(`Con ${f.name.toLowerCase()} đớp rồi nhả! ${bt ? `Nó chê mồi ${bt} rồi.` : 'Nó đòi có mồi.'}`, 'vui', { now: true }); }, 1800); } } } }""")

# --- con đầu tiên: +500 xu + Ngoại kể chuyện ---
rep("if (f.tier >= 3) C2.pity = 0;", "if (f.tier >= 3){ C2.pity = 0; if (first){ ST.xu += 500; setTimeout(() => coinPop('+500 xu · con đầu tiên', '#C9A0F0'), 700); } }")
rep("if (bon) setTimeout(() => say(`Mồi ${BAITN[f.bait]}", "if (bon && !(first && f.tier >= 3)) setTimeout(() => say(`Mồi ${BAITN[f.bait]}")
rep("else if (f.tier >= 3) setTimeout(() => say('Trời đất, con này cả đời Ngoại mới thấy vài lần! Ghi vô Sổ cá liền đi con.', 'vui', { now: true }), 900); }",
    "else if (f.tier >= 3) setTimeout(() => say(first && DONS[k] ? DONS[k] : 'Trời đất, con này cả đời Ngoại mới thấy vài lần! Ghi vô Sổ cá liền đi con.', 'vui', { now: true }), 900); }")

# --- bọt nước điềm: đủ trời + giờ thì nước sủi bọt ở chỗ cá hiếm nằm ---
rep("function fmCast(x, z){", """const DONB = (() => { const g = new T.Group(), ms = []; for (let i = 0; i < 6; i++){ const m = new T.Mesh(new T.SphereGeometry(.05, 8, 6), new T.MeshBasicMaterial({ color: '#F4FBFF', transparent: true, opacity: .9, depthWrite: false })); m.renderOrder = 5; g.add(m); ms.push(m); } g.visible = false; S.add(g); return { g, ms, at: {}, k: '', chk: -9 }; })();
function donSpot(sp){ if (DONB.at[sp]) return DONB.at[sp]; const pts = []; for (let i = 0; i < 400; i++){ const x = R(FAREA.x0 + .4, FAREA.x1 - .4), z = R(R0 + .35, R1 - .25); if (spotOf(x, z) === sp && Math.hypot(x - CAUV.rest.x, z - CAUV.rest.z) > (sp === 'gan' ? .6 : 1.8) && Math.hypot(x - BOAT.position.x, z - BOAT.position.z) > 1.2) pts.push([x, z]); }   /* tránh cầu bến và xuồng che mất */
  if (!pts.length) return DONB.at[sp] = { x: CAUV.rest.x, z: CAUV.rest.z + .8 }; const mx = pts.reduce((a, p) => a + p[0], 0) / pts.length, mz = pts.reduce((a, p) => a + p[1], 0) / pts.length; let b = pts[0], bd = 1e9; for (const p of pts){ const d = Math.hypot(p[0] - mx, p[1] - mz); if (d < bd){ bd = d; b = p; } } return DONB.at[sp] = { x: b[0], z: b[1] }; }
function donTick(t){ if (!cauOn()){ DONB.g.visible = false; return; } if (t - DONB.chk > 2){ DONB.chk = t; const ks = Object.keys(FISHK).filter(k => FISHK[k].tier >= 3 && fAvail(FISHK[k])); DONB.k = ks.length ? ks[0] : ''; }
  DONB.g.visible = !!DONB.k; if (!DONB.k) return; const p = donSpot(FISHK[DONB.k].sp); DONB.ms.forEach((m, i) => { const ph = (t * .7 + i / 6) % 1, a = i * 2.1; m.position.set(p.x + Math.cos(a) * .12 * (1 + ph), WLR + .02 + ph * .03, p.z + Math.sin(a) * .09 * (1 + ph)); m.scale.setScalar(.5 + ph); m.material.opacity = .9 * (1 - ph); }); }
function fmCast(x, z){""")
rep("weedTick(t); ordTick(t);", "weedTick(t); ordTick(t); donTick(t);")

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
