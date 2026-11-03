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
window.__ngoai = () => { const OUT = {}; const ri = new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true }); ri.setPixelRatio(1); ri.setSize(420, 420); ri.setClearColor(0, 0); ri.toneMapping = T.ACESFilmicToneMapping; ri.toneMappingExposure = 1.02;
  const SK = '#E3BC97', SKD = '#D2A57E', HAIR = '#E8DFCC', HAIRL = '#FBF7EE', SHIRT = '#8A5D3B', SHIRTD = '#6B4529';
  function face(g, ex){ // mặt vuông, không thấy mắt: mắt khép thành vệt mí mỏng hoặc ẩn; biểu cảm bằng chân mày + miệng + má
    const z = .243;
    const brow = (sx, rot, y = .9) => M(box(.1, .022, .012), '#B48560', sx * .12, y, z, { p: g, r: [0, 0, sx * rot] });
    const lid = (sx, curve) => { const t = new T.TorusGeometry(.035, .008, 3, 8, Math.PI); const m = M(t, '#8A5D3B', sx * .12, .8, z, { p: g }); m.rotation.z = curve > 0 ? Math.PI : 0; };
    const cheek = sx => M(box(.09, .05, .01), '#F08A6E', sx * .16, .73, z - .002, { p: g });
    if (ex === 'vui'){ brow(-1, -.15); brow(1, -.15); lid(-1, 1); lid(1, 1); cheek(-1); cheek(1); const m = new T.TorusGeometry(.06, .014, 3, 10, Math.PI); M(m, '#9E3B24', 0, .69, z, { p: g, r: [0, 0, Math.PI] }); }
    if (ex === 'lo'){ brow(-1, .32, .91); brow(1, .32, .91); cheek(-1); cheek(1); M(box(.1, .018, .01), '#9E3B24', 0, .66, z, { p: g, r: [0, 0, .12] }); M(box(.05, .016, .01), '#9E3B24', .06, .675, z, { p: g, r: [0, 0, -.3] }); }
    if (ex === 'bat'){ brow(-1, -.05, .95); brow(1, -.05, .95); cheek(-1); cheek(1); M(new T.TorusGeometry(.035, .014, 4, 10), '#9E3B24', 0, .67, z, { p: g }); }
    if (ex === 'dan'){ brow(-1, .1); brow(1, -.25); lid(-1, 1); cheek(-1); cheek(1); M(box(.11, .018, .01), '#9E3B24', 0, .675, z, { p: g }); M(box(.03, .1, .02), SK, .33, .6, .12, { p: g, r: [0, 0, -.25] }); }
  }
  function body(g){ // áo bà ba nâu, khăn rằn
    M(box(.92, .42, .56), SHIRT, 0, .21, 0, { p: g }); for (const y of [.08, .2, .32]) M(sph(.018, 6, 4), '#E8DFCC', 0, y, .285, { p: g }); M(box(.02, .42, .012), SHIRTD, 0, .21, .283, { p: g });
    M(box(.18, .1, .18), SK, 0, .46, 0, { p: g }); M(box(.94, .1, .58), SHIRTD, 0, .4, 0, { p: g });
    for (let k = 0; k < 7; k++) M(box(.14, .09, .6), k % 2 ? '#2B3446' : '#FBF7EE', -.42 + k * .14, .47, 0, { p: g });
    M(box(.12, .32, .06), '#2B3446', .32, .28, .3, { p: g }); for (let k = 0; k < 4; k++) M(box(.12, .02, .062), '#FBF7EE', .32, .16 + k * .07, .3, { p: g }); }
  function head(g){ M(box(.5, .52, .46), SK, 0, .78, 0, { p: g }); M(box(.06, .1, .06), SKD, -.27, .78, 0, { p: g }); M(box(.06, .1, .06), SKD, .27, .78, 0, { p: g }); M(box(.06, .05, .03), SKD, 0, .74, .245, { p: g }); }
  const HAIRS = {
    non(g){ M(box(.52, .1, .48), HAIR, 0, 1.01, -.01, { p: g }); for (const sx of [-1, 1]) M(box(.04, .26, .4), HAIR, sx * .26, .92, -.03, { p: g }); M(ico(.12, 1), HAIRL, 0, .98, -.3, { p: g });
      const n = M(new T.ConeGeometry(.7, .34, 14), '#E3BC97', 0, 1.2, 0, { p: g }); for (let k = 0; k < 5; k++) M(new T.TorusGeometry(.12 + k * .12, .006, 3, 14), '#C9952A', 0, 1.34 - k * .066, 0, { p: g, r: [Math.PI / 2, 0, 0] });
      for (const sx of [-1, 1]) M(box(.012, .32, .012), '#9E3B24', sx * .22, .9, .2, { p: g, r: [0, 0, sx * .15] }); M(box(.42, .012, .012), '#9E3B24', 0, .65, .24, { p: g }); },
    khan(g){ M(box(.52, .1, .48), HAIR, 0, 1.01, -.01, { p: g }); for (const sx of [-1, 1]) M(box(.04, .24, .4), HAIR, sx * .26, .93, -.03, { p: g });
      for (let k = 0; k < 6; k++) M(box(.56, .06, .52), k % 2 ? '#2B3446' : '#FBF7EE', 0, 1.0 + k * .03, -.01, { p: g, s: [1 - k * .07, 1, 1 - k * .07] }); M(box(.16, .12, .1), '#2B3446', .2, 1.06, .26, { p: g, r: [0, 0, .5] }); },
    tran(g){ M(ico(.33, 1), HAIR, 0, 1.02, -.04, { p: g, s: [.88, .5, .82] }); M(box(.54, .14, .1), HAIR, 0, 1.02, .18, { p: g }); for (const sx of [-1, 1]) M(box(.05, .3, .42), HAIR, sx * .265, .93, -.02, { p: g }); M(ico(.15, 1), HAIRL, 0, 1.1, -.32, { p: g }); M(box(.05, .015, .24), '#C9952A', .05, 1.12, -.3, { p: g, r: [0, .5, .6] }); } };
  const shot = (name, build, dir = new T.Vector3(.35, .22, 1)) => { const sc = new T.Scene(), root = new T.Group(); sc.add(root); const pr = ROOT; ROOT = root; build(root); ROOT = pr;
    sc.add(new T.HemisphereLight('#fff4e2', '#94a474', 1.7)); sc.add(new T.AmbientLight('#ffffff', .25)); const l = new T.DirectionalLight('#fff0d8', 1.6); l.position.set(-2, 5, 4); sc.add(l);
    const bb = new T.Box3().setFromObject(root), c = bb.getCenter(new T.Vector3()), sz = Math.max(.82, bb.getSize(new T.Vector3()).length() * .44); const cm = new T.OrthographicCamera(-sz, sz, sz, -sz, .01, 100); cm.position.copy(c).add(dir.clone().normalize().multiplyScalar(20)); cm.lookAt(c);
    ri.render(sc, cm); OUT[name] = ri.domElement.toDataURL('image/png'); sc.traverse(o => o.geometry && o.geometry.dispose()); };
  for (const h of ['non', 'khan', 'tran']) shot('ng_' + h, g => { body(g); head(g); HAIRS[h](g); face(g, 'vui'); });
  for (const e of ['vui', 'lo', 'bat', 'dan']) shot('ex_' + e, g => { body(g); head(g); HAIRS.tran(g); face(g, e); });
  ri.dispose(); ri.forceContextLoss(); return OUT; };
