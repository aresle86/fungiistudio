#!/usr/bin/env python3
"""v171: giàn trên đất (Sắp vườn, đợt 1).
- Ô đất khai hoang trống: thêm lựa "Giàn" cạnh "Liếp" / "Cây". Số giàn không giới hạn.
- Giá giàn 90 xu (gấp rưỡi liếp gốc 60 xu). Đổi liếp qua giàn tính như dựng mới (90 xu). Giàn về lại liếp, san giàn thành cỏ: không tốn.
- Ô đang có cây: hỏi một câu, đồng ý là nhổ và trả lại 1 bao hạt. Cây tới lứa thì nhắc hái trước.
- Giàn trên đất không cần tưới như giàn trên mương. Hai giàn trên mương giữ nguyên.
- ST.gian = {id: 1}; ô bãi có getter P.trellis đọc từ ST.gian nên mọi chỗ đang hỏi P.trellis chạy luôn.
python3 fix171.py live/v170.html live/v171.html"""
import sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf8').read()
def rep(a, b, n=1):
    global t
    c = t.count(a)
    assert c == n, (c, a[:80])
    t = t.replace(a, b)

rep("BUILD = 'v170'", "BUILD = 'v171'")

# 1. ô bãi: P.trellis đọc từ ST.gian
rep("for (const P of PLOTS){ const sdX = sd;",
    "for (const Q of PLOTS) if (Q.bai && !Q.co) Object.defineProperty(Q, 'trellis', { configurable: true, get(){ try { return !!(ST.gian && ST.gian[Q.id]); } catch (e) { return false; } } });\n"
    "for (const P of PLOTS){ const sdX = sd;")
rep("if (!P.trellis && !P.tree){ v.soilMat", "if ((!P.trellis || P.bai) && !P.tree){ v.soilMat")
rep("hit.userData.plot = P.id; S.add(hit); HITS.push(hit);", "hit.userData.plot = P.id; S.add(hit); HITS.push(hit); v.hit = hit;")
rep("if (!ST.land) ST.land = {};", "if (!ST.land) ST.land = {}; if (!ST.gian) ST.gian = {};")

# 2. hình giàn trên ô bãi (xoay dọc theo chiều dài ô), dựng một lần khi cần
rep("if (P.bai){ const on = !hidP(P), lk = locked(P), nh =",
    "if (P.bai){ { const gi = !!P.trellis && !locked(P) && !hidP(P); if (gi && !v.gianG){ const tg = new T.Group(), [a0, b0, a1, b1] = P.b; tg.position.set((a0 + a1) / 2, 0, (b0 + b1) / 2); tg.rotation.y = Math.PI / 2; const pr = ROOT, ps = sd; ROOT = tg; sd = 2100 + id.charCodeAt(0) * 7 + id.length; gianFrame(GIANB[0], GIANB[1], GIANB[2], GIANB[3]); ROOT = pr; sd = ps; const g = v.gianG = new T.Group(); v.root.updateMatrixWorld(true); const iv = v.root.matrixWorld.clone().invert(); for (const m of mergeMeshes(tg)){ m.geometry.applyMatrix4(iv); g.add(m); } v.root.add(g); } if (v.gianG) v.gianG.visible = gi; if (v.hit){ const s = gi ? 2 : 1; v.hit.scale.y = s; v.hit.position.y = .3 * s; } }\n"
    "    const on = !hidP(P), lk = locked(P), nh =")
rep("function gianFrame(u0, v0, u1, v1, top = 1.05){",
    "const GIANB = [-.27, -.5, .27, .5];   /* v171: khung giàn trên ô đất, tính từ tâm ô, xoay 90 độ */\nfunction gianFrame(u0, v0, u1, v1, top = 1.05){")
rep("sway(cond === 'dead' ? .1 : CROPS[p.crop].sway, () => CB[p.crop](typeof unionB === 'function' && ST.pairs && ST.pairs[id] ? unionB(id) : P.b, Math.max(0, st)));\n  ROOT = S; TINT = null;",
    "const gb = !!(P.bai && P.trellis); sway(cond === 'dead' ? .1 : CROPS[p.crop].sway, () => CB[p.crop](gb ? GIANB : typeof unionB === 'function' && ST.pairs && ST.pairs[id] ? unionB(id) : P.b, Math.max(0, st)));\n  ROOT = S; TINT = null; if (gb){ tmp.position.set((P.b[0] + P.b[2]) / 2, 0, (P.b[1] + P.b[3]) / 2); tmp.rotation.y = Math.PI / 2; }")
rep("AVT = PL[id].trellis ?", "AVT = PL[id].trellis && !PL[id].bai ?")

# 3. dựng giàn, tháo giàn, san
rep("function baiSan(id){ const P = PL[id], p = ST.plots[id]; if (!P || !P.bai || locked(P) || p.crop) return; ST.open = ST.open.filter(i => i !== id);",
    "const GIANXU = 90; let SAPASK = null;\n"
    "function gianPuff(id){ const [u0, v0, u1, v1] = PL[id].b; for (let i = 0; i < 16; i++) puff('leaf', R(u0, u1), .15, R(v0, v1), 1, pick(['#6E9A4A', '#8fb85a', '#C9A45C']), .7); for (let i = 0; i < 8; i++) puff('seed', R(u0, u1), .2, R(v0, v1), 1, pick(['#8A5D3B', '#6B4529']), .5); }\n"
    "function gianMake(id){ const P = PL[id]; if (!P || !P.bai || P.co || VISIT) return false; if (!ST.gian) ST.gian = {}; if (ST.gian[id] && !locked(P)) return false; if (ST.xu < GIANXU){ toast(L135(`Dựng giàn tốn ${GIANXU} xu, con còn thiếu ${GIANXU - ST.xu} xu.`, `A trellis costs ${GIANXU} coins, you are ${GIANXU - ST.xu} short.`), 'dan', { now: true }); return false; }\n"
    "  if (locked(P)){ if (objAt(id) || !landOwn(id) || pairHost(id)) return false; ST.open.push(id); ST.plots[id] = pl0(null, 0, .5); if (P.zone === 'song') ST.plots[id].soil = 1; gainXP(2); }\n"
    "  ST.xu -= GIANXU; ST.gian[id] = 1; gianPuff(id); coinPop(L135(`-${GIANXU} xu · dựng giàn`, `-${GIANXU} coins · trellis`), '#F08A6E'); sfx('pop'); buzz(25); avGo(id); PV[id].key = null; for (const Q of PLOTS) refreshPlot(Q.id); save(); hud(); return true; }\n"
    "function gianUnmake(id){ const P = PL[id]; if (!P || !P.bai || !ST.gian || !ST.gian[id] || VISIT) return false; delete ST.gian[id]; gianPuff(id); sfx('pick'); PV[id].key = null; for (const Q of PLOTS) refreshPlot(Q.id); save(); hud(); return true; }\n"
    "function baiSan(id){ const P = PL[id], p = ST.plots[id]; if (!P || !P.bai || locked(P) || p.crop) return; if (ST.gian) delete ST.gian[id]; ST.open = ST.open.filter(i => i !== id);")

# 4. Sắp vườn: lựa Giàn / Làm giàn / Làm liếp
rep("function sapChipsDraw(){ if (SAPSEL && PL[SAPSEL] && PL[SAPSEL].co){",
    "function sapChipsDraw(){ $('#sapChips').classList.remove('ask'); if (SAPSEL && PL[SAPSEL] && PL[SAPSEL].co){")
rep("if (SAPSEL && sapSan(SAPSEL)){ ch.innerHTML = `<button data-c=\"san\"><img src=\"${UIC.sickle || ICON.la}\" alt=\"\">San thành cỏ</button>`; return; }",
    "if (SAPSEL && (sapSan(SAPSEL) || sapDoi(SAPSEL))){ const p = ST.plots[SAPSEL] || {}, gi = !!PL[SAPSEL].trellis, c = p.crop && CROPS[p.crop];\n"
    "    if (c && SAPASK === SAPSEL){ const nm = nm135(c.name).toLowerCase(); ch.classList.add('ask'); ch.innerHTML = `<span class=\"sapq\">${p.dead ? L135(`Dọn ${nm} héo rồi ${gi ? 'làm liếp' : 'dựng giàn'} nghe con`, `Clear the dead ${nm}, then ${gi ? 'make a bed' : 'build the trellis'}`) : L135(`Nhổ ${nm}, trả lại con 1 bao hạt`, `Pull the ${nm}, you get 1 seed bag back`)}</span><span class=\"sapr\"><button data-c=\"doiok\">${L135('Đồng ý', 'OK')}</button><button data-c=\"doino\">${L135('Thôi', 'Never mind')}</button></span>`; return; }\n"
    "    ch.innerHTML = (c ? '' : `<button data-c=\"san\"><img src=\"${UIC.sickle || ICON.la}\" alt=\"\">San thành cỏ</button>`) + (gi ? `<button data-c=\"doi\"><img src=\"${ICON.cai}\" alt=\"\">${L135('Làm liếp', 'Make bed')}</button>` : gianOk() ? `<button data-c=\"doi\"><img src=\"${ICON[gianOk()]}\" alt=\"\">${L135(`Làm giàn · ${GIANXU} xu`, `Trellis · ${GIANXU} coins`)}</button>` : ''); return; }")
rep("ch.innerHTML = `<button data-c=\"liep\"><img src=\"${ICON.cai}\" alt=\"\">Liếp</button>` + (tree.length",
    "ch.innerHTML = `<button data-c=\"liep\"><img src=\"${ICON.cai}\" alt=\"\">Liếp</button>` + (gianOk() ? `<button data-c=\"gian\"><img src=\"${ICON[gianOk()]}\" alt=\"\">${L135(`Giàn · ${GIANXU} xu`, `Trellis · ${GIANXU} coins`)}</button>` : '') + (tree.length")
rep("function sapPick(id){ SAPSEL = SAPSEL === id ? null : id;", "function sapPick(id){ SAPASK = null; SAPSEL = SAPSEL === id ? null : id;")
rep("function sapTap(cx, cy){",
    "const gianOk = () => Object.keys(CROPS).filter(k => CROPS[k].kind === 'trellis' && !CROPS[k].rare && unlocked(k)).sort((a, b) => UNLOCK[a] - UNLOCK[b])[0] || null;\n"
    "const sapDoi = id => { const P = PL[id]; return !!P && !!P.bai && !P.co && !hidP(P) && landOwn(id) && !locked(P) && !objAt(id) && decoAt(id) < 0 && !bigAt(id) && !(ST.pairs || {})[id] && !pairHost(id) && !((ST.plots[id] || {}).crop && CROPS[ST.plots[id].crop].tree) && (!!P.trellis || !!gianOk()); };\n"
    "function sapDoiAct(c){ const id = SAPSEL, P = PL[id], p = ST.plots[id] || {}; if (!P) return; if (c === 'doino'){ SAPASK = null; sapChipsDraw(); return; } if (c === 'gian'){ SAPSEL = null; gianMake(id); return; } if (!sapDoi(id)){ SAPSEL = null; return; }\n"
    "  const gi = !!P.trellis; if (!gi && ST.xu < GIANXU){ SAPSEL = null; SAPASK = null; gianMake(id); return; }\n"
    "  if (p.crop && c === 'doi'){ if (!p.dead && ripe(p)){ SAPSEL = null; toast(L135('Cây tới lứa rồi, hái xong rồi đổi nghe con.', 'It is ready to pick. Harvest first, then switch.'), 'dan', { now: true }); return; } SAPASK = id; sapChipsDraw(); return; }\n"
    "  SAPSEL = null; SAPASK = null; let back = null; if (p.crop){ const k = p.crop; if (!p.dead){ ST.seeds[k] = (ST.seeds[k] || 0) + 1; back = k; } p.cut = 0; Object.assign(p, { crop: null, g: 0, dry: 0, dead: false, wiltT: 0 }); }\n"
    "  const ok = gi ? gianUnmake(id) : gianMake(id); if (!ok){ save(); refreshPlot(id); return; }\n"
    "  const tail = back ? L135(` Trả con 1 bao hạt ${nm135(CROPS[back].name).toLowerCase()}.`, ` 1 ${nm135(CROPS[back].name).toLowerCase()} seed bag returned.`) : ''; toast((gi ? L135('Tháo giàn xong, ô này thành liếp rồi con.', 'Trellis removed, this is a bed now.') : L135('Dựng giàn xong rồi con.', 'Trellis is up, dear.')) + tail); }\n"
    "function sapTap(cx, cy){")
rep("if (id && (sapFree(id, null) || sapSan(id))) return sapPick(id);", "if (id && (sapFree(id, null) || sapSan(id) || sapDoi(id))) return sapPick(id);")
rep("if (SAPSEL && !sapFree(SAPSEL, null) && !sapSan(SAPSEL) && !(PL[SAPSEL].co && !landOwn(SAPSEL))) SAPSEL = null;",
    "if (SAPSEL && !sapFree(SAPSEL, null) && !sapSan(SAPSEL) && !sapDoi(SAPSEL) && !(PL[SAPSEL].co && !landOwn(SAPSEL))) SAPSEL = null;")
rep("else if (P.id === SAPSEL && sapSan(P.id)) h += `<polygon class=\"sel\"", "else if (P.id === SAPSEL && (sapSan(P.id) || sapDoi(P.id))) h += `<polygon class=\"sel\"")
rep("const id = SAPSEL; SAPSEL = null; if (b.dataset.c === 'hint') return;",
    "if (/^(gian|doi|doiok|doino)$/.test(b.dataset.c)){ sapDoiAct(b.dataset.c); return; } const id = SAPSEL; SAPSEL = null; if (b.dataset.c === 'hint') return;")

# 5. chữ: giàn không còn chỉ ở trên mương
rep("`Kéo thả vào chân giàn trên mương để trồng ${c.name.toLowerCase()}`", "`Kéo thả vào chân giàn để trồng ${c.name.toLowerCase()}`")
rep("`${c.name} phải trồng ở giàn trên mương con.`", "L135(`${c.name} phải trồng ở giàn con.`, `${nm135(c.name)} goes on a trellis, dear.`)", 2)
rep("c.kind === 'trellis' ? 'Giàn trên mương' :", "c.kind === 'trellis' ? L135('Trồng ở giàn', 'Grows on a trellis') :")
rep("shT.textContent = c ? c.name : P.tree ? 'Gốc trống' : 'Liếp trống';", "shT.textContent = c ? c.name : P.tree ? 'Gốc trống' : P.trellis ? L135('Giàn trống', 'Empty trellis') : 'Liếp trống';")
rep("h += UX.hero(UIC.seedbag, P.tree ? 'Gốc trống' : 'Liếp trống', P.tree ?", "h += UX.hero(UIC.seedbag, P.tree ? 'Gốc trống' : P.trellis ? L135('Giàn trống', 'Empty trellis') : 'Liếp trống', P.tree ?")
rep("UX.card('Giàn trên mương', 'Rễ sát mương <small>· không cần tưới</small>')",
    "(P.bai ? UX.card(L135('Giàn trên đất', 'Trellis on land'), L135('Giàn che mát gốc <small>· không cần tưới</small>', 'Shaded roots <small>· no watering needed</small>')) : UX.card('Giàn trên mương', 'Rễ sát mương <small>· không cần tưới</small>'))")
rep(": p.crop ? CROPS[p.crop].name : 'Liếp trống'; }", ": p.crop ? CROPS[p.crop].name : P.trellis ? L135('Giàn trống', 'Empty trellis') : 'Liếp trống'; }")
rep("return UX.hero(UIC.seedbag, 'Liếp trống', 'Gieo hạt, hay san phẳng thành đất trống để đặt đồ')",
    "return UX.hero(UIC.seedbag, P.trellis ? L135('Giàn trống', 'Empty trellis') : 'Liếp trống', 'Gieo hạt, hay san phẳng thành đất trống để đặt đồ')")

i = t.index('</style>'); t = t[:i] + (
    "#sapChips.ask{flex-direction:column;align-items:stretch;width:232px}\n"
    "#sapChips .sapq{box-sizing:border-box;background:#FFF8E7;border:2px solid #4A2F1E;border-radius:10px;box-shadow:0 3px 0 #4A2F1E;padding:8px 12px;font:600 13px/1.35 var(--f-body);color:#4A2F1E}\n"
    "#sapChips .sapr{display:flex;gap:8px}#sapChips .sapr button{flex:1;justify-content:center;padding:4px 12px}\n") + t[i:]

open(dst, 'w', encoding='utf8').write(t)
print('ok', len(t))
