p='live/vuon3d.html'; s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:90],s.count(a)); s=s.replace(a,b)
rep("const EXTRA = { trungga: { name: 'Trứng gà', sell: 25, unit: 'trứng' },", "const EXTRA = { matong: { name: 'Mật ong', sell: 70, unit: 'hũ' }, trungga: { name: 'Trứng gà', sell: 25, unit: 'trứng' },")
rep("  ho: { name: 'hố ủ phân', title: 'Hố ủ phân', lv: 8, buy: 100, sheet: 'ho',", "  ong: { name: 'thùng ong', title: 'Thùng ong', lv: 17, buy: 500, sheet: 'ong', hi: 'Ong về rồi đó con! Vườn mình nhiều bông, ong lấy mật đầy thùng. Có ong thì cây trái cũng đậu trái nhiều hơn.' },\n  ho: { name: 'hố ủ phân', title: 'Hố ủ phân', lv: 8, buy: 100, sheet: 'ho',")
rep("if (!ST.ho) ST.ho = { own: 0, at: null, mat: 0, t: 0, bags: 0, done: 0 };", "if (!ST.ho) ST.ho = { own: 0, at: null, mat: 0, t: 0, bags: 0, done: 0 }; if (!ST.ong) ST.ong = { own: 0, at: null, n: 1, t: 0, honey: 0, got: 0 };")
# icons
rep("  icon('catre', p => {", "  icon('matong', p => { add(p, new T.CylinderGeometry(.2, .17, .34, 10), '#E8A93A', 0, 0, 0); add(p, new T.CylinderGeometry(.21, .21, .07, 10), '#8A5D3B', 0, .2, 0); add(p, new T.TorusGeometry(.2, .02, 4, 14), '#C9A04A', 0, .16, 0, [Math.PI / 2, 0, 0]); add(p, new T.BoxGeometry(.18, .14, .01), '#FBF7EE', 0, -.02, .19); add(p, new T.SphereGeometry(.05, 6, 5), '#F2C230', .08, -.02, .2, null, [1.4, 1, 1]); add(p, new T.BoxGeometry(.012, .07, .07), '#2B2B2B', .09, -.02, .21); });   /* hũ mật ong */\n  icon('catre', p => {")
# model view + logic
rep("function scaffold(s = 1){", r'''const ONG = { h0: 12, hMin: 6, cap: 2, up: 400 };   /* thùng ong cấp 17: ong lấy mật từ bông trong vườn; vườn càng nhiều cây, nhiều chậu bông thì mật đầy càng mau */
const ONGV = (() => { const root = DYN(G(0, 0, 0)); return { root, m: null, key: '', bees: [], ...mkBub() }; })();
const ongBloom = () => { try { return PLOTS.filter(P => { const p = ST.plots[P.id]; return p && p.crop && !p.dead; }).length + ((ST.dc && ST.dc.items) || []).length; } catch (e) { return 0; } };
const ongH = () => Math.max(ONG.hMin, ONG.h0 - ongBloom() * .4);
function ongSim(){ const O = ST.ong; if (!O || !O.own) return; const now = Date.now(), T2 = ongH() * 3600e3 / (ST.spd || 1), cap = ONG.cap * (O.n || 1); if (!O.t) O.t = now; if (O.honey >= cap){ O.t = now; return; } let k = 0; while (now - O.t >= T2 && O.honey < cap && k++ < 10){ O.honey++; O.t += T2; } }
function ongTake(){ const O = ST.ong; if (!O || !O.honey) return false; const n = O.honey, v = PV[O.at]; ST.inv.matong = (ST.inv.matong || 0) + n; O.honey = 0; O.got = (O.got || 0) + n; O.t = Date.now(); if (v){ flyTo(ICON.matong, v.cx, .6, v.cz); floatAt(v.cx, .9, v.cz, `+${n} hũ mật ong`, '#F2C230'); } sfx('pop'); gainXP(2 * n); save(); hud(); sayOnce('ong1', 'Mật ong rừng tràm là quý nhất, mật ong vườn nhà cũng ngọt lắm con. Đem bán hay để Ngoại làm chuối nướng mật ong.', 'vui'); return true; }
function ongTick(t){ const v = objRoot(ONGV, 'ong', t); if (!v) return; ongSim(); const O = ST.ong, key = (O.n || 1) + ':' + (O.honey > 0 ? 1 : 0); if (key !== ONGV.key){ ONGV.key = key; if (ONGV.m) ONGV.root.remove(ONGV.m); const g = new T.Group(); ONGV.bees = []; const n = O.n || 1; for (let i = 0; i < n; i++){ const h = beeHive(O.honey > 0 && i === 0); h.scale.setScalar(n > 1 ? .78 : 1); h.position.set(n > 1 ? (i ? .2 : -.2) : 0, 0, n > 1 ? (i ? .06 : -.06) : 0); g.add(h); ONGV.bees.push(...h.userData.bees); } ONGV.m = g; ONGV.root.add(g); }
  beeAnim(ONGV.bees, t); if (O.honey > 0 && !VISIT) objBub(ONGV, v, ICON.matong, t, .95); }
const ongHit = (cx, cy) => bubHit(ONGV, cx, cy);
function ongHTML(){ const O = ST.ong, cap = ONG.cap * (O.n || 1); ongSim(); const left = O.honey >= cap ? 0 : Math.max(0, ongH() * 3600e3 / (ST.spd || 1) - (Date.now() - O.t)), hh = Math.floor(left / 3600e3), mm = Math.ceil((left % 3600e3) / 60000);
  let h = UX.hero(ICON.matong, O.honey ? `${O.honey} hũ mật chờ lấy` : 'Ong đang lấy mật', O.honey >= cap ? 'Thùng đầy rồi, lấy mật ra cho ong làm tiếp' : `Hũ kế tiếp còn ${hh ? hh + ' tiếng ' : ''}${mm} phút`, O.honey ? 'go' : '');
  h += UX.cta([UX.btn('ongtake', 'Lấy mật', { g: 1, img: ICON.matong, dis: !O.honey })]);
  h += '<div class="uxs">' + UX.card('Thùng ong', `${O.n || 1}/2`) + UX.card('Cây, chậu bông', ongBloom()) + UX.card('Một hũ', `${Math.round(ongH())} tiếng`) + '</div>';
  if ((O.n || 1) < 2) h += UX.cta([UX.btn('ongup', 'Thêm thùng thứ hai', { img: UIC.coin, dis: ST.xu < ONG.up, sub: `${ONG.up} xu` })]);
  return h + UX.more('Ong lấy mật', 'Vườn càng nhiều liếp có cây, nhiều chậu bông thì mật đầy càng mau, nhanh nhất sáu tiếng một hũ. Có ong thì cây trái mỗi vụ ra thêm một trái.'); }
'''+"function scaffold(s = 1){")
# sheet
rep("  if (kind === 'ho'){ shT.textContent = 'Hố ủ phân'; h += hoHTML(); }", "  if (kind === 'ho'){ shT.textContent = 'Hố ủ phân'; h += hoHTML(); }\n  if (kind === 'ong'){ shT.textContent = 'Thùng ong'; h += ongHTML(); }")
rep("else if (a === 'reset'){", "else if (a === 'ongtake'){ ongTake(); renderSheet(); return; } else if (a === 'ongup'){ if (ST.xu >= ONG.up && (ST.ong.n || 1) < 2){ ST.xu -= ONG.up; ST.ong.n = 2; coinPop(`-${ONG.up} xu · thùng ong thứ hai`, '#F08A6E'); sfx('up'); save(); hud(); } renderSheet(); return; } else if (a === 'reset'){")
# taps
rep("if (ok === 'say') lsay.takeAll();", "if (ok === 'say') lsay.takeAll(); if (ok === 'ong') ongTake();")
rep("if (hoHit(e.clientX, e.clientY)){ openSheet('ho'); return; }", "if (hoHit(e.clientX, e.clientY)){ openSheet('ho'); return; } if (ongHit(e.clientX, e.clientY)){ ongTake(); openSheet('ong'); return; }")
# tick
rep("try { nongTick(t); khapTick(t); hoTick(t);", "try { nongTick(t); khapTick(t); hoTick(t); ongTick(t);")
# tree bonus
rep("n = Math.max(1, Math.round(harvestN(p) * bonus) - (p.stolen || 0));", "n = Math.max(1, Math.round(harvestN(p) * bonus) - (p.stolen || 0) + (c.tree && ST.ong && ST.ong.own ? 1 : 0));")
# level feature + dishes
rep("16: [['ft_khevang', 'Cổ tích khế vàng']],", "16: [['ft_khevang', 'Cổ tích khế vàng']], 17: [['matong', 'Nuôi ong lấy mật'], ['chuoimat', 'Món mật ong']],")
rep("  banhchuoi: { name: 'Bánh chuối nướng',", "  chuoimat: { name: 'Chuối nướng mật ong', sell: 180, unit: 'dĩa', lv: 17, in: { chuoi: 2, matong: 1, cui: 1 }, t: 50 * 60, story: 'Chuối xiêm nướng than cho vàng, phết mật ong lên nướng thêm một lượt, thơm lừng. Tụi nhỏ trong xóm nghe mùi là chạy qua.' },\n  khemat: { name: 'Khế ngào mật ong', sell: 160, unit: 'hũ', lv: 17, in: { khe: 3, matong: 1, cui: 1 }, t: 70 * 60, story: 'Khế chua xắt lát, ngào với mật ong cho tới khi trong veo. Để dành uống với nước đá mùa nắng là mát ruột.' },\n  banhchuoi: { name: 'Bánh chuối nướng',")
open(p,'w').write(s); print('ok')
