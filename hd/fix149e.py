# v149e: ghe tam bản dùng được nhiều việc (Ares duyệt 14/11/2026: "Ok làm"; luật "làm ra gì phải tận dụng tốt món đó")
# 1. thả lờ có chọn chỗ (gần bến / giữa sông / mé lục bình), lờ gom cá đúng chỗ, 5% ra cá rất hiếm đúng chỗ + đúng mùa
# 2. lờ kéo lên chai lời đồn 30% mỗi lần thu
# 3. câu trên ghe giữa sông: +3 lượt riêng mỗi ngày, cá nặng hơn 20%
# 4. chuyến hàng chợ nổi mỗi ngày: 3 món, trả gấp 1,3
# 5. sơn ghe bằng màu đã mua cho xuồng (không tốn thêm)
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)

rep("BUILD = 'v149d'", "BUILD = 'v149e'")

# --- hằng số + hàm phụ ---
rep("const TB = { lv: 19, xu: 7000, h: 4, help: 2, lo: 6, at: [8.6, R0 + 1.25] };",
    """const TB = { lv: 19, xu: 7000, h: 4, help: 2, lo: 6, at: [8.6, R0 + 1.25], cau: 3, nang: 1.2, lohiem: .05, chai: .3, chomul: 1.3 };
function TBP(){ const k = ST.tb && ST.tb.paint, P = k && k !== 'moc' && CNX.P[k]; return P ? [P[3], P[4]] : ['#B8402E', '#3E7460']; }   /* màu mũi ghe: màu sơn xuồng đã mua, mặc định đỏ viền xanh */
const tbReady = () => !!(ST.tb && ST.tb.done);
const gLeft = () => tbReady() ? TB.cau - (ST.cau.gd === dayKey() ? ST.cau.g || 0 : 0) : 0;
const tbSsn = f => !f.mua || (f.mua === 'nn' ? nnOn() : f.mua === muaSong());
const TBSP = [['gan', 'Gần bến'], ['giua', 'Giữa sông'], ['me', 'Mé lục bình']];
function tbChuyen(){ const B = ST.tb, d = dayKey(); if (B.cd === d && B.co) return B.co;
  let ks = Object.keys(CROPS).filter(k => !CROPS[k].tree && !CROPS[k].rare && unlocked(k) && GD(k) && GD(k).sell && (CROPS[k].kind !== 'trellis' || PLOTS.some(P => P.trellis))); ks = ks.map(k => [k, Math.random()]).sort((a, b) => a[1] - b[1]).slice(0, 3).map(x => x[0]);
  const items = ks.map(k => [k, Math.min(20, Math.max(3, Math.round(110 / GD(k).sell)))]), val = items.reduce((a, [k, q]) => a + q * GD(k).sell, 0); B.cd = d; B.co = { items, xu: Math.round(val * TB.chomul), done: 0 }; save(); return B.co; }
function tbChoGo(){ const o = tbChuyen(); if (o.done || !o.items.every(([k, q]) => has(k) >= q)) return; let n = 0; for (const [k, q] of o.items){ STORE(k)[k] -= q; n += q; } o.done = 1; ST.xu += o.xu; ST.soldN = (ST.soldN || 0) + n; gainXP(12);
  coinPop(`+${o.xu} xu · chuyến hàng chợ nổi`, '#9fd36a'); sfx('coin'); buzz(20); for (let i = 0; i < 14; i++) puff('drop', TB.at[0] + R(-.8, .8), .05, TB.at[1] + R(-.3, .3), 1, '#9cc6e0', .8); save(); hud(); renderSheet(); }
function tbGheMove(){ try { if (FM.ghe){ TBV.root.position.x = bx - 2.6; TBV.root.position.z = R0 + 1.3; } else { TBV.root.position.x = TB.at[0]; TBV.root.position.z = TB.at[1]; } for (let i = 0; i < 10; i++) puff('drop', TBV.root.position.x + R(-.6, .6), .05, TBV.root.position.z + R(-.2, .2), 1, '#9cc6e0', .7); } catch (e) {} }""")

# --- 5. sơn mũi ghe theo màu đã chọn ---
rep("CR = new T.Color('#B8402E'), CG = new T.Color('#3E7460')", "CR = new T.Color(TBP()[0]), CG = new T.Color(TBP()[1])")

# --- 1 + 2. lờ theo chỗ, cá rất hiếm, chai lời đồn ---
rep("const pool = Object.keys(FISHK).filter(k => FISHK[k].tier <= 2), wt = k =>",
    "const sp = B.sp || 'giua', pool0 = Object.keys(FISHK).filter(k => FISHK[k].tier <= 2 && tbSsn(FISHK[k])), pool1 = pool0.filter(k => FISHK[k].sp === sp), pool = pool1.length >= 3 ? pool1 : pool0, wt = k =>")
rep("B.lo = Date.now(); B.got = got; B.gotT = Date.now();",
    """{ const rr = Object.keys(FISHK).filter(k => FISHK[k].tier === 3 && FISHK[k].sp === sp && tbSsn(FISHK[k])); if (rr.length && Math.random() < TB.lohiem){ const k = pick(rr), f = FISHK[k], w = Math.round((f.w[0] + Math.pow(Math.random(), 1.8) * (f.w[1] - f.w[0])) * 100) / 100, L = ST.fishLog[k] = ST.fishLog[k] || { n: 0, max: 0 }, nw = !L.n;
    L.n++; L.max = Math.max(L.max, w); ST.inv[k] = (ST.inv[k] || 0) + 1; xp += 15; got.push([k, w, nw ? 1 : 0]); sfx('tranh'); if (nw){ ST.xu += 500; setTimeout(() => coinPop('+500 xu · con đầu tiên', '#C9A0F0'), 700); setTimeout(() => say(DONS[k] || 'Trời đất, lờ dính con cá hiếm! Ghi vô Sổ cá liền đi con.', 'vui', { now: true }), 1300); } } }   // lờ đúng chỗ + đúng mùa: 5% có cá rất hiếm
  B.chai = null; if (Math.random() < TB.chai){ try { const r = donGive(); if (r) B.chai = r.txt; } catch (e) {} }   // 30% kéo lên cái chai có lời đồn
  B.lo = Date.now(); B.got = got; B.gotT = Date.now();""")
rep("floatAt(TB.at[0], .9, TB.at[1], `Thu lờ · +${n} con cá`, '#BFE3F0');", "floatAt(TB.at[0], .9, TB.at[1], `Thu lờ · +${got.length} con cá`, '#BFE3F0');")

# --- bảng ghe: chai, chọn chỗ thả lờ, chuyến hàng, sơn ---
rep("""  const l = loLeft(), T1 = TB.lo * 3600e3 / (ST.spd || 1); h += UX.hero(UIC.tamban, l > 0 ? 'Lờ đang ngâm dưới sông' : 'Lờ có cá rồi', l > 0 ? `Còn ${fmtMin(Math.ceil(l / 60000))} ra thăm lờ` : 'Thu lờ rồi Ngoại thả lại liền', '', [1 - l / T1, '#7FB3E0']);
  return h + UX.cta([l <= 0 ? UX.btn('tbtake', 'Thu lờ', { g: 1, img: ICON.caro }) : '']); }""",
    """  if (B.chai && Date.now() - (B.gotT || 0) < 15 * 60e3) h += UX.hero(ICON.chai || UIC.task, 'Trong lờ có cái chai', B.chai);
  const l = loLeft(), T1 = TB.lo * 3600e3 / (ST.spd || 1), sp = B.sp || 'giua'; h += UX.hero(UIC.tamban, l > 0 ? 'Lờ đang ngâm dưới sông' : 'Lờ có cá rồi', l > 0 ? `Còn ${fmtMin(Math.ceil(l / 60000))} ra thăm lờ` : 'Thu lờ rồi Ngoại thả lại liền', '', [1 - l / T1, '#7FB3E0']);
  h += UX.cta([l <= 0 ? UX.btn('tbtake', 'Thu lờ', { g: 1, img: ICON.caro }) : '']);
  h += UX.title('Thả lờ ở đâu', 'lờ gom cá của chỗ đó') + UX.cta(TBSP.map(([k, t]) => UX.btn('tbsp', t, { k, g: sp === k })));
  const o = tbChuyen(), okc = o.items.every(([k, q]) => has(k) >= q);
  h += UX.title('Chuyến hàng chợ nổi', o.done ? 'hôm nay chở rồi, mai có chuyến mới' : 'mỗi ngày một chuyến') + (o.done ? '' : `<div class="tbch">${UX.chips(Object.fromEntries(o.items))}</div>` + UX.cta([UX.btn('tbcho', 'Chở đi', { g: 1, img: UIC.coin, dis: !okc, sub: `${o.xu} xu` })]));
  const own = Object.keys((cnoS().own) || {}).filter(k => CNX.P[k] && k !== 'moc');
  if (own.length) h += UX.title('Sơn mũi ghe', 'dùng màu đã mua cho xuồng') + UX.cta([UX.btn('tbson', 'Đỏ viền xanh', { k: '', g: !B.paint }), ...own.map(k => UX.btn('tbson', CNX.P[k][0], { k, g: B.paint === k }))]);
  return h; }""")
rep("else if (a === 'tbtake'){ tbTake(); return; }",
    "else if (a === 'tbtake'){ tbTake(); return; } else if (a === 'tbsp'){ ST.tb.sp = b.dataset.k; save(); sfx('pick'); renderSheet(); return; } else if (a === 'tbcho'){ tbChoGo(); return; } else if (a === 'tbson'){ ST.tb.paint = b.dataset.k || ''; TBV.st = -1; save(); sfx('pick'); renderSheet(); return; }")

# --- 3. câu trên ghe giữa sông ---
rep("""<small>${cauLeft() > 0 ? (FM.tut""", """<small>${FM.ghe ? `Ngoại chèo ghe ra giữa sông · còn ${gLeft()} lượt` : cauLeft() > 0 ? (FM.tut""")
rep("""data-f="cast" ${cauLeft() > 0 ? '' : 'disabled'}""", """data-f="cast" ${(FM.ghe ? gLeft() : cauLeft()) > 0 ? '' : 'disabled'}""")
rep("""${moiHas('sau') || FM.bait === 'sau' ? chip('sau', moiHas('sau'), 'sau') : ''}</div>`}""",
    """${moiHas('sau') || FM.bait === 'sau' ? chip('sau', moiHas('sau'), 'sau') : ''}</div>${tbReady() ? `<div class="fmois"><button class="fmoi${FM.ghe ? ' on' : ''}" data-f="ghe" ${gLeft() > 0 || FM.ghe ? '' : 'disabled'}><img src="${UIC.tamban}" alt="">Câu trên ghe <i>${gLeft()}</i></button></div>` : ''}`}""")
rep("else if (b.dataset.f === 'auto'){", "else if (b.dataset.f === 'ghe'){ FM.ghe = !FM.ghe; fshClear(); tbGheMove(); fuiAim(); sfx('pick'); } else if (b.dataset.f === 'auto'){")
rep("function fmCast(x, z){ if (cauLeft() <= 0) return say('Hôm nay câu đủ rồi, để cá nó sanh sôi. Mai ra câu tiếp nghe.', 'dan', { now: true });",
    "function fmCast(x, z){ if (FM.ghe ? gLeft() <= 0 : cauLeft() <= 0) return say(FM.ghe ? 'Hôm nay chèo ghe câu đủ rồi, mai ra tiếp nghe con.' : 'Hôm nay câu đủ rồi, để cá nó sanh sôi. Mai ra câu tiếp nghe.', 'dan', { now: true }); FM.gc = !!FM.ghe;")
rep("floatAt(FM.bob.x, .25, FM.bob.z, SPOTN[spotOf(FM.bob.x, FM.bob.z)], '#FBF7EE');", "floatAt(FM.bob.x, .25, FM.bob.z, SPOTN[FM.ghe ? 'giua' : spotOf(FM.bob.x, FM.bob.z)], '#FBF7EE');")
rep("FM.tgt = best; FM.wait = best ? 0 : R(3, 6); FM.nib = 0;",
    "FM.tgt = best; FM.wait = best ? 0 : R(3, 6); FM.nib = 0; if (FM.ghe && !FM.tut){ const a = R(0, 6.28); FM.tgt = fshSpawn(fishPick('giua'), { x: FM.bob.x + Math.cos(a) * .6, z: Math.max(FAREA.z0, Math.min(FAREA.z1, FM.bob.z + Math.sin(a) * .4)) }); FM.wait = 0; }")
rep("const sp = spotOf(FM.bob.x, FM.bob.z), rc", "const sp = FM.ghe ? 'giua' : spotOf(FM.bob.x, FM.bob.z), rc")
rep("* 100) / 100, L = ST.fishLog[k] = ST.fishLog[k] || { n: 0, max: 0 }, first", "* (FM.gc ? TB.nang : 1) * 100) / 100, L = ST.fishLog[k] = ST.fishLog[k] || { n: 0, max: 0 }, first")
rep("C2.n++; const bon", "if (FM.gc){ if (C2.gd !== dayKey()){ C2.gd = dayKey(); C2.g = 0; } C2.g++; } else C2.n++; const bon")
rep("function fmExit(){ FM.on = false;", "function fmExit(){ if (FM.ghe){ FM.ghe = false; tbGheMove(); } FM.on = false;")

rep(".ordr.vua{animation:ordin .45s ease-out}", ".ordr.vua{animation:ordin .45s ease-out}\n.tbch{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 8px}")
rep("'Đóng ghe tam bản', `Ghe lớn chở lờ ra sông · ${TB.lo} tiếng thăm lờ một lần · hay gặp loài cá mới`)", "'Đóng ghe tam bản', 'Thả lờ bắt cá, câu giữa sông, chở hàng ra chợ nổi')")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
