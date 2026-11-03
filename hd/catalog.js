window.__catalog = () => { const OUT = {}; const ri = new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true }); ri.setPixelRatio(1); ri.setSize(360, 300); ri.setClearColor(0, 0); ri.toneMapping = T.ACESFilmicToneMapping; ri.toneMappingExposure = 1.0; ri.shadowMap.enabled = true; ri.shadowMap.type = T.PCFSoftShadowMap;
  const B = [-.62, -.42, .62, .42];
  const lights = sc => { sc.add(new T.HemisphereLight('#fff4e2', '#94a474', 1.55)); sc.add(new T.AmbientLight('#ffffff', .2)); const l = new T.DirectionalLight('#fff0d8', 1.5); l.position.set(-3, 9, 2); l.castShadow = true; l.shadow.mapSize.set(1024, 1024); Object.assign(l.shadow.camera, { left: -2, right: 2, top: 2, bottom: -2, near: .5, far: 30 }); l.shadow.bias = -.0005; l.shadow.normalBias = .02; sc.add(l); };
  const base = (root, o = {}) => { const pr = ROOT; ROOT = root; const [u0, v0, u1, v1] = B, w = u1 - u0, l = v1 - v0;
    M(box(w + .24, .02, l + .24), '#86B06A', 0, -.03, 0, { cast: false });
    if (o.water){ const wm = new T.Mesh(new T.BoxGeometry(.8, .01, 1.5), new T.MeshStandardMaterial({ color: '#5A93A0', roughness: .3, flatShading: true })); wm.position.y = -.015; root.add(wm); ROOT = pr; return; }
    M(box(w, .07, l), C.soil, 0, 0, 0); const m = Math.min(1, (o.moist ?? .5) * 1.6), col = SOILC.dry.clone().lerp(SOILC.mid, Math.min(1, m * 2)).lerp(SOILC.wet, Math.max(0, m * 2 - 1) * .7).lerp(SOILC.tired, Math.max(0, (.5 - (o.soil ?? .85)) * 1.6));
    const sm = new T.Mesh(new T.BoxGeometry(w - .03, .006, l - .03), new T.MeshStandardMaterial({ color: col, flatShading: true, roughness: .95 })); sm.position.y = Y + .002; sm.receiveShadow = true; root.add(sm);
    if (o.furrow) for (let k = 1; k < 5; k++) M(box(w - .1, .014, .05), '#9E6A42', 0, Y + .008, v0 + l * k / 5, { cast: false });
    if (o.cracks) for (let k = 0; k < 7; k++) M(box(R(.12, .3), .004, .012), '#6B4529', R(u0 + .15, u1 - .15), Y + .008, R(v0 + .1, v1 - .1), { r: [0, R(0, 3.14), 0], cast: false });
    if (o.mulch) for (let i = 0; i < w * l * 90 * o.mulch; i++) M(box(R(.1, .2), .012, .018), o.old ? pick(['#C9952A', '#B48560', '#8A5D3B']) : pick(['#C9952A', '#B48560', '#B8913E']), R(u0 + .04, u1 - .04), Y + .009, R(v0 + .04, v1 - .04), { r: [R(-.1, .1), R(0, 3.14), 0], cast: false });
    if (o.shine) for (let k = 0; k < 6; k++){ const pd = new T.Mesh(new T.CylinderGeometry(R(.05, .1), R(.05, .1), .003, 7), new T.MeshStandardMaterial({ color: '#6E95C4', roughness: .15, flatShading: true })); pd.position.set(R(u0 + .15, u1 - .15), Y + .008, R(v0 + .1, v1 - .1)); root.add(pd); }
    ROOT = pr; };
  const cams = {};
  const render = (name, sc, frameKey) => { let cm = cams[frameKey]; if (!cm){ const bb = new T.Box3().setFromObject(sc), c = bb.getCenter(new T.Vector3()); const sz = Math.max(.62, bb.getSize(new T.Vector3()).length() * .36); cm = new T.OrthographicCamera(-sz * 1.2, sz * 1.2, sz, -sz, .01, 100); cm.position.copy(c).add(new T.Vector3(1, .816, 1).normalize().multiplyScalar(20)); cm.lookAt(c); cams[frameKey] = cm; }
    ri.render(sc, cm); OUT[name] = ri.domElement.toDataURL('image/png'); sc.traverse(o => o.geometry && o.geometry.dispose()); };
  const cropScene = (k, st, cond) => { const sc = new T.Scene(), root = new T.Group(); sc.add(root); lights(sc); const tr = CROPS[k].kind === 'trellis';
    base(root, tr ? { water: true } : { moist: cond === 'ok' ? .6 : 0, cracks: cond !== 'ok', furrow: st === 0, mulch: (k === 'ot' || k === 'cachua') ? 1 : 0 });
    const tmp = new T.Group(); root.add(tmp); const pr = ROOT; ROOT = tmp; TINT = cond === 'ok' ? null : makeTint(cond); sd = 4242 + k.length * 17;
    if (tr){ TINT = null; gianFrame(-.32, -.62, .32, .62); TINT = cond === 'ok' ? null : makeTint(cond); gianGrow(-.32, -.62, .32, .62, st); }
    else sway(0, () => CB[k](B, st));
    ROOT = pr; TINT = null;
    if (cond !== 'ok') for (const ch of tmp.children){ if (ch.isMesh) continue; ch.scale.y *= cond === 'dead' ? .55 : .82; ch.rotation.z += R(-.25, .25); ch.rotation.x += R(-.15, .15); }
    sc.traverse(o => { if (o.isMesh){ o.castShadow = true; o.receiveShadow = true; } }); return sc; };
  for (const k of Object.keys(CROPS)){ render(k + '_4', cropScene(k, 4, 'ok'), k); for (const st of [0, 1, 2, 3]) render(k + '_' + st, cropScene(k, st, 'ok'), k); render(k + '_wilt', cropScene(k, 4, 'wilt'), k); render(k + '_dead', cropScene(k, 4, 'dead'), k); }
  const soils = { cuoc: { moist: .45, furrow: true }, kho: { moist: 0, cracks: true }, am: { moist: .45 }, uot: { moist: 1, shine: true }, met: { moist: .45, soil: .2, cracks: true }, rom: { moist: .6, mulch: 1 }, romcu: { moist: .5, mulch: .45, old: true } };
  for (const [k, o] of Object.entries(soils)){ const sc = new T.Scene(), root = new T.Group(); sc.add(root); lights(sc); base(root, o); sc.traverse(x => { if (x.isMesh) x.receiveShadow = true; }); render('soil_' + k, sc, 'soil'); }
  ri.dispose(); ri.forceContextLoss(); return OUT; };
