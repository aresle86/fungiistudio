# v145 (BẢN THỬ): món mới + quầy nước + hàng chờ bếp + khách ghé bến + mâm cơm + Tay nghề + nút Bạn bè.
# (1) 6 món bếp mới dùng cá, tôm, ổi, bắp đang ít chỗ xài; 6 món nước pha ở quầy nước (không tốn củi). Hình vẽ bằng code, anh Ares duyệt 13/11.
# (2) Quầy nước: mua bằng xu ở bếp Ngoại, dựng kế chái bếp, 2 ly pha cùng lúc, nước cất gác bếp.
# (3) Hàng chờ bếp: xếp sẵn món, nồi trống là tự lên bếp; 1 chỗ sẵn, mua thêm 2 chỗ bằng xu.
# (4) Đường bán món: khách ghé bến mua món có sẵn trên gác bếp giá hơn 20%; đơn "Mâm cơm" 2-3 món trả gấp rưỡi.
# (5) "Thành thạo" đổi thành "Tay nghề": Quen tay, Mát tay, Nức tiếng; lên bậc Ngoại kể bà con khen. Món nấu nhiều nhất có nhãn "Món tủ".
# (6) Nút "Ghé vườn" đổi thành "Bạn bè", hàng xóm đưa lên đầu; thêm việc "Kết bạn với 1 nhà hàng xóm" có quà.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v144'", "BUILD = 'v145'")

# ---------- (1) hình món mới ----------
A = "icon('cui', p => { [[0, 0],"
assert s.count(A) == 1
N = r"""
  const ly = (p, col, foam) => { add(p, new T.CylinderGeometry(.2, .15, .5, 12), col, 0, -.03, 0); add(p, new T.CylinderGeometry(.16, .16, .03, 12), '#DCE9E8', 0, -.29, 0); add(p, new T.CylinderGeometry(.205, .205, .1, 12, 1, true), '#EAF3F2', 0, .27, 0); add(p, new T.TorusGeometry(.205, .012, 3, 14), '#FBF7EE', 0, .32, 0, [Math.PI / 2, 0, 0]); add(p, new T.CylinderGeometry(.19, .19, .02, 12), foam || col, 0, .225, 0); };
  const da = (p, n = 3) => { for (let k = 0; k < n; k++) add(p, new T.BoxGeometry(.09, .09, .09), '#F4FBFB', -.08 + k * .08, .25, (k % 2 ? .05 : -.04), [R(0, 1), R(0, 1), R(0, 1)]); };
  const onghut = (p, c = '#E8453A') => add(p, new T.CylinderGeometry(.016, .016, .5, 5), c, .1, .34, -.04, [0, 0, -.28]);
  icon('nuocmia', p => { ly(p, '#C9D46A', '#E6EDA0'); da(p); onghut(p); const g = new T.Group(); g.position.set(-.36, -.04, .06); g.rotation.z = .16; p.add(g); const L = .62, n = 3; for (let i = 0; i < n; i++){ const y = -L / 2 + (i + .5) * L / n; add(g, new T.CylinderGeometry(.05, .054, L / n - .01, 7), i % 2 ? '#7A4E62' : '#6C4458', 0, y, 0); if (i < n - 1){ add(g, new T.CylinderGeometry(.058, .058, .016, 7), '#4A3040', 0, y + L / n / 2, 0); add(g, new T.CylinderGeometry(.055, .055, .01, 7), '#C8B890', 0, y + L / n / 2 - .014, 0); } } add(g, new T.CylinderGeometry(.046, .046, .008, 7), '#EFE6C8', 0, L / 2, 0); lf(g, .46, .06, '#7AA858', -.01, L / 2 - .1, 0, .2, .75); lf(g, .2, .04, '#8FBE66', .01, L / 2 - .12, .01, -.3, -.5); });
  icon('nuocdua', p => { const w = jit(new T.IcosahedronGeometry(.3, 2), .008); add(p, w, '#7FB548', 0, -.06, 0, null, [1, 1.05, 1]); add(p, new T.CylinderGeometry(.17, .22, .1, 7), '#F3E7C4', 0, .22, 0); add(p, new T.CylinderGeometry(.11, .11, .02, 10), '#FBFBF4', 0, .275, 0); add(p, new T.CylinderGeometry(.016, .016, .4, 5), '#E8453A', .04, .4, 0, [0, 0, -.3]); add(p, new T.CylinderGeometry(.2, .24, .04, 10), '#B8925E', 0, -.36, 0); });
  icon('sinhtomangcau', p => { ly(p, '#E9EDC4', '#FBFBEE'); for (const [x, z, r] of [[-.06, .02, .09], [.06, -.03, .08], [0, .0, .07]]) blob(p, r, '#FFFFFF', x, .27 + (r === .07 ? .07 : 0), z, [1, .7, 1]); onghut(p, '#E86A8A'); const g = new T.Group(); g.position.set(-.36, -.14, .1); g.rotation.set(0, .5, -.2); p.add(g); add(g, new T.SphereGeometry(.17, 10, 8, 0, Math.PI), '#7FAE4E', 0, 0, 0, [0, Math.PI, 0], [1, 1.15, 1]); for (let k = 0; k < 22; k++){ const a = k * 2.4, e = .25 + (k % 5) * .28; add(g, new T.ConeGeometry(.022, .045, 4), k % 2 ? '#5E8E3A' : '#6E9E44', Math.cos(a) * Math.sin(e) * .17, Math.sin(a) * Math.sin(e) * .195, -Math.cos(e) * .17, [-Math.PI / 2, 0, 0]); } add(g, new T.CircleGeometry(.165, 12), '#FBF9EC', 0, 0, .002, null, [1, 1.15, 1]); add(g, new T.TorusGeometry(.165, .012, 3, 14), '#7FAE4E', 0, 0, .002, null, [1, 1.15, 1]); for (const [x, y] of [[-.05, .06], [.05, .05], [0, -.03], [-.06, -.08], [.06, -.09]]) add(g, new T.SphereGeometry(.02, 6, 5), '#2B2418', x, y, .012, null, [.7, 1.4, .5]); });
  icon('trada', p => { ly(p, '#B8823A', '#C9954A'); da(p, 2); onghut(p, '#F4EEDD'); for (let k = 0; k < 3; k++) add(p, new T.TorusGeometry(.055, .022, 4, 9), '#A8B46A', .3 + (k % 2) * .08, -.27 + k * .012, .08 - k * .09, [Math.PI / 2, 0, 0]); });
  icon('suabap', p => { ly(p, '#F6E08A', '#FFF3B8'); onghut(p, '#E89A2A'); add(p, new T.CylinderGeometry(.06, .045, .34, 8), '#F2C83A', -.33, -.14, .08, [0, 0, .25]); for (let k = 0; k < 4; k++) add(p, new T.TorusGeometry(.058, .012, 3, 8), '#E0A82A', -.33 - (k - 1.5) * .02, -.25 + k * .07, .08, [Math.PI / 2, .25, 0]); const l = add(p, new T.ConeGeometry(.05, .26, 4), '#6FAE4A', -.42, -.2, .06, [0, 0, .7]); l.scale.set(1, 1, .3); });
  icon('nuockhe', p => { ly(p, '#F2D45A', '#F7E08A'); da(p, 2); onghut(p, '#5FAE3F'); const s2 = new T.Shape(); for (let j = 0; j < 10; j++){ const a = j / 10 * 6.28, r = j % 2 ? .05 : .11; j ? s2.lineTo(Math.cos(a) * r, Math.sin(a) * r) : s2.moveTo(r, 0); } add(p, new T.ExtrudeGeometry(s2, { depth: .025, bevelEnabled: false }), '#F7E08A', -.2, .3, .02, [0, .3, 0]); });
  icon('chebap', p => { to(p, '#F7EFCF'); for (let k = 0; k < 16; k++) add(p, new T.BoxGeometry(.045, .03, .04), k % 3 ? '#F2C83A' : '#E8B02A', R(-.2, .2), .07, R(-.16, .16), [0, R(0, 3), 0]); add(p, new T.CylinderGeometry(.1, .1, .012, 8), '#FFFFFF', .05, .075, -.02, null, [1.4, 1, .8]); });
  icon('rophichien', p => { dia(p); const g = new T.Group(); p.add(g); const f = fish2(g, { back: '#B0651C', side: '#D08A2A', belly: '#E6B052', fin: '#A85E18', nose: .86, prof: DEEP, pat: (u, t, y) => u > .28 && u < .74 && y > -.6 && ((u * 13 + y * 1.6) % 1) < .16 ? '#7E4410' : null, dorsal: [[.24, .74, .07, .055, 'spiny']], anal: [[.12, .36, .05, .04, 'round']], tail: 'round', tailL: .15, tailRay: '#7E4410', pect: [.7, -.15, .1, .055], eye: .03, eyeU: .87, eyeT: .38, eyeRim: '#F4EEDD', mouthT: -.05, gillU: .73, gillCol: '#7E4410' }); g.rotation.set(0, 0, 0); p.rotation.set(0, 0, 0); g.rotation.set(-Math.PI / 2 + .12, 0, 0); g.rotation.order = 'YXZ'; g.rotation.y = -.25; g.scale.setScalar(.84); g.position.set(.04, -.04, -.03); for (let k = 0; k < 18; k++) add(p, new T.BoxGeometry(.028, .022, .028), k % 3 ? '#F0C060' : '#E8A83E', R(-.1, .2), .0 + R(0, .012), R(-.09, .05), [R(0, 1), R(0, 1), 0]); for (let k = 0; k < 4; k++){ const l = add(p, new T.CylinderGeometry(.08, .08, .014, 7), k % 2 ? '#5FAE3F' : '#7CC456', .16 + k * .05, -.085 + k * .004, .2 - k * .035, [R(-.25, .25), 0, R(-.25, .25)]); l.scale.set(1.2, 1, .75); } for (let k = 0; k < 2; k++){ add(p, new T.CylinderGeometry(.05, .05, .014, 9), '#E8453A', -.24 + k * .08, -.085 + k * .01, .2 - k * .02, [.2, 0, .1]); add(p, new T.CylinderGeometry(.03, .03, .016, 7), '#F7A08A', -.24 + k * .08, -.084 + k * .01, .2 - k * .02, [.2, 0, .1]); } });
  icon('chathatlat', p => { dia(p); for (const [x, z, y] of [[-.14, -.04, 0], [.12, -.06, 0], [0, .12, 0], [-.02, 0, .05]]){ add(p, new T.CylinderGeometry(.11, .11, .045, 10), '#D9A04A', x, -.06 + y, z, [R(-.08, .08), 0, R(-.08, .08)]); add(p, new T.CylinderGeometry(.085, .085, .01, 10), '#C2842E', x, -.034 + y, z); for (let k = 0; k < 4; k++) add(p, new T.BoxGeometry(.012, .012, .03), '#5FAE3F', x + R(-.05, .05), -.026 + y, z + R(-.05, .05), [0, R(0, 3), 0]); } add(p, new T.CylinderGeometry(.07, .05, .05, 8), '#FBF7EE', .26, -.06, .16); add(p, new T.CylinderGeometry(.06, .06, .01, 8), '#C9682A', .26, -.035, .16); });
  icon('laukeo', p => { add(p, new T.CylinderGeometry(.36, .3, .24, 14, 1, true), '#B8BEC4', 0, -.06, 0); add(p, new T.CylinderGeometry(.3, .3, .02, 14), '#9AA1A8', 0, -.18, 0); add(p, new T.TorusGeometry(.36, .02, 3, 16), '#D8DEE2', 0, .06, 0, [Math.PI / 2, 0, 0]); add(p, new T.CylinderGeometry(.34, .34, .02, 14), '#E8A04A', 0, .04, 0); for (const sg of [-1, 1]) add(p, new T.TorusGeometry(.05, .016, 4, 8, Math.PI), '#8A9097', sg * .39, .02, 0, [Math.PI / 2, 0, sg > 0 ? -Math.PI / 2 : Math.PI / 2]); for (const [x, z, r] of [[-.12, .04, .4], [.08, -.08, -.5], [.04, .12, 1.2]]){ add(p, new T.CapsuleGeometry(.028, .2, 2, 6), '#8A8468', x, .07, z, [Math.PI / 2, 0, r]); } for (let k = 0; k < 8; k++){ const l = add(p, new T.ConeGeometry(.04, .2, 3), k % 2 ? '#5aa83e' : '#3F8A34', R(-.24, .24), .075, R(-.2, .2), [Math.PI / 2, R(0, 3), 0]); l.scale.set(1, 1, .4); } for (const [x, z] of [[-.2, -.12], [.2, .08]]) blob(p, .055, '#E8453A', x, .07, z, [1, .5, 1]); add(p, new T.CylinderGeometry(.16, .2, .1, 8), '#6B4529', 0, -.28, 0); add(p, new T.ConeGeometry(.06, .1, 5), '#F08A3E', 0, -.26, .2); });
  icon('tomnuong', p => { dia(p); for (const [x, z, ry] of [[-.06, -.1, .12], [-.02, .1, -.1]]){ const h = new T.Group(); p.add(h); tom2(h, { body: '#E8603A', body2: '#F0784A', dark: '#B83A1C', claw: '#D8502A', joint: '#F2B03A', leg: '#F09A6A' }); h.rotation.set(0, ry, 0); h.scale.setScalar(.55); h.position.set(x, -.03, z); } p.rotation.set(0, 0, 0); for (let k = 0; k < 6; k++) add(p, new T.BoxGeometry(.05, .006, .012), '#3A2A1E', -.2 + k * .07, .025, -.1 + (k % 2) * .2, [0, .6, 0]); add(p, new T.CylinderGeometry(.075, .055, .05, 8), '#FBF7EE', -.27, -.065, .22); add(p, new T.CylinderGeometry(.065, .065, .01, 8), '#F4EEDD', -.27, -.04, .22); for (let k = 0; k < 6; k++) add(p, new T.BoxGeometry(.014, .014, .014), k % 2 ? '#E8453A' : '#3F8A34', -.27 + R(-.04, .04), -.032, .22 + R(-.04, .04)); const lm = add(p, new T.SphereGeometry(.06, 8, 6, 0, Math.PI), '#8FC24A', .27, -.07, .2, [-Math.PI / 2, 0, .5]); add(p, new T.CircleGeometry(.055, 8), '#DDEB9A', .27, -.068, .2, [-Math.PI / 2, 0, 0]); });
  icon('oilac', p => { add(p, new T.CylinderGeometry(.24, .17, .44, 12), '#F7F4EA', 0, -.06, 0); add(p, new T.TorusGeometry(.24, .014, 3, 14), '#6E95C4', 0, .16, 0, [Math.PI / 2, 0, 0]); for (let k = 0; k < 9; k++){ const a = k * 2.4, r = .05 + (k % 3) * .06; const m = add(p, new T.SphereGeometry(.09, 7, 5, 0, Math.PI), k % 2 ? '#B7D46A' : '#A6C85A', Math.cos(a) * r, .17 + (k % 3) * .03, Math.sin(a) * r, [R(-.6, .6), R(0, 3), R(-.6, .6)]); m.scale.set(.7, 1, .5); } for (let k = 0; k < 12; k++) add(p, new T.BoxGeometry(.014, .014, .014), k % 3 ? '#E8453A' : '#C9682A', R(-.16, .16), .24 + R(0, .04), R(-.14, .14)); add(p, new T.CylinderGeometry(.008, .008, .4, 4), '#C9A66B', .08, .34, -.05, [0, 0, -.25]); });
"""
i = s.index(A); ls = s.rfind('\n', 0, i)
s = s[:ls] + N.rstrip('\n') + s[ls:]

# ---------- (1) món mới ----------
rep("""d.lv0 = d.lv; d.lv = lv; d.sell = sell; if (inn) d.in = inn; } }
""", r"""d.lv0 = d.lv; d.lv = lv; d.sell = sell; if (inn) d.in = inn; } }
/* v145: món mới cho cá, tôm, ổi, bắp; món nước (nuoc: 1) pha ở quầy nước, không tốn củi */
Object.assign(DISH, {
  rophichien: { name: 'Rô phi chiên xù', sell: 85, unit: 'dĩa', lv: 10, in: { rophi: 1, trungga: 1, cui: 1 }, t: 12 * 60, story: 'Rô phi lăn trứng, chiên giòn tới vây. Chấm nước mắm me, cuốn rau sống là hết cơm.' },
  oilac: { name: 'Ổi lắc muối ớt', sell: 100, unit: 'ly', lv: 11, in: { oi: 4, ot: 1, muoi: 1 }, t: 3 * 60, story: 'Ổi xắt miếng, bỏ muối ớt vô ly lắc cho đều. Tụi nhỏ đi học về là ghé hỏi liền.' },
  chebap: { name: 'Chè bắp', sell: 185, unit: 'chén', lv: 12, in: { bap: 3, dua: 1, duong: 1, cui: 1 }, t: 30 * 60, story: 'Bắp nạo nấu sánh, chan nước cốt dừa. Chè bắp ăn nóng hay ăn nguội đều ngon.' },
  chathatlat: { name: 'Chả cá thát lát', sell: 105, unit: 'dĩa', lv: 13, in: { thatlat: 1, hanh: 2, cui: 1 }, t: 20 * 60, story: 'Cá thát lát nạo lấy thịt, quết với hành cho dai rồi chiên vàng. Hồi đó đám tiệc nào cũng có.' },
  laukeo: { name: 'Lẩu cá kèo', sell: 210, unit: 'nồi', lv: 14, in: { keo: 2, cachua: 2, raumuong: 3, cui: 1 }, t: 35 * 60, story: 'Cá kèo còn nhảy thả vô nồi nước chua, nhúng rau muống. Trời mưa lâm râm mà có nồi lẩu này là ấm bụng.' },
  tomnuong: { name: 'Tôm càng nướng muối ớt', sell: 125, unit: 'dĩa', lv: 15, in: { tomcang: 1, ot: 1, muoi: 1, cui: 1 }, t: 15 * 60, story: 'Tôm càng xanh ướp muối ớt, nướng lửa than cho đỏ vỏ. Lột ra thịt ngọt lịm.' },
  nuockhe: { name: 'Nước khế', sell: 75, unit: 'ly', lv: 10, nuoc: 1, in: { khe: 4, duong: 1 }, t: 3 * 60, story: 'Khế chua vắt lấy nước, thêm chút đường. Trưa nắng uống một ly là mát tới chiều.' },
  suabap: { name: 'Sữa bắp', sell: 135, unit: 'ly', lv: 10, nuoc: 1, in: { bap: 3, duong: 1 }, t: 8 * 60, story: 'Bắp non xay nhuyễn, lọc lấy nước nấu lên. Thơm mùi bắp, ngọt thanh.' },
  nuocdua: { name: 'Nước dừa', sell: 70, unit: 'trái', lv: 12, nuoc: 1, in: { dua: 2 }, t: 2 * 60, story: 'Dừa xiêm chặt nắp, cắm ống hút. Nước ngọt như đường phèn.' },
  trada: { name: 'Trà khổ qua đá', sell: 140, unit: 'ly', lv: 13, nuoc: 1, in: { trakhoqua: 1 }, t: 2 * 60, story: 'Trà khổ qua phơi nhà mình, pha rồi bỏ đá. Uống đắng đầu lưỡi mà hậu ngọt.' },
  sinhtomangcau: { name: 'Sinh tố mãng cầu', sell: 95, unit: 'ly', lv: 14, nuoc: 1, in: { mangcau: 2, duong: 1 }, t: 5 * 60, story: 'Mãng cầu dầm với đường, bỏ đá bào. Chua chua ngọt ngọt, ai uống cũng khen.' },
  nuocmia: { name: 'Nước mía', sell: 80, unit: 'ly', lv: 17, nuoc: 1, in: { mia: 2 }, t: 3 * 60, story: 'Mía ép lấy nước, vắt thêm trái tắc. Ghe xuồng đi ngang ai cũng ghé làm một ly.' } });
const QN = { lv: 10, xu: 350 }, BQ = { cost: [150, 400] };
""")

# ---------- (2) quầy nước: mô hình ----------
rep("function firewood(x, z, ry = 0){", r"""function quayNuoc(x, z){ const g = DYN(G(x, 0, z, 0)); g.visible = false;   /* v145: quầy nước ở mé sông kế cầu ván (anh Ares dời 13/11), mua rồi mới hiện */
  for (const [px, pz] of [[-.3, -.16], [.3, -.16], [-.3, .16], [.3, .16]]) M(cyl(.025, .028, .44, 6), C.bamboo, px, .22, pz, { p: g });
  M(box(.76, .04, .46), '#A07450', 0, .46, 0, { p: g }); M(box(.68, .03, .38), '#8A5D3B', 0, .16, 0, { p: g });   // mặt quầy, kệ dưới
  M(box(.76, .1, .02), '#E9B23A', 0, .39, .235, { p: g, cast: false }); M(box(.02, .1, .46), '#E9B23A', -.385, .39, 0, { p: g, cast: false }); M(box(.02, .1, .46), '#E9B23A', .385, .39, 0, { p: g, cast: false });   // diềm vải
  for (const [jx, c] of [[-.22, '#C9D46A'], [-.02, '#F2D24A'], [.18, '#E88A4A']]){ M(cyl(.075, .065, .17, 8), c, jx, .565, -.06, { p: g }); M(cyl(.08, .08, .02, 8), '#EAF3F2', jx, .66, -.06, { p: g, cast: false }); }   // ba bình nước
  for (const lx of [-.12, .02, .16]) M(cyl(.032, .026, .08, 7), '#F4FBFB', lx, .52, .12, { p: g, cast: false });   // ly
  M(cyl(.018, .018, 1.3, 6), '#6B4529', -.3, .65, -.16, { p: g }); M(cyl(.02, .62, .2, 10), '#E05A47', -.3, 1.3, -.16, { p: g }); M(cyl(.6, .62, .03, 10), '#FBF7EE', -.3, 1.2, -.16, { p: g, cast: false }); M(sph(.035, 6, 5), '#FBF7EE', -.3, 1.41, -.16, { p: g });   // dù
  for (let k = 0; k < 3; k++) M(cyl(.022, .026, .8, 6), k % 2 ? '#7A4E62' : '#6C4458', .47 + k * .045, .4, -.1 + k * .05, { p: g, r: [0, 0, -.13] });   // bó mía dựng kế bên
  M(box(.18, .2, .18), '#7FB7C9', .2, .27, .02, { p: g }); M(box(.2, .02, .2), '#EAF3F2', .2, .38, .02, { p: g, cast: false });   // thùng đá
  const hit = new T.Mesh(new T.BoxGeometry(1.0, 1.4, .7), new T.MeshBasicMaterial({ visible: false })); hit.position.set(x, .7, z); S.add(hit);
  return { x, z, g, hit }; }
function firewood(x, z, ry = 0){""")
rep("const BEPW = bepHut(5.15, .05);", "const BEPW = bepHut(5.15, .05), QNW = quayNuoc(-.5, 8.3);")

# ---------- CSS ----------
rep(".slots{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}", ".slots{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}\n"
    ".bq{margin-top:10px;background:#FBF7EE;border:2px solid #E8DFCC;border-radius:14px;padding:8px 12px}.bq>b{display:block;font:16px/1.2 var(--f-game);color:#4A2F1E}.bq>span{display:block;font-size:13px;color:#8A5D3B}"
    ".bqs{display:flex;flex-wrap:wrap;gap:10px;margin-top:8px;align-items:center}"
    ".bqi{position:relative;width:52px;height:52px;border-radius:12px;border:2px solid #CDBBA0;background:#F3EADB;display:grid;place-items:center;font:700 24px/1 var(--f-game);color:#8A5D3B;padding:0;cursor:pointer}"
    ".bqi.add{border-style:dashed}.bqi img{width:40px;height:40px}.bqi i{position:absolute;right:-7px;top:-7px;width:22px;height:22px;border-radius:50%;background:#C24A2E;color:#fff;font:700 14px/22px sans-serif;font-style:normal}"
    ".bqb{min-height:52px;border-radius:12px;border:2px solid #E3C36A;background:#FFF3C9;color:#6B4529;font:700 14px/1.2 var(--f-body,'Baloo 2'),sans-serif;padding:4px 12px;display:inline-flex;align-items:center;gap:4px;cursor:pointer}.bqb img{width:18px;height:18px}.bqb:disabled{opacity:.55}"
    ".leadt.mam{background:#4F7D44;font-size:12px}.leadt.kh{background:#C2553A;font-size:12px}.rpk .leadt{margin-left:6px}")

# ---------- (3) hàng chờ + (2) quầy nước: luật chơi ----------
rep("function bepSim(dt){ if (!ST.bep) ST.bep = { lit: 0, pots: [null, null], made: {} }; for (const p of ST.bep.pots) if (p && p.t > 0) p.t = Math.max(0, p.t - dt); }",
r"""function bepSim(dt){ if (!ST.bep) ST.bep = { lit: 0, pots: [null, null], made: {} }; for (const p of ST.bep.pots) if (p && p.t > 0) p.t = Math.max(0, p.t - dt);
  if (!ST.qn) ST.qn = { own: 0, pots: [null, null] }; for (const p of ST.qn.pots) if (p && p.t > 0) p.t = Math.max(0, p.t - dt);
  const B = ST.bep; if (B.q && B.q.length) for (let i = 0; i < B.pots.length && B.q.length; i++){ const p = B.pots[i]; if (p && (p.t > 0 || gbUsed() >= GB_CAP)) continue; if (p) bepBank(p.k); const k = B.q.shift(), T2 = ttTime(k, DISH[k].t); B.pots[i] = { k, t: T2, T: T2 }; } }   /* v145: nồi trống (hoặc chín mà gác bếp còn chỗ) thì món chờ tự lên bếp */
function bepBank(k){ const B = ST.bep, d = DISH[k]; ST.gb[k] = (ST.gb[k] || 0) + 1; if (!B.made[k]) setTimeout(() => { try { bump('newdish'); } catch (e) {} }, 0); ttAdd(k, d.t); B.made[k] = (B.made[k] || 0) + 1; try { gainXP(ttXP(k, d.sell / 8)); bump('cook'); } catch (e) {} }
function bepQCap(){ return 1 + ((ST.bep && ST.bep.qx) || 0); }
function bepQAdd(k){ const B = ST.bep, d = DISH[k]; B.q = B.q || []; if (!d || d.nuoc || (ST.lv || 1) < dLv(k) || B.q.length >= bepQCap() || !bepCan(k)) return; for (const [j, q] of Object.entries(d.in)) STORE(j)[j] -= q; B.q.push(k); sfx('pop'); buzz(10); save(); hud(); }
function bepQDel(i){ const B = ST.bep, k = (B.q || [])[i]; if (!k) return; B.q.splice(i, 1); for (const [j, q] of Object.entries(DISH[k].in)) STORE(j)[j] = (STORE(j)[j] || 0) + q; sfx('pick'); toast(L135(`Lấy ${DISH[k].name.toLowerCase()} khỏi hàng chờ, đồ nấu trả lại kho.`, `${DISH[k].name} removed, ingredients returned.`)); save(); hud(); }
function bepQBuy(b){ const B = ST.bep, n = B.qx || 0, c = BQ.cost[n]; if (c == null || ST.xu < c) return; ST.xu -= c; B.qx = n + 1; try { coinPop(`-${c} xu`, '#F08A6E'); sfx('up'); } catch (e) {} toast(L135(`Hàng chờ bếp thêm một chỗ, giờ xếp được ${bepQCap()} món.`, `Kitchen queue now holds ${bepQCap()} dishes.`), 'vui'); save(); hud(); }
function bepQHTML(){ const B = ST.bep, q = B.q || [], cap = bepQCap(), n = B.qx || 0, c = BQ.cost[n]; let h = `<div class="bq"><b>${L135('Hàng chờ', 'Queue')}</b><span>${L135('Xếp sẵn món, nồi nào trống là tự lên bếp', 'Line up dishes, they start when a pot frees up')}</span><div class="bqs">`;
  for (let i = 0; i < cap; i++){ const k = q[i]; h += k ? `<button class="bqi" data-a="bqdel" data-n="${i}" aria-label="${L135('Bỏ', 'Remove')} ${DISH[k].name}"><img src="${ICON[k]}" alt=""><i>×</i></button>` : `<button class="bqi add" data-a="bqpick" aria-label="${L135('Xếp món chờ', 'Queue a dish')}">+</button>`; }
  if (c != null) h += `<button class="bqb" data-a="bqbuy" ${ST.xu >= c ? '' : 'disabled'}>${L135('Thêm chỗ', 'Add slot')} · <img src="${UIC.coin}" alt="">${c}</button>`;
  return h + '</div></div>'; }
function qnOn(){ return !!(ST.qn && ST.qn.own); }
function qnBuy(b){ if (qnOn() || (ST.lv || 1) < QN.lv || ST.xu < QN.xu) return; ST.xu -= QN.xu; ST.qn = ST.qn || { own: 0, pots: [null, null] }; ST.qn.own = 1; try { coinPop(`-${QN.xu} xu`, '#F08A6E'); sfx('up'); for (let n = 0; n < 8; n++) puff('spark', QNW.x, .7, QNW.z, 1, pick(['#F5D27A', '#9fd36a']), .5); } catch (e) {} say('Quầy nước dựng xong rồi đó con, ngoài mé sông kế cầu ván. Nước pha mau lắm, khỏi tốn củi.', 'vui', { now: true }); save(); hud(); }
function qnCook(k){ const d = DISH[k], Q = ST.qn, i = Q.pots.findIndex(p => !p); if (!qnOn() || !d || !d.nuoc || (ST.lv || 1) < dLv(k) || i < 0 || !bepCan(k)) return; for (const [j, q] of Object.entries(d.in)) STORE(j)[j] -= q;
  Q.pots[i] = { k, t: ttTime(k, d.t), T: ttTime(k, d.t) }; sfx('pop'); buzz(10); save(); hud(); if (!ST.bep.made[k]) setTimeout(() => say(d.story, 'vui', { idle: true }), 300); }
function qnTake(i){ const Q = ST.qn, p = Q.pots[i]; if (!p || p.t > 0) return false; if (gbUsed() >= GB_CAP){ toast('Gác bếp hết chỗ rồi con. Đem món ra chợ bán bớt hay giao cho hàng xóm nghe.', 'lo', { now: true }); return false; }
  Q.pots[i] = null; bepBank(p.k); try { flyTo(ICON[p.k], QNW.x, .7, QNW.z); floatAt(QNW.x, 1.0, QNW.z, `+1 ${DISH[p.k].name.toLowerCase()}`, '#F5D27A'); sfx('coin'); } catch (e) {} save(); hud(); return true; }
function qnTakeAll(){ let n = 0; if (!qnOn()) return 0; ST.qn.pots.forEach((p, i) => { if (p && p.t <= 0 && qnTake(i)) n++; }); return n; }""")

rep("const d = DISH[p.k]; ST.gb[p.k] = (ST.gb[p.k] || 0) + 1; B.pots[i] = null; if (!B.made[p.k]) setTimeout(() => { try { bump('newdish'); } catch (e) {} }, 0); ttAdd(p.k, d.t); B.made[p.k] = (B.made[p.k] || 0) + 1; flyTo(",
    "const d = DISH[p.k]; B.pots[i] = null; bepBank(p.k); flyTo(")
rep("sfx('coin'); gainXP(ttXP(p.k, d.sell / 8)); bump('cook'); save(); hud(); return true; }", "sfx('coin'); save(); hud(); return true; }")
rep("function bepCook(k){ const d = DISH[k], B = ST.bep, i = B.pots.findIndex(p => !p); if ((ST.lv || 1) < dLv(k)", "function bepCook(k){ const d = DISH[k], B = ST.bep, i = B.pots.findIndex(p => !p); if (d.nuoc || (ST.lv || 1) < dLv(k)")

# quầy nước: hiện mô hình, bong bóng lấy nước, chạm
rep("const BEPV = (() => { const b = bubbleK('h'); return { b, hit: b.children.find(c => c.userData.bub) }; })();",
r"""const BEPV = (() => { const b = bubbleK('h'); return { b, hit: b.children.find(c => c.userData.bub) }; })();
const QNV = (() => { const b = bubbleK('h'); b.visible = false; return { b, hit: b.children.find(c => c.userData.bub) }; })();
function qnTick(t){ const own = qnOn() && !VISIT; QNW.g.visible = own; const ready = own && ST.qn.pots.find(p => p && p.t <= 0); QNV.b.visible = !!ready; if (ready){ try { bubIcon(QNV.b, ICON[ready.k]); } catch (e) {} QNV.b.quaternion.copy(cam.quaternion); QNV.b.position.set(QNW.x, 1.75 + Math.sin(t * 2 + 1) * .035, QNW.z); QNV.b.scale.setScalar(.85 * BUBS * (1 + .07 * Math.abs(Math.sin(t * 3 + 1)))); } }
function qnHitAt(cx, cy){ if (!qnOn() || VISIT) return false; ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); return ray.intersectObjects(QNV.b.visible ? [QNV.hit, QNW.hit] : [QNW.hit], false).length > 0; }""")
rep("function bepTick(t){ const B = ST.bep; if (!B) return;", "function bepTick(t){ try { qnTick(t); } catch (e) {} const B = ST.bep; if (!B) return;")
rep("  if (bepHitAt(OX, OY)){ if ((ST.lv || 1) >= BEP.lv", "  if (qnHitAt(OX, OY)){ sfx('pick'); qnTakeAll(); openSheet('quay'); return; }\n  if (bepHitAt(OX, OY)){ if ((ST.lv || 1) >= BEP.lv")

# sheet + nút
rep("  if (kind === 'bep'){ shT.textContent = 'Bếp Ngoại'; h += bepHTML(); }", "  if (kind === 'bep'){ shT.textContent = 'Bếp Ngoại'; h += bepHTML(); }\n  if (kind === 'quay'){ shT.textContent = L135('Quầy nước', 'Drink stall'); h += qnHTML(); }")
rep("  else if (a === 'bpcook'){ bepCook(b.dataset.k); SHEET.pick = null; }",
    "  else if (a === 'qnbuy'){ qnBuy(b); } else if (a === 'goquay'){ openSheet('quay'); return; } else if (a === 'gobep'){ openSheet('bep'); return; } else if (a === 'qncook'){ qnCook(b.dataset.k); SHEET.pick = null; } else if (a === 'qntake'){ qnTake(+b.dataset.n); } else if (a === 'qntakeall'){ qnTakeAll(); }"
    " else if (a === 'bqpick'){ SHEET.pick = -1; } else if (a === 'bqadd'){ bepQAdd(b.dataset.k); SHEET.pick = null; } else if (a === 'bqdel'){ bepQDel(+b.dataset.n); } else if (a === 'bqbuy'){ bepQBuy(b); } else if (a === 'khsell'){ khSell(b); } else if (a === 'khskip'){ khSkip(); }\n"
    "  else if (a === 'bpcook'){ bepCook(b.dataset.k); SHEET.pick = null; }")
rep("pick: (aPut, i, R, label) => `<button class=\"back\" data-a=\"pickback\">‹ Quay lại</button>` + UX.title(`Chọn món cho ${label.toLowerCase()} ${i + 1}`)",
    "pick: (aPut, i, R, label) => `<button class=\"back\" data-a=\"pickback\">‹ Quay lại</button>` + UX.title(i < 0 ? label : `Chọn món cho ${label.toLowerCase()} ${i + 1}`)")

# bếp: bỏ món nước khỏi danh sách nồi, món tủ, hàng chờ, thẻ quầy nước
rep("if (SHEET && SHEET.pick != null) return UX.pick('bpcook', SHEET.pick, Object.fromEntries(Object.entries(DISH).map(([k, d]) => [k, { ...d, lv: dLv(k), t: d.t / ST.spd }])), 'Nồi');",
    "if (SHEET && SHEET.pick != null){ const tu = monTu(), R = Object.fromEntries(Object.entries(DISH).filter(([, d]) => !d.nuoc).map(([k, d]) => [k, { ...d, name: d.name + (k === tu ? `<em class=\"leadt mam\">${L135('Món tủ', 'Signature')}</em>` : ''), lv: dLv(k), t: d.t / ST.spd }])); return SHEET.pick < 0 ? UX.pick('bqadd', -1, R, L135('Chọn món xếp hàng chờ', 'Pick a dish to queue')) : UX.pick('bpcook', SHEET.pick, R, 'Nồi'); }")
rep("'Nồi', 'Chín rồi · chạm lấy')).join('') + '</div>';", "'Nồi', 'Chín rồi · chạm lấy')).join('') + '</div>' + bepQHTML();")
rep("  return h + ttRow('bep') + UX.more('Bếp Ngoại', 'Hai nồi nấu cùng lúc, mỗi món một bó củi.",
    "  if (lv >= QN.lv) h += qnOn() ? `<div class=\"vcard\"><img src=\"${ICON.nuockhe}\" alt=\"\"><div><b>${L135('Quầy nước', 'Drink stall')}</b><span>${L135('Pha nước mau, khỏi tốn củi', 'Quick drinks, no firewood')}</span></div><button class=\"btn g\" data-a=\"goquay\">${L135('Ra quầy', 'Open')}</button></div>` : `<div class=\"vcard\"><img src=\"${ICON.nuockhe}\" alt=\"\"><div><b>${L135('Dựng quầy nước', 'Build a drink stall')}</b><span>${L135('Pha nước khế, sữa bắp… bán cho bà con. Pha mau, khỏi tốn củi', 'Starfruit juice, corn milk… quick to make, no firewood')}</span></div><button class=\"btn g\" data-a=\"qnbuy\" ${ST.xu >= QN.xu ? '' : 'disabled'}>${L135('Dựng', 'Build')} · ${QN.xu} xu</button></div>`;\n"
    "  return h + ttRow('bep') + UX.more('Bếp Ngoại', 'Hai nồi nấu cùng lúc, mỗi món một bó củi. Xếp món vô hàng chờ thì nồi trống là tự nấu tiếp.")
rep("function bepHTML(){", r"""function monTu(){ const m = (ST.bep && ST.bep.made) || {}; let b = null; for (const k in m) if (DISH[k] && m[k] >= 3 && (!b || m[k] > m[b])) b = k; return b; }   /* món nấu nhiều nhất (từ 3 lần) */
function qnHTML(){ const Q = ST.qn; if (!qnOn()) return UX.hero(ICON.nuockhe, L135('Chưa có quầy nước', 'No drink stall yet'), L135('Vô bếp Ngoại dựng quầy nghe con', "Build one from Ngoại's kitchen")) + UX.cta([UX.btn('gobep', L135('Vô bếp', 'Kitchen'), { g: 1, img: ICON.cui })]);
  if (SHEET && SHEET.pick != null){ const tu = monTu(); return UX.pick('qncook', SHEET.pick, Object.fromEntries(Object.entries(DISH).filter(([, d]) => d.nuoc).map(([k, d]) => [k, { ...d, name: d.name + (k === tu ? `<em class="leadt mam">${L135('Món tủ', 'Signature')}</em>` : ''), lv: dLv(k), t: d.t / ST.spd }])), 'Ly'); }
  const done = Q.pots.filter(p => p && p.t <= 0), run = Q.pots.filter(p => p && p.t > 0); let h = '';
  if (done.length) h += UX.hero(ICON[done[0].k], L135(`${done.length} ly pha xong rồi`, `${done.length} ready`), L135('Lấy cất lên gác bếp nghe con', 'Take them to the kitchen shelf'), 'go');
  else if (run.length){ const t = run.reduce((a, b) => a.t < b.t ? a : b); h += UX.hero(ICON[t.k], `${L135('Đang pha', 'Making')} ${DISH[t.k].name.toLowerCase()}`, `${L135('Còn', '')} ${bepT(t.t)} ${L135('là xong', 'left')}`, '', [1 - t.t / (t.T || DISH[t.k].t), '#5BB8C9']); }
  else h += UX.hero(ICON.nuockhe, L135('Quầy đang rảnh', 'Stall is free'), L135('Chạm ly trống để chọn nước pha', 'Tap an empty glass to pick a drink'));
  h += UX.cta([done.length ? UX.btn('qntakeall', L135('Lấy hết', 'Take all'), { g: 1, img: ICON[done[0].k] }) : '']);
  h += '<div class="slots">' + Q.pots.map((p, i) => UX.slot(i, p ? { ...p, T: p.T || DISH[p.k].t, t: p.t } : null, DISH, 'bpick', 'qntake', 'Ly', L135('Xong rồi · chạm lấy', 'Ready · tap'))).join('') + '</div>';
  h += `<div class="uxs one" style="margin-top:10px">${UX.card('Gác bếp', `${gbUsed()}/${GB_CAP} <small>chỗ</small>`, UX.mbar(gbUsed() / GB_CAP, '#C9A66B'))}</div>`;
  return h + UX.more(L135('Quầy nước', 'Drink stall'), L135('Hai ly pha cùng lúc, không tốn củi. Nước pha xong cất gác bếp, đem ra chợ bán hoặc giao đơn nhà bên. Khách ghé bến cũng hay hỏi mua nước. Pha nước cũng tính vô tay nghề bếp.', 'Two drinks at once, no firewood. Drinks go to the kitchen shelf to sell or deliver.')); }
function bepHTML(){""")

# đơn hàng: món nước cần có quầy
rep("if (DISH[k] && !ST.bep) return false;", "if (DISH[k] && !ST.bep) return false; if (DISH[k] && DISH[k].nuoc && !qnOn()) return false;")
rep("Object.keys(DISH).some(k => dLv(k) <= lv && !(ST.bep && ST.bep.made && ST.bep.made[k]))", "Object.keys(DISH).some(k => dLv(k) <= lv && (!DISH[k].nuoc || qnOn()) && !(ST.bep && ST.bep.made && ST.bep.made[k]))")

# ---------- (4) mâm cơm + khách ghé bến ----------
rep("  const items = [], add = (k, q) =>", r"""  if (lv >= 9 && ST.bep && ST.bep.lit && !L0.some(o => o.mam) && Math.random() < .25){ const md = ST.bep.made || {}, ds = Object.keys(DISH).filter(k => !DISH[k].nuoc && md[k] && ok(k));   /* v145: mâm cơm 2-3 món đã từng nấu, trả gấp rưỡi */
    if (ds.length >= 3){ const n = lv >= 14 && Math.random() < .5 ? 3 : 2, it = []; while (it.length < n) it.push([pick1(ds.filter(x => !it.some(([y]) => y === x))), 1]); const nk = Object.keys(DISH).filter(k => DISH[k].nuoc && ok(k)); if (nk.length && Math.random() < .5) it.push([pick1(nk), 2]);
      for (const [k] of it) last[k] = now; const val = it.reduce((s2, [k, q]) => s2 + q * ttSell(k), 0); return { id: Date.now() + '' + Math.floor(Math.random() * 1e4), who, why: pick1(['dọn mâm cơm đãi khách', 'dọn mâm cúng giỗ', 'dọn mâm cơm ngày mùa']), items: it, xu: Math.round(val * 1.5 / 5) * 5, xp: Math.max(3, Math.round(val * 1.5 / 10)), mam: 1 }; } }
  const items = [], add = (k, q) =>""")
rep("const ordWhyOf = o => o.ghe || o.lead ? o.why", "const ordWhyOf = o => o.ghe || o.lead || o.mam ? o.why")
rep("${o.lead ? '<em class=\"leadt\">Món mới</em>' : ''}</b><span>mua về ${ordWhyOf(o)}", "${o.lead ? '<em class=\"leadt\">Món mới</em>' : ''}${o.mam ? `<em class=\"leadt mam\">${L135('Mâm cơm', 'Feast')}</em>` : ''}</b><span>${o.mam ? '' : 'mua về '}${ordWhyOf(o)}")
rep("function ordHTML(){ if ((ST.lv || 1) < ORD.lv || !ST.ord) return '';", r"""const KH = { every: 18 * 60, stay: 40 * 60, mul: 1.2, who: ['Khách đi xuồng', 'Cô bán hàng bông', 'Chú ghe lúa', 'Mấy cô đi chợ sớm', 'Thầy giáo làng'] }; let KHLIVE = 0;
/* v145: khách ghé bến hỏi mua món đang có trên gác bếp, trả hơn 20%; không bán cũng không sao */
function khSim(dt){ if ((ST.lv || 1) < BEP.lv || !ST.bep || !ST.bep.lit) return; const K = ST.kh = ST.kh || { cur: null, acc: 0 };
  if (K.cur){ K.cur.t -= dt; if (K.cur.t <= 0) K.cur = null; return; } K.acc += dt; if (K.acc < KH.every) return;
  const ds = Object.keys(DISH).filter(k => (ST.gb[k] || 0) > 0); if (!ds.length){ K.acc = KH.every - 90; return; }
  const items = [], a = ds[Math.floor(Math.random() * ds.length)]; items.push([a, Math.min(ST.gb[a], Math.random() < .4 ? 2 : 1)]); const r2 = ds.filter(k => k !== a); if (r2.length && Math.random() < .5){ const b2 = r2[Math.floor(Math.random() * r2.length)]; items.push([b2, 1]); }
  K.cur = { who: KH.who[Math.floor(Math.random() * KH.who.length)], items, xu: Math.max(5, Math.round(items.reduce((s2, [k, q]) => s2 + q * ttSell(k), 0) * KH.mul / 5) * 5), t: KH.stay }; K.acc = 0;
  if (KHLIVE) try { toast(L135('Có khách ghé bến hỏi mua món nấu. Mở Chợ, coi bên Đơn hàng nghe con.', 'A visitor at the pier wants cooked food. Check Orders.'), 'vui'); sfx('pop'); } catch (e) {} }
function khSell(b){ const K = ST.kh, c = K && K.cur; if (!c || !c.items.every(([k, q]) => has(k) >= q)) return; let n = 0; for (const [k, q] of c.items){ STORE(k)[k] -= q; n += q; } ST.xu += c.xu; K.cur = null; K.acc = 0; try { coinFly(b, 4); sfx('coin'); coinPop(`+${c.xu} xu · ${L135('khách ghé bến', 'pier visitor')}`, '#9fd36a'); gainXP(Math.max(1, Math.round(c.xu / 20))); bump('sell', n); } catch (e) {} save(); hud(); }
function khSkip(){ const K = ST.kh; if (K){ K.cur = null; K.acc = 0; } save(); }
function khHTML(){ const c = ST.kh && ST.kh.cur; if (!c) return ''; const ok = c.items.every(([k, q]) => has(k) >= q), m = Math.max(1, Math.ceil(c.t / ST.spd / 60));
  return `<div class="sub">${L135('Khách ghé bến', 'Pier visitor')}</div><div class="ordr${ok ? ' ok' : ''}"><div class="ow"><b>${c.who}<em class="leadt kh">${L135('Trả giá cao', 'Pays more')}</em></b><span>${L135(`hỏi mua món nấu sẵn · còn đợi ${m >= 60 ? Math.round(m / 60) + ' tiếng' : m + ' phút'}`, `wants ready-made food · waits ${m} min`)}</span></div><div class="oi">${c.items.map(([k, q]) => { const have = has(k); return `<span class="oit${have >= q ? ' got' : ''}"><img src="${ICON[k]}" alt=""><i>${Math.min(have, q)}/${q}</i></span>`; }).join('')}</div><div class="oa"><button class="btn g" data-a="khsell" ${ok ? '' : 'disabled'}>${ok ? `${L135('Bán', 'Sell')} · ${c.xu} xu` : L135('Hết món rồi', 'Out of stock')}</button><button class="btn oskip" data-a="khskip">${L135('Để dành', 'Keep it')}</button></div></div>`; }
function ordHTML(){ const h = ordHTML0(); return h ? khHTML() + h : h; }
function ordHTML0(){ if ((ST.lv || 1) < ORD.lv || !ST.ord) return '';""")
rep("function ordSim(dt){ if (!ST.ord) ST.ord = { list: [], acc: 0, first: 0 };", "function ordSim(dt){ try { khSim(dt); } catch (e) {} if (!ST.ord) ST.ord = { list: [], acc: 0, first: 0 };")
rep("gioSim(s2); } catch (e) {} off -= s2; } }", "gioSim(s2); } catch (e) {} off -= s2; } KHLIVE = 1; }")

# ---------- (5) Tay nghề ----------
rep("function ttAdd(k, sec){", r"""function ttTier(b){ return b >= 3 ? L135('Nức tiếng', 'Renowned') : b === 2 ? L135('Mát tay', 'Deft') : b === 1 ? L135('Quen tay', 'Handy') : L135('Mới học', 'Learning'); }
function ttKhen(b){ return b >= 3 ? L135('Đồ nhà mình nức tiếng cả xóm rồi con ơi. Ghe ngoài sông cũng ghé hỏi.', 'Our goods are known all over now. Even passing boats stop to ask.') : b === 2 ? L135('Bà con khen nhà mình mát tay, làm món nào cũng ngon.', 'Neighbors say we have the touch. Everything turns out good.') : L135('Con làm riết quen tay rồi đó. Bà con khen đồ nhà mình làm khéo.', "You've got the hang of it. Neighbors like what we make."); }
function ttAdd(k, sec){""")
rep("toast(`${ttName(s)} ${L135('lên', 'reached')} ${b} ${L135('sao thành thạo', b > 1 ? 'skill stars' : 'skill star')} · ${ttPerk(b)}`);",
    "toast(`${L135('Tay nghề', 'Skill')} ${ttName(s)}: ${ttTier(b)} · ${ttPerk(b)}`); say(ttKhen(b), 'vui', { now: true });")
rep("<b>${L135('Thành thạo', 'Skill')}</b>", "<b>${L135('Tay nghề', 'Skill')} · ${ttTier(st)}</b>")
rep("L135(`Đã làm ${ttHr(h)} giờ · đủ ba sao rồi`,", "L135(`Đã làm ${ttHr(h)} giờ · nức tiếng cả xóm rồi`,")
rep("giờ nữa lên sao: ${ttPerk(st + 1)}`,", "giờ nữa lên bậc ${ttTier(st + 1)}: ${ttPerk(st + 1)}`,")
rep("/* v144: thành thạo chỗ chế biến, tính theo giờ làm */", "/* v144: tay nghề chỗ chế biến, tính theo giờ làm; v145 gọi là Tay nghề: Quen tay, Mát tay, Nức tiếng */")

# ---------- (6) Bạn bè ----------
rep('<span class="tg">Ghé vườn</span>', '<span class="tg">Bạn bè</span>')
rep("if (kind === 'vuon'){ shT.textContent = 'Ghé vườn'; h += vuonHTML(); }", "if (kind === 'vuon'){ shT.textContent = L135('Bạn bè', 'Friends'); h += vuonHTML(); }")
rep("function vuonHTML(){ const left = mauLeft(); return UX.title('Vườn mẫu') + `", "function vuonHTML(){ const left = mauLeft(); return nbHTML() + UX.title('Vườn mẫu') + `")
rep("""<button class="btn g" data-a="gomau">Chèo qua</button></div>` + nbHTML(); }""", """<button class="btn g" data-a="gomau">Chèo qua</button></div>`; }""")
rep("NB2.at = 0; await nbLoad(true); return r; }", "NB2.at = 0; await nbLoad(true); try { ST.banDone = 1; bump('ban'); save(); } catch (e) {} return r; }")
rep("  try { if (cauOn()) F.push({ lv: CAU.lv, t: 'fish', txt: 'Câu 2 con cá', need: 2, rw: ['coin', 20] });",
    "  try { if (lv >= VUON.lv && ST.player && !ST.banDone && !(NB2.list || []).some(n => n.followed)) F.push({ lv: VUON.lv + .6, t: 'ban', txt: 'Kết bạn với 1 nhà hàng xóm', need: 1, rw: ['coin', 60] }); } catch (e) {}\n"
    "  try { if (cauOn()) F.push({ lv: CAU.lv, t: 'fish', txt: 'Câu 2 con cá', need: 2, rw: ['coin', 20] });")
n = s.count("x.t === 'cook' ? (ICON.canhchuaca || ICON.com) :"); assert n >= 1, n
s = s.replace("x.t === 'cook' ? (ICON.canhchuaca || ICON.com) :", "x.t === 'ban' ? AVIMG.banbe : x.t === 'cook' ? (ICON.canhchuaca || ICON.com) :")

# lên cấp 10 báo có quầy nước; tên tiếng Anh
rep("for (const k in DCLV){ if (!DCK[k]) continue; const L = LVFEAT[DCLV[k]]", "(LVFEAT[QN.lv] = LVFEAT[QN.lv] || []).push(['nuockhe', 'Quầy nước']);\nfor (const k in DCLV){ if (!DCK[k]) continue; const L = LVFEAT[DCLV[k]]")
rep('const NEN = {"cai": "Mustard greens",', 'const NEN = {"rophichien": "Crispy fried tilapia", "oilac": "Shaken guava with chili salt", "chebap": "Sweet corn pudding", "chathatlat": "Featherback fish cakes", "laukeo": "Goby hotpot", "tomnuong": "Grilled river prawn", "nuockhe": "Starfruit juice", "suabap": "Corn milk", "nuocdua": "Coconut water", "trada": "Iced bitter melon tea", "sinhtomangcau": "Soursop smoothie", "nuocmia": "Sugarcane juice", "cai": "Mustard greens",')

# --- Kết bạn dễ hơn (Ares OK 13/11): (a) gợi ý "Bà con đang chơi" bấm 1 cái là kết bạn; (b) mua hàng ở xuồng bà con xong thì làm quen chủ xuồng.
rep("NB2.err = ''; } catch (e) { NB2.err = String(e.message || e); } finally",
    "NB2.err = ''; try { NB2.sug = await rpc('mv2_suggest', { p_code: CLOUD.cred.code, p_secret: CLOUD.cred.secret }) || []; } catch (e) { NB2.sug = NB2.sug || []; } } catch (e) { NB2.err = String(e.message || e); } finally")
rep("function nbHTML(){",
    "function nbSugHTML(){ const F = NB2.list || [], L = (NB2.sug || []).filter(n => !F.some(x => x.code === n.code && x.followed)).slice(0, 5); if (!L.length) return '';\n"
    "  return `<div class=\"sub\">${L135('Bà con đang chơi', 'Farmers playing now')}</div><div class=\"meta\">${L135('Bấm Kết bạn là thành hàng xóm, khỏi cần xin mã.', 'Tap Add friend to become neighbours. No code needed.')}</div>` + L.map(n => `<div class=\"vcard nb\"><img src=\"${AVIMG.face[n.av] || AVIMG.face[0]}\" alt=\"\" class=\"nbav\"><div><b>${esc(n.name || L135('Bà con', 'Farmer'))}</b><span>${esc(n.garden || '')} · ${L135('cấp', 'level')} ${n.lv}</span></div><div class=\"nbb\"><button class=\"btn g\" data-a=\"nbfol\" data-k=\"${n.code}\">${L135('Kết bạn', 'Add friend')}</button></div></div>`).join(''); }\n"
    "function nbHTML(){")
rep("if (!NB2.list.length) return h + `<div class=\"note\">Chưa có hàng xóm nào. Gửi link vườn cho bạn bè đi con.</div>`;",
    "if (!NB2.list.length) return h + `<div class=\"note\">Chưa có hàng xóm nào. Gửi link vườn cho bạn bè đi con.</div>` + nbSugHTML();")
rep("<div class=\"nbb\">${btns}</div></div>`; }).join(''); }",
    "<div class=\"nbb\">${btns}</div></div>`; }).join('') + nbSugHTML(); }")
rep("else if (a === 'nbfol'){ nbFollow(b.dataset.k).catch(() => {}); return; }",
    "else if (a === 'nbfol'){ if (b.disabled) return; b.disabled = true; const nm0 = ((NB2.sug || []).find(n => n.code === b.dataset.k) || {}).name; nbFollow(b.dataset.k).then(() => { sfx('pop'); toast(L135(`${nm0 || 'Bạn'} thành hàng xóm rồi đó con.`, `${nm0 || 'They'} are your neighbour now.`), 'vui'); }).catch(() => { b.disabled = false; toast(L135('Mạng chập chờn, chút nữa con thử lại nghe.', 'The connection is shaky. Try again in a bit.'), 'dan'); }); return; }")
# (b) chủ xuồng
rep(".nbb{display:flex;flex-direction:column;gap:6px;align-items:flex-end}", ".nbb{display:flex;flex-direction:column;gap:6px;align-items:flex-end}.nbb .btn{min-height:44px}")
rep("b.got = {}; b.sd = 0; }", "b.got = {}; b.sd = 0; b.fr = {}; }")
rep("b.buy += n; sfx('pop'); cnbFx(k, el, bt.i); coinPop(cnL(`-${c2} xu",
    "b.buy += n; b.fr = b.fr || {}; b.fr[it.id] = bt.it.some(x => b.fr[x.id] === 2) ? 2 : (b.fr[it.id] || 1); sfx('pop'); cnbFx(k, el, bt.i); coinPop(cnL(`-${c2} xu")
rep("h += `<div class=\"meta\">${left ? cnL(`Hôm nay con còn mua được ${left} món ở bến.`",
    "{ const fs = bt.real && b.fr ? Math.max(0, ...bt.it.map(x => b.fr[x.id] || 0)) : 0; if (fs) h += `<div class=\"vcard nb\"><img src=\"${AVIMG.banbe}\" alt=\"\" class=\"nbav\"><div><b>${fs === 2 ? cnL('Hai nhà là hàng xóm rồi', 'You are neighbours now') : cnL('Làm quen chủ xuồng', 'Meet the boat owner')}</b><span>${fs === 2 ? cnL('Bữa nào chèo qua vườn nhau chơi nghe con.', 'Row over to visit each other some day.') : cnL('Mua bán quen mặt rồi, kết bạn để bữa nào chèo qua vườn nhau chơi.', 'You have traded. Add them to visit each other.')}</span></div><div class=\"nbb\">${fs === 2 ? '' : `<button class=\"btn g\" data-a=\"cnobcfr\" data-i=\"${bt.i}\">${cnL('Kết bạn', 'Add friend')}</button>`}</div></div>`; }\n"
    "    h += `<div class=\"meta\">${left ? cnL(`Hôm nay con còn mua được ${left} món ở bến.`")
rep("else if (a === 'cnobcmine'){ openSheet('chono', 'ben'); cnbSync(); }",
    "else if (a === 'cnobcmine'){ openSheet('chono', 'ben'); cnbSync(); } else if (a === 'cnobcfr') cnbFr(+d.i);")
rep("function cnbTitle(arg){",
    "async function cnbFr(i){ const b = cnbS(), bt = cnoBcBoats()[i]; if (!bt || !bt.real || !b.fr || CNX.busy) return; const it = bt.it.find(x => b.fr[x.id] === 1); if (!it) return; CNX.busy = 1; let r; try { r = await cnbRpc('mv2_ben_friend', { p_id: it.id }); } catch (e) { return cnbFail(e); } finally { CNX.busy = 0; }\n"
    "  if (!r || !r.ok) return toast(cnL('Chưa kết bạn được, chút nữa con thử lại nghe.', 'Could not add them yet. Try again in a bit.'), 'dan');\n"
    "  for (const x of bt.it) if (b.fr[x.id]) b.fr[x.id] = 2; NB2.at = 0; try { ST.banDone = 1; bump('ban'); } catch (e) {} save(); sfx('pop'); toast(r.was ? cnL(`${r.name || 'Nhà này'} là hàng xóm của con rồi.`, `${r.name || 'They'} are already your neighbour.`) : cnL(`${r.name || 'Bạn'} thành hàng xóm rồi đó con.`, `${r.name || 'They'} are your neighbour now.`), 'vui'); renderSheet(); }\n"
    "function cnbTitle(arg){")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
