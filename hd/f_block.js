/* --- lò sấy (cấp 10): chạy cả đêm, tốn củi; sấy mứt khế, xoài, dừa; ớt chuối nhanh gấp đôi nong --- */
if (!ST.say) ST.say = { own: 0, at: null, trays: [null, null], done: 0, made: {} };
const SAYR = { mutkhe: SAY.mutkhe, xoaisay: SAY.xoaisay, comdua: SAY.comdua, mutdua: SAY.mutdua, otkho: { ...PHOI.otkho, t: PHOI.otkho.t / 2 }, chuoiphoi: { ...PHOI.chuoiphoi, t: PHOI.chuoiphoi.t / 2 } };
function saySim(dt){ const L = ST.say; if (!L || !L.own) return; for (const t of L.trays) if (t && t.t > 0) t.t = Math.max(0, t.t - dt); }
const lsay = {
  put(i, k){ const L = ST.say, d = SAYR[k]; if (!d || L.trays[i] || (ST.lv || 1) < d.lv || !canIn(d.in)) return; if (((ST.gb || {}).cui || 0) < 1) return say('Lò sấy cần một bó củi mỗi mẻ con. Nhặt củi hay mua ở chợ nghe.', 'dan', { now: true });
    for (const [ik, n] of Object.entries(d.in)) STORE(ik)[ik] -= n; ST.gb.cui--; const fast = !L.done && !L.trays.some(t => t && t.fast); L.trays[i] = { k, t: fast ? 40 : d.t, T: fast ? 40 : d.t, fast }; sfx('pick'); buzz(10); gainXP(1); save(); hud(); },
  take(i){ const L = ST.say, t = L.trays[i]; if (!t || t.t > 0) return false; if (gbUsed() >= GB_CAP){ say('Gác bếp hết chỗ rồi con. Bán bớt đồ trên gác bếp nghe.', 'lo', { now: true }); return false; }
    STORE(t.k)[t.k] = (STORE(t.k)[t.k] || 0) + 1; L.trays[i] = null; L.done = (L.done || 0) + 1; L.made[t.k] = 1; const d = GD(t.k), P = PV[L.at]; if (P){ flyTo(ICON[t.k], P.cx, .3, P.cz); floatAt(P.cx, .7, P.cz, `+1 ${d.unit} ${d.name.toLowerCase()}`); }
    sfx('pop'); gainXP(Math.round(d.sell / 15)); save(); hud(); return true; },
  takeAll(){ let n = 0; ST.say.trays.forEach((t, i) => { if (t && t.t <= 0 && lsay.take(i)) n++; }); if (n) sayOnce('say1', 'Thơm lừng! Mứt sấy cất lên gác bếp, Tết mang ra đãi khách hay giao cho ghe chợ nổi đều được.', 'vui'); return n; } };
function sayHTML(){ const L = ST.say; let h = `<div class="meta">Lò sấy gạch · chạy cả đêm, không cần nắng, mỗi mẻ một bó củi (gác bếp còn ${(ST.gb || {}).cui || 0} bó)</div>`;
  L.trays.forEach((t, i) => { if (!t){ h += `<div class="sub">Khay ${i + 1} · trống</div><div class="acts">` + Object.keys(SAYR).map(k => { const d = SAYR[k], lk = (ST.lv || 1) < d.lv, can = !lk && canIn(d.in); return `<button class="btn${can ? ' g' : ''}" data-a="sput" data-k="${k}" data-n="${i}" ${can ? '' : 'disabled'}>${d.name}<small>${lk ? `tới cấp ${d.lv}` : `${needTxt(d.in)} · ${fmtT(d.t)}`}</small></button>`; }).join('') + '</div>'; return; }
    const d = SAYR[t.k], done = t.t <= 0; h += `<div class="srow"><div class="sic"><img src="${ICON[t.k]}" alt=""></div><div class="sn"><b>Khay ${i + 1} · ${d.name}</b>${done ? '<span class="mkh">Sấy xong, cất lên gác bếp</span>' : `${bar(1 - t.t / t.T, '#E9823A')}<span class="mkh">còn ${fmtT(t.t)}${t.fast ? ' · mẻ đầu Ngoại canh lửa giùm' : ''}</span>`}</div><span></span>${done ? `<button class="btn g sall" data-a="stake" data-n="${i}">Lấy</button>` : '<span></span>'}</div>`; });
  h += `<div class="note">Đường cát mua ở chợ, ${DUONG_PRICE} xu một bịch. Ớt, chuối sấy lò nhanh gấp đôi phơi nong.</div><div class="acts"><button class="btn" data-a="gocho3">Ra chợ mua đường, củi</button>${moveBtn('say')}</div>`; return h; }
const SAYV = (() => { const root = DYN(G(0, 0, 0)), pr = ROOT; ROOT = root;
  M(box(.62, .42, .46), '#B5653E', 0, .21, 0, { p: root }); for (let r = 0; r < 4; r++) M(box(.63, .012, .47), '#9A4F2E', 0, .06 + r * .1, 0, { p: root, cast: false });   // gạch
  M(box(.66, .05, .5), '#8A4528', 0, .445, 0, { p: root }); M(cyl(.06, .07, .36, 7), '#9A4F2E', .2, .62, -.12, { p: root }); M(cyl(.075, .075, .03, 7), '#6B3A22', .2, .81, -.12, { p: root });
  M(box(.22, .2, .02), '#3A2418', 0, .14, .235, { p: root }); const fire = M(cone(.06, .12, 5), '#F08A3E', 0, .1, .22, { p: root, cast: false });
  for (const x of [-.32, .32]) M(box(.04, .3, .04), '#7A5236', x, .15, .26, { p: root }); M(box(.7, .025, .14), '#C9A66B', 0, .3, .3, { p: root });   // kệ khay phía trước
  ROOT = pr; return { root, fire, ...mkBub() }; })();
let SAYSMK = 0;
function sayTick(t, dt){ const v = objRoot(SAYV, 'say', t); if (!v) return; const L = ST.say, on = L.trays.some(x => x && x.t > 0); SAYV.fire.visible = on; SAYV.fire.scale.y = 1 + Math.sin(t * 9) * .25;
  if (on && (SAYSMK -= dt) <= 0){ SAYSMK = .5; puff('leaf', v.cx + .2, .85, v.cz - .12, 1, '#D8D2C8', .25); } const done = L.trays.find(x => x && x.t <= 0); if (done) objBub(SAYV, v, ICON[done.k], t, .95); }
const sayHit = (cx, cy) => bubHit(SAYV, cx, cy);
/* --- giỏ lục bình (cấp 10): Ngoại ngồi hiên đan, 5 lục bình khô → 1 giỏ, 1 giờ, tối đa 4 giỏ mỗi ngày --- */
const GIO = { lv: 10, need: 5, t: 3600, day: 4, at: [1.2, 1.62] };
if (!ST.gio) ST.gio = { d: '', n: 0, t: 0, on: 0, done: 0 };
const gioOn = () => (ST.lv || 1) >= GIO.lv;
function gioSim(dt){ const g = ST.gio; if (g && g.on && g.t > 0) g.t = Math.max(0, g.t - dt); }
const gio = {
  put(){ const g = ST.gio; if (g.d !== dayKey()){ g.d = dayKey(); g.n = 0; } if (g.on) return; if (g.n >= GIO.day) return say('Hôm nay Ngoại đan đủ bốn cái rồi, mỏi tay lắm con. Mai đan tiếp nghe.', 'dan', { now: true });
    if (has('lucbinhkho') < GIO.need) return say(`Cần ${GIO.need} bó lục bình khô. Vớt lục bình cất gác bếp rồi đem phơi nong nghe con.`, 'dan', { now: true }); STORE('lucbinhkho').lucbinhkho -= GIO.need; g.on = 1; g.t = g.done ? GIO.t : 30; g.T = g.t; g.n++; sfx('pick'); save(); hud();
    say(g.done ? 'Ngoại ngồi hiên đan, chừng một tiếng là xong một cái.' : 'Ngoại đan giỏ lục bình từ hồi con gái. Coi nè, chút xíu là xong.', 'vui', { now: true }); },
  take(){ const g = ST.gio; if (!g.on || g.t > 0) return; if (gbUsed() >= GB_CAP) return say('Gác bếp hết chỗ rồi con.', 'lo', { now: true }); STORE('gio').gio = (STORE('gio').gio || 0) + 1; g.on = 0; g.done++; const [x, z] = GIO.at; flyTo(ICON.gio, x, .4, z); floatAt(x, .7, z, '+1 giỏ lục bình'); sfx('pop'); gainXP(3); save(); hud(); sayOnce('gio1', 'Giỏ lục bình đi chợ nổi bán chạy lắm, khách nước ngoài cũng mua.', 'vui'); } };
function gioHTML(){ const g = ST.gio, left = g.d === dayKey() ? GIO.day - g.n : GIO.day; let h = `<div class="meta">Ngoại ngồi hiên đan giỏ · ${GIO.need} bó lục bình khô một giỏ, còn đan được ${left} giỏ hôm nay</div>`;
  h += `<div class="kv"><span>Lục bình khô</span><b>${has('lucbinhkho')} bó</b></div><div class="kv"><span>Đang đan</span><b>${g.on ? (g.t > 0 ? 'còn ' + fmtT(g.t) : 'xong rồi') : 'chưa'}</b></div>`;
  h += `<div class="note">Lục bình vớt dưới mương, sông cất gác bếp (khi vịt no). Đem phơi nong thành lục bình khô.</div><div class="acts">`;
  return h + (g.on && g.t <= 0 ? `<button class="btn g" data-a="giotake">Lấy giỏ</button>` : `<button class="btn${!g.on ? ' g' : ''}" data-a="gioput" ${g.on || left <= 0 || has('lucbinhkho') < GIO.need ? 'disabled' : ''}>Nhờ Ngoại đan một giỏ</button>`) + '</div>'; }
const GIOV = (() => { const [x, z] = GIO.at, root = DYN(G(x, 0, z, .3)), pr = ROOT; ROOT = root;
  M(box(.22, .1, .22), '#8A5D3B', 0, .05, 0, { p: root }); for (const [px, pz] of [[-.09, -.09], [.09, -.09], [-.09, .09], [.09, .09]]) M(cyl(.012, .012, .1, 4), '#6B4529', px, .05, pz, { p: root });   // ghế đẩu
  const g = G(.28, 0, .05, 0, root); M(new T.CylinderGeometry(.13, .09, .14, 10, 1, true), '#B8A070', 0, .07, 0, { p: g, ds: true }); for (let k = 0; k < 3; k++) M(new T.TorusGeometry(.1 + k * .012, .006, 3, 12), '#9A8050', 0, .03 + k * .045, 0, { p: g, r: [Math.PI / 2, 0, 0], cast: false });
  for (let k = 0; k < 6; k++) M(cyl(.008, .008, .34, 3), '#C9B27A', -.2 + R(-.04, .04), .02, .12 + k * .018, { p: root, r: [0, R(-.3, .3), Math.PI / 2], cast: false });   // bó cọng khô
  ROOT = pr; const hit = new T.Mesh(new T.BoxGeometry(.7, .5, .5), new T.MeshBasicMaterial({ visible: false })); hit.position.set(x + .1, .25, z); S.add(hit); return { root, hit, ...mkBub() }; })();
function gioTick(t){ const on = gioOn() && !VISIT, g = ST.gio; GIOV.root.visible = on; GIOV.hit.visible = on; GIOV.b.visible = false; if (!on) return; const [x, z] = GIO.at;
  const show = (g.on && g.t <= 0) || (!g.on && has('lucbinhkho') >= GIO.need && (g.d !== dayKey() || g.n < GIO.day)); if (show){ const b = GIOV.b; b.visible = true; try { bubIcon(b, g.on ? ICON.gio : ICON.lucbinhkho); } catch (e) {} b.quaternion.copy(cam.quaternion); b.position.set(x + .15, .65 + Math.sin(t * 2) * .03, z); b.scale.setScalar(.8 * BUBS); } }
function gioHit(cx, cy){ if (!gioOn() || VISIT) return null; ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); const hs = ray.intersectObjects([GIOV.hb, GIOV.hit].filter(h => h.visible !== false && (!h.parent || h.parent.visible !== false)), false); return hs.length ? (hs[0].object === GIOV.hb ? 'bub' : 'gio') : null; }
/* --- ghe chợ nổi (cấp 10): mỗi ngày một ghe bẹo ghé bến, đơn lớn nhiều món, trả cao --- */
const GHE = { lv: 10, mul: 1.6, from: 6 };
if (!ST.ghe) ST.ghe = { d: '', o: null, done: 0 };
const gheOn = () => (ST.lv || 1) >= GHE.lv;
function gheSim(){ const g = ST.ghe; if (!gheOn() || VISIT) return; const dk = dayKey(); if (g.d === dk) return; if (new Date().getHours() < GHE.from) return; g.d = dk; try { const a = ordMake(), b = ordMake(), m = new Map(); for (const [k, q] of [...a.items, ...b.items]) m.set(k, (m.get(k) || 0) + q);
  const items = [...m.entries()].slice(0, 4).map(([k, q]) => [k, Math.max(2, q)]), val = items.reduce((s2, [k, q]) => s2 + q * GD(k).sell, 0); g.o = { id: 'ghe' + Date.now(), who: pick(['Ghe bẹo cô Sáu', 'Ghe bẹo chú Mười', 'Ghe chợ nổi Cái Răng', 'Ghe bẹo dì Bảy']), why: 'đem ra chợ nổi Cái Răng bán', items, xu: Math.round(val * GHE.mul / 5) * 5, xp: 6 + items.length * 3, ghe: 1 }; } catch (e) {} }
function gheGive(el){ const g = ST.ghe, o = g.o; if (!o || !ordCan(o)) return; for (const [k, q] of o.items) STORE(k)[k] -= q; ST.xu += o.xu; g.o = null; g.done = (g.done || 0) + 1; if (el) coinFly(el, 7); sfx('coin'); coinPop(`+${o.xu} xu · ${o.who}`, '#9fd36a'); gainXP(o.xp);
  say(pick(['Ghe bẹo nhổ sào đi rồi, mai lại ghé. Hàng nhà mình đem ra chợ nổi bán chạy lắm con.', 'Cô Sáu khen hàng nhà mình đẹp, dặn mai để dành thêm.']), 'vui', { now: true }); save(); hud(); }
function gheHTML(){ const o = ST.ghe.o; if (!gheOn()) return ''; let h = '<div class="sub">Ghe chợ nổi</div>'; if (!o) return h + `<div class="note">${ST.ghe.d === dayKey() ? 'Ghe bẹo hôm nay đi rồi, mai sáng lại ghé.' : 'Sáng sớm ghe bẹo mới ghé bến con.'}</div>`;
  const ok = ordCan(o); return h + `<div class="ordr ghe${ok ? ' ok' : ''}"><div class="ow"><b>${o.who}</b><span>${o.why}</span></div><div class="oi">${o.items.map(([k, q]) => { const have = has(k); return `<span class="oit${have >= q ? ' got' : ''}"><img src="${ICON[k]}" alt=""><i>${Math.min(have, q)}/${q}</i></span>`; }).join('')}</div><div class="oa"><button class="btn g" data-a="ghegive" ${ok ? '' : 'disabled'}>Giao · ${o.xu} xu</button></div></div>`; }
const GHEV = (() => { const root = DYN(G(bx + 3.4, WLR + .06, R0 + 1.25, -.08)), pr = ROOT; ROOT = root;
  const hull = new T.CylinderGeometry(.24, .2, 1.9, 10, 1, false, 0, Math.PI); hull.rotateZ(Math.PI / 2); hull.rotateX(Math.PI); M(hull, '#6B4529', 0, .14, 0, { p: root, s: [1, .55, 1] });
  M(box(1.75, .03, .4), '#8A5D3B', 0, .15, 0, { p: root }); for (const sx of [-1, 1]) M(cone(.13, .3, 4), '#6B4529', sx * .98, .2, 0, { p: root, r: [0, 0, -sx * Math.PI / 2] });
  for (const sx of [-1, 1]){ M(sph(.04, 6, 4), '#FBF7EE', sx * .78, .2, .19, { p: root }); M(sph(.02, 5, 4), '#1a1a1a', sx * .78, .2, .225, { p: root }); }   // mắt ghe
  const mui = G(.15, .15, 0, 0, root); M(new T.CylinderGeometry(.24, .24, .5, 8, 1, true, 0, Math.PI), '#C9A66B', 0, .14, 0, { p: mui, r: [0, 0, Math.PI / 2], ds: true });   // mui ghe
  M(cyl(.018, .022, 1.5, 5), C.bamboo, -.55, .85, 0, { p: root });   // cây bẹo treo hàng mẫu
  for (const [y, c, s2] of [[1.45, '#E9C94A', 1], [1.25, '#F2D25A', .9], [1.05, '#8CC63F', .8]]){ M(cyl(.004, .004, .1, 3), '#8A6A4A', -.55, y + .08, 0, { p: root }); M(sph(.07 * s2, 6, 4), c, -.55, y, 0, { p: root, s: [1, 1.3, 1] }); }
  for (let k = 0; k < 6; k++) M(sph(.06, 6, 4), pick(['#8CC63F', '#E9C94A', '#E8453A', '#F08A3E']), .5 + R(-.2, .2), .22, R(-.1, .1), { p: root });   // trái cây trên ghe
  ROOT = pr; const hit = new T.Mesh(new T.BoxGeometry(2, 1.2, .8), new T.MeshBasicMaterial({ visible: false })); root.add(hit); hit.position.set(0, .4, 0); return { root, hit, ...mkBub() }; })();
function gheTick(t){ const on = gheOn() && !!ST.ghe.o && !VISIT; GHEV.root.visible = on; GHEV.b.visible = false; if (!on) return; GHEV.root.position.y = WLR + .06 + Math.sin(t * 1.4) * .012; GHEV.root.rotation.z = Math.sin(t * 1.1) * .015;
  const b = GHEV.b; b.visible = true; try { bubIcon(b, ICON.ghe); } catch (e) {} b.quaternion.copy(cam.quaternion); b.position.set(bx + 3.4, 1.0 + Math.sin(t * 2) * .035, R0 + 1.25); b.scale.setScalar(.9 * BUBS * (1 + .07 * Math.abs(Math.sin(t * 3)))); }
function gheHit(cx, cy){ if (!GHEV.root.visible) return false; ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); return ray.intersectObjects([GHEV.hb, GHEV.hit], false).length > 0; }
/* --- tre gai sau nhà (cấp 11): bụi tre gai che đất, dọn xong (việc lên cấp 12) thì mở 10 ô --- */
const TREV = (() => { const root = DYN(G(0, 0, 0)), pr = ROOT; ROOT = root; const ps = sd; sd = 4242;
  sway(.35, () => { for (let k = 0; k < 16; k++){ const x = R(SAU.x0, SAU.x0 + 4.4), z = R(SAU.z0, SAU.z0 + 1.4), g = G(x, 0, z, R(0, 6)); for (let j = 0; j < 5; j++){ const h = R(.8, 1.5); M(cyl(.018, .024, h, 5), pick([C.bamboo, '#8FA04A', '#A8A050']), R(-.08, .08), h / 2, R(-.08, .08), { p: g, r: [R(-.15, .15), 0, R(-.15, .15)] }); }
    for (let j = 0; j < 4; j++) leaf(g, R(.25, .4), .05, pick(['#5a8e3a', '#7aa84a', '#6E9F57']), j * 1.6, R(.5, .9), { droop: .4, cast: false }); } });
  sd = ps; ROOT = pr; root.visible = false; return { root }; })();
function treTick(){ TREV.root.visible = (ST.lv || 1) >= SAU.lv && !(ST.qd || {})[12]; }
/* --- Sổ vườn: mùa xoài đầu tiên ở cấp 12, Ngoại trao Sổ vườn --- */
function soVuon(){ if ((ST.lv || 1) < 12 || ST.sovuon) return; ST.sovuon = 1; save(); setTimeout(() => { say('Mùa xoài đầu tiên của con đó. Ngoại già rồi, cuốn Sổ vườn này Ngoại giao lại cho con giữ. Từ giờ vườn này là vườn của con.', 'vui', { now: true }); try { confetti($('#avb')); confetti($('#bSo')); } catch (e) {} sfx('up'); }, 900); }

