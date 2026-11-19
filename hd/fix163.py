# v162 -> v163:
# 1) Ghe tam bản: bấm "Chở đi" thì ghe chèo ra khỏi bến, khuất một lúc rồi chèo về, quay mũi đậu lại; chạm ghe thì máy quay lia tới.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), n, a[:60])
    s = s.replace(a, b)
rep("BUILD = 'v162'", "BUILD = 'v163'")

# ---------- 1) chuyến hàng: ghe đi thật ----------
rep("coinPop(`+${o.xu} xu · chuyến hàng chợ nổi`, '#9fd36a'); sfx('coin'); buzz(20); for (let i = 0; i < 14; i++) puff('drop', TB.at[0] + R(-.8, .8), .05, TB.at[1] + R(-.3, .3), 1, '#9cc6e0', .8); save(); hud(); renderSheet(); }",
    "coinPop(`+${o.xu} xu · chuyến hàng chợ nổi`, '#9fd36a'); sfx('coin'); buzz(20); for (let i = 0; i < 14; i++) puff('drop', TB.at[0] + R(-.8, .8), .05, TB.at[1] + R(-.3, .3), 1, '#9cc6e0', .8); save(); hud(); try { closeSheet(); tbTrip(); } catch (e) { renderSheet(); } }\n"
    "function tbTrip(){ if (FM.on && FM.ghe) return; TBV.tw = null; TBV.trip = { t0: -1, pf: 0, away: false, home: false }; tbCam(.7); }   /* chở hàng: ghe rời bến, khuất rồi về */\n"
    "function tbCam(d){ try { const P = TBV.root.position; camTo(new T.Vector3(P.x + .5, .2, P.z + .4), Math.max(cam.zoom, DEFZ() * 1.15), d || .55); } catch (e) {} }   /* lia máy quay tới ghe, nhích lên trên cho khỏi bị bảng che */\n"
    "function tbTripEnd(){ const q = TBV.trip; if (!q) return; TBV.trip = null; try { if (q.gz != null){ if (!GGO) GHEV.root.position.z = q.gz; if (BAYV) BAYV.root.position.z = q.bz; } } catch (e) {} const P = TBV.root.position; P.x = TB.at[0]; P.z = TB.at[1]; TBV.root.rotation.y = -.04; }")
rep("function tbGheMove(quiet){ try { const P = TBV.root.position,", "function tbGheMove(quiet){ try { tbTripEnd(); const P = TBV.root.position,")
rep("TBV.root.visible = on && !!ST.tb; if (!on) return; const B = ST.tb;", "TBV.root.visible = on && !!ST.tb && !(TBV.trip && TBV.trip.away); if (!on) return; const B = ST.tb;")
rep("try { if (CRG.ng) CRG.ng.visible = !!(FM.ghe && FM.on) || !!TBV.tw; } catch (e) {}", "try { if (TBV.trip && TBV.m && TBV.st === 3) cauNguoi(); if (CRG.ng) CRG.ng.visible = !!(FM.ghe && FM.on) || !!TBV.tw || !!TBV.trip; } catch (e) {}")
rep("  if (st === 1) objBub(TBV, { cx: x, cz: z }, UIC.tamban || ICON.cuoc, t, .5);",
    """  if (TBV.trip){ const q = TBV.trip, P = TBV.root.position, X0 = x, Z0 = z, ZL = R0 + 1.85, XE = x + 11, cl = k => Math.max(0, Math.min(1, k)), sm = k => k * k * (3 - 2 * k); if (q.t0 < 0){ q.t0 = t; q.nz = 0; q.gz = GHEV.root.position.z; q.bz = BAYV ? BAYV.root.position.z : 0; } const u = t - q.t0; let wake = 0;
    { const ne = (u > .2 && u < 4.2) || (u >= 6.4 && P.x > 7.3 && u < 10.4) ? 1 : 0; q.nz += (ne - q.nz) * .07; const dz = -.4 * q.nz; if (!GGO) GHEV.root.position.z = q.gz + dz; if (BAYV) BAYV.root.position.z = q.bz + dz; }   /* ghe khách đang đậu nép vô bờ nhường đường */
    if (u < 4.2){ const k = u / 4.2, a = cl(k * 3); P.x = X0 + (XE - X0) * Math.pow(k, 1.7); P.z = Z0 + (ZL - Z0) * sm(a); TBV.root.rotation.y = -.04 - Math.sin(a * Math.PI) * .3; TBV.root.rotation.x += Math.sin(t * 5.5) * .03; wake = 1; q.away = false; }   /* lấy đà, tách bến ra làn ngoài rồi xuôi dòng */
    else if (u < 6.4){ q.away = true; }
    else if (u < 10.4){ const k = (u - 6.4) / 4, e = 1 - Math.pow(1 - k, 1.9); q.away = false; P.x = XE + (X0 + .35 - XE) * e; P.z = ZL + (Z0 + .15 - ZL) * sm(cl((k - .6) / .4)); TBV.root.rotation.y = Math.PI - .04; TBV.root.rotation.x += Math.sin(t * 5.5) * .03 * (1 - k); wake = k < .9 ? -1 : 0; }   /* về: mũi quay ngược, chậm dần */
    else if (u < 12.6){ const k = sm((u - 10.4) / 2.2); P.x = X0 + .35 * (1 - k); P.z = Z0 + .15 * (1 - k) - .1 * Math.sin(k * Math.PI); TBV.root.rotation.y = (Math.PI - .04) * (1 - k) - .04 * k; }   /* quay mũi, tấp vô chỗ đậu */
    else { tbTripEnd(); for (let i = 0; i < 6; i++) puff('drop', x + R(-.9, .9), .05, z + R(-.25, .25), 1, '#9cc6e0', .5); try { sfx('pick'); } catch (e) {} }
    if (wake && t - q.pf > .12){ q.pf = t; puff('drop', P.x - wake * 1.15 + R(-.1, .1), .05, P.z + R(-.18, .18), 1, '#9cc6e0', .45); } }
  if (st === 1) objBub(TBV, { cx: x, cz: z }, UIC.tamban || ICON.cuoc, t, .5);""")
rep("else if (loLeft() <= 0 && !FM.ghe && !TBV.tw) objBub(TBV, { cx: x - .3, cz: z }, ICON.caro, t, .8); }", "else if (loLeft() <= 0 && !FM.ghe && !TBV.tw && !TBV.trip) objBub(TBV, { cx: x - .3, cz: z }, ICON.caro, t, .8); }")
# chạm ghe: lia máy quay tới; ghe đang đi chuyến thì chỉ lia máy
rep("if (th){ const B = ST.tb; if (B && !B.done) tbTell(); else if (B && loLeft() <= 0) tbTake(); else openSheet('tb'); hud(); return; } }",
    "if (th){ const B = ST.tb; if (!FM.on) tbCam(); if (TBV.trip){ hud(); return; } if (B && !B.done) tbTell(); else if (B && loLeft() <= 0) tbTake(); else openSheet('tb'); hud(); return; } }")
rep("UX.btn('tbcau', 'Chèo ra câu', { g: 1, img: ICON.cancau, dis: gLeft() <= 0 })", "UX.btn('tbcau', 'Chèo ra câu', { g: 1, img: ICON.cancau, dis: gLeft() <= 0 || !!TBV.trip })")

# ---- đợt 2: nhẹ khung vẽ chính. Ụ đất dưới cây hai ô có 104 cọng cỏ, mỗi cọng một lưới riêng → gộp theo màu y như ụ đất cây một ô ----
rep("FR.mound(mg, .6, false); sd = ps2; } v.mound = 1;", "FR.mound(mg, .6, false); sd = ps2; try { v.root.updateMatrixWorld(true); const ms = mergeMeshes(mg); v.root.remove(mg); const iv = v.root.matrixWorld.clone().invert(); ms.forEach(m => { m.geometry.applyMatrix4(iv); v.root.add(m); }); } catch (e) {} } v.mound = 1;")

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
