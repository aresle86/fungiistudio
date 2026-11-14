/* ===== v149f — ông Bảy Kiếng: hình (đã duyệt), ghe, sổ tìm mua ===== */
function bayArt(){ if (bayArt.c) return bayArt.c; return bayArt.c = ((M0) => {
const MC_ = {}, own = (c, ds) => MC_[c + (ds ? 'd' : '')] || (MC_[c + (ds ? 'd' : '')] = new T.MeshStandardMaterial({ color: c, flatShading: true, roughness: .9, side: ds ? T.DoubleSide : T.FrontSide }));
const M = (g, c, x, y, z, o = {}) => M0(g, typeof c === 'string' ? own(c, o.ds) : c, x, y, z, o);
const OUT = {}, V = (a, b, c) => new T.Vector3(a, b, c), ball = (r, d = 1) => new T.IcosahedronGeometry(r, d);
const shot = (name, W, H, build, o = {}) => { const ri = ICR(); ri.setClearColor(0, 0); ri.toneMapping = T.ACESFilmicToneMapping; ri.toneMappingExposure = 1.02; ri.shadowMap.enabled = true; ri.setSize(W, H); const sc = new T.Scene(), root = new T.Group(); sc.add(root); const pr = ROOT; ROOT = root; try { build(root); } finally { ROOT = pr; TINT = null; }
  sc.add(new T.HemisphereLight('#fff4e2', '#94a474', 1.6)); sc.add(new T.AmbientLight('#ffffff', .25)); const l = new T.DirectionalLight('#fff0d8', 1.6); l.position.set(-2, 5, 4); l.castShadow = true; l.shadow.mapSize.set(1024, 1024); Object.assign(l.shadow.camera, { left: -2.5, right: 2.5, top: 2.5, bottom: -2.5 }); l.shadow.bias = -.0005; l.shadow.normalBias = .02; sc.add(l);
  root.traverse(q => { if (q.isMesh) q.castShadow = true; }); root.updateMatrixWorld(true);
  const bb = new T.Box3().setFromObject(root), c = bb.getCenter(V()), dir = (o.dir || V(.3, .18, 1)).clone().normalize();
  if (o.gd){ const gd = new T.Mesh(new T.CircleGeometry(o.gd, 24), new T.ShadowMaterial({ opacity: .18 })); gd.rotation.x = -Math.PI / 2; gd.position.y = bb.min.y + .001; gd.receiveShadow = true; sc.add(gd); }
  const cm = new T.OrthographicCamera(-1, 1, 1, -1, .01, 100); cm.position.copy(c).add(dir.multiplyScalar(20)); cm.lookAt(c); cm.updateMatrixWorld(true); const inv = cm.matrixWorldInverse; let x0 = 1e9, x1 = -1e9, y0 = 1e9, y1 = -1e9;
  for (const x of [bb.min.x, bb.max.x]) for (const y of [bb.min.y, bb.max.y]) for (const z of [bb.min.z, bb.max.z]){ const p = V(x, y, z).applyMatrix4(inv); x0 = Math.min(x0, p.x); x1 = Math.max(x1, p.x); y0 = Math.min(y0, p.y); y1 = Math.max(y1, p.y); }
  const pad = o.pad ?? 1.06, cx = (x0 + x1) / 2, cy = (y0 + y1) / 2; let hw = (x1 - x0) / 2 * pad, hh = (y1 - y0) / 2 * pad; if (hw / hh > W / H) hh = hw * H / W; else hw = hh * W / H;
  cm.left = cx - hw; cm.right = cx + hw; cm.top = cy + hh; cm.bottom = cy - hh; cm.updateProjectionMatrix();
  toonRender(ri, sc, cm); const u = toonURL(); sc.traverse(q => q.geometry && q.geometry.dispose()); ICR(); return u; };
const seg = (p, a, b, r0, r1, c, n = 7) => { const d = V().subVectors(b, a), m = M(cyl(r1, r0, d.length(), n), c, (a.x + b.x) / 2, (a.y + b.y) / 2, (a.z + b.z) / 2, { p }); m.quaternion.setFromUnitVectors(V(0, 1, 0), d.normalize()); return m; };

/* ---------- ÔNG BẢY KIẾNG ---------- */
const P = { SK: '#D9A77C', SKD: '#C4915F', WH: '#F4F0E4', AO: '#F1E8D2', QUAN: '#4A3B30', HAT: '#7A5A3E', HATD: '#4A3626', KA: '#9E3B24', KB: '#FBF7EE', RIM: '#6B3A1C', BR: '#C9952A' };
const kieng = (p, x, y, z, r) => { const q = G(x, y, z, 0, p); if (r) q.rotation.set(...r); for (const sx of [-1, 1]) M(new T.TorusGeometry(.058, .011, 5, 14), P.RIM, sx * .1, 0, 0, { p: q }); M(box(.09, .012, .012), P.RIM, 0, .012, 0, { p: q }); return q; };
const lup = (p, hand, lens) => { seg(p, hand, lens.clone().add(hand.clone().sub(lens).setLength(.08)), .015, .013, '#6B4529', 6); const q = G(lens.x, lens.y, lens.z, 0, p); M(new T.TorusGeometry(.078, .014, 5, 16), P.BR, 0, 0, 0, { p: q }); M(new T.CircleGeometry(.072, 16), '#DCEFF2', 0, 0, -.004, { p: q, ds: true, cast: false }); return q; };
const so = (p, x, y, z, r, s = 1) => { const q = G(x, y, z, 0, p); q.rotation.set(...r); q.scale.setScalar(s); M(box(.17, .22, .04), '#7A4A2A', 0, 0, 0, { p: q }); M(box(.155, .205, .03), '#F4EAD0', .012, 0, 0, { p: q }); M(box(.03, .224, .044), '#4A3626', .045, 0, 0, { p: q }); M(box(.075, .05, .006), '#E8D9A8', -.02, .04, .021, { p: q, cast: false }); return q; };
const ong = (g, pose = 'xem') => { const sit = pose === 'ngoi', j = G(0, 0, 0, 0, g);
  for (const sx of [-1, 1]){ const lg = G(sx * .09, .28, 0, 0, j); if (sit){ lg.rotation.x = -1.4; lg.position.set(sx * .09, .31, .08); } M(cyl(.075, .09, .24, 8), P.QUAN, 0, -.12, 0, { p: lg }); M(ball(.065), P.SK, 0, -.24, .02, { p: lg, s: [1, .6, 1.3] }); M(box(.11, .02, .19), '#B48560', 0, -.272, .03, { p: lg }); }
  const t = G(0, .3, 0, 0, j); t.rotation.x = pose === 'kha' ? .02 : .1;
  M(ball(.23), P.AO, 0, .15, 0, { p: t, s: [.92, 1, .82] }); M(cyl(.185, .215, .08, 9), P.AO, 0, .01, 0, { p: t });
  for (const y of [.06, .15, .24]) M(ball(.016), '#B48560', 0, y, .192, { p: t });
  for (let k = 0; k < 8; k++) M(ball(.045), k % 2 ? P.KA : P.KB, Math.cos(k / 7 * Math.PI) * .185, .315 + Math.sin(k / 7 * Math.PI) * .02, .03 + Math.sin(k / 7 * Math.PI) * .09, { p: t, s: [1, .6, 1] });
  for (let k = 0; k < 4; k++) M(box(.065, .05, .04), k % 2 ? P.KA : P.KB, -.16, .25 - k * .05, .14, { p: t });
  M(ball(.055), P.SK, 0, .37, 0, { p: t });
  const arm = (sx, T2, bend) => { const S0 = V(sx * .175, .27, .02), E = S0.clone().lerp(T2, .5).add(V(...bend)); M(ball(.065), P.AO, S0.x, S0.y, S0.z, { p: t }); seg(t, S0, E, .06, .055, P.AO); M(ball(.056), P.AO, E.x, E.y, E.z, { p: t }); seg(t, E, T2, .054, .05, P.AO); M(ball(.06), P.SK, T2.x, T2.y, T2.z, { p: t }); };
  // đầu
  const h = G(0, .6, .04, 0, t); h.rotation.set(pose === 'kha' ? -.16 : pose === 'lau' ? .1 : 0, 0, pose === 'kha' ? .08 : pose === 'xem' ? -.05 : 0);
  M(ball(.29, 2), P.SK, 0, 0, 0, { p: h, s: [1, .98, .93] });
  for (const sx of [-1, 1]){ M(ball(.06), P.SKD, sx * .295, -.02, 0, { p: h, s: [.6, 1.1, .8] }); M(ball(.11), P.WH, sx * .235, .02, -.07, { p: h, s: [.7, 1.15, 1.1] }); }
  M(ball(.2), P.WH, 0, -.03, -.16, { p: h, s: [1.2, .9, .8] });
  M(ball(.045), P.SKD, 0, -.05, .272, { p: h, s: [1, 1.1, 1] });
  const n = G(0, .13, -.01, 0, h); n.rotation.x = -.1;
  M(cyl(.37, .43, .03, 14), P.HAT, 0, .02, 0, { p: n }); M(cyl(.215, .25, .19, 12), P.HAT, 0, .125, 0, { p: n }); M(cyl(.254, .258, .05, 12), P.HATD, 0, .06, 0, { p: n }); M(ball(.2), P.HAT, 0, .21, 0, { p: n, s: [1.07, .35, 1.07] });
  const z = .262, f = G(0, 0, 0, 0, h), brow = (sx, rot, y = .09) => M(ball(.035), P.WH, sx * .105, y, z - .002, { p: f, s: [1.5, .5, .5], r: [0, 0, sx * rot] }),
    eye = sx => { M(ball(.028), '#4A2F1E', sx * .1, .012, z - .004, { p: f, s: [1, 1.15, .45] }); M(ball(.01, 0), '#FBF7EE', sx * .1 - .01, .026, z + .008, { p: f }); },
    arc = sx => M(new T.TorusGeometry(.032, .009, 3, 8, Math.PI), '#6B4529', sx * .1, .0, z + .005, { p: f });
  for (const sx of [-1, 1]){ M(ball(.045), '#E89A7A', sx * .17, -.075, z - .035, { p: f, s: [1, .6, .3] }); M(ball(.05), P.WH, sx * .052, -.108, z + .002, { p: f, s: [1.3, .45, .5], r: [0, 0, -sx * .38] }); }
  M(ball(.06), P.WH, 0, -.22, z - .055, { p: f, s: [1, .8, .7] }); M(new T.ConeGeometry(.05, .13, 6), P.WH, 0, -.285, z - .065, { p: f, r: [Math.PI + .25, 0, 0] });
  if (pose === 'xem' || sit){ brow(-1, -.1); brow(1, -.3, .1); eye(-1); if (sit) eye(1); kieng(f, 0, -.062, z + .035);
    if (sit){ arm(1, V(.27, .22, .2), [.06, -.07, 0]); lup(t, V(.27, .22, .2), V(.3, .43, .22)); arm(-1, V(-.13, .07, .25), [-.06, .02, 0]); }
    else { const hand = V(.25, .4, .3), lens = V(.11, .6, .43); arm(1, hand, [.07, -.07, .02]); const q = lup(t, hand, lens); M(ball(.04), '#4A2F1E', 0, 0, .004, { p: q, s: [1, 1.15, .3] }); M(ball(.014, 0), '#FBF7EE', -.014, .02, .018, { p: q }); arm(-1, V(-.14, .1, .2), [-.07, 0, 0]); so(t, -.05, .1, .235, [-.15, .1, .12]); } }
  if (pose === 'lau'){ brow(-1, .12); brow(1, .12); arc(-1); arc(1); arm(1, V(.1, .2, .25), [.1, -.05, 0]); arm(-1, V(-.1, .2, .25), [-.1, -.05, 0]); kieng(t, 0, .23, .31, [-.5, 0, .08]);
    for (let a = 0; a < 3; a++) for (let b = 0; b < 3; b++) M(box(.04, .04, .012), (a + b) % 2 ? P.KA : P.KB, .1 + a * .04, .16 - b * .04, .305, { p: t, r: [0, 0, .1] }); }
  if (pose === 'kha'){ brow(-1, -.25, .1); brow(1, -.25, .1); arc(-1); arc(1); kieng(f, 0, -.062, z + .035); M(new T.CircleGeometry(.055, 12, Math.PI, Math.PI), '#9E3B24', 0, -.13, z - .012, { p: f, r: [-.3, 0, 0] });
    arm(1, V(.045, .33, .3), [.13, -.1, .03]); arm(-1, V(-.26, .1, .07), [-.1, .03, -.03]); so(t, -.3, .0, .1, [0, 1.3, .1], .9); }
  return j; };

/* ---------- MÓN TREO NHỎ ---------- */
const mFish = (p, x, y, z, s = 1, col = '#6E7F5A', bel = '#E8DFCC') => { const q = G(x, y, z, 0, p); q.scale.setScalar(s); q.rotation.z = -Math.PI / 2 + .12; M(ball(.06), col, 0, 0, 0, { p: q, s: [1.9, .85, .55] }); M(ball(.05), bel, .005, -.018, 0, { p: q, s: [1.7, .6, .5] }); M(cone(.05, .08, 4), col, -.14, 0, 0, { p: q, r: [0, 0, -Math.PI / 2], s: [1, 1, .3] }); M(cone(.03, .05, 4), col, 0, .055, 0, { p: q, s: [1.6, 1, .3] }); for (const sz of [-1, 1]) M(ball(.01, 0), '#2B1E16', .075, .012, sz * .028, { p: q }); return q; };
const mKhom = (p, x, y, z, s = 1, col = '#F2A81E') => { const q = G(x, y, z, 0, p); q.scale.setScalar(s); M(ball(.055), col, 0, 0, 0, { p: q, s: [1, 1.3, 1] }); for (let k = 0; k < 6; k++){ const a = k * 1.05; M(cone(.014, .08, 4), k % 2 ? '#5E8A5A' : '#A8623A', Math.cos(a) * .02, .095, Math.sin(a) * .02, { p: q, r: [Math.sin(a) * .5, 0, -Math.cos(a) * .5] }); } return q; };
const mOt = (p, x, y, z, s = 1, col = '#FFC928') => { const q = G(x, y, z, 0, p); q.scale.setScalar(s); for (let k = 0; k < 5; k++){ const a = k * 1.26, d = .028; M(cone(.016, .11, 5), k % 2 ? col : '#F2B01E', Math.cos(a) * d, -.05, Math.sin(a) * d, { p: q, r: [Math.PI + Math.sin(a) * .3, 0, -Math.cos(a) * .3] }); M(ball(.014, 0), '#4F9E3A', Math.cos(a) * d * .6, .01, Math.sin(a) * d * .6, { p: q }); } return q; };
const mBap = (p, x, y, z, s = 1) => { const q = G(x, y, z, 0, p); q.scale.setScalar(s); for (const sx of [-1, 1]){ M(ball(.035), sx > 0 ? '#6A3A86' : '#8A58A6', sx * .035, -.06, 0, { p: q, s: [.75, 1.9, .75], r: [0, 0, sx * .2] }); M(cone(.02, .08, 4), '#E3D3A0', sx * .02, .03, 0, { p: q, r: [0, 0, sx * .3] }); } return q; };
const mCa = (p, x, y, z, s = 1) => { const q = G(x, y, z, 0, p); q.scale.setScalar(s); M(cyl(.004, .004, .1, 4), '#5aa83e', 0, -.03, 0, { p: q }); for (let k = 0; k < 6; k++){ const sx = k % 2 ? 1 : -1, yy = -.005 - (k >> 1) * .035; M(ball(.022), k % 3 ? '#FFC928' : '#FFD95A', sx * .024, yy, (k % 3 - 1) * .012, { p: q }); } return q; };
const mKq = (p, x, y, z, s = 1) => { const q = G(x, y, z, 0, p); q.scale.setScalar(s); M(ball(.04), '#4E8A2E', 0, -.05, 0, { p: q, s: [.62, 1.7, .62] }); for (let k = 0; k < 10; k++){ const a = k * 2.4, yy = -.1 + k * .011; M(ball(.012, 0), '#6AA53A', Math.cos(a) * .024, yy, Math.sin(a) * .024, { p: q }); } M(cone(.012, .03, 4), '#4E8A2E', 0, -.125, 0, { p: q, r: [Math.PI, 0, 0] }); return q; };
const mMong = (p, x, y, z, s = 1) => { const q = G(x, y, z, 0, p); q.scale.setScalar(s); for (let k = 0; k < 3; k++) M(ball(.05), k % 2 ? '#6E4A86' : '#5A3A72', (k - 1) * .045, -.05 - (k % 2) * .03, 0, { p: q, s: [.95, 1.05, .25], r: [0, 0, (k - 1) * -.4] }); for (let k = 0; k < 5; k++) M(ball(.012, 0), '#3A2450', (k - 2) * .014, -.005 - (k % 2) * .014, .012, { p: q }); return q; };
const day = (p, a, b) => seg(p, a, b, .003, .003, '#8A6A3A', 4);

/* ---------- GHE ÔNG BẢY ---------- */
const ghe = g => { const pr = ROOT, ps = sd, nL = LIGHTS.length, b = gheTB(false); sd = ps; LIGHTS.length = nL; ROOT = pr; g.add(b); ROOT = b;
  const L = 1, W = .27, wU = u => W * Math.pow(Math.max(0, 1 - Math.pow(Math.abs(u), 2.4)), .55), ybU = u => -.08 + .3 * Math.pow(Math.abs(u), 4), ytU = u => .16 + (u > 0 ? .26 : .18) * Math.pow(Math.abs(u), 3);
  // mui lá dài phía lái
  const mx0 = -.62, mx1 = .08, mr = .215, my = .15; M(new T.CylinderGeometry(mr, mr, (mx1 - mx0) * L, 14, 1, true, 0, Math.PI), '#A88A4E', (mx0 + mx1) / 2 * L, my, 0, { r: [0, 0, Math.PI / 2], ds: true });
  for (let k = 0; k < 3; k++) M(new T.CylinderGeometry(mr + .012, mr + .012, .13, 14, 1, true, 0, Math.PI), k % 2 ? '#B89A58' : '#8E733E', mx0 * L + .1 + k * .25, my, 0, { r: [0, 0, Math.PI / 2], ds: true });
  for (let k = 0; k <= 4; k++) M(new T.TorusGeometry(mr + .016, .008, 3, 14, Math.PI), '#6B4529', (mx0 + (mx1 - mx0) * k / 4) * L, my, 0, { r: [0, Math.PI / 2, 0], cast: false });
  for (const z of [-1, 1]) M(box((mx1 - mx0) * L, .018, .018), '#6B4529', (mx0 + mx1) / 2 * L, my, z * (mr + .004));
  M(box(.004, .2, .34), '#E8DFCC', mx0 * L - .004, my + .08, 0);   // tấm màn sau lái
  // đèn bão treo đầu mui
  { const x = mx1 * L + .03, y = my + mr - .09; day(b, V(x, my + mr, 0), V(x, y + .05, 0)); M(cyl(.012, .02, .02, 6), '#3A2A1C', x, y + .04, 0); M(cyl(.022, .022, .05, 7), '#FFD23F', x, y, 0); M(cyl(.026, .026, .012, 7), '#3A2A1C', x, y - .03, 0); }
  // hòm gỗ + cân đĩa
  { const hx = .24, hy = ytU(.24) - .03; const q = G(hx, hy, -.03, .1, b); M(box(.2, .12, .17), '#8A5A2B', 0, .06, 0, { p: q }); M(box(.21, .025, .18), '#6B4529', 0, .125, 0, { p: q }); M(box(.03, .04, .01), P.BR, 0, .1, .09, { p: q }); for (const sx of [-1, 1]) M(box(.012, .12, .175), '#6B4529', sx * .08, .06, 0, { p: q });
    M(cyl(.006, .008, .13, 5), P.BR, 0, .2, 0, { p: q }); M(box(.17, .008, .008), P.BR, 0, .26, 0, { p: q }); for (const sx of [-1, 1]){ day(q, V(sx * .08, .26, 0), V(sx * .08, .19, 0)); M(cyl(.032, .022, .012, 9), P.BR, sx * .08, .185, 0, { p: q }); } M(ball(.018), '#FFC928', -.08, .2, 0, { p: q }); }
  // thúng hàng phía mũi
  { const q = G(.6, ytU(.6) - .04, .03, 0, b); M(new T.CylinderGeometry(.075, .055, .07, 12, 1, true), '#B89A58', 0, .035, 0, { p: q, ds: true }); M(cyl(.055, .055, .006, 12), '#8A6A3A', 0, .003, 0, { p: q }); for (const [x, z, c] of [[-.03, .01, '#6A3A86'], [.025, -.015, '#FFC928'], [0, .03, '#4E8A2E'], [.02, .03, '#F2A81E']]) M(ball(.028), c, x, .06, z, { p: q }); }
  // cây bẹo ở mũi: treo món ông đang tìm mua
  { const base = V(.86, ytU(.86) - .05, 0), top = V(1.02, 1.42, 0); seg(b, base, top, .017, .011, C.bamboo, 6); for (let k = 1; k < 6; k++){ const q = base.clone().lerp(top, k / 6); M(cyl(.019, .019, .01, 6), '#A8914E', q.x, q.y, q.z, { r: [0, 0, -.13] }); }
    const hang = (f, dx, len, mk) => { const a = base.clone().lerp(top, f), e = a.clone().add(V(dx, .04, 0)); seg(b, a, e, .006, .005, C.bamboo, 4); const d = e.clone().add(V(0, -len, 0)); day(b, e, d); mk(d); };
    hang(.97, -.13, .1, d => { b.userData.slot = G(d.x, d.y, d.z, 0, b); }); hang(.72, .11, .07, d => mKhom(b, d.x, d.y - .09, d.z, 1.1)); hang(.5, -.1, .05, d => mOt(b, d.x, d.y - .01, d.z, 1.1));
    M(box(.09, .05, .004), '#B8402E', top.x + .045, top.y - .03, 0, { ds: true }); }
  // mái chèo gác lái
  { const a = V(-.95, ytU(-.95) + .02, .1), e = V(-.3, .47, .3); seg(b, a, e, .011, .011, '#8A5A2B', 5); M(box(.2, .012, .05), '#8A5A2B', a.x - .08, a.y - .04, a.z - .025, { r: [0, .3, .62] }); }
  // ông Bảy ngồi trước mui
  { const q = G(.45, ytU(.45) - .08, 0, 0, b); q.scale.setScalar(.56); ong(q, 'ngoi'); }
  ROOT = pr; return b; };

/* ---------- 2 MÓN THƯỞNG ---------- */
const tre = (p, a, b, r = .028) => { seg(p, a, b, r, r * .9, C.bamboo, 7); const n = Math.max(2, Math.round(a.distanceTo(b) / .22)); for (let k = 1; k < n; k++){ const q = a.clone().lerp(b, k / n), m = M(cyl(r * 1.12, r * 1.12, .012, 7), '#A8914E', q.x, q.y, q.z, { p }); m.quaternion.setFromUnitVectors(V(0, 1, 0), V().subVectors(b, a).normalize()); } };
const bang = g => { for (const sx of [-1, 1]) tre(g, V(sx * .46, 0, 0), V(sx * .46, 1.0, 0), .032); tre(g, V(-.56, .93, 0), V(.56, .93, 0), .026);
  for (const sx of [-1, 1]){ day(g, V(sx * .3, .93, 0), V(sx * .3, .8, 0)); }
  M(box(.78, .36, .045), '#8A5A2B', 0, .62, 0, { p: g }); M(box(.72, .3, .05), '#B07A40', 0, .62, .004, { p: g }); for (const sx of [-1, 1]) for (const sy of [-1, 1]) M(ball(.014, 0), P.BR, sx * .35, .62 + sy * .14, .03, { p: g });
  const f = mFish(g, -.02, .62, .05, 2.5, '#E8A81E', '#FFD95A'); f.rotation.z = .08; f.scale.set(2.5, 2.5, 1.6);
  M(box(.1, .13, .006), '#B8402E', .47, .86, .035, { p: g, r: [0, 0, -.1] }); M(box(.05, .1, .006), '#B8402E', .5, .76, .035, { p: g, r: [0, 0, .15] });
  const cols = [['#5F7A66', '#E8DFCC'], ['#C77B3A', '#F4D9A8'], ['#6A6F8A', '#E8DFCC'], ['#8A4A3A', '#F0C8B0'], ['#3F6A5A', '#D9E8C8']];
  for (let k = 0; k < 5; k++){ const x = -.3 + k * .15, y = .44; day(g, V(x, y, 0), V(x, y - .07 - (k % 2) * .04, 0)); mFish(g, x, y - .2 - (k % 2) * .04, 0, .95, cols[k][0], cols[k][1]); } };
const gian = g => { for (const sx of [-1, 1]){ tre(g, V(sx * .5, 0, 0), V(sx * .5, 1.05, 0), .032); seg(g, V(sx * .5, .0, .0), V(sx * .5, .3, .0), .034, .034, C.bamboo, 7); }
  tre(g, V(-.62, 1.0, 0), V(.62, 1.0, 0), .026); tre(g, V(-.56, .62, 0), V(.56, .62, 0), .022);
  // mái lá nhỏ che mưa
  for (const sz of [-1, 1]) M(box(1.3, .02, .2), sz > 0 ? '#B89A58' : '#A88A4E', 0, 1.1, sz * .085, { p: g, r: [sz * .5, 0, 0] }); M(box(1.32, .025, .03), '#6B4529', 0, 1.15, 0, { p: g });
  const hang = (x, y0, len, mk) => { day(g, V(x, y0, 0), V(x, y0 - len, 0)); mk(x, y0 - len); };
  hang(-.32, 1.0, .1, (x, y) => mBap(g, x, y, 0, 1.9)); hang(0, 1.0, .1, (x, y) => mKhom(g, x, y - .12, 0, 1.7, '#F7B928')); hang(.32, 1.0, .08, (x, y) => mOt(g, x, y - .0, 0, 1.9));
  hang(-.32, .62, .07, (x, y) => mKq(g, x, y, 0, 1.9)); hang(0, .62, .07, (x, y) => mCa(g, x, y - .03, 0, 2)); hang(.32, .62, .07, (x, y) => mMong(g, x, y, 0, 1.35)); };


const FC = { cadua: ['#C77B3A', '#F4D9A8'], hu: ['#6A6F8A', '#E8DFCC'], rodauvang: ['#E8A81E', '#FFD95A'], locbong: ['#5F7A66', '#E8DFCC'] };
const mini = (k, p, s = 1) => { const q = G(0, 0, 0, 0, p); q.scale.setScalar(s); k === 'khommat' ? mKhom(q, 0, -.09, 0, 1.1, '#F7B928') : k === 'otvang' ? mOt(q, 0, -.01, 0, 1.1) : k === 'baptim' ? mBap(q, 0, 0, 0, 1.2) : k === 'cachuavang' ? mCa(q, 0, -.03, 0, 1.3) : k === 'khoquarung' ? mKq(q, 0, 0, 0, 1.2) : k === 'mongtoitia' ? mMong(q, 0, 0, 0, .9) : mFish(q, 0, -.13, 0, 1.25, ...(FC[k] || FC.locbong)); return q; };
const PIC = {}; return { ong, ghe, bang, gian, mini, pic: pose => PIC[pose] || (PIC[pose] = shot('p', 320, 374, g => ong(g, pose), { gd: .5, pad: 1.1 })) };
})(M); }
/* gộp lưới theo vật liệu: một món chỉ còn vài lần vẽ */
function bayFuse(root){ root.updateMatrixWorld(true); const inv = new T.Matrix4().copy(root.matrixWorld).invert(), bk = new Map(), drop = [];
  root.traverse(o => { if (!o.isMesh) return; let g = o.geometry.index ? o.geometry.toNonIndexed() : o.geometry.clone(); for (const n of Object.keys(g.attributes)) if (n !== 'position' && n !== 'normal') g.deleteAttribute(n); if (!g.attributes.normal) g.computeVertexNormals(); g.clearGroups(); g.applyMatrix4(new T.Matrix4().multiplyMatrices(inv, o.matrixWorld));
    const key = o.material.uuid + (o.castShadow ? 'c' : ''); if (!bk.has(key)) bk.set(key, { mat: o.material, cast: o.castShadow, list: [] }); bk.get(key).list.push(g); drop.push(o); });
  for (const o of drop) o.parent.remove(o); for (const b of bk.values()){ const m = new T.Mesh(mergeGeometries(b.list, false), b.mat); m.castShadow = b.cast; m.receiveShadow = true; root.add(m); b.list.forEach(x => x.dispose()); } return root; }
const BAYK = ['mongtoitia', 'otvang', 'cachuavang', 'khoquarung', 'baptim', 'khommat', 'cadua', 'hu', 'rodauvang', 'locbong'];
const bayName = k => nm135((CROPS[k] || FISHK[k]).name), bayN = k => ST.inv[k] || 0;
function bayWant(){ if (ST.bayW) return ST.bayW; let pool = BAYK.filter(k => QUY[k] ? unlocked(QUY[k].base) : (() => { try { return cauOn(); } catch (e) { return false; } })()); if (!pool.length) pool = ['mongtoitia']; let hsh = 0; for (const c of dayKey()) hsh = (hsh * 31 + c.charCodeAt(0)) % 9973; return pool[hsh % pool.length]; }
const bayU = k => (GD(k) || {}).unit || 'con'; const bayBase = k => CROPS[k] ? CROPS[k].sell : FPRICE[k];
const bayPrice = (k, first) => k === 'caho' ? 900 : Math.round(bayBase(k) * (first ? 3 : 1.5) * (bayWant() === k ? 1.5 : 1) * (!first && (bayS().th[k] || 1) > 1 ? 1.2 : 1));
const bayOn = () => quyOn() && !VISIT && (!(ST.bay || {}).met || [0, 3].includes(new Date().getDay()) || !!ST.bayF);
let BAYV = null, BAYD = null;
try { const A = bayArt(), pr = ROOT, root = DYN(G(bx + 6.5, WLR + .1, R0 + 1.25, -.08)), gg = new T.Group(); root.add(gg); gg.scale.setScalar(1.12); const b = A.ghe(gg); ROOT = pr; const slot = b.userData.slot; bayFuse(gg);
  const hit = new T.Mesh(new T.BoxGeometry(2.5, 1.9, .8), new T.MeshBasicMaterial({ visible: false })); root.add(hit); hit.position.set(0, .7, 0); root.visible = false; BAYV = { root, hit, slot, w: '', ...mkBub() }; BAYV.b.visible = false;
  const gian = DYN(G(1.0, 0, 2.3, 0)); gian.scale.setScalar(.8); A.gian(gian); bayFuse(gian); gian.visible = false; const bang = DYN(G(bx + .25, 0, R0 - .75, 0)); bang.scale.setScalar(.8); A.bang(bang); bayFuse(bang); bang.visible = false; BAYD = { gian, bang }; ROOT = pr; } catch (e) { console.warn('bay', e); }
function bayTick(t){ try { bayNote(t); } catch (e) {} if (!BAYV) return; const on = bayOn(), st = (ST.bay || {}).set || {}, R = BAYV.root; if (BAYD){ BAYD.gian.visible = !!st.giong; BAYD.bang.visible = !!st.ca; } if (on && !R.visible && !BAYV.au){ BAYV.au = 1; try { aud('ghe'); } catch (e) {} } R.visible = on; if (!on){ BAYV.b.visible = false; return; }
  const w = bayWant(); if (BAYV.w !== w){ BAYV.w = w; const s = BAYV.slot; while (s.children.length) s.remove(s.children[0]); try { bayArt().mini(w, s); } catch (e) {} }
  R.position.y = WLR + .1 + Math.sin(t * 1.3 + 1) * .012; R.rotation.z = Math.sin(t * 1.05 + 1) * .015; const b = BAYV.b, show = (ST.bay || {}).seen !== dayKey(); b.visible = show; if (show){ bubIcon(b, ICON[w]); b.quaternion.copy(cam.quaternion); b.position.set(R.position.x - .25, 1.15 + Math.sin(t * 2 + 1) * .035, R.position.z); b.scale.setScalar(.9 * BUBS * (1 + .07 * Math.abs(Math.sin(t * 3)))); } }
function bayHit(cx, cy){ if (!BAYV || !BAYV.root.visible) return false; ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); return ray.intersectObjects(BAYV.b.visible ? [BAYV.hb, BAYV.hit] : [BAYV.hit], false).length > 0; }
function bayStall(t){ const A = bayArt(), pr = ROOT; try { const o = G(0, 0, 0, 0, t); o.scale.setScalar(.52); A.ong(o, 'xem'); const s = G(.42, 0, .05, 0, t); M(box(.34, .26, .26), '#8A5A2B', 0, .13, 0, { p: s }); M(box(.36, .03, .28), '#6B4529', 0, .27, 0, { p: s }); const m = G(0, .4, 0, 0, s); A.mini('khommat', m, 1.3); const m2 = G(-.1, .34, .06, 0, s); A.mini('otvang', m2, 1.2); bayFuse(t); } finally { ROOT = pr; } }
function baySet(){ const B = bayS(); let got = 0; if (!B.set.giong && QGI.every(k => B.stamp[k])){ B.set.giong = 1; got = 1; } if (!B.set.ca && QCA.every(k => B.stamp[k])){ B.set.ca = 1; got = 2; } if (!got) return 0;
  try { sfx('lvl'); confettiAt(innerWidth / 2, innerHeight * .4, 44, 1.2); } catch (e) {} if (SHEET && SHEET.bay) SHEET.bay = { pose: 'kha', line: got === 1 ? 'Đủ sáu giống quý rồi! Qua tặng cháu cái giàn treo trái giống, dựng trước hiên cho bà con ghé coi.' : 'Đủ năm con cá quý! Qua tặng cháu tấm bảng Tay câu, treo ở bến cho cả xóm biết.' }; return got; }
function bayHTML(){ const B = bayS(), w = bayWant(), held = BAYK.filter(k => bayN(k) > 0), fresh = [...BAYK, 'caho'].find(k => !B.stamp[k] && (k === 'caho' ? quyGot(k) : bayN(k) > 0));
  if (!SHEET.bay){ SHEET.bay = { pose: fresh ? 'lau' : 'xem', line: !B.met ? 'Qua là Bảy Kiếng, đi ghe gom đồ quý miệt vườn. Cháu có trái lạ, cá lạ thì để dành cho qua nghe.' : fresh ? 'Ủa, cháu có món lạ đó hả? Đưa qua coi.' : L135(`Bữa nay qua tìm mua ${quyGot(w) ? bayName(w).toLowerCase() : 'một món cháu chưa gặp'}. Có thì qua trả thêm phân nửa.`, `Today I'm looking for ${quyGot(w) ? bayName(w).toLowerCase() : 'something you have not found yet'}. Bring it and I pay half again.`) }; if (!B.met || B.seen !== dayKey()){ B.met = 1; B.seen = dayKey(); save(); } }
  const S = SHEET.bay, nst = [...QGI, ...QCA].filter(k => B.stamp[k]).length; let pic = ''; try { pic = bayArt().pic(S.pose); } catch (e) {}
  let h = `<div class="bayh"><img src="${pic}" alt=""><div class="bayq">${S.line}</div></div>` + UX.title('Hôm nay qua tìm mua') + `<div class="qset ok${quyGot(w) ? '' : ' no'}"><img src="${ICON[w]}" alt=""><div><b>${quyGot(w) ? bayName(w) : '???'}</b><span>Trả thêm phân nửa giá</span></div></div>`;
  h += UX.title('Món quý cháu đang có');
  if (!held.length && fresh !== 'caho') h += '<div class="qset"><div><b>Chưa có món nào</b><span>Chăm liếp cho đúng, câu cho đúng lúc, có ngày gặp.</span></div></div>';
  if (fresh === 'caho') h += `<div class="qset"><img src="${ICON.caho}" alt=""><div><b>${FISHK.caho.name}</b><span>Cháu gặp rồi thả về sông. Kể qua nghe là đủ.</span></div></div>` + UX.cta([UX.btn('baygiao', 'Kể chuyện cá hô · +900 xu', { g: 1, k: 'caho' })]);
  for (const k of held){ const n = bayN(k), st = B.stamp[k]; h += `<div class="qset"><img src="${ICON[k]}" alt=""><div><b>${bayName(k)} · ${n}</b><span>${st ? L135('Qua mua ' + bayPrice(k, 0) + ' xu một ' + bayU(k) + (B.th[k] > 1 ? ' · đã trả thêm' : ''), 'I buy at ' + bayPrice(k, 0) + ' coins each' + (B.th[k] > 1 ? ' · raised' : '')) : L135('Món đầu qua ghi sổ, trả ' + bayPrice(k, 1) + ' xu', 'First one goes in my book, ' + bayPrice(k, 1) + ' coins')}</span></div></div>`
      + UX.cta(st ? [UX.btn('baythach', 'Nói thách', { k, dis: B.th[k] != null }), UX.btn('bayban', L135(`Bán ${n} · +${bayPrice(k, 0) * n} xu`, `Sell ${n} · +${bayPrice(k, 0) * n} coins`), { g: 1, k })] : [UX.btn('baygiao', L135(`Giao món đầu · +${bayPrice(k, 1)} xu`, `Hand over · +${bayPrice(k, 1)} coins`), { g: 1, k })]); }
  h += UX.title('Sổ tìm mua', nst + '/11') + '<div class="bayg">' + [...QGI, ...QCA].map(k => `<div class="${B.stamp[k] ? 'st' : quyGot(k) ? '' : 'no'}"><img src="${ICON[k]}" alt=""></div>`).join('') + '</div>'
    + UX.cta([UX.btn('bayhoi', 'Hỏi chuyện đồ quý', { dis: B.rd === dayKey() })]) + `<p class="bayn">${(ST.lv || 1) >= CHM.lv ? 'Ngày nào qua cũng ngồi ngoài chợ huyện. Thứ Tư với Chủ nhật qua ghé bến nhà cháu.' : 'Thứ Tư với Chủ nhật qua ghé bến nhà cháu.'}</p>`; return h; }
function bayAct(a, b){ const B = bayS(), k = b.dataset.k, S = SHEET.bay || (SHEET.bay = {});
  if (a === 'baygiao'){ if (B.stamp[k]) return; if (k === 'caho'){ if (!quyGot(k)) return; } else { if (!bayN(k)) return; ST.inv[k]--; } const v = bayPrice(k, 1); B.stamp[k] = dayKey(); ST.xu += v; try { sfx('coin'); coinFly(b, 6); coinPop(L135(`+${v} xu · ông Bảy ghi sổ`, `+${v} coins · in Uncle Bảy's book`), '#F5D27A'); } catch (e) {}
    S.pose = 'lau'; S.line = k === 'caho' ? 'Cá hô mà cháu cũng gặp rồi hả? Thả nó về là phải. Để qua ghi vô sổ.' : `Chèn ơi, ba chục năm qua mới thấy lại ${QUY[k] ? 'trái' : 'con'} này. Để qua ghi vô sổ.`; baySet(); }
  else if (a === 'baythach'){ if (B.th[k] != null) return; if (Math.random() < .6){ B.th[k] = 1.2; S.pose = 'xem'; S.line = 'Ừa, hàng đẹp vậy thì qua trả thêm cho cháu.'; try { sfx('up'); } catch (e) {} } else { B.th[k] = 1; S.pose = 'kha'; S.line = 'Khà khà, cháu nói thách còn non lắm.'; try { sfx('pick'); } catch (e) {} } }
  else if (a === 'bayban'){ const n = bayN(k); if (!n) return; const v = bayPrice(k, 0) * n; ST.inv[k] = 0; delete B.th[k]; ST.xu += v; ST.soldN = (ST.soldN || 0) + n; try { sfx('coin'); coinFly(b, Math.min(8, n + 2)); coinPop(L135(`+${v} xu · bán ${n} ${bayU(k)}`, `+${v} coins · sold ${n}`)); } catch (e) {} S.pose = 'xem'; S.line = 'Món này qua chở lên chợ huyện, người ta quý lắm.'; }
  else if (a === 'bayhoi'){ if (B.rd === dayKey()) return; const r = donAny(); B.rd = dayKey(); S.pose = 'xem'; S.line = r ? r.txt : 'Chuyện đồ quý qua kể cháu nghe hết rồi đó.'; try { sfx('pick'); } catch (e) {} }
  save(); hud(); renderSheet(); }
/* báo trước + đơn giống quý: mỗi thứ một lần, không hối */
let BAYNT = -9; function bayNote(t){ if (t - BAYNT < 6) return; BAYNT = t; if (VISIT || !quyOn() || !ST.player || !document.getElementById('intro').hidden) return; ST.seen = ST.seen || {}; const Q = quyQ(), ms = muaSong();
  if (!ST.seen.quy0){ ST.seen.quy0 = 1; Q.ss = ms; save(); say('Ngoại nghe nói liếp nào chăm đúng ý thì có khi ra trái lạ, kèm hạt giống quý. Con mở Sổ, trang Đồ quý coi thử nghe.', 'vui', { idle: true }); return; }
  let ca = false; try { ca = cauOn(); } catch (e) {} if (ca && !ST.seen.quyca){ ST.seen.quyca = 1; save(); say('Sông mình có mấy con cá quý, hiếm ai gặp lắm. Bóng tụi nó Ngoại vẽ sẵn trong Sổ, trang Đồ quý đó con.', 'vui', { idle: true }); return; }
  if (Q.ss !== ms){ Q.ss = ms; save(); if (QGI.some(k => QUY[k].mua === ms && unlocked(QUY[k].base) && !Q.got[k])) say(ms === 'kho' ? 'Vô mùa khô rồi con. Có mấy giống quý chỉ ra mùa này thôi đó.' : 'Vô mùa mưa rồi con. Có mấy giống quý chỉ ra mùa này thôi đó.', 'vui', { idle: true }); return; }
  if (ST.ord && ST.ord.list && (ST.lv || 1) >= ORD.lv && ST.ord.quy !== dayKey()){ const k = QGI.find(k => bayN(k) > 0); if (k){ const q = Math.min(3, bayN(k)); ST.ord.quy = dayKey(); ST.ord.list.unshift({ id: 'quy' + Date.now(), who: 'Bà con xóm trên', why: 'ăn thử giống quý vườn mình', items: [[k, q]], xu: Math.round(q * GD(k).sell * 1.4 / 5) * 5, xp: 4 + q * 2, quy: 1 }); save(); hud(); } } }
/*BAY_END*/
