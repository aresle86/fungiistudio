#!/usr/bin/env python3
"""Bộ giao diện "Ván gỗ, giấy dó" (đợt UI2): mặt nhân vật ôm sát mặt cầu, icon Bạn bè áo bà ba nón lá, icon nút kiểu sticker viền đậm,
bỏ khay nút, thẻ việc dạng giấy ghim trên ván, thanh tiến độ số nằm giữa thanh, bảng khung ván + ghim đỏ + nút đóng tròn đỏ, nút khối dày.
Dùng: python3 ui2fix.py <vào> <ra>. Mỗi chỗ vá khớp đúng 1 lần."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b):
    global s
    c = s.count(a); assert c == 1, (c, a[:110]); s = s.replace(a, b)

# ---------- A. mặt nhân vật: miệng, má ôm theo mặt cầu (trước đây là đĩa phẳng, nhìn nghiêng lòi ra như lưỡi) ----------
rep("""  if (a.smile === 'open'){ M(new T.CircleGeometry(.065, 12, Math.PI, Math.PI), '#9E3B24', 0, -.1, z - .006, { p: h, r: [-.3, 0, 0] }); M(new T.CircleGeometry(.032, 10, Math.PI, Math.PI), '#E8453A', 0, -.138, z - .009, { p: h, r: [-.3, 0, 0], s: [1.2, .6, 1] }); }
  else { const m = M(new T.TorusGeometry(.05, .011, 3, 10, 2.2), '#9E3B24', 0, -.065, z - .012, { p: h }); m.rotation.set(-.3, 0, Math.PI + .48); }""",
"""  { const FZ = (x, y) => .288 * Math.sqrt(Math.max(0, 1 - (x / .312) ** 2 - (y / .288) ** 2)), conf = (geo, ox, oy, lift, dz = 1) => { geo = geo.index ? geo.toNonIndexed() : geo; const P = geo.attributes.position; for (let i = 0; i < P.count; i++){ const x = P.getX(i) + ox, y = P.getY(i) + oy; P.setXYZ(i, x, y, FZ(x, y) + lift + P.getZ(i) * dz); } geo.computeVertexNormals(); return geo; };   /* chi tiết mặt uốn theo mặt cầu đầu, nằm sát da, nhìn nghiêng không lòi ra */
    if (a.smile === 'open'){ M(conf(new T.CircleGeometry(.065, 14, Math.PI, Math.PI), 0, -.1, .004), '#9E3B24', 0, 0, 0, { p: h, ds: true, cast: false }); const tg = new T.CircleGeometry(.032, 12, Math.PI, Math.PI); tg.scale(1.2, .6, 1); M(conf(tg, 0, -.138, .006), '#E8453A', 0, 0, 0, { p: h, ds: true, cast: false }); }
    else { const tg = new T.TorusGeometry(.05, .011, 4, 12, 2.2); tg.rotateZ(Math.PI + .48); M(conf(tg, 0, -.065, .006, .5), '#9E3B24', 0, 0, 0, { p: h, cast: false }); } }""")
rep("""M(ball(.052, 1), '#F08A6E', sx * .16, -.07, z - .03, { p: h, s: [1, .6, .3] });""",
    """{ const cg = new T.CircleGeometry(.05, 12); cg.scale(1, .6, 1); const P = cg.attributes.position, FZ = (x, y) => .288 * Math.sqrt(Math.max(0, 1 - (x / .312) ** 2 - (y / .288) ** 2)); for (let i = 0; i < P.count; i++){ const x = P.getX(i) + sx * .16, y = P.getY(i) - .07; P.setXYZ(i, x, y, FZ(x, y) + .003); } cg.computeVertexNormals(); M(cg, '#F08A6E', 0, 0, 0, { p: h, ds: true, cast: false }); }""")

# ---------- A2. trang phục chi tiết hơn: áo bà ba (cổ tròn, hàng nút, 2 túi, tà trước tà sau xẻ hông, ống tay lỡ có viền), quần ống rộng có lai;
#              Gió: sơ mi mở khoác ngoài áo thun trắng (thấy rõ cổ thun, hai vạt sơ mi có ve, tay sơ mi xắn) ----------
rep("""  M(ball(.24, 1), a.shirt, 0, .46, 0, { p: g, s: [1, .95, .86] }); M(cyl(.21, .245, .1, 9), a.shirt, 0, .31, 0, { p: g });
  if (a.open){ M(box(.16, .24, .02), '#F2EEE4', 0, .45, .2, { p: g }); for (const sx of [-1, 1]) M(box(.06, .26, .022), a.shirt, sx * .11, .45, .195, { p: g, r: [0, 0, sx * .08] }); }
  else for (const y of [.36, .46, .56]) M(ball(.018, 1), btn, 0, y, .21, { p: g });
  for (const sx of [-1, 1]) M(box(.09, .03, .05), a.shirt, sx * .06, .63, .14, { p: g, r: [.4, 0, -sx * .6] });   // cổ áo""",
"""  { const dk = new T.Color(a.shirt).multiplyScalar(.78).getStyle(), TEE = '#F4F1EA', sp = (r, ph0, phL, th0, thL, col, y = .46) => M(new T.SphereGeometry(r, 18, 12, ph0, phL, th0, thL), col, 0, y, 0, { p: g, s: [1, .95, .86], ds: true });   /* phi = π/2 là mặt trước (+z) */
    if (a.open){ M(ball(.24, 1), TEE, 0, .46, 0, { p: g, s: [1, .95, .86] }); M(cyl(.21, .235, .1, 9), TEE, 0, .31, 0, { p: g });   /* áo thun trắng bên trong */
      M(new T.TorusGeometry(.065, .014, 4, 14), '#D8D2C4', 0, .64, .07, { p: g, r: [1.2, 0, 0], cast: false });   /* cổ thun tròn */
      sp(.252, Math.PI / 2 + .3, Math.PI * 2 - .6, .25, 2.55, a.shirt);   /* sơ mi mở: bọc vòng ra sau, chừa khoảng trước ngực thấy áo thun */
      M(new T.CylinderGeometry(.218, .252, .12, 18, 1, true, Math.PI / 2 + .3, Math.PI * 2 - .6), a.shirt, 0, .3, 0, { p: g, ds: true });   /* vạt sơ mi dài hơn áo thun */
      for (const sx of [-1, 1]){ const v = G(sx * .075, .5, .2, 0, g); v.rotation.set(-.15, 0, sx * .1); M(box(.04, .3, .015), dk, 0, 0, 0, { p: v }); M(box(.06, .07, .016), dk, sx * .02, .14, -.01, { p: v, r: [0, 0, sx * .5] }); }   /* nẹp và ve áo */
      M(box(.07, .06, .012), dk, .12, .44, .2, { p: g, r: [0, .35, 0] }); }   /* túi ngực sơ mi */
    else { M(ball(.24, 1), a.shirt, 0, .46, 0, { p: g, s: [1, .95, .86] }); M(cyl(.21, .245, .1, 9), a.shirt, 0, .31, 0, { p: g });
      M(new T.TorusGeometry(.068, .016, 4, 14), dk, 0, .635, .065, { p: g, r: [1.2, 0, 0], cast: false });   /* cổ tròn bà ba */
      M(box(.022, .3, .012), dk, 0, .44, .205, { p: g, r: [-.12, 0, 0], cast: false }); for (const y of [.33, .41, .49, .57]) M(ball(.017, 1), btn, 0, y, .213 + (y - .45) * -.12, { p: g });   /* nẹp + 4 nút */
      for (const sx of [-1, 1]){ M(box(.075, .065, .014), dk, sx * .11, .32, .198, { p: g, r: [0, sx * .32, 0], cast: false }); M(box(.075, .012, .016), new T.Color(a.shirt).multiplyScalar(.65).getStyle(), sx * .11, .352, .2, { p: g, r: [0, sx * .32, 0], cast: false }); } }   /* 2 túi dưới */
    for (const fz of [1, -1]) M(box(.36, .12, .03), a.open ? a.shirt : a.shirt, 0, .225, fz * .155, { p: g, r: [fz * -.12, 0, 0] });   /* tà trước, tà sau buông xuống, hở hai bên hông (xẻ tà) */
  }""")
rep("""  for (const sx of [-1, 1]){ const ar = G(sx * .2, .56, .02, 0, g); ar.rotation.z = sx * (o.wave && sx > 0 ? 2.4 : .3); M(ball(.075, 1), a.shirt, 0, 0, 0, { p: ar }); M(cyl(.058, .066, .2, 7), SKN, 0, -.11, 0, { p: ar });""",
"""  for (const sx of [-1, 1]){ const ar = G(sx * .2, .56, .02, 0, g); ar.rotation.z = sx * (o.wave && sx > 0 ? 2.4 : .3); M(ball(.075, 1), a.shirt, 0, 0, 0, { p: ar }); M(cyl(.058, .066, .2, 7), SKN, 0, -.11, 0, { p: ar }); M(cyl(.072, .076, .1, 8), a.shirt, 0, -.05, 0, { p: ar }); M(new T.TorusGeometry(.074, a.open ? .018 : .01, 4, 12), a.open ? a.shirt : new T.Color(a.shirt).multiplyScalar(.78).getStyle(), 0, -.1, 0, { p: ar, r: [Math.PI / 2, 0, 0], cast: false });   /* ống tay lỡ, viền tay (Gió: tay sơ mi xắn) */""")
rep("""M(cyl(.095, .125, .26, 8), a.pants, 0, -.12, 0, { p: lg });""","""M(cyl(.095, .125, .26, 8), a.pants, 0, -.12, 0, { p: lg }); M(new T.TorusGeometry(.122, .016, 4, 14), new T.Color(a.pants).multiplyScalar(.75).getStyle(), 0, -.235, 0, { p: lg, r: [Math.PI / 2, 0, 0], cast: false });   /* lai quần */""")
# ---------- A3. icon Hạt dựng lại: túi vải bố bầu, miệng túi xòe bèo, cột dây lác thắt nơ, nhãn giấy vẽ mầm cây, mầm non nhú lên, vài hạt rơi trước túi ----------
rep("""  shot('seedbag', () => { const g = G(0, 0, 0); M(box(.62, .8, .14), '#E3BC97', 0, .4, 0, { p: g }); M(box(.64, .1, .16), '#D2A57E', 0, .82, 0, { p: g }); for (let k = 0; k < 6; k++) M(box(.07, .04, .17), '#B48560', -.26 + k * .105, .88, 0, { p: g }); M(cyl(.18, .18, .02, 12), '#FBF7EE', 0, .42, .075, { p: g, r: [Math.PI / 2, 0, 0] }); M(cyl(.012, .015, .14, 5), '#6fae3a', 0, .4, .09, { p: g }); for (const sx of [-1, 1]){ const l = M(sph(.055, 6, 4), sx > 0 ? C.leafM : '#8fc84a', sx * .06, .48, .09, { p: g, s: [1.6, .7, .5] }); l.rotation.z = sx * .5; } }, new T.Vector3(.5, .45, 1));""",
"""  shot('seedbag', () => { const g = G(0, 0, 0), MM = {}, X = c => MM[c] || (MM[c] = new T.MeshStandardMaterial({ color: c, flatShading: true, roughness: .85, side: T.DoubleSide }));   /* túi hạt giống vải bố */
    const pf = [[0, 0], [.2, .006], [.3, .07], [.335, .2], [.32, .34], [.27, .46], [.18, .55], [.14, .6], [.15, .64], [.2, .69], [.25, .73], [.27, .745]].map(([r, y]) => new T.Vector2(r, y)), lg = new T.LatheGeometry(pf, 22), P = lg.attributes.position;
    for (let i = 0; i < P.count; i++){ const y = P.getY(i); if (y > .63){ const a = Math.atan2(P.getZ(i), P.getX(i)), k = 1 + Math.sin(a * 7) * .12 * (y - .63) / .115; P.setX(i, P.getX(i) * k); P.setZ(i, P.getZ(i) * k); P.setY(i, y + Math.sin(a * 7 + 1) * .018 * (y - .63) / .115); } }
    lg.computeVertexNormals(); M(lg, X('#D8AE72'), 0, 0, 0, { p: g });
    for (const y of [.12, .22, .32, .42]){ const t = new T.TorusGeometry(.3 + (y < .3 ? .03 : -.01) - (y > .4 ? .03 : 0), .005, 3, 28); M(t, X('#C29560'), 0, y, 0, { p: g, r: [Math.PI / 2, 0, 0], cast: false }); }   /* thớ vải */
    M(new T.CircleGeometry(.17, 18), X('#5A3A1E'), 0, .66, 0, { p: g, r: [-Math.PI / 2, 0, 0] }); for (let k = 0; k < 9; k++){ const a = k * 2.3, r = .05 + (k % 3) * .035; M(sph(.026, 6, 4), X(k % 2 ? '#E8C27A' : '#C9934A'), Math.cos(a) * r, .672, Math.sin(a) * r, { p: g, s: [1, .6, .75], cast: false }); }   /* hạt trong miệng túi */
    { const st = M(cyl(.014, .018, .2, 6), X('#6FAE3A'), .03, .76, .02, { p: g }); st.rotation.z = -.12; for (const [sx, c] of [[-1, '#8FCB4E'], [1, '#6FAE3A']]){ const l = G(.03 + sx * .02, .86, .02, 0, g); l.rotation.z = sx * -.9; M(sph(.07, 8, 6), X(c), sx * .06, 0, 0, { p: l, s: [1.5, .5, .9] }); } }   /* mầm non nhú lên */
    M(new T.TorusGeometry(.148, .02, 6, 24), X('#8A5D2E'), 0, .6, 0, { p: g, r: [Math.PI / 2, 0, 0] }); for (const sx of [-1, 1]){ M(new T.TorusGeometry(.045, .014, 5, 12), X('#8A5D2E'), sx * .05, .61, .17, { p: g, r: [0, 0, sx * .5], s: [1, .7, 1] }); const e = M(cyl(.011, .011, .12, 5), X('#8A5D2E'), sx * .035, .54, .165, { p: g }); e.rotation.z = sx * .35; } M(sph(.024, 6, 5), X('#6B4529'), 0, .61, .17, { p: g });   /* dây lác thắt nơ */
    M(new T.CylinderGeometry(.338, .338, .2, 16, 1, true, -.5, 1), X('#FBF3DC'), 0, .25, 0, { p: g }); M(new T.CylinderGeometry(.34, .34, .012, 16, 1, true, -.5, 1), X('#C24A2E'), 0, .344, 0, { p: g, cast: false }); M(new T.CylinderGeometry(.34, .34, .012, 16, 1, true, -.5, 1), X('#C24A2E'), 0, .156, 0, { p: g, cast: false });   /* nhãn giấy, viền đỏ */
    M(box(.012, .09, .01), X('#4E8A2E'), 0, .23, .343, { p: g, cast: false }); for (const sx of [-1, 1]){ const l = M(sph(.03, 8, 5), X(sx > 0 ? '#6FAE3A' : '#8FCB4E'), sx * .035, .285, .342, { p: g, s: [1.4, .65, .25], cast: false }); l.rotation.z = sx * .45; } M(box(.09, .012, .01), X('#8A5D2E'), 0, .185, .343, { p: g, cast: false });   /* mầm vẽ trên nhãn */
    for (const [x, z, c] of [[.3, .24, '#E8C27A'], [.36, .14, '#C9934A'], [.22, .32, '#C9934A'], [.4, .28, '#E8C27A'], [-.28, .26, '#E8C27A']]) M(sph(.028, 6, 4), X(c), x, .02, z, { p: g, s: [1, .55, .75] });   /* hạt rơi */
  }, new T.Vector3(.45, .5, 1));""")
# ---------- B. nón lá đội đầu (tuỳ chọn) + icon Bạn bè: ba người áo bà ba đội nón lá chụm vai, người giữa vẫy tay ----------
rep("""  // tóc""", """  if (o.hatOn){ const n = G(0, 1.23, -.02, 0, g); n.rotation.set(-.14, 0, -.05); M(new T.ConeGeometry(.41, .21, 16), '#EAD9B2', 0, 0, 0, { p: n }); for (let k = 1; k < 4; k++) M(new T.TorusGeometry(.41 * (1 - k / 4), .006, 3, 20), '#C9952A', 0, -.105 + .21 * k / 4, 0, { p: n, r: [Math.PI / 2, 0, 0], cast: false }); M(new T.TorusGeometry(.405, .012, 3, 24), '#B8862E', 0, -.105, 0, { p: n, r: [Math.PI / 2, 0, 0], cast: false }); }
  // tóc""")
anchor = "ri.render(sc, cm); OUT[kind].push(ri.domElement.toDataURL('image/png')); sc.traverse(o2 => o2.geometry && o2.geometry.dispose()); } }\n  ri.dispose(); ri.forceContextLoss(); sd = ps; return OUT; })();"
rep(anchor, """ri.render(sc, cm); OUT[kind].push(ri.domElement.toDataURL('image/png')); sc.traverse(o2 => o2.geometry && o2.geometry.dispose()); } }
  { ri.setSize(300, 240); const sc = new T.Scene(), root = new T.Group(); sc.add(root); const pr = ROOT; ROOT = root;   /* icon Bạn bè cho nút Ghé vườn */
    for (const [i, x, z, ry, sh] of [[0, -.64, -.1, .35, '#B5553A'], [1, .64, -.1, -.35, '#4E78A8'], [2, 0, .14, 0, '#D9A53A']]){ const gg = new T.Group(); gg.position.set(x, 0, z); gg.rotation.y = ry; root.add(gg); sd = 7; avBuild(gg, { ...AVS[[0, 3, 1][i]], shirt: sh, prop: null, smile: 'open', hair: ['bob', 'sweep', 'pony'][i] }, { hatOn: true, wave: i === 2 }); }
    ROOT = pr; sc.add(new T.HemisphereLight('#fff4e2', '#94a474', 1.6)); sc.add(new T.AmbientLight('#ffffff', .25)); const l = new T.DirectionalLight('#fff0d8', 1.6); l.position.set(-2, 5, 4); sc.add(l);
    const c = new T.Vector3(0, .8, 0), sz = .84, cm = new T.OrthographicCamera(-sz * 1.25, sz * 1.25, sz, -sz, .01, 100); cm.position.copy(c).add(new T.Vector3(.2, .25, 1).normalize().multiplyScalar(20)); cm.lookAt(c); ri.render(sc, cm); OUT.banbe = ri.domElement.toDataURL('image/png'); sc.traverse(o2 => o2.geometry && o2.geometry.dispose()); }
  ri.dispose(); ri.forceContextLoss(); sd = ps; return OUT; })();""")

# ---------- C. icon nút kiểu sticker: viền nâu đậm dày bao ngoài + bóng đổ, đứng nổi trên mọi nền ----------
rep("""$('#nxq').addEventListener('click', e => {""", r"""/* --- sticker: viền nâu đậm quanh hình (giãn alpha 16 hướng), bóng đổ mềm; dùng cho icon nút ở HUD --- */
const STKC = {};
function sticker(url, w = 3, col = '#3A2616'){ if (!url) return Promise.resolve(url); if (STKC[url]) return STKC[url]; return (STKC[url] = new Promise(res => { const im = new Image(); im.onload = () => { try { const p0 = w + 4, W = im.width + p0 * 2, H = im.height + p0 * 2 + 4, c = document.createElement('canvas'); c.width = W; c.height = H; const x = c.getContext('2d'), t = document.createElement('canvas'); t.width = W; t.height = H; const y = t.getContext('2d');   /* viền mảnh như ref: chỉ để icon tách khỏi nền; màu tươi hơn chút; bóng đổ nhẹ dưới chân */
      for (let k = 0; k < 20; k++){ const a = k / 20 * Math.PI * 2; y.drawImage(im, p0 + Math.cos(a) * w, p0 + Math.sin(a) * w); } y.globalCompositeOperation = 'source-in'; y.fillStyle = col; y.fillRect(0, 0, W, H);
      x.save(); x.globalAlpha = .22; x.drawImage(t, 0, 4); x.restore(); x.globalAlpha = .92; x.drawImage(t, 0, 0); x.globalAlpha = 1; x.filter = 'saturate(1.18) contrast(1.06)'; x.drawImage(im, p0, p0); x.filter = 'none'; res(c.toDataURL('image/png')); } catch (e) { res(url); } }; im.onerror = () => res(url); im.src = url; })); }
function stickerHud(){ for (const [id, u] of [['icSo', UIC.so], ['icCho', ICON.cho], ['icSet', ICON.set], ['icSeed', null], ['icRom', null], ['icCan', UIC.can], ['icCtr', UIC.center], ['icVuon', AVIMG.banbe]]){ const im = document.getElementById(id); if (!im) continue; const src = u || im.getAttribute('src'); if (!src || im.dataset.stk === src) continue; im.dataset.stk = src; sticker(src).then(d => { im.src = d; im.dataset.stk = src; }); } }
setTimeout(stickerHud, 50); setTimeout(stickerHud, 1500);
$('#nxq').addEventListener('click', e => {""")
rep("""b.hidden = !on; if (!on) return; { const im = document.getElementById('icVuon'), u = (typeof UIC !== 'undefined' && UIC.tamban) || ICON.ghe; if (im && u && im.dataset.u !== u){ im.src = u; im.dataset.u = u; } } const n =""",
    """b.hidden = !on; if (!on) return; const n =""")

# ---------- E. thanh tiến độ trong thẻ việc: số nằm giữa thanh ----------
rep("""`<span class="nqb"><i><u style="width:${Math.round(Math.max(0, Math.min(1, f)) * 100)}%"></u></i><em>${em}</em></span>`""",
    """`<span class="nqb"><i><u style="width:${Math.round(Math.max(0, Math.min(1, f)) * 100)}%"></u><em>${em}</em></i></span>`""")

# ---------- D. CSS bộ "Ván gỗ, giấy dó" ----------
CSS = r"""
/* ===== UI2: Ván gỗ, giấy dó ===== */
:root{--vg:#9A6A3C;--vgD:#6B4529;--vgK:#4A2F1E;--dz:#FFF8EA;--dz2:#F6EBD3;--pin:#D9483A;--la:#7DB84A;--laD:#4E7A2E;--rom:#F2C64A;--romD:#B8862E}
.ui.bot>.row,#tray{background:none!important;box-shadow:none!important;padding:0!important}
.bt img,.tl img{filter:none!important}
.bt .tg,.tl .tg{font-size:13px;padding:2px 9px 3px;margin-top:-6px}
.bvn{right:8px;top:0}
/* thẻ việc: tờ giấy dó trên khung ván, ghim đỏ */
.nxq{background:var(--dz)!important;border:3px solid var(--vg);box-shadow:0 0 0 2px var(--vgK),0 4px 0 2px var(--vgK),0 9px 14px rgba(43,52,70,.25)!important;border-radius:14px!important;padding:16px 12px 8px 8px!important}
.nxq::before{content:'';position:absolute;left:50%;top:-8px;width:14px;height:14px;margin-left:-7px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#FF8A7A,var(--pin) 55%,#8E2418);box-shadow:0 2px 0 rgba(0,0,0,.25)}
.nxq>small{background:linear-gradient(var(--rom),#E3A92E)!important;color:var(--vgK)!important;border:2px solid var(--vgK);box-shadow:0 2px 0 var(--vgK)}
.nxq .nqb i{position:relative;height:16px!important;border-radius:9px!important;background:var(--vgD)!important;box-shadow:inset 0 2px 0 rgba(0,0,0,.25),0 0 0 2px var(--vgK);min-width:120px!important}
.nxq .nqb i u{background:linear-gradient(#FFE27A,var(--rom))!important;box-shadow:inset 0 -3px 0 rgba(184,134,46,.6)}
.nxq .nqb i em{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:400 12px/1 var(--f-game);font-style:normal;color:#fff;text-shadow:1px 1px 0 var(--vgK),-1px 1px 0 var(--vgK),1px -1px 0 var(--vgK),-1px -1px 0 var(--vgK),0 1.5px 0 var(--vgK)}
/* bảng: khung ván dày, giấy dó bên trong, ghim đỏ, tiêu đề trên thanh gỗ, nút đóng tròn đỏ */
.sheet{background:var(--dz)!important;border:7px solid var(--vg);box-shadow:0 0 0 3px var(--vgK),0 7px 0 3px var(--vgK),0 16px 30px rgba(43,52,70,.35)!important;border-radius:24px!important;padding-top:6px!important;overflow-x:hidden}
.sheet .shH{position:sticky;top:-6px;z-index:2;margin:-6px -16px 8px;padding:10px 12px 10px 16px;background:linear-gradient(#B07A46,var(--vg));border-bottom:3px solid var(--vgK)}
.sheet .shH h2{font-size:24px}
.x,#shX,.fui .x{width:36px!important;height:36px!important;border-radius:50%!important;background:radial-gradient(circle at 35% 30%,#FF8A7A,var(--pin) 60%)!important;color:#fff!important;font:700 22px/1 var(--f-body)!important;box-shadow:0 0 0 2.5px var(--vgK),0 3px 0 2.5px var(--vgK)!important;text-shadow:0 1px 0 rgba(0,0,0,.3)}
/* nút khối dày: phụ gỗ nâu, chính xanh lá chuối, nhận thưởng vàng rơm */
.btn{background:linear-gradient(#C08A55,#A0703E)!important;border:2.5px solid var(--vgK)!important;border-radius:14px!important;box-shadow:inset 0 2px 0 rgba(255,255,255,.35),0 4px 0 var(--vgK)!important}
.btn.g{background:linear-gradient(#9CD066,var(--la))!important;box-shadow:inset 0 2px 0 rgba(255,255,255,.45),0 4px 0 var(--vgK)!important}
.btn:active:not(:disabled){transform:translateY(3px);box-shadow:inset 0 2px 0 rgba(255,255,255,.35),0 1px 0 var(--vgK)!important}
.btn:disabled{filter:saturate(.35) brightness(1.05);opacity:.75}
/* thẻ thông tin trong bảng: giấy viền nâu mảnh */
.uxh{background:#FFFDF6!important;box-shadow:0 0 0 2px #E3C9A6!important}
/* câu Ngoại nói: giấy dó viền nâu mảnh, gọn */
.ngoai p{background:var(--dz)!important;box-shadow:0 0 0 2px var(--vg),0 3px 0 2px var(--vgK)!important;border-radius:14px!important}
"""
i = s.rindex("</style>"); s = s[:i] + CSS + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s)
print('ok')
