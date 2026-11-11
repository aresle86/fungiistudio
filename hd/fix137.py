# v137: QC chợ nổi + Bến bà con (anh Ares 11/11): thẻ đơn có "Ra bến tìm" không bóp chữ nữa,
# bến hiện đủ mọi món bán được (đồ khô, mắm, món nấu không còn bị cắt ở 14 món), chia nhóm cho dễ tìm.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v136a'", "BUILD = 'v137'")

# 1) thẻ đơn nhà bên / ghe bẹo có nút "Ra bến tìm": nút xuống hàng riêng, tên người mua giữ nguyên bề ngang
rep("#cnSo,#cnBen{min-width:110px;height:52px;font-size:18px;margin-right:10px}",
    "#cnSo,#cnBen{min-width:110px;height:52px;font-size:18px;margin-right:10px}\n"
    ".ordr:has([data-a=cnofind]){grid-template-columns:minmax(0,1fr)!important}"
    ".ordr:has([data-a=cnofind]) .oa{grid-column:1!important;grid-row:auto!important;flex-wrap:wrap}"
    ".ordr:has([data-a=cnofind]) .oa .btn.g{flex:1 1 100%!important}"
    ".ordr .oa [data-a=cnofind]{margin-left:auto;padding-left:14px;padding-right:14px}\n"
    ".cngh{font:700 15px/1.2 var(--f-body,'Baloo 2'),sans-serif;color:#4A2F1E!important;opacity:1!important;margin:14px 2px 2px}")

# 2) bến: không cắt ở 14 món, chia hai nhóm
a = "const ks = [...Object.keys(ST.inv || {}), ...Object.keys(ST.gb || {})].filter((k, i, a) => a.indexOf(k) === i && cnbOk(k) && has(k) > 0).sort((x, y) => has(y) - has(x)).slice(0, 14);"
assert s.count(a) == 1
i = s.index(a)
j0 = s.index("h += ks.length ? ks.map(k => ", i)
j1 = s.index("}).join('') : `<div class=\"note\">", j0)
row = s[j0 + len("h += ks.length ? ks.map(k => "):j1] + "}"
tail = "}).join('') : `<div class=\"note\">${cnL('Kho chưa có món nào bán được.', 'Nothing in the shed to sell yet.')}</div>`;"
assert s[j1:j1 + len(tail)] == tail
new = ("const ks = [...Object.keys(ST.inv || {}), ...Object.keys(ST.gb || {})].filter((k, i, a) => a.indexOf(k) === i && cnbOk(k) && has(k) > 0).sort((x, y) => has(y) - has(x));\n"
       "  const cnbRow = k => " + row + ", ksF = ks.filter(k => STORE(k) !== ST.gb), ksD = ks.filter(k => STORE(k) === ST.gb);\n"
       "  h += ks.length ? (ksF.length ? `<div class=\"cngh\">${cnL('Rau trái, trứng', 'Produce and eggs')}</div>` + ksF.map(cnbRow).join('') : '') + (ksD.length ? `<div class=\"cngh\">${cnL('Đồ khô, mắm, món nấu', 'Dried, pickled and cooked')}</div>` + ksD.map(cnbRow).join('') : '') : `<div class=\"note\">${cnL('Kho chưa có món nào bán được.', 'Nothing in the shed to sell yet.')}</div>`;")
s = s[:i] + new + s[j1 + len(tail):]


def within(start, end, a, b, n=1):
    global s
    i = s.index(start); j = s.index(end, i + len(start)); seg = s[i:j]
    assert seg.count(a) == n, (seg.count(a), a[:60])
    s = s[:i] + seg.replace(a, b) + s[j:]

# 3) hiệu ứng: món bay lên xuồng khi mua / bày, xuồng nhún, xu bay về khi ghe về
rep("async function cnbPut(k, n){", "function cnbFx(k, el, bi){ try { const B = CHM.B, now = performance.now() / 1000; if (B){ if (B.me) B.me.userData.hit = now; if (bi != null && B.pals && B.pals[bi]) B.pals[bi].userData.hit = now; } if (!el || FXRM() || !ICON[k]) return; const a = el.getBoundingClientRect(); if (!a.width) return; const sh = document.querySelector('.sheet:not([hidden])'), top = sh ? sh.getBoundingClientRect().top : innerHeight * .6; for (let j = 0; j < 3; j++){ const d = document.createElement('img'); d.src = ICON[k]; d.className = 'fly'; d.style.zIndex = 80; arcFly(d, a.left + a.width / 2, a.top + a.height / 2, innerWidth / 2 + R(-40, 40), Math.max(70, top - 40), { dur: 640, delay: j * 85, lift: R(60, 110), side: R(-30, 30), s0: .5, sp: 1.1, s1: .55, spin: R(-40, 40) }); } } catch (e) {} }\nasync function cnbPut(k, n, el){")
rep("else if (a === 'cnobcput') cnbPut(d.k, +d.n);", "else if (a === 'cnobcput') cnbPut(d.k, +d.n, el);")
within("async function cnbBuy(", "async function cnbPut(", "sfx('pop'); coinPop(", "sfx('pop'); cnbFx(k, el, bt.i); coinPop(", 2)
within("async function cnbPut(", "async function cnbBack(", "sfx('pop'); save(); hud(); renderSheet();", "sfx('pop'); cnbFx(k, el); save(); hud(); renderSheet();", 2)
rep("ST.xu += xu; try { sfx('coin'); } catch (e) {}", "ST.xu += xu; try { sfx('coin'); coinFly(document.body, Math.min(7, 2 + n)); } catch (e) {}")
# chạm ghe/xuồng: ghe nhún một cái
rep("function cnoTap(best){ if (!best) return; let a = best.slice(3); sfx('pick');", "function cnoTap(best){ if (!best) return; let a = best.slice(3); sfx('pick'); try { const h = CHM.B.hits.find(x => x[0] === best); if (h && h[2]) h[2].userData.hit = performance.now() / 1000; } catch (e) {}")

# 4) cảnh sống động hơn: ghe nhún rõ hơn, cò bay thiệt, nước gợn, xuồng bà con chèo trong rạch
rep("for (const o of B.live){ const u = o.userData; o.position.y = u.y0 + Math.sin(t * 1.3 + u.ph) * .012; o.rotation.z = Math.sin(t * .9 + u.ph) * .014 * (u.rz || 1); }",
    "for (const o of B.live){ const u = o.userData, dp = u.hit ? Math.max(0, 1 - (t - u.hit) / .8) : 0; o.position.y = u.y0 + Math.sin(t * 1.3 + u.ph) * .026 - Math.sin(dp * Math.PI * 3) * dp * .08; o.rotation.z = Math.sin(t * .9 + u.ph) * .03 * (u.rz || 1) + Math.sin(dp * 10) * dp * .06; o.rotation.x = Math.sin(t * .7 + u.ph * 1.7) * .014; }")
i0 = s.index('/* cò bay */'); i1 = s.index('\n', i0); old = s[i0:i1]
assert s.count(old) == 1 and old.rstrip().endswith('}')
s = s.replace(old, '/* cò bay: dựng sau khi gom lưới để vỗ cánh được (v137) */')
rep("  /* ánh sáng */\n", """  /* v137: cò bay thiệt, gợn nước quanh xuồng, xuồng bà con chèo trong rạch */
  const birds = [], wg = new T.BoxGeometry(.3, .02, .1), wm = new T.MeshBasicMaterial({ color: '#FFFDF6', fog: false }); for (const [x, y, z, sp] of [[2, 5.2, -16, .55], [2.9, 5.5, -16.6, .55], [3.7, 5.15, -17, .55], [-12, 4.6, -18, .45]]){ const b = new T.Group(); b.position.set(x, y, z); b.userData = { y0: y, sp, ph: R(0, 6) }; for (const s2 of [-1, 1]){ const w = new T.Group(); w.userData.s = s2; const m = new T.Mesh(wg, wm); m.position.x = s2 * .15; w.add(m); b.add(w); } root.add(b); birds.push(b); }
  const rips = [], rg = new T.RingGeometry(.42, .47, 28); pals.slice(0, 5).map(b => [b.position.x, b.position.z]).concat([[-2.5, 2.2], [3.2, 1.0], [-5.5, -.5], [5, BZ - 4]]).forEach(([x, z], i) => { const m = new T.Mesh(rg, new T.MeshBasicMaterial({ color: '#F4FBF8', transparent: true, opacity: 0, depthWrite: false })); m.rotation.x = -Math.PI / 2; m.position.set(x, .03, z); m.userData.ph = (i * .37) % 1; root.add(m); rips.push(m); });
  const dao = G(5, .03, BZ - 13, Math.PI / 2, root); dao.scale.setScalar(1.2); { const P3 = CNX.P.cham || CNX.P.moc; hull(dao, P3[3], P3[4], 1); person(dao, -.25, 0, 0, Math.PI / 2, 3, AVS[3 % AVS.length].shirt, 'nonla'); const t3 = G(.12, 0, 0, 0, dao); heap(t3, 0, 0, ['#7DB063', '#E6D9B8', '#E07A2E'], 6, .07, .045); dao.traverse(o => { if (o.isMesh){ o.castShadow = true; o.userData.sway = 0; } }); try { bmMerge(dao, new Set()); mergeRig(dao); } catch (e) {} } dao.userData = { z: BZ - 13, z0: BZ - 15.5, z1: BZ - 2.6, dir: 1, ry: -Math.PI / 2, w: 0 };
  /* ánh sáng */
""")
rep("return { sc, root, hits, live, me, meM, wk, TX, steam, hl, tags, pals, mist: MIST, t: 0 }; }", "return { sc, root, hits, live, me, meM, wk, TX, steam, hl, tags, pals, mist: MIST, birds, rips, dao, t: 0 }; }")
rep("  /* bảng tên giữ cỡ chữ đọc được; xuồng bà con ở xa quá thì ẩn tên */\n", """  if (B.birds) for (const b of B.birds){ const u = b.userData; b.position.x += u.sp * dt; if (b.position.x > 32) b.position.x = -32; b.position.y = u.y0 + Math.sin(t * .8 + u.ph) * .25; for (const w of b.children) w.rotation.z = w.userData.s * (.15 + Math.sin(t * 7 + u.ph) * .45); }
  if (B.rips) for (const m of B.rips){ const f = (t * .4 + m.userData.ph) % 1; m.scale.setScalar(.4 + f * 1.5); m.material.opacity = .36 * (1 - f) * Math.min(1, f * 6); }
  if (B.dao){ const o = B.dao, u = o.userData; if (u.w > 0) u.w -= dt; else { u.z += u.dir * .6 * dt; if (u.z > u.z1){ u.z = u.z1; u.dir = -1; u.w = 3; } else if (u.z < u.z0){ u.z = u.z0; u.dir = 1; u.w = 4; } } const tr = u.dir > 0 ? -Math.PI / 2 : Math.PI / 2; let d2 = tr - u.ry; d2 = Math.atan2(Math.sin(d2), Math.cos(d2)); u.ry += d2 * Math.min(1, dt * 1.2); o.rotation.y = u.ry; o.position.set(5 + Math.sin(u.z * .35) * .3, .03 + Math.sin(t * 1.3 + 4) * .026, u.z); o.rotation.z = Math.sin(t * .9 + 4) * .03; }
  /* bảng tên giữ cỡ chữ đọc được; xuồng bà con ở xa quá thì ẩn tên */
""")
# bảng tên ghe ở chợ cũng không bị cắt mép màn hình (trước chỉ giữ cho xuồng bà con ở bến)
rep("if (q.far){ if (q.x0 === undefined) q.x0 = o.position.x; o.position.x = q.x0; }", "if (!q.p0) q.p0 = o.position.clone(); o.position.copy(q.p0);")
rep("if (q.far && bk > .5 && o.visible){ wp.sub(C.position); const dz = wp.dot(fw), cx = wp.dot(rt), hw = Math.tan(C.fov * Math.PI / 360) * dz * C.aspect, lim = hw * .97 - o.scale.x / 2; if (dz > 0 && lim > 0) o.position.x += Math.max(-lim, Math.min(lim, cx)) - cx; }",
    "if (o.visible && !q.bt && (q.far ? bk > .5 : bk < .5)){ const w0 = wp.clone(); wp.sub(C.position); const dz = wp.dot(fw), cx = wp.dot(rt), hw = Math.tan(C.fov * Math.PI / 360) * dz * C.aspect, lim = hw * .96 - o.scale.x * ws.x / 2; if (dz > 0 && lim > 0){ const sh = Math.max(-lim, Math.min(lim, cx)) - cx; if (Math.abs(sh) > 1e-4) o.position.copy(o.parent.worldToLocal(w0.addScaledVector(rt, sh))); } }")

# 5) màn dọc: ba nút dưới chợ nổi xếp một hàng, đỡ che cảnh
rep(".cngh{font:", "@media (orientation:portrait){#chUi:has(#cnBen:not([hidden])){flex-direction:row;flex-wrap:wrap;justify-content:center;align-items:flex-end;gap:8px;padding:0 10px}#chUi:has(#cnBen:not([hidden])) > .btn{min-width:0!important;margin-right:0!important;font-size:16px!important;height:52px;padding:0 14px}}\\n.cngh{font:")

# 6) thẻ "Về vườn ngày …" không đè lên bảng đang mở
rep("openSheet = (kind, arg) => { if (VISIT && kind !== 'visit' && kind !== 'bug') return;", "openSheet = (kind, arg) => { if (VISIT && kind !== 'visit' && kind !== 'bug') return; try { const dd = document.querySelector('.ddt.on'); if (dd) dd.classList.remove('on'); } catch (e) {}")

# món bay, xu bay ở chợ nổi: trước bị luật "ẩn hết trừ…" của chợ giấu mất
rep("body.chon > :not(#c):not(.ui.top):not(#chUi):not(#chFade):not(#sheet):not(#scrim):not(script):not(style):not(#load){", "body.chon > :not(#c):not(.ui.top):not(#chUi):not(#chFade):not(#sheet):not(#scrim):not(script):not(style):not(#load):not(.fly):not(#fx):not(#tstw){")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
