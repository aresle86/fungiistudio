/* ===== đồ đặt trên bãi (cấp 7–8): nong phơi, khạp muối, hố ủ phân — mỗi món chiếm 1 ô cỏ, dời được bằng Sửa vườn ===== */
const NONG = { lv: 7, buy: 80, n: 4, sun: [6, 18], first: 20 };
const OBJD = {
  nong: { name: 'bộ nong phơi', title: 'Nong phơi', lv: 7, buy: 80, sheet: 'nong', hi: 'Bộ nong tre này Ngoại mua của ông Ba đan đó. Phơi ớt, phơi chuối, nắng lên là khô. Mẻ đầu Ngoại phơi giùm cho mau.' },
  khap: { name: 'khạp muối', title: 'Khạp muối', lv: 8, buy: 150, sheet: 'khap', hi: 'Hai cái khạp da lươn này hồi xưa Ngoại muối dưa cải, muối hột vịt. Muối rồi để lâu không hư đâu con. Mua muối hột ở chợ nghe.' },
  ho: { name: 'hố ủ phân', title: 'Hố ủ phân', lv: 8, buy: 100, sheet: 'ho', hi: 'Hố này con bỏ lá rụng, lục bình, rau dư vô. Đủ đồ là Ngoại ủ, một ngày ra một bao phân. Bón liếp nào đất mệt là tốt lại liền.' } };
const OBJK = Object.keys(OBJD);
const sunAt = ms => { const h = new Date(ms).getHours(); return h >= NONG.sun[0] && h < NONG.sun[1]; };
if (!ST.nong) ST.nong = { own: 0, at: null, trays: [null, null, null, null], done: 0, made: {} };
if (!ST.khap) ST.khap = { own: 0, at: null, jars: [null, null], done: 0, made: {} };
if (!ST.ho) ST.ho = { own: 0, at: null, mat: 0, t: 0, bags: 0, done: 0 };
const nongOn = () => (ST.lv || 1) >= NONG.lv, objOn = k => (ST.lv || 1) >= OBJD[k].lv;
const objAt = id => OBJK.find(k => ST[k] && ST[k].own && ST[k].at === id) || null;
const freeCell = () => { const c = PLOTS.find(P => P.bai && !hidP(P) && locked(P) && !objAt(P.id)); return c ? c.id : null; };
function objPuff(id){ const [u0, v0, u1, v1] = PL[id].b; for (let i = 0; i < 12; i++) puff('leaf', R(u0, u1), .12, R(v0, v1), 1, pick(['#C9A66B', '#E3C46A', '#86B06A']), .6); }
function buyObj(k, at){ const D = OBJD[k], O = ST[k]; if (O.own || !objOn(k)) return; if (!(at && PL[at] && PL[at].bai && locked(PL[at]) && !objAt(at))) at = freeCell();
  if (!at) return say('Bãi hết ô cỏ trống rồi con. Bấm Sửa vườn, san bớt một liếp trống ra mới có chỗ.', 'dan', { now: true }); if (ST.xu < D.buy) return say(`${D.title} ${D.buy} xu, con còn thiếu ${D.buy - ST.xu} xu.`, 'dan');
  ST.xu -= D.buy; O.own = 1; O.at = at; coinPop(`-${D.buy} xu · ${D.name}`, '#F08A6E'); sfx('up'); save(); refreshPlot(at); hud(); objPuff(at); say(D.hi, 'vui', { now: true }); camTo(new T.Vector3(PV[at].cx, .3, PV[at].cz), Math.max(cam.zoom, DEFZ() * 1.2)); }
function placeObj(k, id){ const O = ST[k], P = PL[id]; if (!O || !O.own || !P || !P.bai || hidP(P) || !locked(P) || objAt(id)) return false; const old = O.at; O.at = id; save(); if (old) refreshPlot(old); refreshPlot(id); objPuff(id); sfx('pop'); buzz(12); return true; }
function objRoot(V, k, t){ const O = ST[k], on = !!(O && O.own && O.at && PV[O.at] && !hidP(PL[O.at])); V.root.visible = on; if (V.b) V.b.visible = false; if (!on) return null; const v = PV[O.at]; V.root.position.set(v.cx, 0, v.cz); return v; }
function objBub(V, v, url, t, y = .62){ const b = V.b; b.visible = true; try { bubIcon(b, url); } catch (e) {} b.quaternion.copy(cam.quaternion); b.position.set(v.cx, y + Math.sin(t * 2) * .035, v.cz); b.scale.setScalar(.85 * BUBS * (1 + .07 * Math.abs(Math.sin(t * 3)))); }
function bubHit(V, cx, cy){ if (!V.b || !V.b.visible) return false; ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); return ray.intersectObject(V.hb, false).length > 0; }
const mkBub = () => { const b = bubbleK('h'); return { b, hb: b.children.find(c => c.userData.bub) }; };
/* --- nong phơi: phơi theo nắng giờ thật --- */
function nongSim(dt, ms = Date.now()){ const N = ST.nong; if (!N || !N.own) return; const sun = sunAt(ms); for (const t of N.trays) if (t && t.t > 0 && (sun || t.fast)) t.t = Math.max(0, t.t - dt); }
const phoiName = k => k === 'lucbinh' ? 'lục bình' : k === 'muoi' ? 'muối' : (GD(k) ? GD(k).name.toLowerCase() : k);
const needTxt = inp => Object.entries(inp).map(([ik, n]) => `${n} ${phoiName(ik)}`).join(' + ');
const canIn = inp => Object.entries(inp).every(([ik, n]) => (ik === 'lucbinh' ? 0 : has(ik)) >= n);
const phoiNeed = k => needTxt(PHOI[k].in), phoiCan = k => canIn(PHOI[k].in);
const nong = {
  buy(at){ buyObj('nong', at); }, place(id){ return placeObj('nong', id); },
  put(i, k){ const N = ST.nong, d = PHOI[k]; if (!d || N.trays[i] || (ST.lv || 1) < d.lv || !phoiCan(k)) return; for (const [ik, n] of Object.entries(d.in)) STORE(ik)[ik] -= n;
    const fast = !N.done && !N.trays.some(t => t && t.fast); N.trays[i] = { k, t: fast ? NONG.first : d.t, T: fast ? NONG.first : d.t, fast }; sfx('pick'); buzz(10); gainXP(1); save(); hud();
    if (!fast && !sunAt(Date.now())) say('Trời tối rồi, nong nằm yên đó, sáng mai nắng lên là khô tiếp. Không hư đâu con.', 'dan', { now: true }); },
  take(i){ const N = ST.nong, t = N.trays[i]; if (!t || t.t > 0) return false; if (gbUsed() >= GB_CAP){ say('Gác bếp hết chỗ rồi con. Đem đồ khô ra chợ bán bớt nghe.', 'lo', { now: true }); return false; }
    STORE(t.k)[t.k] = (STORE(t.k)[t.k] || 0) + 1; N.trays[i] = null; N.done = (N.done || 0) + 1; N.made[t.k] = 1; const P = PV[N.at]; if (P){ flyTo(ICON[t.k], P.cx, .3, P.cz); floatAt(P.cx, .6, P.cz, `+1 ${PHOI[t.k].unit} ${PHOI[t.k].name.toLowerCase()}`); }
    sfx('pop'); gainXP(Math.round(PHOI[t.k].sell / 15)); save(); hud(); return true; },
  takeAll(){ let n = 0; ST.nong.trays.forEach((t, i) => { if (t && t.t <= 0 && nong.take(i)) n++; }); if (n) sayOnce('nong1', 'Ớt khô rồi đó con, Ngoại cất trên gác bếp. Hàng xóm hay hỏi mua ớt khô về làm muối ớt lắm.', 'vui'); return n; } };
const moveBtn = k => `<button class="btn" data-a="omove" data-k="${k}">Dời qua ô khác</button>`;
function nongHTML(){ const N = ST.nong, sun = sunAt(Date.now()); let h = `<div class="meta">Phơi bằng nắng thật, từ ${NONG.sun[0]} giờ sáng tới ${NONG.sun[1]} giờ chiều · ${sun ? 'đang có nắng' : 'trời tối, nong nằm yên chờ nắng'}</div>`;
  N.trays.forEach((t, i) => { if (!t){ h += `<div class="sub">Nong ${i + 1} · trống</div><div class="acts">` + Object.keys(PHOI).map(k => { const d = PHOI[k], lk = (ST.lv || 1) < d.lv, can = !lk && phoiCan(k); return `<button class="btn${can ? ' g' : ''}" data-a="nput" data-k="${k}" data-n="${i}" ${can ? '' : 'disabled'}>${d.name}<small>${lk ? `tới cấp ${d.lv}` : phoiNeed(k)}</small></button>`; }).join('') + '</div>'; return; }
    const d = PHOI[t.k], done = t.t <= 0; h += `<div class="srow"><div class="sic"><img src="${ICON[t.k]}" alt=""></div><div class="sn"><b>Nong ${i + 1} · ${d.name}</b>${done ? '<span class="mkh">Khô rồi, cất lên gác bếp</span>' : `${bar(1 - t.t / t.T, '#E9B23A')}<span class="mkh">còn ${fmtT(t.t)} nắng${t.fast ? ' · mẻ đầu Ngoại phơi giùm' : ''}</span>`}</div><span></span>${done ? `<button class="btn g sall" data-a="ntake" data-n="${i}">Lấy</button>` : '<span></span>'}</div>`; });
  h += `<div class="note">Đồ khô cất trên gác bếp (${gbUsed()} / ${GB_CAP} chỗ), bán ở chợ hay giao hàng xóm. Trời tối thì nong nằm yên, không hư.</div><div class="acts">${moveBtn('nong')}</div>`; return h; }
const NONGV = (() => { const root = DYN(G(0, 0, 0)), pr = ROOT; ROOT = root; const xs = [-.19, .19], zs = [-.16, .16];
  for (const z of zs){ M(cyl(.013, .013, .76, 5), C.bamboo, 0, .1, z, { p: root, r: [0, 0, Math.PI / 2] }); for (const x of [-.34, .34]) M(cyl(.012, .014, .1, 5), '#8A5D3B', x, .05, z, { p: root }); }
  const slots = []; for (const z of zs) for (const x of xs){ const g = G(x, .115, z, R(0, 6), root); M(new T.CylinderGeometry(.17, .16, .02, 14), '#C9A66B', 0, 0, 0, { p: g }); M(new T.TorusGeometry(.17, .012, 4, 16), '#A07A45', 0, .012, 0, { p: g, r: [Math.PI / 2, 0, 0] });
    for (const r of [.06, .115]) M(new T.TorusGeometry(r, .004, 3, 14), '#B48C55', 0, .011, 0, { p: g, r: [Math.PI / 2, 0, 0], cast: false }); slots.push({ g: G(0, .012, 0, 0, g), key: null }); }
  ROOT = pr; return { root, slots, ...mkBub() }; })();
function nongFill(sl, t){ const key = t ? t.k + ':' + Math.min(3, Math.floor((1 - t.t / t.T) * 4)) : '-'; if (key === sl.key) return; sl.key = key; for (const m of [...sl.g.children]) sl.g.remove(m); if (!t) return;
  const dry = Math.min(1, 1 - t.t / t.T), pr = ROOT; ROOT = sl.g; const ps = sd; sd = 77 + sl.g.id;
  const mix = (a, b) => '#' + new T.Color(a).lerp(new T.Color(b), dry).getHexString();
  if (t.k === 'otkho') for (let k = 0; k < 14; k++){ const a = rnd() * 6.28, r = Math.sqrt(rnd()) * .12; M(new T.CapsuleGeometry(.011, .045 - dry * .01, 2, 5), mix('#E0402A', '#8E2A1C'), Math.cos(a) * r, .012, Math.sin(a) * r, { r: [Math.PI / 2, R(0, 3), 0], cast: false }); }
  else if (t.k === 'chuoiphoi') for (let k = 0; k < 5; k++){ const a = k / 5 * 6.28; M(sph(.04, 6, 4), mix('#E9C96A', '#8A5A2E'), Math.cos(a) * .08, .01, Math.sin(a) * .08, { s: [1.6, .35 - dry * .1, .8], r: [0, -a, 0], cast: false }); }
  else for (let k = 0; k < 10; k++) M(box(R(.16, .24), .008, .016), mix('#6E9F57', '#B8A070'), R(-.06, .06), .008 + k * .002, R(-.08, .08), { r: [0, R(0, 3), 0], cast: false });
  sd = ps; ROOT = pr; }
function nongTick(t){ const v = objRoot(NONGV, 'nong', t); if (!v) return; const N = ST.nong; N.trays.forEach((tr, i) => nongFill(NONGV.slots[i], tr)); const done = N.trays.find(tr => tr && tr.t <= 0); if (done) objBub(NONGV, v, ICON[done.k], t); }
const nongHit = (cx, cy) => bubHit(NONGV, cx, cy);
/* --- khạp muối (cấp 8): muối dưa cải, hột vịt; không cần nắng, để lâu không hư --- */
const MUOI_PRICE = 4;
function khapSim(dt){ const K = ST.khap; if (!K || !K.own) return; for (const j of K.jars) if (j && j.t > 0) j.t = Math.max(0, j.t - dt); }
const khap = {
  put(i, k){ const K = ST.khap, d = MUOI[k]; if (!d || K.jars[i] || (ST.lv || 1) < d.lv || !canIn(d.in)) return; for (const [ik, n] of Object.entries(d.in)) STORE(ik)[ik] -= n; const fast = !K.done && !K.jars.some(j => j && j.fast);
    K.jars[i] = { k, t: fast ? 30 : d.t, T: fast ? 30 : d.t, fast }; sfx('pick'); buzz(10); gainXP(1); save(); hud(); },
  take(i){ const K = ST.khap, j = K.jars[i]; if (!j || j.t > 0) return false; const d = MUOI[j.k]; if (gbUsed() + d.out > GB_CAP){ say('Gác bếp hết chỗ rồi con. Bán bớt đồ trên gác bếp nghe.', 'lo', { now: true }); return false; }
    STORE(j.k)[j.k] = (STORE(j.k)[j.k] || 0) + d.out; K.jars[i] = null; K.done = (K.done || 0) + 1; K.made[j.k] = 1; const P = PV[K.at]; if (P){ flyTo(ICON[j.k], P.cx, .3, P.cz); floatAt(P.cx, .6, P.cz, `+${d.out} ${d.unit} ${d.name.toLowerCase()}`); }
    sfx('pop'); gainXP(Math.round(d.sell * d.out / 15)); save(); hud(); return true; },
  takeAll(){ let n = 0; ST.khap.jars.forEach((j, i) => { if (j && j.t <= 0 && khap.take(i)) n++; }); if (n) sayOnce('khap1', 'Dưa muối chua vừa tới nè. Hồi đó nhà mình ăn dưa cải với thịt kho cả tuần Tết.', 'vui'); return n; } };
function khapHTML(){ const K = ST.khap; let h = `<div class="meta">Hai khạp da lươn · muối xong để bao lâu cũng được, không hư</div>`;
  K.jars.forEach((j, i) => { if (!j){ h += `<div class="sub">Khạp ${i + 1} · trống</div><div class="acts">` + Object.keys(MUOI).map(k => { const d = MUOI[k], lk = (ST.lv || 1) < d.lv, can = !lk && canIn(d.in); return `<button class="btn${can ? ' g' : ''}" data-a="kput" data-k="${k}" data-n="${i}" ${can ? '' : 'disabled'}>${d.name}<small>${needTxt(d.in)}</small></button>`; }).join('') + '</div>'; return; }
    const d = MUOI[j.k], done = j.t <= 0; h += `<div class="srow"><div class="sic"><img src="${ICON[j.k]}" alt=""></div><div class="sn"><b>Khạp ${i + 1} · ${d.name}</b>${done ? `<span class="mkh">Thấm muối rồi, được ${d.out} ${d.unit}</span>` : `${bar(1 - j.t / j.T, '#86B06A')}<span class="mkh">còn ${fmtT(j.t)}${j.fast ? ' · Ngoại có hũ muối sẵn cho con' : ''}</span>`}</div><span></span>${done ? `<button class="btn g sall" data-a="ktake" data-n="${i}">Vớt ra</button>` : '<span></span>'}</div>`; });
  h += `<div class="note">Muối hột mua ở chợ, ${MUOI_PRICE} xu một bịch, để trên gác bếp (đang có ${(ST.gb || {}).muoi || 0} bịch).</div><div class="acts"><button class="btn" data-a="gocho3">Ra chợ mua muối</button>${moveBtn('khap')}</div>`; return h; }
const KHAPV = (() => { const root = DYN(G(0, 0, 0)), pr = ROOT; ROOT = root; const jars = [];
  for (const [x, z, s] of [[-.17, -.05, 1], [.18, .08, .9]]){ const g = G(x, 0, z, R(0, 6), root); M(new T.LatheGeometry([[0, 0], [.13, .02], [.19, .12], [.2, .2], [.16, .3], [.1, .34], [.1, .37], [0, .37]].map(([a, b]) => new T.Vector2(a * s, b * s)), 10), '#6B3E22', 0, 0, 0, { p: g });
    M(new T.TorusGeometry(.105 * s, .015, 4, 10), '#4A2A16', 0, .365 * s, 0, { p: g, r: [Math.PI / 2, 0, 0] }); for (let k = 0; k < 3; k++) M(new T.TorusGeometry(.2 * s - k * .012, .006, 3, 12), '#8A5530', 0, (.16 + k * .03) * s, 0, { p: g, r: [Math.PI / 2, 0, 0], cast: false });
    const lid = G(0, .38 * s, 0, 0, g); M(new T.CylinderGeometry(.13 * s, .14 * s, .025, 10), '#B48560', 0, 0, 0, { p: lid }); M(box(.03, .03, .16 * s), '#8A5D3B', 0, .025, 0, { p: lid }); jars.push({ g, lid }); }
  M(box(.18, .04, .12), '#E9E4D8', .05, .02, .2, { p: root, r: [0, .4, 0] });   // bịch muối hột bên cạnh
  ROOT = pr; return { root, jars, ...mkBub() }; })();
function khapTick(t){ const v = objRoot(KHAPV, 'khap', t); if (!v) return; const K = ST.khap; K.jars.forEach((j, i) => { const L = KHAPV.jars[i].lid; L.rotation.z = j && j.t <= 0 ? .35 + Math.sin(t * 3) * .03 : 0; L.position.x = j && j.t <= 0 ? .05 : 0; });
  const done = K.jars.find(j => j && j.t <= 0); if (done) objBub(KHAPV, v, ICON[done.k], t, .7); }
const khapHit = (cx, cy) => bubHit(KHAPV, cx, cy);
/* --- hố ủ phân (cấp 8): lá rụng, lục bình, rau dư → bao phân; bón liếp đất mệt --- */
const HO = { need: 6, t: 24 * 3600, first: 60, max: 5, cap: 12, soil: .3 };
function hoSim(dt){ const H = ST.ho; if (!H || !H.own) return; if (H.t > 0){ H.t = Math.max(0, H.t - dt); if (H.t <= 0){ H.bags = Math.min(HO.max, (H.bags || 0) + 1); H.done = (H.done || 0) + 1; } } if (H.t <= 0 && H.mat >= HO.need && (H.bags || 0) < HO.max){ H.mat -= HO.need; H.t = H.done ? HO.t : HO.first; } }
const hoRoom = () => ST.ho && ST.ho.own && ST.ho.mat < HO.cap;
function hoAdd(n, x, z){ const H = ST.ho; if (!hoRoom()) return false; H.mat = Math.min(HO.cap, H.mat + n); hoSim(0); if (x != null && PV[H.at]) flyTo(ICON.phan, x, .2, z); save(); return true; }
const hoWorst = () => PLOTS.filter(P => !P.tree && !P.trellis && !hidP(P) && !locked(P) && ST.plots[P.id] && ST.plots[P.id].soil < .95).sort((a, b) => ST.plots[a.id].soil - ST.plots[b.id].soil)[0];
function hoBon(id){ const H = ST.ho, P = id ? PL[id] : hoWorst(); if (!H.bags || !P){ if (!P) say('Liếp nào đất cũng tốt hết rồi con, để dành phân bữa sau.', 'vui', { now: true }); return; } const p = ST.plots[P.id]; p.soil = Math.min(1, p.soil + HO.soil); H.bags--; const v = PV[P.id];
  for (let i = 0; i < 14; i++) puff('seed', R(P.b[0], P.b[2]), .2, R(P.b[1], P.b[3]), 1, pick(['#5A371F', '#6B4529', '#8A5D3B']), .6); floatAt(v.cx, .5, v.cz, `Bón phân: ${P.name.toLowerCase()} đất tốt lên`, '#9fd36a'); sfx('pick'); buzz(12); gainXP(2); save(); hud(); }
function hoRau(){ const k = Object.keys(ST.inv).filter(k => CROPS[k] && !CROPS[k].tree && ST.inv[k] > 0).sort((a, b) => ST.inv[b] - ST.inv[a])[0]; if (!k) return say('Kho không còn rau dư con. Lá rụng với lục bình bỏ vô cũng được.', 'dan', { now: true }); if (!hoRoom()) return say('Hố đầy rồi con, đợi Ngoại ủ xong mẻ này.', 'dan', { now: true }); ST.inv[k]--; hoAdd(1); sfx('pick'); hud(); }
function hoHTML(){ const H = ST.ho; let h = `<div class="meta">Đủ ${HO.need} phần đồ ủ là Ngoại ủ, ${H.done ? 'một ngày' : 'mẻ đầu một phút'} ra một bao phân</div>`;
  h += `<div class="kv"><span>Đồ ủ trong hố</span>${bar(H.mat / HO.need, '#8A5D3B')}<b class="sm">${H.mat} / ${HO.need} phần</b></div><div class="kv"><span>Đang ủ</span><b>${H.t > 0 ? 'còn ' + fmtT(H.t) : 'chưa'}</b></div><div class="kv"><span>Phân đã ủ</span><b>${H.bags || 0} bao</b></div>`;
  h += `<div class="note">Quét lá rụng +2 phần, vớt lục bình +1 phần (vịt no rồi thì lục bình vô hố), rau dư trong kho +1 phần. Bón một bao: đất liếp +0,3.</div>`;
  const w = hoWorst(); h += `<div class="acts"><button class="btn${H.bags ? ' g' : ''}" data-a="hobon" ${H.bags && w ? '' : 'disabled'}>Bón liếp đất mệt nhất${w ? ` · ${w.name.toLowerCase()}` : ''}</button><button class="btn" data-a="horau" ${hoRoom() ? '' : 'disabled'}>Bỏ 1 rau dư</button>${moveBtn('ho')}</div>`; return h; }
const HOV = (() => { const root = DYN(G(0, 0, 0)), pr = ROOT; ROOT = root;
  for (const [x, z, w, l] of [[0, -.24, .62, .05], [0, .24, .62, .05], [-.29, 0, .05, .5], [.29, 0, .05, .5]]) M(box(w, .1, l), '#6B4529', x, .04, z, { p: root });   // bờ ván
  for (const [x, z] of [[-.29, -.24], [.29, -.24], [-.29, .24], [.29, .24]]) M(cyl(.02, .022, .2, 5), C.bamboo, x, .09, z, { p: root });
  const fill = G(0, 0, 0, 0, root); M(box(.54, .03, .44), '#4A2F1E', 0, .015, 0, { p: fill, cast: false });
  const top = G(0, 0, 0, 0, root); for (let k = 0; k < 16; k++) M(box(R(.08, .16), .012, .03), pick(['#C9952A', '#B48560', '#6E9F57', '#8A5D3B']), R(-.22, .22), .04, R(-.17, .17), { p: top, r: [0, R(0, 3), 0], cast: false });
  const bags = []; for (let k = 0; k < 3; k++){ const b = M(sph(.07, 6, 4), '#B8A27A', .42, .07, -.15 + k * .15, { p: root, s: [1, 1.2, .9] }); bags.push(b); }
  ROOT = pr; return { root, fill, top, bags, ...mkBub() }; })();
function hoTick(t){ const v = objRoot(HOV, 'ho', t); if (!v) return; const H = ST.ho; HOV.top.visible = H.mat > 0 || H.t > 0; HOV.top.position.y = Math.min(1, H.mat / HO.need) * .03; HOV.bags.forEach((b, i) => b.visible = i < (H.bags || 0));
  if (H.bags) objBub(HOV, v, ICON.phan, t); }
const hoHit = (cx, cy) => bubHit(HOV, cx, cy);
/* --- lò ấp vịt (cấp 9): trấu giữ ấm, ấp 4 trứng vịt, nở thêm vịt cho đàn --- */
const LO = { lv: 9, eggs: 4, cui: 1, t: 18 * 3600, first: 60, at: [-1.45, 6.3], sellDuck: 40 };
if (!ST.lo) ST.lo = { t: 0, on: 0, done: 0, hatch: 0 };
const loOn = () => (ST.lv || 1) >= LO.lv;
function loSim(dt){ const L = ST.lo; if (!L || !L.on) return; if (L.t > 0){ L.t = Math.max(0, L.t - dt); if (L.t <= 0) L.hatch = LO.eggs; } }
const lo = {
  put(){ const L = ST.lo; if (!loOn() || L.on) return; if ((ST.inv.trungvit || 0) < LO.eggs) return say(`Cần ${LO.eggs} trứng vịt mới ấp được một lứa con.`, 'dan', { now: true }); if (((ST.gb || {}).cui || 0) < LO.cui) return say('Cần một bó củi hun trấu cho ấm con. Nhặt củi hay mua ở chợ nghe.', 'dan', { now: true });
    ST.inv.trungvit -= LO.eggs; ST.gb.cui -= LO.cui; L.on = 1; L.t = L.done ? LO.t : LO.first; L.T = L.t; sfx('pick'); buzz(10); gainXP(2); save(); hud(); say(L.done ? 'Vùi trứng trong trấu ấm rồi. Ngoại canh lửa cho, chừng mười tám tiếng là nở.' : 'Lứa đầu Ngoại ấp sẵn từ bữa trước, chút xíu là nở con coi.', 'vui', { now: true }); },
  hatch(){ const L = ST.lo; if (!L.on || L.t > 0 || !L.hatch) return; const v = ST.vit, room = Math.max(0, vitCap() - v.n), add = Math.min(L.hatch, room), sold = L.hatch - add; v.n += add; v.trough += add; L.on = 0; L.hatch = 0; L.done++; vitSpawn();
    const [x, z] = LO.at; for (let i = 0; i < 12; i++) puff('leaf', x + R(-.2, .2), .25, z + R(-.2, .2), 1, pick(['#ffe266', '#F5D27A', '#E9C96A']), .5); sfx('pop'); buzz(20); gainXP(6);
    if (sold){ ST.xu += sold * LO.sellDuck; coinPop(`+${sold * LO.sellDuck} xu · bán ${sold} vịt con`); } say(add ? `Nở ${add} con vịt rồi nè! Ngoại thả chung với đàn.${sold ? ` Chuồng hết chỗ nên Ngoại bán ${sold} con cho cô Tư, được ${sold * LO.sellDuck} xu.` : ''}` : `Chuồng vịt hết chỗ, Ngoại bán ${sold} vịt con cho cô Tư được ${sold * LO.sellDuck} xu. Nâng chuồng thì nuôi thêm được.`, 'vui', { now: true }); save(); hud(); } };
function loHTML(){ const L = ST.lo; let h = `<div class="meta">Lò ấp trấu của Ngoại · ${LO.eggs} trứng vịt + ${LO.cui} bó củi một lứa</div>`;
  h += `<div class="kv"><span>Trong lò</span><b>${L.on ? (L.t > 0 ? `${LO.eggs} trứng, còn ${fmtT(L.t)}` : `${L.hatch} vịt con mới nở`) : 'trống'}</b></div><div class="kv"><span>Chuồng vịt</span><b>${ST.vit.n} / ${vitCap()} con</b></div>`;
  h += `<div class="note">Vịt nở ra vô chuồng chung với đàn. Chuồng hết chỗ thì Ngoại bán vịt con cho hàng xóm, ${LO.sellDuck} xu một con.</div><div class="acts">`;
  h += L.on && L.t <= 0 ? `<button class="btn g" data-a="lohatch">Bắt vịt con</button>` : `<button class="btn${!L.on ? ' g' : ''}" data-a="loput" ${L.on ? 'disabled' : ''}>Ấp ${LO.eggs} trứng vịt</button>`; return h + '</div>'; }
const LOV = (() => { const [x, z] = LO.at, root = DYN(G(x, 0, z, .5)), pr = ROOT; ROOT = root;
  for (const [px, pz, hh] of [[-.32, -.22, .62], [.32, -.22, .62], [-.32, .22, .48], [.32, .22, .48]]) M(cyl(.02, .024, hh, 5), '#8A5D3B', px, hh / 2, pz, { p: root });
  for (let r = 0; r < 4; r++){ const m = M(box(.78, .03, .17), r % 2 ? C.thatch : C.thatchD, 0, .64 - r * .05, -.24 + r * .15, { p: root }); m.rotation.x = .32; }   // mái lá
  M(box(.56, .2, .32), '#7A5236', 0, .1, 0, { p: root }); M(box(.5, .02, .26), '#D9B26A', 0, .205, 0, { p: root, cast: false });   // thùng gỗ đầy trấu
  const eggs = []; for (let k = 0; k < 4; k++) eggs.push(M(sph(.03, 7, 5), '#E2F0EA', -.15 + k * .1, .215, R(-.05, .05), { p: root, s: [.85, 1.1, .85], cast: false }));
  const ducks = []; for (let k = 0; k < 4; k++){ const d = duckling(-.18 + k * .12, .1, R(0, 6), false); root.add(d); d.position.set(-.18 + k * .12, .21, R(-.04, .06)); ducks.push(d); }
  M(cyl(.05, .06, .08, 7), '#6B4529', .38, .04, .12, { p: root }); const fire = M(cone(.035, .08, 5), '#F08A3E', .38, .12, .12, { p: root, cast: false });
  ROOT = pr; const hit = new T.Mesh(new T.BoxGeometry(.9, .7, .7), new T.MeshBasicMaterial({ visible: false })); hit.position.set(x, .35, z); S.add(hit); return { root, eggs, ducks, fire, hit, ...mkBub() }; })();
function loTick(t){ const on = loOn(), L = ST.lo; LOV.root.visible = on; LOV.b.visible = false; if (!on) return; const hatched = L.on && L.t <= 0; LOV.eggs.forEach(e => e.visible = !!L.on && !hatched); LOV.ducks.forEach((d, i) => { d.visible = hatched; d.position.y = .21 + Math.abs(Math.sin(t * 6 + i)) * .02; });
  LOV.fire.visible = !!L.on && !hatched; LOV.fire.scale.y = 1 + Math.sin(t * 9) * .2; const [x, z] = LO.at;
  if (hatched || !L.on){ const b = LOV.b; b.visible = hatched || ((ST.inv.trungvit || 0) >= LO.eggs && !L.done); try { bubIcon(b, hatched ? ICON.vitcon : ICON.trungvit); } catch (e) {} b.quaternion.copy(cam.quaternion); b.position.set(x, .9 + Math.sin(t * 2) * .035, z); b.scale.setScalar(.8 * BUBS); } }
function loHit(cx, cy){ if (!loOn()) return null; ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); const hs = ray.intersectObjects([LOV.hb, LOV.hit].filter(h => h.visible !== false && (!h.parent || h.parent.visible !== false)), false); return hs.length ? (hs[0].object === LOV.hb ? 'bub' : 'lo') : null; }
/* --- câu cá ở bến (cấp 9): thả cần, chờ phao giật rồi chạm --- */
const CAU = { lv: 9, day: 10, wait: [4, 10], bite: 1.6, fish: [['caro', .65], ['caloc', .35]] };
if (!ST.cau) ST.cau = { d: '', n: 0, got: 0 };
let CST = null;   // { st: 'wait'|'bite'|'miss', t }
const cauOn = () => (ST.lv || 1) >= CAU.lv, cauLeft = () => (ST.cau.d === dayKey() ? CAU.day - ST.cau.n : CAU.day);
const CAUV = (() => { const root = DYN(G(0, 0, 0)), pr = ROOT; ROOT = root; const base = new T.Vector3(bx - .2, .24, R0 + 1.3), tip = new T.Vector3(bx - .95, .78, R0 + 1.72);
  stick(root, base.x, base.y, base.z, tip.x, tip.y, tip.z, .011, '#C9A66B'); M(box(.05, .12, .05), '#6B4529', bx - .23, .2, R0 + 1.22, { p: root }); M(cyl(.06, .07, .08, 7), '#8A6A4A', bx - .05, .24, R0 + 1.15, { p: root });   // cần tre, cọc gác, giỏ mồi
  const ph = G(0, 0, 0, 0, root); M(sph(.03, 7, 5), '#E8453A', 0, .015, 0, { p: ph }); M(sph(.022, 7, 5), '#FBF7EE', 0, .045, 0, { p: ph }); M(cyl(.004, .004, .05, 3), '#4A2F1E', 0, .08, 0, { p: ph });
  const lg = new T.BufferGeometry().setFromPoints([tip, tip]); const line = new T.Line(lg, new T.LineBasicMaterial({ color: '#F5ECD6', transparent: true, opacity: .8 })); root.add(line);
  ROOT = pr; const hit = new T.Mesh(new T.SphereGeometry(.35, 8, 6), new T.MeshBasicMaterial({ visible: false })); hit.position.set(bx - .7, .3, R0 + 1.6); S.add(hit); return { root, ph, line, tip, hit, rest: new T.Vector3(bx - .98, WLR + .01, R0 + 1.92), ...mkBub() }; })();
function cauTick(t, dt){ const on = cauOn() && !VISIT; CAUV.root.visible = on; CAUV.b.visible = false; CAUV.hit.visible = on; if (!on) return; const ph = CAUV.ph, r = CAUV.rest;
  if (CST){ CST.t -= dt; if (CST.st === 'wait' && CST.t <= 0){ CST = { st: 'bite', t: CAU.bite }; sfx('pop'); buzz(25); } else if (CST.st === 'bite' && CST.t <= 0){ CST = null; say(pick(['Cá ăn mồi chạy mất rồi con. Phao giật là chạm liền nghe.', 'Hụt rồi! Lần sau phao chìm là giựt cần liền.']), 'dan', { now: true }); } }
  ph.visible = !!CST; if (CST){ const bite = CST.st === 'bite'; ph.position.set(r.x + Math.sin(t * 1.3) * .02, r.y + (bite ? -.03 - Math.abs(Math.sin(t * 18)) * .03 : Math.sin(t * 2.2) * .008), r.z); const pos = CAUV.line.geometry.attributes.position; pos.setXYZ(1, ph.position.x, ph.position.y + .1, ph.position.z); pos.setXYZ(0, CAUV.tip.x, CAUV.tip.y, CAUV.tip.z); pos.needsUpdate = true; }
  CAUV.line.visible = !!CST; const b = CAUV.b; const show = CST ? CST.st === 'bite' : cauLeft() > 0 && !ST.cau.got; if (show){ b.visible = true; try { bubIcon(b, CST ? UIC.excl || ICON.caro : ICON.cancau); } catch (e) {} b.quaternion.copy(cam.quaternion); b.position.set(CST ? r.x : bx - .7, (CST ? .45 : .75) + Math.sin(t * 2) * .03, CST ? r.z : R0 + 1.6); b.scale.setScalar((CST ? 1 : .8) * BUBS * (1 + (CST ? .15 : .07) * Math.abs(Math.sin(t * (CST ? 10 : 3))))); } }
function cauHit(cx, cy){ if (!cauOn() || VISIT) return false; ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); return ray.intersectObjects([CAUV.hb, CAUV.hit].filter(h => h.visible !== false && (!h.parent || h.parent.visible !== false)), false).length > 0; }
function cauTap(){ const C2 = ST.cau; if (C2.d !== dayKey()){ C2.d = dayKey(); C2.n = 0; }
  if (!CST){ if (C2.n >= CAU.day) return say('Hôm nay câu đủ rồi con, để cá nó sanh sôi. Mai ra câu tiếp nghe.', 'dan', { now: true }); if (kCap() - kUsed() <= 0) return say('Kho đầy rồi, câu lên không có chỗ để cá đâu con.', 'lo', { now: true });
    CST = { st: 'wait', t: R(CAU.wait[0], CAU.wait[1]) }; C2.n++; sfx('pick'); buzz(8); sayOnce('cau1', 'Thả cần rồi đó. Ngồi im, chừng nào phao đỏ giật chìm là chạm liền nghe con.', 'vui'); save(); return; }
  if (CST.st === 'wait'){ CST = null; return say('Giựt sớm quá cá chưa ăn mồi con. Đợi phao chìm hẳn nghe.', 'dan', { now: true }); }
  CST = null; let r2 = Math.random(), k = CAU.fish[0][0]; for (const [fk, p] of CAU.fish){ if (r2 < p){ k = fk; break; } r2 -= p; } ST.inv[k] = (ST.inv[k] || 0) + 1; C2.got = 0; ST.cau.tot = (ST.cau.tot || 0) + 1;
  const r = CAUV.rest; flyTo(ICON[k], r.x, .3, r.z); floatAt(r.x, .6, r.z, `+1 ${GD(k).name.toLowerCase()}`, '#9fd36a'); for (let i = 0; i < 10; i++) puff('drop', r.x, .05, r.z, 1, '#9cc6e0', .7); sfx('coin'); buzz(30); gainXP(k === 'caloc' ? 4 : 2); bump('fish', 1); save(); hud();
  if (k === 'caloc') sayOnce('caloc1', 'Cá lóc đồng nè con! Đem nấu canh chua cá lóc là ngon hết sẩy.', 'vui'); }

