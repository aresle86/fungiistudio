p='live/vuon3d.html'; s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,a[:90]; s=s.replace(a,b)
# 1. awning out of static house, into roofState (matches roof colors)
rep("  { const aw = G(0, fy + .9, d / 2 + .02, 0, g); aw.rotation.x = .32; for (let r = 0; r < 3; r++) for (let c = 0; c < 16; c++){ const jag = R(-.02, .03); M(box(.2, .04, .3 + jag), pick([C.thatch, C.thatchD, '#D9B48A']), -1.55 + c * .207, -r * .012, .14 + r * .23 + jag / 2, { p: aw }); } }", "")
rep("  const ridge = st === 0 ? OLD[1] : NEW[1];", "  { const aw = new T.Group(); aw.position.set(0, 0, d / 2 + .02); aw.rotation.x = .32; g.add(aw); for (let r = 0; r < 3; r++) for (let c = 0; c < 16; c++){ const x = -1.55 + c * .207, jag = st === 2 ? R(-.005, .01) : R(-.02, .03), pal = st === 0 || (st === 1 && x > -.1) ? OLD : NEW; if (st === 0 && rnd() < .05) continue; M(box(.2, st === 2 ? .05 : .04, .3 + jag), st === 0 && rnd() < .08 ? MOSS : pal[rnd() < .35 ? 2 + (c % 2) : r % 2], x, -r * .012, .14 + r * .23 + jag / 2, { p: aw }); } }   // mái hiên cùng màu mái chính\n  const ridge = st === 0 ? OLD[1] : NEW[1];")
# 2. richer houseUp with bougainvillea growth stage
i=s.index("function houseUp(){"); j=s.index("function scaffold(s = 1){")
s=s[:i]+r'''function houseUp(bg = 3){ const g = new T.Group(), pr = ROOT; ROOT = g; const fy = .2, d = 1.8, w = 2.8;   /* sửa nhà cấp 18; bg = giàn bông giấy lớn dần 1→3 */
  const MS = c => new T.MeshStandardMaterial({ color: c, flatShading: true, roughness: .9 }), GT = [MS('#C0643C'), MS('#B4583A'), MS('#CA7048')], GROUT = MS('#D9C3A0'), BRK = MS('#9C4A2E'), RED = MS('#B8402E'), GOLD = MS('#E0B040'), XANH = MS('#4E8C74'), XANH2 = MS('#3E7460'), WOODN = MS('#C79A62');
  // sân gạch tàu có viền gạch thẻ
  M(box(.78, .012, .34), GROUT, 0, .006, d / 2 + 1.02, { cast: false }); for (let i = 0; i < 5; i++) for (let j = 0; j < 2; j++) M(box(.135, .02, .135), GT[(i * 3 + j) % 3], -.286 + i * .143, .014, d / 2 + .95 + j * .145, { cast: false });
  for (const sx of [-1, 1]) M(box(.035, .03, .34), BRK, sx * .4, .015, d / 2 + 1.02); M(box(.83, .03, .035), BRK, 0, .015, d / 2 + 1.2);
  // vách trước sửa mới: nẹp ván vàng mật, khung cửa sổ sơn xanh, câu đối đỏ hai bên cửa, liễn chữ trên cửa
  for (let k = 0; k < 18; k++) M(box(.022, .86, .008), k % 3 ? WOODN : MS('#D6AC72'), -w / 2 + .08 + k * (w - .16) / 17, fy + .45, d / 2 + .014, { cast: false });
  for (const x of [-.92, .92]){ for (const [bx2, by, bw, bh] of [[0, .19, .56, .05], [0, -.19, .58, .05], [-.26, 0, .05, .4], [.26, 0, .05, .4]]) M(box(bw, bh, .02), XANH, x + bx2, fy + .55 + by, d / 2 + .05); M(box(.6, .02, .1), XANH2, x, fy + .33, d / 2 + .09); }
  for (const sx of [-1, 1]){ M(box(.09, .5, .012), RED, sx * .47, fy + .42, d / 2 + .045); for (let k = 0; k < 4; k++) M(box(.04, .04, .004), GOLD, sx * .47, fy + .6 - k * .12, d / 2 + .053, { cast: false }); }
  M(box(.56, .1, .012), RED, 0, fy + .83, d / 2 + .05); for (let k = 0; k < 4; k++) M(box(.06, .05, .004), GOLD, -.18 + k * .12, fy + .83, d / 2 + .058, { cast: false });
  for (const x of [-.75, .55]){ M(cyl(.003, .003, .1, 3), C.ink, x, fy + .83, d / 2 + .5); const ln = G(x, fy + .7, d / 2 + .5, 0, g); M(sph(.07, 8, 6), RED, 0, 0, 0, { p: ln, s: [1, 1.15, 1] }); for (const y of [.075, -.075]) M(cyl(.035, .035, .015, 8), GOLD, 0, y, 0, { p: ln }); M(cyl(.003, .003, .06, 3), GOLD, 0, -.11, 0, { p: ln }); }   // hai lồng đèn đỏ
  // bàn thờ ông Thiên: đế, trụ vuông, khay, miếu mái ngói đỏ, lư hương, nhang, bình bông vạn thọ, dĩa trái cây, đèn dầu
  const bt = G(1.75, 0, d / 2 + 1.0, -.2, g); M(box(.16, .05, .16), MS('#B8B2A4'), 0, .025, 0, { p: bt }); M(box(.06, .9, .06), RED, 0, .5, 0, { p: bt }); M(box(.3, .03, .24), WOODN, 0, .96, 0, { p: bt }); for (const [x, z] of [[-.13, -.1], [.13, -.1], [-.13, .1], [.13, .1]]) M(box(.02, .02, .02), GOLD, x, .985, z, { p: bt, cast: false });
  M(box(.2, .15, .14), RED, 0, 1.05, -.03, { p: bt }); M(box(.12, .1, .01), MS('#3A1E14'), 0, 1.04, .042, { p: bt, cast: false }); M(box(.1, .02, .005), GOLD, 0, 1.11, .042, { p: bt, cast: false });
  for (const sg of [-1, 1]){ const m = M(box(.3, .02, .14), MS('#A8462E'), 0, 1.16, -.03 + sg * .05, { p: bt }); m.rotation.x = sg * .55; } M(cyl(.012, .012, .3, 5), GOLD, 0, 1.2, -.03, { p: bt, r: [0, 0, Math.PI / 2] }); for (const sx of [-1, 1]) M(cone(.012, .05, 4), GOLD, sx * .15, 1.22, -.03, { p: bt, r: [0, 0, -sx * .9] });
  M(cyl(.03, .025, .035, 8), GOLD, 0, .995, .07, { p: bt }); for (const x of [-.012, 0, .012]){ M(cyl(.002, .002, .08, 3), MS('#7A2A1A'), x, 1.05, .07, { p: bt, cast: false }); M(sph(.004, 4, 3), MS('#FF6A2A'), x, 1.09, .07, { p: bt, cast: false }); }
  M(cyl(.016, .012, .05, 6), MS('#F4F0E4'), .1, 1.0, .06, { p: bt }); for (let k = 0; k < 5; k++) M(ico(.016, 0), MS('#F29A1E'), .1 + Math.cos(k * 1.3) * .015, 1.04 + (k % 2) * .01, .06 + Math.sin(k * 1.3) * .015, { p: bt, cast: false });
  M(cyl(.035, .03, .01, 8), MS('#F4F0E4'), -.09, .98, .06, { p: bt }); for (const [x, z, c] of [[-.1, .06, '#F2C230'], [-.08, .07, '#86B06A'], [-.09, .05, '#E8453A']]) M(sph(.014, 6, 4), MS(c), x, .995, z, { p: bt, cast: false });
  // giàn bông giấy: dây leo cột, lan theo mép mái hiên, lớn dần theo bg
  const BG = [MS('#E0457E'), MS('#D23A72'), MS('#EE6A98'), MS('#F07AA6')], LF = MS('#4F8A3A'), LF2 = MS('#6FA84E'), N = [0, 22, 46, 80][bg], X1 = [-1.5, -1.25, -.75, -.15][bg];
  M(cyl(.03, .04, .9, 5), '#6B4529', -1.62, .45, d / 2 + .66, { r: [0, 0, .08] }); for (let k = 0; k < 3 + bg; k++) M(cyl(.008, .01, .4, 4), '#6B4529', -1.6 + k * .02, .3 + k * .12, d / 2 + .68, { r: [R(-.5, .5), 0, R(-.6, .6)], cast: false });
  for (let k = 0; k < N; k++){ const t = k / N, x = -1.68 + t * (X1 + 1.68) + R(-.06, .06), y = fy + .76 + Math.sin(t * 3.1) * .07 + R(-.05, .1), z = d / 2 + .6 + R(-.08, .14), lf = k % 4 === 3; M(lf ? box(.06, .01, .035) : ico(R(.035, .058), 0), lf ? (k % 8 === 3 ? LF : LF2) : BG[k % 4], x, y, z, { r: lf ? [R(0, 1), R(0, 3), R(0, 1)] : undefined, cast: false }); }
  if (bg >= 2) for (let k = 0; k < (bg === 3 ? 7 : 3); k++){ const x = -1.5 + k * .2; for (let j = 0; j < 4 + bg; j++) M(ico(.03, 0), BG[(j + k) % 4], x + R(-.03, .03), fy + .72 - j * .06, d / 2 + .7 + R(-.02, .02), { cast: false }); }   // chùm bông rủ xuống
  for (let k = 0; k < 6 + bg * 4; k++) M(ico(.038, 0), k % 3 === 2 ? LF : BG[k % 4], -1.62 + R(-.1, .1), fy + .05 + k * (.7 / (6 + bg * 4)), d / 2 + .68 + R(-.06, .06), { cast: false });
  // máng xối tre chẻ đôi, móc đỡ, ống xuống lu
  const W2 = w / 2; M(new T.CylinderGeometry(.03, .03, 1.9, 8, 1, true, 0, Math.PI), MS('#9CBF52'), W2 + .07, fy + .86, -.1, { r: [Math.PI / 2, 0, Math.PI], ds: true }); for (let k = 0; k < 5; k++) M(box(.012, .06, .012), '#6B4529', W2 + .06, fy + .89, -.95 + k * .45);
  M(cyl(.02, .02, .55, 6), MS('#8DB04A'), W2 + .07, fy + .58, .82); for (let k = 0; k < 3; k++) M(cyl(.024, .024, .01, 6), MS('#6E8F2E'), W2 + .07, fy + .4 + k * .17, .82, { cast: false });
  // lu da lươn trên kệ gạch, nắp gỗ, gáo dừa
  const lu = G(W2 + .1, 0, 1.0, 0, g); M(box(.36, .06, .36), BRK, 0, .03, 0, { p: lu }); M(new T.SphereGeometry(.2, 12, 9), MS('#5E4632'), 0, .25, 0, { p: lu, s: [1, 1.1, 1] }); M(cyl(.13, .15, .06, 12), MS('#4E3A28'), 0, .47, 0, { p: lu }); M(cyl(.15, .15, .02, 12), MS('#8A5D3B'), 0, .51, 0, { p: lu });
  for (let k = 0; k < 5; k++) M(new T.TorusGeometry(.2, .006, 3, 16), GOLD, 0, .17 + k * .05, 0, { p: lu, r: [Math.PI / 2, 0, 0], s: [1 - Math.abs(k - 2) * .06, 1 - Math.abs(k - 2) * .06, 1], cast: false });
  M(new T.SphereGeometry(.05, 8, 6, 0, Math.PI * 2, 0, Math.PI / 2), MS('#6B4A30'), .04, .52, 0, { p: lu, r: [Math.PI, 0, 0] }); M(cyl(.007, .007, .16, 4), '#8A5D3B', .12, .53, 0, { p: lu, r: [0, 0, Math.PI / 2] });
  // hai chậu kiểng hai bên thềm (cùng kiểu chậu kiểng trong tiệm)
  for (const [sx, k] of [[-1, 'kimquyt'], [1, 'nguyetque']]){ const c = G(sx * .5, 0, d / 2 + .86, 0, g); c.scale.setScalar(.75); try { chauKieng(c, CHAU[k]); } catch (e) {} }
  ROOT = pr; return g; }
'''+s[j:]
open(p,'w').write(s); print('ok')
