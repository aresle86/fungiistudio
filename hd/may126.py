# may126: tiệm may cô Ba (bước 3). Chạy sau ch125.py.
# - Ở chợ huyện chạm tiệm may mở bảng "Tiệm may cô Ba". Lần đầu đo ni; lần đầu may cho Ngoại cô Ba nói số đo bà cô còn giữ.
# - Chọn: may cho ai (tên người chơi / Ngoại) · món (bà ba ôm eo, bà ba suông, quần, khăn rằn; Ngoại: bà ba, khăn rằn)
#   · vải (bông, xi-ta; cấp 23 thêm lụa, lãnh Mỹ A chỉ màu đen) · màu · hoa văn. Hình xem trước, giá, thời gian may.
# - Đặt may: cọc nửa tiền, cô Ba may một món một lúc (ST.may.q). Xong lên lấy, trả nốt. Đồ của mình vô tủ (ST.tu.it) và mặc liền;
#   đồ của Ngoại (ST.ng.it) Ngoại mặc liền, về vườn Ngoại nói. Nón tai bèo, mũ phớt bán sẵn, mua là có.
# - Tủ đồ thêm ngăn "Ngoại mặc". Hình Ngoại dựng lại theo đồ: Object.assign(NGOAI, NGOAIB(ngOF())).
# Giá theo bảng anh Ares duyệt: khăn 600, bà ba bông 1.500, xi-ta 2.500, lụa 5.000, lãnh 12.000; quần 60% giá áo cùng vải.
import sys, json
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a))
    s = s.replace(a, b)

# Ngoại: dựng nhanh một hình để xem trước (OF.one)
rep("for (const e of ['lo', 'dan']) shot(", "if (!OF.one) for (const e of ['lo', 'dan']) shot(")
rep("shot('ex_bat', g =>", "if (!OF.one) shot('ex_bat', g =>")
rep("shot('ex_nhay', g =>", "if (!OF.one) shot('ex_nhay', g =>")

TM = r"""/* ---------- tiệm may cô Ba ---------- */
const TMV = { bong: ['vải bông', 1500, 4, 21], xita: ['xi-ta', 2500, 6, 21], lua: ['lụa', 5000, 10, 23], lanh: ['lãnh Mỹ A', 12000, 12, 23] };   /* tên, giá áo, giờ may, cấp mở */
const TMC = { bong: [['#E8B4C0', 'hồng'], ['#3E7FC4', 'xanh dương'], ['#5E8A4A', 'xanh lá'], ['#E8C25A', 'vàng'], ['#B5553A', 'đỏ gạch'], ['#7A4A6A', 'tím'], ['#EFE6D2', 'ngà'], ['#2B2522', 'đen']],
  lua: [['#F2E6C8', 'ngà'], ['#B8C8D8', 'xanh nhạt'], ['#E8C8D0', 'hồng phấn'], ['#9CC4BA', 'xanh ngọc'], ['#D8C090', 'vàng nhạt'], ['#7A3A4A', 'đỏ rượu']], lanh: [['#1A181E', 'đen']],
  quan: [['#22201E', 'đen'], ['#4A3326', 'nâu'], ['#26304A', 'xanh đậm'], ['#EFE6D2', 'trắng']], khan: [['#2B2522', 'đen'], ['#B5302A', 'đỏ'], ['#3E5E8A', 'xanh'], ['#6B4529', 'nâu']] };
TMC.xita = TMC.bong;
const TMK = { me: [['om', 'Bà ba ôm eo'], ['suong', 'Bà ba suông'], ['quan', 'Quần'], ['khan', 'Khăn rằn'], ['non', 'Nón']], ng: [['ao', 'Bà ba'], ['khan', 'Khăn rằn']] };
const TMN = [['taibeo', 'Nón tai bèo', 300, '#6E7A4A'], ['phot', 'Mũ phớt', 800, '#5A4030']];
const TMP = { tron: 'trơn', bongnhi: 'bông nhí', soc: 'sọc' };
function tmS(){ ST.may = ST.may || { q: [], ni: 0, ngni: 0, n: 0 }; return ST.may; }
function ngS(){ ST.ng = ST.ng || { w: {}, it: {} }; return ST.ng; }
function ngOF(){ const N = ngS(), of = {}; for (const id of Object.values(N.w)) if (N.it[id]) Object.assign(of, N.it[id].o); return of; }
let NGOK = 0; function ngApply(){ try { Object.assign(NGOAI, NGOAIB(ngOF())); $('#ngoaiImg').src = NGOAI.ex_vui; } catch (e) { console.warn('ng', e); } }
function tmCfg(){ const c = SHEET.tm = SHEET.tm || { who: 'me', k: 'om', fab: 'bong', col: 0, pat: 'tron' }; const lv = ST.lv || 1; if (!TMK[c.who].some(x => x[0] === c.k)) c.k = TMK[c.who][0][0]; if ((TMV[c.fab] || [])[3] > lv) c.fab = 'bong';
  const pal = c.k === 'quan' ? TMC.quan : c.k === 'khan' ? TMC.khan : TMC[c.fab]; if (c.col >= pal.length) c.col = 0; if (c.fab !== 'bong' && c.pat === 'bongnhi') c.pat = 'tron'; if (c.fab !== 'xita' && c.pat === 'soc') c.pat = 'tron'; if (c.fab === 'lanh' || c.k === 'khan' || c.k === 'quan') c.pat = 'tron'; return c; }
function tmItem(c){ const pal = c.k === 'quan' ? TMC.quan : c.k === 'khan' ? TMC.khan : TMC[c.fab], [col, cn] = pal[c.col], V = TMV[c.fab];
  if (c.k === 'khan') return { k: 'khan', name: `Khăn rằn ${cn}`, o: c.who === 'ng' ? { khan: [col, '#FBF7EE'] } : { khan: [col, '#F2EEE4'] }, price: 600, h: 2 };
  if (c.k === 'quan') return { k: 'quan', name: `Quần ${V[0] === 'vải bông' ? '' : V[0] + ' '}${cn}`.replace('  ', ' '), o: c.fab === 'lanh' ? { pants: '#1A181E', pfab: 'lanh' } : { pants: col, pfab: c.fab }, price: Math.round(V[1] * .6), h: Math.max(2, Math.round(V[2] * .7)) };
  const kn = c.who === 'ng' ? 'Bà ba' : c.k === 'om' ? 'Bà ba ôm' : 'Bà ba suông', pn = c.pat !== 'tron' ? ' ' + TMP[c.pat] : '';
  const o = c.who === 'ng' ? { ao: col, fab: c.fab, pat: c.pat } : { shirt: col, fab: c.fab, pat: c.pat, cut: c.k, tay: 'dai', open: false };
  return { k: 'ao', name: `${kn} ${V[0] === 'vải bông' ? '' : V[0] + ' '}${cn}${pn}`.replace('  ', ' '), o, price: V[1], h: V[2] }; }
const TMPV = { key: '', url: '' };
function tmPrev(c, it){ const key = JSON.stringify([c.who, it.o]); if (TMPV.key === key) return TMPV.url; TMPV.key = key;
  if (c.who === 'ng'){ const of = { ...ngOF(), one: 1 }; if (it.k === 'ao'){ delete of.ao; delete of.fab; delete of.pat; } Object.assign(of, it.o); TMPV.url = NGOAIB(of).ex_vui; }
  else { const a = avOf(ST.player.av); if (it.k === 'ao'){ delete a.prop; } Object.assign(a, it.o); if (a.hat && a.prop === 'non') a.prop = null; TMPV.url = avShot(a, 'full'); } return TMPV.url; }
function tmChip(f, v, label, on, dis){ return `<button class="tmc${on ? ' on' : ''}" data-a="tmset" data-k="${f}" data-i="${v}"${dis ? ' disabled' : ''}>${esc(label)}</button>`; }
function tiemHTML(){ const M2 = tmS(), lv = ST.lv || 1, nm = ST.player.name, q = M2.q[0]; let h = TMSAY ? `<div class="tmsay"><b>${fxT('Cô Ba')}</b>${esc(fxT(TMSAY))}</div>` : '';
  if (q){ const left = q.t0 + q.dur - Date.now(), it = q.it; const im = q.who === 'ng' ? NGOAIB({ ...ngOF(), one: 1, ...it.o }).ex_vui : (() => { const a = avOf(ST.player.av); if (it.k === 'ao') delete a.prop; Object.assign(a, it.o); if (a.hat && a.prop === 'non') a.prop = null; return avShot(a, 'full'); })();
    if (left > 0) return h + `<div class="tmpv"><img src="${im}" alt=""><div><b>Cô Ba đang may</b><span>${esc(it.name)}${q.who === 'ng' ? ' cho Ngoại' : ''}</span><span class="tmbar"><i style="width:${Math.round(c01(1 - left / q.dur) * 100)}%"></i></span><span>Còn ${fmtT(left / 1000)}. Đồ may xong cô giữ hoài, rảnh thì lên lấy.</span></div></div>`;
    const rest = it.price - q.paid; return h + `<div class="tmpv"><img src="${im}" alt=""><div><b>May xong rồi!</b><span>${esc(it.name)}${q.who === 'ng' ? ' cho Ngoại' : ''}</span><button class="btn g" data-a="tmtake">Lấy đồ · trả nốt ${rest.toLocaleString('vi-VN')} xu</button></div></div>`; }
  if (!M2.ni) return h + `<div class="tmpv"><img src="${UIC.task}" alt=""><div><b>Đo ni</b><span>Lần đầu may, cô Ba đo vai, eo, dài tay rồi ghi vô sổ. Lần sau khỏi đo lại.</span><button class="btn g" data-a="tmni">Đứng cho cô Ba đo</button></div></div>`;
  const c = tmCfg(), it = tmItem(c);
  h += `<div class="sub">May cho</div><div class="tmrow">${tmChip('who', 'me', nm, c.who === 'me')}${tmChip('who', 'ng', 'Ngoại', c.who === 'ng')}</div>`;
  h += `<div class="sub">Món</div><div class="tmrow">${TMK[c.who].map(([k, n]) => tmChip('k', k, n, c.k === k)).join('')}</div>`;
  if (c.k === 'non') return h + `<div class="tmrow tmnon">${TMN.map(([k, n, p, col]) => { const has = ST.tu && ST.tu.it && ST.tu.it['non_' + k]; return `<button class="tmn" data-a="tmbuy" data-k="${k}"${has ? ' disabled' : ''}><span class="sw" style="background:${col}"></span><b>${n}</b><span>${has ? 'Có rồi' : p.toLocaleString('vi-VN') + ' xu · mua liền'}</span></button>`; }).join('')}</div>`;
  if (c.k !== 'khan') h += `<div class="sub">Vải</div><div class="tmrow">${Object.entries(TMV).map(([k, v]) => tmChip('fab', k, v[3] > lv ? `${v[0]} · cấp ${v[3]}` : v[0], c.fab === k, v[3] > lv)).join('')}</div>`;
  const pal = c.k === 'quan' ? TMC.quan : c.k === 'khan' ? TMC.khan : TMC[c.fab];
  h += `<div class="sub">Màu</div><div class="tmrow">${pal.map(([col, n], i) => `<button class="tmsw${c.col === i ? ' on' : ''}" data-a="tmset" data-k="col" data-i="${i}" aria-label="${n}" style="background:${c.k === 'khan' ? `repeating-conic-gradient(${col} 0 25%,#F2EEE4 0 50%) 0 0/12px 12px` : col}"></button>`).join('')}</div>`;
  if (c.k !== 'khan' && c.k !== 'quan' && (c.fab === 'bong' || c.fab === 'xita')) h += `<div class="sub">Hoa văn</div><div class="tmrow">${tmChip('pat', 'tron', 'Trơn', c.pat === 'tron')}${c.fab === 'bong' ? tmChip('pat', 'bongnhi', 'Bông nhí', c.pat === 'bongnhi') : tmChip('pat', 'soc', 'Sọc', c.pat === 'soc')}</div>`;
  const coc = Math.ceil(it.price / 2);
  h += `<div class="tmpv"><img src="${tmPrev(c, it)}" alt=""><div><b>${esc(it.name)}</b><span>${it.price.toLocaleString('vi-VN')} xu · may chừng ${it.h} tiếng</span><button class="btn g" data-a="tmorder"${ST.xu < coc ? ' disabled' : ''}>Đặt may · cọc ${coc.toLocaleString('vi-VN')} xu</button>${ST.xu < coc ? '<span>Chưa đủ xu đặt cọc.</span>' : ''}</div></div>`;
  return h; }
let TMSAY = ''; function tmSay(t){ TMSAY = t; try { chSay(t); } catch (e) {} if (SHEET && SHEET.kind === 'tiemmay') renderSheet(); }
function tmNi(){ const M2 = tmS(); M2.ni = 1; save(); sfx('pick'); tmSay(`${ST.player.name} đứng thẳng lên cô đo… vai, eo, dài tay. Rồi, cô ghi vô sổ. Giờ chọn món đi con.`); }
function tmOrder(){ const M2 = tmS(); if (M2.q.length) return; const c = tmCfg(), it = tmItem(c), coc = Math.ceil(it.price / 2); if (ST.xu < coc) return; if (c.who === 'ng' && !M2.ngni){ M2.ngni = 1; setTimeout(() => tmSay('Ngoại con thì cô may cho bà hoài, số đo cô còn giữ nè.'), 300); }
  ST.xu -= coc; M2.q.push({ who: c.who, it: { ...it }, t0: Date.now(), dur: it.h * 3600e3, paid: coc }); M2.n++; save(); hud(); sfx('coin'); tmSay(`Cô nhận rồi nghe. Chừng ${it.h} tiếng nữa xong, đồ may xong cô giữ hoài, rảnh thì lên lấy.`); }
function tmTake(){ const M2 = tmS(), q = M2.q[0]; if (!q || q.t0 + q.dur > Date.now()) return; const rest = q.it.price - q.paid; if (ST.xu < rest){ toast(`Còn thiếu ${(rest - ST.xu).toLocaleString('vi-VN')} xu, con bán bớt rồi lên lấy nghe.`, 'dan'); return; }
  ST.xu -= rest; M2.q.shift(); const id = 'm' + Date.now().toString(36);
  if (q.who === 'ng'){ const N = ngS(); N.it[id] = { k: q.it.k, name: q.it.name, o: q.it.o }; N.w[q.it.k] = id; N.gift = 1; ngApply(); tmSay('Đem về cho Ngoại mặc thử, thế nào bà cũng mừng.'); }
  else { ST.tu = ST.tu || {}; ST.tu.it = ST.tu.it || {}; ST.tu.it[id] = { k: q.it.k, name: q.it.name, o: q.it.o }; tuWear(q.it.k, id); tmSay(`${ST.player.name} mặc vô coi, vừa khít chưa! Cô may là phải đẹp.`); }
  save(); hud(); sfx('up'); try { confetti($('#avb')); } catch (e) {} }
function tmBuy(k){ const n = TMN.find(x => x[0] === k); if (!n) return; ST.tu = ST.tu || {}; ST.tu.it = ST.tu.it || {}; if (ST.tu.it['non_' + k]) return; if (ST.xu < n[2]){ toast('Chưa đủ xu mua nón.', 'dan'); return; } ST.xu -= n[2]; ST.tu.it['non_' + k] = { k: 'non', name: n[1], o: { hat: k } }; tuWear('non', 'non_' + k); save(); hud(); sfx('coin'); tmSay(`Đội thử coi, ${n[1].toLowerCase()} hợp với con ghê.`); }
function tuNgHTML(){ const N = ngS(), ids = Object.keys(N.it); if (!ids.length) return ''; const cur = k => N.w[k] || 'base'; let h = `<div class="sub">Ngoại mặc</div><div class="tugrid">`; const b = (k, id, name, sw) => `<button class="tui${cur(k) === id ? ' on' : ''}" data-a="ngwear" data-k="${k}" data-i="${id}"><span class="sw" style="${sw}"></span><b>${esc(name)}</b></button>`;
  h += b('ao', 'base', 'Bà ba nâu của Ngoại', 'background:#8A5D3B'); for (const id of ids.filter(i => N.it[i].k === 'ao')){ const o = N.it[id].o; h += b('ao', id, N.it[id].name, o.fab === 'lanh' ? 'background:linear-gradient(135deg,#1A181E 40%,#5A5868 50%,#1A181E 60%)' : `background:${o.ao}`); }
  if (ids.some(i => N.it[i].k === 'khan')){ h += b('khan', 'base', 'Khăn rằn cũ', 'background:repeating-conic-gradient(#2B3446 0 25%,#FBF7EE 0 50%) 0 0/14px 14px'); for (const id of ids.filter(i => N.it[i].k === 'khan')) h += b('khan', id, N.it[id].name, `background:repeating-conic-gradient(${N.it[id].o.khan[0]} 0 25%,#FBF7EE 0 50%) 0 0/14px 14px`); }
  return h + '</div>'; }
function ngWear(k, id){ const N = ngS(); if (id === 'base') delete N.w[k]; else if (N.it[id]) N.w[k] = id; save(); ngApply(); sfx('pick'); }
"""
# chèn sau phần chợ huyện (cần chSay, avOf, avShot)
rep("/* avatar đứng trong vườn, trước bậc thềm */\nawait LDY(0);\nlet AVW = null;", TM + "/* avatar đứng trong vườn, trước bậc thềm */\nawait LDY(0);\nlet AVW = null;")
rep("function chShop(){", "function chShop(){ $('#chSay').hidden = true; TMSAY = `${(ST.player && ST.player.name) || 'Con'} đó hả? Lớn dữ vậy! Vô đây cô coi, vải mới về đủ màu.`; openSheet('tiemmay'); return;")
rep("  if (kind === 'tudo'){ shT.textContent = 'Tủ đồ'; shB.innerHTML = tudoHTML(); return; }",
    "  if (kind === 'tudo'){ shT.textContent = 'Tủ đồ'; shB.innerHTML = tudoHTML(); return; }\n  if (kind === 'tiemmay'){ shT.textContent = 'Tiệm may cô Ba'; shB.innerHTML = tiemHTML(); return; }")
rep("if (a === 'chgo'){ chEnter(); return; }",
    "if (a === 'chgo'){ chEnter(); return; } if (a === 'tmset'){ const c = tmCfg(), k = b.dataset.k, v = b.dataset.i; c[k] = k === 'col' ? +v : v; if (k !== 'col') c.col = k === 'fab' && v === 'lanh' ? 0 : c.col; renderSheet(); return; } if (a === 'tmni'){ tmNi(); renderSheet(); return; } if (a === 'tmorder'){ tmOrder(); renderSheet(); return; } if (a === 'tmtake'){ tmTake(); renderSheet(); return; } if (a === 'tmbuy'){ tmBuy(b.dataset.k); renderSheet(); return; } if (a === 'ngwear'){ ngWear(b.dataset.k, b.dataset.i); renderSheet(); return; }")
# tủ đồ: ngăn Ngoại mặc
rep("  h += `<div class=\"acts\"><button class=\"btn\" data-a=\"avatar\">Đổi dáng, tên vườn</button></div>`;", "  h += tuNgHTML();\n  h += `<div class=\"acts\"><button class=\"btn\" data-a=\"avatar\">Đổi dáng, tên vườn</button></div>`;")
# áp đồ Ngoại khi mở game; Ngoại nói khi về vườn với đồ mới
rep("function avHud(){ try { nxq(); } catch (e) {}", "function avHud(){ try { nxq(); } catch (e) {} if (!NGOK && ST.ng && ST.ng.w && Object.keys(ST.ng.w).length){ NGOK = 1; ngApply(); }")
rep("CHM.on = false; ctl.enabled = true;", "CHM.on = false; ctl.enabled = true; if (ST.ng && ST.ng.gift){ ST.ng.gift = 0; save(); setTimeout(() => say('Trời đất, may chi cho Ngoại tốn tiền vậy con. Mà đẹp thiệt, mai Ngoại mặc đi chùa.', 'vui', { now: true }), 1100); }")
rep("button,[data-a],.btn{touch-action:manipulation}",
    "button,[data-a],.btn{touch-action:manipulation} body.sheeton #chUi{display:none} .tmsay{background:#FFF8EA;border-radius:14px;padding:8px 12px 9px;margin:0 0 6px;box-shadow:0 2px 0 #E3D3BC;font-size:14.5px;line-height:1.35;color:var(--ink)} .tmsay b{display:block;font-family:var(--f-game);font-size:14px;color:#B02A1A} .tmrow{display:flex;flex-wrap:wrap;gap:6px;margin-top:4px} .tmc{appearance:none;border:0;background:#FBF7EE;border-radius:999px;padding:7px 12px;font:inherit;font-size:14px;font-weight:700;color:var(--ink);box-shadow:0 2px 0 #E3D3BC;min-height:36px} .tmc.on{background:#86B06A;color:#fff;box-shadow:0 2px 0 #6E9A54} .tmc:disabled{opacity:.5} .tmsw{appearance:none;border:0;width:34px;height:34px;border-radius:50%;box-shadow:inset 0 0 0 2px rgba(0,0,0,.12)} .tmsw.on{box-shadow:0 0 0 3px #FFF8EA,0 0 0 5px #86B06A} .tmpv{display:flex;gap:12px;align-items:center;background:#FBF7EE;border-radius:16px;padding:10px;margin-top:12px;box-shadow:0 3px 0 #E3D3BC} .tmpv img{width:96px;height:122px;object-fit:contain;flex:none} .tmpv > div{display:flex;flex-direction:column;gap:6px;flex:1} .tmpv b{font-family:var(--f-game);font-size:17px;color:var(--ink)} .tmpv span{font-size:13.5px;color:#6B4529} .tmbar{height:8px;border-radius:4px;background:#E8DCC4;overflow:hidden;display:block} .tmbar i{display:block;height:100%;background:#E9B23A} .tmn{appearance:none;border:0;background:#FBF7EE;border-radius:14px;padding:8px 10px;display:flex;flex-direction:column;align-items:center;gap:4px;font:inherit;color:var(--ink);box-shadow:0 3px 0 #E3D3BC;min-width:120px} .tmn b{font-size:14px} .tmn span:last-child{font-size:12.5px;color:#6B4529} .tmn .sw{width:30px;height:30px;border-radius:50%} .tmn:disabled{opacity:.6}")
EN = {'Tiệm may cô Ba': "Ms Ba's tailor shop", 'May cho': 'Sew for', 'Món': 'Item', 'Vải': 'Fabric', 'Màu': 'Colour', 'Hoa văn': 'Pattern', 'Ngoại': 'Grandma', 'Bà ba ôm eo': 'Fitted bà ba', 'Bà ba suông': 'Loose bà ba', 'Bà ba': 'Bà ba', 'Trơn': 'Plain', 'Bông nhí': 'Small flowers', 'Sọc': 'Stripes', 'Đo ni': 'Measuring',
  'Lần đầu may, cô Ba đo vai, eo, dài tay rồi ghi vô sổ. Lần sau khỏi đo lại.': 'For a first order Ms Ba measures shoulders, waist and sleeves and writes them in her book. No need next time.', 'Đứng cho cô Ba đo': 'Stand still for Ms Ba', 'Cô Ba đang may': 'Ms Ba is sewing', 'May xong rồi!': 'All sewn!', 'Chưa đủ xu đặt cọc.': 'Not enough coins for the deposit.', 'Ngoại mặc': 'Grandma wears', 'Bà ba nâu của Ngoại': "Grandma's brown bà ba", 'Khăn rằn cũ': 'Old checked scarf', 'Nón tai bèo': 'Bucket hat', 'Mũ phớt': 'Fedora', 'Có rồi': 'Owned',
  'Ngoại con thì cô may cho bà hoài, số đo cô còn giữ nè.': "I've sewn for your grandma for years, I still have her measurements.", 'Đem về cho Ngoại mặc thử, thế nào bà cũng mừng.': "Take it home for Grandma to try, she'll be so pleased.", 'Trời đất, may chi cho Ngoại tốn tiền vậy con. Mà đẹp thiệt, mai Ngoại mặc đi chùa.': "Oh my, why spend money on Grandma, dear? But it's lovely. I'll wear it to the pagoda tomorrow.", 'Chưa đủ xu mua nón.': 'Not enough coins for the hat.'}
rep('["^còn (\\\\d+) (.+) nữa thì hạ giá$", "price drops after $1 more"]', '["^còn (\\\\d+) (.+) nữa thì hạ giá$", "price drops after $1 more"], ["^(.+) đó hả\\\\? Lớn dữ vậy! Vô đây cô coi, vải mới về đủ màu\\\\.$", "$1, is that you? Look how you\'ve grown! Come in, the new fabric came in every colour."], ["^(.+) đứng thẳng lên cô đo… vai, eo, dài tay\\\\. Rồi, cô ghi vô sổ\\\\. Giờ chọn món đi con\\\\.$", "$1, stand up straight… shoulders, waist, sleeves. There, it\'s in my book. Now pick something, dear."], ["^(.+) mặc vô coi, vừa khít chưa! Cô may là phải đẹp\\\\.$", "$1, put it on, a perfect fit! My sewing is always lovely."]')
rep('"Bán hết": "Sell all", ', '"Bán hết": "Sell all", ' + ''.join(json.dumps(k, ensure_ascii=False) + ': ' + json.dumps(v, ensure_ascii=False) + ', ' for k, v in EN.items()))
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
