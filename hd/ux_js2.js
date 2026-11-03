/* --- khạp muối --- */
function khapHTML(){ const K = ST.khap; if (SHEET && SHEET.pick != null) return UX.pick('kput', SHEET.pick, MUOI, 'Khạp');
  const done = K.jars.filter(j => j && j.t <= 0), run = K.jars.filter(j => j && j.t > 0); let h = '';
  if (done.length) h += UX.hero(ICON[done[0].k], `${done.length} khạp thấm muối rồi`, 'Vớt ra cất lên gác bếp nghe con', 'go');
  else if (run.length){ const t = run.reduce((a, b) => a.t < b.t ? a : b); h += UX.hero(ICON[t.k], `Đang muối ${MUOI[t.k].name.toLowerCase()}`, `Còn ${fmtT(t.t)} là ăn được`, '', [1 - t.t / t.T, '#86B06A']); }
  else h += UX.hero(ICON.khap, 'Hai khạp đang trống', 'Chạm khạp trống để muối dưa hay hột vịt');
  h += UX.cta([done.length ? UX.btn('ktakeall', 'Vớt ra hết', { g: 1, img: ICON[done[0].k] }) : '']);
  h += '<div class="slots">' + K.jars.map((j, i) => UX.slot(i, j, MUOI, 'kpick', 'ktake', 'Khạp', 'Thấm rồi · chạm vớt')).join('') + '</div>';
  h += `<div class="uxs" style="margin-top:10px">${UX.card('Muối hột', `${has('muoi')} <small>bịch</small>`, '', has('muoi') ? '' : 'warn')}${UX.card('Gác bếp', `${gbUsed()}/${GB_CAP} <small>chỗ</small>`, UX.mbar(gbUsed() / GB_CAP, '#C9A66B'))}</div>`;
  if (!has('muoi')) h += UX.cta([UX.btn('gocho3', 'Ra chợ mua muối', { img: ICON.muoi, sub: `${MUOI_PRICE} xu một bịch` })]);
  return h + UX.more('Cách muối', `Muối xong để bao lâu cũng được, không hư. Dưa cải chua ăn với thịt kho, hột vịt muối ăn cháo trắng.<div class="acts">${moveBtn('khap')}</div>`); }
/* --- lò sấy --- */
function sayHTML(){ const L = ST.say; if (SHEET && SHEET.pick != null) return UX.pick('sput', SHEET.pick, SAYR, 'Khay');
  const done = L.trays.filter(t => t && t.t <= 0), run = L.trays.filter(t => t && t.t > 0), cui = has('cui'); let h = '';
  if (done.length) h += UX.hero(ICON[done[0].k], `${done.length} khay sấy xong`, 'Lấy cất lên gác bếp nghe con', 'go');
  else if (run.length){ const t = run.reduce((a, b) => a.t < b.t ? a : b); h += UX.hero(ICON[t.k], `Đang sấy ${SAYR[t.k].name.toLowerCase()}`, `Còn ${fmtT(t.t)}, lò chạy cả đêm`, '', [1 - t.t / t.T, '#E9823A']); }
  else if (!cui) h += UX.hero(ICON.cui, 'Hết củi rồi', 'Mỗi mẻ sấy cần một bó củi', 'warn');
  else h += UX.hero(ICON.say, 'Lò đang nguội', 'Chạm khay trống để sấy mứt, trái cây');
  h += UX.cta([done.length ? UX.btn('stakeall', 'Lấy hết', { g: 1, img: ICON[done[0].k] }) : '', !cui ? UX.btn('gocho3', 'Mua củi', { img: ICON.cui, sub: '3 xu một bó' }) : '']);
  h += '<div class="slots">' + L.trays.map((t, i) => UX.slot(i, t, SAYR, 'spick', 'stake', 'Khay', 'Sấy xong · chạm lấy')).join('') + '</div>';
  h += `<div class="uxs" style="margin-top:10px">${UX.card('Củi', `${cui} <small>bó · 1 bó một mẻ</small>`, '', cui ? '' : 'warn')}${UX.card('Đường cát', `${has('duong')} <small>bịch</small>`)}</div>`;
  return h + UX.more('Cách sấy', `Lò sấy chạy cả đêm, không cần nắng. Ớt, chuối sấy lò nhanh gấp đôi phơi nong. Đường cát mua ở chợ, ${DUONG_PRICE} xu một bịch.<div class="acts"><button class="btn" data-a="gocho3">Ra chợ</button>${moveBtn('say')}</div>`); }
/* --- hố ủ phân --- */
function hoHTML(){ const H = ST.ho, w = hoWorst(); let h = '';
  if (H.bags) h += UX.hero(ICON.phan, `Có ${H.bags} bao phân`, w ? `Bón cho ${w.name.toLowerCase()} đang đất mệt nhất` : 'Liếp nào đất cũng tốt, để dành bữa sau', 'go');
  else if (H.t > 0) h += UX.hero(ICON.ho, 'Đang ủ phân', `Còn ${fmtT(H.t)} ra một bao`, '', [1 - H.t / (H.done ? HO.t : HO.first), '#8A5D3B']);
  else h += UX.hero(ICON.ho, `Cần thêm ${Math.max(0, HO.need - H.mat)} phần đồ ủ`, 'Quét lá, vớt lục bình, bỏ rau dư vô hố', H.mat ? '' : 'warn');
  h += UX.cta([H.bags ? UX.btn('hobon', 'Bón liếp đất mệt', { g: 1, img: ICON.phan, dis: !w, sub: w ? w.name.toLowerCase() : '' }) : '', UX.btn('horau', 'Bỏ 1 rau dư', { img: ICON.cai, dis: !hoRoom() })]);
  h += '<div class="uxs">' + UX.card('Đồ ủ trong hố', `${H.mat}/${HO.need} <small>phần</small>`, UX.pips(ICON.la || ICON.lucbinh, Math.min(H.mat, HO.need), HO.need)) + UX.card('Phân đã ủ', `${H.bags || 0}/${HO.max} <small>bao</small>`, UX.pips(ICON.phan, H.bags || 0, HO.max), H.bags ? 'go' : '') + '</div>';
  return h + UX.more('Cách ủ phân', `Quét lá rụng +2 phần, vớt lục bình +1 phần (vịt no rồi thì lục bình vô hố), rau dư trong kho +1 phần. Đủ ${HO.need} phần thì Ngoại ủ, một ngày ra một bao. Bón một bao: đất liếp +0,3.<div class="acts">${moveBtn('ho')}</div>`); }
/* --- lò ấp vịt --- */
function loHTML(){ const L = ST.lo, egg = ST.inv.trungvit || 0, cui = has('cui'), room = vitCap() - ST.vit.n; let h = '';
  if (L.on && L.t <= 0) h += UX.hero(ICON.vitcon, `${L.hatch} vịt con nở rồi!`, room >= L.hatch ? 'Bắt thả chung với đàn nghe con' : `Chuồng còn ${room} chỗ, dư thì Ngoại bán ${LO.sellDuck} xu một con`, 'go');
  else if (L.on) h += UX.hero(ICON.trungvit, `Đang ấp ${LO.eggs} trứng`, `Còn ${fmtT(L.t)} là nở`, '', [1 - L.t / (L.T || LO.t), '#E9B23A']);
  else h += UX.hero(ICON.vitcon, 'Lò ấp đang trống', egg >= LO.eggs && cui >= LO.cui ? `Đủ ${LO.eggs} trứng vịt với củi rồi, ấp liền được` : `Cần ${LO.eggs} trứng vịt và ${LO.cui} bó củi`, egg >= LO.eggs && cui >= LO.cui ? '' : 'warn');
  h += UX.cta([L.on && L.t <= 0 ? UX.btn('lohatch', 'Bắt vịt con', { g: 1, img: ICON.vitcon }) : !L.on ? UX.btn('loput', `Ấp ${LO.eggs} trứng vịt`, { g: 1, img: ICON.trungvit, dis: egg < LO.eggs || cui < LO.cui }) : '']);
  h += '<div class="uxs">' + UX.card('Trứng vịt', `${egg}/${LO.eggs}`, UX.pips(ICON.trungvit, Math.min(egg, LO.eggs), LO.eggs), egg >= LO.eggs ? 'go' : '') + UX.card('Chuồng vịt', `${ST.vit.n}/${vitCap()} <small>con</small>`, UX.pips(ICON.vitmai, ST.vit.n, vitCap(), 8), room ? '' : 'warn') + '</div>';
  return h + UX.more('Cách ấp', `Vùi ${LO.eggs} trứng vịt trong trấu, hun một bó củi cho ấm, chừng ${LO.t / 3600} tiếng là nở. Vịt con vô chuồng chung với đàn, chuồng hết chỗ thì Ngoại bán cho hàng xóm.`); }
/* --- hiên nhà đan giỏ --- */
function gioHTML(){ const g = ST.gio, left = g.d === dayKey() ? GIO.day - g.n : GIO.day, kho = has('lucbinhkho'); let h = '';
  if (g.on && g.t <= 0) h += UX.hero(ICON.gio, 'Ngoại đan xong một giỏ', 'Lấy cất lên gác bếp nghe con', 'go');
  else if (g.on) h += UX.hero(ICON.gio, 'Ngoại đang đan giỏ', `Còn ${fmtT(g.t)} là xong`, '', [1 - g.t / (g.T || GIO.t), '#B8A070']);
  else if (left <= 0) h += UX.hero(ICON.gio, 'Hôm nay đan đủ rồi', 'Mai Ngoại đan tiếp nghe con', '');
  else h += UX.hero(ICON.lucbinhkho, kho >= GIO.need ? 'Đủ lục bình khô rồi' : `Cần ${GIO.need} bó lục bình khô`, kho >= GIO.need ? 'Nhờ Ngoại đan một giỏ nghe' : 'Vớt lục bình rồi đem phơi nong', kho >= GIO.need ? '' : 'warn');
  h += UX.cta([g.on && g.t <= 0 ? UX.btn('giotake', 'Lấy giỏ', { g: 1, img: ICON.gio }) : !g.on ? UX.btn('gioput', 'Nhờ Ngoại đan một giỏ', { g: 1, img: ICON.gio, dis: left <= 0 || kho < GIO.need }) : '']);
  h += '<div class="uxs">' + UX.card('Lục bình khô', `${kho}/${GIO.need} <small>bó</small>`, UX.pips(ICON.lucbinhkho, Math.min(kho, GIO.need), GIO.need), kho >= GIO.need ? 'go' : '') + UX.card('Hôm nay', `${GIO.day - left}/${GIO.day} <small>giỏ</small>`, UX.pips(ICON.gio, GIO.day - left, GIO.day)) + '</div>';
  return h + UX.more('Cách đan giỏ', `Lục bình vớt dưới mương, sông cất lên gác bếp (khi vịt no). Phơi nong 5 lục bình ra 5 bó khô. Ngoại đan ${GIO.need} bó một giỏ, mỗi ngày tối đa ${GIO.day} giỏ.`); }
/* --- ô bãi: đắp liếp, đặt đồ --- */
function suaHTML(id){ const P = PL[id], p = ST.plots[id], ok = objAt(id), cost = P.cost || BAI.cost; let h = '';
  if (ok){ const D = OBJD[ok]; return UX.hero(ICON[ok], D.title, 'Đang đặt ở ô này') + UX.cta([UX.btn('oopen', `Mở ${D.name}`, { g: 1, k: ok, img: ICON[ok] }), `<button class="btn" data-a="omove" data-k="${ok}"><span>Dời qua ô khác</span></button>`]); }
  if (locked(P)){ h += UX.hero(ICON.cuoc || UIC.sickle, zoneName(P), P.zone === 'song' ? 'Đất phù sa màu mỡ, đắp xong đất tốt sẵn' : 'Đắp liếp để trồng, hay đặt đồ ở ô này');
    h += UX.cta([UX.btn('openbed', 'Đắp liếp', { g: 1, img: UIC.seedbag, dis: ST.xu < cost, sub: `${cost} xu` })]);
    const objs = OBJK.filter(objOn); if (objs.length) h += UX.title('Hay đặt đồ ở đây') + '<div class="upg">' + objs.map(k => { const O = ST[k], D = OBJD[k]; return O.own ? UX.upc('ohere', ICON[k], `Dời ${D.name} về đây`, null, { k, why: 'đang ở ô khác' }) : UX.upc('obuy', ICON[k], D.title, D.buy, { k, dis: ST.xu < D.buy }); }).join('') + '</div>';
    return h; }
  if (p.crop) return UX.hero(ICON[p.crop], CROPS[p.crop].name, 'Hái xong, liếp trống rồi mới san lại được con');
  return UX.hero(UIC.seedbag, 'Liếp trống', 'Gieo hạt, hay san lại thành cỏ để đặt đồ') + UX.cta([UX.btn('pickseed', 'Chọn hạt để gieo', { g: 1, img: UIC.seedbag }), `<button class="btn" data-a="bsan"><span>San thành cỏ</span></button>`]); }
/* --- bếp: thêm dòng trạng thái trên cùng --- */
function bepHTML(){ const B = ST.bep; if ((ST.lv || 1) < BEP.lv || !B.lit) return bepHTML0(); const done = B.pots.filter(p => p && p.t <= 0), run = B.pots.filter(p => p && p.t > 0); let h = '';
  if (done.length) h += UX.hero(ICON[done[0].k], `${done.length} nồi chín rồi`, 'Lấy cất lên gác bếp nghe con', 'go');
  else if (run.length){ const t = run.reduce((a, b) => a.t < b.t ? a : b); h += UX.hero(ICON[t.k], `Đang nấu ${DISH[t.k].name.toLowerCase()}`, `Còn ${bepT(t.t)} là chín`, '', [1 - t.t / DISH[t.k].t, '#E9A23A']); }
  else h += UX.hero(ICON.cui, 'Bếp đang rảnh', `Chọn món nấu bên dưới · củi còn ${has('cui')} bó`, has('cui') ? '' : 'warn');
  return h + bepHTML0(); }
