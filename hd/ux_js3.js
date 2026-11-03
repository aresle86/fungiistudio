/* --- Sổ · Việc của Ngoại: cấp, việc lên cấp, việc hôm nay — có hình, có thanh tiến độ --- */
const LVFEAT = { 2: [['la', 'Việc lặt vặt']], 3: [['cho', 'Đơn nhà bên'], ['sau', 'Bắt sâu']], 4: [['trungchien', 'Bếp Ngoại'], ['cui', 'Nhặt củi'], ['cuoc', 'Góc vườn mới']], 5: [['mai', 'Mua gà, ấp trứng']], 6: [['vitmai', 'Chuồng vịt']],
  7: [['cuoc', 'Bãi hông nhà · Sửa vườn'], ['nong', 'Nong phơi']], 8: [['khap', 'Khạp muối'], ['ho', 'Hố ủ phân']], 9: [['caloc', 'Mé sông'], ['cancau', 'Câu cá'], ['vitcon', 'Lò ấp vịt']], 10: [['say', 'Lò sấy'], ['ghe', 'Ghe chợ nổi'], ['gio', 'Giỏ lục bình']], 11: [['xoaisay', 'Sau nhà 10 ô']], 12: [['mutdua', 'Món Tết'], ['so', 'Sổ vườn']] };
const icOf = k => ICON[k] || UIC[k] || UIC.task;
function pgLevel(){ const lv = ST.lv || 1, n = lv + 1, need = XPN[n], prev = XPN[lv], xp = ST.xp || 0, q = QUEST[n] && !(ST.qd || {})[n] ? QUEST[n] : null; let h = '';
  if (!need) return UX.hero(UIC.so, `Cấp ${lv} · vườn của con`, 'Cấp cao nhất hiện có. Chăm vườn, giao ghe chợ nổi, chờ mùa xoài nghe con', 'go');
  const f = (xp - prev) / (need - prev), ready = xp >= need;
  h += UX.hero(AVIMG && ST.player ? AVIMG.face[ST.player.av] : UIC.sprout, `Cấp ${lv}`, ready ? (q ? `Đủ kinh nghiệm rồi, làm việc Ngoại dặn là lên cấp ${n}` : `Sắp lên cấp ${n}`) : `Còn ${need - xp} kinh nghiệm nữa lên cấp ${n}`, ready ? 'go' : '', [f, '#86B06A']);
  const ks = Object.keys(UNLOCK).filter(k => UNLOCK[k] === n), feats = [...ks.map(k => [k, CROPS[k].name]), ...(LVFEAT[n] || [])];
  if (feats.length) h += UX.title(`Cấp ${n} mở`) + `<div class="ulk">${feats.map(([k, t]) => `<span><img src="${icOf(k)}" alt="">${t}</span>`).join('')}</div>`;
  if (q){ h += UX.title(`Việc để lên cấp ${n}`, ready ? '' : 'đủ kinh nghiệm mới làm được');
    const qi = q.t === 'weed' ? UIC.sickle : q.t === 'pay' ? (q.exp ? ICON.cuoc : n === 10 ? ICON.cuoc : n === 12 ? ICON.cuoc : UIC.coin) : UIC.task;
    let body = `<div class="qcd${ready ? '' : ' wait'}"><img src="${qi}" alt=""><div class="qt"><b>${q.txt}</b><span>${q.how}</span>`;
    if (q.t === 'weed') body += `<div class="qg"><span>Vuốt liềm dọc mé mương</span><em>${ST.weed || 0}/${q.need}</em></div>${UX.mbar((ST.weed || 0) / q.need, '#86B06A')}`;
    if (q.t === 'goal') body += q.goals.map(([t, f2, nn]) => { const v = Math.min(nn, f2()); return `<div class="qg${v >= nn ? ' ok' : ''}"><span>${v >= nn ? '✓ ' : ''}${t}</span><em>${v}/${nn}</em></div>${UX.mbar(v / nn, v >= nn ? '#7CC04A' : '#E9B23A')}`; }).join('');
    body += '</div></div>'; h += body;
    if (q.t === 'pay') h += `<div class="cta"><button class="btn g" data-b="quest" data-k="${n}" ${ready && ST.xu >= q.xu ? '' : 'disabled'}><img src="${UIC.coin}" alt=""><span>Trả ${q.xu} xu${!ready ? '<small>chưa đủ kinh nghiệm</small>' : ST.xu < q.xu ? `<small>còn thiếu ${q.xu - ST.xu} xu</small>` : ''}</span></button></div>`; }
  return h + UX.more('Kinh nghiệm có từ đâu', 'Hái rau, lượm trứng (món càng quý càng nhiều), gieo hạt, cho gà vịt ăn, cứu cây héo, đắp liếp mới, giao đơn, làm xong việc Ngoại nhờ.'); }
const TASKIC = x => x.t === 'water' ? UIC.can : x.t === 'mulch' || x.t === 'buyrom' ? ICON.rom : x.t === 'harvest' ? ICON[x.k] : x.t === 'sell' ? ICON.cho : x.t === 'plant' ? UIC.seedbag : UIC.task;
function pgViec(){ ensureTasks(); const T2 = ST.tasks, nd = T2.list.filter(x => x.done).length, wd = ['Chủ nhật', 'thứ Hai', 'thứ Ba', 'thứ Tư', 'thứ Năm', 'thứ Sáu', 'thứ Bảy'][new Date().getDay()];
  let h = hdr('viec') + '<div class="uxbk">' + pgLevel() + UX.title(`Việc hôm nay · ${wd}`, `xong ${nd}/${T2.list.length}`);
  h += T2.list.map(x => `<div class="tkc${x.done ? ' done' : ''}"><img src="${TASKIC(x)}" alt=""><div class="tt"><b>${x.txt}</b>${x.done ? '<span class="ok">Xong rồi</span>' : (x.need > 1 ? UX.mbar(x.have / x.need, '#E9B23A') + `<span>${x.have}/${x.need}</span>` : '<span>Chưa làm</span>')}</div><span class="rw"><img src="${x.rw[0] === 'coin' ? UIC.coin : ICON.rom}" alt="">+${x.rw[1]}</span></div>`).join('');
  h += `<div class="tkc bonus${T2.got ? ' done' : ''}"><img src="${ICON[T2.bonus]}" alt=""><div class="tt"><b>${T2.got ? 'Đã nhận quà' : 'Xong hết việc hôm nay'}</b><span>Ngoại tặng 1 bao hạt ${CROPS[T2.bonus].name.toLowerCase()}</span>${UX.mbar(nd / T2.list.length, '#7CC04A')}</div><span class="rw"><img src="${UIC.seedbag}" alt="">+1</span></div>`;
  return h + '</div>'; }
/* --- bếp: nồi dạng ô, chạm nồi trống để chọn món --- */
function bepHTML(){ const B = ST.bep, lv = ST.lv || 1; if (lv < BEP.lv) return UX.hero(ICON.trungchien, 'Bếp Ngoại còn nguội', `Tới cấp ${BEP.lv} Ngoại chỉ con nấu bếp củi nghe`);
  if (!B.lit){ const c = has('cui'); return UX.hero(ICON.cui, 'Nhóm lại bếp củi', `Bếp nguội lâu rồi. Nhặt ${BEP.lite} nhánh củi khô dưới gốc cây về nhóm bếp`, c >= BEP.lite ? 'go' : 'warn') + UX.cta([UX.btn('bplite', 'Nhóm bếp', { g: 1, img: ICON.cui, dis: c < BEP.lite, sub: `${Math.min(c, BEP.lite)}/${BEP.lite} củi` })]) + '<div class="uxs one">' + UX.card('Củi', `${c}/${BEP.lite}`, UX.pips(ICON.cui, Math.min(c, BEP.lite), BEP.lite)) + '</div>' + UX.more('Mua củi', 'Chợ cũng bán củi, 3 xu một bó.'); }
  if (SHEET && SHEET.pick != null) return UX.pick('bpcook', SHEET.pick, Object.fromEntries(Object.entries(DISH).map(([k, d]) => [k, { ...d, t: d.t / ST.spd }])), 'Nồi');
  const done = B.pots.filter(p => p && p.t <= 0), run = B.pots.filter(p => p && p.t > 0), cui = has('cui'); let h = '';
  if (done.length) h += UX.hero(ICON[done[0].k], `${done.length} nồi chín rồi`, 'Lấy cất lên gác bếp nghe con', 'go');
  else if (run.length){ const t = run.reduce((a, b) => a.t < b.t ? a : b); h += UX.hero(ICON[t.k], `Đang nấu ${DISH[t.k].name.toLowerCase()}`, `Còn ${bepT(t.t)} là chín`, '', [1 - t.t / DISH[t.k].t, '#E9A23A']); }
  else h += UX.hero(ICON.cui, cui ? 'Bếp đang rảnh' : 'Hết củi rồi', cui ? 'Chạm nồi trống để chọn món nấu' : 'Mỗi món nấu cần một bó củi', cui ? '' : 'warn');
  h += UX.cta([done.length ? UX.btn('bptakeall', 'Lấy hết', { g: 1, img: ICON[done[0].k] }) : '', !cui ? UX.btn('gocho3', 'Mua củi', { img: ICON.cui, sub: '3 xu một bó' }) : '']);
  h += '<div class="slots">' + B.pots.map((p, i) => UX.slot(i, p ? { ...p, T: DISH[p.k].t, t: p.t } : null, DISH, 'bpick', 'bptake', 'Nồi', 'Chín rồi · chạm lấy')).join('') + '</div>';
  h += `<div class="uxs" style="margin-top:10px">${UX.card('Củi', `${cui} <small>bó</small>`, '', cui ? '' : 'warn')}${UX.card('Gác bếp', `${gbUsed()}/${GB_CAP} <small>chỗ</small>`, UX.mbar(gbUsed() / GB_CAP, '#C9A66B'))}</div>`;
  return h + UX.more('Bếp Ngoại', 'Hai nồi nấu cùng lúc, mỗi món một bó củi. Món chín cất lên gác bếp, đem ra chợ bán hoặc giao đơn nhà bên. Lần đầu nấu món nào Ngoại kể chuyện món đó.'); }
/* --- bến nhà --- */
function benHTML(){ const nOrd = (ST.ord && ST.ord.list || []).length, nOk = ST.ord ? ST.ord.list.filter(ordCan).length : 0, lv = ST.lv || 1, left = mauLeft(), gh = gheOn() && ST.ghe.o; let h = '';
  if (gh) h += UX.hero(ICON.ghe, 'Ghe bẹo chợ nổi đang đậu', `Đơn lớn ${ST.ghe.o.xu} xu, ghe đi lúc hết ngày`, 'go');
  else if (nOk) h += UX.hero(ICON.cho, `${nOk} đơn giao được rồi`, 'Hàng xóm đang chờ ở bến', 'go');
  else h += UX.hero(UIC.task, 'Bến nhà', lv >= ORD.lv ? (nOrd ? `${nOrd} đơn hàng xóm đang chờ` : 'Chưa có xuồng ai ghé') : 'Xuồng nhà mình đậu ở bến, chèo đi thăm vườn người ta được');
  h += UX.cta([lv >= ORD.lv ? UX.btn('gocho2', gh ? 'Xem đơn ghe chợ nổi' : `Đơn nhà bên${nOrd ? ' · ' + nOrd : ''}`, { g: !!(nOk || gh), img: ICON.cho }) : '']);
  h += UX.title('Đi ghé vườn') + `<div class="vcard"><img src="${ICON.xoai || ICON.cai}" alt=""><div><b>Vườn mẫu của Ngoại</b><span>Ngoại cho hái ${MAU.picks} món mỗi ngày${left < MAU.picks ? `, hôm nay còn ${left}` : ''}</span>${UX.pips(ICON.cai, left, MAU.picks)}</div><button class="btn g" data-a="gomau">Chèo qua</button></div>`;
  return h + nbHTML(); }
