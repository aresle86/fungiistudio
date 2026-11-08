  // ==== v118: biểu tượng 12 giống mới, cùng kiểu với cà chua, khổ qua (khối nhiều mặt, ánh sáng chung) ====
  const lathe = (f, n = 10, segs = 10) => { const prof = []; for (let i = 0; i <= n; i++){ const t = i / n; prof.push(new T.Vector2(Math.max(.002, f(t)), t)); } return new T.LatheGeometry(prof, segs).toNonIndexed(); };
  const lfi = (p, L, W, c, x, y, z, r) => { const g = new T.Group(); g.position.set(x, y, z); if (r) g.rotation.set(...r); p.add(g); add(g, fin(blade(L, W, .3, .12, 4)), c); return g; };
  // ---- ĐU ĐỦ: trái nguyên bầu bĩnh vàng cam ửng xanh, nửa bổ dọc ruột cam hạt đen ----
  shot('dudu', p => { const pf = t => .25 * Math.pow(Math.sin(Math.PI * Math.min(1, .03 + t)), .6) * (1 - .3 * t) + .012;
    const w = new T.Group(); w.position.set(-.14, .06, -.1); w.rotation.z = .55; p.add(w); add(w, fin(jit(lathe(pf, 12, 11), .006)), '#F2A93A', 0, -.3, 0, null, [1, .6, 1]);
    for (let k = 0; k < 7; k++){ const a = -.6 + k * .2, t = .55 + (k % 3) * .1, r = pf(t) * 1.004; add(w, fin(new T.CircleGeometry(.035, 6)), '#9DBA4A', Math.cos(a) * r, -.3 + t * .6, Math.sin(a) * r, null, [1, 2.2, 1]).lookAt(Math.cos(a) * 9, -.3 + t * .6, Math.sin(a) * 9); }
    add(w, fin(new T.CylinderGeometry(.02, .024, .05, 5)), '#6E8F3A', 0, .31, 0);
    const h = new T.Group(); h.position.set(.16, -.12, .16); h.rotation.set(-1.2, 0, .5); p.add(h); add(h, fin(new T.SphereGeometry(.22, 10, 6, 0, 6.283, 0, Math.PI / 2)), '#F2B04A', 0, 0, 0, null, [1, .55, 1.35]);
    add(h, fin(new T.CircleGeometry(.215, 14)), '#F07A3A', 0, .003, 0, [-Math.PI / 2, 0, 0], [1, 1.35, 1]); add(h, fin(new T.CircleGeometry(.1, 10)), '#E0603A', 0, .006, 0, [-Math.PI / 2, 0, 0], [1, 1.5, 1]);
    for (let k = 0; k < 16; k++) add(h, fin(new T.IcosahedronGeometry(.02, 0)), '#2A2420', (rn() - .5) * .1, .02, (rn() - .5) * .22); }, V(.15, .4, 1));

  // ---- MÃNG CẦU: trái tròn hơi tim, mắt múi xanh nhạt viền trắng phấn ----
  shot('mangcau', p => { const g = new T.Group(); g.rotation.z = -.15; p.add(g); add(g, fin(jit(new T.IcosahedronGeometry(.3, 1), .01)), '#8DB860', 0, 0, 0, null, [1, 1.08, 1]);
    const d = new T.IcosahedronGeometry(1, 2), pp = d.attributes.position, v = V(), seen = {}; for (let i = 0; i < pp.count; i++){ v.fromBufferAttribute(pp, i); const key = v.x.toFixed(2) + v.y.toFixed(2) + v.z.toFixed(2); if (seen[key]) continue; seen[key] = 1; if (v.z < -.2) continue;
      add(g, fin(new T.IcosahedronGeometry(.06, 0)), rn() < .5 ? '#A6CC78' : '#9AC46C', v.x * .3, v.y * .32, v.z * .3, null, [1, 1, .55]).lookAt(v.x * 2, v.y * 2, v.z * 2); }
    add(g, fin(new T.CylinderGeometry(.02, .025, .1, 5)), '#6E5A3A', .02, .36, 0, [0, 0, .3]); lfi(p, .34, .11, '#4F9E3A', .1, .26, -.1, [0, .3, -.9]); }, V(.2, .3, 1));
  // ---- SUNG: chùm ba trái tròn đầy, dẹt đáy, cổ ngắn, xanh ửng đỏ ----
  shot('sung', p => { const pf = t => .2 * Math.pow(Math.sin(Math.PI * Math.min(1, .02 + t * 1.1)), .5) * (1 - .45 * Math.max(0, t - .55) / .45) + .02;
    const fig = (x, y, z, s, c) => { add(p, fin(jit(lathe(pf, 10, 10), .006)), c, x, y - .18 * s, z, null, [s, .4 * s, s]); add(p, fin(new T.CircleGeometry(.03 * s, 6)), '#7A4A3A', x, y - .18 * s - .002, z, [Math.PI / 2, 0, 0]); add(p, fin(new T.CylinderGeometry(.014, .018, .07 * s, 4)), '#7A8A4A', x, y + .25 * s, z); };
    add(p, fin(tube([V(-.36, .34, -.12), V(-.05, .3, -.1), V(.32, .32, -.14)], t => .038, 4, 5)), '#9A9088');
    fig(-.17, .06, .0, 1, '#9DBA58'); fig(.19, .04, .06, .96, '#C2804A'); fig(.02, -.2, .18, .92, '#B39A50'); lfi(p, .36, .17, '#4F9E3A', .1, .3, -.2, [0, .2, -1.3]); }, V(.2, .3, 1));

  // ---- BƯỞI NĂM ROI: trái tròn đầy hơi nhọn cuống, vỏ xanh vàng lấm tấm, kèm múi bưởi ----
  shot('buoi', p => { const pf = t => .33 * Math.pow(Math.sin(Math.PI * Math.min(1, .02 + t)), .55) * (1 - .32 * Math.pow(t, 1.5)) + .02;
    add(p, fin(jit(lathe(pf, 12, 12), .008)), '#BFD25A', -.06, -.28, -.04, null, [1, .62, 1]); add(p, fin(new T.CylinderGeometry(.018, .022, .06, 4)), '#6E7A3A', -.06, .36, -.04);
    for (let k = 0; k < 22; k++){ const a = rn() * 6.28, t = .12 + rn() * .7, r = pf(t) * 1.004, y = -.28 + t * .62; add(p, fin(new T.CircleGeometry(.009, 5)), '#D8E07A', -.06 + Math.cos(a) * r, y, -.04 + Math.sin(a) * r).lookAt(-.06 + Math.cos(a) * 9, y, -.04 + Math.sin(a) * 9); }
    const m = new T.Group(); m.position.set(.24, -.2, .2); m.rotation.set(.3, -.5, -.2); p.add(m); add(m, fin(new T.SphereGeometry(.17, 8, 6, 0, Math.PI * .6, 0, Math.PI)), '#F6E2C0', 0, 0, 0, null, [1, .8, 1]);
    lfi(p, .3, .15, '#3F8A34', .03, .34, -.06, [0, .4, -1.0]); }, V(.15, .3, 1));

  // ---- VÚ SỮA LÒ RÈN: trái tròn xanh bóng, nửa bổ ngang ruột trắng sữa, sao tím nhạt giữa ----
  shot('vusualr', p => { add(p, fin(jit(new T.IcosahedronGeometry(.25, 2), .005)), '#79B44A', -.13, .02, -.08); add(p, fin(new T.CylinderGeometry(.015, .02, .07, 4)), '#7A6A3A', -.13, .29, -.08);
    for (let k = 0; k < 5; k++){ const a = k * 1.2566; add(p, fin(new T.ConeGeometry(.025, .07, 3)), '#5E8A3A', -.13 + Math.cos(a) * .035, .25, -.08 + Math.sin(a) * .035, [Math.sin(a) * 1.4, 0, -Math.cos(a) * 1.4]); }
    const h = new T.Group(); h.position.set(.18, -.1, .1); h.rotation.set(-1.05, 0, .25); p.add(h); add(h, fin(new T.SphereGeometry(.22, 10, 6, 0, 6.283, 0, Math.PI / 2)), '#79B44A', 0, 0, 0, null, [1, .8, 1]);
    add(h, fin(new T.CircleGeometry(.205, 12)), '#F6F2E6', 0, .002, 0, [-Math.PI / 2, 0, 0]); add(h, fin(new T.CircleGeometry(.16, 12)), '#FBF8F0', 0, .004, 0, [-Math.PI / 2, 0, 0]);
    for (let k = 0; k < 8; k++){ const a = k * .785; add(h, fin(new T.BoxGeometry(.012, .002, .1)), '#D8C8E8', Math.cos(a) * .05, .006, Math.sin(a) * .05, [0, -a + Math.PI / 2, 0]); add(h, fin(new T.IcosahedronGeometry(.016, 0)), '#5A3A2A', Math.cos(a + .4) * .09, .01, Math.sin(a + .4) * .09, null, [1, .5, 1.4]); } }, V(.15, .35, 1));
  // ---- SẦU RIÊNG: trái bầu dục đầy gai, cuống to ----
  shot('saurieng', p => { const g = new T.Group(); g.rotation.z = .25; p.add(g); add(g, fin(jit(new T.IcosahedronGeometry(.3, 1), .01)), '#8E9A3A', 0, 0, 0, null, [1, 1.18, 1]);
    const d = new T.IcosahedronGeometry(1, 2), pp = d.attributes.position, v = V(), seen = {}; for (let i = 0; i < pp.count; i++){ v.fromBufferAttribute(pp, i); const key = v.x.toFixed(2) + v.y.toFixed(2) + v.z.toFixed(2); if (seen[key]) continue; seen[key] = 1; if (v.z < -.3 || v.y > .9) continue;
      const c = add(g, fin(new T.ConeGeometry(.045, .1, 4)), rn() < .5 ? '#9AA644' : '#A8B050', v.x * .32, v.y * .37, v.z * .32); c.lookAt(v.x * 3, v.y * 3.4, v.z * 3); c.rotateX(Math.PI / 2); }
    add(g, fin(new T.CylinderGeometry(.035, .045, .14, 5)), '#6E6A3A', 0, .42, 0); }, V(.2, .3, 1));
  // ---- DỪA SÁP: trái dừa vạt nắp, cơm trắng đặc sệt đầy trái ----
  shot('duasap', p => { const g = new T.Group(); g.rotation.z = -.2; p.add(g); add(g, fin(jit(new T.IcosahedronGeometry(.3, 2), .006)), '#7FA848', 0, -.04, 0, null, [1, .98, 1]);
    add(g, fin(new T.CylinderGeometry(.24, .26, .04, 12)), '#E9D9B4', 0, .2, 0); add(g, fin(new T.CylinderGeometry(.21, .22, .045, 12)), '#FBF6EA', 0, .21, 0); add(g, fin(jit(new T.IcosahedronGeometry(.13, 1), .01)), '#FFFDF6', .02, .23, .02, null, [1, .3, 1]);
    const sp = new T.Group(); sp.position.set(.12, .3, .06); sp.rotation.set(.3, .2, -.7); g.add(sp); add(sp, fin(new T.BoxGeometry(.03, .34, .008)), '#C9A27E', 0, .15, 0); add(sp, fin(new T.SphereGeometry(.05, 6, 4)), '#C9A27E', 0, -.04, 0, null, [1, 1.3, .3]); }, V(.15, .5, 1));
  // ---- BẦU: trái bầu bụng phình, cổ ngắn, xanh nhạt đốm trắng ----
  shot('bau', p => { const pf = t => t < .6 ? .2 * Math.pow(Math.sin(Math.PI * Math.min(1, .03 + t / .6 * .5)), .5) + .03 : .23 - (t - .6) / .4 * .1;
    const mk = (x, y, z, rz, s, c) => { const g = new T.Group(); g.position.set(x, y, z); g.rotation.z = rz; p.add(g); add(g, fin(jit(lathe(pf, 12, 11), .004)), c, 0, -.3 * s, 0, null, [s, .62 * s, s]);
      for (let k = 0; k < 12; k++){ const a = rn() * 6.28, t = .08 + rn() * .75, r = pf(t) * s * 1.006, y = -.3 * s + t * .62 * s; add(g, fin(new T.CircleGeometry(.01, 5)), '#EEF5DC', Math.cos(a) * r, y, Math.sin(a) * r).lookAt(Math.cos(a) * 9, y, Math.sin(a) * 9); }
      add(g, fin(tube([V(0, .3 * s, 0), V(.02, .37 * s, 0), V(.07, .42 * s, 0)], t => .018, 3, 5)), '#6E9A3A'); };
    mk(-.15, .04, -.12, .45, 1, '#A9D27A'); mk(.16, -.04, .12, .2, .95, '#B9DB8C'); }, V(.15, .25, 1));

  // ---- MƯỚP: trái mướp mập, đầu to đuôi thon, xanh thẫm sọc nhạt ----
  shot('muop', p => { const pf = t => .12 * Math.pow(Math.sin(Math.PI * Math.min(1, .03 + t)), .45) * (1 - .3 * t) + .015;
    const mk = (x, y, z, rz, s, c) => { const g = new T.Group(); g.position.set(x, y, z); g.rotation.z = rz; p.add(g); add(g, fin(lathe(pf, 12, 10)), c, 0, -.36 * s, 0, null, [s, .72 * s, s]);
      for (let k = 0; k < 10; k += 2){ const a = k / 10 * 6.283; add(g, fin(lathe(t => pf(t) * .22, 10, 3)), '#6E9A52', Math.cos(a) * .1 * s, -.36 * s, Math.sin(a) * .1 * s, null, [.6 * s, .72 * s, .6 * s]); }
      add(g, fin(tube([V(0, .36 * s, 0), V(.02, .43 * s, 0), V(.06, .48 * s, 0)], t => .016, 3, 5)), '#6E9A3A'); add(g, fin(new T.ConeGeometry(.06, .06, 5)), '#F2C83A', .08, .5 * s, 0, [0, 0, -.6]); };
    mk(-.13, .03, -.1, .6, 1, '#3E6E32'); mk(.14, -.03, .12, .3, .94, '#4A7A38'); }, V(.15, .25, 1));

  // ---- ĐẬU RỒNG: ba trái bốn cánh rộng, xếp quạt, dài ngắn khác nhau ----
  shot('daurong', p => { const pod = (rz, L, x, c, cw) => { const g = new T.Group(); g.position.set(x, -.3, 0); g.rotation.z = rz; p.add(g); add(g, fin(new T.CylinderGeometry(.04, .032, L, 6)), c, 0, L / 2, 0);
      for (let w = 0; w < 4; w++){ const f = new T.Group(); f.rotation.y = w * Math.PI / 2 + Math.PI / 4; g.add(f); add(f, fin(new T.BoxGeometry(.1, L * .94, .012)), cw, .06, L / 2, 0); for (let j = 0; j < 6; j++) add(f, fin(new T.BoxGeometry(.016, .03, .014)), '#C2E88A', .11, L * .1 + j * L * .15, 0); }
      add(g, fin(new T.ConeGeometry(.03, .07, 5)), '#6E9A3A', 0, L + .03, 0); };
    pod(.5, .5, -.1, '#94CC62', '#A2D46C'); pod(0, .56, .02, '#9ED46A', '#A8DC70'); pod(-.5, .44, .14, '#8CC45C', '#9CD066'); }, V(.15, .35, 1));

  // ---- KHÓM: trái tròn đầy vàng cam, mắt khóm xoắn, chùm lá vương miện cao rõ ----
  shot('khom', p => { const g = new T.Group(); g.position.y = -.1; g.rotation.z = -.15; p.add(g); const pf = t => .22 * Math.pow(Math.sin(Math.PI * Math.min(1, .05 + t * .95)), .4) + .02; add(g, fin(lathe(pf, 10, 11)), '#D89A2A', 0, -.3, 0, null, [1, .5, 1]);
    for (let r = 0; r < 6; r++) for (let k = 0; k < 10; k++){ const t = .1 + r * .15, a = k / 10 * 6.283 + r * .32, rr = pf(t) * 1.02, y = -.3 + t * .5; add(g, fin(new T.IcosahedronGeometry(.04, 0)), (r + k) % 3 ? '#E8B43A' : '#C98A2A', Math.cos(a) * rr, y, Math.sin(a) * rr, null, [1, .8, .5]).lookAt(Math.cos(a) * 9, y, Math.sin(a) * 9); }
    add(g, fin(new T.CylinderGeometry(.05, .07, .05, 7)), '#5E8A5A', 0, .22, 0);
    for (let k = 0; k < 16; k++){ const a = k * 2.4, inner = k / 16, L = .34 - inner * .14 + (k % 3) * .03; lfi(g, L, .05, k % 2 ? '#5E8A5A' : '#6F9A60', 0, .22, 0, [0, a, 0]).children[0].rotation.x = -.25 - (1 - inner) * .55; } }, V(.15, .3, 1));

  // ---- MÍA TÍM: hai khúc mía đốt rõ, đầu chặt lộ ruột trắng ngà ----
  shot('mia', p => { const cane = (x, z, rz, L, c) => { const g = new T.Group(); g.position.set(x, 0, z); g.rotation.z = rz; p.add(g); const n = 4; for (let i = 0; i < n; i++){ const y = -L / 2 + (i + .5) * L / n; add(g, fin(new T.CylinderGeometry(.065, .07, L / n - .012, 7)), c, 0, y, 0); add(g, fin(new T.CylinderGeometry(.074, .074, .018, 7)), '#4A3040', 0, y + L / n / 2, 0); add(g, fin(new T.CylinderGeometry(.071, .071, .012, 7)), '#C8B890', 0, y + L / n / 2 - .016, 0); }
      add(g, fin(new T.CircleGeometry(.064, 7)), '#EFE6C8', 0, L / 2 + .01, 0, [-Math.PI / 2, 0, 0]); };
    cane(-.08, -.05, .35, .86, '#6C4458'); cane(.1, .08, .15, .78, '#7A4E62'); lfi(p, .5, .07, '#7AA858', .02, .2, -.12, [0, .2, -.6]); }, V(.2, .3, 1));
