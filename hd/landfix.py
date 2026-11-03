#!/usr/bin/env python3
"""Đất chưa mở = đất hoang um tùm (cùng màu nền với đất thường, không còn tấm thảm xanh đậm); sương mỏng lại;
thêm bụi rậm, cây con, chuối dại, dừa nước con (mé sông); mép khu cắm cọc tre giăng dây lác. Dùng: python3 landfix.py <vào> <ra>."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b):
    global s
    c = s.count(a); assert c == 1, (c, a[:100]); s = s.replace(a, b)
rep("""      M(box(W + .3, .02, L + .3), '#5E8A42', cx, .005, cz, { cast: false, sway: 0 });""",
"""      sway(.6, () => { const tall = z.k === 'song';   /* đất hoang: không trải thảm màu riêng, chỉ thứ mọc trên đó làm nên khác biệt */
        for (let i = 0; i < Math.round(W * L * .55); i++){ const g = G(R(Z.x0 + .1, Z.x0 + W - .1), 0, R(Z.z0 + .1, Z.z0 + L - .1), R(0, 6)), h = R(.5, .9); M(cyl(.012, .02, h, 5), pick(['#7A6A3A', '#6B5A30']), 0, h / 2, 0, { p: g, cast: false }); for (let k = 0; k < 5; k++) leaf(g, R(.22, .34), .07, pick(['#5E8A3A', '#6E9F57', '#4F7D44']), k * 1.25, R(.5, .9), { y: h * R(.75, 1), droop: .45, cast: false }); }   /* cây con */
        for (let i = 0; i < Math.round(W * L * .3); i++){ const g = G(R(Z.x0 + .15, Z.x0 + W - .15), 0, R(Z.z0 + .15, Z.z0 + L - .15), R(0, 6)); for (let k = 0; k < 5; k++) leaf(g, R(.55, .85), .16, pick(tall ? ['#6FA04A', '#5E8A3A', '#7FAE50'] : ['#7FAE50', '#6FA04A', '#8FB85A']), k * 1.25, R(.9, 1.2), { droop: .65, cast: false }); }   /* bụi chuối dại / dừa nước con lá to */
        for (let i = 0; i < Math.round(W * L * 1.4); i++) M(ico(R(.12, .22), 1), pick(['#4F7D44', '#5E8A3A', '#6E9A48', '#7A9A3E']), R(Z.x0, Z.x0 + W), R(.06, .14), R(Z.z0, Z.z0 + L), { s: [1, .8, 1], cast: false }); });   /* bụi rậm */
      { const e = .12, x0 = Z.x0 - e, x1 = Z.x0 + W + e, z0 = Z.z0 - e, z1 = Z.z0 + L + e, post = (x, zz) => { const h = R(.32, .4); M(cyl(.018, .024, h, 5), pick(['#B8925A', '#A8844E']), x, h / 2, zz, { cast: false, sway: 0 }); };   /* mép khu: cọc tre cắm thưa, giăng dây lác */
        for (const [ax, az, bx, bz] of [[x0, z0, x1, z0], [x1, z0, x1, z1], [x1, z1, x0, z1], [x0, z1, x0, z0]]){ const len = Math.hypot(bx - ax, bz - az), n = Math.max(1, Math.round(len / .9)); for (let k = 0; k < n; k++) post(ax + (bx - ax) * k / n, az + (bz - az) * k / n); M(box(len, .008, .008), '#C9A86A', (ax + bx) / 2, .25, (az + bz) / 2, { r: [0, -Math.atan2(bz - az, bx - ax), 0], cast: false, sway: 0 }); } }""")
rep("""new T.MeshBasicMaterial({ map: fogTx, transparent: true, opacity: .5, depthWrite: false })""", """new T.MeshBasicMaterial({ map: fogTx, transparent: true, opacity: .2, depthWrite: false })""")
rep('m.material.opacity = .2 + .1 * Math', 'm.material.opacity = .1 + .06 * Math')
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
