p='live/vuon3d.html'; s=open(p).read()
code = r"""function gheTB(){ const g = new T.Group(), pr = ROOT; ROOT = g;   /* ghe tam bản cấp 19: vỏ ván đen dầu chai, mũi sơn đỏ viền xanh có mắt ghe, mui tre lợp lá cong, lờ tre chất phía lái, sào chống, mái chèo lái */
  const MS = c => new T.MeshStandardMaterial({ color: c, flatShading: true, roughness: .9 }), HULL = MS('#4A3626'), INN = MS('#9C7650'), PLK = MS('#C9A27E'), RED = MS('#B8402E'), GRN = MS('#3E7460'), WH = MS('#F4F0E4'), INK = MS('#1E1A16'), MUI = MS('#C9AE52'), MUI2 = MS('#B89A44'), BAM = MS('#B9A45A'), TRE = MS('#C7B070');
  const L = 1.0, W = .27, N = 28, wU = u => W * Math.pow(Math.max(0, 1 - Math.pow(Math.abs(u), 2.4)), .55), ybU = u => -.08 + .3 * Math.pow(Math.abs(u), 4), ytU = u => .07 + (u > 0 ? .3 : .2) * Math.pow(Math.abs(u), 3);
  const shell = (inset, lift, mat, u0 = -1, u1 = 1) => { const pos = [], sec = u => { const w = Math.max(0, wU(u) - inset), yb = ybU(u) + lift, yt = ytU(u); return [[-w, yt], [-w * .7, yb], [w * .7, yb], [w, yt]]; };
    for (let i = 0; i < N; i++){ const a = -1 + 2 * i / N, b = -1 + 2 * (i + 1) / N; if (b <= u0 || a >= u1) continue; const A = sec(a), B = sec(b);
      for (let j = 0; j < 3; j++){ const p = [a * L, A[j][1], A[j][0]], q = [a * L, A[j + 1][1], A[j + 1][0]], r = [b * L, B[j][1], B[j][0]], s2 = [b * L, B[j + 1][1], B[j + 1][0]]; pos.push(...p, ...r, ...q, ...q, ...r, ...s2); } }
    const ge = new T.BufferGeometry(); ge.setAttribute('position', new T.Float32BufferAttribute(pos, 3)); ge.computeVertexNormals(); return M(ge, mat, 0, 0, 0, { ds: true }); };
  shell(0, 0, HULL); shell(.02, .025, INN);
  // dải sơn đỏ mũi + viền xanh, mép be
  for (const sz of [-1, 1]){ const band = (u0, u1, dy, mat, th) => { const pts = []; for (let i = 0; i <= 12; i++){ const u = u0 + (u1 - u0) * i / 12; pts.push(new T.Vector3(u * L, ytU(u) - dy, sz * (wU(u) + .004))); } M(new T.TubeGeometry(new T.CatmullRomCurve3(pts), 24, th, 4, false), mat, 0, 0, 0); };
    band(.55, .985, .03, RED, .026); band(.55, .985, .065, GRN, .009); band(-.98, .98, -.006, MS('#2E2218'), .014); band(-.98, -.6, .03, RED, .02);
    // mắt ghe: tròng trắng, con ngươi đen, mí đỏ
    const u = .8, ex = u * L, ey = ytU(u) - .045, ez = sz * (wU(u) + .012), ry = sz * (Math.PI / 2 - .5); const e = G(ex, ey, ez, 0, g); e.rotation.y = ry;
    M(new T.CircleGeometry(.04, 14), WH, 0, 0, sz > 0 ? .001 : -.001, { p: e, s: [1.45, .8, 1], r: [0, sz > 0 ? 0 : Math.PI, 0], ds: true, cast: false }); M(new T.CircleGeometry(.022, 12), INK, 0, 0, sz > 0 ? .003 : -.003, { p: e, r: [0, sz > 0 ? 0 : Math.PI, 0], ds: true, cast: false }); M(box(.12, .008, .004), RED, 0, .034, 0, { p: e, cast: false }); }
  // ván sạp, ván ngang
  for (const u of [-.78, -.45, -.1, .3, .62]){ const w = wU(u) - .02; M(box(.05, .02, w * 2), PLK, u * L, ytU(u) - .04, 0); }
  for (const [u0, u1] of [[-.75, -.48], [.33, .6]]){ const um = (u0 + u1) / 2; M(box((u1 - u0) * L, .01, wU(um) * 1.25), MS('#B48C64'), um * L, ybU(um) + .035, 0, { cast: false }); }
  // mui: vòm tre lợp lá cong giữa ghe
  const mx0 = -.42, mx1 = .26, mr = .21; M(new T.CylinderGeometry(mr, mr, (mx1 - mx0) * L, 14, 1, true, -Math.PI / 2, Math.PI), MUI, (mx0 + mx1) / 2 * L, .1, 0, { r: [0, 0, Math.PI / 2], ds: true });
  M(new T.CylinderGeometry(mr + .012, mr + .012, (mx1 - mx0) * L * .4, 14, 1, true, -Math.PI / 2, Math.PI), MUI2, mx0 * L + (mx1 - mx0) * L * .2, .1, 0, { r: [0, 0, Math.PI / 2], ds: true });
  for (let k = 0; k <= 4; k++){ const x = (mx0 + (mx1 - mx0) * k / 4) * L; M(new T.TorusGeometry(mr + .014, .008, 3, 14, Math.PI), MS('#8A6A3A'), x, .1, 0, { r: [0, Math.PI / 2, 0], cast: false }); }
  for (const z of [-1, 1]) M(box((mx1 - mx0) * L, .016, .016), MS('#8A6A3A'), (mx0 + mx1) / 2 * L, .1, z * (mr + .004));
  M(new T.CircleGeometry(mr, 14, 0, Math.PI), MS('#3A2A1C'), mx1 * L - .01, .1, 0, { r: [0, Math.PI / 2, 0], ds: true, cast: false });   // lòng mui tối
  // lờ tre chất phía lái
  const lo = (x, y, z, ry, rz) => { const o = G(x, y, z, ry, g); o.rotation.z = rz; M(new T.CylinderGeometry(.03, .075, .26, 10, 1, true), TRE, 0, 0, 0, { p: o, ds: true }); for (let k = 0; k < 4; k++) M(new T.TorusGeometry(.04 + k * .011, .005, 3, 10), MS('#8A6A3A'), 0, .1 - k * .065, 0, { p: o, r: [Math.PI / 2, 0, 0], cast: false }); M(new T.ConeGeometry(.072, .08, 10, 1, true), MS('#B09A5C'), 0, -.15, 0, { p: o, r: [Math.PI, 0, 0], ds: true }); };
  lo(-.62 * L, .08, -.05, .2, Math.PI / 2); lo(-.66 * L, .08, .09, -.1, Math.PI / 2 + .1); lo(-.64 * L, .17, .02, .05, Math.PI / 2 - .05);
  // cái chài cuộn, thúng, lu nước nhỏ ở mũi
  { const c = G(.42 * L, ybU(.42) + .07, -.05, 0, g); M(sph(.07, 8, 6), MS('#8C8C78'), 0, 0, 0, { p: c, s: [1.3, .55, 1] }); for (let k = 0; k < 8; k++) M(sph(.008, 4, 3), MS('#6E6E62'), Math.cos(k * .8) * .08, -.01, Math.sin(k * .8) * .06, { p: c, cast: false }); }
  { const t2 = G(.48 * L, ybU(.48) + .05, .09, 0, g); M(new T.CylinderGeometry(.065, .045, .06, 12, 1, true), MS('#A88A52'), 0, .03, 0, { p: t2, ds: true }); M(cyl(.045, .045, .005, 12), MS('#8A6A3A'), 0, 0, 0, { p: t2 }); for (const [x, z, c] of [[-.02, .01, '#E8453A'], [.02, -.01, '#F2C230']]) M(sph(.022, 6, 4), MS(c), x, .05, z, { p: t2, cast: false }); }
  // mái chèo lái + cọc, sào chống dọc mạn
  { const o = G(-.9 * L, .2, 0, 0, g); o.rotation.z = .9; M(cyl(.01, .01, .6, 5), PLK, 0, 0, 0, { p: o }); M(box(.06, .2, .014), PLK, 0, -.36, 0, { p: o }); M(cyl(.014, .016, .16, 5), MS('#6B4529'), .02, -.02, 0, { p: g }); }
  M(cyl(.009, .009, 1.7, 5), BAM, 0, ytU(0) + .03, wU(0) + .01, { r: [0, 0, Math.PI / 2 - .04] });
  // đèn bão treo đầu mui, cờ nhỏ
  { const pl = G(mx1 * L + .06, 0, 0, 0, g); M(cyl(.008, .008, .32, 4), MS('#6B4529'), 0, .2, 0, { p: pl }); lamp(pl, .05, .3, 0, .55); }
  ROOT = pr; return g; }
"""
a="function scaffold(s = 1){"
assert s.count(a)==1
s=s.replace(a, code + a)
open(p,'w').write(s)
