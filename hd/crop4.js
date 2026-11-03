window.__crop4 = (smooth) => { const OUT = {}; const ri = new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true }); ri.setPixelRatio(1); ri.setSize(320, 320); ri.setClearColor(0, 0); ri.toneMapping = T.ACESFilmicToneMapping; ri.toneMappingExposure = 1.0;
  const V = (a, b, c) => new T.Vector3(a, b, c), Q = smooth ? 1 : .45, S = n => Math.max(4, Math.round(n * Q));
  const MC = {}; const mt = c => MC[c] || (MC[c] = new T.MeshStandardMaterial({ color: c, flatShading: !smooth, roughness: smooth ? .42 : .8, metalness: 0, side: T.DoubleSide }));
  const add = (p, geo, c, x = 0, y = 0, z = 0, r, s) => { const m = new T.Mesh(geo, mt(c)); m.position.set(x, y, z); if (r) m.rotation.set(...r); if (s) m.scale.set(...s); p.add(m); return m; };
  // mặt cong dạng cánh/lá: dài L, rộng W, cụp ngang cu, cong ra sau be
  const petal = (L, W, cu = .5, be = .2, wp = .8, tip = 1) => { const ns = S(14), nt = S(8), pos = [], idx = [];
    for (let i = 0; i <= ns; i++){ const s = i / ns, w = W * Math.pow(Math.sin(Math.PI * Math.min(1, Math.pow(s, wp) * (tip ? 1 : .5) + (tip ? 0 : .5))), .8) + (tip ? 0 : 0);
      for (let j = 0; j <= nt; j++){ const t = j / nt * 2 - 1; pos.push(t * w, s * L, -cu * t * t * w + be * L * s * s); } }
    for (let i = 0; i < ns; i++) for (let j = 0; j < nt; j++){ const a = i * (nt + 1) + j, b = a + nt + 1; idx.push(a, b, a + 1, a + 1, b, b + 1); }
    const g = new T.BufferGeometry(); g.setAttribute('position', new T.Float32BufferAttribute(pos, 3)); g.setIndex(idx); g.computeVertexNormals(); return g; };
  // ống cong bán kính đổi dần
  const tubeV = (pts, rf, rs = 10) => { const cur = new T.CatmullRomCurve3(pts), n = S(24), fr = cur.computeFrenetFrames(n, false), pos = [], idx = [], R2 = S(rs);
    for (let i = 0; i <= n; i++){ const t = i / n, p = cur.getPoint(t), r = rf(t), N = fr.normals[i], B = fr.binormals[i]; for (let j = 0; j <= R2; j++){ const a = j / R2 * 6.283; pos.push(p.x + (Math.cos(a) * N.x + Math.sin(a) * B.x) * r, p.y + (Math.cos(a) * N.y + Math.sin(a) * B.y) * r, p.z + (Math.cos(a) * N.z + Math.sin(a) * B.z) * r); } }
    for (let i = 0; i < n; i++) for (let j = 0; j < R2; j++){ const a = i * (R2 + 1) + j, b = a + R2 + 1; idx.push(a, b, a + 1, a + 1, b, b + 1); }
    const g = new T.BufferGeometry(); g.setAttribute('position', new T.Float32BufferAttribute(pos, 3)); g.setIndex(idx); g.computeVertexNormals(); return g; };
  const shot = (name, build, dir = V(.15, .3, 1)) => { const sc = new T.Scene(), root = new T.Group(); sc.add(root); sd = 17; build(root);
    sc.add(new T.HemisphereLight('#fff8ec', '#8a9a70', 1.5)); sc.add(new T.AmbientLight('#ffffff', .25)); const l = new T.DirectionalLight('#fff3dc', 2.3); l.position.set(-3, 5, 6); sc.add(l); const l2 = new T.DirectionalLight('#dfe8ff', .6); l2.position.set(4, 1, -2); sc.add(l2);
    const bb = new T.Box3().setFromObject(root), c = bb.getCenter(V()), s = bb.getSize(V()), sz = Math.max(s.x, s.y) * .56; const cm = new T.OrthographicCamera(-sz, sz, sz, -sz, .01, 100); cm.position.copy(c).add(dir.clone().normalize().multiplyScalar(20)); cm.lookAt(c); ri.render(sc, cm); OUT[name] = ri.domElement.toDataURL('image/png'); };
  // ---- BẮP ----
  shot('bap', p => { const g = new T.Group(); g.rotation.z = -.62; p.add(g); const RX = .2, RY = .48;
    add(g, new T.SphereGeometry(1, S(20), S(14)), '#E39A00', 0, 0, 0, null, [RX * .93, RY * .98, RX * .93]);
    const rows = 12, cols = 12; for (let i = 0; i < rows; i++){ const v = -.88 + 1.76 * (i + .5) / rows, ry = v * RY, rr = RX * Math.sqrt(1 - v * v * .92); for (let j = 0; j < cols; j++){ const a = j / cols * 6.283 + .1, n = V(Math.cos(a) * RY, v * RX * .9, Math.sin(a) * RY).normalize();
      const kw = Math.PI * rr / cols * 1.12, kh = RY * 1.76 / rows * .58; const k = add(g, new T.SphereGeometry(1, S(10), S(8)), (i * 7 + j * 3) % 6 ? '#FFC414' : '#F5B000', Math.cos(a) * rr, ry, Math.sin(a) * rr, null, [kw, kh, .055]); { const ax = V(0, 1, 0), z = n.clone(), x = V().crossVectors(ax, z).normalize(), y = V().crossVectors(z, x); k.quaternion.setFromRotationMatrix(new T.Matrix4().makeBasis(x, y, z)); } } }
    for (const [a, L, W, be, c] of [[1.45, .8, .27, .5, '#6fbe4a'], [3.1, .72, .26, .42, '#5aa83e'], [4.85, .78, .27, .52, '#7cc04a'], [-.15, .4, .24, .4, '#86c84e']]){ const hg = new T.Group(); hg.position.y = -.56; hg.rotation.y = a; g.add(hg); add(hg, petal(L, W, 1.15, be, .75), c, 0, 0, RX * .5); }
    add(g, new T.CylinderGeometry(.08, .1, .12, S(12)), '#9fdc6e', 0, -.6, 0); }, V(.15, .2, 1));
  // ---- ỚT ----
  shot('ot', p => { const chili = (x, rz, s, col, flip) => { const g = new T.Group(); g.position.x = x; g.rotation.z = rz; p.add(g); const pts = []; for (let i = 0; i <= 8; i++){ const t = i / 8; pts.push(V(flip * Math.sin(t * 1.9) * .22 * s, -t * .78 * s, Math.sin(t * 2.2) * .04)); }
      add(g, tubeV(pts, t => s * (.12 * Math.pow(1 - t, .55) + .012) * (t < .08 ? .85 + t * 2 : 1)), col);
      add(g, new T.SphereGeometry(.112 * s, S(14), S(10)), col, 0, -.01, 0, null, [1, .5, 1]);
      for (let k = 0; k < 5; k++){ const cg = new T.Group(); cg.rotation.y = k * 1.2566; cg.position.y = .02; g.add(cg); add(cg, petal(.2 * s, .07 * s, .4, -.15, .6), '#4F9E3A', 0, 0, .02, [Math.PI / 2 + .35, 0, 0]); }
      add(g, tubeV([V(0, .02, 0), V(.02 * flip, .1 * s, 0), V(.08 * flip, .18 * s, 0)], t => .028 * s * (1 - t * .3), 7), '#5aa83e'); };
    chili(-.08, .45, 1, '#E8453A', 1); chili(.1, -.15, 1.1, '#D6352C', -1); });
  // ---- HÀNH LÁ ----
  shot('hanh', p => { const g = new T.Group(); g.rotation.z = -.28; p.add(g);
    for (const [x, z, tl, h] of [[-.12, .02, .18, 1], [-.04, -.05, .06, 1.08], [.05, .04, -.06, .95], [.13, -.02, -.18, 1.02]]){ const st = new T.Group(); st.position.set(x, 0, z); st.rotation.z = tl * .4; g.add(st);
      add(st, tubeV([V(0, -.45, 0), V(0, -.2, 0), V(0, .02, 0)], t => .068 + .012 * Math.sin(t * 3), 12), '#FBF7EE'); add(st, new T.SphereGeometry(.06, S(10), S(8)), '#F2EEE4', 0, -.46, 0, null, [1.15, .75, 1.15]);
      add(st, tubeV([V(0, 0, 0), V(0, .12, 0)], t => .066, 12), '#cfe8a0', 0, 0, 0);
      for (const sp of [-1, 1]){ const pts = [V(0, .1, 0), V(sp * .03 + tl * .2, .35 * h, 0), V(sp * .08 + tl * .6, .62 * h, .02), V(sp * .16 + tl * 1.0, .82 * h, .04)]; add(st, tubeV(pts, t => .05 * (1 - Math.pow(t, 2.4)) + .004, 10), sp > 0 ? '#5aa83e' : '#4F9E3A'); }
      for (let k = 0; k < 4; k++) add(st, tubeV([V(0, -.5, 0), V((k - 1.5) * .02, -.56, .01), V((k - 1.5) * .045, -.6, .02)], t => .006, 4), '#E3D3BC'); }
    add(g, new T.TorusGeometry(.215, .03, S(8), S(24)), '#C24A2E', 0, -.14, 0, [Math.PI / 2, 0, 0], [1.08, .5, 1]); });
  // ---- CẢI XANH (cải ngọt bó: cọng trắng xanh to, lá tròn đầu) ----
  shot('cai', p => { const lv = [[0, .55, '#4F9E3A', .5], [1.26, .62, '#5aa83e', .46], [2.52, .58, '#6fbe4a', .48], [3.78, .62, '#4F9E3A', .45], [5.03, .56, '#5aa83e', .5], [.63, .25, '#7cc04a', .46], [3.4, .28, '#86c84e', .44]];
    for (const [a, tilt, c, L] of lv){ const g = new T.Group(); g.rotation.y = a; p.add(g); const arm = new T.Group(); arm.rotation.x = tilt; g.add(arm);
      add(arm, petal(.34, .085, .7, .05, .45), '#e4f3c8', 0, 0, .02); add(arm, petal(L, .22, .4, .1, .45), c, 0, .2, .03);
      add(arm, tubeV([V(0, .2, .035), V(0, .2 + L * .7, .035 + L * .06)], t => .01 * (1 - t * .6), 5), '#cfe8a0'); } }, V(.1, .35, 1));
  // ---- CÀ CHUA ----
  shot('cachua', p => { const tom = (x, y, z, s) => { const geo = new T.SphereGeometry(s, S(24), S(16)), pp = geo.attributes.position, v = V(); for (let i = 0; i < pp.count; i++){ v.fromBufferAttribute(pp, i); const az = Math.atan2(v.z, v.x), pol = Math.acos(Math.max(-1, Math.min(1, v.y / s))); const k = 1 + .05 * Math.cos(az * 5) * Math.sin(pol); v.multiplyScalar(k); v.y *= .82; if (v.y > s * .6) v.y -= (v.y - s * .6) * .6; pp.setXYZ(i, v.x, v.y, v.z); } geo.computeVertexNormals();
      const g = new T.Group(); g.position.set(x, y, z); p.add(g); add(g, geo, '#E8453A'); for (let k = 0; k < 5; k++){ const cg = new T.Group(); cg.rotation.y = k * 1.2566 + .3; cg.position.y = s * .72; g.add(cg); add(cg, petal(s * .55, s * .2, .5, -.25, .6), '#4F9E3A', 0, 0, 0, [Math.PI / 2 - .25, 0, 0]); }
      add(g, tubeV([V(0, s * .7, 0), V(.02, s * .9, 0), V(.07, s * 1.02, 0)], t => s * .07, 7), '#5aa83e'); };
    tom(-.17, -.08, .05, .26); tom(.2, -.1, -.05, .24); tom(.02, .2, -.12, .27); });
  // ---- KHỔ QUA ----
  shot('khoqua', p => { const prof = []; for (let i = 0; i <= S(44); i++){ const t = i / S(44); prof.push(new T.Vector2(.17 * Math.pow(Math.sin(Math.PI * t), .75) * (1 - .25 * t) + .002, -.55 + t * 1.1)); }
    const geo = new T.LatheGeometry(prof, S(64)), pp = geo.attributes.position, v = V(); for (let i = 0; i < pp.count; i++){ v.fromBufferAttribute(pp, i); const az = Math.atan2(v.z, v.x), r = Math.hypot(v.x, v.z); const rg = Math.pow(Math.max(0, Math.cos(az * 9)), 2), bump = 1 + .13 * rg + .12 * rg * Math.pow(Math.max(0, Math.sin(v.y * 46 + (Math.floor((az + 3.2) / .698) % 2) * 1.6)), 2); v.x = Math.cos(az) * r * bump; v.z = Math.sin(az) * r * bump; pp.setXYZ(i, v.x, v.y, v.z); } geo.computeVertexNormals();
    for (const [x, rz, c, s] of [[-.1, .5, '#9fd36a', 1], [.13, .15, '#86c84e', .92]]){ const g = new T.Group(); g.position.x = x; g.rotation.z = rz; g.scale.setScalar(s); p.add(g); add(g, geo, c); add(g, tubeV([V(0, .52, 0), V(.03, .64, 0), V(.09, .72, 0)], t => .025, 7), '#5aa83e'); }
    const lf = new T.Group(); lf.position.set(.05, .42, -.1); p.add(lf); add(lf, petal(.32, .16, .3, .2, .8), '#4F9E3A', 0, 0, 0, [-.6, .4, -.9]); });
  ri.dispose(); return OUT; };
