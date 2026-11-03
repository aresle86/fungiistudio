/* ===== UX kit cho bảng: điều con muốn biết nhất nằm trên cùng (hero), việc chính kế đó (nút to), chi tiết bên dưới, luật chơi gấp lại ===== */
const c01 = v => Math.max(0, Math.min(1, v));
const UX = {
  hero: (img, title, sub, tone = '', ring = null) => `<div class="uxh ${tone}"><div class="hi">${ring ? `<span class="ring" style="--p:${c01(ring[0]).toFixed(3)};--c:${ring[1]}"></span>` : ''}<img src="${img}" alt=""></div><div class="tx"><b>${title}</b><span>${sub}</span></div></div>`,
  pips: (img, n, max, cap = 10) => { const m = Math.min(max, cap); let h = '<span class="pips">'; for (let i = 0; i < m; i++) h += `<img src="${img}" class="${i < n ? '' : 'off'}" alt="">`; return h + (max > cap ? `<span class="more">+${max - cap}</span>` : '') + '</span>'; },
  card: (label, val, extra = '', tone = '') => `<div class="uxc ${tone}"><span class="l">${label}</span><span class="v">${val}</span>${extra}</div>`,
  mbar: (f, col) => `<div class="mbar"><i style="width:${Math.round(c01(f) * 100)}%;background:${col}"></i></div>`,
  cta: btns => { const b = btns.filter(Boolean); return b.length ? `<div class="cta">${b.join('')}</div>` : ''; },
  btn: (a, label, o = {}) => `<button class="btn${o.g ? ' g' : ''}${o.r ? ' r' : ''}" data-a="${a}"${o.k != null ? ` data-k="${o.k}"` : ''}${o.n != null ? ` data-n="${o.n}"` : ''}${o.hold ? ` data-hold="${o.hold}"` : ''} ${o.dis ? 'disabled' : ''}>${o.img ? `<img src="${o.img}" alt="">` : ''}<span>${label}${o.sub ? `<small>${o.sub}</small>` : ''}</span></button>`,
  upc: (a, img, title, cost, o = {}) => `<button class="upc" data-a="${a}"${o.k != null ? ` data-k="${o.k}"` : ''} ${o.dis ? 'disabled' : ''}><img src="${img}" alt=""><div><b>${title}</b>${o.why ? `<span class="why">${o.why}</span>` : cost != null ? `<span><img src="${UIC.coin}" alt="">${cost} xu</span>` : ''}</div></button>`,
  title: (t, small = '') => `<div class="uxt">${t}${small ? `<small>${small}</small>` : ''}</div>`,
  more: (t, html) => `<details class="uxm"><summary>${t}</summary><div>${html}</div></details>`,
  chips: inp => Object.entries(inp).map(([k, n]) => { const hv = has(k); return `<span class="chip${hv < n ? ' no' : ''}"><img src="${ICON[k]}" alt="">${Math.min(hv, n)}/${n}</span>`; }).join(''),
  // ô chế biến: trống (chạm để chọn món) · đang làm (vòng thời gian) · xong (chạm để lấy)
  slot: (i, t, R, aPick, aTake, label, doneTxt = 'Xong rồi · chạm lấy') => { if (!t) return `<button class="slot empty" data-a="${aPick}" data-n="${i}"><div class="si">+</div><div><b>${label} ${i + 1}</b><span>Chạm để chọn món</span></div></button>`;
    const d = R[t.k] || GD(t.k), done = t.t <= 0; return `<button class="slot${done ? ' done' : ''}" ${done ? `data-a="${aTake}" data-n="${i}"` : 'data-a="noop"'}><div class="si"><span class="ring" style="--p:${c01(1 - t.t / t.T).toFixed(3)};--c:${done ? '#7CC04A' : '#E9B23A'}"></span><img src="${ICON[t.k]}" alt=""></div><div><b>${d.name}</b><span>${done ? doneTxt : 'còn ' + fmtT(t.t)}</span></div></button>`; },
  // danh sách món để chọn: hình thành phẩm, nguyên liệu có/thiếu, thời gian, giá bán
  pick: (aPut, i, R, label) => `<button class="back" data-a="pickback">‹ Quay lại</button>` + UX.title(`Chọn món cho ${label.toLowerCase()} ${i + 1}`) + Object.keys(R).map(k => { const d = R[k], lk = (ST.lv || 1) < (d.lv || 1), can = !lk && canIn(d.in);
    return `<button class="rcp${lk ? ' lock' : ''}" data-a="${aPut}" data-k="${k}" data-n="${i}" ${can ? '' : 'disabled'}><img src="${ICON[k]}" alt=""><div class="rt"><b>${d.name}</b><div class="ins">${lk ? `<span class="chip no">Tới cấp ${d.lv}</span>` : UX.chips(d.in)}</div></div><div class="rm">${fmtT(d.t)}<em><img src="${UIC.coin}" alt="">${d.sell}${d.out > 1 ? ' ×' + d.out : ''}</em></div></button>`; }).join('') };
const PART = (n, unit = 'phần') => `${n} <small>${unit}</small>`;
/* --- chuồng gà --- */
function gaHTML(){ const g = ST.ga, cap = gaCap(), lvOk = (ST.lv || 1) >= GA.buyLv, b = g.brood, lay = gaLaying(), tcap = g.hens * GA.trough, food = Math.floor(g.trough), nestCap = g.hens * GA.nestMax;
  const next = food >= 1 && lay > 0 ? Math.max(0, GA.cyc - g.acc) / ST.spd : null, bap = ST.inv.bap || 0; let h = '';
  if (g.eggs > 0) h += UX.hero(ICON.trungga, `Có ${g.eggs} trứng chờ lượm`, g.eggs >= nestCap ? 'Ổ đầy rồi, lượm đi thì gà mới đẻ tiếp' : next != null ? `Trứng kế tiếp chừng ${fmtT(next)}` : 'Máng hết đồ ăn, cho gà ăn để đẻ tiếp', 'go');
  else if (food < 1) h += UX.hero(ICON.mai, 'Máng hết thức ăn', 'Gà nhịn đói thì không đẻ. Cho ăn liền nghe con', 'warn');
  else h += UX.hero(ICON.mai, 'Gà đang đẻ', `Trứng kế tiếp chừng ${fmtT(next)}`, '', [1 - next * ST.spd / GA.cyc, '#E9B23A']);
  h += UX.cta([g.eggs ? UX.btn('gaegg', `Lượm ${g.eggs} trứng`, { g: 1, img: ICON.trungga }) : '', UX.btn('gafeed', food >= tcap ? 'Máng đầy' : 'Cho ăn', { g: !g.eggs && food < tcap, img: ICON.bap, dis: food >= tcap, sub: food >= tcap ? '' : bap ? `dùng ${bap} bắp trong kho` : `mua cám ${GA.cam} xu/phần` })]);
  const lasts = lay > 0 ? Math.floor(g.trough / lay) * GA.cyc / ST.spd : 0;
  h += '<div class="uxs">' + UX.card('Máng ăn', PART(`${food}/${tcap}`), UX.mbar(g.trough / Math.max(1, tcap), food < 1 ? '#F08A6E' : '#E9B23A') + `<span class="l" style="margin-top:5px">${food ? 'đủ chừng ' + fmtT(lasts) : 'hết rồi'}</span>`, food < 1 ? 'warn' : '')
    + UX.card('Trong ổ', PART(`${g.eggs}/${nestCap}`, 'trứng'), UX.pips(ICON.trungga, g.eggs, nestCap, 9), g.eggs ? 'go' : '') + '</div>';
  h += '<div class="uxs one">' + UX.card('Đàn gà', `${g.hens} mái${g.rooster ? ' · 1 trống' : ''} <small>· chuồng ${g.hens + g.rooster}/${cap} chỗ</small>`, `<span class="pips">${Array.from({ length: g.hens }, () => `<img src="${ICON.mai}" alt="">`).join('')}${g.rooster ? `<img src="${ICON.trong}" alt="">` : ''}${Array.from({ length: Math.max(0, cap - g.hens - g.rooster) }, () => `<img src="${ICON.mai}" class="off" alt="">`).join('')}</span>`) + '</div>';
  if (b) h += '<div class="uxs one">' + UX.card(b.stage === 'egg' ? 'Đang ấp trứng' : 'Gà con đang lớn', `còn ${fmtT(((b.stage === 'egg' ? GA.brood : GA.grow) - b.t) / ST.spd)}`, UX.mbar(b.t / (b.stage === 'egg' ? GA.brood : GA.grow), '#86B06A'), 'go') + '</div>';
  if (lvOk){ const full = g.hens + g.rooster >= cap, why = b ? 'đang ấp một lứa' : !g.rooster ? 'cần gà trống' : g.hens < 2 ? 'cần 2 gà mái' : !(ST.inv.trungga > 0) ? 'cần 1 trứng trong kho' : '';
    h += UX.title('Nuôi thêm', `${g.hens + g.rooster}/${cap} chỗ`) + '<div class="upg">' + UX.upc('gabuy', ICON.mai, 'Mua gà mái', GA.buy, { dis: full || ST.xu < GA.buy, why: full ? 'chuồng hết chỗ' : '' }) + (g.lv + 1 < GA.caps.length ? UX.upc('gaup', ICON.camga, `Chuồng ${GA.caps[g.lv + 1]} con`, GA.up[g.lv + 1], { dis: ST.xu < GA.up[g.lv + 1] }) : '') + UX.upc('gahatch', ICON.trungga, 'Ấp 1 trứng', null, { dis: !!why, why: why || 'nở sau ' + fmtT(GA.brood / ST.spd) }) + '</div>'; }
  h += UX.more('Cách nuôi gà', `Gà đẻ mỗi ${GA.cyc / 3600} tiếng một trứng nếu máng còn thức ăn. Cho ăn dùng bắp trong kho trước (1 trái = ${GA.bapPhan} phần), thiếu thì mua cám ${GA.cam} xu một phần. ${lvOk ? `Ấp trứng cần gà trống và một trứng trong kho, nở ra mái thì đẻ thêm, trống thì Ngoại bán giùm ${GA.roosterSell} xu.` : `Tới cấp ${GA.buyLv} mua thêm gà, nâng chuồng và ấp trứng được.`}`);
  return h; }
/* --- chuồng vịt --- */
function vitHTML(){ const v = ST.vit, cap = vitCap(), tcap = v.n * VIT.trough, food = Math.floor(v.trough), nestCap = v.n * VIT.nestMax, rm = ST.inv.raumuong || 0;
  const next = food >= 1 ? Math.max(0, VIT.cyc - v.acc) / ST.spd : null; let h = '';
  if (v.eggs > 0) h += UX.hero(ICON.trungvit, `Có ${v.eggs} trứng vịt chờ lượm`, next != null ? `Lứa kế tiếp chừng ${fmtT(next)}` : 'Máng hết đồ ăn rồi con', 'go');
  else if (food < 1) h += UX.hero(ICON.vitmai, 'Máng vịt hết đồ ăn', 'Cho rau muống hay vớt lục bình cho vịt ăn', 'warn');
  else h += UX.hero(ICON.vitmai, 'Vịt đang đẻ', `Lứa trứng kế tiếp chừng ${fmtT(next)}`, '', [1 - next * ST.spd / VIT.cyc, '#E9B23A']);
  h += UX.cta([v.eggs ? UX.btn('viteggs', `Lượm ${v.eggs} trứng`, { g: 1, img: ICON.trungvit }) : '', UX.btn('vitfeed', food >= tcap ? 'Máng đầy' : 'Cho ăn', { g: !v.eggs && food < tcap, img: ICON.raumuong, dis: food >= tcap, sub: food >= tcap ? '' : rm ? `dùng ${rm} bó rau muống` : `mua cám ${VIT.cam} xu/phần` })]);
  h += '<div class="uxs">' + UX.card('Máng ăn', PART(`${food}/${tcap}`), UX.mbar(v.trough / Math.max(1, tcap), food < 1 ? '#F08A6E' : '#86B06A') + `<span class="l" style="margin-top:5px">${food ? 'đủ chừng ' + fmtT(Math.floor(v.trough / v.n) * VIT.cyc / ST.spd) : 'hết rồi'}</span>`, food < 1 ? 'warn' : '')
    + UX.card('Trong ổ', PART(`${v.eggs}/${nestCap}`, 'trứng'), UX.pips(ICON.trungvit, v.eggs, nestCap, 9), v.eggs ? 'go' : '') + '</div>';
  h += '<div class="uxs one">' + UX.card('Đàn vịt', `${v.n} vịt mái <small>· chuồng ${v.n}/${cap} chỗ</small>`, UX.pips(ICON.vitmai, v.n, cap, 12)) + '</div>';
  h += UX.title('Nuôi thêm', `${v.n}/${cap} chỗ`) + '<div class="upg">' + UX.upc('vitbuy', ICON.vitmai, 'Mua vịt mái', VIT.buy, { dis: v.n >= cap || ST.xu < VIT.buy, why: v.n >= cap ? 'chuồng hết chỗ' : '' }) + (v.lv + 1 < VIT.caps.length ? UX.upc('vitup', ICON.vitmai, `Chuồng ${VIT.caps[v.lv + 1]} con`, VIT.up[v.lv + 1], { dis: ST.xu < VIT.up[v.lv + 1] }) : '') + '</div>';
  h += UX.more('Cách nuôi vịt', `Vịt đẻ mỗi ${VIT.cyc / 3600} tiếng một trứng nếu máng còn thức ăn. Vịt ăn rau muống trong kho (1 bó = ${VIT.rm} phần), lục bình vớt dưới mương (+1 phần, khỏi tốn xu), thiếu thì mua cám ${VIT.cam} xu một phần.${(ST.lv || 1) >= 9 ? ' Lò ấp trấu cạnh chuồng ấp trứng vịt ra vịt con.' : ''}`);
  return h; }
/* --- liếp, giàn, gốc cây --- */
const moistTxt = m => m <= 0 ? 'Khô' : m < .35 ? 'Hơi khô' : m < .75 ? 'Vừa' : 'Ướt đẫm', soilTxt = s2 => s2 > .75 ? 'Tốt' : s2 > .45 ? 'Khá' : 'Đất mệt';
function plotHTML(P, p, id){ const st = stageOf(p), cond = condOf(p), c = p.crop && CROPS[p.crop], rom = ST.inv.rom || 0, mulched = p.mulch > ST.gt; let h = '', cta = [];
  if (c){ const left = (c.grow - p.g) / (mulched ? 1.08 : 1) / fastK(p) / ST.spd, rp = ripe(p), dry = !P.trellis && p.moist <= 0;
    if (p.dead) h += UX.hero(ICON[p.crop], 'Cây chết khô rồi', 'Giữ nút nhổ bỏ rồi gieo lại nghe con', 'warn');
    else if (rp) h += UX.hero(ICON[p.crop], 'Chín rồi, hái thôi!', `Được chừng ${Math.max(1, harvestN(p) - (p.stolen || 0))} ${c.unit}${c.cuts > 1 && !c.tree ? ` · đợt ${(p.cut || 0) + 1}/${c.cuts}` : ''}`, 'go');
    else if (cond === 'wilt') h += UX.hero(ICON[p.crop], `${STAGE[st]} · đang héo`, 'Tưới liền kẻo thu kém', 'warn', [p.g / c.grow, '#F08A6E']);
    else if (dry) h += UX.hero(ICON[p.crop], 'Khô đất, cây ngừng lớn', `${STAGE[st]} · tưới là lớn tiếp`, 'warn', [p.g / c.grow, '#F08A6E']);
    else h += UX.hero(ICON[p.crop], STAGE[st], `Còn ${fmtT(left)} là chín${c.cuts > 1 && !c.tree ? ` · đợt ${(p.cut || 0) + 1}/${c.cuts}` : ''}`, '', [p.g / c.grow, '#86B06A']);
    if (rp) cta.push(UX.btn('harvest', 'Hái', { g: 1, img: ICON[p.crop] })); else if (p.dead) cta.push(UX.btn('', 'Giữ để nhổ bỏ', { r: 1, hold: 'pull' })); else if (!P.trellis && p.moist < .35) cta.push(UX.btn('water', 'Tưới', { g: 1, img: UIC.can })); }
  else { h += UX.hero(UIC.seedbag, P.tree ? 'Gốc trống' : 'Liếp trống', P.tree ? 'Trồng cây giống ở gốc này' : 'Gieo hạt mới nghe con'); cta.push(UX.btn('pickseed', P.tree ? 'Chọn cây giống' : 'Chọn hạt để gieo', { g: 1, img: UIC.seedbag })); }
  h += UX.cta(cta);
  if (!P.trellis){ const mp = Math.round(c01(p.moist) * 5), sp = Math.round(c01(p.soil) * 5);
    h += '<div class="uxs">' + UX.card('Độ ẩm', moistTxt(p.moist), UX.pips(UIC.drop, mp, 5), p.moist <= 0 ? 'warn' : '') + UX.card('Đất', soilTxt(p.soil), UX.pips(UIC.sprout, sp, 5), p.soil <= .45 ? 'warn' : '') + '</div>';
    if (!P.tree) h += '<div class="uxs one">' + UX.card('Rơm phủ', mulched ? `còn ${fmtT((p.mulch - ST.gt) / ST.spd)} <small>· giữ ẩm, lớn nhanh hơn</small>` : 'Chưa phủ <small>· phủ rơm giữ ẩm lâu, cây lớn nhanh</small>', '', mulched ? 'go' : '') + '</div>'; }
  else h += '<div class="uxs one">' + UX.card('Giàn trên mương', 'Rễ sát mương <small>· không cần tưới</small>') + '</div>';
  const acts = [];
  if (c && !p.dead && !P.trellis && !cta.some(x => x.includes('data-a="water"'))) acts.push(UX.btn('water', 'Tưới', { dis: p.moist > .92 }));
  if (!P.trellis && !P.tree) acts.push(UX.btn('mulch', `Phủ rơm · còn ${rom}`, { dis: rom < 1 || mulched }));
  if (!P.trellis && !P.tree && ST.ho && ST.ho.bags > 0 && p.soil < .95) acts.push(UX.btn('bon', `Bón phân · còn ${ST.ho.bags}`));
  if (acts.length) h += `<div class="acts">${acts.join('')}</div>`;
  if (c && !p.dead && !c.tree) h += UX.more('Khác', `Nhổ bỏ cây đang trồng để gieo cây khác. Giữ nút một chút để nhổ.<div class="acts"><button class="btn r hold" data-hold="pull">Giữ để nhổ bỏ</button></div>`);
  return h; }
/* --- nong phơi (ô + chọn món) --- */
function nongHTML(){ const N = ST.nong, sun = sunAt(Date.now());
  if (SHEET && SHEET.pick != null) return UX.pick('nput', SHEET.pick, PHOI, 'Nong');
  const done = N.trays.filter(t => t && t.t <= 0).length, run = N.trays.filter(t => t && t.t > 0), soon = run.length ? Math.min(...run.map(t => t.t)) : 0; let h = '';
  if (done) h += UX.hero(ICON[N.trays.find(t => t && t.t <= 0).k], `${done} nong khô rồi`, 'Lấy cất lên gác bếp nghe con', 'go');
  else if (run.length) h += UX.hero(UIC.sun, sun ? 'Đang phơi nắng' : 'Trời tối, nong nằm yên', sun ? `Nong kế tiếp khô sau ${fmtT(soon)} nắng` : `Sáng mai ${NONG.sun[0]} giờ nắng lên là khô tiếp, không hư đâu`, sun ? '' : 'warn');
  else h += UX.hero(ICON.nong, '4 nong đang trống', 'Chạm một nong trống để phơi đồ', '');
  h += UX.cta([done ? UX.btn('ntakeall', `Lấy ${done} món khô`, { g: 1, img: ICON[N.trays.find(t => t && t.t <= 0).k] }) : '']);
  h += '<div class="slots">' + N.trays.map((t, i) => UX.slot(i, t, PHOI, 'npick', 'ntake', 'Nong', 'Khô rồi · chạm lấy')).join('') + '</div>';
  h += `<div class="uxs one" style="margin-top:10px">${UX.card('Gác bếp', `${gbUsed()}/${GB_CAP} <small>chỗ · đồ khô cất ở đây</small>`, UX.mbar(gbUsed() / GB_CAP, gbUsed() >= GB_CAP ? '#F08A6E' : '#C9A66B'))}</div>`;
  h += UX.more('Cách phơi', `Phơi bằng nắng thật, từ ${NONG.sun[0]} giờ sáng tới ${NONG.sun[1]} giờ chiều. Trời tối nong nằm yên, không hư. Đồ khô bán ở chợ hay giao hàng xóm.<div class="acts">${moveBtn('nong')}</div>`); return h; }
