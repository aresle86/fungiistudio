#!/usr/bin/env python3
"""v170: ghe hoa quả Tết gom hàng + báo mùa Tết.
- Ghe hoa quả Tết (ghe chợ hoa đậu bến nhà dịp Tết) gom dưa hấu 50 xu/trái, cúc 34 xu/chậu (cao hơn Chợ 25%).
  Mỗi ngày ghe gom tối đa 10 trái dưa, 15 chậu cúc. Giao đủ cả hai trong ngày: ghe tặng 1 bao hạt lạ.
- Trên ghe có thêm dưa hấu nằm cạnh chậu cúc; bong bóng trái dưa nổi trên ghe, chạm là mở bảng giao.
- Thẻ "Mùa Tết · tới hết <ngày>" trên màn chính, chạm mở bảng Mùa Tết (mùa có gì, tới ngày nào). Không có đồng hồ đếm lùi.
- Ngoại báo một lần khi vô mùa (ghe đậu tới hết mùng 10) và một lần trước mùa 1-3 ngày.
python3 fix170.py live/v169.html live/v170.html"""
import sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf8').read()
def rep(a, b, n=1):
    global t
    c = t.count(a)
    assert c == n, (c, a[:80])
    t = t.replace(a, b)

rep("BUILD = 'v169'", "BUILD = 'v170'")

# 1. dưa hấu trên ghe chợ hoa
rep("R(-.05, .05), { cast: false }); } ROOT = pr2; } boat.visible = false;",
    "R(-.05, .05), { cast: false }); } for (const [x, z, s, c] of [[-.3, .075, 1, '#2E6B3A'], [0, -.075, 1.08, '#3C8243'], [.3, .075, .95, '#2E6B3A'], [.03, .085, .82, '#3C8243'], [-.3, -.08, .88, '#3C8243'], [.3, -.08, .9, '#2E6B3A']]){ const m = M(ico(.06, 1), c, x, .185 + .05 * s, z, { cast: false }); m.scale.set(1.28 * s, s, s); } ROOT = pr2; } boat.visible = false;")

# 2. ghe gom hàng + bảng Mùa Tết + thẻ + lời Ngoại
JS = r"""const TGHE = { duahau: { gia: 50, ngay: 10 }, cuc: { gia: 34, ngay: 15 } };   /* ghe hoa quả Tết: cao hơn Chợ 25%, mỗi ngày gom có hạn */
function tetInfo(now = new Date()){ const n = dayN(now); for (const y of [now.getFullYear(), now.getFullYear() + 1]){ const s = TETD[y]; if (!s) continue; const t0 = new Date(s + 'T00:00:00'), d = n - dayN(t0); if (d <= 9){ const e = new Date(t0); e.setDate(e.getDate() + 9); return { y, d, end: e.getDate() + '/' + (e.getMonth() + 1) }; } } return null; }
function tetSoon(){ if (ST.muaTest === 'soon') return 2; if (ST.muaTest) return 0; const I = tetInfo(); return I && I.d >= -10 && I.d <= -8 ? -7 - I.d : 0; }
function tgS(){ if (!ST.tetGhe || ST.tetGhe.d !== dayKey()) ST.tetGhe = { d: dayKey() }; return ST.tetGhe; }
const tgLeft = k => Math.max(0, TGHE[k].ngay - (tgS()[k] || 0));
const tgCan = () => ['duahau', 'cuc'].some(k => Math.min(STORE(k)[k] || 0, tgLeft(k)) > 0);
function tgHTML(){ const G2 = tgS(), I = tetInfo() || { end: '' }, R = SHEET.tg;
  let h = UX.hero(ICON.duahau, L135('Ghe gom dưa hấu với cúc', 'The boat buys watermelon and mums'), L135(`Mua cao hơn Chợ. Ghe đậu bến tới hết mùng 10 (${I.end})`, `Pays more than the market. Docked here until ${I.end}`));
  for (const k of ['duahau', 'cuc']){ const c = CROPS[k], it = TGHE[k], have = STORE(k)[k] || 0, left = tgLeft(k), n = Math.min(have, left);
    h += `<div class="srow"><div class="sic"><img src="${ICON[k]}" alt=""><span class="sq">${have}</span></div><div class="sn"><b>${fxT(c.name)}</b>${stI('coin', L135(`${it.gia} xu/${c.unit}`, `${it.gia} coins each`))}<span class="mkh">${left ? L135(`Hôm nay ghe còn gom ${left} ${c.unit}`, `The boat takes ${left} more today`) : L135('Hôm nay ghe gom đủ rồi, mai giao tiếp', 'Enough for today, more tomorrow')}</span></div><span></span><button class="btn g sall" data-a="tggive" data-k="${k}" ${n ? '' : 'disabled'}>${n ? L135(`Giao ${n}`, `Deliver ${n}`) + `<small>+${n * it.gia} xu</small>` : L135('Giao', 'Deliver')}</button></div>`; }
  if (R){ h += UX.title(L135('Ghe tặng bao hạt lạ', 'A mystery seed bag from the boat'));
    if (R.xu) h += `<div class="qset ok"><img src="${UIC.coin}" alt=""><div><b>+${R.xu} xu</b><span>${L135('Ghe gửi con chút quà Tết', 'A little Tet gift from the boat')}</span></div></div>`;
    else R.out.slice().sort((a, b) => (a.q ? 2 : a.don ? 1 : 0) - (b.q ? 2 : b.don ? 1 : 0)).forEach(o => { h += o.don ? `<div class="qset"><img src="${UIC.task}" alt=""><div><b>${L135('Lời đồn đồ quý', 'A rumour')}</b><span>${esc(fxT(o.don))}</span></div></div>` : `<div class="qset${o.q ? ' ok' : ''}"><img src="${ICON[o.k]}" alt=""><div><b>${o.n} ${L135('hạt', 'seed' + (o.n > 1 ? 's' : ''))} ${fxT(CROPS[o.k].name).toLowerCase()}</b><span>${o.q ? L135('Hạt giống quý, hiếm lắm đó', 'A rare seed') : L135('Đã bỏ vô túi hạt', 'Added to your seeds')}</span></div></div>`; }); }
  h += `<div class="note">${G2.qua ? L135('Hôm nay con giao đủ rồi, ghe đã tặng 1 bao hạt lạ. Mai ghe gom tiếp.', 'All delivered today and the boat gave you a mystery seed bag. It buys again tomorrow.') : L135(`Giao đủ ${TGHE.duahau.ngay} trái dưa hấu với ${TGHE.cuc.ngay} chậu cúc trong ngày, ghe tặng 1 bao hạt lạ. Dư thì bán ở Chợ như thường.`, `Deliver ${TGHE.duahau.ngay} watermelons and ${TGHE.cuc.ngay} mum pots in one day and the boat gives you a mystery seed bag. Sell any extra at the market.`)}</div>`;
  return h; }
function tgGive(k, b){ const it = TGHE[k]; if (!it || mua() !== 'tet' || VISIT) return; const G2 = tgS(), SRC = STORE(k), n = Math.min(SRC[k] || 0, tgLeft(k)); if (n < 1) return;
  const v = n * it.gia; SRC[k] -= n; G2[k] = (G2[k] || 0) + n; ST.xu += v; ST.soldN = (ST.soldN || 0) + n; try { coinFly(b, Math.min(6, n)); } catch (e) {} coinPop(L135(`+${v} xu · giao ${n} ${CROPS[k].unit}`, `+${v} coins · ${n} delivered`)); try { sfx('coin'); } catch (e) {}
  if (!G2.qua && !tgLeft('duahau') && !tgLeft('cuc')){ G2.qua = 1; let R = null; try { if (blPool().length) R = blRoll(); } catch (e) { R = null; } if (!R){ ST.xu += BLA.gia; R = { xu: BLA.gia }; } SHEET.tg = R; try { sfx('lvl'); buzz(40); } catch (e) {} toast(L135('Giao đủ rồi, ghe tặng con 1 bao hạt lạ', 'All delivered. The boat gives you a mystery seed bag')); }
  save(); hud(); try { bump('sell', n); } catch (e) {} ST.seen.sold = 1; }
function tetHTML(){ const I = tetInfo() || { end: '' }, row = (img, a, b2) => `<div class="qset"><img src="${img}" alt=""><div><b>${a}</b><span>${b2}</span></div></div>`;
  let h = UX.hero(ICON.lixi, L135('Tết về miệt vườn', 'Tet in the garden'), L135(`Từ 23 tháng Chạp tới hết mùng 10 (${I.end})`, `From the 23rd of the last lunar month until ${I.end}`));
  h += row(ICON.duahau, L135('Ghe hoa quả Tết', 'Tet fruit boat'), L135(`Đậu ở bến nhà. Gom dưa hấu ${TGHE.duahau.gia} xu, cúc ${TGHE.cuc.gia} xu, cao hơn Chợ`, `At your pier. Buys watermelon for ${TGHE.duahau.gia} and mums for ${TGHE.cuc.gia} coins, above market price`));
  h += row(ICON.cuc, L135('Tiệm Tết ngoài Chợ', 'Tet shop at the market'), L135('Bán hạt dưa hấu, hạt cúc với mai vàng chậu', 'Sells watermelon seeds, mum seeds and a potted apricot blossom'));
  if ((ST.lv || 1) >= ORD.lv) h += row(ICON.gio, L135('Đơn bày mâm ngũ quả', 'Five-fruit tray order'), L135('Mỗi ngày ghe chợ hoa đặt một đơn, trả cao', 'One well-paid order from the flower boat each day'));
  h += row(ICON.lixi, L135('Lì xì của Ngoại', "Grandma's lucky money"), L135('Mùng 1 tới mùng 3, vô vườn là Ngoại lì xì', 'On the first three days of the new year'));
  h += `<div class="acts">${UX.btn('tgopen', L135('Ra ghe hoa quả', 'Go to the boat'), { g: 1 })}${UX.btn('tetcho', L135('Ghé Tiệm Tết', 'Visit the Tet shop'))}</div>`;
  h += `<div class="note">${L135('Hết mùng 10 ghe rời bến. Dưa hấu với cúc còn trong kho vẫn bán ở Chợ như thường.', 'After the 10th the boat leaves. Watermelon and mums left in storage still sell at the market.')}</div>`; return h; }
function tetChipUp(){ const c = document.getElementById('tetChip'); if (!c) return; const on = mua() === 'tet' && !VISIT; c.hidden = !on; document.body.classList.toggle('teton', on); if (!on) return; const I = tetInfo() || { end: '' }; document.getElementById('tetChipI').src = ICON.lixi; c.querySelector('b').textContent = L135('Mùa Tết', 'Tet season'); document.getElementById('tetChipD').textContent = L135('tới hết ' + I.end, 'until ' + I.end); c.setAttribute('aria-label', L135('Mùa Tết, tới hết ' + I.end, 'Tet season, until ' + I.end)); }
"""
rep("function seasonTick(t){ const on = mua() === 'tet' && !VISIT;", JS + "function seasonTick(t){ const on = mua() === 'tet' && !VISIT; try { tgTick(t, on); } catch (e) {}")
rep("  if (!on || (SEAST++ % 90)) return; const d = tetDay(), y = new Date().getFullYear(), key = d < 3 ? `tet${y}_${d}` : `tet${y}_ra`; const line = TETLINES[String(Math.min(3, d))];\n  if (line && !ST.seen[key] && document.getElementById('intro').hidden && ST.player){ ST.seen[key] = 1; save(); say(line, 'vui', { idle: true }); }",
    "  if (SEAST++ % 90) return; try { tetChipUp(); } catch (e) {} const okSay = !VISIT && document.getElementById('intro').hidden && ST.player, TI = tetInfo(), ty = ST.muaTest ? 'thu' : TI ? TI.y : 0;\n"
    "  if (!on){ if (okSay && tetSoon() && !ST.seen[`tet${ty}_sap`]){ ST.seen[`tet${ty}_sap`] = 1; save(); say(L135('Sắp tới hai mươi ba tháng Chạp rồi con. Ít bữa nữa ghe hoa quả Tết ghé bến, Tiệm Tết ngoài chợ cũng mở bán hạt dưa hấu với hạt cúc.', 'The 23rd of the last lunar month is near. In a few days the Tet fruit boat will dock, and the Tet shop at the market opens with watermelon and mum seeds.'), 'vui', { idle: true }); } return; }\n"
    "  const d = tetDay(), y = new Date().getFullYear(), key = d < 3 ? `tet${y}_${d}` : `tet${y}_ra`; const line = TETLINES[String(Math.min(3, d))];\n"
    "  if (okSay && !ST.seen[`tet${ty}_bao`]){ ST.seen[`tet${ty}_bao`] = 1; save(); say(L135('Tết tới rồi con. Ghe hoa quả đậu bến mình tới hết mùng 10, có dưa hấu với cúc thì đem giao, ghe mua cao hơn chợ.', 'Tet is here. The fruit boat stays at our pier until the 10th day of the new year. Bring it watermelon and mums, it pays more than the market.'), 'vui', { idle: true }); }\n"
    "  else if (line && !ST.seen[key] && okSay){ ST.seen[key] = 1; save(); say(line, 'vui', { idle: true }); }")

# 3. bong bóng trái dưa trên ghe
# thẻ "Về vườn ngày n/7" không đè nút đóng của Sổ: mở Sổ là cất thẻ (bảng thường đã làm vậy)
rep("closeSheet(); if (TOOL) clearTool(); fan.hidden = true; PEND = null; hideTip(); BOOK = { tab, sel:",
    "closeSheet(); try { const dd = document.querySelector('.ddt.on'); if (dd) dd.classList.remove('on'); } catch (e) {} if (TOOL) clearTool(); fan.hidden = true; PEND = null; hideTip(); BOOK = { tab, sel:")
rep("const XOM = { lv: 5, who:",
    "const TGV = (() => { const b = bubbleK('h'); b.visible = false; return { b, hit: b.children.find(c => c.userData.bub) }; })();\n"
    "function tgTick(t, on){ TGV.b.visible = on; if (!on) return; try { bubIcon(TGV.b, ICON.duahau); } catch (e) {} TGV.b.quaternion.copy(cam.quaternion); TGV.b.position.set(BOAT.position.x + (ORDV.b.visible ? .62 : 0), .95 + Math.sin(t * 2 + 1.3) * .035, BOAT.position.z); TGV.b.scale.setScalar(.85 * BUBS * (1 + (tgCan() ? .08 : .03) * Math.abs(Math.sin(t * 3 + .8)))); }\n"
    "function tgHitAt(cx, cy){ if (!TGV.b.visible) return false; ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); return ray.intersectObjects([TGV.hit], false).length > 0; }\n"
    "const XOM = { lv: 5, who:")
rep("{ const oh = ordHitAt(OX, OY); if (oh === 'bub'){", "{ if (tgHitAt(OX, OY)){ openSheet('tetghe'); return; } const oh = ordHitAt(OX, OY); if (oh === 'bub'){")

# 4. bảng
rep("  if (kind === 'baola'){ shT.textContent = L135('Sạp cô Út', \"Auntie Ut's stall\"); h += blHTML(); }",
    "  if (kind === 'baola'){ shT.textContent = L135('Sạp cô Út', \"Auntie Ut's stall\"); h += blHTML(); }\n"
    "  if (kind === 'tetghe'){ shT.textContent = L135('Ghe hoa quả Tết', 'Tet fruit boat'); h += tgHTML(); }\n"
    "  if (kind === 'tet'){ shT.textContent = L135('Mùa Tết', 'Tet season'); h += tetHTML(); }")
rep("else if (a === 'tetbuy'){ tetBuy(b.dataset.k); }",
    "else if (a === 'tetbuy'){ tetBuy(b.dataset.k); } else if (a === 'tggive'){ tgGive(b.dataset.k, b); } else if (a === 'tgopen'){ openSheet('tetghe'); return; } else if (a === 'tetcho'){ openSheet('cho'); SHEET.tab = 'mua'; renderSheet(); return; }")

# 5. thẻ Mùa Tết trên màn chính
rep('<div class="t" id="tt">06:00</div><div class="n" id="tn">Bình minh</div></div></button>\n',
    '<div class="t" id="tt">06:00</div><div class="n" id="tn">Bình minh</div></div></button>\n'
    '  <button class="tetchip" id="tetChip" hidden aria-label="Mùa Tết"><img id="tetChipI" alt=""><span><b>Mùa Tết</b><small id="tetChipD"></small></span></button>\n')
rep("$('#clock').addEventListener('click', () => openSheet('set'));",
    "$('#clock').addEventListener('click', () => openSheet('set')); $('#tetChip').addEventListener('click', () => openSheet('tet'));")
i = t.index('</style>'); t = t[:i] + (
    ".tetchip{appearance:none;border:0;margin-top:4px;cursor:pointer;pointer-events:auto;display:flex;align-items:center;gap:8px;min-height:44px;padding:4px 12px 4px 8px;border-radius:16px;background:linear-gradient(#D8362E,#B3211F);box-shadow:0 4px 0 #6E1512,0 8px 12px rgba(43,52,70,.2);color:#FFF3C4;font-family:var(--f-game);text-align:left}\n"
    ".tetchip[hidden]{display:none}.tetchip img{width:32px;height:32px;flex:none}.tetchip b{display:block;font-weight:400;font-size:15px;line-height:1.15}.tetchip small{display:block;font:600 12px var(--f-body);line-height:1.2;color:#FFE9A8;white-space:nowrap}\n"
    ".tetchip:focus-visible{outline:3px solid var(--sun);outline-offset:2px}\n"
    "@media (max-width:560px){.tetchip{position:absolute;left:16px;top:calc(100px + env(safe-area-inset-top,0px));margin-top:0}body.teton .nxq{top:calc(172px + env(safe-area-inset-top,0px))}}\n") + t[i:]

open(dst, 'w', encoding='utf8').write(t)
print('ok', len(t))
