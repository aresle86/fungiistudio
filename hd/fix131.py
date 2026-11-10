# -*- coding: utf-8 -*-
# v131 sau v130: người chơi tưởng "Giàn bầu mướp" mé ao (đồ trang trí ao, 4.000 xu) hái được.
# Anh Ares chọn: giữ là đồ trang trí, chỉ sửa lời cho rõ (không trộn đồ trang trí với đồ thu hoạch).
# 1. Lời Ngoại lúc mua giàn bỏ chữ "có đồ ăn", nói rõ giàn để ngắm, muốn hái bầu thì trồng ở giàn trên mương.
# 2. Mục "Trang trí ao" trong bảng Ao cá ghi rõ đồ trang trí chỉ để ngắm.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v130'", "BUILD = 'v131'")
OLD = "Giàn bầu mướp bắc ngang mé ao, có bóng mát lại có đồ ăn."
NEW = "Giàn bầu mướp bắc ngang mé ao cho mát. Giàn này để ngắm thôi nghe con, muốn hái bầu thì trồng ở giàn trên mương."
rep('"' + OLD + '": "A gourd trellis over the bank gives shade and supper."',
    '"' + NEW + '": "A gourd trellis over the bank for shade. This one is just for looks, dear. To pick gourds, plant them on the trellis over the canal."')
rep("'" + OLD + "'", "'" + NEW + "'")
O2 = "Chạm món đã mua để cất hay đặt lại, không tốn xu"
N2 = "Chỉ để ngắm, không thu hoạch"
rep('"' + O2 + '": "Tap an item you own to store or place it, free of charge"',
    '"' + N2 + '": "Just for looks, no harvest"')
rep("'" + O2 + "'", "'" + N2 + "'")
assert OLD not in s and s.count(NEW) == 2 and s.count(N2) == 2

# ---------- 3. Sắp vườn: cây trái vô khay, sáng ô trồng được, lời từ chối nói thật ----------
# Người chơi báo: trong Sắp vườn bấm "Cây" ở đâu cũng bị từ chối với lời sai ("ô ngay dưới cũng phải trống"),
# trong khi cây trái chỉ trồng được ở Mé sông / Sau nhà (hai ô trên dưới). Khay cũng không có cây.
# a) treeTop(id): ô trên của cặp ô trồng được (chạm ô trên hay ô dưới đều ra cặp đó); treePlant nhận cả ô dưới.
rep("function treePlant(id, k){ const y = treeSpot(id), c = CROPS[k];",
    "function treeTop(id){ if (treeSpot(id)) return id; const P = PL[id]; if (!P || !P.bai || !TREEZ[zoneOf(P)]) return null; const Z = zoneOf(P) === 'song' ? SONG : SAU, i = +id.slice(1) - 1; if (Math.floor(i / Z.cols) !== 1) return null; const t = id[0] + (i - Z.cols + 1); return treeSpot(t) ? t : null; }\n"
    "const treeSpots = () => PLOTS.filter(P => P.bai && treeSpot(P.id)).map(P => P.id), treeZoneOn = () => PLOTS.some(P => P.bai && TREEZ[zoneOf(P)] && !hidP(P)), treeKs = () => Object.keys(CROPS).filter(k => CROPS[k].tree && !CROPS[k].rare && unlocked(k));\n"
    "const treeWhere = () => PLOTS.some(P => P.bai && P.zone === 'sau' && !hidP(P)) ? 'Cây trái trồng ở Mé sông hoặc Sau nhà' : 'Cây trái trồng ở Mé sông', treeNo = () => treeWhere() + '. Cần hai ô đất trống của con, trên dưới liền nhau.';\n"
    "function treePlant(id, k){ id = treeTop(id) || id; const y = treeSpot(id), c = CROPS[k];")
# b) khay: món loại 'tree'
rep("function sapIc(it){ if (it.t === 'obj')", "function sapIc(it){ if (it.t === 'tree') return ICON[it.k] || UIC.task; if (it.t === 'obj')")
rep("function sapName(it){ return it.t === 'obj'", "function sapName(it){ return it.t === 'tree' ? 'Cây ' + CROPS[it.k].name.toLowerCase() : it.t === 'obj'")
rep("function sapWhy(id, it){ const P = PL[id]; if (!P || !P.bai) return '';",
    "function sapWhy(id, it){ const P = PL[id]; if (!P || !P.bai) return ''; if (it && it.t === 'tree') return !TREEZ[zoneOf(P)] ? treeWhere() : !landOwn(id) ? 'Chưa khai hoang' : 'Cần 2 ô trống, trên dưới';")
rep("function sapFit(id, it){ if (!id) return null;", "function sapFit(id, it){ if (!id) return null; if (it.t === 'tree'){ const t = treeTop(id); return t ? [t, treeSpot(t)] : null; }")
rep("function sapPut(it, id){\n", "function sapPut(it, id){\n  if (it.t === 'tree'){ const t = treeTop(id); if (!t) return false; treePlant(t, it.k); return !!(ST.pairs || {})[t]; }\n")
rep("buy = (it.t === 'obj' && !ST[it.k].own) || it.t === 'ao';", "buy = (it.t === 'obj' && !ST[it.k].own) || it.t === 'ao' || it.t === 'tree';")
# kéo cây: không có chỗ thì nói thật và không nhấc; có chỗ thì lia máy tới
rep("function sapDragStart(it, cx, cy){ if (it.t === 'big'",
    "let SAPHI = 0;\nfunction sapTreeGo(){ const sp = treeSpots(); if (!sp.length) return false; const top = $('#sapBar').getBoundingClientRect().bottom + 30, bot = $('#sapTray').getBoundingClientRect().top - 30; if (sp.some(t => { const [x, y] = sapMid(PL[t]); return x > 30 && x < innerWidth - 30 && y > top && y < bot; })) return true; const z0 = zoneOf(PL[sp[0]]), B = sapUnion(sp.filter(t => zoneOf(PL[t]) === z0).flatMap(t => [t, treeSpot(t)])); try { camTo(new T.Vector3((B[0] + B[2]) / 2 + .4, .3, (B[1] + B[3]) / 2 + .6), cam.zoom); } catch (e) {} return true; }\n"
    "function sapDragStart(it, cx, cy){ if (it.t === 'tree' && !sapTreeGo()){ toast(treeNo(), 'dan', { now: true }); return; } if (it.t === 'big'")
rep("const ok = it.t === 'big' || it.t === 'ao' ? !!bigFit(P.id, sapBk(it))", "const ok = it.t === 'tree' ? !!treeTop(P.id) : it.t === 'big' || it.t === 'ao' ? !!bigFit(P.id, sapBk(it))")
# chạm (không kéo) vô cây trong khay: lia tới và làm sáng các cặp ô trồng được vài giây
rep("else if (P.id === SAPSEL && sapSan(P.id)) h += `<polygon class=\"sel\" points=\"${sapPoly(P.b)}\"/>`; }",
    "else if (P.id === SAPSEL && sapSan(P.id)) h += `<polygon class=\"sel\" points=\"${sapPoly(P.b)}\"/>`; if (SAPHI > performance.now()) for (const t of treeSpots()) h += `<polygon class=\"fit\" points=\"${sapPoly(sapUnion([t, treeSpot(t)]), .03)}\"/>`; }")
rep("if (TRAYP && e.pointerId === TRAYP.pid){ TRAYP = null; toast('Kéo món này ra một ô đất trống của con'); }",
    "if (TRAYP && e.pointerId === TRAYP.pid){ const tt = TRAYP.it.t === 'tree'; TRAYP = null; if (!tt) toast('Kéo món này ra một ô đất trống của con'); else if (sapTreeGo()){ SAPHI = performance.now() + 4000; SAPSEL = null; toast('Kéo cây ra chỗ đang sáng nghe con'); } else toast(treeNo(), 'dan', { now: true }); }")
# khay: thêm hàng "CÂY TRÁI" (lướt ngang), chỉ khi đã có vùng trồng cây
rep("  if (((ST.lv || 1) >= BIGD.ao.lv || (ST.keep || {}).ao) && !(ST.big.ao && ST.big.ao.own)) B.push({ t: 'ao', k: 'ao', buy: BIGD.ao.buy }); return [...L, ...B]; }",
    "  if (((ST.lv || 1) >= BIGD.ao.lv || (ST.keep || {}).ao) && !(ST.big.ao && ST.big.ao.own)) B.push({ t: 'ao', k: 'ao', buy: BIGD.ao.buy });\n"
    "  const TR = treeZoneOn() ? treeKs().map(k => { const n = (ST.seeds || {})[k] || 0; return n > 0 ? { t: 'tree', k, n } : { t: 'tree', k, buy: CROPS[k].seed }; }) : []; return [...L, ...B, ...TR]; }")
rep("  h += SAPITEMS.map((it, i) => `<div class=\"it${it.buy ? ' buy' : ''}${it.buy && ST.xu < it.buy ? ' poor' : ''}\" data-i=\"${i}\">",
    "  const itH = (it, i) => `<div class=\"it${it.buy ? ' buy' : ''}${it.buy && ST.xu < it.buy ? ' poor' : ''}\" data-i=\"${i}\">")
rep("${it.buy ? `<em><img src=\"${UIC.coin}\" alt=\"\">${it.buy}</em>` : ''}</div>`).join('');",
    "${it.buy ? `<em><img src=\"${UIC.coin}\" alt=\"\">${it.buy}</em>` : ''}</div>`, nT = SAPITEMS.filter(it => it.t === 'tree').length;\n  h += SAPITEMS.map((it, i) => it.t === 'tree' ? '' : itH(it, i)).join('');")
rep("  if (!SAPITEMS.length && !dcOn()) h +=", "  if (SAPITEMS.length === nT && !dcOn()) h +=")
rep("  t.innerHTML = h + '</div>'; }",
    "  if (nT) h += '</div><div class=\"stl\">CÂY TRÁI · chiếm 2 ô, kéo ra chỗ sáng</div><div class=\"row tr\">' + SAPITEMS.map((it, i) => it.t === 'tree' ? itH(it, i) : '').join('');\n  t.innerHTML = h + '</div>'; }")
rep("#sapTray .emp{", "#sapTray .stl{font:400 12px/1.3 var(--f-game);color:#6B4529;padding:8px 2px 0 4px}\n#sapTray .row.tr{flex-wrap:nowrap;overflow-x:auto;overflow-y:hidden;max-height:none;padding-top:8px;padding-bottom:5px;-webkit-overflow-scrolling:touch}\n#sapTray .row.tr .it{touch-action:pan-x}\n@media (max-width:480px){#sapTray{max-width:none}#sapTray .row:not(.tr){display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px 4px;padding-right:2px}#sapTray .row:not(.tr) .it{width:auto;min-width:0;padding-left:1px;padding-right:1px}#sapTray .row.tr{gap:4px;padding-right:2px;align-items:flex-start}#sapTray .row.tr .it{flex:0 0 calc((100% - 12px) / 4);width:auto;min-width:0;padding-left:1px;padding-right:1px}}\n#sapTray .emp{")
# c) nút "Cây" chỉ hiện ở ô trồng được; lời từ chối nói thật
rep("(tree.length ? `<button data-c=\"cay\">", "(tree.length && SAPSEL && treeTop(SAPSEL) ? `<button data-c=\"cay\">")
rep("{ if (!treeSpot(id)) return toast('Cây trái chiếm hai ô, ô ngay dưới cũng phải trống', 'dan', { now: true }); SHSUB = 'cay'; openSheet('plot', id); }",
    "{ const t = treeTop(id); if (!t) return toast(treeNo(), 'dan', { now: true }); SHSUB = 'cay'; openSheet('plot', t); }")
# d) bảng ô đất trống: ô trồng được cây thì hiện lại danh sách cây (trước đó bị nút Sắp vườn che mất)
T1o, T1n = 'Trồng cây trái · chiếm ô này và ô ngay dưới', 'Trồng cây trái · chiếm 2 ô trên dưới'
T2o, T2n = 'Hay trồng cây trái · chiếm ô này và ô ngay dưới', 'Hay trồng cây trái · chiếm 2 ô trên dưới'
rep("UX.title('" + T1o + "')", "UX.title('" + T1n + "')")
rep('"' + T1o + '": "Plant a fruit tree · takes this cell and the one below"', '"' + T1n + '": "Plant a fruit tree · takes 2 cells, one above the other"')
rep('"' + T2o + '": "Or plant a fruit tree · uses this plot and the one below"', '"' + T2n + '": "Or plant a fruit tree · takes 2 cells, one above the other"')
TL = "h += UX.title('" + T2o + "') + '<div class=\"upg\">' + ks.map(k => unlocked(k) ? UX.upc('treeplant', ICON[k], 'Cây ' + CROPS[k].name.toLowerCase(), CROPS[k].seed, { k, dis: ST.xu < CROPS[k].seed }) : '').join('') + '</div>';"
rep("{ const y = treeSpot(id); if (y){ const ks = Object.keys(CROPS).filter(k => CROPS[k].tree && !CROPS[k].rare); " + TL + " } else if (TREEZ[zoneOf(P)] && pairBelow(id)) h += '<div class=\"note\">Muốn trồng cây trái thì ô ngay dưới cũng phải là đất trống của con.</div>'; }",
    "{ const y = treeTop(id); if (y){ const ks = Object.keys(CROPS).filter(k => CROPS[k].tree && !CROPS[k].rare); " + TL.replace(T2o, T2n) + " } else if (TREEZ[zoneOf(P)] && treeKs().length) h += '<div class=\"note\">Muốn trồng cây trái thì cần hai ô đất trống của con, trên dưới liền nhau.</div>'; }")
rep("if (sapOk()) return h + sapAltHTML();",
    "if (sapOk()){ if (treeTop(id) && treeKs().length) h += UX.title('" + T2n + "') + '<div class=\"upg\">' + treeKs().map(k => UX.upc('treeplant', ICON[k], 'Cây ' + CROPS[k].name.toLowerCase(), CROPS[k].seed, { k, dis: ST.xu < CROPS[k].seed })).join('') + '</div>'; else if (TREEZ[zoneOf(P)] && treeKs().length) h += '<div class=\"note\">Muốn trồng cây trái thì cần hai ô đất trống của con, trên dưới liền nhau.</div>'; return h + sapAltHTML(); }")
# e) bản tiếng Anh
rep('"Cây trái chiếm hai ô, ô ngay dưới cũng phải trống": "Fruit trees take two cells, the one below must be empty too", ',
    '"Cây trái trồng ở Mé sông": "Fruit trees grow at the Riverbank", "Cây trái trồng ở Mé sông hoặc Sau nhà": "Fruit trees grow at the Riverbank or Behind the house", '
    '"Cây trái trồng ở Mé sông. Cần hai ô đất trống của con, trên dưới liền nhau.": "Fruit trees grow at the Riverbank. They need two of your empty cells, one above the other.", '
    '"Cây trái trồng ở Mé sông hoặc Sau nhà. Cần hai ô đất trống của con, trên dưới liền nhau.": "Fruit trees grow at the Riverbank or Behind the house. They need two of your empty cells, one above the other.", '
    '"Cần 2 ô trống, trên dưới": "Needs 2 empty cells, one above the other", "Kéo cây ra chỗ đang sáng nghe con": "Drag the tree to the glowing spot, dear", '
    '"CÂY TRÁI · chiếm 2 ô, kéo ra chỗ sáng": "FRUIT TREES · 2 cells, drag to the glowing spot", '
    '"Muốn trồng cây trái thì cần hai ô đất trống của con, trên dưới liền nhau.": "To plant a fruit tree you need two of your empty cells, one above the other.", ')
# khay hai hang vuot ngang: vuot ngang la cuon, keo doc moi la keo mon ra vuon
rep("TRAYP = { pid: e.pointerId, x: e.clientX, y: e.clientY, it: { t: it.t, k: it.k } };",
    "TRAYP = { pid: e.pointerId, x: e.clientX, y: e.clientY, it: { t: it.t, k: it.k }, sc: e.pointerType === 'touch' && !!c.closest('.row.tr') };")
rep("> 8){ const it = TRAYP.it; TRAYP = null; sapDragStart(it, e.clientX, e.clientY); } });",
    "> 8){ const it = TRAYP.it, sc = TRAYP.sc && Math.abs(e.clientX - TRAYP.x) > Math.abs(e.clientY - TRAYP.y); TRAYP = null; if (!sc) sapDragStart(it, e.clientX, e.clientY); } });")
# ten cay ban tieng Anh: "Banana tree" thay vi "Cay banana"; hai chu trong khay chua dich
OLDN = "'Cây ' + CROPS[k].name.toLowerCase()"
assert s.count(OLDN) == 3, s.count(OLDN); s = s.replace(OLDN, "treeNm(k)")
rep("'Cây ' + CROPS[it.k].name.toLowerCase()", "treeNm(it.k)")
rep("function sapName(it){", "function treeNm(k){ const n = CROPS[k].name.toLowerCase(); return EN ? n.charAt(0).toUpperCase() + n.slice(1) + ' tree' : 'Cây ' + n; }\nfunction sapName(it){")
assert '"TÚI ĐỒ · kéo ra vườn":' not in s and '"Mua thêm":' not in s
rep('"Cần 2 ô trống, trên dưới": ', '"TÚI ĐỒ · kéo ra vườn": "BAG · drag into the garden", "Mua thêm": "Buy more", "Cần 2 ô trống, trên dưới": ')
# bỏ mũi tên của bảng gieo (anh Ares: mũi tên lệch)
rep('.rng::after{content:"";position:absolute;', '.rng::after{display:none;content:"";position:absolute;')
open(DST, 'w', encoding='utf-8').write(s)
print('ok', DST)
