#!/usr/bin/env python3
"""v98: bướm nhỏ lại đúng cỡ so với liếp (sải cánh ~0,15), bay kiểu bướm: chập chờn lên xuống theo nhịp vỗ, lượn ngoằn ngoèo, chậm,
lúc lướt cánh, đậu xuống ngọn cây xếp cánh khép mở chậm rồi bay tiếp. Icon Sổ bướm giữ nguyên."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep("""m = buMesh(k); m.position.set(x + R(-1, 1), R(.5, 1), z + R(-1, 1)); BUV.root.add(m); const hit = new T.Mesh(new T.SphereGeometry(.22, 6, 4), new T.MeshBasicMaterial({ visible: false })); m.add(hit);
    BUV.list.push({ k, m, hit, tx: x, tz: z, life: R(25, 45), ph: R(0, 6), rest: 0 }); }""",
"""m = buMesh(k); m.scale.multiplyScalar(.5); m.position.set(x + R(-1, 1), R(.5, .8), z + R(-1, 1)); BUV.root.add(m); const hit = new T.Mesh(new T.SphereGeometry(.22, 6, 4), new T.MeshBasicMaterial({ visible: false })); hit.scale.setScalar(.2 / (.22 * m.scale.x)); m.add(hit);   /* cỡ thật so với liếp; vùng chạm vẫn đủ lớn để bắt */
    BUV.list.push({ k, m, hit, tx: x + R(-.4, .4), tz: z + R(-.3, .3), life: R(25, 45), ph: R(0, 6), rest: 0, land: 0, hd: R(0, 6.28), gl: 0 }); }""")
rep("""for (const b of [...BUV.list]){ b.life -= dt; const p = b.m.position; if (b.life <= 0){ } else if (b.rest > 0){ b.rest -= dt; } else { const dx = b.tx - p.x, dz = b.tz - p.z, d = Math.hypot(dx, dz); if (d < .25){ if (Math.random() < .5) b.rest = R(1.5, 3.5); const sp = buSpots(), q = pick(sp); b.tx = q[0] + R(-.4, .4); b.tz = q[1] + R(-.3, .3); } else { p.x += dx / d * dt * .55; p.z += dz / d * dt * .55; b.m.rotation.y = Math.atan2(dx, dz); } p.y += (Math.max(.35, Math.min(1.1, .55 + Math.sin(t * 1.3 + b.ph) * .3)) - p.y) * dt * 2; }
    const fl = b.rest > 0 ? Math.sin(t * 3 + b.ph) * .25 + .9 : Math.sin(t * 18 + b.ph) * .9; for (const [w, sg] of b.m.userData.wings) w.rotation.z = sg * fl;""",
"""for (const b of [...BUV.list]){ b.life -= dt; const p = b.m.position; let fl;
    if (b.life <= 0){ fl = Math.sin(t * 16 + b.ph) * .9; }
    else if (b.rest > 0){ b.rest -= dt; fl = 1.25 + Math.sin(t * 1.6 + b.ph) * .3; b.m.rotation.z *= .9; if (b.rest <= 0){ const q = pick(buSpots()); b.tx = q[0] + R(-.45, .45); b.tz = q[1] + R(-.3, .3); b.land = 0; } }   /* đậu: cánh dựng gần khép, mở ra khép vào chậm */
    else { const dx = b.tx - p.x, dz = b.tz - p.z, d = Math.hypot(dx, dz), want = Math.atan2(dx, dz) + Math.sin(t * 2.1 + b.ph) * .9 + Math.sin(t * 5.3 + b.ph * 1.7) * .45;   /* hướng bay ngoằn ngoèo quanh đích */
      let dh = want - b.hd; dh = Math.atan2(Math.sin(dh), Math.cos(dh)); b.hd += dh * Math.min(1, dt * 3.5); b.gl -= dt; if (b.gl < -R(1.2, 2.6)) b.gl = R(.25, .5);   /* thỉnh thoảng lướt cánh một chút */
      const glide = b.gl > 0, sp = (d < .6 ? .16 : .3) * (glide ? .8 : 1) * (1 + Math.sin(t * 7 + b.ph) * .25); p.x += Math.sin(b.hd) * sp * dt; p.z += Math.cos(b.hd) * sp * dt; b.m.rotation.y = b.hd; b.m.rotation.z = -dh * .5;
      const bob = glide ? 0 : Math.max(0, Math.sin(t * 14 + b.ph)) * .045, cruise = d < .35 ? .2 : .32 + Math.sin(t * .9 + b.ph) * .12 + Math.sin(t * 2.7 + b.ph * 2) * .05; p.y += (cruise + bob - p.y) * Math.min(1, dt * 5);   /* nhấp nhô theo nhịp vỗ cánh, gần đích thì hạ thấp */
      fl = glide ? .35 + Math.sin(t * 3 + b.ph) * .05 : Math.sin(t * 14 + b.ph) * 1.0;
      if (d < .12){ if (Math.random() < .7){ b.rest = R(2, 5); b.land = 1; p.y = .2; } else { const q = pick(buSpots()); b.tx = q[0] + R(-.45, .45); b.tz = q[1] + R(-.3, .3); } } }
    for (const [w, sg] of b.m.userData.wings) w.rotation.z = sg * fl;""")
rep("""if (b.life <= 0){ p.y += dt * .8; if (p.y > 3){""", """if (b.life <= 0){ p.y += dt * .5; p.x += Math.sin(t * 3 + b.ph) * dt * .2; if (p.y > 3){""")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
