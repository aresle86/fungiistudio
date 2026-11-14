# v149f — ĐỒ QUÝ: giống quý + ông Bảy Kiếng (Ares duyệt ý, hình và số xu 14/11/2026)
#  1. 6 giống quý đột biến từ cây thường (ớt sừng vàng, bắp nếp tím, cà chua bi vàng, khổ qua rừng, mồng tơi tía, khóm mật).
#     Không bán ở đâu. Mỗi giống 4 điều kiện ẩn (đất, chăm, mùa, lúc hái). Đủ 4: mỗi lần hái 10% ra trái lạ + 1 hạt, lần thứ 6 chắc chắn.
#     Đúng 3/4: Ngoại nhận ra, lộ điều còn thiếu. Trồng hạt quý: bán gấp 3, mỗi lần hái 25% để lại 1 hạt. Món đầu +300 xu + chuyện Ngoại kể.
#  2. Lời đồn (giao đơn, chợ huyện, chai trong lờ) giờ kể cả cá lẫn giống.
#  3. Sổ thêm trang "Đồ quý miệt vườn" 11 ô.
#  4. Ông Bảy Kiếng: ghe ghé bến 2 ngày/tuần, sạp ở chợ huyện; món đầu x3, sau x1,5; hôm nay tìm mua +50%; nói thách 1 lần 60% được +20%.
#  5. Đủ bộ cá / đủ bộ giống: mỗi bộ một món trang trí riêng, bạn ghé thấy.
# Không đổi server. Không thêm liếp, không thêm bản đồ.
import sys, os
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
HERE = os.path.dirname(os.path.abspath(__file__))

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)

rep("BUILD = 'v149e'", "BUILD = 'v149f'")

# ---------- 1. GIỐNG QUÝ: bảng + điều kiện (đặt sớm, trước buildCrop) ----------
A = r"""
/* v149f — giống quý */
const QUY = {
  otvang: { base: 'ot', name: 'Ớt sừng vàng', en: 'Golden horn chili', col: '#F2A81E', dat: 'tot', cham: 'am', mua: 'kho', hai: 'chieu' },
  baptim: { base: 'bap', name: 'Bắp nếp tím', en: 'Purple sticky corn', col: '#8A58A6', dat: 'bon', cham: 'rom', mua: 'mua', hai: 'sang' },
  cachuavang: { base: 'cachua', name: 'Cà chua bi vàng', en: 'Yellow cherry tomato', col: '#FFC93A', dat: 'bon', cham: 'am', mua: 'kho', hai: 'sang' },
  khoquarung: { base: 'khoqua', name: 'Khổ qua rừng', en: 'Wild bitter melon', col: '#4E8A2E', dat: 'tot', cham: 'lua2', mua: 'mua', hai: 'chieu' },
  mongtoitia: { base: 'mongtoi', name: 'Mồng tơi tía', en: 'Purple Malabar spinach', col: '#7A4A96', dat: 'tot', cham: 'lua2', mua: 'mua', hai: 'thuan' },
  khommat: { base: 'khom', name: 'Khóm mật', en: 'Honey pineapple', col: '#F7B928', dat: 'bon', cham: 'rom', mua: 'kho', hai: 'chieu' } };
for (const k in QUY){ const q = QUY[k]; q.k = k; CROPS[k] = { ...CROPS[q.base], name: q.name, sell: CROPS[q.base].sell * 3, rare: 'quy', base: q.base }; }
const QUYB = {}; for (const k in QUY) QUYB[QUY[k].base] = k;
const QCX = ['dat', 'cham', 'mua', 'hai'];
const QCL = { tot: 'đất tốt', bon: 'đất đã bón phân', rom: 'phủ rơm', am: 'tưới đủ, không để héo', lua2: 'hái từ lứa thứ hai', mua: 'mùa mưa', kho: 'mùa khô', sang: 'hái buổi sáng', chieu: 'hái buổi chiều', thuan: 'tay trồng thuần thục' };
const quyOn = () => (ST.lv || 1) >= 3;
const quyMet = (q, p, x) => { const v = q[x]; return v === 'tot' ? p.soil >= .8 : v === 'bon' ? !!p.bon : v === 'rom' ? (p.mulch || 0) > ST.gt : v === 'am' ? !p.kho : v === 'lua2' ? (p.cut || 0) >= 1 : v === 'mua' || v === 'kho' ? muaSong() === v : v === 'thuan' ? mastS(q.base) >= 2 : gioNow() === v; };
const quySign = p => quyOn() && stageOf(p) >= 2 && QCX.every(x => quyMet(QUY[QUYB[p.crop]], p, x));
const QTM = {}, qtC = new T.Color(), qtQ = new T.Color(), qtH = {};
const quyTint = (k, sign) => c => { const key = k + sign + c; if (QTM[key] !== undefined) return QTM[key] || c;
  qtC.set(snap(c)); qtC.getHSL(qtH); const { h, s, l } = qtH, green = h > .15 && h < .48 && s > .15, red = (h < .06 || h > .94) && s > .35; let hit = 0;
  if (sign){ if (green){ qtQ.set(QUY[k].col); qtC.lerp(qtQ, .26); hit = 1; } }
  else if (k === 'otvang' || k === 'cachuavang'){ if (red){ qtC.setHSL(.115, .92, Math.min(.62, l + .12)); hit = 1; } }
  else if (k === 'baptim'){ if (h >= .1 && h <= .17 && s > .4){ qtC.setHSL(.78, .42, l * .62); hit = 1; } }
  else if (k === 'khoquarung'){ if (green){ qtC.setHSL(h, s, l * .72); hit = 1; } }
  else if (k === 'mongtoitia'){ if (green){ qtC.setHSL(.8, s * .8, l * .8); hit = 1; } }
  else if (k === 'khommat'){ if (h >= .06 && h <= .17 && s > .3){ qtC.setHSL(.12, .95, Math.min(.66, l + .1)); hit = 1; } }
  return (QTM[key] = hit ? new T.MeshStandardMaterial({ color: qtC.clone(), flatShading: true, roughness: .92, metalness: 0, side: T.DoubleSide }) : 0) || c; };
"""
rep("h: .5, rare: 'tet' } });", "h: .5, rare: 'tet' } });" + A)
rep("Object.assign(CB, NCB);", "Object.assign(CB, NCB); for (const k in QUY) CB[k] = CB[QUY[k].base];")

# vẽ 3D: giống quý đổi màu; liếp thường đủ 4 điều kiện thì lá ửng màu giống đó
rep(", key = (p.crop || '-') + st + cond; if (key === v.key) return false;",
    "; let qs = 0; try { qs = p.crop && QUYB[p.crop] && cond === 'ok' && quySign(p) ? 1 : 0; } catch (e) {} const key = (p.crop || '-') + st + cond + (qs ? 'q' : ''); if (key === v.key) return false;")
rep("TINT = cond === 'ok' ? null : makeTint(cond);",
    "TINT = cond !== 'ok' ? makeTint(cond) : CROPS[p.crop].rare === 'quy' ? quyTint(p.crop, 0) : qs ? quyTint(QUYB[p.crop], 1) : null;")

# cờ chăm sóc
rep("p.soil = Math.min(1, p.soil + HO.soil); H.bags--;", "p.soil = Math.min(1, p.soil + HO.soil); p.bon = 1; H.bags--;")
rep("if (p.dry > WILT) p.wiltT = (p.wiltT || 0) + dt;", "if (p.dry > WILT){ p.wiltT = (p.wiltT || 0) + dt; p.kho = 1; }")
rep("cut: 0, fast: 0, nw:", "cut: 0, fast: 0, kho: 0, nw:")
rep("wiltT: 0, cut: 0 }); refreshPlot(id); save(); closeSheet();", "wiltT: 0, cut: 0, bon: 0, kho: 0 }); refreshPlot(id); save(); closeSheet();")

# hái
rep("p.stolen = 0; try { mastUp(p.crop); } catch (e) {}", "p.stolen = 0; try { mastUp(p.crop); } catch (e) {} try { quyHarvest(id, p); } catch (e) {}")

# gieo: hết hạt quý
rep("if (c.rare && !pk) return say(`Hết hạt ${c.name.toLowerCase()} rồi. Giống quý chỉ bán ở Tiệm Tết trong Chợ.`, 'dan');",
    "if (c.rare && !pk) return say(c.rare === 'quy' ? L135(`Hết hạt ${c.name.toLowerCase()} rồi. Giống này không ai bán, mình phải tự gầy lại thôi con.`, `Out of ${c.name.toLowerCase()} seed. Nobody sells this one, dear, we have to raise it again ourselves.`) : `Hết hạt ${c.name.toLowerCase()} rồi. Giống quý chỉ bán ở Tiệm Tết trong Chợ.`, 'dan');")

# không cho giống quý lọt vào quà hạt, đơn thường, gợi ý mở khoá
rep("const ks = Object.keys(CROPS).filter(c => unlocked(c) && !CROPS[c].tree); const c = ks[Math.floor(Math.random() * ks.length)] || 'cai'; ST.seeds[c] = (ST.seeds[c] || 0) + 3;",
    "const ks = Object.keys(CROPS).filter(c => unlocked(c) && !CROPS[c].tree && !CROPS[c].rare); const c = ks[Math.floor(Math.random() * ks.length)] || 'cai'; ST.seeds[c] = (ST.seeds[c] || 0) + 3;")
rep("pool = Object.keys(CROPS).filter(k => unlocked(k) && (!CROPS[k].tree || (ST.fg || {})[k]))", "pool = Object.keys(CROPS).filter(k => unlocked(k) && !CROPS[k].rare && (!CROPS[k].tree || (ST.fg || {})[k]))")
rep("const ks = Object.keys(CROPS).filter(k => fits(k, P0)).sort((a, b) => UNLOCK[a] - UNLOCK[b])", "const ks = Object.keys(CROPS).filter(k => fits(k, P0) && !CROPS[k].rare).sort((a, b) => UNLOCK[a] - UNLOCK[b])")
rep("const nxt = P ? null : ks.filter(k => !unlocked(k)).sort((a, b) => UNLOCK[a] - UNLOCK[b])[0];", "const nxt = P ? null : ks.filter(k => !unlocked(k) && !CROPS[k].rare).sort((a, b) => UNLOCK[a] - UNLOCK[b])[0];")

# hình giống quý: vẽ lại cây gốc với bảng màu đổi
rep("const crop5 = () => {", "const crop5 = (QM, QK) => {")
rep("const MC = {}; const mt = c => MC[c] || (MC[c] = new T.MeshStandardMaterial({ color: c, flatShading: true, roughness: .85, metalness: 0, side: T.DoubleSide }));",
    "const MC = {}; const mt = c0 => { const c = QM && QM[String(c0).toLowerCase()] || c0; return MC[c] || (MC[c] = new T.MeshStandardMaterial({ color: c, flatShading: true, roughness: .85, metalness: 0, side: T.DoubleSide })); };")
rep("const shot = (name, build, dir = V(.25, .35, 1)) => {", "const shot = (name, build, dir = V(.25, .35, 1)) => { if (QK && name !== QK) return;")
rep("Object.assign(ICON, crop5()); Object.assign(ICON, FR.icons);", """Object.assign(ICON, crop5()); Object.assign(ICON, FR.icons);
{ const QIC = { otvang: { '#C9302A': '#E89A0E', '#B02A25': '#CC8208', '#E8453A': '#FFBE1E', '#D6352C': '#EFA512' }, baptim: { '#FFD23F': '#6A3A86', '#F2B824': '#9A6CB0' }, cachuavang: { '#E8453A': '#FFB81E', '#D6352C': '#EE9C0C', '#E25A3B': '#FFC93A' }, khoquarung: { '#86c84e': '#4E8A2E', '#9fd36a': '#6AA53A' }, khommat: { '#D89A2A': '#F7B928', '#E8B43A': '#FFD95A', '#C98A2A': '#E08A1A', '#6F9A60': '#A8623A' } };
  for (const k in QUY){ const b = QUY[k].base; try { if (QIC[k]){ const m = {}; for (const a in QIC[k]) m[a.toLowerCase()] = QIC[k][a]; ICON[k] = crop5(m, b)[b]; } } catch (e) {} if (!ICON[k]) ICON[k] = ICON[b]; } }""")

# lời đồn: cá lẫn giống
rep("const r = donGive(); if (r) B.chai = r.txt;", "const r = donAny(); if (r) B.chai = r.txt;")
rep("if (cauOn() && ST.donD !== dayKey()){ const r = donGive();", "if (ST.donD !== dayKey()){ const r = donAny();")
rep("if (cauOn() && ST.donC !== dayKey()){ const r = donGive();", "if (ST.donC !== dayKey()){ const r = donAny();")
rep("chSay(r.txt, 'Ông Tám bán cần câu')", "chSay(r.txt, r.q ? 'Cô Út bán rau' : 'Ông Tám bán cần câu')")

rep("tk('ghe', () => gheTick(t)); tk('tb', () => tbTick(t));", "tk('ghe', () => gheTick(t)); tk('tb', () => tbTick(t)); tk('quy', () => quyTick(t));")

MAIN = open(os.path.join(HERE, 'fix149f_main.js'), encoding='utf-8').read()
rep("function pgViecMini(){", MAIN + "\nfunction pgViecMini(){")

for part in ('fix149f_so.py', 'fix149f_bay.py', 'fix149f_en.py'):
    pth = os.path.join(HERE, part)
    if os.path.exists(pth):
        exec(open(pth, encoding='utf-8').read())

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
