# v160 -> v161:
# 1) ghe ông Bảy Kiếng đậu chồng lên ghe tam bản (cùng một chỗ trên rạch): dời ghe ông Bảy xuống phía dưới, ghe tam bản nhích ra khỏi ghe bẹo.
# 2) "Câu trên ghe": ghe nhảy cóc ra giữa sông (đổi toạ độ tức thì, lại nằm khuất sau tán cây). Giờ ghe chèo êm ra chỗ thấy được, chèo êm về.
# 3) bảng Ghe tam bản có thêm nút "Chèo ra câu" (trước chỉ thấy trong lúc câu cá).
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), n, a[:60])
    s = s.replace(a, b)
rep("BUILD = 'v160'", "BUILD = 'v161'")
# 1) chỗ đậu
rep("root = DYN(G(bx + 6.5, WLR + .1, R0 + 1.25, -.08)), gg = new T.Group();", "root = DYN(G(bx + 10.3, WLR + .1, R0 + 1.25, -.08)), gg = new T.Group();")
rep("lo: 6, at: [8.6, R0 + 1.25],", "lo: 6, at: [6.6, R0 + 1.25],")
# ghe tam bản của mình đậu sát cầu ván; ghe bẹo ghé thì đậu phía ngoài (đổi chỗ hai ghe), để ghe mình chèo ra câu khỏi phải lách qua ghe bẹo
rep("const root = DYN(G(bx + 3.4, WLR + .1, R0 + 1.25, -.08)), pr = ROOT; ROOT = root; const ps = sd, nL = LIGHTS.length; root.add(gheBeo());", "const root = DYN(G(bx + 6.9, WLR + .1, R0 + 1.25, -.08)), pr = ROOT; ROOT = root; const ps = sd, nL = LIGHTS.length; root.add(gheBeo());")
rep("b.position.set(bx + 3.2, 1.0 + Math.sin(t * 2) * .035, R0 + 1.25);", "b.position.set(bx + 6.7, 1.0 + Math.sin(t * 2) * .035, R0 + 1.25);")
# 2) chèo êm
rep("function tbGheMove(){ try { if (FM.ghe){ TBV.root.position.x = bx - 2.6; TBV.root.position.z = R0 + 1.3; } else { TBV.root.position.x = TB.at[0]; TBV.root.position.z = TB.at[1]; } for (let i = 0; i < 10; i++) puff('drop', TBV.root.position.x + R(-.6, .6), .05, TBV.root.position.z + R(-.2, .2), 1, '#9cc6e0', .7); } catch (e) {} }",
    "function tbGheMove(quiet){ try { const P = TBV.root.position, out = !!FM.ghe, w = { x0: P.x, z0: P.z, x1: out ? bx + 3.0 : TB.at[0], z1: out ? R0 + 1.77 : TB.at[1], t0: -1, pf: 0 }; w.d = Math.max(1.1, Math.min(2.6, Math.hypot(w.x1 - w.x0, w.z1 - w.z0) * .95)); TBV.tw = w; if (!quiet && FM.on) camTo(new T.Vector3(out ? bx + 1.5 : bx - .4, .2, out ? R0 + 1.4 : R0 + 1.25), cam.zoom, w.d * .9); } catch (e) {} }")
rep("function fmExit(){ if (FM.ghe){ FM.ghe = false; tbGheMove(); }", "function fmExit(){ if (FM.ghe){ FM.ghe = false; tbGheMove(1); }")
rep("TBV.root.rotation.z = Math.sin(t * .8) * .02; TBV.root.rotation.x = Math.sin(t * 1.2) * .015;",
    "TBV.root.rotation.z = Math.sin(t * .8) * .02; TBV.root.rotation.x = Math.sin(t * 1.2) * .015;\n"
    "  if (TBV.tw){ const w = TBV.tw, P = TBV.root.position; if (w.t0 < 0) w.t0 = t; const k = Math.min(1, (t - w.t0) / w.d), e = k * k * k * (k * (6 * k - 15) + 10), a = Math.sin(e * Math.PI), dir = w.x1 < w.x0 ? -1 : 1;   /* chèo êm: lấy đà, lướt, chậm lại; vòng ra ngoài né xuồng đậu ở bến */\n"
    "    P.x = w.x0 + (w.x1 - w.x0) * e; P.z = w.z0 + (w.z1 - w.z0) * e; TBV.root.rotation.y = -.04 - dir * a * .07; TBV.root.rotation.x += Math.sin(t * 5.5) * .03 * a;\n"
    "    if (k < 1 && t - w.pf > .12){ w.pf = t; puff('drop', P.x - dir * 1.15 + R(-.1, .1), .05, P.z + R(-.18, .18), 1, '#9cc6e0', .45); }\n"
    "    if (k >= 1){ TBV.tw = null; TBV.root.rotation.y = -.04; for (let i = 0; i < 5; i++) puff('drop', P.x + R(-.9, .9), .05, P.z + R(-.25, .25), 1, '#9cc6e0', .5); } }")
rep("else if (loLeft() <= 0) objBub(TBV, { cx: x - .3, cz: z }, ICON.caro, t, .8); }", "else if (loLeft() <= 0 && !FM.ghe && !TBV.tw) objBub(TBV, { cx: x - .3, cz: z }, ICON.caro, t, .8); }")
# 3) nút ra câu trong bảng ghe
rep("  const o = tbChuyen(), okc = o.items.every(([k, q]) => has(k) >= q);",
    "  if (cauOn()) h += UX.title('Câu giữa sông', gLeft() > 0 ? `còn ${gLeft()} lượt hôm nay` : 'hôm nay câu đủ rồi, mai ra tiếp') + UX.cta([UX.btn('tbcau', 'Chèo ra câu', { g: 1, img: ICON.cancau, dis: gLeft() <= 0 })]);\n"
    "  const o = tbChuyen(), okc = o.items.every(([k, q]) => has(k) >= q);")
rep("else if (a === 'tbcho'){ tbChoGo(); return; }", "else if (a === 'tbcho'){ tbChoGo(); return; } else if (a === 'tbcau'){ fmEnter(); if (FM.on && !FM.tut && gLeft() > 0){ FM.ghe = true; fshClear(); tbGheMove(); fuiAim(); } return; }")
# 4) chợ huyện thoáng hơn: nhìn lùi ra, kéo được cả lên xuống, chụm hai ngón (hay lăn chuột) để lại gần / lùi xa; sông và bãi cỏ trải dài ra hai bên, hết cảnh "miếng nền lơ lửng".
rep("M(box(16, .04, 4), grey(C.song), 0, -.16, 3.9, { p: g, cast: false });", "M(box(64, .04, 30), grey(C.song), 0, -.16, 16.9, { p: g, cast: false }); for (const sx of [-1, 1]) M(box(24, .16, 4.9), grey('#8DBF5A'), sx * 20, -.1, -.3, { p: g, cast: false });")
rep("M(box(18, .16, 6), grey('#8DBF5A'), 0, -.1, -5.75, { p: back, cast: false });", "M(box(64, .16, 6), grey('#8DBF5A'), 0, -.1, -5.75, { p: back, cast: false });")
rep("[[-4.6, -4.0, 2.7, .2], [-.4, -4.2, 3.0, -.12], [4.2, -4.0, 2.8, .18]]) dua(x, z, h, l); }", "[[-4.6, -4.0, 2.7, .2], [-.4, -4.2, 3.0, -.12], [4.2, -4.0, 2.8, .18], [-9.6, -1.4, 2.6, -.2], [-11.4, .6, 2.9, .16], [10.2, -1.2, 2.8, .2], [12.2, .5, 2.5, -.15], [-9.0, -4.4, 2.5, .15], [9.4, -4.3, 2.9, -.18]]) dua(x, z, h, l); }")
rep("C.zoom = (MOBILE && innerHeight > innerWidth ? 1.25 : .95) * (cn ? CNX.zoom : 1); const tg = new T.Vector3(CHM.tx, cn ? .55 : .5, cn ? -.35 : .45);",
    "C.zoom = (MOBILE && innerHeight > innerWidth ? 1.02 : .9) * (CHM.zm || 1); const tg = new T.Vector3(CHM.tx, .5, .45 + (CHM.tz || 0));")
rep("CHM.tx = CHM.tx0;", "CHM.tx = CHM.tx0; CHM.tz = 0; CHM.zm = 1;")
rep("tx: CHM.tx, dl: CNX.dl || 0", "tx: CHM.tx, tz: CHM.tz || 0, dl: CNX.dl || 0")
rep("if (Math.abs(dx) > 8) d.moved = true; if (d.moved){", "if (Math.hypot(dx, e.clientY - d.y) > 8) d.moved = true; if (d.moved && CHM.kind !== 'cn'){ const kz = (CHM.cam ? (CHM.cam.right - CHM.cam.left) / CHM.cam.zoom : 6) / innerWidth; CHM.tz = Math.max(-2.2, Math.min(1.6, d.tz - (e.clientY - d.y) * kz * 1.9)); } if (d.moved){")
rep("Math.max(-4.6, Math.min(5.6, d.tx - dx * k * 1.15))", "Math.max(-6.4, Math.min(7.2, d.tx - dx * k * 1.15))")
rep("addEventListener('wheel', e => { if (!CHM.on || CHM.kind !== 'cn'",
    "const chZm = z => { CHM.zm = Math.max(.8, Math.min(1.45, z)); };\n"
    "addEventListener('wheel', e => { if (!CHM.on || CHM.kind === 'cn' || !e.target || e.target.id !== 'c') return; chZm((CHM.zm || 1) * Math.exp(-e.deltaY * .0015)); }, { passive: true });\n"
    "{ const P = new Map(), dist = () => { const a = [...P.values()]; return Math.hypot(a[0].x - a[1].x, a[0].y - a[1].y); }; let pin = null;\n"
    "  addEventListener('pointerdown', e => { if (!CHM.on || CHM.kind === 'cn' || e.target.id !== 'c'){ P.clear(); pin = null; return; } P.set(e.pointerId, { x: e.clientX, y: e.clientY }); if (P.size === 2){ pin = { d: Math.max(20, dist()), z: CHM.zm || 1 }; CHM.drag = null; } });\n"
    "  addEventListener('pointermove', e => { if (!P.has(e.pointerId)) return; P.set(e.pointerId, { x: e.clientX, y: e.clientY }); if (pin && P.size === 2 && CHM.on){ CHM.drag = null; chZm(pin.z * dist() / pin.d); } });\n"
    "  const up = e => { P.delete(e.pointerId); if (P.size < 2) pin = null; }; addEventListener('pointerup', up); addEventListener('pointercancel', up); }\n"
    "addEventListener('wheel', e => { if (!CHM.on || CHM.kind !== 'cn'")
# 5) chợ nổi + bến bà con: bến kéo được bốn phía, chụm tay phóng to; máy quay bến hạ thấp cho thấy trời; chợ nổi kéo ngang xa hơn, chụm tay được
rep("b: [5, 9.2, -5.6, 5, .3, -16.2, 58]", "b: [5, 7.6, -4.4, 5, .5, -16.6, 60]")
rep("for (let i = 0; i < 7; i++){ let a = V.w[i] + (V.c[i] - V.w[i]) * d; if (i === 0 || i === 3) a += x; v[i] = a + (V.b[i] - a) * e; }",
    "for (let i = 0; i < 7; i++){ let a = V.w[i] + (V.c[i] - V.w[i]) * d; if (i === 0 || i === 3) a += x; v[i] = a + (V.b[i] - a) * e; }\n"
    "  { CNX.bxs = (CNX.bxs || 0) + ((CNX.bx || 0) - (CNX.bxs || 0)) * .25; CNX.bzs = (CNX.bzs || 0) + ((CNX.bz || 0) - (CNX.bzs || 0)) * .25; CNX.bms = (CNX.bms || 0) + ((CNX.bzm || 0) - (CNX.bms || 0)) * .2; const ox = CNX.bxs * e, oz = CNX.bzs * e, zk = 1 - .5 * CNX.bms * e; v[0] += ox; v[3] += ox; v[2] += oz; v[5] += oz; for (let i = 0; i < 3; i++) v[i] = v[i + 3] + (v[i] - v[i + 3]) * zk; }")
rep("function cnoBenV(v){ CNX.ben = v ? 1 : 0;", "function cnoBenV(v){ CNX.ben = v ? 1 : 0; CNX.bx = 0; CNX.bz = 0; CNX.bzm = 0;")
rep("CHM.drag = { x: e.clientX, y: e.clientY, tx: CHM.tx, tz: CHM.tz || 0, dl: CNX.dl || 0, moved: false, id: e.pointerId };",
    "CHM.drag = { x: e.clientX, y: e.clientY, tx: CHM.tx, tz: CHM.tz || 0, dl: CNX.dl || 0, bx: CNX.bx || 0, bz: CNX.bz || 0, moved: false, id: e.pointerId };")
rep("if (CHM.kind === 'cn'){ const dy = e.clientY - d.y; if (!d.ax",
    "if (CHM.kind === 'cn'){ const dy = e.clientY - d.y; if (CNX.ben && !CNX.son){ if (Math.hypot(dx, dy) > 8) d.moved = true; if (d.moved){ const kk = 1 - .45 * (CNX.bzm || 0); CNX.bx = Math.max(-2.2, Math.min(2.2, d.bx - dx * 9 / innerWidth * kk)); CNX.bz = Math.max(-5.5, Math.min(1.2, d.bz - dy * 15 / innerHeight * kk)); } return; } if (!d.ax")
rep("CHM.tx = Math.max(-6, Math.min(6, d.tx - dx * 14 / innerWidth * (1 - .6 * d.dl)));", "CHM.tx = Math.max(-8.5, Math.min(6, d.tx - dx * 14 / innerWidth * (1 - .6 * d.dl)));")
# chụm tay + lăn chuột cho chợ nổi và bến
rep("if (!CHM.on || CHM.kind === 'cn' || e.target.id !== 'c'){ P.clear(); pin = null; return; } P.set(e.pointerId, { x: e.clientX, y: e.clientY }); if (P.size === 2){ pin = { d: Math.max(20, dist()), z: CHM.zm || 1 }; CHM.drag = null; } });",
    "if (!CHM.on || (CHM.kind === 'cn' && CNX.son) || e.target.id !== 'c'){ P.clear(); pin = null; return; } P.set(e.pointerId, { x: e.clientX, y: e.clientY }); if (P.size === 2){ pin = { d: Math.max(20, dist()), z: CHM.kind !== 'cn' ? CHM.zm || 1 : CNX.ben ? CNX.bzm || 0 : CNX.dl || 0 }; CHM.drag = null; } });")
rep("if (pin && P.size === 2 && CHM.on){ CHM.drag = null; chZm(pin.z * dist() / pin.d); } });",
    "if (pin && P.size === 2 && CHM.on){ CHM.drag = null; const r = dist() / pin.d; if (CHM.kind !== 'cn') chZm(pin.z * r); else { const z = Math.max(0, Math.min(1, pin.z + (r - 1) * .9)); if (CNX.ben) CNX.bzm = z; else CNX.dl = z; } } });")
rep("if (!CHM.on || CHM.kind !== 'cn' || CNX.ben || !e.target || e.target.id !== 'c') return; CNX.dl = Math.max(0, Math.min(1, (CNX.dl || 0) - e.deltaY * .0015));",
    "if (!CHM.on || CHM.kind !== 'cn' || CNX.son || !e.target || e.target.id !== 'c') return; if (CNX.ben){ CNX.bzm = Math.max(0, Math.min(1, (CNX.bzm || 0) - e.deltaY * .0015)); return; } CNX.dl = Math.max(0, Math.min(1, (CNX.dl || 0) - e.deltaY * .0015));")
# bảng tên xuồng: lại gần thì không phình quá 1,4 lần cỡ nhỏ nhất (trước phình tự do, che nhau)
rep("k = Math.max(1, need); o.visible = !(q.far", "k = Math.max(need, Math.min(1, need * 1.4)); o.visible = !(q.far")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
