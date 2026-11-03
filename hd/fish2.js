/* ===== Khuôn cá v2: thân dựng theo mặt cắt (dẹp hai bên, thon về cuống đuôi), màu tô theo từng mặt (lưng sậm, bụng sáng, sọc/đốm nằm trên da),
   vây lưng/hậu môn/ngực/bụng/đuôi là tấm phẳng có tia vây, mắt/miệng/mang/râu bám đúng mặt da. Cần sẵn trong phạm vi: T, V, add, mt, seg. ===== */
const fish2 = (p, o) => {
  const L = .4, g = new T.Group(); p.add(g); p.rotation.set(.28, -.42, .16);
  const K = o.prof;   /* [u, nửa cao, nửa dày, tâm y] từ cuống đuôi (u=0) tới mũi (u=1) */
  const at = (u, i) => { if (u <= K[0][0]) return K[0][i]; for (let k = 1; k < K.length; k++) if (u <= K[k][0]){ const a = K[k - 1], b = K[k], t = (u - a[0]) / (b[0] - a[0]), s = t * t * (3 - 2 * t); return a[i] + (b[i] - a[i]) * s; } return K[K.length - 1][i]; };
  const nose = u => u > o.nose ? Math.sqrt(Math.max(0, 1 - Math.pow((u - o.nose) / (1 - o.nose), 2))) : 1;
  const P = (u, t) => { const h = at(u, 1) * nose(u), w = at(u, 2) * nose(u), yc = at(u, 3); return V(-L + 2 * L * u, yc + h * Math.sin(t), w * Math.cos(t)); };
  const N = (u, t) => { const e = .002, a = P(Math.min(1, u + e), t).sub(P(Math.max(0, u - e), t)), b = P(u, t + e).sub(P(u, t - e)); return V().crossVectors(a, b).normalize(); };
  g.userData.P = P; g.userData.N = N;
  /* thân */
  const NU = 34, NT = 18, pos = [], col = [], cA = new T.Color(o.back), cB = new T.Color(o.side || o.back), cC = new T.Color(o.belly), tmp = new T.Color();
  const colAt = (u, t) => { const y = Math.sin(t), c = y > .35 ? cA.clone().lerp(cB, (1 - y) / .65 * .6) : y > -.25 ? cB.clone() : cB.clone().lerp(cC, Math.min(1, (-.25 - y) / .45)); const q = o.pat && o.pat(u, t, y); return q ? tmp.set(q).clone() : c; };
  const uu = i => { const s = i / NU; return 1 - Math.pow(1 - s, 1.25); };
  for (let i = 0; i < NU; i++) for (let j = 0; j < NT; j++){ const u0 = uu(i), u1 = uu(i + 1), t0 = -Math.PI / 2 + j / NT * 2 * Math.PI, t1 = -Math.PI / 2 + (j + 1) / NT * 2 * Math.PI;
    const a = P(u0, t0), b = P(u1, t0), c = P(u1, t1), d = P(u0, t1), k = colAt((u0 + u1) / 2, (t0 + t1) / 2);
    for (const v of [a, b, c, a, c, d]){ pos.push(v.x, v.y, v.z); col.push(k.r, k.g, k.b); } }
  { const h = at(0, 1), cy = at(0, 3), w = at(0, 2), c0 = V(-L, cy, 0); for (let j = 0; j < NT; j++){ const a = P(0, -Math.PI / 2 + j / NT * 2 * Math.PI), b = P(0, -Math.PI / 2 + (j + 1) / NT * 2 * Math.PI); for (const v of [c0, b, a]) { pos.push(v.x, v.y, v.z); col.push(cB.r, cB.g, cB.b); } } }
  const bg = new T.BufferGeometry(); bg.setAttribute('position', new T.Float32BufferAttribute(pos, 3)); bg.setAttribute('color', new T.Float32BufferAttribute(col, 3)); bg.computeVertexNormals();
  const body = new T.Mesh(bg, new T.MeshStandardMaterial({ vertexColors: true, flatShading: true, roughness: .8, side: T.DoubleSide })); body.castShadow = body.receiveShadow = true; g.add(body);
  /* tấm vây phẳng: pts là đa giác 2D trong mặt phẳng XY; rays = các tia vây (cặp điểm) vẽ đậm hơn */
  const finCol = o.fin || o.back, rayCol = o.ray || new T.Color(finCol).multiplyScalar(.7).getStyle();
  const plate = (par, pts, rays, c = finCol, rc = rayCol, edge) => { const mk = (ps, cc, z) => { const sh = new T.Shape(); ps.forEach(([x, y], i) => i ? sh.lineTo(x, y) : sh.moveTo(x, y)); const mm = add(par, new T.ShapeGeometry(sh), cc); mm.position.z = z; return mm; }; let m;
    if (edge){ const cx = pts.reduce((a, q) => a + q[0], 0) / pts.length, cy = pts.reduce((a, q) => a + q[1], 0) / pts.length; mk(pts.map(([x, y]) => [cx + (x - cx) * 1.1, cy + (y - cy) * 1.1]), edge, 0); m = mk(pts, c, .0016); mk(pts, c, -.0016); } else m = mk(pts, c, 0); (rays || []).forEach(([a, b]) => { const d = V(b[0] - a[0], b[1] - a[1], 0), l = d.length(), q = add(par, new T.PlaneGeometry(l, .005), rc, (a[0] + b[0]) / 2, (a[1] + b[1]) / 2, 0); q.rotation.z = Math.atan2(d.y, d.x); }); return m; };
  const topY = u => at(u, 3) + at(u, 1) * nose(u), botY = u => at(u, 3) - at(u, 1) * nose(u), X = u => -L + 2 * L * u;
  /* vây lưng / vây hậu môn: chân vây cắm ngập vào thân 0,012; spec = [u đầu, u cuối, cao đầu, cao cuối, kiểu] */
  const median = (spec, top) => { const [u0, u1, h0, h1, kind] = spec, n = 9, pts = [], rays = [], sg = top ? 1 : -1, edge = u => (top ? topY(u) : botY(u)) - sg * .012;
    for (let i = 0; i <= n; i++){ const u = u0 + (u1 - u0) * i / n; pts.push([X(u), edge(u)]); }
    for (let i = n; i >= 0; i--){ const u = u0 + (u1 - u0) * i / n, f = i / n, hh = kind === 'round' ? (h0 + (h1 - h0) * f) * Math.sin(Math.PI * Math.min(1, .15 + f * .85)) : kind === 'sail' ? h0 * Math.pow(1 - f, .6) * (f < .1 ? f / .1 : 1) + h1 * f : h0 + (h1 - h0) * f, spike = kind === 'spiny' && i % 2 ? -.35 : 0, base = edge(u) + sg * .012;
      pts.push([X(u) - (kind === 'sail' ? .04 * f : .015), base + sg * hh * (1 + spike)]); if (i % 2 === 0 || kind !== 'spiny') rays.push([[X(u), base - sg * .006], [X(u) - .015, base + sg * hh * .96]]); }
    plate(g, pts, rays, top ? (o.dorsalCol || finCol) : (o.analCol || finCol), rayCol, top ? o.dorsalEdge : o.analEdge); };
  (o.dorsal || []).forEach(s => median(s, true)); (o.anal || []).forEach(s => median(s, false));
  /* đuôi: gắn ngập vào cuống đuôi */
  { const hp = at(0, 1), cy = at(0, 3), x0 = -L + .03, Lt = o.tailL || .2, kind = o.tail || 'fork', pts = [], rays = [];
    if (kind === 'fork'){ pts.push([x0, cy + hp * .9], [x0 - Lt * .55, cy + hp + Lt * .62], [x0 - Lt, cy + hp + Lt * .78], [x0 - Lt * .62, cy], [x0 - Lt, cy - hp - Lt * .78], [x0 - Lt * .55, cy - hp - Lt * .62], [x0, cy - hp * .9]); }
    else if (kind === 'round'){ pts.push([x0, cy + hp * .9]); for (let i = 0; i <= 10; i++){ const a = Math.PI / 2 - i / 10 * Math.PI; pts.push([x0 - Lt * .3 - Lt * .7 * Math.cos(a), cy + (hp + Lt * .5) * Math.sin(a)]); } pts.push([x0, cy - hp * .9]); }
    else { pts.push([x0, cy + hp], [x0 - Lt, cy + hp * .2], [x0 - Lt * 1.05, cy], [x0 - Lt, cy - hp * .2], [x0, cy - hp]); }
    for (let i = 0; i < 7; i++){ const f = i / 6 - .5, e = kind === 'fork' ? [x0 - Lt * (.62 + .38 * Math.abs(f * 2)), cy + f * 2 * (hp + Lt * .7)] : kind === 'round' ? [x0 - Lt * .3 - Lt * .7 * Math.cos(f * Math.PI) * .95, cy + (hp + Lt * .5) * Math.sin(f * Math.PI) * .95] : [x0 - Lt * .95, cy + f * hp * .4]; rays.push([[x0 + .005, cy + f * hp * 1.2], e]); }
    plate(g, pts, rays, o.tailCol || finCol, o.tailRay || rayCol, o.tailEdge); }
  /* vây chẵn: ngực, bụng, hai bên; chân vây nằm trên da */
  const pair = (u, t, len, wid, tilt, droop, c = finCol) => { for (const sg of [-1, 1]){ const tt = sg > 0 ? t : Math.PI - t, b = P(u, tt), f = new T.Group(); f.position.copy(b); g.add(f); f.rotation.set(0, sg * tilt, droop);
      plate(f, [[.008, .01], [-len * .45, wid * .55], [-len, wid * .25], [-len * .95, -wid * .2], [-len * .4, -wid * .45], [.008, -.008]], [[[0, 0], [-len * .9, wid * .2]], [[0, 0], [-len * .9, 0]], [[0, 0], [-len * .85, -wid * .15]]], c); } };
  if (o.pect) pair(o.pect[0], o.pect[1], o.pect[2], o.pect[3], .55, -.35);
  if (o.pelv) pair(o.pelv[0], o.pelv[1], o.pelv[2], o.pelv[3], .35, -.6, o.pelvCol || finCol);
  /* chi tiết bám da */
  const onSkin = (u, t, sg, out = 0) => { const tt = sg > 0 ? t : Math.PI - t; return { p: P(u, tt).add(N(u, tt).multiplyScalar(out)), n: N(u, tt) }; };
  const tubeOn = (pts, r, c) => { const m = add(g, new T.TubeGeometry(new T.CatmullRomCurve3(pts), pts.length * 4, r, 4, false), c); m.castShadow = false; return m; };
  for (const sg of [-1, 1]){
    { const er = o.eye || .03, s = onSkin(o.eyeU || .86, o.eyeT || .35, sg), q = new T.Quaternion().setFromUnitVectors(V(0, 0, 1), s.n);
      const e = add(g, new T.SphereGeometry(er, 10, 8), o.eyeRim || '#F2E6B8', s.p.x, s.p.y, s.p.z, null, [1, 1, .55]); e.quaternion.copy(q);
      const pu = add(g, new T.SphereGeometry(er * .62, 10, 8), '#141414', ...s.p.clone().addScaledVector(s.n, er * .38).toArray(), null, [1, 1, .45]); pu.quaternion.copy(q);
      add(g, new T.SphereGeometry(er * .2, 6, 4), '#FFFFFF', ...s.p.clone().addScaledVector(s.n, er * .62).add(V(er * .18, er * .22, 0)).toArray()); }
    if (o.gill !== false){ const gu = o.gillU || .74, pts = []; for (let k = 0; k <= 6; k++){ const t = -.85 + k / 6 * 1.75; pts.push(onSkin(gu + Math.cos(t) * .025, t, sg, .002).p); } tubeOn(pts, .0035, o.gillCol || new T.Color(o.side || o.back).multiplyScalar(.6).getStyle()); }
    { const mt0 = o.mouthT || -.15, ml = o.mouthL || .06, pts = []; for (let k = 0; k <= 4; k++){ pts.push(onSkin(1 - ml + ml * k / 4 - .003, mt0 + k / 4 * .05, sg, .002).p); } tubeOn(pts, .004, '#3A2418'); }
    for (const [bu, bt, len, dy] of (o.barbels || [])){ const s = onSkin(bu, bt, sg, -.003), d = V(.05, dy, sg * .05).normalize(); const a = s.p, b = a.clone().addScaledVector(d, len * .5), c = b.clone().add(V(-len * .1, -len * .35, sg * len * .15)); seg(g, a, b, .006, .004, o.barbCol || '#4A3A2A'); seg(g, b, c, .004, .002, o.barbCol || '#4A3A2A'); }
    (o.spots || []).forEach(([u, t, r, c]) => { const s = onSkin(u, t, sg, -r * .55), m = add(g, new T.SphereGeometry(r, 8, 6), c, s.p.x, s.p.y, s.p.z, null, [1, 1, .4]); m.quaternion.setFromUnitVectors(V(0, 0, 1), s.n); });
  }
  if (o.threads) for (const sg of [-1, 1]){ const [u, len] = o.threads, s0 = onSkin(u, -1.25, sg, -.004).p, pts = [s0, s0.clone().add(V(-len * .15, -len * .25, sg * .02)), s0.clone().add(V(-len * .5, -len * .45, sg * .035)), s0.clone().add(V(-len, -len * .5, sg * .04))]; tubeOn(pts, .0035, o.threadCol || finCol); }
  if (o.extra) o.extra(g, { P, N, onSkin, plate, tubeOn, L, X, topY, botY, at });
  return g; };

/* tôm càng xanh: đầu ngực có chủy răng cưa, bụng 6 đốt cong úp chồng mí, quạt đuôi, mắt cuống, 2 càng xanh dài nhiều đốt kẹp mở, 5 đôi chân bò, râu dài vắt ra sau */
const tom2 = (p, o = {}) => { const g = new T.Group(); p.add(g); p.rotation.set(.62, -.3, .05);   /* nghiêng lưng về phía người nhìn để thấy quạt đuôi xòe */
  const cb = o.body || '#4F7F92', cd = o.dark || '#2F566A', cc = o.claw || '#1F5FA8', cj = o.joint || '#E07A3A', cl = o.leg || '#6E98A8';
  const ell = (c, x, y, z, rx, ry, rz, rot) => { const m = add(g, new T.SphereGeometry(1, 12, 9), c, x, y, z, rot || null, [rx, ry, rz]); return m; };
  /* đầu ngực */
  ell(cb, .12, .02, 0, .2, .1, .085); ell(cd, .14, .085, 0, .17, .035, .06);
  { const sh = new T.Shape(); sh.moveTo(0, 0); for (let i = 0; i <= 8; i++) sh.lineTo(.03 + i * .025, .025 + (i % 2 ? .012 : 0) - i * .002); sh.lineTo(.24, .012); sh.lineTo(.03, -.012); sh.lineTo(0, 0); add(g, new T.ShapeGeometry(sh), cd, .26, .06, 0, [0, 0, .25]); }
  /* bụng: 6 đốt cong xuống, mỗi đốt chồng mí lên đốt sau */
  const ab = []; let ang = .15; for (let i = 0; i < 6; i++){ const r = .085 - i * .009, a = ang; ang += .3; const cx = -.04 - i * .074, cy = .02 - Math.pow(i, 1.5) * .0085;   /* bụng duỗi ra sau, chỉ hơi cong để quạt đuôi xòe thấy rõ */ ab.push([cx, cy, r]); ell(i % 2 ? cb : (o.body2 || '#5A8EA2'), cx, cy, 0, r * 1.05, r * .95, r * .9); ell(cd, cx + .01, cy + r * .55, 0, r * .8, r * .35, r * .75); }
  { const [x4, y4] = ab[4], [x, y, r] = ab[5], d = V(x - x4, y - y4, 0).normalize(), tf = new T.Group(); tf.position.set(x + d.x * r * .8, y + d.y * r * .8, 0); tf.quaternion.setFromUnitVectors(V(1, 0, 0), d); g.add(tf);   /* quạt đuôi: telson nhọn ở giữa + 2 cặp lá đuôi xòe ngang, nối liền đốt cuối, hơi khum */
    const blade = (len, wid, c) => { const sh = new T.Shape(); sh.moveTo(0, -wid * .35); sh.quadraticCurveTo(len * .55, -wid, len, -wid * .2); sh.quadraticCurveTo(len * 1.04, 0, len, wid * .2); sh.quadraticCurveTo(len * .55, wid, 0, wid * .35); sh.lineTo(0, -wid * .35); const ge = new T.ShapeGeometry(sh, 6); ge.rotateX(Math.PI / 2); return add(tf, ge, c); };
    { const sh = new T.Shape(); sh.moveTo(-.01, -.018); sh.lineTo(.14, -.007); sh.lineTo(.155, 0); sh.lineTo(.14, .007); sh.lineTo(-.01, .018); const ge = new T.ShapeGeometry(sh); ge.rotateX(Math.PI / 2); add(tf, ge, cd, 0, .004, 0); }
    for (const sg of [-1, 1]) for (const [a, len, wid, c] of [[.3, .14, .036, cb], [.62, .12, .032, o.body2 || cb]]){ const m = blade(len, wid, c); m.rotation.set(sg * .12, -sg * a, 0); m.position.set(-.008, -.002, sg * .008); }
    add(tf, new T.SphereGeometry(r * .55, 10, 8), cb, -.01, 0, 0, null, [1, .7, 1.1]); }
  /* chân bơi dưới bụng */
  for (let i = 0; i < 5; i++){ const [x, y, r] = ab[i]; for (const sg of [-1, 1]) seg(g, V(x, y - r * .7, sg * r * .4), V(x - .01, y - r * .7 - .05, sg * r * .55), .006, .003, cl); }
  /* mắt cuống */
  for (const sg of [-1, 1]){ const a = V(.27, .06, sg * .03), b = V(.31, .1, sg * .07); seg(g, a, b, .012, .012, cd); add(g, new T.SphereGeometry(.022, 8, 6), '#141414', b.x, b.y, b.z); add(g, new T.SphereGeometry(.007, 5, 4), '#FFFFFF', b.x + .008, b.y + .01, b.z + sg * .012); }
  /* râu */
  for (const sg of [-1, 1]){ const pts = [V(.3, .05, sg * .04), V(.38, .14, sg * .1), V(.18, .24, sg * .16), V(-.12, .26, sg * .2), V(-.34, .2, sg * .22)]; add(g, new T.TubeGeometry(new T.CatmullRomCurve3(pts), 30, .004, 4, false), cl); add(g, new T.TubeGeometry(new T.CatmullRomCurve3([V(.31, .04, sg * .02), V(.42, .06, sg * .05), V(.5, .1, sg * .06)]), 10, .004, 4, false), cl); }
  /* 4 đôi chân bò */
  for (let i = 0; i < 4; i++) for (const sg of [-1, 1]){ const x = .2 - i * .055, a = V(x, -.04, sg * .05), b = V(x + .01, -.11, sg * .13), c = V(x + .03, -.17, sg * .14); seg(g, a, b, .009, .007, cl); seg(g, b, c, .007, .004, cl); add(g, new T.SphereGeometry(.009, 6, 4), cj, b.x, b.y, b.z); }
  /* càng: đôi chân thứ hai dài, đốt xanh nối khớp cam, kẹp mở (tép: càng nhỏ ngắn) */
  if (o.tep) for (const sg of [-1, 1]){ const j0 = V(.24, -.04, sg * .05), j1 = V(.34, -.08, sg * .12), j2 = V(.44, -.06, sg * .14); seg(g, j0, j1, .008, .007, cc); seg(g, j1, j2, .007, .005, cc); add(g, new T.SphereGeometry(.009, 6, 4), cj, j1.x, j1.y, j1.z); }
  else for (const sg of [-1, 1]){ const j0 = V(.22, -.04, sg * .06), j1 = V(.36, -.06, sg * .2), j2 = V(.58, -.02, sg * .26), j3 = V(.78, .04, sg * .24);
    seg(g, j0, j1, .014, .013, cc); seg(g, j1, j2, .013, .014, cc); seg(g, j2, j3, .016, .02, cc); for (const j of [j1, j2]) add(g, new T.SphereGeometry(.018, 8, 6), cj, j.x, j.y, j.z);
    const d = j3.clone().sub(j2).normalize(), up = V(0, 1, 0), f1 = j3.clone().addScaledVector(d, .14).addScaledVector(up, .035), f2 = j3.clone().addScaledVector(d, .13).addScaledVector(up, -.03);
    seg(g, j3, f1, .016, .004, cc); seg(g, j3, f2, .014, .004, cd); add(g, new T.SphereGeometry(.02, 8, 6), cc, j3.x, j3.y, j3.z); add(g, new T.SphereGeometry(.007, 5, 4), cj, f1.x, f1.y, f1.z); }
  return g; };
