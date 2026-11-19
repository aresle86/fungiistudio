# v161 -> v162:
# 1) Bến bà con: nới rạch từ 7,2 ra 10,8 (bờ lùi mỗi bên 1,8), xuồng bà con dạt ra hai bên, cầu khỉ dài theo, nhà và cây lùi theo bờ.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), n, a[:60])
    s = s.replace(a, b)
rep("BUILD = 'v161'", "BUILD = 'v162'")
# bờ
rep("bank(-40, 1.4); bank(8.6, 40); M(box(.5, .12, 12), '#9A8262', 1.5, .02, BZ - 6, { cast: false }); M(box(.5, .12, 12), '#9A8262', 8.5, .02, BZ - 6, { cast: false });",
    "bank(-40, -.4); bank(10.4, 40); M(box(.5, .12, 12), '#9A8262', -.3, .02, BZ - 6, { cast: false }); M(box(.5, .12, 12), '#9A8262', 10.3, .02, BZ - 6, { cast: false });")
rep("if (x > 1.1 && x < 8.9) continue; duanuoc(x, BZ + .15", "if (x > -.7 && x < 10.7) continue; duanuoc(x, BZ + .15")
rep("duanuoc(1.35, BZ - 1 - i * 1.2, 4, .9); duanuoc(8.65, BZ - 1 - i * 1.2, 4, .9);", "duanuoc(-.45, BZ - 1 - i * 1.2, 4, .9); duanuoc(10.45, BZ - 1 - i * 1.2, 4, .9);")
rep("if (x > .4 && x < 9.6) continue; dua(x, BZ - 1.4", "if (x > -1.4 && x < 11.4) continue; dua(x, BZ - 1.4")
# nhà mặt tiền + khói bếp
rep("nha(-1.2, BZ - .2, '#DCC39A', 1, 1.05); nha(10.6, BZ - .3, '#C8A584', 1, 1.1); nha(13.2, BZ - .2, '#D8BE92', 0);",
    "nha(-1.75, BZ - .2, '#DCC39A', 1, 1.05); nha(12.0, BZ - .3, '#C8A584', 1, 1.1); nha(13.9, BZ - .2, '#D8BE92', 0);")
rep("[[-9.3, BZ - .4], [-1.0, BZ - .4]]", "[[-9.3, BZ - .4], [-1.55, BZ - .4]]")
rep("const HX = [-9.5, -5.6, -3.4, -1.2, 10.6, 13.2]", "const HX = [-9.5, -5.6, -3.4, -1.75, 12.0, 13.9]")
# cầu khỉ: dài hơn, 6 nhịp
a = "{ const z = BZ - .1, x0 = 1.2, x1 = 8.8, y = 1.25;"
i0 = s.index(a); i1 = s.index("person(root, 4.6, y + .32, z", i0); seg = s[i0:i1]
seg2 = seg.replace("x0 = 1.2, x1 = 8.8", "x0 = -.6, x1 = 10.6").replace("i <= 4", "i <= 6").replace("i / 4", "i / 6").replace("i < 4", "i < 6").replace("(i + 1) / 4", "(i + 1) / 6")
assert seg2.count("/ 6") == 4 and "/ 4" not in seg2 and "= 4" not in seg2 and "< 4" not in seg2, seg2
s = s[:i0] + seg2 + s[i1:]
rep("for (const sx of [1.6, 8.4]){ M(cyl(.02, .02, 1.7, 5)", "for (const sx of [-.2, 10.2]){ M(cyl(.02, .02, 1.7, 5)")
# xuồng bà con dạt ra
rep("x = L ? 2.7 : 7.3, z = BZ - 2.0 - row * 2.3", "x = L ? 2.6 : 7.4, z = BZ - 2.0 - row * 2.3")
rep("'#6B4529', L ? 1.65 : 8.35, .35, z + (L ? .3 : -.3)", "'#6B4529', L ? 1.55 : 8.45, .35, z + (L ? .3 : -.3)")
# cây cỏ, nhà dọc rạch
rep("if (x > .6 && x < 9.4) continue; if (HX.some", "if (x > -1.2 && x < 11.2) continue; if (HX.some")
rep("const x = R(-19, 19); if (x > 1.1 && x < 8.9) continue;", "const x = R(-19, 19); if (x > -.7 && x < 10.7) continue;")
rep("nha(-.1, BZ - 3.4, '#D8BE92', 1, .95); nha(10.2, BZ - 5.4, '#C8A584', 1); nha(-.2, BZ - 7.9, '#D2B48A', 0, .9);",
    "nha(-1.9, BZ - 3.4, '#D8BE92', 1, .95); nha(12.0, BZ - 5.4, '#C8A584', 1); nha(-2.0, BZ - 7.9, '#D2B48A', 0, .9);")
rep("x = sd2 ? 9.35 + R(0, .5) : .65 - R(0, .5)", "x = sd2 ? 11.15 + R(0, .5) : -1.15 - R(0, .5)")
rep("new T.Vector3(1.2, 0, BZ - .6), new T.Vector3(8.8, 3.8, BZ + .5)", "new T.Vector3(-.6, 0, BZ - .6), new T.Vector3(10.6, 3.8, BZ + .5)")
rep("/* —— bờ —— rạch bà con mở ở x 1.5..8.5 */", "/* —— bờ —— rạch bà con mở ở x -.3..10.3 (v162 nới rộng) */")
# kéo ngang ở bến rộng theo
rep("CNX.bx = Math.max(-2.2, Math.min(2.2,", "CNX.bx = Math.max(-3.4, Math.min(3.4,")

# 2) Chợ nổi + Bến bà con: kéo tự do mọi phía, có đà trượt, mép mềm (hết khoá trục, hết khựng)
rep("CHM.drag = { x: e.clientX, y: e.clientY, tx: CHM.tx, tz: CHM.tz || 0, dl: CNX.dl || 0, bx: CNX.bx || 0, bz: CNX.bz || 0, moved: false, id: e.pointerId }; }, true);",
    "CNX.vx = 0; CNX.vz = 0; CHM.drag = { x: e.clientX, y: e.clientY, tx: CHM.tx, tz: CHM.tz || 0, cz: CNX.tz || 0, dl: CNX.dl || 0, bx: CNX.bx || 0, bz: CNX.bz || 0, moved: false, id: e.pointerId }; }, true);\n"
    "const CNL = { tx: [-10, 7.5], tz: [-6, 3], bx: [-4.2, 4.2], bz: [-6.5, 1.2] }, cnRb = (v, L) => v < L[0] ? L[0] - (L[0] - v) * .35 : v > L[1] ? L[1] + (v - L[1]) * .35 : v;\n"
    "addEventListener('pointercancel', e => { const d = CHM.drag; if (d && e.pointerId === d.id) CHM.drag = null; });")
a = "if (CNX.ben && !CNX.son){ if (Math.hypot(dx, dy) > 8) d.moved = true;"
i0 = s.index(a); i1 = s.index("return; } if (Math.hypot(dx, e.clientY - d.y) > 8) d.moved = true;", i0)
s = s[:i0] + ("if (Math.hypot(dx, dy) > 8) d.moved = true; if (!d.moved || CNX.son) return; const now = performance.now(), dt = Math.max(8, Math.min(60, now - (d.t || now - 16))); d.t = now; let nx, nz, ox, oz; "
    "if (CNX.ben){ const kk = 1 - .45 * (CNX.bzm || 0); ox = CNX.bx || 0; oz = CNX.bz || 0; nx = CNX.bx = cnRb(d.bx - dx * 9 / innerWidth * kk, CNL.bx); nz = CNX.bz = cnRb(d.bz - dy * 15 / innerHeight * kk, CNL.bz); } "
    "else { const kk = 1 - .6 * (CNX.dl || 0); ox = CHM.tx || 0; oz = CNX.tz || 0; nx = CHM.tx = cnRb(d.tx - dx * 14 / innerWidth * kk, CNL.tx); nz = CNX.tz = cnRb(d.cz - dy * 18 / innerHeight * kk, CNL.tz); } "
    "d.vx = (d.vx || 0) * .5 + (nx - ox) / dt * 16 * .5; d.vz = (d.vz || 0) * .5 + (nz - oz) / dt * 16 * .5; ") + s[i1:]
rep("CHM.drag = null; if (!d.moved) chTap(e.clientX, e.clientY); });",
    "CHM.drag = null; if (!d.moved) chTap(e.clientX, e.clientY); else if (CHM.kind === 'cn' && !CNX.son && performance.now() - (d.t || 0) < 90){ const c = v => Math.max(-.5, Math.min(.5, v || 0)); CNX.vx = c(d.vx); CNX.vz = c(d.vz); } });")
# máy quay: trượt theo đà, dội nhẹ ở mép, đi theo êm
rep("function cnoCam(C){ const V = innerHeight > innerWidth ? CNV.p : CNV.l, d = CNX.dl || 0, x = CHM.tx || 0;",
    "function cnoCam(C){ if (!CHM.drag){ const g = (o, k, L, vk) => { let p = o[k] || 0, v = CNX[vk] || 0; p += v; v *= .92; if (Math.abs(v) < .003) v = 0; if (p < L[0]){ p += (L[0] - p) * .2; v *= .5; if (L[0] - p < .004) p = L[0]; } else if (p > L[1]){ p += (L[1] - p) * .2; v *= .5; if (p - L[1] < .004) p = L[1]; } o[k] = p; CNX[vk] = v; }; if (CNX.ben){ g(CNX, 'bx', CNL.bx, 'vx'); g(CNX, 'bz', CNL.bz, 'vz'); } else if (!CNX.son){ g(CHM, 'tx', CNL.tx, 'vx'); g(CNX, 'tz', CNL.tz, 'vz'); } }\n"
    "  CNX.txs = (CNX.txs || 0) + ((CHM.tx || 0) - (CNX.txs || 0)) * .3; CNX.tzs = (CNX.tzs || 0) + ((CNX.tz || 0) - (CNX.tzs || 0)) * .3; CNX.dls = (CNX.dls || 0) + ((CNX.dl || 0) - (CNX.dls || 0)) * .3;\n"
    "  const V = innerHeight > innerWidth ? CNV.p : CNV.l, d = CNX.dls, x = CNX.txs, tz = CNX.tzs;")
rep("if (i === 0 || i === 3) a += x; v[i] = a + (V.b[i] - a) * e; }", "if (i === 0 || i === 3) a += x; if (i === 2 || i === 5) a += tz; v[i] = a + (V.b[i] - a) * e; }")
rep("new T.Vector3(.5 + x * (1 - e), 0, -1)), 16)", "new T.Vector3(.5 + x * (1 - e), 0, -1 + tz * (1 - e))), 16)")
rep("CHM.on = true; CHM.tx = 0; CNX.dl = 0;", "CHM.on = true; CHM.tx = 0; CNX.dl = 0; CNX.tz = 0; CNX.txs = 0; CNX.tzs = 0; CNX.dls = 0; CNX.vx = 0; CNX.vz = 0;")
rep("CNX.ben = v ? 1 : 0; CNX.bx = 0; CNX.bz = 0; CNX.bzm = 0;", "CNX.ben = v ? 1 : 0; CNX.bx = 0; CNX.bz = 0; CNX.bzm = 0; CNX.vx = 0; CNX.vz = 0;")
rep("kéo ngang để chèo đi coi, kéo lên xuống để lại gần hay lùi ra.", "kéo qua lại, lên xuống để chèo đi coi, chụm hai ngón để lại gần hay lùi ra.")
rep("drag sideways to row along, drag up or down to come closer or step back.", "drag any way to row around, pinch to come closer or step back.")

# 3) Chợ nổi: dàn ghe ra, hết chồng lên nhau (chừa lối x ~5.5 cho xuồng mình chèo vô rạch)
rep("bigBoat('trai', -1.3, -.8, .42,", "bigBoat('trai', -.5, .8, .42,")
rep("bigBoat('rau', 2.8, -5.8, -.3,", "bigBoat('rau', 2.2, -6.8, -.3,")
rep("bigBoat('kho', -6.2, -7.0, .2,", "bigBoat('kho', -2.8, -9.0, .2,")
rep("smallBoat(3.0, 1.6, -.5, {", "smallBoat(7.4, 1.0, -.5, {")
rep("smallBoat(-3.8, -4.4, 2.6, {", "smallBoat(-2.2, -4.8, 2.6, {")
rep("smallBoat(-1.6, -7.6, .2, {", "smallBoat(-7.4, -6.4, .2, {")
rep("smallBoat(-8.4, -3.2, -.3, {", "smallBoat(-9.2, -2.6, -.3, {")
rep("smallBoat(3.6, -1.2, .28, { id: 'hutieu' })", "smallBoat(3.5, -3.0, .28, { id: 'hutieu' })")
rep("streak(3.9, -.95, 1.6, .36);", "streak(3.8, -2.75, 1.6, .36);")
rep("smallBoat(7.6, -2.5, .2, { id: 'son',", "smallBoat(7.0, -5.6, .2, { id: 'son',")
rep("const b2 = G(.75, .03, -.15, 2.45, root);", "const b2 = G(1.55, .03, 1.45, 2.45, root);")
rep("[[-1.2, 1.5, -.7], [5, 1.6, BZ + .4], [2.8, 1.5, -5.8], [3.8, .8, -1.1]]", "[[-.4, 1.5, .9], [5, 1.6, BZ + .4], [2.2, 1.5, -6.8], [3.7, .8, -2.9]]")
rep("if (pz > -2.4){ gx = 5.4; gz = -2.6; }", "if (pz > -2.4){ gx = 6.4; gz = -2.6; }")
rep("else if (pz < -2.8){ gx = 5.4; gz = -2.2; idle = .12; }", "else if (pz < -2.8){ gx = 6.4; gz = -2.2; idle = .12; }")
# tên xuồng trong rạch chỉ hiện khi đã vô bến (ở ngoài chợ nó đè lên bảng tên ghe)
rep("o.visible = !(q.far && need > 2.6) && !(q.bt && bk > .5);", "o.visible = !(q.far && (need > 2.6 || bk < .35)) && !(q.bt && bk > .5);")
# màn ngang: nâng máy quay lên chút cho các hàng ghe tách nhau
rep("l: { w: [-1, 3.4, 10.5, 1.2, 1.2, -4, 36],", "l: { w: [-1, 4.8, 11.5, 1.2, .9, -4, 36],")
# 4) Câu trên ghe: cần câu, dây, phao ở trên ghe tam bản (không còn ở cầu ván), có người ngồi mũi ghe cầm cần (dùng lại nhân vật của người chơi như ở chợ nổi)
rep("const fk = at(.32); stick(root, fk.x, WLR - .06,", "const rigP = G(0, 0, 0, 0, root); root.userData.rigP = rigP; const fk = at(.32); stick(rigP, fk.x, WLR - .06,")
rep("stick(root, fk.x, fk.y - .03, fk.z,", "stick(rigP, fk.x, fk.y - .03, fk.z,", 2)
rep("const cn = G(bx - .02, .2, R0 + 1.12, 0, root);", "const cn = G(bx - .02, .2, R0 + 1.12, 0, rigP);")
rep("function tbGheMove(quiet){", """const CRG = { on: false, v: new T.Vector3(), d: new T.Vector3(), up: new T.Vector3(0, 1, 0), dn: new T.Vector3(0, -1, 0), q: new T.Quaternion(), p0: null, q0: null, ax0: null, r0: null, ng: null, key: '', at: [.8, .05, 0, -2.57] };
function cauNguoi(){ const a = avOf(ST.player ? ST.player.av : 0), key = JSON.stringify(a); if (CRG.ng && CRG.key === key) return CRG.ng; if (CRG.ng) TBV.root.remove(CRG.ng);   /* người ngồi mũi ghe: nhân vật của người chơi, hai tay đưa ra trước cầm cần */
  const g = G(CRG.at[0], CRG.at[1], CRG.at[2], CRG.at[3], TBV.root), pr = ROOT; ROOT = g; g.scale.setScalar(.41); try { avBuild(g, a, {}); if (a.handL) a.handL.rotation.set(-1.15, 0, .3); if (a.handR) a.handR.rotation.set(-1.15, 0, -.3); } catch (e) {} ROOT = pr; CRG.ng = g; CRG.key = key; return g; }
function cauRig(){ const C = CAUV, J = C.RODJ[0], on = !!(FM.ghe && FM.on && TBV.m && TBV.st === 3 && TBV.root.visible);   /* câu trên ghe: dời gốc cần ra tay người ngồi ghe, phao nằm cạnh ghe; thôi thì trả về cầu ván */
  if (!CRG.p0){ CRG.p0 = J.position.clone(); CRG.q0 = J.quaternion.clone(); CRG.ax0 = C.RODAX.clone(); CRG.r0 = C.rest.clone(); }
  if (on){ const g = cauNguoi(); g.visible = true; g.updateWorldMatrix(true, false); CRG.v.set(0, .47, .2).applyMatrix4(g.matrixWorld); CRG.d.set(0, .6, .8).transformDirection(g.matrixWorld);
    J.position.copy(CRG.v); J.quaternion.setFromUnitVectors(CRG.up, CRG.d); C.RODAX.crossVectors(CRG.d, CRG.dn).normalize().applyQuaternion(CRG.q.copy(J.quaternion).invert());
    if (TBV.tw) C.rest.set(C.tip.x, C.tip.y - .34, C.tip.z); else C.rest.set(CRG.v.x + CRG.d.x * 1.2, WLR + .01, CRG.v.z + CRG.d.z * 1.2);   /* đang chèo thì phao treo lủng lẳng ở ngọn cần */
    if (C.root.userData.rigP) C.root.userData.rigP.visible = false; }
  else if (CRG.on){ J.position.copy(CRG.p0); J.quaternion.copy(CRG.q0); C.RODAX.copy(CRG.ax0); C.rest.copy(CRG.r0); if (C.root.userData.rigP) C.root.userData.rigP.visible = true; }
  if (on !== CRG.on){ CRG.on = on; if (!CRG.fa) CRG.fa = Object.assign({}, FAREA); Object.assign(FAREA, on ? { x0: bx + 2.6, x1: bx + 5.0, z0: R0 + .45, z1: R0 + 1.3 } : CRG.fa); try { fshClear(); DONB.at = {}; DONB.chk = -9; } catch (e) {} } }   /* trên ghe thì cá và chỗ quăng nằm ở khúc nước trước mũi ghe */
function tbGheMove(quiet){""")
rep("function rodBend(t, dt){ const C = CAUV, ph = FM.on ? FM.ph : 'idle';", "function rodBend(t, dt){ try { cauRig(); } catch (e) {} const C = CAUV, ph = FM.on ? FM.ph : 'idle';")
rep("function tbTick(t){ const on = tbOn(); TBV.b.visible = false;", "function tbTick(t){ const on = tbOn(); TBV.b.visible = false; try { if (CRG.ng) CRG.ng.visible = !!(FM.ghe && FM.on) || !!TBV.tw; } catch (e) {}")
rep("camTo(new T.Vector3(out ? bx + 1.5 : bx - .4, .2, out ? R0 + 1.4 : R0 + 1.25), cam.zoom, w.d * .9);", "camTo(new T.Vector3(out ? bx + 3.3 : bx - .4, .2, out ? R0 + 1.3 : R0 + 1.25), cam.zoom, w.d * .9);")
rep("`Ngoại chèo ghe ra giữa sông · còn ${gLeft()} lượt`", "`Chèo ghe ra giữa sông · còn ${gLeft()} lượt`")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
