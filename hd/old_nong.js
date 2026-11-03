/* ===== nong phơi (cấp 7): 4 cái nong tre trên giá thấp, đặt ở một ô bãi hông nhà; phơi theo nắng giờ thật ===== */
const NONG = { lv: 7, buy: 80, n: 4, sun: [6, 18], first: 20 };
const sunAt = ms => { const h = new Date(ms).getHours(); return h >= NONG.sun[0] && h < NONG.sun[1]; };
if (!ST.nong) ST.nong = { own: 0, at: null, trays: [null, null, null, null], done: 0, made: {} };
const nongOn = () => (ST.lv || 1) >= NONG.lv;
function nongSim(dt, ms = Date.now()){ const N = ST.nong; if (!N || !N.own) return; const sun = sunAt(ms); for (const t of N.trays) if (t && t.t > 0 && (sun || t.fast)) t.t = Math.max(0, t.t - dt); }
const phoiName = k => k === 'lucbinh' ? 'lục bình' : (GD(k) ? GD(k).name.toLowerCase() : k);
const phoiNeed = k => Object.entries(PHOI[k].in).map(([ik, n]) => `${n} ${phoiName(ik)}`).join(' + ');
const phoiCan = k => Object.entries(PHOI[k].in).every(([ik, n]) => (ik === 'lucbinh' ? 0 : has(ik)) >= n);
const freeCell = () => { const c = PLOTS.find(P => P.bai && locked(P) && ST.nong.at !== P.id); return c ? c.id : null; };
const nong = {
  buy(at){ const N = ST.nong; if (N.own || !nongOn()) return; at = at || freeCell(); if (!at) return say('Bãi hông nhà hết ô cỏ trống rồi con. San bớt một liếp trống ra mới có chỗ để nong.', 'dan', { now: true }); if (ST.xu < NONG.buy) return say(`Bộ nong phơi ${NONG.buy} xu, con còn thiếu ${NONG.buy - ST.xu} xu.`, 'dan');
    ST.xu -= NONG.buy; N.own = 1; N.at = at; coinPop(`-${NONG.buy} xu · bộ nong phơi`, '#F08A6E'); sfx('up'); save(); refreshPlot(at); hud(); nongPuff(at);
    say('Bộ nong tre này Ngoại mua của ông Ba đan đó. Phơi ớt, phơi chuối, nắng lên là khô. Mẻ đầu Ngoại phơi giùm cho mau.', 'vui', { now: true }); camTo(new T.Vector3(PV[at].cx, .3, PV[at].cz), Math.max(cam.zoom, DEFZ() * 1.2)); },
  place(id){ const N = ST.nong, P = PL[id]; if (!N.own || !P || !P.bai || !locked(P)) return false; const old = N.at; N.at = id; save(); if (old) refreshPlot(old); refreshPlot(id); nongPuff(id); sfx('pop'); buzz(12); return true; },
  put(i, k){ const N = ST.nong, d = PHOI[k]; if (!d || N.trays[i] || (ST.lv || 1) < d.lv || !phoiCan(k)) return; for (const [ik, n] of Object.entries(d.in)) STORE(ik)[ik] -= n;
    const fast = !N.done && !N.trays.some(t => t && t.fast); N.trays[i] = { k, t: fast ? NONG.first : d.t, T: fast ? NONG.first : d.t, fast }; sfx('pick'); buzz(10); gainXP(1); save(); hud();
    if (!fast && !sunAt(Date.now())) say('Trời tối rồi, nong nằm yên đó, sáng mai nắng lên là khô tiếp. Không hư đâu con.', 'dan', { now: true }); },
  take(i){ const N = ST.nong, t = N.trays[i]; if (!t || t.t > 0) return false; if (gbUsed() >= GB_CAP){ say('Gác bếp hết chỗ rồi con. Đem đồ khô ra chợ bán bớt nghe.', 'lo', { now: true }); return false; }
    STORE(t.k)[t.k] = (STORE(t.k)[t.k] || 0) + 1; N.trays[i] = null; N.done = (N.done || 0) + 1; N.made[t.k] = 1; const P = PV[N.at]; if (P){ flyTo(ICON[t.k], P.cx, .3, P.cz); floatAt(P.cx, .6, P.cz, `+1 ${PHOI[t.k].unit} ${PHOI[t.k].name.toLowerCase()}`); }
    sfx('pop'); gainXP(Math.round(PHOI[t.k].sell / 15)); save(); hud(); return true; },
  takeAll(){ let n = 0; ST.nong.trays.forEach((t, i) => { if (t && t.t <= 0 && nong.take(i)) n++; }); if (n) sayOnce('nong1', 'Ớt khô rồi đó con, Ngoại cất trên gác bếp. Hàng xóm hay hỏi mua ớt khô về làm muối ớt lắm.', 'vui'); return n; } };
function nongPuff(id){ const [u0, v0, u1, v1] = PL[id].b; for (let i = 0; i < 12; i++) puff('leaf', R(u0, u1), .12, R(v0, v1), 1, pick(['#C9A66B', '#E3C46A', '#86B06A']), .6); }
function nongHTML(){ const N = ST.nong, sun = sunAt(Date.now()); let h = `<div class="meta">Phơi bằng nắng thật, từ ${NONG.sun[0]} giờ sáng tới ${NONG.sun[1]} giờ chiều · ${sun ? 'đang có nắng' : 'trời tối, nong nằm yên chờ nắng'}</div>`;
  N.trays.forEach((t, i) => { if (!t){ h += `<div class="sub">Nong ${i + 1} · trống</div><div class="acts">` + Object.keys(PHOI).map(k => { const d = PHOI[k], lk = (ST.lv || 1) < d.lv, can = !lk && phoiCan(k); return `<button class="btn${can ? ' g' : ''}" data-a="nput" data-k="${k}" data-n="${i}" ${can ? '' : 'disabled'}>${d.name}<small>${lk ? `tới cấp ${d.lv}` : phoiNeed(k)}</small></button>`; }).join('') + '</div>'; return; }
    const d = PHOI[t.k], done = t.t <= 0; h += `<div class="srow"><div class="sic"><img src="${ICON[t.k]}" alt=""></div><div class="sn"><b>Nong ${i + 1} · ${d.name}</b>${done ? '<span class="mkh">Khô rồi, cất lên gác bếp</span>' : `${bar(1 - t.t / t.T, '#E9B23A')}<span class="mkh">còn ${fmtT(t.t)} nắng${t.fast ? ' · mẻ đầu Ngoại phơi giùm' : ''}</span>`}</div><span></span>${done ? `<button class="btn g sall" data-a="ntake" data-n="${i}">Lấy</button>` : '<span></span>'}</div>`; });
  h += `<div class="note">Đồ khô cất trên gác bếp (${gbUsed()} / ${GB_CAP} chỗ), bán ở chợ hay giao hàng xóm. Trời tối thì nong nằm yên, không hư.</div><div class="acts"><button class="btn" data-a="nmove">Dời nong qua ô khác</button></div>`; return h; }
/* Sửa vườn: chạm ô bãi để đắp liếp, san lại thành cỏ, đặt hay dời nong */
function suaTitle(id){ const P = PL[id], p = ST.plots[id]; return ST.nong.own && ST.nong.at === id ? 'Nong phơi' : locked(P) ? 'Bãi cỏ' : p.crop ? CROPS[p.crop].name : 'Liếp trống'; }
function suaHTML(id){ const P = PL[id], p = ST.plots[id], N = ST.nong; let h = '';
  if (N.own && N.at === id) return h + `<div class="note">Bộ nong phơi đang đặt ở ô này.</div><div class="acts"><button class="btn g" data-a="nopen">Mở nong</button><button class="btn" data-a="nmove">Dời qua ô khác</button></div>`;
  if (locked(P)){ h += `<div class="bedc"><img src="${ICON.cuoc || UIC.sickle}" alt=""><span class="ar">›</span><img src="${UIC.seedbag}" alt=""><div><b>Cuốc cỏ, đắp liếp mới</b><span>Đắp liếp ô này rồi gieo như liếp ngoài vườn.</span></div><span class="cst${ST.xu < BAI.cost ? ' poor' : ''}">${stI('coin', BAI.cost)}</span></div>`;
    h += `<div class="acts"><button class="btn g" data-a="openbed" ${ST.xu < BAI.cost ? 'disabled' : ''}>Đắp liếp · ${BAI.cost} xu</button>`;
    if (nongOn()) h += N.own ? `<button class="btn" data-a="nhere">Dời nong về ô này</button>` : `<button class="btn" data-a="nbuy" ${ST.xu < NONG.buy ? 'disabled' : ''}>Đặt bộ nong phơi ở đây · ${NONG.buy} xu</button>`;
    return h + '</div>'; }
  if (p.crop) return h + `<div class="note">Liếp này đang trồng ${CROPS[p.crop].name.toLowerCase()}. Hái xong, liếp trống rồi mới san lại được con.</div>`;
  return h + `<div class="note">Liếp đang trống. San lại thành bãi cỏ thì trả chỗ cho nong hay để đắp chỗ khác, muốn đắp lại thì tốn ${BAI.cost} xu như mới.</div><div class="acts"><button class="btn" data-a="bsan">San lại thành cỏ</button></div>`; }
function baiSan(id){ const P = PL[id], p = ST.plots[id]; if (!P || !P.bai || locked(P) || p.crop) return; ST.open = ST.open.filter(i => i !== id); ST.plots[id] = pl0(null); PV[id].key = null; refreshPlot(id);
  const [u0, v0, u1, v1] = P.b; for (let i = 0; i < 14; i++) puff('leaf', R(u0, u1), .12, R(v0, v1), 1, pick(['#6E9A4A', '#8fb85a']), .6); sfx('pick'); save(); hud(); }
function suaOn(on, move){ if (on && (VISIT || !baiOn())) return; SUA = on ? { move: move || null } : null; document.body.classList.toggle('sua', !!SUA); const b = $('#suaBar'); if (b) b.hidden = !SUA; suaTx();
  for (const P of PLOTS) if (P.bai) refreshPlot(P.id); if (SUA){ closeSheet(); camTo(new T.Vector3(BAIC.x + .4, .3, BAIC.z + .3), Math.max(cam.zoom, DEFZ() * 1.15)); sayOnce('sua1', 'Bãi hông nhà con muốn đắp liếp chỗ nào, để cỏ chỗ nào, đặt nong chỗ nào là tùy con. Chạm từng ô mà sửa nghe.', 'vui'); } }
function suaTx(){ const t = $('#suaTx'); if (t && SUA) t.textContent = SUA.move ? 'Chạm một ô cỏ để đặt nong' : 'Chạm từng ô: đắp liếp, san cỏ, đặt nong'; }
// mô hình bộ nong: giá tre thấp, 4 nong tròn đan, đồ phơi đổi màu dần theo độ khô
const NONGV = (() => { const root = DYN(G(0, 0, 0)), pr = ROOT; ROOT = root; const xs = [-.19, .19], zs = [-.16, .16];
  for (const z of zs){ M(cyl(.013, .013, .76, 5), C.bamboo, 0, .1, z, { p: root, r: [0, 0, Math.PI / 2] }); for (const x of [-.34, .34]) M(cyl(.012, .014, .1, 5), '#8A5D3B', x, .05, z, { p: root }); }
  const trays = [], slots = []; for (const z of zs) for (const x of xs){ const g = G(x, .115, z, R(0, 6), root); M(new T.CylinderGeometry(.17, .16, .02, 14), '#C9A66B', 0, 0, 0, { p: g }); M(new T.TorusGeometry(.17, .012, 4, 16), '#A07A45', 0, .012, 0, { p: g, r: [Math.PI / 2, 0, 0] });
    for (const r of [.06, .115]) M(new T.TorusGeometry(r, .004, 3, 14), '#B48C55', 0, .011, 0, { p: g, r: [Math.PI / 2, 0, 0], cast: false }); trays.push(g); slots.push({ g: G(0, .012, 0, 0, g), key: null }); }
  ROOT = pr; const b = bubbleK('h'); return { root, trays, slots, b, hb: b.children.find(c => c.userData.bub) }; })();
function nongFill(sl, t){ const key = t ? t.k + ':' + Math.min(3, Math.floor((1 - t.t / t.T) * 4)) : '-'; if (key === sl.key) return; sl.key = key; for (const m of [...sl.g.children]) sl.g.remove(m); if (!t) return;
  const dry = Math.min(1, 1 - t.t / t.T), pr = ROOT; ROOT = sl.g; const ps = sd; sd = 77 + sl.g.id;
  const mix = (a, b) => '#' + new T.Color(a).lerp(new T.Color(b), dry).getHexString();
  if (t.k === 'otkho') for (let k = 0; k < 14; k++){ const a = rnd() * 6.28, r = Math.sqrt(rnd()) * .12; M(new T.CapsuleGeometry(.011, .045 - dry * .01, 2, 5), mix('#E0402A', '#8E2A1C'), Math.cos(a) * r, .012, Math.sin(a) * r, { r: [Math.PI / 2, R(0, 3), 0], cast: false }); }
  else if (t.k === 'chuoiphoi') for (let k = 0; k < 5; k++){ const a = k / 5 * 6.28; M(sph(.04, 6, 4), mix('#E9C96A', '#8A5A2E'), Math.cos(a) * .08, .01, Math.sin(a) * .08, { s: [1.6, .35 - dry * .1, .8], r: [0, -a, 0], cast: false }); }
  else for (let k = 0; k < 10; k++) M(box(R(.16, .24), .008, .016), mix('#6E9F57', '#B8A070'), R(-.06, .06), .008 + k * .002, R(-.08, .08), { r: [0, R(0, 3), 0], cast: false });
  sd = ps; ROOT = pr; }
function nongTick(t){ const N = ST.nong, on = !!(N && N.own && N.at && PV[N.at] && baiOn()); NONGV.root.visible = on; NONGV.b.visible = false; if (!on) return; const v = PV[N.at]; NONGV.root.position.set(v.cx, 0, v.cz);
  N.trays.forEach((tr, i) => nongFill(NONGV.slots[i], tr)); const done = N.trays.find(tr => tr && tr.t <= 0);
  if (done){ const b = NONGV.b; b.visible = true; try { bubIcon(b, ICON[done.k]); } catch (e) {} b.quaternion.copy(cam.quaternion); b.position.set(v.cx, .62 + Math.sin(t * 2) * .035, v.cz); b.scale.setScalar(.85 * BUBS * (1 + .07 * Math.abs(Math.sin(t * 3)))); } }
function nongHit(cx, cy){ if (!NONGV.b.visible) return false; ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); return ray.intersectObject(NONGV.hb, false).length > 0; }
