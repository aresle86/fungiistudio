#!/usr/bin/env python3
"""v101: ghe bẹo chợ nổi dựng lại trên vỏ ghe tam bản đã duyệt (mắt ghe, sơn mũi), lớn hơn: mui lá phía lái, cây bẹo tre ở mũi treo khóm, bí đỏ, chùm khoai lang
(cách ghe bẹo rao hàng), khoang chất thúng bí đỏ, dừa, khóm, xoài. Icon bong bóng là chính chiếc ghe bẹo."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
old_start = "const GHEV = (() => { const root = DYN(G(bx + 3.4, WLR + .06, R0 + 1.25, -.08)), pr = ROOT; ROOT = root;"
i = s.index(old_start); j = s.index("return { root, hit, ...mkBub() }; })();", i) + len("return { root, hit, ...mkBub() }; })();")
s = s[:i] + r"""function gheBeo(){ const g = gheTB(false), pr = ROOT; ROOT = g; g.scale.setScalar(1.12);   /* ghe bẹo: vỏ ghe tam bản, mui lá ở lái, cây bẹo ở mũi, khoang chở hàng */
  const MS = c => new T.MeshStandardMaterial({ color: c, flatShading: true, roughness: .9, side: T.DoubleSide }), MUI = MS('#C9AE52'), MUI2 = MS('#B89A44'), DAY = MS('#8A6A3A'), BAM = MS('#B9A45A'), TH = MS('#A88A52');
  const BI = MS('#E07A2E'), BI2 = MS('#C9651F'), DUA = MS('#6E9F3A'), KHOM = MS('#D9A23A'), KHOMV = MS('#4E8A34'), XOAI = MS('#F2C230'), KL = MS('#8E4A7A'), CUONG = MS('#5E7A2E');
  /* mui lá dừa nước phía lái */
  const mx0 = -.64, mx1 = -.2, Lm = 1, Wm = .27, wU = u => Wm * Math.pow(Math.max(0, 1 - Math.pow(Math.abs(u), 2.4)), .55), ytU = u => .16 + (u > 0 ? .26 : .18) * Math.pow(Math.abs(u), 3);   /* cùng công thức vỏ ghe tam bản */
  const muiGeo = (u0, u1, dr) => { const NU = 14, NT = 16, pos = [], idx = []; for (let i = 0; i <= NU; i++){ const u = u0 + (u1 - u0) * i / NU, rr = wU(u) - .028 + dr, y0 = ytU(u) + .002; for (let j = 0; j <= NT; j++){ const th = Math.PI * j / NT; pos.push(u * Lm, y0 + Math.sin(th) * rr * .92, Math.cos(th) * rr); } }
    for (let i = 0; i < NU; i++) for (let j = 0; j < NT; j++){ const a2 = i * (NT + 1) + j, b2 = a2 + NT + 1; idx.push(a2, b2, a2 + 1, a2 + 1, b2, b2 + 1); } const ge = new T.BufferGeometry(); ge.setAttribute('position', new T.Float32BufferAttribute(pos, 3)); ge.setIndex(idx); ge.computeVertexNormals(); return ge; };
  M(muiGeo(mx0, mx1, 0), MUI, 0, 0, 0, { ds: true });   /* mui đặt lọt trong mép be: mỗi lát mui rộng theo lòng ghe chỗ đó, mép mui tựa lên be từ phía trong, không lòi ra mạn */
  M(muiGeo(mx0, mx0 + (mx1 - mx0) * .42, .006), MUI2, 0, 0, 0, { ds: true });
  for (let k = 0; k <= 3; k++){ const u = mx0 + (mx1 - mx0) * k / 3, rr = wU(u) - .03, y0 = ytU(u) + .002, pts = []; for (let j = 0; j <= 12; j++){ const th = Math.PI * j / 12; pts.push(new T.Vector3(u * Lm, y0 + Math.sin(th) * rr * .92, Math.cos(th) * rr)); } M(new T.TubeGeometry(new T.CatmullRomCurve3(pts), 16, .008, 3), DAY, 0, 0, 0, { cast: false }); }
  /* khóm: trái vàng sần + chùm lá nhọn */
  const khom = (p, x, y, z, s2 = 1, rz = 0) => { const o = G(x, y, z, 0, p); o.rotation.z = rz; o.scale.setScalar(s2); M(new T.IcosahedronGeometry(.05, 0), KHOM, 0, 0, 0, { p: o, s: [1, 1.4, 1] }); for (let k = 0; k < 5; k++) M(cone(.014, .07, 3), KHOMV, Math.cos(k * 1.26) * .012, .08, Math.sin(k * 1.26) * .012, { p: o, r: [Math.sin(k * 1.26) * .45, 0, -Math.cos(k * 1.26) * .45], cast: false }); return o; };
  const bi = (p, x, y, z, s2 = 1) => { const o = G(x, y, z, 0, p); o.scale.setScalar(s2); M(sph(.07, 10, 6), BI, 0, 0, 0, { p: o, s: [1, .72, 1] }); for (let k = 0; k < 6; k++) M(box(.008, .095, .02), BI2, Math.cos(k * 1.05) * .066, 0, Math.sin(k * 1.05) * .066, { p: o, r: [0, -k * 1.05, 0], s: [1, .72, 1], cast: false }); M(cyl(.008, .01, .03, 4), CUONG, 0, .055, 0, { p: o, cast: false }); return o; };
  /* cây bẹo tre dựng ở mũi, treo hàng mẫu cho khách thấy từ xa */
  const px = .6, py0 = .1, ph = 1.15; M(cyl(.016, .02, ph, 6), BAM, px, py0 + ph / 2, 0); for (let k = 1; k < 6; k++) M(cyl(.021, .021, .012, 6), MS('#8E7A3A'), px, py0 + k * ph / 6, 0, { cast: false });
  const hang = (y, z, build) => { const top = py0 + ph - .02; M(cyl(.004, .004, top - y, 3), DAY, px, (top + y) / 2, z, { cast: false }); build(px, y - .05, z); };
  M(box(.012, .012, .26), BAM, px, py0 + ph - .02, 0, { cast: false });
  hang(py0 + ph - .26, -.11, (x, y, z) => khom(g, x, y, z, 1.1, Math.PI));
  hang(py0 + ph - .34, .11, (x, y, z) => bi(g, x, y, z, .85));
  hang(py0 + ph - .5, 0, (x, y, z) => { for (let k = 0; k < 4; k++) M(new T.CapsuleGeometry(.018, .05, 2, 5), KL, x + (k - 1.5) * .022, y - (k % 2) * .02, z + (k % 2 ? .015 : -.015), { r: [0, 0, (k - 1.5) * .2], cast: false }); });
  /* khoang chở hàng: thúng bí đỏ, dừa, khóm, xoài */
  const thung = (x, z, fill) => { const t = G(x, .1, z, 0, g); M(new T.CylinderGeometry(.11, .08, .08, 12, 1, true), TH, 0, .04, 0, { p: t, ds: true }); M(new T.TorusGeometry(.11, .008, 3, 12), DAY, 0, .08, 0, { p: t, r: [Math.PI / 2, 0, 0], cast: false }); fill(t); };
  thung(-.04, -.07, t => { bi(t, -.03, .1, 0, .8); bi(t, .04, .11, .03, .7); });
  thung(.14, .07, t => { for (const [x, z] of [[-.03, -.02], [.03, .02], [0, .03]]) M(sph(.045, 8, 6), DUA, x, .1, z, { p: t, s: [1, .9, 1] }); });
  thung(.32, -.06, t => { for (const [x, z, r] of [[-.03, 0, .2], [.03, .02, -.25]]) khom(t, x, .12, z, .9, r); });
  for (const [x, z] of [[-.08, .08], [-.03, .1], [-.06, .12]]) M(sph(.032, 7, 5), XOAI, x, .14, z, { s: [1.3, 1, 1], cast: false });
  bi(g, .42, .16, .1, .8);
  ROOT = pr; return g; }
const GHEV = (() => { const root = DYN(G(bx + 3.4, WLR + .1, R0 + 1.25, -.08)), pr = ROOT; ROOT = root; const ps = sd, nL = LIGHTS.length; root.add(gheBeo()); sd = ps; LIGHTS.length = nL; ROOT = pr;
  const hit = new T.Mesh(new T.BoxGeometry(2.3, 1.4, .8), new T.MeshBasicMaterial({ visible: false })); root.add(hit); hit.position.set(0, .45, 0); return { root, hit, ...mkBub() }; })();""" + s[j:]
rep("GHEV.root.position.y = WLR + .06 + Math.sin(t * 1.4) * .012;", "GHEV.root.position.y = WLR + .1 + Math.sin(t * 1.4) * .012;")
rep("b.position.set(bx + 3.4, 1.0 + Math.sin(t * 2) * .035, R0 + 1.25);", "b.position.set(bx + 3.2, 1.0 + Math.sin(t * 2) * .035, R0 + 1.25);")
# icon ghe bẹo dựng từ mô hình thật, cùng chỗ dựng icon ghe tam bản
rep("UIC.tamban = toonURL(); }", """UIC.tamban = toonURL(); }
  { const ps = sd, nL = LIGHTS.length, sc = new T.Scene(), m = gheBeo(); sd = ps; LIGHTS.length = nL; sc.add(m); sc.add(new T.HemisphereLight('#fff6e6', '#9aaa78', 1.9)); const l = new T.DirectionalLight('#fff0d0', 1.9); l.position.set(-2, 6, 3); sc.add(l);   /* icon ghe bẹo: chính chiếc ghe, thấy cây bẹo treo hàng */
    const bb = new T.Box3().setFromObject(m), c = bb.getCenter(new T.Vector3()), sz = bb.getSize(new T.Vector3()).length() * .44; const cm = new T.OrthographicCamera(-sz, sz, sz, -sz, .01, 100); cm.position.copy(c).add(new T.Vector3(.55, .55, 1).normalize().multiplyScalar(20)); cm.lookAt(c); toonRender(ri, sc, cm); ICON.ghe = toonURL(); }""")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
