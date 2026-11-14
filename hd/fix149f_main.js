/* ===== v149f — đồ quý: giống quý ===== */
const QUYS = { otvang: 'Ớt sừng vàng đó con. Hồi xưa bà cố trồng một bụi trước sân, trái chín vàng như nghệ, cay mà thơm lắm.', baptim: 'Bắp nếp tím nè con. Hồi nhỏ Ngoại hay luộc một nồi, nước ra tím như lá cẩm, cả xóm qua xin.', cachuavang: 'Cà chua bi vàng, ngọt như trái cây. Hồi đó má Ngoại để dành cho mấy đứa nhỏ ăn chơi.', khoquarung: 'Khổ qua rừng trái nhỏ xíu mà đắng thấu trời. Ông ngoại con nói đắng vậy mới mát gan.', mongtoitia: 'Mồng tơi tía, nấu canh nước ra tím hồng. Hồi con gái Ngoại còn lấy trái nó nhuộm móng tay.', khommat: 'Khóm mật, ruột vàng như mật ong. Giống này Ngoại tưởng mất luôn rồi, ai dè vườn mình còn giữ được.' };
if (EN){ for (const k in QUY) CROPS[k].name = QUY[k].name = QUY[k].en; Object.assign(QCL, { tot: 'rich soil', bon: 'fertilized soil', rom: 'straw mulch', am: 'well watered, never wilted', lua2: 'picked from the second crop on', mua: 'rainy season', kho: 'dry season', sang: 'picked in the morning', chieu: 'picked in the afternoon', thuan: 'a practiced hand' }); }
const quyQ = () => { const Q = ST.quy = ST.quy || {}; Q.n = Q.n || {}; Q.got = Q.got || {}; Q.hint = Q.hint || {}; Q.nm = Q.nm || {}; return Q; };
const quyHas = (k, x) => { const Q = ST.quy || {}; return ((Q.hint || {})[k] || '').includes(x[0]) || !!(Q.got || {})[k]; };
const quyLab = (q, x) => QCL[q[x]];
const quyHint = q => QCX.map(x => quyHas(q.k, x) ? quyLab(q, x) : '???').join(' · ');
function quyLearn(k, x){ const Q = quyQ(); if (quyHas(k, x)) return 0; Q.hint[k] = (Q.hint[k] || '') + x[0]; save(); return 1; }
const quyDonTxt = (q, x) => { const n = q.name.toLowerCase(), b = CROPS[q.base].name.toLowerCase(), l = quyLab(q, x); if (EN) return x === 'dat' ? `They say ${n} only shows up in ${b} beds with ${l}.` : x === 'cham' ? `Word is, to find ${n} the ${b} bed needs: ${l}.` : x === 'mua' ? `Growers say ${n} only comes in the ${l}.` : `Rumor has it ${n} must be ${l}.`; return x === 'dat' ? `Người ta đồn ${n} chỉ ra ở liếp ${b} ${l}.` : x === 'cham' ? `Nghe nói muốn gặp ${n} thì liếp ${b} phải ${l}.` : x === 'mua' ? `Dân vườn nói ${n} chỉ ra vô ${l}.` : `Nghe đồn ${n} phải ${l} mới gặp.`; };
function quyDon(){ const ks = Object.keys(QUY).filter(k => unlocked(QUY[k].base) && !(ST.quy && ST.quy.got && ST.quy.got[k]) && QCX.some(x => !quyHas(k, x))); if (!ks.length) return null;
  const ss = ks.filter(k => QUY[k].mua === muaSong()), k = pick(ss.length ? ss : ks), x = pick(QCX.filter(x => !quyHas(k, x))); quyLearn(k, x); return { k, x, q: 1, txt: quyDonTxt(QUY[k], x) }; }
function donAny(){ const a = []; try { if (cauOn()) a.push(donGive); } catch (e) {} if (quyOn()) a.push(quyDon); if (!a.length) return null; if (a.length === 2 && Math.random() < .5) a.reverse(); return a[0]() || (a[1] ? a[1]() : null); }
function quyGive(k, x, z){ const Q = quyQ(), q = QUY[k], first = !Q.got[k]; ST.inv[k] = (ST.inv[k] || 0) + 1; ST.seeds[k] = (ST.seeds[k] || 0) + 1; Q.got[k] = 1;
  try { sfx('lvl'); } catch (e) {} try { buzz(60); } catch (e) {} try { confettiAt(innerWidth / 2, innerHeight * .42, 36, 1.1); } catch (e) {}
  setTimeout(() => floatAt(x, CROPS[k].h * .6 + .45, z, L135('Trái lạ! +1 hạt ', 'Rare! +1 seed ') + q.name.toLowerCase(), '#F5D27A'), 450);
  if (first){ ST.xu += 300; setTimeout(() => { try { coinPop(L135('+300 xu · ', '+300 coins · ') + q.name, '#F5D27A'); } catch (e) {} hud(); }, 900); setTimeout(() => say(QUYS[k], 'vui', { now: true }), 1300); }
  else setTimeout(() => say(L135(`Lại ra ${q.name.toLowerCase()} nữa nè con. Để dành hạt mà gieo nghe.`, `Another ${q.name.toLowerCase()}, dear. Keep the seed for sowing.`), 'vui', { idle: true }), 1200);
  save(); hud(); }
function quyHarvest(id, p){ if (VISIT || !quyOn()) return; const k0 = p.crop, c = CROPS[k0], x = PV[id].cx, z = PV[id].cz;
  if (c.rare === 'quy'){ if (Math.random() < .25){ ST.seeds[k0] = (ST.seeds[k0] || 0) + 1; setTimeout(() => floatAt(x, c.h * .6 + .4, z, L135('+1 hạt ', '+1 seed ') + c.name.toLowerCase(), '#F5D27A'), 500); } return; }
  const k = QUYB[k0]; if (!k) return; const Q = quyQ(), q = QUY[k], miss = QCX.filter(m => !quyMet(q, p, m));
  if (!miss.length){ const n = Q.n[k] = (Q.n[k] || 0) + 1; if (Math.random() < .1 || n >= 6){ Q.n[k] = 0; quyGive(k, x, z); } }
  else if (miss.length === 1 && Q.nm[k] !== dayKey()){ Q.nm[k] = dayKey(); const m = miss[0]; quyLearn(k, m); setTimeout(() => say(L135(`Lứa ${c.name.toLowerCase()} này ngó lạ lạ mà chưa ra hẳn giống quý. Ngoại đoán còn thiếu: ${quyLab(q, m)}.`, `This ${c.name.toLowerCase()} crop looked a little odd, but not quite a rare one. Ngoại guesses it still needs: ${quyLab(q, m)}.`), 'vui', { idle: true }), 900); } }
let QTT = -9; function quyTick(t){ if (t - QTT < 5) return; QTT = t; if (!quyOn()) return; for (const P of PLOTS){ const p = ST.plots[P.id]; if (p && p.crop && QUYB[p.crop] && PV[P.id]){ try { buildCrop(P.id); } catch (e) {} } } }
{ const hue = async (src, lo, hi, H2, ks, kl) => { const im = new Image(); im.src = src; await im.decode(); const c = document.createElement('canvas'); c.width = c.height = im.naturalWidth || 160; const x = c.getContext('2d'); x.drawImage(im, 0, 0, c.width, c.height); const d = x.getImageData(0, 0, c.width, c.height), a = d.data, col = new T.Color(), o = {};
    for (let i = 0; i < a.length; i += 4){ if (!a[i + 3]) continue; col.setRGB(a[i] / 255, a[i + 1] / 255, a[i + 2] / 255); col.getHSL(o); if (o.s < .22 || o.h < lo || o.h > hi) continue; col.setHSL(H2 + (o.h - (lo + hi) / 2) * .25, Math.min(1, o.s * ks), o.l * kl); a[i] = col.r * 255; a[i + 1] = col.g * 255; a[i + 2] = col.b * 255; }
    x.putImageData(d, 0, 0); return c.toDataURL(); };
  (async () => { try { ICON.mongtoitia = await hue(ICON.mongtoi, .17, .47, .81, .8, .82); } catch (e) {} try { if (ICON.baptim === ICON.bap) ICON.baptim = await hue(ICON.bap, .09, .17, .78, .55, .6); } catch (e) {} })(); }
/* ===== trang Đồ quý miệt vườn (11 ô) ===== */
for (const k in QUY) QUY[k].k = k;
const QGI = Object.keys(QUY), QCA = ['cadua', 'hu', 'rodauvang', 'locbong', 'caho'], QTAG = ['Giống quý', '#F2C230', '#4A2F1E'];
const bayS = () => { const B = ST.bay = ST.bay || {}; B.stamp = B.stamp || {}; B.th = B.th || {}; B.set = B.set || {}; return B; };
const quyGot = k => QUY[k] ? !!((ST.quy || {}).got || {})[k] : !!((ST.fishLog || {})[k] || {}).n;
const quySt = k => !!(((ST.bay || {}).stamp || {})[k]);
function pgQuy(part){ const ng = QGI.filter(quyGot).length, nc = QCA.filter(quyGot).length, sg = QGI.filter(quySt).length, sc = QCA.filter(quySt).length, set = (ST.bay || {}).set || {}; let h = '';
  const dau = k => quySt(k) ? '<small class="qst">Đã ghi sổ</small>' : '';
  if (part !== 2){ h += `<div class="bkhn" style="color:#9A6A14">${L135('Đồ quý miệt vườn · đã gặp ', 'Rare finds · found ')}${ng + nc}/11</div>` + UX.title('Giống quý', ng + '/6') + '<div class="fgrid">' + QGI.map(k => { const q = QUY[k], b = CROPS[q.base];
      return quyGot(k) ? `<div class="fcd" style="--tc:${QTAG[1]};--tt:${QTAG[2]}"><img src="${ICON[k]}" alt=""><b>${CROPS[k].name}</b><small class="ftag">${QTAG[0]}</small><span>${quyHint(q)}</span>${dau(k)}<i>${QUYS[k]}</i></div>`
        : `<div class="fcd no"><img src="${ICON[k]}" alt=""><b>???</b><small class="ftag" style="background:${QTAG[1]};color:${QTAG[2]}">${QTAG[0]}</small><span>${unlocked(q.base) ? L135('Ra từ liếp ', 'Comes from a bed of ') + b.name.toLowerCase() : 'Chưa có giống gốc'}</span><span>${quyHint(q)}</span></div>`; }).join('') + '</div>'; }
  if (part !== 1){ h += UX.title('Cá quý', nc + '/5') + '<div class="fgrid">' + QCA.map(k => { const f = FISHK[k], T0 = FTIER[f.tier];
      return quyGot(k) ? `<div class="fcd" style="--tc:${T0[1]};--tt:${T0[2]}"><img src="${ICON[k]}" alt=""><b>${nm135(f.name)}</b><small class="ftag">${T0[0]}</small><span>${fHint(f, 1)}</span>${dau(k)}<i>${f.line}</i></div>`
        : `<div class="fcd no"><img src="${ICON[k]}" alt=""><b>???</b><small class="ftag" style="background:${T0[1]};color:${T0[2]}">${T0[0]}</small><span>${cauOn() ? fHint(f) : 'Chưa ra bến câu'}</span></div>`; }).join('') + '</div>'
    + UX.title('Ông Bảy Kiếng tặng') + `<div class="qset${set.giong ? ' ok' : ''}"><img src="${ICON.otvang}" alt=""><div><b>Giàn trái giống trước hiên</b><span>${set.giong ? 'Đã dựng trước hiên nhà' : L135('Giao đủ 6 giống quý cho ông Bảy · ', 'Hand all 6 rare crops to Uncle Bảy · ') + sg + '/6'}</span></div></div>`
    + `<div class="qset${set.ca ? ' ok' : ''}"><img src="${ICON.locbong}" alt=""><div><b>Bảng Tay câu ở bến</b><span>${set.ca ? 'Đã treo ở bến nhà' : L135('Giao đủ 5 cá quý cho ông Bảy · ', 'Hand all 5 rare fish to Uncle Bảy · ') + sc + '/5'}</span></div></div>`; }
  return h; }
/*QUY_END*/
