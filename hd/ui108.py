# v108 đợt 1 — áp hệ thống giao diện (hd/hud-hethong.md) vào game, anh Ares duyệt mock 4/11:
#  1. CSS hệ thống cho mọi bảng: dải tiêu đề cùng màu viền gỗ; thẻ trạng thái (.uxh) giấy sẫm viền giấy; ô số (.uxc) trắng viền mực
#     bóng 3px, icon + số to + nhãn dưới; thanh (.mbar / .bar) rãnh nâu ruột vàng, bo theo chỗ đặt; nút 4 loại (chính xanh, phụ giấy,
#     thưởng vàng, đóng đỏ), viền 2px bóng 3px, không inset; chữ tối không bóng.
#  2. UX.hero có thanh thời gian thay vòng tròn; UX.card nhận icon.
#  3. Chuồng gà: ba ô số một hàng (máng, ổ, đàn), "Trứng kế [thanh] 2g58".
#  4. Thẻ Ngoại nhờ: 3 ô (việc theo cấp có nhãn CẤP + chấm bước; 2 việc hôm nay; ô xong vàng "Nhận"; "+N" còn lại), chạm từng ô.
#  5. Khay trái: số hạt/rơm là badge đỏ góc trên phải; hết thì icon mờ, nhãn vàng "+ N xu" / "Mua hạt".
# Dùng: python3 ui108.py live/vuon3d.html live/v108a.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:70], c, n); s = s.replace(a, b)

CSS = r'''<style id="s108">
/* ===== v108 hệ thống giao diện (hd/hud-hethong.md) ===== */
.sheet{background:linear-gradient(var(--vg) 0 34px,var(--dz) 34px)!important}
.sheet .shH{background:var(--vg)!important}
#shB{text-shadow:none}
/* thẻ trạng thái */
.uxh{background:#F6EBD3!important;box-shadow:none!important;border:2px solid #E3C9A6;border-radius:16px;padding:10px}
.uxh.go{background:#E8F3DA!important;border-color:#B9DB9A}
.uxh.warn{background:#FCE6D8!important;border-color:#F2B79C}
.uxh .hi{width:60px;height:60px;background:#fff;border:2px solid var(--vgK);border-radius:10px;box-sizing:border-box}
.uxh .hi img{width:46px;height:46px}
.uxh .tx>b{text-shadow:none}
.uxh .tx>span.hb{display:flex;align-items:center;gap:8px;font-size:13px}
.uxh .tx>span.hb>b{font-family:var(--f-game);font-weight:400;font-size:14px;color:var(--vgK);white-space:nowrap}
.uxh .tx .bar{margin-top:6px}
.uxh .tx>span.hb .bar{flex:1;margin-top:0}
/* thanh: rãnh nâu, viền mực, ruột vàng; bo theo chỗ đặt */
.bar{display:block;height:14px;border-radius:6px;background:#6B4529;border:2px solid var(--vgK);position:relative;overflow:hidden;box-sizing:border-box}
.bar i{position:absolute;left:0;top:0;bottom:0;background:var(--rom);border-radius:4px}
.bar em{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:400 10px/1 var(--f-game);font-style:normal;color:#fff;text-shadow:1px 1px 0 var(--vgK),-1px 1px 0 var(--vgK),1px -1px 0 var(--vgK),-1px -1px 0 var(--vgK)}
.mbar{height:10px!important;border-radius:4px!important;background:#6B4529!important;border:2px solid var(--vgK);box-sizing:border-box;width:100%;margin-top:4px!important}
.mbar i{border-radius:2px!important}
/* ô số */
.uxc{background:#fff!important;border:2px solid var(--vgK);border-radius:10px!important;box-shadow:0 3px 0 var(--vgK)!important;padding:8px 6px 7px!important;display:flex;flex-direction:column;align-items:center;text-align:center;gap:4px}
.uxc.warn{background:#FFF1EA!important}
.uxc.go{background:#F3FBE9!important}
.uxc .ci{width:30px;height:30px}
.uxc .v{display:block;margin:0;font-size:22px;line-height:1;color:var(--vgK);text-align:center}
.uxc .v small{font:600 12px var(--f-body);color:#8A5D3B}
.uxc .l{order:9;font:600 12px/1.2 var(--f-body);color:#8A5D3B;margin-top:2px}
.uxc .pips{justify-content:center;margin-top:3px}
.uxc .pips img{width:14px;height:14px}
.uxs.three{grid-template-columns:1fr 1fr 1fr}
/* nút: 4 loại */
.sheet .btn{border:2px solid var(--vgK)!important;border-radius:10px!important;box-shadow:0 3px 0 var(--vgK)!important;text-shadow:none}
.sheet .btn:not(.g):not(.r){background:var(--dz)!important;color:var(--vgK)!important}
.sheet .btn.g{background:var(--la)!important;text-shadow:0 1px 0 var(--vgK)}
.sheet .btn.r{background:var(--pin)!important;text-shadow:0 1px 0 var(--vgK)}
.sheet .btn:active:not(:disabled){transform:translateY(2px);box-shadow:0 1px 0 var(--vgK)!important}
.sheet .btn:disabled{opacity:.55;filter:none}
.sheet .btn small{text-shadow:none}
.cta .btn img{width:26px;height:26px;margin:-6px 0}
.upc{background:var(--dz);box-shadow:0 3px 0 var(--vgK);border:2px solid var(--vgK);border-radius:10px}
.upc:disabled{opacity:.55;box-shadow:0 3px 0 var(--vgK)}
.upc span{color:#8A5D3B}
.upc img{width:30px;height:30px}
/* thẻ Ngoại nhờ: 3 ô */
.nxq{display:block!important;max-width:none!important;width:min(392px,calc(100vw - 24px))!important;padding:18px 8px 8px!important;border-radius:16px!important}
.nxq>small{top:-11px!important;left:10px!important;padding:3px 9px!important;line-height:1!important;font-size:11px!important;border-radius:8px!important;text-shadow:none!important}
.nxq .qrow{display:flex;gap:6px}
.nxq .q{flex:1;min-width:0;position:relative;background:#fff;border:2px solid var(--vgK);border-radius:10px;padding:6px 5px 5px;display:flex;flex-direction:column;align-items:center;gap:4px;box-shadow:0 2px 0 var(--vgK);text-align:center}
.nxq .q>*{flex:none}
.nxq .q>img{width:30px;height:30px}
.nxq .q>b{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;font:400 12px/1.1 var(--f-game);color:var(--vgK);overflow:hidden;max-width:100%;min-height:2.2em;display:-webkit-box}
.nxq .q .bar{width:100%;border-radius:4px}
.nxq .q .bar i{border-radius:2px}
.nxq .q.done{background:#FFF0B8}
.nxq .q .claim{height:22px;box-sizing:border-box;width:100%;justify-content:center;background:var(--rom);border:2px solid var(--vgK);border-radius:6px;padding:0 6px;font:400 12px/1 var(--f-game);color:var(--vgK);display:flex;align-items:center;gap:3px;white-space:nowrap}
.nxq .q .claim img{width:13px;height:13px}
.nxq .q .more{position:absolute;right:-6px;top:-8px;background:var(--vgK);color:#fff;font:400 10px/16px var(--f-game);padding:0 5px;border-radius:8px}
.nxq .q .tag{position:absolute;left:-6px;top:-8px;background:var(--rom);border:2px solid var(--vgK);color:var(--vgK);font:400 9px/12px var(--f-game);padding:0 5px;border-radius:7px;letter-spacing:.04em}
.nxq .q .steps{display:flex;gap:4px;height:6px;margin-top:-1px}
.nxq .q .steps i{width:6px;height:6px;border-radius:50%;background:#EADBB8;border:1px solid var(--vgK);box-sizing:border-box}
.nxq .q .steps i.on{background:var(--rom)}
.nxq .q .nqcs{display:flex;flex-wrap:wrap;justify-content:center;gap:3px}
.nxq .q .nqc{font-size:11px}
@media (max-width:560px){ .nxq{left:12px!important;right:12px!important;width:auto!important} }
/* khay trái: badge đỏ đếm; hết thì icon mờ + nhãn vàng mua */
.tl .tn{right:-2px!important;top:-4px!important;left:auto!important;min-width:20px;height:20px;padding:0 6px!important;border-radius:10px!important;background:#D9483A!important;border:2px solid #FBF7EE;color:#fff!important;font:400 12px/16px var(--f-game)!important;box-shadow:none!important;box-sizing:border-box;text-align:center;display:block!important;z-index:2}
.tl .tn:empty,.tl.zero .tn{display:none!important}
.tl.zero .tg{background:linear-gradient(#FFE27A,var(--rom))!important;color:var(--vgK)!important;text-shadow:none}
</style>'''
# --- 1. CSS: chèn sau khối <style> cuối cùng ---
i = s.rfind('</style>'); assert i > 0
s = s[:i + len('</style>')] + CSS + s[i + len('</style>'):]

# --- 2. UX.hero: thanh thay vòng; UX.card nhận icon ---
rep('''hero: (img, title, sub, tone = '', ring = null) => `<div class="uxh ${tone}"><div class="hi">${ring ? `<span class="ring" style="--p:${c01(ring[0]).toFixed(3)};--c:${ring[1]}"></span>` : ''}<img src="${img}" alt=""></div><div class="tx"><b>${title}</b><span>${sub}</span></div></div>`,''',
    '''hero: (img, title, sub, tone = '', ring = null) => { const bar = ring ? `<span class="bar"><i style="width:${Math.round(c01(ring[0]) * 100)}%"></i></span>` : ''; return `<div class="uxh ${tone}"><div class="hi"><img src="${img}" alt=""></div><div class="tx"><b>${title}</b>${ring && ring[2] ? `<span class="hb">${sub}${bar}<b>${ring[2]}</b></span>` : `<span>${sub}</span>${bar}`}</div></div>`; },''')
rep('''card: (label, val, extra = '', tone = '') => `<div class="uxc ${tone}"><span class="l">${label}</span><span class="v">${val}</span>${extra}</div>`,''',
    '''card: (label, val, extra = '', tone = '', img = '') => `<div class="uxc ${tone}">${img ? `<img class="ci" src="${img}" alt="">` : ''}<span class="l">${label}</span><span class="v">${val}</span>${extra}</div>`,''')
# giờ ngắn: 2g58 · 35p · 20 giây
rep("const fmtT = s => {", "const fmtS = s => { s = Math.max(0, Math.round(s)); if (s < 60) return s + ' giây'; const m = Math.round(s / 60); if (m < 60) return m + 'p'; const h = Math.floor(m / 60), mm = m % 60; return mm ? h + 'g' + String(mm).padStart(2, '0') : h + ' giờ'; };\nconst fmtT = s => {")

# --- 3. Chuồng gà ---
rep("  h += UX.cta([g.eggs ? UX.btn('gaegg', `Lượm ${g.eggs} trứng`, { g: 1, img: ICON.trungga }) : '', UX.btn('gafeed', food >= tcap ? 'Máng đầy' : 'Cho ăn', { g: !g.eggs && food < tcap, img: ICON.bap, dis: food >= tcap, sub: food >= tcap ? '' : bap ? `đổ đầy máng · ${bap} trái bắp` : `mua cám ${GA.cam} xu/phần` })]);\n", '')
rep("const lasts = lay > 0 ? Math.floor(g.trough / lay) * GA.cyc / ST.spd : 0;", "const lasts = lay > 0 ? Math.floor(g.trough / lay) * GA.cyc / ST.spd : 0; const CTA = [g.eggs ? UX.btn('gaegg', `Lượm ${g.eggs} trứng`, { g: 1, img: ICON.trungga }) : '', UX.btn('gafeed', food >= tcap ? 'Máng đầy' : 'Cho ăn', { g: !g.eggs && food < tcap, img: ICON.bap, dis: food >= tcap, sub: food >= tcap ? '' : bap ? `đổ đầy máng · ${bap} trái bắp` : `mua cám ${GA.cam} xu/phần` })];")
rep("else h += UX.hero(ICON.mai, 'Gà đang đẻ', `Trứng kế tiếp chừng ${fmtT(next)}`, '', [1 - next * ST.spd / GA.cyc, '#E9B23A']);",
    "else h += UX.hero(ICON.mai, 'Gà đang đẻ', 'Trứng kế', '', [1 - next * ST.spd / GA.cyc, '#E9B23A', fmtS(next)]);")
rep('''  h += '<div class="uxs">' + UX.card('Máng ăn', PART(`${food}/${tcap}`), UX.mbar(g.trough / Math.max(1, tcap), food < 1 ? '#F08A6E' : '#E9B23A') + `<span class="l" style="margin-top:5px">${food ? (lay > 0 ? 'đủ chừng ' + fmtT(lasts) : 'mái đang ấp, máng để dành') : 'hết rồi'}</span>`, food < 1 ? 'warn' : '')
    + UX.card('Trong ổ', PART(`${g.eggs}/${nestCap}`, 'trứng'), UX.pips(ICON.trungga, g.eggs, nestCap, 9), g.eggs ? 'go' : '') + '</div>';
  h += '<div class="uxs one">' + UX.card('Đàn gà', `${g.hens} mái${g.rooster ? ' · 1 trống' : ''} <small>· chuồng ${g.hens + g.rooster}/${cap} chỗ</small>`, `<span class="pips">${Array.from({ length: g.hens }, () => `<img src="${ICON.mai}" alt="">`).join('')}${g.rooster ? `<img src="${ICON.trong}" alt="">` : ''}${Array.from({ length: Math.max(0, cap - g.hens - g.rooster) }, () => `<img src="${ICON.mai}" class="off" alt="">`).join('')}</span>`) + '</div>';''',
    '''  h += '<div class="uxs three">' + UX.card(food ? (lay > 0 ? 'Máng ăn · đủ ' + fmtS(lasts) : 'Máng để dành') : 'Máng hết rồi', `${food}<small>/${tcap}</small>`, UX.mbar(g.trough / Math.max(1, tcap), food < 1 ? '#F08A6E' : '#F2C64A'), food < 1 ? 'warn' : '', ICON.bap)
    + UX.card('Trong ổ', `${g.eggs}<small>/${nestCap}</small>`, UX.pips(ICON.trungga, g.eggs, nestCap, 6), g.eggs ? 'go' : '', ICON.trungga)
    + UX.card(`Đàn · ${g.hens + g.rooster}/${cap} chỗ`, `${g.hens}${g.rooster ? ' <small>+1</small>' : ''}`, `<span class="pips">${Array.from({ length: g.hens }, () => `<img src="${ICON.mai}" alt="">`).join('')}${g.rooster ? `<img src="${ICON.trong}" alt="">` : ''}${Array.from({ length: Math.max(0, cap - g.hens - g.rooster) }, () => `<img src="${ICON.mai}" class="off" alt="">`).join('')}</span>`, '', ICON.mai) + '</div>' + UX.cta(CTA);''')

# --- 4. Thẻ Ngoại nhờ 3 ô ---
rep('''  const h = `<small>${go ? 'LÀM LIỀN' : lab}</small><img src="${ic}" alt=""><span class="nqt"><b>${t}</b>${chips ? `<span class="nqb nqcs">${chips}</span>` : `<span class="nqb"><i><u style="width:${Math.round(Math.max(0, Math.min(1, f)) * 100)}%"></u><em>${em}</em></i></span>`}${dl}</span>`;''',
    '''  /* v108: 3 ô — ô 1 việc đang theo (việc cấp có nhãn CẤP + chấm bước), ô 2–3 việc hôm nay (xong thì vàng "Nhận"), "+N" còn lại */
  const tShort = x => String(x).replace(/^Nhờ Ngoại /, '').replace(/ trong vườn$/, '').replace(/^Gieo hạt /, 'Gieo ').replace(/^Đặt (\d+ )?món trang trí/, 'Đặt $1đồ trang trí').replace(/^./, c => c.toUpperCase());
  const slot = (ic2, t2, inner, cls = '', a = '') => `<span class="q ${cls}" data-a="${a}"><img src="${ic2}" alt=""><b>${tShort(t2)}</b>${inner}</span>`;
  const barH = (f2, em2) => `<span class="bar"><i style="width:${Math.round(Math.max(0, Math.min(1, f2)) * 100)}%"></i><em>${em2}</em></span>`;
  const steps = q && q.t === 'goal' && lab === 'NGOẠI NHỜ' && q.goals.length > 1 ? `<span class="steps">${q.goals.map(([, f2, nn]) => `<i class="${f2() >= nn ? 'on' : ''}"></i>`).join('')}</span>` : '';
  const slots = [slot(ic, t, (chips ? `<span class="nqcs">${chips}</span>` : barH(f, em)) + steps + (lab === 'NGOẠI NHỜ' ? '<span class="tag">CẤP</span>' : ''), '', act)];
  try { ensureTasks(); const L2 = ST.tasks.list.filter(x => !(isTask && act === 'task:' + x.t + ':' + (x.k || ''))), pick = [...L2.filter(x => x.done && x.cl === false), ...L2.filter(x => !x.done)], show = pick.slice(0, 2);
    show.forEach((x, i) => { let ic3; try { ic3 = TASKIC(x); } catch (e) { ic3 = UIC.task; } const more = i === show.length - 1 && pick.length > show.length ? `<span class="more">+${pick.length - show.length}</span>` : '';
      slots.push(x.done ? slot(ic3, x.txt, `<span class="claim">${x.rw && x.rw[0] === 'coin' ? `<img src="${UIC.coin}" alt="">+${x.rw[1]} ` : ''}Nhận</span>` + more, 'done', 'book') : slot(ic3, x.txt, barH(x.have / x.need, x.need > 1 ? `${x.have}/${x.need}` : 'chưa làm') + more, '', 'task:' + x.t + ':' + (x.k || ''))); }); } catch (e) {}
  const h = `<small>${go ? 'LÀM LIỀN' : lab}</small><span class="qrow">${slots.join('')}</span>`;''')
rep('''$('#nxq').addEventListener('click', e => { sfx('pick'); if (e.target.closest('[data-d]')) return openBook('viec'); if ($('#nxq').dataset.a === 'weed') weedGo(); else if (($('#nxq').dataset.a || '').startsWith('pen:')) penGo($('#nxq').dataset.a.slice(4)); else if (($('#nxq').dataset.a || '').startsWith('task:')){ const [, t, k] = $('#nxq').dataset.a.split(':'); taskGo(t, k); } else openBook('viec'); });''',
    '''$('#nxq').addEventListener('click', e => { sfx('pick'); if (e.target.closest('[data-d]')) return openBook('viec'); const sq = e.target.closest('.q'), a = (sq && sq.dataset.a) || $('#nxq').dataset.a || ''; if (a === 'weed') weedGo(); else if (a.startsWith('pen:')) penGo(a.slice(4)); else if (a.startsWith('task:')){ const [, t, k] = a.split(':'); taskGo(t, k); } else openBook('viec'); });''')

# --- 5. Khay trái ---
rep('<span class="tg">Hạt</span></button>', '<span class="tg">Hạt</span><span class="tn" id="tSeedN"></span></button>')
rep('''$('#tRomN').innerHTML = rn > 0 ? rn : `<img src="${UIC.coin}" alt="">${ROM_PRICE}`; } catch (e) {}''',
    '''$('#tRomN').textContent = rn > 0 ? rn : ''; const tgr = tb.querySelector('.tg'); if (tgr) tgr.textContent = rn > 0 ? 'Rơm' : '+ ' + ROM_PRICE + ' xu'; } catch (e) {} try { const sn = Object.values(ST.seeds || {}).reduce((a, b) => a + (b || 0), 0), ts = TRAY.seed; ts.classList.toggle('zero', sn < 1); $('#tSeedN').textContent = sn > 0 ? sn : ''; const tgs = ts.querySelector('.tg'); if (tgs) tgs.textContent = sn > 0 ? 'Hạt' : 'Mua hạt'; } catch (e) {}''')

rep("UX.hero(ICON.vitmai, 'Vịt đang đẻ', `Lứa trứng kế tiếp chừng ${fmtT(next)}`, '', [1 - next * ST.spd / VIT.cyc, '#E9B23A'])", "UX.hero(ICON.vitmai, 'Vịt đang đẻ', 'Trứng kế', '', [1 - next * ST.spd / VIT.cyc, '#E9B23A', fmtS(next)])")
rep("const BUILD = 'v107b'", "const BUILD = 'v108a'")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
