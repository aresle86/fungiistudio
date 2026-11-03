/* Sửa vườn: chạm ô bãi để đắp liếp, san lại thành cỏ, đặt hay dời đồ (nong, khạp, hố ủ) */
const zoneName = P => P.zone === 'song' ? 'Đất bồi mé sông' : 'Bãi cỏ';
function suaTitle(id){ const P = PL[id], p = ST.plots[id], ok = objAt(id); return ok ? OBJD[ok].title : locked(P) ? zoneName(P) : p.crop ? CROPS[p.crop].name : 'Liếp trống'; }
function suaHTML(id){ const P = PL[id], p = ST.plots[id], ok = objAt(id), cost = P.cost || BAI.cost; let h = '';
  if (ok) return h + `<div class="note">${OBJD[ok].title} đang đặt ở ô này.</div><div class="acts"><button class="btn g" data-a="oopen" data-k="${ok}">Mở ${OBJD[ok].name}</button>${moveBtn(ok)}</div>`;
  if (locked(P)){ h += `<div class="bedc"><img src="${ICON.cuoc || UIC.sickle}" alt=""><span class="ar">›</span><img src="${UIC.seedbag}" alt=""><div><b>${P.zone === 'song' ? 'Lên liếp đất bồi' : 'Cuốc cỏ, đắp liếp mới'}</b><span>${P.zone === 'song' ? 'Đất phù sa mé sông màu mỡ, đắp xong là đất tốt sẵn.' : 'Đắp liếp ô này rồi gieo như liếp ngoài vườn.'}</span></div><span class="cst${ST.xu < cost ? ' poor' : ''}">${stI('coin', cost)}</span></div>`;
    h += `<div class="acts"><button class="btn g" data-a="openbed" ${ST.xu < cost ? 'disabled' : ''}>Đắp liếp · ${cost} xu</button>`;
    for (const k of OBJK){ if (!objOn(k)) continue; const O = ST[k], D = OBJD[k]; h += O.own ? `<button class="btn" data-a="ohere" data-k="${k}">Dời ${D.name} về đây</button>` : `<button class="btn" data-a="obuy" data-k="${k}" ${ST.xu < D.buy ? 'disabled' : ''}>Đặt ${D.name} ở đây · ${D.buy} xu</button>`; }
    return h + '</div>'; }
  if (p.crop) return h + `<div class="note">Liếp này đang trồng ${CROPS[p.crop].name.toLowerCase()}. Hái xong, liếp trống rồi mới san lại được con.</div>`;
  return h + `<div class="note">Liếp đang trống. San lại thành cỏ thì có chỗ đặt đồ hay để đắp chỗ khác, muốn đắp lại thì tốn ${cost} xu như mới.</div><div class="acts"><button class="btn" data-a="bsan">San lại thành cỏ</button></div>`; }
function baiSan(id){ const P = PL[id], p = ST.plots[id]; if (!P || !P.bai || locked(P) || p.crop) return; ST.open = ST.open.filter(i => i !== id); ST.plots[id] = pl0(null); PV[id].key = null; refreshPlot(id);
  const [u0, v0, u1, v1] = P.b; for (let i = 0; i < 14; i++) puff('leaf', R(u0, u1), .12, R(v0, v1), 1, pick(['#6E9A4A', '#8fb85a']), .6); sfx('pick'); save(); hud(); }
function suaOn(on, move){ if (on && (VISIT || !baiOn())) return; SUA = on ? { move: move || null } : null; document.body.classList.toggle('sua', !!SUA); const b = $('#suaBar'); if (b) b.hidden = !SUA; suaTx();
  for (const P of PLOTS) if (P.bai) refreshPlot(P.id); if (SUA){ closeSheet(); const O = move && ST[move] && PV[ST[move].at]; camTo(O ? new T.Vector3(O.cx, .3, O.cz) : new T.Vector3(BAIC.x + .4, .3, BAIC.z + .3), Math.max(cam.zoom, DEFZ() * 1.15)); sayOnce('sua1', 'Bãi hông nhà con muốn đắp liếp chỗ nào, để cỏ chỗ nào, đặt đồ chỗ nào là tùy con. Chạm từng ô mà sửa nghe.', 'vui'); } }
function suaTx(){ const t = $('#suaTx'); if (t && SUA) t.textContent = SUA.move ? `Chạm một ô cỏ để đặt ${OBJD[SUA.move].name}` : 'Chạm từng ô: đắp liếp, san cỏ, đặt đồ'; }
