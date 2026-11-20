#!/usr/bin/env python3
"""v173: dời cây ăn trái, đổi chỗ, cất cây vô túi (Sắp vườn, đợt 3).
- Trong Sắp vườn: nhấn giữ cây ăn trái là nhấc lên. Kéo qua 2 ô đất trống trên dưới (Mé sông / Sau nhà) là dời. Không tốn xu, cây giữ nguyên độ lớn và trái.
- Thả lên cây khác: hai cây đổi chỗ. Thả lên 2 ô liếp / giàn / đất trống: cây qua đó, liếp về chỗ cũ của cây.
- Kéo vô Túi đồ: hỏi một câu, đồng ý thì cất, trả lại 1 cây giống (không trả xu). 2 ô thành đất trống, làm liếp / giàn như thường. Cây đang có trái thì nhắc hái trước.
- Món kéo mới {t:'cay', k:<giống>, from:<ô trên>}; món 'tree' cũ vẫn là cây giống trong túi.
python3 fix173.py live/v172.html live/v173.html"""
import sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf8').read()
def rep(a, b, n=1):
    global t
    c = t.count(a)
    assert c == n, (c, a[:80])
    t = t.replace(a, b)

rep("BUILD = 'v172'", "BUILD = 'v173'")

# 1. cây nhấc được, ô nhận, dời / đổi chỗ, cất
rep("// món đang nằm ở ô id, nhấc lên được\nfunction sapItemAt(id){",
    "// v173: cây ăn trái đang trồng, nhấc lên dời được (chỉ trong Sắp vườn)\n"
    "let CAYASK = null;\n"
    "function sapCayAt(id){ if (!SAP || !id || !PL[id]) return null; const h = (ST.pairs || {})[id] ? id : pairHost(id); if (!h || !PL[h] || hidP(PL[h])) return null; const c = (ST.plots[h] || {}).crop; if (!c || !CROPS[c] || !CROPS[c].tree) return null; return { t: 'cay', k: c, from: h }; }\n"
    "function cayTop(id){ const P = PL[id]; if (!P || !P.bai || !TREEZ[zoneOf(P)]) return null; if (pairBelow(id)) return id; const h = pairHost(id); if (h) return h; const Z = zoneOf(P) === 'song' ? SONG : zoneOf(P) === 'kia' ? BKR : SAU, i = +id.slice(1) - 1; if (Math.floor(i / Z.cols) !== 1) return null; const t0 = id[0] + (i - Z.cols + 1); return pairBelow(t0) === id ? t0 : null; }\n"
    "const cayCellOk = c => bareFree(c) || !!sapLiepAt(c);\n"
    "function cayFit(id, it){ const t0 = cayTop(id); if (!t0) return null; if (t0 === it.from) return [t0, ST.pairs[t0]]; if ((ST.pairs || {})[t0]) return sapCayAt(t0) ? [t0, ST.pairs[t0]] : null; const y = pairBelow(t0); return y && cayCellOk(t0) && cayCellOk(y) ? [t0, y] : null; }\n"
    "function cayMove(a, b){ if (a === b) return true; const ya = (ST.pairs || {})[a], yb = pairBelow(b); if (!ya || !yb || !cayFit(b, { t: 'cay', from: a })) return false; const tb = !!ST.pairs[b]; ST.gian = ST.gian || {};\n"
    "  const get = c => ({ o: ST.open.includes(c), p: ST.plots[c], g: !!ST.gian[c] }), set = (c, s) => { ST.open = ST.open.filter(i => i !== c); if (s.o) ST.open.push(c); if (s.p) ST.plots[c] = s.p; else delete ST.plots[c]; delete ST.gian[c]; if (s.g) ST.gian[c] = 1; };\n"
    "  const A = get(a), YA = get(ya), B = get(b), YB = get(yb); set(a, B); set(ya, YB); set(b, A); set(yb, YA); ST.pairs[b] = yb; if (tb) ST.pairs[a] = ya; else delete ST.pairs[a];\n"
    "  for (const c of [a, ya, b, yb]){ PV[c].key = null; refreshPlot(c); } pairFillAll(); objPuff(b); if (tb) objPuff(a); sfx('pop'); buzz(12); save(); hud(); return true; }\n"
    "function cayStore(it){ const h = it.from, p = ST.plots[h]; if (!p || !(ST.pairs || {})[h]) return false; if (!p.dead && ripe(p)){ toast(L135('Cây đang có trái, con hái xong rồi cất nghe.', 'The tree has fruit. Pick it first, then store the tree.'), 'dan', { now: true }); return false; } CAYASK = h; SAPSEL = h; sapChipsDraw(); sfx('pick'); return true; }\n"
    "function cayAct(c){ const h = CAYASK; CAYASK = null; SAPSEL = null; if (c !== 'cayok' || !h) return; const p = ST.plots[h], y = (ST.pairs || {})[h]; if (!p || !y || !p.crop) return; const k = p.crop; if (!p.dead) ST.seeds[k] = (ST.seeds[k] || 0) + 1; delete ST.pairs[h]; ST.open = ST.open.filter(i => i !== h); ST.plots[h] = pl0(null);\n"
    "  for (const x of [h, y]){ PV[x].key = null; refreshPlot(x); } pairFillAll(); objPuff(h); sfx('pop'); buzz(12); save(); hud(); sapTrayDraw(); toast(p.dead ? L135('Dọn cây héo xong, hai ô thành đất trống rồi con.', 'Dead tree cleared. Both plots are empty land now.') : L135(`Đã cất ${treeNm(k).toLowerCase()} vô túi, trả con 1 cây giống. Hai ô thành đất trống.`, `${treeNm(k)} stored. You get 1 sapling back, and both plots are empty land.`)); }\n"
    "// món đang nằm ở ô id, nhấc lên được\nfunction sapItemAt(id){")

rep("{ const c0 = id || sapCellXY(cx, cy); return sapItemAt(c0) || sapLiepAt(c0); } }",
    "{ const c0 = id || sapCellXY(cx, cy); let r = sapItemAt(c0) || sapLiepAt(c0) || sapCayAt(c0); if (!r && SAP) try { r = sapCayAt(treeHitAt(cx, cy)); } catch (e) {} return r; } }")

# 2. hình, tên
rep("if (it.t === 'tree') return ICON[it.k] || UIC.task; if (it.t === 'obj') return ICON[it.k === 'ong'",
    "if (it.t === 'tree' || it.t === 'cay') return ICON[it.k] || UIC.task; if (it.t === 'obj') return ICON[it.k === 'ong'")
rep(": it.t === 'tree' ? treeNm(it.k) : it.t === 'obj' ? OBJD[it.k].title", ": it.t === 'tree' || it.t === 'cay' ? treeNm(it.k) : it.t === 'obj' ? OBJD[it.k].title")

# 3. đặt, hiện trạng, ô nhận, lý do
rep("function sapPut(it, id){\n  if (it.t === 'liep') return !!it.from && liepMove(it.from, id);",
    "function sapPut(it, id){\n  if (it.t === 'cay'){ const f = it.from && cayFit(id, it); return !!f && cayMove(it.from, f[0]); }\n  if (it.t === 'liep') return !!it.from && liepMove(it.from, id);")
rep("function sapNow(it, id){ if (it.t === 'liep')", "function sapNow(it, id){ if (it.t === 'cay') return { t: 'cay', k: it.k, from: id }; if (it.t === 'liep')")
rep("function sapFit(id, it){ if (!id) return null; if (it.t === 'tree'){", "function sapFit(id, it){ if (!id) return null; if (it.t === 'cay') return cayFit(id, it); if (it.t === 'tree'){")
rep("function sapWhy(id, it){ const P = PL[id]; if (!P || !P.bai) return '';",
    "function sapWhy(id, it){ const P = PL[id]; if (!P || !P.bai) return ''; if (it && it.t === 'cay') return !TREEZ[zoneOf(P)] ? treeWhere() : !landOwn(id) ? 'Chưa khai hoang' : L135('Cần 2 ô trên dưới: đất trống, liếp hoặc cây khác', 'Needs 2 plots, one above the other: empty land, beds or another tree');")
rep("const ok = it.t === 'tree' ? !!treeTop(P.id) :", "const ok = it.t === 'cay' ? !!cayFit(P.id, it) : it.t === 'tree' ? !!treeTop(P.id) :")
rep("else if (DROP){ const cs = DROP.it.t === 'big' ?", "else if (DROP){ const cs = DROP.it.t === 'cay' ? [DROP.it.from, (ST.pairs || {})[DROP.it.from]] : DROP.it.t === 'big' ?")

# 4. nhấc lên: nhắc khi không còn chỗ; dọn câu hỏi cũ
rep("  DROP = null; window.__sapLift = it.from || it.t === 'big' ? it.t + ':' + it.k : null;",
    "  CAYASK = null; if (it.t === 'cay' && !PLOTS.some(P => { const f = cayFit(P.id, it); return f && f[0] !== it.from; })) toast(L135('Chưa có chỗ 2 ô trên dưới để dời qua. Kéo vô túi là cất cây.', 'No 2-plot spot to move to yet. Drag to the bag to store the tree.'), 'dan', { now: true });\n"
    "  DROP = null; window.__sapLift = it.from || it.t === 'big' ? it.t + ':' + it.k : null;")

# 5. thả vô túi: hỏi một câu
rep("if (D.tray){ if (it.t === 'liep') toast(", "if (D.tray){ if (it.t === 'cay'){ cayStore(it); return; } if (it.t === 'liep') toast(")

# 6. nút sau khi thả: Đặt / Về chỗ cũ
rep("const k = DROP.it.t === 'liep' ? 'liep' :", "const k = DROP.it.t === 'liep' || DROP.it.t === 'cay' ? 'liep' :")

# 7. câu hỏi cất cây (dùng khung hỏi có sẵn)
rep("function sapChipsDraw(){ $('#sapChips').classList.remove('ask');",
    "function sapChipsDraw(){ $('#sapChips').classList.remove('ask'); if (CAYASK && SAPSEL === CAYASK){ const ch = $('#sapChips'), p = ST.plots[CAYASK] || {}, nm = p.crop ? treeNm(p.crop).toLowerCase() : ''; ch.classList.add('ask'); ch.innerHTML = `<span class=\"sapq\">${p.dead ? L135(`Dọn ${nm} héo, hai ô thành đất trống nghe con`, `Clear the dead ${nm}; both plots become empty land`) : L135(`Cất ${nm} vô túi, trả lại con 1 cây giống. Trồng lại thì cây lớn lại từ đầu.`, `Store the ${nm}. You get 1 sapling back; replanting starts it growing again.`)}</span><span class=\"sapr\"><button data-c=\"cayok\">${L135('Đồng ý', 'OK')}</button><button data-c=\"cayno\">${L135('Thôi', 'Never mind')}</button></span>`; return; }")
rep("function sapPick(id){ SAPASK = null;", "function sapPick(id){ SAPASK = null; CAYASK = null;")
rep("if (SAPSEL && !sapFree(SAPSEL, null) && !sapSan(SAPSEL)", "if (SAPSEL && SAPSEL !== CAYASK && !sapFree(SAPSEL, null) && !sapSan(SAPSEL)")
rep("if (/^(gian|doi|doiok|doino)$/.test(b.dataset.c)){", "if (/^cay(ok|no)$/.test(b.dataset.c)){ cayAct(b.dataset.c); return; } if (/^(gian|doi|doiok|doino)$/.test(b.dataset.c)){")
rep("function sapTap(cx, cy){ if (DROP){ DROP = null; return; }", "function sapTap(cx, cy){ CAYASK = null; if (DROP){ DROP = null; return; }")

# 7b. khung hỏi không chui xuống dưới bảng Túi đồ
rep("ch.style.transform = `translate(${sapX(x, w).toFixed(1)}px,${Math.max(bar, y - 76).toFixed(1)}px)`; } else ch.hidden = true;",
    "const tt = $('#sapTray').getBoundingClientRect().top || innerHeight; ch.style.transform = `translate(${sapX(x, w).toFixed(1)}px,${Math.max(bar, Math.min(y - 76, tt - (ch.offsetHeight || 60) - 12)).toFixed(1)}px)`; } else ch.hidden = true;")

# 8. lời nhắc
rep("if (id && sapItemAt(id)) toast('Nhấn giữ rồi kéo để dời, kéo vô túi để cất');",
    "if (id && (sapItemAt(id) || sapCayAt(id))) toast('Nhấn giữ rồi kéo để dời, kéo vô túi để cất');")
rep("if (!ST.seen.sap1){ ST.seen.sap2 = 1;",
    "if (ST.seen.sap1 && ST.seen.sap2 && !ST.seen.sap3 && PLOTS.some(P => sapCayAt(P.id))) sayOnce('sap3', L135('Cây trái giờ cũng dời được rồi con. Nhấn giữ cây rồi kéo qua hai ô khác, thả lên cây khác là đổi chỗ. Kéo vô túi là cất, Ngoại trả lại cây giống.', 'Fruit trees can move now. Press and hold a tree and drag it to two other plots, or drop it on another tree to swap. Drag it to the bag to store it and get the sapling back.'), 'vui');\n"
    "    else if (!ST.seen.sap1){ ST.seen.sap2 = 1; ST.seen.sap3 = 1;")
rep("Liếp với giàn cũng dời được y vậy.', 'Your land, your layout. Press and hold anything to lift and drag it; drop it on the bag to store it. Beds and trellises move the same way.')",
    "Liếp, giàn, cây trái cũng dời được y vậy.', 'Your land, your layout. Press and hold anything to lift and drag it; drop it on the bag to store it. Beds, trellises and fruit trees move the same way.')")

open(dst, 'w', encoding='utf8').write(t)
print('ok', len(t))
