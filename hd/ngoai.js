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
