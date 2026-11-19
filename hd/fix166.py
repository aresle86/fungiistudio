# v165 -> v166:
# 1) Bến bà con: bảng tên xuồng treo trên ngọn cây bẹo (cao 1,6) nên nhìn như chỉ vô xuồng hàng sau.
#    Hạ bảng xuống sát xuồng của nó (TAGY), mũi nhọn của bảng chỉ thẳng vô xuồng.
# 2) Tiếng Anh: dịch nốt tên người nói "Ông Tám bán cần câu" và bốn mẫu lời đồn cá ở chợ huyện.
import sys, os
SRC, DST = sys.argv[1], sys.argv[2]
TAGY = os.environ.get('TAGY', '.95')
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), n, a[:60])
    s = s.replace(a, b)
rep("BUILD = 'v165'", "BUILD = 'v166'")

rep("const tg = tag(root, x + Math.cos(ry) * .55, 1.6, z - Math.sin(ry) * .55, pl.nm,",
    "const tg = tag(root, x + Math.cos(ry) * .55, " + TAGY + ", z - Math.sin(ry) * .55, pl.nm,")

rep("  UIRX.unshift(\n    [/^Sổ bướm · ",
    "  Object.assign(UIEN, { 'Ông Tám bán cần câu': 'Uncle Tám the tackle seller' });\n"
    "  const _dsp = { 'gần bến': 'near the pier', 'giữa sông': 'out in mid-river', 'mé lục bình': 'by the water hyacinth' }, _dgi = { 'sáng': 'in the morning', 'trưa': 'at noon', 'chiều': 'in the afternoon', 'đêm': 'at night' },\n"
    "    _dmo = { 'trùn': 'worms', 'cơm nguội': 'leftover rice', 'tép': 'shrimp', 'sâu, châu chấu': 'bugs and grasshoppers' },\n"
    "    _dtr = { 'mùa khô': 'in the dry season', 'mùa mưa': 'in the rainy season', 'mùa nước nổi': 'in the flood season', 'nước lớn': 'at high tide', 'nước ròng': 'at low tide', 'đêm trăng rằm': 'on a full-moon night', 'đêm không trăng': 'on a moonless night', 'trời nào cũng được': 'in any weather' },\n"
    "    _dl = (a, d, j) => a.split(', ').map(w => d[w] || w).join(j);\n"
    "  UIRX.unshift(\n"
    "    [/^Nghe nói con (.+) hay nằm (gần bến|giữa sông|mé lục bình)\\.$/, (m, n, a) => 'Word is the ' + _nm(n) + ' likes to stay ' + _dsp[a] + '.'],\n"
    "    [/^Người ta đồn con (.+) chỉ ăn lúc (.+)\\.$/, (m, n, a) => a === 'cả ngày' ? 'They say the ' + _nm(n) + ' bites all day.' : 'They say the ' + _nm(n) + ' only bites ' + _dl(a, _dgi, ' or ') + '.'],\n"
    "    [/^Dân câu nói con (.+) mê mồi (.+) lắm\\.$/, (m, n, a) => 'Anglers say the ' + _nm(n) + ' loves ' + (_dmo[a] || a) + '.'],\n"
    "    [/^Nghe nói phải (.+) mới gặp con (.+)\\.$/, (m, a, n) => 'Word is you only meet the ' + _nm(n) + ' ' + _dl(a, _dtr, ', ') + '.'],\n"
    "    [/^Sổ bướm · ")

# 3) Tặng giống quý cho hàng xóm (số Ares duyệt 19/11): phải còn >= 2 hạt (không tặng hạt cuối), dùng chung lượt tặng 1 lần / người / ngày
#    của máy chủ (mv2_act kiểu gift, không sửa máy chủ), người tặng +15 kinh nghiệm. Nút "Tặng hạt" thường không lấy hạt giống quý nữa.
#    Người nhận hái ra thì ghi Sổ Đồ quý (đem cho ông Bảy được) nhưng không có 300 xu tìm ra lần đầu.
rep(".rpk .leadt{margin-left:8px}",
    ".rpk .leadt{margin-left:8px}.leadt.gq{background:#8F6212;font-size:12px}.rpk .rt>b{display:flex;flex-wrap:wrap;align-items:center;gap:4px 8px}.rpk .rt>b .leadt{margin-left:0}"
    ".gqrow{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:8px;padding:12px;background:#FBF7EE;border-radius:var(--r2);box-shadow:0 3px 0 #E3D3BC}"
    ".gqrow>b{flex:1 1 100%;font-size:14px;color:#4A2F1E}.gqrow .btn{min-height:44px;display:inline-flex;align-items:center;gap:8px}.gqrow .btn img{width:24px;height:24px;flex:none}"
    "@media (max-width:560px){ .vcard.nb .nbb{flex-wrap:wrap} }")
rep("const btns = (ask ? `<button class=\"btn\" data-a=\"nbgive\" data-k=\"${n.code}\">Tặng hạt</button>` : '') + ",
    "const btns = (ask ? `<button class=\"btn\" data-a=\"nbgive\" data-k=\"${n.code}\">Tặng hạt</button>` : '') + (GQL.length ? `<button class=\"btn\" data-a=\"nbq\" data-k=\"${n.code}\">${L135('Tặng giống quý', 'Gift a rare seed')}</button>` : '') + ")
rep("const VD = vdGet(); return h + NB2.list.map(n => { const ask = NB2.ask[n.code],",
    "const VD = vdGet(), GQL = gqList(); return h + NB2.list.map(n => { const ask = NB2.ask[n.code],")
rep("</div><div class=\"nbb\">${btns}</div></div>`; }).join('') + nbSugHTML(); }",
    "</div><div class=\"nbb\">${btns}</div></div>` + (SHEET && SHEET.gq === n.code && GQL.length ? `<div class=\"gqrow\"><b>${L135('Chọn giống tặng ', 'Pick a seed for ')}${esc(n.name || L135('hàng xóm', 'your neighbour'))}</b>${GQL.map(k => `<button class=\"btn\" data-a=\"nbqgive\" data-k=\"${n.code}\" data-n=\"${k}\"><img src=\"${ICON[k]}\" alt=\"\">${L135(QUY[k].name, QUY[k].en)} · ${L135('còn', 'have')} ${ST.seeds[k]}</button>`).join('')}</div>` : ''); }).join('') + nbSugHTML(); }\n"
    "function gqList(){ return QGI.filter(k => (ST.seeds[k] || 0) >= 2).sort((a, b) => ST.seeds[b] - ST.seeds[a]); }")
rep("else if (a === 'nbgive'){ const code = b.dataset.k, k = Object.entries(ST.seeds).filter(([, n]) => n > 0)",
    "else if (a === 'nbq'){ SHEET.gq = SHEET.gq === b.dataset.k ? null : b.dataset.k; }\n"
    "  else if (a === 'nbqgive'){ const code = b.dataset.k, k = b.dataset.n; if (b.disabled || !QUY[k] || !((ST.seeds[k] || 0) >= 2)) return; b.disabled = true;\n"
    "    rpc('mv2_act', { p_code: CLOUD.cred.code, p_secret: CLOUD.cred.secret, p_other: code, p_kind: 'gift', p_payload: { k, n: 1, seed: 1 } }).then(r => { if (r && r.ok){ ST.seeds[k]--; delete NB2.ask[code]; SHEET.gq = null; save(); buyFx(b, ICON[k], L135(`Tặng 1 hạt ${QUY[k].name.toLowerCase()}`, `Gave 1 ${QUY[k].en.toLowerCase()} seed`), 0); gainXP(15); } else toast('Hôm nay con tặng người này rồi.', 'vui', { now: true }); renderSheet(); }).catch(e => { toast(vErr(e, 'chưa tặng được'), 'lo', { now: true }); renderSheet(); }); return; }\n"
    "  else if (a === 'nbgive'){ const code = b.dataset.k, k = Object.entries(ST.seeds).filter(([j, n]) => n > 0 && CROPS[j] && !CROPS[j].rare)")
rep("if (c.rare === 'quy'){ if (!(ST.seeds[k0] > 0) || Math.random() < .25){",
    "if (c.rare === 'quy'){ { const Q0 = quyQ(); if (!Q0.got[k0]){ Q0.got[k0] = 1; setTimeout(() => say(L135(`Giống ${c.name.toLowerCase()} bà con tặng ra trái rồi nè. Ngoại ghi vô Sổ Đồ quý cho con nghe.`, `The ${(QUY[k0].en || c.name).toLowerCase()} our neighbour gave us has fruited. Ngoại wrote it into the Rare Book for you.`), 'vui', { idle: true }), 1100); } }\n"
    "    if (!(ST.seeds[k0] > 0) || Math.random() < .25){")

# 4) Nấu bằng giống quý (số Ares duyệt 19/11): giá món = giá thường + 2,6 x giá gốc cho mỗi trái giống quý bỏ vô nồi.
#    Người chơi tự chọn dòng "Giống quý" trong bảng chọn món (chỉ hiện khi đủ trái giống quý cho nguyên liệu đó), không tự lấy trái quý.
#    Món bán qua rất nhiều đường (chợ, ghe, đơn nhà bên, khách bến…) nên ghi sổ ST.gbq[k] = { n: số món quý trên gác, s: tổng xu thêm, c: số món lần lưu trước };
#    mỗi lần lưu thấy món rời gác bếp thì trả phần thêm (món quý tính đi trước).
rep("<img src=\"${ICON[k]}\" alt=\"\"><div class=\"rt\"><b>${d.name}</b>", "<img src=\"${ICON[d.k0 || k]}\" alt=\"\"><div class=\"rt\"><b>${d.name}</b>")
rep("<div class=\"rm\">${fmtT(ttTime(k, d.t))}<em>", "<div class=\"rm\">${fmtT(ttTime(d.k0 || k, d.t))}<em>")
rep("tu = monTu(), R = Object.fromEntries(Object.entries(DISH).filter(([, d]) => !d.nuoc).map(", "tu = monTu(), R = gqRows(SHEET.pick, Object.entries(DISH).filter(([, d]) => !d.nuoc).map(")
rep("t: d.t / ST.spd }])); return SHEET.pick < 0", "t: d.t / ST.spd }])); return SHEET.pick < 0")
rep("function bepCook(k){ const d = DISH[k], B = ST.bep, i = B.pots.findIndex(p => !p); if (d.nuoc || (ST.lv || 1) < dLv(k) || i < 0 || !bepCan(k)) return; for (const [j, q] of Object.entries(d.in)) STORE(j)[j] -= q;\n"
    "  B.pots[i] = { k, t: ttTime(k, d.t), T: ttTime(k, d.t) }; if (kemUse(k)) B.pots[i].x2 = 1;",
    "function gqSub(k){ const d = DISH[k]; if (!d || d.nuoc) return null; const inp = {}; let b = 0; for (const [j, q] of Object.entries(d.in)){ const r = QUYB[j]; if (r && has(r) >= q){ inp[r] = q; b += 2.6 * CROPS[j].sell * q; } else inp[j] = q; } return b ? { in: inp, b: Math.round(b) } : null; }\n"
    "function gqRows(i, E){ const o = {}; for (const [k, d] of E){ const s = i >= 0 ? gqSub(k) : null; if (s && (ST.lv || 1) >= (d.lv || 1) && canIn(s.in)) o[k + '~q'] = { ...d, k0: k, in: s.in, sell: d.sell + s.b, name: d.name + `<em class=\"leadt gq\">${L135('Giống quý', 'Rare crop')}</em>` }; o[k] = d; } return o; }\n"
    "function gqSold(){ const G = ST.gbq; if (!G) return; let pay = 0; for (const k of Object.keys(G)){ const L = G[k], cur = (ST.gb && ST.gb[k]) || 0, n = Math.min(L.n, Math.max((L.c || 0) - cur, L.n - cur, 0)); if (n > 0){ const v = n >= L.n ? L.s : Math.round(L.s / L.n * n); L.n -= n; L.s -= v; pay += v; } L.c = cur; if (L.n <= 0) delete G[k]; }\n"
    "  if (pay > 0){ ST.xu += pay; setTimeout(() => { try { sfx('coin'); coinPop(L135(`+${pay} xu · món giống quý`, `+${pay} coins · rare-crop dish`), '#F5D27A'); hud(); } catch (e) {} }, 350); } }\n"
    "function bepCook(k){ let gq = null; if (/~q$/.test(k)){ k = k.slice(0, -2); gq = gqSub(k); if (!gq || !canIn(gq.in)) return; } const d = DISH[k], B = ST.bep, i = B.pots.findIndex(p => !p); if (d.nuoc || (ST.lv || 1) < dLv(k) || i < 0 || !(gq || bepCan(k))) return; for (const [j, q] of Object.entries(gq ? gq.in : d.in)) STORE(j)[j] -= q;\n"
    "  B.pots[i] = { k, t: ttTime(k, d.t), T: ttTime(k, d.t) }; if (gq) B.pots[i].q = gq.b; if (kemUse(k)) B.pots[i].x2 = 1;")
rep("if (p) bepBank(p.k, p.x2);", "if (p) bepBank(p.k, p.x2, p.q);")
rep("B.pots[i] = null; bepBank(p.k, p.x2);", "B.pots[i] = null; bepBank(p.k, p.x2, p.q);")
rep("function bepBank(k, x2){ const B = ST.bep, d = DISH[k]; ST.gb[k] = (ST.gb[k] || 0) + (x2 ? 2 : 1);",
    "function bepBank(k, x2, gq){ const B = ST.bep, d = DISH[k]; ST.gb[k] = (ST.gb[k] || 0) + (x2 ? 2 : 1); if (gq){ const G = ST.gbq = ST.gbq || {}, L = G[k] = G[k] || { n: 0, s: 0, c: 0 }, m = x2 ? 2 : 1; L.n += m; L.s += gq * m; }")
rep("const save = () => { if (VISIT) return; ST.real", "const save = () => { if (VISIT) return; try { gqSold(); } catch (e) {} ST.real")
rep("  if (B.kem || Object.values(KEM).some(j => has(j) >= 1)) h += `<div class=\"vcard\"><img src=\"${ICON.khocasac}\"",
    "  { const G = Object.entries(ST.gbq || {}).filter(([, L]) => L.n > 0), n = G.reduce((a, [, L]) => a + L.n, 0), sx = G.reduce((a, [, L]) => a + L.s, 0); if (n) h += `<div class=\"vcard\"><img src=\"${ICON[G[0][0]]}\" alt=\"\"><div><b>${L135('Món nấu bằng giống quý', 'Rare-crop dishes')}</b><span>${L135(`${n} món trên gác bếp · bán ra được thêm ${sx} xu`, `${n} in the loft · worth ${sx} extra coins when sold`)}</span></div></div>`; }\n"
    "  if (B.kem || Object.values(KEM).some(j => has(j) >= 1)) h += `<div class=\"vcard\"><img src=\"${ICON.khocasac}\"")

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
