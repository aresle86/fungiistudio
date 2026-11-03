window.__crop5 = () => { const OUT = {}; const ri = new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true }); ri.setPixelRatio(1); ri.setSize(320, 320); ri.setClearColor(0, 0); ri.toneMapping = T.ACESFilmicToneMapping; ri.toneMappingExposure = 1.0;
  const V = (a, b, c) => new T.Vector3(a, b, c); let seed = 7; const rn = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const MC = {}; const mt = c => MC[c] || (MC[c] = new T.MeshStandardMaterial({ color: c, flatShading: true, roughness: .85, metalness: 0, side: T.DoubleSide }));
  const jit = (g, a) => { g = g.index ? g.toNonIndexed() : g; const p = g.attributes.position, key = {}, v = V(); for (let i = 0; i < p.count; i++){ v.fromBufferAttribute(p, i); const k = v.x.toFixed(3) + ',' + v.y.toFixed(3) + ',' + v.z.toFixed(3); if (!key[k]) key[k] = [(rn() - .5) * a, (rn() - .5) * a, (rn() - .5) * a]; const d = key[k]; p.setXYZ(i, v.x + d[0], v.y + d[1], v.z + d[2]); } g.computeVertexNormals(); return g; };
  const add = (p, geo, c, x = 0, y = 0, z = 0, r, s) => { const m = new T.Mesh(geo, mt(c)); m.position.set(x, y, z); if (r) m.rotation.set(...r); if (s) m.scale.set(...s); p.add(m); return m; };
  // lá phẳng nhiều mặt: dài L, rộng W, gân giữa gập fo, cong ra be
  const blade = (L, W, fo = .25, be = .15, ns = 4, wp = .7) => { const pos = []; const pt = (s, t) => { const w = W * Math.sin(Math.PI * Math.min(.999, Math.pow(s, wp))) * (1 - s * .15); return [t * w, s * L, -Math.abs(t) * w * fo + be * L * s * s]; };
    for (let i = 0; i < ns; i++){ const s0 = i / ns, s1 = (i + 1) / ns; for (const [t0, t1] of [[-1, 0], [0, 1]]){ const a = pt(s0, t0), b = pt(s0, t1), c = pt(s1, t0), d = pt(s1, t1); pos.push(...a, ...b, ...c, ...c, ...b, ...d); } }
    const g = new T.BufferGeometry(); g.setAttribute('position', new T.Float32BufferAttribute(pos, 3)); g.computeVertexNormals(); return g; };
  // ống cong, ít mặt
  const tube = (pts, rf, n = 6, rs = 6) => { const cur = new T.CatmullRomCurve3(pts), fr = cur.computeFrenetFrames(n, false), pos = [], idx = [];
    for (let i = 0; i <= n; i++){ const t = i / n, p = cur.getPoint(t), r = rf(t), N = fr.normals[i], B = fr.binormals[i]; for (let j = 0; j <= rs; j++){ const a = j / rs * 6.283; pos.push(p.x + (Math.cos(a) * N.x + Math.sin(a) * B.x) * r, p.y + (Math.cos(a) * N.y + Math.sin(a) * B.y) * r, p.z + (Math.cos(a) * N.z + Math.sin(a) * B.z) * r); } }
    for (let i = 0; i < n; i++) for (let j = 0; j < rs; j++){ const a = i * (rs + 1) + j, b = a + rs + 1; idx.push(a, b, a + 1, a + 1, b, b + 1); }
    const g = new T.BufferGeometry(); g.setAttribute('position', new T.Float32BufferAttribute(pos, 3)); g.setIndex(idx); return g.toNonIndexed(); };
  const fin = g => { g.computeVertexNormals(); return g; };
  const shot = (name, build, dir = V(.25, .35, 1)) => { const sc = new T.Scene(), root = new T.Group(); sc.add(root); seed = 7 + name.length; build(root);
    sc.add(new T.HemisphereLight('#fff8ec', '#8a9a70', 1.45)); sc.add(new T.AmbientLight('#ffffff', .2)); const l = new T.DirectionalLight('#fff3dc', 2.4); l.position.set(-3, 5, 5); sc.add(l);
    const bb = new T.Box3().setFromObject(root), c = bb.getCenter(V()), s = bb.getSize(V()), sz = Math.max(s.x, s.y) * .56; const cm = new T.OrthographicCamera(-sz, sz, sz, -sz, .01, 100); cm.position.copy(c).add(dir.clone().normalize().multiplyScalar(20)); cm.lookAt(c); ri.render(sc, cm); OUT[name] = ri.domElement.toDataURL('image/png'); };
  // ---- ỚT: hai trái song song, so le trước sau, cùng hướng cong ----
  shot('ot', p => { const chili = (x, y, z, s, col, colD) => { const g = new T.Group(); g.position.set(x, y, z); g.rotation.z = -.25; p.add(g);
      const pts = [V(0, 0, 0), V(.02 * s, -.17 * s, 0), V(.07 * s, -.36 * s, 0), V(.15 * s, -.52 * s, 0), V(.27 * s, -.62 * s, 0)];
      add(g, fin(jit(tube(pts, t => s * (.125 * Math.pow(1 - t, .5) + .008) * (t < .1 ? .8 + t * 2 : 1), 7, 6), .006)), col);
      add(g, fin(jit(new T.IcosahedronGeometry(.1 * s, 0), .004)), colD, 0, .0, 0, null, [1.2, .6, 1.2]);
      add(g, fin(new T.ConeGeometry(.1 * s, .07 * s, 5)), '#4F9E3A', 0, .035 * s, 0);
      add(g, fin(tube([V(0, .05 * s, 0), V(-.01 * s, .14 * s, 0), V(.04 * s, .22 * s, 0)], t => .022 * s, 3, 5)), '#5aa83e'); };
    chili(-.1, .1, -.18, .92, '#C9302A', '#B02A25'); chili(.06, 0, .12, 1, '#E8453A', '#D6352C'); }, V(.15, .25, 1));
  // ---- BẮP: trái bắp nhiều mặt, lá vỏ nằm ngoài trái, ngọn vểnh ----
  shot('bap', p => { const g = new T.Group(); g.rotation.z = -.5; p.add(g);
    const prof = [[.0, -.48], [.11, -.44], [.16, -.34], [.18, -.22], [.19, -.1], [.19, .02], [.18, .14], [.16, .26], [.13, .37], [.08, .46], [.0, .51]].map(([r, y]) => new T.Vector2(r, y));
    const cobg = new T.LatheGeometry(prof, 10).toNonIndexed(), P = prof.length, col = [], cA = new T.Color('#FFD23F'), cB = new T.Color('#F2B824'); for (let i = 0; i < cobg.attributes.position.count / 3; i++){ const q = Math.floor(i / 2), seg = Math.floor(q / (P - 1)), ring = q % (P - 1), c = (seg + ring) % 2 ? cA : cB; for (let k = 0; k < 3; k++) col.push(c.r, c.g, c.b); }
    cobg.setAttribute('color', new T.Float32BufferAttribute(col, 3)); cobg.computeVertexNormals(); const cm = new T.Mesh(cobg, new T.MeshStandardMaterial({ vertexColors: true, flatShading: true, roughness: .85 })); g.add(cm);
    const husk = (a, L, W, lean, col) => { const h = new T.Group(); h.rotation.y = a; g.add(h); const pv = new T.Group(); pv.position.set(0, -.44, .13); pv.rotation.x = lean; h.add(pv); add(pv, fin(blade(L, W, .12, .1, 4)), col); };
    husk(-.95, .8, .24, .3, '#5aa83e'); husk(.95, .84, .24, .28, '#6fbe4a'); husk(3.14, .78, .22, .3, '#4F9E3A'); husk(.0, .46, .2, .42, '#7cc04a');
    add(g, fin(new T.CylinderGeometry(.06, .08, .14, 6)), '#86B06A', 0, -.53, 0); }, V(.2, .2, 1));
  // ---- HÀNH LÁ: thân trắng ngắn, lá xanh dài mảnh, rễ ----
  shot('hanh', p => { const g = new T.Group(); g.rotation.z = -.32; p.add(g);
    for (const [x, z, sp, h] of [[-.1, .02, -.12, 1], [-.035, -.04, -.04, 1.08], [.03, .04, .04, .96], [.095, -.02, .12, 1.03], [0, .08, .0, .92]]){ const s = new T.Group(); s.position.set(x, 0, z); g.add(s);
      add(s, fin(new T.CylinderGeometry(.042, .047, .26, 6)), '#FBF7EE', 0, -.3, 0); add(s, fin(new T.IcosahedronGeometry(.052, 0)), '#F2EEE4', 0, -.44, 0, null, [1, .8, 1]);
      add(s, fin(new T.CylinderGeometry(.038, .042, .14, 6)), '#cfe8a0', 0, -.1, 0);
      add(s, fin(tube([V(0, -.03, 0), V(sp * .3, .35 * h, 0), V(sp * .8, .7 * h, .01), V(sp * 1.6, .95 * h, .02)], t => .036 * (1 - Math.pow(t, 2.5)) + .004, 6, 6)), (x * 100 | 0) % 2 ? '#5aa83e' : '#4F9E3A');
      for (let k = 0; k < 3; k++) add(s, fin(tube([V(0, -.47, 0), V((k - 1) * .02, -.52, 0), V((k - 1) * .04, -.56, .01)], t => .005, 2, 3)), '#E3D3BC'); }
    add(g, fin(new T.TorusGeometry(.14, .026, 4, 8)), '#C24A2E', 0, -.15, 0, [Math.PI / 2, 0, 0], [1, .62, 1]); }, V(.2, .3, 1));
  // ---- CÀ CHUA: ba trái nhiều mặt ----
  shot('cachua', p => { const tom = (x, y, z, s, col) => { const geo = fin(jit(new T.IcosahedronGeometry(s, 1), s * .06)); const g = new T.Group(); g.position.set(x, y, z); p.add(g); add(g, geo, col, 0, 0, 0, null, [1, .84, 1]);
      add(g, fin(new T.ConeGeometry(s * .42, s * .14, 5)), '#4F9E3A', 0, s * .86, 0); add(g, fin(new T.CylinderGeometry(s * .05, s * .06, s * .22, 4)), '#5aa83e', 0, s * 1.0, 0, [0, 0, .3]); };
    tom(-.17, -.08, .05, .26, '#E8453A'); tom(.2, -.1, -.05, .24, '#D6352C'); tom(.02, .2, -.14, .26, '#E25A3B'); });
  // ---- KHỔ QUA: hai trái so le, gân nổi ----
  shot('khoqua', p => { const mk = (x, y, z, rz, s, col) => { const prof = []; for (let i = 0; i <= 9; i++){ const t = i / 9; prof.push(new T.Vector2((.15 * Math.pow(Math.sin(Math.PI * t), .7) * (1 - .25 * t) + .004) * s, (-.5 + t) * s)); }
      const geo = new T.LatheGeometry(prof, 10).toNonIndexed(), pp = geo.attributes.position, v = V(); for (let i = 0; i < pp.count; i++){ v.fromBufferAttribute(pp, i); const az = Math.atan2(v.z, v.x), r = Math.hypot(v.x, v.z), ridge = Math.round(az / (6.283 / 10) * 2) % 2 === 0 ? 1.12 : .96; v.x = Math.cos(az) * r * ridge; v.z = Math.sin(az) * r * ridge; pp.setXYZ(i, v.x, v.y, v.z); }
      const g = new T.Group(); g.position.set(x, y, z); g.rotation.z = rz; p.add(g); add(g, fin(geo), col); for (let r = 0; r < 10; r += 2) for (let k = 1; k < 8; k++){ const tt = k / 8, yy = (-.5 + tt) * s, rr = (.15 * Math.pow(Math.sin(Math.PI * tt), .7) * (1 - .25 * tt)) * s * 1.1, a = r / 10 * 6.283 + (k % 2) * .25; add(g, fin(new T.IcosahedronGeometry(.022 * s, 0)), col, Math.cos(a) * rr, yy, Math.sin(a) * rr); } add(g, fin(tube([V(0, .5 * s, 0), V(.02, .6 * s, 0), V(.07, .66 * s, 0)], t => .022, 3, 5)), '#5aa83e'); };
    mk(-.1, .05, -.15, .42, .95, '#86c84e'); mk(.1, 0, .12, .3, 1, '#9fd36a'); }, V(.15, .25, 1));
  // ---- CẢI XANH: bó cải cọng trắng, lá to nhiều mặt ----
  shot('cai', p => { const lv = [[0, .3, '#4F9E3A', .42], [1.25, .36, '#5aa83e', .4], [2.5, .32, '#6fbe4a', .42], [3.75, .36, '#4F9E3A', .4], [5.0, .3, '#5aa83e', .42]];
    for (const [a, tilt, c, L] of lv){ const g = new T.Group(); g.rotation.y = a; p.add(g); const arm = new T.Group(); arm.rotation.x = tilt; g.add(arm);
      add(arm, fin(blade(.34, .07, .45, .0, 3, 1.4)), '#e9f5d2', 0, 0, .05); add(arm, fin(blade(L, .2, .25, .06, 4, 1.5)), c, 0, .26, .05); add(arm, fin(new T.CylinderGeometry(.008, .012, L * .8, 3)), '#cfe8a0', 0, .26 + L * .4, .05); }
    add(p, fin(new T.CylinderGeometry(.09, .08, .06, 7)), '#e9f5d2', 0, .0, 0); }, V(.1, .3, 1));
  ri.dispose(); return OUT; };
