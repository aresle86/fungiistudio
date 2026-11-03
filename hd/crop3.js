window.__crop3 = () => { const OUT = {}; const ri = new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true }); ri.setPixelRatio(1); ri.setSize(240, 240); ri.setClearColor(0, 0); ri.toneMapping = T.ACESFilmicToneMapping; ri.toneMappingExposure = 1.05;
  const V = (a, b, c) => new T.Vector3(a, b, c);
  const shot = (name, build, dir = V(.35, .35, 1)) => { const sc = new T.Scene(), root = new T.Group(); sc.add(root); const pr = ROOT; ROOT = root; sd = 31 + name.length * 5; build(root); ROOT = pr;
    sc.add(new T.HemisphereLight('#fff6e6', '#9aaa78', 1.9)); sc.add(new T.AmbientLight('#ffffff', .35)); const l = new T.DirectionalLight('#fff0d0', 1.9); l.position.set(-2, 6, 4); sc.add(l);
    const bb = new T.Box3().setFromObject(root), c = bb.getCenter(V()), s = bb.getSize(V()), sz = Math.max(s.x, s.y, s.z) * .62; const cm = new T.OrthographicCamera(-sz, sz, sz, -sz, .01, 100); cm.position.copy(c).add(dir.clone().normalize().multiplyScalar(20)); cm.lookAt(c); ri.render(sc, cm); OUT[name] = ri.domElement.toDataURL('image/png'); };
  // BẮP: trái bắp bóc vỏ, hạt vàng nổi hạt, vỏ xanh tách 3 lá, râu nâu
  shot('bap', () => { const g = G(0, 0, 0); g.rotation.z = -.5;
    for (let r = 0; r < 9; r++){ const y = -.32 + r * .08, rad = .13 * Math.sin(Math.PI * (.18 + .7 * (r + .5) / 9)) + .02; for (let k = 0; k < 10; k++){ const a = k / 10 * 6.28 + (r % 2) * .31; M(ico(.042, 0), r % 3 === 1 ? '#E9A51C' : '#F2B824', Math.cos(a) * rad, y, Math.sin(a) * rad, { p: g, s: [1, .85, 1] }); } }
    M(cyl(.11, .1, .66, 10), '#C98A1E', 0, -.0, 0, { p: g });
    for (let k = 0; k < 6; k++){ const t = M(cyl(.006, .004, .16, 3), '#A0612C', R(-.03, .03), .42, R(-.03, .03), { p: g }); t.rotation.set(R(-.5, .5), 0, R(-.6, .6)); }
    for (const [a, c, op] of [[0, '#8fc84a', .55], [2.1, '#6fbe4a', .7], [4.2, '#9fd36a', .45]]){ const lg = G(0, -.38, 0, a, g); const lf = M(leafGeo(.62, .16, .55, -.05, 6), c, 0, 0, 0, { p: lg, ds: true }); lf.rotation.z = Math.PI / 2 + op; lf.position.x = .05; }
    M(cyl(.04, .05, .16, 6), '#7aa83e', 0, -.46, 0, { p: g }); }, V(.2, .25, 1));
  // ỚT: ba trái ớt đỏ cong, cuống xanh
  shot('ot', () => { const pep = (x, y, rz, s, col) => { const g = G(x, y, 0); g.rotation.z = rz; const pts = []; for (let i = 0; i <= 8; i++){ const t = i / 8; pts.push(V(Math.sin(t * 1.7) * .2 * s, -t * .6 * s, 0)); } const cur = new T.CatmullRomCurve3(pts);
      const geo = new T.TubeGeometry(cur, 16, .07 * s, 7, false), pos = geo.attributes.position; // thon dần về mũi
      for (let i = 0; i < pos.count; i++){ const seg = Math.floor(i / 8) / 16, p0 = cur.getPoint(Math.min(1, seg)), v = V().fromBufferAttribute(pos, i); const k = 1 - seg * .85; v.sub(p0).multiplyScalar(k).add(p0); pos.setXYZ(i, v.x, v.y, v.z); } geo.computeVertexNormals();
      M(geo, col, 0, 0, 0, { p: g }); M(sph(.072 * s, 8, 6), col, 0, 0, 0, { p: g, s: [1, .6, 1] }); M(cone(.07 * s, .05, 7), '#4F7D44', 0, .02, 0, { p: g, r: [Math.PI, 0, 0] }); const st = M(cyl(.014 * s, .018 * s, .14 * s, 5), '#6E9F57', -.02, .1 * s, 0, { p: g }); st.rotation.z = .5; };
    pep(-.06, .05, -.55, 1, '#E8453A'); pep(0, .08, .05, 1.12, '#D6352C'); pep(.06, .05, .65, .95, '#F05A3A'); }, V(.05, .12, 1));
  // HÀNH LÁ: bó hành, thân trắng, lá xanh ống, rễ, buộc dây đỏ
  shot('hanh', () => { const g = G(0, 0, 0); g.rotation.z = -.35;
    for (let k = 0; k < 6; k++){ const x = (k - 2.5) * .06, z = (k % 2) * .04 - .02, tilt = -(k - 2.5) * .11; const b = G(x, 0, z, 0, g); b.rotation.z = tilt;
      M(cyl(.04, .046, .2, 7), '#FBF7EE', 0, -.2, 0, { p: b }); M(sph(.052, 7, 5), '#F2EEE4', 0, -.31, 0, { p: b, s: [1, .8, 1] }); M(cyl(.034, .04, .1, 7), '#cfe8a0', 0, -.05, 0, { p: b });
      const lc = k % 2 ? '#4F9E3A' : '#5aa83e'; M(cyl(.024, .034, .55, 7), lc, 0, .27, 0, { p: b }); M(cone(.024, .08, 7), lc, 0, .585, 0, { p: b });
      for (let j = 0; j < 3; j++){ const rt = M(cyl(.004, .003, .07, 3), '#E3D3BC', R(-.02, .02), -.38, 0, { p: b }); rt.rotation.z = R(-.6, .6); } }
    M(new T.TorusGeometry(.17, .028, 4, 14), '#C24A2E', 0, -.12, 0, { p: g, r: [Math.PI / 2, 0, 0], s: [1.2, .5, 1] }); }, V(.1, .2, 1));
  ri.dispose(); return OUT; };
