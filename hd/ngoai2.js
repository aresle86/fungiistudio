window.__ngoai = () => { const OUT = {}; const ri = new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true }); ri.setPixelRatio(1); ri.setSize(480, 560); ri.setClearColor(0, 0); ri.toneMapping = T.ACESFilmicToneMapping; ri.toneMappingExposure = 1.02; ri.shadowMap.enabled = true;
  const SK = '#E3BC97', SKD = '#D2A57E', HAIR = '#E8DFCC', HAIRL = '#FBF7EE', AO = '#8A5D3B', AOD = '#6B4529', QUAN = '#2B3446';
  const ball = (r, d = 1) => new T.IcosahedronGeometry(r, d);
  function body(g, up = false, o = {}){ const arm = o.arm ?? (up ? 2.55 : .32);
    // chân + dép
    for (const sx of [-1, 1]){ const lg = G(sx * .1, .28, 0, 0, g); if (o.hop && sx > 0){ lg.rotation.x = 1.25; lg.position.y += .03; } M(cyl(.085, .105, .24, 8), QUAN, 0, -.12, 0, { p: lg }); M(ball(.07, 1), SK, 0, -.24, .02, { p: lg, s: [1, .6, 1.3] }); M(box(.12, .02, .2), '#B48560', 0, -.272, .03, { p: lg }); }
    // thân áo bà ba tròn
    M(ball(.25, 1), AO, 0, .45, 0, { p: g, s: [1, .92, .9] }); M(cyl(.22, .25, .08, 9), AO, 0, .31, 0, { p: g });
    for (const y of [.36, .45, .54]) M(ball(.018, 1), '#E8DFCC', 0, y, .222, { p: g });
    // khăn rằn vắt vai
    for (let k = 0; k < 8; k++) M(ball(.05, 1), k % 2 ? QUAN : '#FBF7EE', Math.cos(k / 7 * Math.PI) * .2, .6 + Math.sin(k / 7 * Math.PI) * .02, .04 + Math.sin(k / 7 * Math.PI) * .1, { p: g, s: [1, .6, 1] });
    for (let k = 0; k < 4; k++) M(box(.07, .05, .04), k % 2 ? QUAN : '#FBF7EE', .17, .54 - k * .05, .17, { p: g });
    // tay mập
    for (const sx of [-1, 1]){ const a = G(sx * .19, .55, .02, 0, g); a.rotation.z = sx * arm; M(ball(.07, 1), AO, 0, 0, 0, { p: a }); M(cyl(.06, .07, .2, 7), AO, 0, -.1, 0, { p: a }); M(ball(.065, 1), SK, 0, -.22, 0, { p: a }); }
    M(ball(.06, 1), SK, 0, .66, 0, { p: g }); }
  function head(g, hair){ const h = G(0, .9, 0, 0, g);
    M(ball(.3, 2), SK, 0, 0, 0, { p: h, s: [1.05, .95, .95] });
    for (const sx of [-1, 1]) M(ball(.06, 1), SKD, sx * .31, -.01, 0, { p: h, s: [.6, 1, .8] });
    M(ball(.035, 1), SKD, 0, -.04, .29, { p: h });
    hair(h); return h; }
  const HAIR_BASE = h => { M(ball(.31, 2), HAIR, 0, .07, -.04, { p: h, s: [1.08, .82, 1.02] }); for (let k = 0; k < 5; k++) M(ball(.07, 1), HAIR, -.16 + k * .08, .15, .22 - Math.abs(k - 2) * .02, { p: h, s: [1, .7, .6] }); };
  const HAIRS = {
    tran(h){ HAIR_BASE(h); M(ball(.15, 1), HAIRL, 0, .3, -.18, { p: h }); M(cyl(.012, .012, .3, 4), '#C9952A', .04, .3, -.18, { p: h, r: [0, 0, 1.3] }); },
    non(h){ HAIR_BASE(h); const n = G(0, .135, -.01, 0, h); n.rotation.x = -.1; M(new T.ConeGeometry(.55, .3, 14), '#E3BC97', 0, .15, 0, { p: n }); for (let k = 1; k < 5; k++){ const y = .3 * k / 5, r = .55 * (1 - y / .3) + .004; M(new T.TorusGeometry(r, .007, 3, 28), '#C9952A', 0, y, 0, { p: n, r: [Math.PI / 2, 0, 0], cast: false }); } M(new T.TorusGeometry(.552, .012, 3, 28), '#B48560', 0, .002, 0, { p: n, r: [Math.PI / 2, 0, 0] }); },
    khan(h){ HAIR_BASE(h); for (let k = 0; k < 5; k++) M(new T.TorusGeometry(.26 - k * .02, .045, 5, 12), k % 2 ? QUAN : '#FBF7EE', 0, .14 + k * .045, -.03, { p: h, r: [Math.PI / 2 - .2, 0, 0] }); M(ball(.07, 1), QUAN, .18, .26, .16, { p: h }); } };
  function face(h, ex){ const z = .272, f = G(0, 0, 0, 0, h);
    const brow = (sx, rot, y = .1) => M(box(.08, .018, .015), '#B48560', sx * .1, y, z - .01, { p: f, r: [-.2, 0, sx * rot] });
    const lid = sx => M(new T.TorusGeometry(.032, .009, 3, 8, Math.PI), '#6B4529', sx * .1, .0, z + .005, { p: f, r: [0, 0, Math.PI] });
    const flat = (y, up, r = .13, arc = .75, col = '#9E3B24', dz = 0) => { const t = new T.TorusGeometry(r, .014, 3, 10, arc); const m = M(t, col, 0, up ? y + r : y - r, z - .004 + dz, { p: f }); m.rotation.set(-.28, 0, up ? -Math.PI / 2 - arc / 2 : Math.PI / 2 - arc / 2); };
    const eye = sx => { M(ball(.03, 1), '#4A2F1E', sx * .1, .0, z - .004, { p: f, s: [1, 1.15, .45] }); M(ball(.01, 0), '#FBF7EE', sx * .1 - .01, .014, z + .008, { p: f }); };
    const cheek = sx => M(ball(.05, 1), '#F08A6E', sx * .16, -.07, z - .03, { p: f, s: [1, .6, .3] });
    cheek(-1); cheek(1);
    if (ex === 'vui'){ brow(-1, -.2, .115); brow(1, -.2, .115); eye(-1); eye(1); M(new T.CircleGeometry(.07, 12, Math.PI, Math.PI), '#9E3B24', 0, -.095, z - .006, { p: f, r: [-.3, 0, 0] }); M(new T.CircleGeometry(.035, 10, Math.PI, Math.PI), '#F08A6E', 0, -.135, z - .009, { p: f, r: [-.3, 0, 0], s: [1.2, .6, 1] }); }
    if (ex === 'nhay'){ brow(-1, -.25, .125); brow(1, -.25, .125); eye(-1); eye(1); M(new T.CircleGeometry(.085, 14, Math.PI, Math.PI), '#9E3B24', 0, -.09, z - .006, { p: f, r: [-.3, 0, 0] }); M(new T.CircleGeometry(.045, 10, Math.PI, Math.PI), '#F08A6E', 0, -.14, z - .01, { p: f, r: [-.3, 0, 0], s: [1.2, .6, 1] }); }
    if (ex === 'lo'){ brow(-1, .35, .11); brow(1, .35, .11); lid(-1); lid(1); flat(-.115, false, .13, .62, '#9E3B24', .02); }
    if (ex === 'bat'){ brow(-1, -.05, .14); brow(1, -.05, .14); eye(-1); eye(1); M(new T.CircleGeometry(.045, 14), '#9E3B24', 0, -.12, z - .01, { p: f, r: [-.3, 0, 0] }); M(new T.TorusGeometry(.045, .01, 4, 14), '#6B4529', 0, -.12, z - .008, { p: f, r: [-.3, 0, 0] }); }
    if (ex === 'dan'){ brow(-1, .1); brow(1, -.25, .12); lid(-1); M(box(.06, .012, .012), '#6B4529', .1, .0, z, { p: f }); M(box(.11, .015, .012), '#9E3B24', 0, -.125, z - .018, { p: f, r: [-.3, 0, 0] }); } }
  const shot = (name, build, dir = new T.Vector3(.3, .18, 1)) => { const sc = new T.Scene(), root = new T.Group(); sc.add(root); const pr = ROOT; ROOT = root; build(root); ROOT = pr;
    sc.add(new T.HemisphereLight('#fff4e2', '#94a474', 1.6)); sc.add(new T.AmbientLight('#ffffff', .25)); const l = new T.DirectionalLight('#fff0d8', 1.6); l.position.set(-2, 5, 4); l.castShadow = true; sc.add(l);
    const gd = new T.Mesh(new T.CircleGeometry(.45, 20), new T.ShadowMaterial({ opacity: .18 })); gd.rotation.x = -Math.PI / 2; gd.receiveShadow = true; sc.add(gd); root.traverse(o => { if (o.isMesh) o.castShadow = true; });
    const c = new T.Vector3(0, .78, 0), sz = 1.0; const cm = new T.OrthographicCamera(-sz * 480 / 560, sz * 480 / 560, sz, -sz, .01, 100); cm.position.copy(c).add(dir.clone().normalize().multiplyScalar(20)); cm.lookAt(c);
    ri.render(sc, cm); OUT[name] = ri.domElement.toDataURL('image/png'); sc.traverse(o => o.geometry && o.geometry.dispose()); };
  shot('ng_side', g => { body(g); const h = head(g, HAIRS.non); face(h, 'vui'); }, new T.Vector3(1, .3, .8));
  shot('ex_vui', g => { const j = G(0, .07, 0, 0, g); j.rotation.z = -.1; body(j, false, { hop: true, arm: 1.25 }); const h = head(j, HAIRS.non); h.rotation.z = .08; face(h, 'vui'); });
  for (const e of ['lo', 'dan']) shot('ex_' + e, g => { body(g); const h = head(g, HAIRS.non); face(h, e); });
  shot('ex_bat', g => { body(g, false, { arm: 2.2 }); const h = head(g, HAIRS.non); h.rotation.x = .06; face(h, 'bat'); });
  shot('ex_nhay', g => { const j = G(0, .2, 0, 0, g); j.rotation.z = .08; body(j, true); const h = head(j, HAIRS.non); h.rotation.x = -.12; face(h, 'nhay'); sd = 99; for (let i = 0; i < 46; i++){ const a = rnd() * 6.28, r = R(.35, .75), y = R(.25, 1.75); const pc = M(rnd() < .5 ? box(.05, .012, .03) : new T.OctahedronGeometry(.03, 0), pick(['#EDB940', '#F08A6E', '#86B06A', '#6E95C4', '#E25A3B', '#FBF7EE']), Math.cos(a) * r, y, Math.sin(a) * r * .5 + .15, { p: g }); pc.rotation.set(R(0, 3), R(0, 3), R(0, 3)); } });
  ri.dispose(); ri.forceContextLoss(); return OUT; };
