# NHÁP v149: 3 mẫu nữ nhìn ra con gái từ phía trước (người chơi báo "không thấy con gái").
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v148'", "BUILD = 'v149'")
rep("{ id: 'moc', name: 'Mộc', hair: 'bob',", "{ id: 'moc', name: 'Mộc', girl: true, hair: 'bob',")
rep("{ id: 'nang', name: 'Nắng', hair: 'pony',", "{ id: 'nang', name: 'Nắng', girl: true, hair: 'pony',")
rep("{ id: 'lanh', name: 'Lành', hair: 'bun',", "{ id: 'lanh', name: 'Lành', girl: true, hair: 'bun',")
# lông mi
rep("M(box(.07, .016, .012), HR, sx * .1, .095, z - .012, { p: h, r: [-.2, 0, sx * -.12] }); }",
    "M(box(.07, .016, .012), HR, sx * .1, .095, z - .012, { p: h, r: [-.2, 0, sx * -.12] }); if (a.girl) for (const [dx, dy, rz] of [[.036, .03, .75], [.046, .012, .35]]) M(box(.034, .011, .01), '#2A2320', sx * (.1 + dx), dy, z - .016 - dx * .25, { p: h, r: [0, 0, sx * rz], cast: false }); }")
# Nắng: hai bím thả trước vai
A = s[s.index("  if (a.hair === 'pony'){"):s.index("  if (a.hair === 'bun'){")]
rep(A, "  if (a.hair === 'pony'){ bang(5); for (const sx of [-1, 1]){ M(ball(.11, 1), HR, sx * .27, -.04, -.02, { p: h, s: [.6, 1.3, .95] }); for (let k = 0; k < 4; k++) M(ball(.07 - k * .006, 1), HR, sx * (.27 - k * .012), -.2 - k * .085, .04 + k * .035, { p: h, s: [1, 1.05, 1] }); M(new T.TorusGeometry(.04, .016, 4, 10), '#C8452E', sx * .222, -.5, .175, { p: h, r: [Math.PI / 2, 0, 0], cast: false }); M(ball(.045, 1), HR, sx * .22, -.55, .185, { p: h, s: [.9, 1.3, .9] }); } }\n")
# Lành: búi cao + tóc mai dài + kẹp bông
B = s[s.index("  if (a.hair === 'bun'){"):s.index("  if (a.hair === 'spiky'){")]
rep(B, "  if (a.hair === 'bun'){ bang(4); for (const sx of [-1, 1]) M(ball(.1, 1), HR, sx * .265, -.1, .0, { p: h, s: [.55, 2.1, .9] }); if (!(o.hatOn || a.hat)){ M(ball(.15, 1), HR, 0, .34, -.1, { p: h, s: [1.1, .9, 1.1] }); M(new T.TorusGeometry(.1, .018, 4, 12), '#C8452E', 0, .25, -.09, { p: h, r: [Math.PI / 2 - .25, 0, 0], cast: false }); for (let k = 0; k < 5; k++) M(ball(.028, 0), '#F6D34A', .2 + Math.cos(k * 1.257) * .034, .15 + Math.sin(k * 1.257) * .034, .225, { p: h, cast: false }); M(ball(.02, 0), '#E8695A', .2, .15, .24, { p: h, cast: false }); } }\n")
# Ba tóc nam khác hẳn nhau: Gió chỉa dựng hở trán, Sông rẽ ngôi 7/3 mái xéo, Đất xoăn bồng to
C = s[s.index("  if (a.hair === 'spiky'){"):s.index("  return h; }\nawait LDY(0);")]
rep(C, """  const noHat = !(o.hatOn || a.hat);
  if (a.hair === 'spiky'){ for (let k = 0; k < 6; k++){ const c = M(cone(.06, .12, 5), HR, -.2 + k * .08, .2, .2 - Math.abs(k - 2.5) * .03, { p: h }); c.rotation.set(.9, 0, (2.5 - k) * .12); } if (noHat) for (let k = 0; k < 9; k++){ const an = k / 9 * 6.28, r = k % 2 ? .19 : .09; const c = M(cone(.095, .3 - (k % 3) * .04, 5), HR, Math.cos(an) * r, .33, Math.sin(an) * r + .02, { p: h }); c.rotation.set(Math.sin(an) * .45 + .25, 0, -Math.cos(an) * .45); } }
  if (a.hair === 'sweep'){ bang(4); for (const sx of [-1, 1]) M(ball(.06, 1), HR, sx * .285, .05, .07, { p: h, s: [.5, 1.1, .8] }); if (noHat){ const cv = new T.CatmullRomCurve3([[-.2, .27, .13], [-.02, .36, .14], [.16, .35, .08], [.28, .29, 0], [.36, .26, -.08], [.4, .32, -.13], [.36, .38, -.15]].map(q => new T.Vector3(...q))); for (let k = 0; k <= 14; k++){ const t = k / 14, q = cv.getPoint(t); M(ball(.12 - t * .05, 1), HR, q.x, q.y, q.z, { p: h, s: [1, .85, 1] }); } } }
  if (a.hair === 'curly'){ if (noHat) for (let k = 0; k < 30; k++){ const an = k * 2.4, el = .1 + (k % 5) * .26, r = .325; M(ico(.095, 0), HR, Math.cos(an) * Math.cos(el) * r, Math.sin(el) * r + .07, Math.sin(an) * Math.cos(el) * r - .04, { p: h }); } for (const sx of [-1, 1]) M(ico(.09, 0), HR, sx * .29, .04, .0, { p: h }); for (let k = 0; k < 5; k++) M(ico(.085, 0), HR, -.2 + k * .1, .19 + (k % 2) * .03, .24 - Math.abs(k - 2) * .02, { p: h }); }
""")
# ảnh mặt tròn: lùi khung một chút để tóc (búi Lành, chỏm Gió, sóng Sông) không bị cắt
rep("const c = kind === 'full' ? new T.Vector3(0, .62, 0) : new T.Vector3(0, .92, 0), sz = kind === 'full' ? .78 : .42,", "const c = kind === 'full' ? new T.Vector3(0, .64, 0) : new T.Vector3(.03, .97, 0), sz = kind === 'full' ? .8 : .49,")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
