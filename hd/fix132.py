# -*- coding: utf-8 -*-
# v132 sau v131 (góp ý anh Ares):
# 1. Bong bóng của liếp/giàn nằm trước chuồng gà khó bấm: hộp chạm của chuồng (1.1 x 1.2 x 1.0) được xét
#    TRƯỚC bong bóng liếp nên nuốt cú chạm. Giờ bong bóng liếp được xét trước chuồng gà, cỏ dại dưới đất,
#    bếp, ao, công trình lớn, bướm, chuồng chưa mua. Bong bóng trứng/máng của chuồng gà nằm gần máy hơn thì vẫn thắng.
# 2. Lục bình khô có trong danh sách chọn món của nong cả khi giỏ lục bình được giữ lại (keep.gio) mà chưa tới cấp 15.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v131'", "BUILD = 'v132'")

# ---------- 1. bong bóng liếp thắng đồ vật phía sau ----------
# a) nhớ khoảng cách bong bóng liếp trúng tia
rep("const hb = ray.intersectObjects(bubs, false)[0]; if (hb){ PBH = true; return hb.object.userData.plot; }",
    "const hb = ray.intersectObjects(bubs, false)[0]; if (hb){ PBH = true; PBD = hb.distance; return hb.object.userData.plot; }")
rep("function plotHit0(cx, cy){ PBH = false;", "let PBD = 0;\nfunction gaBubD(cx, cy){ try { if (!gaOn()) return 1e9; ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); const h = ray.intersectObjects(GAV.hits.filter(m => m.userData.bub && m.parent && m.parent.visible !== false), false)[0]; return h ? h.distance : 1e9; } catch (e) { return 1e9; } }   /* bong bóng trứng, máng của chuồng gà: gần máy hơn bong bóng liếp thì nó thắng */\nfunction plotHit0(cx, cy){ PBH = false;")
# b) pointerdown: cỏ dại dưới đất và chuồng gà nhường bong bóng liếp
rep("const g = groundAt(e.clientX, e.clientY); return g && weedNear(g.x, g.z, .26) >= 0 ? { x: g.x, z: g.z } : null; } catch (er) { return null; } })();",
    "if (plotHit(e.clientX, e.clientY) && PBH) return null; const g = groundAt(e.clientX, e.clientY); return g && weedNear(g.x, g.z, .26) >= 0 ? { x: g.x, z: g.z } : null; } catch (er) { return null; } })();")
rep("const gk = VISIT || wg ? null : gaHit(e.clientX, e.clientY), id = gk || wg ? null : plotHit(e.clientX, e.clientY),",
    "const pid0 = wg ? null : plotHit(e.clientX, e.clientY), pb0 = !!pid0 && PBH && !(!VISIT && gaBubD(e.clientX, e.clientY) < PBD), gk = VISIT || wg || pb0 ? null : gaHit(e.clientX, e.clientY), id = gk || wg ? null : pid0,")
rep("gk, wg, bub: !!id && PBH, moved: false, held: false };", "gk, wg, bub: !!id && pb0, moved: false, held: false };")
# c) pointerup: bướm, công trình, ao, bếp, chuồng chưa mua cũng nhường bong bóng liếp
for a in ["const bh = buHit(e.clientX, e.clientY);", "const fh = ftHitAt(e.clientX, e.clientY);", "if (aoHit(e.clientX, e.clientY) && !(SUA && SUA.move))",
          "if (kcaHit(e.clientX, e.clientY) || kbenHit(e.clientX, e.clientY))", "if (noteHit(e.clientX, e.clientY)) return;", "if (bepHitAt(e.clientX, e.clientY)){ if ((ST.lv || 1) >= BEP.lv"]:
    rep(a, a.replace("e.clientX, e.clientY", "OX, OY"))
rep("if (!VISIT){ ndc.set(e.clientX / innerWidth * 2 - 1, -(e.clientY / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); for (const [k, P] of Object.entries(PENS)){",
    "if (!VISIT && !g.bub){ ndc.set(e.clientX / innerWidth * 2 - 1, -(e.clientY / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); for (const [k, P] of Object.entries(PENS)){")

# ---------- 2. lục bình trong danh sách chọn món của nong; món đủ đồ xếp lên đầu ----------
rep("Object.keys(R).filter(k => (ST.lv || 1) >= (R[k].lv || 1)).map(k => { const d = R[k], lk = (ST.lv || 1) < (d.lv || 1), can = !lk && canIn(d.in);",
    "Object.keys(R).filter(k => (ST.lv || 1) >= (R[k].lv || 1) || (k === 'lucbinhkho' && gioOn())).sort((a, b) => (canIn(R[b].in) ? 1 : 0) - (canIn(R[a].in) ? 1 : 0)).map(k => { const d = R[k], lk = (ST.lv || 1) < (d.lv || 1) && !(k === 'lucbinhkho' && gioOn()), can = !lk && canIn(d.in);")
# ---------- 3. chậm chu kỳ đẻ: gà 3 -> 5 tiếng, vịt 4 -> 6 tiếng (anh Ares duyệt) ----------
rep("buy: 150, cyc: 3 * 3600, trough: 2, caps: [4, 6, 9, 12]", "buy: 150, cyc: 5 * 3600, trough: 2, caps: [4, 6, 9, 12]")
rep("buy: 180, cyc: 4 * 3600, trough: 2, caps: [4, 8, 12]", "buy: 180, cyc: 6 * 3600, trough: 2, caps: [4, 8, 12]")
rep("mỗi con một phần mỗi 3 tiếng.\": \"Hens fed on home-grown corn lay sooner. With a full trough they eat slowly, one portion each every 3 hours.\"", "mỗi con một phần mỗi 5 tiếng.\": \"Hens fed on home-grown corn lay sooner. With a full trough they eat slowly, one portion each every 5 hours.\"")
rep("mỗi con một phần mỗi 3 tiếng.' : 'Không có bắp", "mỗi con một phần mỗi 5 tiếng.' : 'Không có bắp")
rep("\"Vịt đẻ mỗi 4 tiếng một trứng nếu máng còn thức ăn.\": \"Ducks lay an egg every 4 hours while there's feed.\"", "\"Vịt đẻ mỗi 6 tiếng một trứng nếu máng còn thức ăn.\": \"Ducks lay an egg every 6 hours while there's feed.\"")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', DST)
