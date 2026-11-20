#!/usr/bin/env python3
"""v172: dời liếp, dời giàn (Sắp vườn, đợt 2).
- Trong Sắp vườn: nhấn giữ liếp hoặc giàn trên ô đất khai hoang là nhấc lên, kéo qua ô đất trống rồi thả. Không tốn xu.
- Cây đang trồng đi theo nguyên vẹn (độ lớn, độ ẩm, rơm phủ, đất). Giàn qua ô mới vẫn là giàn.
- Thả xong hiện 2 nút: Đặt ở đây / Hủy (về chỗ cũ). Liếp không cất vô túi được.
- Chưa dời: liếp gốc quanh nhà (ô không phải đất khai hoang), ô có cây ăn trái (đợt 3).
- Món kéo mới {t:'liep', k:'liep'|'gian', from:id}; chỉ nhấc được khi đang ở Sắp vườn (ngoài Sắp vườn nhấn giữ liếp vẫn mở bảng như cũ).
python3 fix172.py live/v171.html live/v172.html"""
import sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf8').read()
def rep(a, b, n=1):
    global t
    c = t.count(a)
    assert c == n, (c, a[:80])
    t = t.replace(a, b)

rep("BUILD = 'v171'", "BUILD = 'v172'")

# 1. liếp / giàn nhấc được + dời
rep("// món đang nằm ở ô id, nhấc lên được\nfunction sapItemAt(id){",
    "// v172: liếp / giàn trên ô đất, nhấc lên dời được (chỉ trong Sắp vườn)\n"
    "function sapLiepAt(id){ const P = id && PL[id]; if (!SAP || !P || !P.bai || P.co || hidP(P) || !landOwn(id) || locked(P) || objAt(id) || decoAt(id) >= 0 || bigAt(id) || (ST.pairs || {})[id] || pairHost(id)) return null; const c = (ST.plots[id] || {}).crop; if (c && CROPS[c] && CROPS[c].tree) return null; return { t: 'liep', k: P.trellis ? 'gian' : 'liep', from: id }; }\n"
    "const liepOk = (id, it) => id === it.from || sapFree(id, it) || !!sapLiepAt(id);   /* ô trống, hoặc liếp khác để đổi chỗ */\n"
    "function liepMove(a, b){ if (a === b) return true; const A = PL[a]; if (!A || locked(A)) return false; const sw = !!sapLiepAt(b); if (!sw && !sapFree(b, { t: 'liep' })) return false; const ga = !!A.trellis, gb = sw && !!PL[b].trellis, pa = ST.plots[a] || pl0(null), pb = sw ? ST.plots[b] : pl0(null); ST.gian = ST.gian || {}; ST.plots[b] = pa; ST.plots[a] = pb; delete ST.gian[a]; delete ST.gian[b]; if (ga) ST.gian[b] = 1; if (gb) ST.gian[a] = 1; if (!sw){ ST.open = ST.open.map(i => i === a ? b : i); ST.land[a] = { st: 'own' }; if (!ST.land[b]) ST.land[b] = { st: 'own' }; } if (sw) objPuff(a); PV[a].key = null; PV[b].key = null; refreshPlot(a); refreshPlot(b); objPuff(b); sfx('pop'); buzz(12); save(); hud(); return true; }\n"
    "// món đang nằm ở ô id, nhấc lên được\nfunction sapItemAt(id){")
rep("} catch (e) {} return sapItemAt(id || sapCellXY(cx, cy)); }",
    "} catch (e) {} { const c0 = id || sapCellXY(cx, cy); return sapItemAt(c0) || sapLiepAt(c0); } }")

# 2. hình, tên
rep("function sapIc(it){ if (it.t === 'tree')",
    "function sapIc(it){ if (it.t === 'liep'){ const c = it.from && (ST.plots[it.from] || {}).crop; return (c && ICON[c]) || (it.k === 'gian' && ICON[gianOk()]) || ICON.cai; } if (it.t === 'tree')")
rep("function sapName(it){ return it.t === 'tree' ?",
    "function sapName(it){ return it.t === 'liep' ? (it.k === 'gian' ? L135('Giàn', 'Trellis') : L135('Liếp', 'Bed')) : it.t === 'tree' ?")

# 3. đặt, hiện trạng sau khi đặt
rep("function sapPut(it, id){\n  if (it.t === 'tree'){",
    "function sapPut(it, id){\n  if (it.t === 'liep') return !!it.from && liepMove(it.from, id);\n  if (it.t === 'tree'){")
rep("function sapNow(it, id){ if (it.t === 'obj')",
    "function sapNow(it, id){ if (it.t === 'liep') return { t: 'liep', k: it.k, from: id }; if (it.t === 'obj')")

# 3b. ô nhận: ô trống hoặc liếp khác (đổi chỗ)
rep("return sapFree(id, it) ? [id] : null; }\nfunction sapCellXY", "return (it.t === 'liep' ? liepOk(id, it) : sapFree(id, it)) ? [id] : null; }\nfunction sapCellXY")
rep("? !!dcFit(P.id, it, it.k) : sapFree(P.id, it); h +=", "? !!dcFit(P.id, it, it.k) : it.t === 'liep' ? liepOk(P.id, it) : sapFree(P.id, it); h +=")

# 4. nhấc lên mà không có ô trống: nhắc
rep("DROP = null; window.__sapLift = it.from || it.t === 'big' ? it.t + ':' + it.k : null;",
    "if (it.t === 'liep' && !PLOTS.some(P => P.id !== it.from && liepOk(P.id, it))) toast(L135('Chưa có ô đất trống để dời qua. Con khai hoang thêm nghe.', 'No empty land to move to yet. Clear more land first.'), 'dan', { now: true });\n"
    "  DROP = null; window.__sapLift = it.from || it.t === 'big' ? it.t + ':' + it.k : null;")

# 5. thả vô túi: liếp không cất được
rep("if (D.tray){ if (it.from && sapStore(it)) toast(`Đã cất ${sapName(it).toLowerCase()} vô túi`);",
    "if (D.tray){ if (it.t === 'liep') toast(L135('Liếp với giàn không cất vô túi được, con kéo qua ô đất trống nghe.', 'Beds and trellises cannot go in the bag. Drag them to empty land.'), 'dan', { now: true }); else if (it.from && sapStore(it)) toast(`Đã cất ${sapName(it).toLowerCase()} vô túi`);")

# 6. nút sau khi thả: liếp chỉ có Đặt / Hủy
rep("const k = DROP.it.t === 'big' ? 'home' : 'box', lbl = DROP.it.t === 'big' ? 'Về chỗ cũ' : 'Cất vô túi'; if (bt.dataset.k !== k){ bt.dataset.k = k; bt.innerHTML = `<button class=\"y\" data-d=\"ok\" aria-label=\"Đặt ở đây\">${SAPSV.ok}</button><button class=\"n\" data-d=\"no\" aria-label=\"Hủy\">${SAPSV.no}</button><button class=\"s\" data-d=\"box\" aria-label=\"${lbl}\">${SAPSV[k]}</button>`; }",
    "const k = DROP.it.t === 'liep' ? 'liep' : DROP.it.t === 'big' ? 'home' : 'box', lbl = DROP.it.t === 'big' ? 'Về chỗ cũ' : 'Cất vô túi'; if (bt.dataset.k !== k){ bt.dataset.k = k; bt.innerHTML = `<button class=\"y\" data-d=\"ok\" aria-label=\"${L135('Đặt ở đây', 'Place here')}\">${SAPSV.ok}</button><button class=\"n\" data-d=\"no\" aria-label=\"${k === 'liep' ? L135('Về chỗ cũ', 'Put it back') : 'Hủy'}\">${SAPSV.no}</button>` + (k === 'liep' ? '' : `<button class=\"s\" data-d=\"box\" aria-label=\"${lbl}\">${SAPSV[k]}</button>`); }")

# 7. lời nhắc
rep("if (id && sapItemAt(id)) toast('Nhấn giữ rồi kéo để dời, kéo vô túi để cất'); else if (id && PL[id].bai && !locked(PL[id]) && (ST.plots[id] || {}).crop) toast('Liếp đang có cây, hái xong mới san được con.');",
    "if (id && sapItemAt(id)) toast('Nhấn giữ rồi kéo để dời, kéo vô túi để cất'); else if (id && sapLiepAt(id)) toast(L135('Nhấn giữ rồi kéo qua ô đất trống, hoặc thả lên liếp khác để đổi chỗ.', 'Press and hold, then drag to empty land, or drop on another bed to swap.')); else if (id && PL[id].bai && !locked(PL[id]) && (ST.plots[id] || {}).crop) toast('Liếp đang có cây, hái xong mới san được con.');")
rep("sayOnce('sap1', 'Đất của con, muốn đặt gì ở đâu cũng được. Nhấn giữ món nào là nhấc lên kéo đi, kéo vô túi là cất.', 'vui');",
    "if (!ST.seen.sap1){ ST.seen.sap2 = 1; sayOnce('sap1', L135('Đất của con, muốn đặt gì ở đâu cũng được. Nhấn giữ món nào là nhấc lên kéo đi, kéo vô túi là cất. Liếp với giàn cũng dời được y vậy.', 'Your land, your layout. Press and hold anything to lift and drag it; drop it on the bag to store it. Beds and trellises move the same way.'), 'vui'); }\n"
    "    else if (PLOTS.some(P => sapLiepAt(P.id))) sayOnce('sap2', L135('Liếp với giàn giờ dời được rồi con. Nhấn giữ rồi kéo qua ô đất trống, hoặc thả lên liếp khác cho hai bên đổi chỗ. Cây đang trồng đi theo luôn.', 'Beds and trellises can move now. Press and hold, then drag to empty land, or drop on another bed to swap. The crops come along.'), 'vui');")

open(dst, 'w', encoding='utf8').write(t)
print('ok', len(t))
