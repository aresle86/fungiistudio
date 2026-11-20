#!/usr/bin/env python3
"""v169: máy quay điện thoại thoáng hơn.
- Vườn đã mở rộng (bãi cỏ, mé sông) thì mặc định điện thoại dọc lùi ra: 1.45 -> 1.3 -> 1.15.
- Máy quay lia tới chỗ ăn mừng (gà nở, mua khạp cá, nâng chuồng vịt) xong thì tự lùi về mức cũ.
- Ngoại chào lúc vô vườn không giữ mức phóng gần đang dở nữa.
python3 fix169.py live/v168.html live/v169.html"""
import sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf8').read()
def rep(a, b, n=1):
    global t
    c = t.count(a)
    assert c == n, (c, a[:80])
    t = t.replace(a, b)

rep("BUILD = 'v168'", "BUILD = 'v169'")

# 1. mặc định điện thoại dọc theo cỡ vườn
rep("const DEFZ = () => (MOBILE && innerHeight > innerWidth ? 1.45 : 1.3);",
    "const DEFZ = () => { if (!(MOBILE && innerHeight > innerWidth)) return 1.3; let lv = 1; try { lv = ST.lv || 1; } catch (e) {} return lv >= SONG.lv ? 1.15 : lv >= BAI.lv ? 1.3 : 1.45; };")

# 2. lia tới coi rồi lùi về: camPeek
rep("function camTo(tg, zm, d){ CAMGO",
    "function camPeek(tg, zm, ms){ const z0 = cam.zoom; camTo(tg, zm); if (zm <= z0 + .01) return; setTimeout(() => { try { if (CAMGO || VISIT || busy() || Math.abs(cam.zoom - zm) > .02 || ctl.target.distanceTo(tg) > .6) return; camTo(ctl.target.clone(), Math.max(z0, .01), .9); } catch (e) {} }, ms || 3200); } function camTo(tg, zm, d){ CAMGO")
rep("if (!busy() && !VISIT) camTo(new T.Vector3(p.x, .3, p.z), Math.max(cam.zoom, DEFZ() * 2.2));",
    "if (!busy() && !VISIT) camPeek(new T.Vector3(p.x, .3, p.z), Math.max(cam.zoom, DEFZ() * 2.2));")
rep("closeSheet(); camTo(new T.Vector3(KCA.at[0], .3, KCA.at[1]), Math.max(cam.zoom, DEFZ() * 2));",
    "closeSheet(); camPeek(new T.Vector3(KCA.at[0], .3, KCA.at[1]), Math.max(cam.zoom, DEFZ() * 2));")
rep("closeSheet(); camTo(new T.Vector3(VIT.at[0], .3, VIT.at[1]), Math.max(cam.zoom, DEFZ() * 1.6));",
    "closeSheet(); camPeek(new T.Vector3(VIT.at[0], .3, VIT.at[1]), Math.max(cam.zoom, DEFZ() * 1.6));")

# 3. Ngoại chào: không giữ mức phóng gần đang dở
rep("const v = PV[go]; camTo(new T.Vector3(v.cx, .3, v.cz), cam.zoom); }",
    "const v = PV[go]; camTo(new T.Vector3(v.cx, .3, v.cz), CAMGO && CAMGO.zm > CAMGO.z0 ? CAMGO.z0 : cam.zoom); }")

# 4. bảng chọn trên liếp đè lên nút Về giữa / Sắp vườn thì tạm ẩn hai nút đó (màn thoáng hơn nên liếp hay nằm cao)
i = t.index('</style>'); t = t[:i] + 'body.ringov #bCtr,body.ringov #bSua{visibility:hidden}\n' + t[i:]
rep("function ringPos(){ if (RING.hidden || RINGID == null) return;",
    "function ringOv(on){ if (!!ringOv.on === !!on) return; ringOv.on = !!on; document.body.classList.toggle('ringov', !!on); } function ringPos(){ if (RING.hidden || RINGID == null) return ringOv(0);")
rep("RING.style.setProperty('--ax', Math.max(-w / 2 + 22, Math.min(w / 2 - 22, ax - x)) + 'px'); }",
    "RING.style.setProperty('--ax', Math.max(-w / 2 + 22, Math.min(w / 2 - 22, ax - x)) + 'px'); try { const a = RING.getBoundingClientRect(); let ov = false; for (const q of ['#bCtr', '#bSua']){ const e = $(q); if (!e || e.hidden) continue; const b = e.getBoundingClientRect(); if (!b.width) continue; if (a.left < b.right + 8 && a.right > b.left - 8 && a.top < b.bottom + 8 && a.bottom > b.top - 8) ov = true; } ringOv(ov); } catch (e) {} }")

open(dst, 'w', encoding='utf8').write(t)
print('ok', len(t))
