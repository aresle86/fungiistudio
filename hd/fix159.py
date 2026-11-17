# v158 -> v159: 5 mô hình nhỏ treo trên ghe ông Bảy cho 5 giống quý mới
# (mướp hương, mía lau, bầu hồ lô, hành hương, rau muống tía), để ông "tìm mua" được cả 11 giống.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), n, a[:60])
    s = s.replace(a, b)
rep("BUILD = 'v158'", "BUILD = 'v159'")
NEW = r"""const mMuop = (p, x, y, z, s = 1) => { const q = G(x, y, z, 0, p); q.scale.setScalar(s); M(cyl(.004, .004, .03, 4), '#5E8A3A', 0, -.015, 0, { p: q }); M(ball(.04), '#84BC5E', 0, -.1, 0, { p: q, s: [.5, 2, .5] }); for (let k = 0; k < 3; k++) M(ball(.04), '#3F7A34', 0, -.1, 0, { p: q, s: [.53, 1.97, .07], r: [0, k * 1.047, 0] }); M(ball(.013, 0), '#F2C43A', 0, -.182, 0, { p: q, s: [1, .6, 1] }); return q; };
const mMia = (p, x, y, z, s = 1) => { const q = G(x, y, z, 0, p); q.scale.setScalar(s); for (let k = 0; k < 3; k++){ const a = k * 2.094 + .4, dx = Math.cos(a) * .012, dz = Math.sin(a) * .012; M(cyl(.012, .012, .2, 6), k === 1 ? '#CBD472' : '#B9C45C', dx, -.1, dz, { p: q }); for (let j = 0; j < 4; j++) M(cyl(.0132, .0132, .006, 6), '#8FA04C', dx, -.025 - j * .05 - k * .006, dz, { p: q }); } M(cyl(.0255, .0255, .011, 8), '#C9A24A', 0, -.06, 0, { p: q }); M(cyl(.0255, .0255, .011, 8), '#C9A24A', 0, -.15, 0, { p: q }); return q; };
const mBau = (p, x, y, z, s = 1) => { const q = G(x, y, z, 0, p); q.scale.setScalar(s); M(cyl(.004, .005, .03, 4), '#7A8A4A', 0, -.015, 0, { p: q }); M(ball(.027), '#C4DE8E', 0, -.045, 0, { p: q, s: [1, 1.05, 1] }); M(ball(.02), '#C4DE8E', 0, -.072, 0, { p: q, s: [.8, 1, .8] }); M(ball(.046), '#C4DE8E', 0, -.118, 0, { p: q, s: [1, .94, 1] }); return q; };
const mHanh = (p, x, y, z, s = 1) => { const q = G(x, y, z, 0, p); q.scale.setScalar(s); for (let k = 0; k < 7; k++){ const u = (k - 3) / 3, dx = u * .05, dz = (k % 2 ? 1 : -1) * .008, yb = -.135 + Math.abs(u) * .018; seg(q, V(u * .012, 0, dz * .3), V(dx, yb + .012, dz), .0045, .0055, k % 2 ? '#4F9E3A' : '#5FAE44', 5); M(ball(.013), k % 2 ? '#D9A9C6' : '#E3BCD2', dx, yb, dz, { p: q, s: [1, 1.35, 1] }); M(cone(.006, .016, 4), '#E8DFCC', dx, yb - .022, dz, { p: q, r: [Math.PI, 0, 0] }); } M(cyl(.024, .024, .01, 8), '#C9A24A', 0, -.022, 0, { p: q, s: [1, 1, .5] }); return q; };
const mRm = (p, x, y, z, s = 1) => { const q = G(x, y, z, 0, p); q.scale.setScalar(s); for (let k = 0; k < 6; k++){ const a = k * 1.047 + .3, dx = Math.cos(a) * .034, dz = Math.sin(a) * .022, ye = -.125 - (k % 3) * .014; seg(q, V(dx * .3, 0, dz * .3), V(dx, ye, dz), .005, .004, k % 2 ? '#7A4466' : '#8E5478', 5); M(ball(.022), k % 2 ? '#5E9A3E' : '#6FAE48', dx, ye - .024, dz, { p: q, s: [.62, 1.35, .3], r: [0, -a + 1.57, 0] }); } M(cyl(.025, .025, .012, 8), '#C9A24A', 0, -.045, 0, { p: q, s: [1, 1, .74] }); return q; };
const mini = (k, p, s = 1) => { const q = G(0, 0, 0, 0, p); q.scale.setScalar(s); k === 'muophuong' ? mMuop(q, 0, 0, 0, 1.05) : k === 'mialau' ? mMia(q, 0, 0, 0, 1) : k === 'bauholo' ? mBau(q, 0, 0, 0, 1.15) : k === 'hanhhuong' ? mHanh(q, 0, 0, 0, 1.15) : k === 'raumuongtia' ? mRm(q, 0, 0, 0, 1.1) : k === 'khommat' ?"""
rep("const mini = (k, p, s = 1) => { const q = G(0, 0, 0, 0, p); q.scale.setScalar(s); k === 'khommat' ?", NEW)
# mon cu: keo xuong cho khong loi len tren moc treo
rep("mKhom(q, 0, -.09, 0, 1.1, '#F7B928')", "mKhom(q, 0, -.135, 0, 1, '#F7B928')")
rep("mOt(q, 0, -.01, 0, 1.1)", "mOt(q, 0, -.03, 0, 1.1)")
rep("mBap(q, 0, 0, 0, 1.2)", "mBap(q, 0, -.072, 0, 1.05)")
rep("mKq(q, 0, 0, 0, 1.2)", "mKq(q, 0, -.03, 0, 1.2)")
rep("mMong(q, 0, 0, 0, .9)", "mMong(q, 0, -.01, 0, .9)")
rep("let pool = BAYK.filter(k => QUY[k] ?", "let pool = [...BAYK, ...BAYK5].filter(k => QUY[k] ?")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
