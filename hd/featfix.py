#!/usr/bin/env python3
"""v101: (1) việc hôm nay theo đồ đã mở: đặt đồ mới mở (nong, khạp, lò sấy, hố phân, thùng ong), dùng đồ đã có (phơi, muối, sấy),
nấu bếp, câu cá, giao ghe bẹo, cho gà vịt ăn, lượm trứng, việc lặt vặt. Đồ mới mở ở cấp gần nhất ưu tiên trước; còn lại điền việc cơ bản.
(2) chuồng vịt lớn dần theo bậc nâng cấp: 8 con có ổ rơm thứ hai + cầu ván xuống mương; 12 con có mái lá lớn che chuồng + máng thứ hai."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# ---- hook đếm việc còn thiếu ----
rep("floatAt(x + .25, .45, z, `+${got} phần · ${parts.join(', ')}`, '#F5D27A'); sfx('pick'); buzz(10); gainXP(1); save(); hud(); },",
    "floatAt(x + .25, .45, z, `+${got} phần · ${parts.join(', ')}`, '#F5D27A'); sfx('pick'); buzz(10); gainXP(1); bump('feed'); save(); hud(); },")
rep("for (const [k, q] of o.items) STORE(k)[k] -= q; ST.xu += o.xu; g.o = null;", "for (const [k, q] of o.items) STORE(k)[k] -= q; ST.xu += o.xu; g.o = null; bump('ghe');")
rep("  put(i, k){ const N = ST.nong, d = PHOI[k]; if (!d || N.trays[i] || (ST.lv || 1) < d.lv || !phoiCan(k)) return;",
    "  put(i, k){ const N = ST.nong, d = PHOI[k]; if (!d || N.trays[i] || (ST.lv || 1) < d.lv || !phoiCan(k)) return; setTimeout(() => bump('nong'), 0);")
rep("  put(i, k){ const K = ST.khap, d = MUOI[k]; if (!d || K.jars[i] || (ST.lv || 1) < d.lv || !canIn(d.in)) return;",
    "  put(i, k){ const K = ST.khap, d = MUOI[k]; if (!d || K.jars[i] || (ST.lv || 1) < d.lv || !canIn(d.in)) return; setTimeout(() => bump('khap'), 0);")
rep("  put(i, k){ const L = ST.say, d = SAYR[k]; if (!d || L.trays[i] || (ST.lv || 1) < d.lv || !canIn(d.in)) return; if (((ST.gb || {}).cui || 0) < 1) return say(",
    "  put(i, k){ const L = ST.say, d = SAYR[k]; if (!d || L.trays[i] || (ST.lv || 1) < d.lv || !canIn(d.in)) return; if (((ST.gb || {}).cui || 0) >= 1) setTimeout(() => bump('say'), 0); if (((ST.gb || {}).cui || 0) < 1) return say(")

# ---- bộ việc theo đồ đã mở ----
rep("function ensureTasks(){ const dk = dayKey();",
    r"""/* việc theo những thứ đã mở; lv = cấp mở, càng mới càng ưu tiên */
const ownObj = k => !!(ST[k] && ST[k].own);
function featTasks(){ const lv = ST.lv || 1, F = [];
  try { for (const k of ['nong', 'khap', 'ho', 'say', 'ong']){ const d = OBJD[k]; if (!d || lv < d.lv) continue; if (!ownObj(k)) F.push({ lv: d.lv + .5, t: 'own', k, txt: `Đặt ${d.name} trong vườn`, need: 1, rw: ['coin', 20] }); } } catch (e) {}
  try { if (ownObj('nong')) F.push({ lv: OBJD.nong.lv, t: 'nong', txt: 'Phơi 1 nong', need: 1, rw: ['coin', 15] }); if (ownObj('khap')) F.push({ lv: OBJD.khap.lv, t: 'khap', txt: 'Muối 1 khạp', need: 1, rw: ['coin', 20] }); if (ownObj('say')) F.push({ lv: OBJD.say.lv, t: 'say', txt: 'Sấy 1 mẻ ở lò', need: 1, rw: ['coin', 25] }); } catch (e) {}
  try { if (lv >= BEP.lv) F.push({ lv: BEP.lv, t: 'cook', txt: 'Nấu 1 món ở bếp Ngoại', need: 1, rw: ['coin', 20] }); } catch (e) {}
  try { if (cauOn()) F.push({ lv: CAU.lv, t: 'fish', txt: 'Câu 2 con cá', need: 2, rw: ['coin', 20] }); } catch (e) {}
  try { if (gheOn()) F.push({ lv: GHE.lv, t: 'ghe', txt: 'Giao hàng cho ghe bẹo', need: 1, rw: ['coin', 25] }); } catch (e) {}
  try { const ga = gaOn(), vi = vitOn(); if (ga || vi){ const L0 = vi ? VIT.lv : GA.lv; F.push({ lv: L0, t: 'feed', txt: ga && vi ? 'Cho gà vịt ăn 2 lần' : vi ? 'Cho vịt ăn 2 lần' : 'Cho gà ăn 2 lần', need: 2, rw: ['coin', 15] }); F.push({ lv: L0 - .1, t: 'egg', txt: 'Lượm 4 trứng', need: 4, rw: ['coin', 20] }); } } catch (e) {}
  try { if (lv >= 2) F.push({ lv: 2, t: 'odd', txt: 'Làm 2 việc lặt vặt quanh vườn', need: 2, rw: ['coin', 15] }); } catch (e) {}
  return F; }
function ownCheck(){ try { ensureTasks(); for (const x of ST.tasks.list) if (x.t === 'own' && !x.done && ownObj(x.k)) bump('own', 1, x.k); } catch (e) {} }
setInterval(ownCheck, 2500);
function ensureTasks(){ const dk = dayKey();""")
rep("const pool = TASKT.slice(), list = []; while (list.length < 5 && pool.length) list.push(pool.splice(Math.floor(r() * pool.length), 1)[0](r));",
    """const pool = TASKT.slice(), list = []; { const F = featTasks().sort((a, b) => b.lv - a.lv); if (F.length){ list.push(F.shift()); const nf = Math.min(F.length, 2); for (let i = 0; i < nf; i++) list.push(F.splice(Math.floor(r() * Math.min(F.length, 4)), 1)[0]); } }   /* thứ mới mở nhất luôn có việc, thêm 2 việc theo đồ đã có */
  while (list.length < 5 && pool.length){ const x = pool.splice(Math.floor(r() * pool.length), 1)[0](r); if (!list.some(y => y.t === x.t)) list.push(x); }""")
# lên cấp: làm lại việc hôm nay để có việc của đồ mới mở (giữ việc đã xong, đã nhận)
rep("function checkLevel(){", "function tasksRefresh(){ try { ensureTasks(); const T2 = ST.tasks, have = new Set(T2.list.map(x => x.t + ':' + (x.k || ''))), F = featTasks().sort((a, b) => b.lv - a.lv).filter(f => !have.has(f.t + ':' + (f.k || ''))); let i = T2.list.length - 1; for (const f of F.slice(0, 2)){ while (i >= 0 && (T2.list[i].done || T2.list[i].have > 0)) i--; if (i < 0) break; T2.list[i] = { ...f, have: 0, done: false }; i--; } soBadge(); } catch (e) {} }   /* lên cấp: đổi việc chưa đụng tới thành việc của đồ mới mở */\nfunction checkLevel(){")
rep("function levelUp(n){", "function levelUp(n){ setTimeout(() => { try { tasksRefresh(); if (BOOK) renderBook(); } catch (e) {} }, 400);")
# icon + bay tới cho việc mới
rep("const TASKIC = x => x.t === 'water' ? UIC.can :",
    "const TASKIC = x => x.t === 'own' ? (UIC['ob_' + x.k] || ICON[x.k] || ICON.nong || UIC.task) : x.t === 'nong' ? (ICON.nong || ICON.otkho) : x.t === 'khap' ? (ICON.khap || ICON.dacai) : x.t === 'say' ? (ICON.say || ICON.mutkhe) : x.t === 'cook' ? (ICON.canhchuaca || ICON.com) : x.t === 'fish' ? (ICON.caro || UIC.task) : x.t === 'ghe' ? ICON.ghe : x.t === 'feed' ? (ICON.lucbinh || ICON.bap) : x.t === 'egg' ? (ICON.trungvit || ICON.trungga) : x.t === 'odd' ? (ICON.la || ICON.sau || UIC.task) : x.t === 'water' ? UIC.can :")
rep("  else if (t === 'sell'){ openSheet('cho'); return; }",
    """  else if (t === 'own'){ try { suaOn(true); } catch (e) {} toast(`Chạm một ô đất trống để đặt ${(OBJD[k] || {}).name || 'đồ mới'}`); return; }
  else if (t === 'nong' || t === 'khap' || t === 'say'){ const O = ST[t]; if (O && O.at && PV[O.at]){ const w = PV[O.at]; camTo(new T.Vector3(w.cx, .3, w.cz), Math.max(cam.zoom, DEFZ() * 1.2)); setTimeout(() => { pingAt(w.cx, w.cz); openSheet(t); }, 700); } else openSheet(t); return; }
  else if (t === 'cook'){ openSheet('bep'); return; } else if (t === 'fish'){ openSheet('ben'); return; }
  else if (t === 'ghe'){ const p = GHEV.root.position; camTo(new T.Vector3(p.x, .3, p.z - .6), Math.max(cam.zoom, DEFZ() * 1.15)); setTimeout(() => pingAt(p.x, p.z), 450); return; }
  else if (t === 'feed' || t === 'egg'){ try { penGo(vitOn() ? 'vit' : 'ga'); } catch (e) {} return; }
  else if (t === 'sell'){ openSheet('cho'); return; }""")
# đổi số đếm việc cũ trên thẻ: cần thêm dòng 'đi làm' cho việc mới → pgTasks dùng data-k t:k sẵn

# ---- chuồng vịt lớn dần ----
rep("  ROOT = pr; const hit = new T.Mesh(new T.BoxGeometry(1.2, .7, .9), new T.MeshBasicMaterial({ visible: false })); hit.position.set(x, .3, z); S.add(hit);\n  const bE = bubbleK('h'), bF = bubbleK('h'); return { root, eggs, feed, hit, struct, bE, bF,",
    r"""  const up1 = G(0, 0, 0, 0, root), up2 = G(0, 0, 0, 0, root);   /* nâng cấp nhìn thấy được: 8 con, 12 con */
  { const pr2 = ROOT; ROOT = up1; M(new T.CylinderGeometry(.11, .085, .05, 9), '#B48560', .2, .03, -.18, { p: up1 }); for (let k = 0; k < 3; k++) M(sph(.03, 7, 5), k % 2 ? '#E2F0EA' : '#CFE6DC', .17 + k * .035, .065, -.18 + (k % 2) * .02, { p: up1, s: [.85, 1.15, .85], cast: false });
    for (let k = 0; k < 7; k++) M(box(.07, .018, .3), k % 2 ? '#B48560' : '#A07450', -.62 - k * .075, .06 - k * .03, .05, { p: up1, r: [0, 0, -.38] });   /* cầu ván tre thả xuống mương cho vịt lội */
    for (const z2 of [-.11, .21]) M(cyl(.012, .014, .62, 4), '#8A5D3B', -.8, .0, z2, { p: up1, r: [0, 0, Math.PI / 2 - .38], cast: false });
    ROOT = up2; for (const [px, pz] of [[-.5, -.36], [.5, -.36], [-.5, .36], [.5, .36]]) M(cyl(.022, .026, .62, 5), '#8A5D3B', px, .31, pz, { p: up2 });
    for (const sz of [-1, 1]){ const r2 = G(0, .66, sz * .21, 0, up2); r2.rotation.x = sz * .5; for (let k = 0; k < 4; k++) M(box(1.18, .025, .13), k % 2 ? C.thatch : C.thatchD, 0, 0, sz * (-.16 + k * .105), { p: r2 }); }
    M(box(1.2, .04, .05), '#6B4529', 0, .74, 0, { p: up2 });
    const mg2 = new T.CylinderGeometry(.06, .06, .42, 8, 1, true, 0, Math.PI); M(mg2, C.bamboo, -.05, .05, .27, { p: up2, r: [0, 0, Math.PI / 2], ds: true }); for (let k = 0; k < 5; k++) M(box(.06, .012, .03), '#5aa83e', -.2 + k * .07, .06, .27, { p: up2, r: [0, k, 0], cast: false });
    ROOT = pr2; }
  ROOT = pr; const hit = new T.Mesh(new T.BoxGeometry(1.2, .7, .9), new T.MeshBasicMaterial({ visible: false })); hit.position.set(x, .3, z); S.add(hit);
  const bE = bubbleK('h'), bF = bubbleK('h'); return { root, eggs, feed, hit, struct, bE, bF, up1, up2,""")
rep("function vitTick(t){ const on = vitOn(), v = ST.vit; VITV.root.visible = on;",
    "function vitTick(t){ const on = vitOn(), v = ST.vit; VITV.root.visible = on; VITV.up1.visible = (v.lv || 0) >= 1; VITV.up2.visible = (v.lv || 0) >= 2;")
rep("v.lv = nx; coinPop(`-${c} xu · chuồng vịt ${VIT.caps[nx]} con`, '#F08A6E'); sfx('up');",
    "v.lv = nx; coinPop(`-${c} xu · chuồng vịt ${VIT.caps[nx]} con`, '#F08A6E'); sfx('up'); try { closeSheet(); camTo(new T.Vector3(VIT.at[0], .3, VIT.at[1]), Math.max(cam.zoom, DEFZ() * 1.6)); setTimeout(() => { for (let i = 0; i < 18; i++) puff('spark', VIT.at[0] + R(-.5, .5), .4, VIT.at[1] + R(-.4, .4), 1, pick(['#F5D27A', '#FBF7EE', '#86B06A']), .7); }, 600); } catch (e) {}")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
