p='live/vuon3d.html'; s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,a[:90]; s=s.replace(a,b)
# --- vịt pen: pay now, build 2h, finish later
rep("function penFix(k){ const P = PENS[k], F = P.F, st = P.st(); if (st.fixed || !penCan(k)) return; ST.inv.rom -= F.rom; ST.tre -= F.tre; ST.xu -= F.xu; P.reset(); st.fixed = 1; coinPop(`-${F.xu} xu · ${k === 'ga' ? 'sửa' : 'dựng'} ${P.name}`, '#F08A6E'); const c = P.at();",
    "function penFix(k){ const P = PENS[k], F = P.F, st = P.st(); if (st.fixed || bldOn(k) || !penCan(k)) return; ST.inv.rom -= F.rom; ST.tre -= F.tre; ST.xu -= F.xu; coinPop(`-${F.xu} xu · ${k === 'ga' ? 'sửa' : 'dựng'} ${P.name}`, '#F08A6E'); if (BLDH[k]){ bldStart(k); RING.hidden = true; RINGID = null; save(); hud(); return; } penDone(k); }\nfunction penDone(k){ const P = PENS[k], st = P.st(); P.reset(); st.fixed = 1; const c = P.at();")
rep("for (const [k, P] of Object.entries(PENS)){ const fixed = !!P.st().fixed, show = !fixed && lv >= P.F.lv && !VISIT;",
    "for (const [k, P] of Object.entries(PENS)){ const fixed = !!P.st().fixed, show = !fixed && lv >= P.F.lv && !VISIT && !bldOn(k);")
rep("if (need && ST.odd){", "if (need && ST.odd && !bldOn(need)){")
rep("function penRing(k){ const P = PENS[k], F = P.F, r = ST.inv.rom || 0, tr = ST.tre || 0, ok = penCan(k);", "function penRing(k){ if (bldOn(k)) return bldTell(k); const P = PENS[k], F = P.F, r = ST.inv.rom || 0, tr = ST.tre || 0, ok = penCan(k);")
# --- ao: build 2h
rep("ST.xu -= D.buy; ST.big.ao = { own: 1, at: null }; bigPlace('ao', a); coinPop(`-${D.buy} xu · đào ao cá`, '#F08A6E'); hud(); closeSheet(); say('Đào ao xong rồi! Cá nào con câu được, đẹp nhất Ngoại thả vô ao nuôi. Bạn bè ghé chơi là thấy liền.', 'vui', { now: true }); sfx('up'); }",
    "ST.xu -= D.buy; ST.big.ao = { own: 1, at: null }; bigPlace('ao', a); coinPop(`-${D.buy} xu · đào ao cá`, '#F08A6E'); hud(); closeSheet(); bldStart('ao'); sfx('pop'); }")
rep("function aoTick(t){ const B = ST.big.ao, c = B && B.own ? bigCenter('ao') : null;", "function aoTick(t){ const B = ST.big.ao, c = B && B.own && !bldOn('ao') ? bigCenter('ao') : null;")
# --- lò sấy: build 4h
rep("ST.xu -= D.buy; O.own = 1; O.at = at; coinPop(`-${D.buy} xu · ${D.name}`, '#F08A6E'); sfx('up'); save(); refreshPlot(at); hud(); objPuff(at); say(D.hi, 'vui', { now: true });",
    "ST.xu -= D.buy; O.own = 1; O.at = at; coinPop(`-${D.buy} xu · ${D.name}`, '#F08A6E'); sfx('up'); save(); refreshPlot(at); hud(); objPuff(at); if (BLDH[k]) bldStart(k); else say(D.hi, 'vui', { now: true });")
rep("function sayTick(t, dt){ const v = objRoot(SAYV, 'say', t); if (!v) return;", "function sayTick(t, dt){ const v = objRoot(SAYV, 'say', t); if (!v) return; if (bldOn('say')){ SAYV.root.visible = false; return; }")
rep("{ const ok = HP && HP.bai && objAt(hid); if (ok){", "{ const ok = HP && HP.bai && objAt(hid); if (ok && bldOn(ok) && !SUA){ bldTell(ok); return; } if (ok){")
# --- the build system
rep("function maiTick(t){", r'''const BLDH = { vit: 2, ao: 2, say: 4 }, BLDN = { vit: 'Xóm qua dựng chuồng vịt', ao: 'Xóm qua đào ao', say: 'Xóm qua xây lò sấy' }, BLDV = {};   /* món lớn xây có thời gian chờ, bạn ghé vườn phụ bớt 1 tiếng (tối đa nửa thời gian) */
const bldOn = k => !!(ST.bld && ST.bld[k] && !ST.bld[k].done);
function bldStart(k){ ST.bld = ST.bld || {}; ST.bld[k] = { t: Date.now(), help: 0 }; save(); const at = bldAt(k); if (at && !VISIT){ camTo(new T.Vector3(at[0], .3, at[1]), Math.max(cam.zoom, DEFZ() * 1.1)); for (let i = 0; i < 16; i++) puff('leaf', at[0] + R(-.4, .4), .3, at[1] + R(-.4, .4), 1, pick(['#C9952A', '#B48560', '#86B06A']), .8); } toast(`${BLDN[k]} · chừng ${BLDH[k]} tiếng`); }
function bldLeft(k){ const B = ST.bld && ST.bld[k]; if (!B || B.done) return 0; return Math.max(0, (BLDH[k] - Math.min(BLDH[k] / 2, B.help || 0)) * 3600e3 / (ST.spd || 1) - (Date.now() - B.t)); }
function bldTell(k){ const l = bldLeft(k), h = Math.floor(l / 3600e3), m = Math.max(1, Math.ceil((l % 3600e3) / 60000)); toast(`${BLDN[k]} · còn ${h ? h + ' tiếng ' : ''}${m} phút · bạn ghé phụ bớt 1 tiếng`); }
function bldAt(k){ if (k === 'vit') return [VIT.at[0], VIT.at[1]]; if (k === 'ao') return bigCenter('ao'); const O = ST[k]; if (O && O.at && PV[O.at]) return [PV[O.at].cx, PV[O.at].cz]; return null; }
function bldDone(k){ const B = ST.bld[k]; B.done = 1; save(); const at = bldAt(k); if (at && !VISIT) for (let i = 0; i < 20; i++) puff('spark', at[0] + R(-.5, .5), .6, at[1] + R(-.5, .5), 1, pick(['#F5D27A', '#FBF7EE']), .8);
  if (k === 'vit') penDone('vit'); else if (k === 'ao') setTimeout(() => say('Đào ao xong rồi! Cá nào con câu được, đẹp nhất Ngoại thả vô ao nuôi. Bạn bè ghé chơi là thấy liền.', 'vui', { idle: true }), 300); else if (OBJD[k]) setTimeout(() => say(OBJD[k].hi, 'vui', { idle: true }), 300); sfx('up'); hud(); }
function scaffold(s = 1){ const g = new T.Group(), pr = ROOT; ROOT = g;   /* chỗ đang xây: cột tre, đà ngang, bó tre, đống lá, cây cuốc */
  for (const [x, z] of [[-.38, -.32], [.38, -.32], [-.38, .32], [.38, .32]]) M(cyl(.022, .026, .85, 6), '#B9A45A', x * s, .42, z * s);
  for (const z of [-.32, .32]) M(cyl(.016, .016, .82 * s, 5), '#A08A4A', 0, .7, z * s, { r: [0, 0, Math.PI / 2] }); for (const x of [-.38, .38]) M(cyl(.016, .016, .7 * s, 5), '#A08A4A', x * s, .74, 0, { r: [Math.PI / 2, 0, 0] });
  for (const x of [-.38, .38]) for (const z of [-.32, .32]) M(new T.TorusGeometry(.03, .008, 3, 8), '#6B4529', x * s, .7, z * s, { r: [Math.PI / 2, 0, 0], cast: false });
  const bt = G(.1 * s, .04, .55 * s, .3, g); for (let k = 0; k < 4; k++) M(cyl(.022, .022, .8, 6), k % 2 ? '#9CBF52' : '#8DB04A', 0, .02 + (k > 1 ? .04 : 0), -.05 + (k % 2) * .05, { p: bt, r: [0, 0, Math.PI / 2] });
  const lp = G(-.5 * s, 0, .45 * s, -.4, g); for (let k = 0; k < 6; k++) M(box(.36, .015, .1), k % 2 ? '#C9AE52' : '#D9B95A', 0, .01 + k * .016, (k % 3 - 1) * .03, { p: lp, r: [0, k * .15, 0] });
  const hoe = G(.42 * s, 0, .5 * s, .8, g); M(cyl(.012, .012, .5, 4), '#8A5D3B', 0, .03, 0, { p: hoe, r: [0, 0, Math.PI / 2 - .1] }); M(box(.05, .02, .09), '#8C8C88', .25, .04, 0, { p: hoe });
  ROOT = pr; return g; }
function bldTick(t){ if (!ST.bld) return; for (const k in BLDH){ const B = ST.bld[k]; let V = BLDV[k]; const on = !!(B && !B.done); if (!on){ if (V) V.root.visible = false, V.b.visible = false; continue; }
    if (!VISIT && bldLeft(k) <= 0){ bldDone(k); continue; } const at = bldAt(k); if (!at) continue;
    if (!V){ V = BLDV[k] = { root: DYN(G(0, 0, 0)), ...mkBub() }; V.root.add(scaffold(k === 'ao' ? 1.6 : 1)); } V.root.visible = true; V.root.position.set(at[0], 0, at[1]); V.b.visible = false; if (!VISIT) objBub(V, { cx: at[0], cz: at[1] }, ICON.cuoc || UIC.task, t, 1.25); } }
function maiTick(t){ bldTick(t);''')
# hit for building bubbles
rep("if (MAIV.b && MAIV.b.visible && MAIV.hb && ray.intersectObject(MAIV.hb, false).length) return { mai: 1 };",
    "if (MAIV.b && MAIV.b.visible && MAIV.hb && ray.intersectObject(MAIV.hb, false).length) return { mai: 1 }; for (const k in BLDV){ const V = BLDV[k]; if (V.b.visible && V.hb && ray.intersectObject(V.hb, false).length) return { bld: k }; }")
rep("if (fh){ if (fh.mai){", "if (fh){ if (fh.bld){ bldTell(fh.bld); return; } if (fh.mai){")
# friends help
rep("if (ST.mai && !ST.mai.done) ST.mai.help = Math.min(MAI.help, (ST.mai.help || 0) + Object.keys(by).length);",
    "if (ST.mai && !ST.mai.done) ST.mai.help = Math.min(MAI.help, (ST.mai.help || 0) + Object.keys(by).length); for (const k in (ST.bld || {})) if (!ST.bld[k].done) ST.bld[k].help = (ST.bld[k].help || 0) + Object.keys(by).length;")
open(p,'w').write(s); print('ok')
