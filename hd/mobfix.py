#!/usr/bin/env python3
"""v97: (1) điện thoại: 4 nút Ghé vườn/Sổ/Chợ/Cài đặt thành cột dọc mép phải, dải dưới đáy dành cho lời Ngoại;
(2) bong bóng liếp kéo xa thì thành chấm màu nhỏ (xanh có đồ thu, cam cần làm), zoom gần mới hiện bong bóng đủ icon."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# ---------- 2. bong bóng thành chấm khi nhìn xa ----------
rep("""M(new T.CircleGeometry(.205, 32), MB('#FFFBF2'), 0, 0, .012, { p: g, cast: false }).userData.ro = 2;""",
    """const disk = M(new T.CircleGeometry(.205, 32), MB('#FFFBF2'), 0, 0, .012, { p: g, cast: false }); disk.userData.ro = 2; g.userData.disk = disk;""")
rep("""tri(.095, .13, -.2, BN, .001).userData.ro = 0;""", """const tailB = tri(.095, .13, -.2, BN, .001); tailB.userData.ro = 0; g.userData.tailB = tailB;""")
rep("""function bubCol(g, c){ if (!g || g.userData.col === c) return; g.userData.col = c;""",
    """function bubDot(g, on){ if (!g || !!g.userData.dot === on) return; g.userData.dot = on; const u = g.userData; for (const m of [u.pl, u.tail, u.tailB]) if (m) m.visible = !on; if (u.disk) u.disk.material.color.set(on ? (u.col || BUBC.lam) : '#FFFBF2'); }   /* nhìn xa: bong bóng thu thành chấm tròn đúng màu, đỡ phủ kín vùng liếp */
function bubCol(g, c){ if (!g || g.userData.col === c) return; g.userData.col = c; if (g.userData.dot && g.userData.disk) g.userData.disk.material.color.set(c);""")
rep("""else if (v.want === 's') bg.scale.setScalar(.8); if (BUBS !== 1) bg.scale.multiplyScalar(BUBS); }""",
    """else if (v.want === 's') bg.scale.setScalar(.8); if (BUBS !== 1) bg.scale.multiplyScalar(BUBS); const far = cam.zoom < DEFZ() * .82; bubDot(bg, far); if (far){ bg.scale.setScalar(.42 * BUBS); bg.position.y = v.bubY - .12; } }""")

# mũi tên chỉ đường chỉ hiện khi việc nằm hẳn ngoài màn hình (không chỉ tới bong bóng đang thấy ở mép)
rep("if (sx > mx && sx < W - mx && sy > top && sy < H - bot){ seen.add(url); continue; }", "if (sx > -12 && sx < innerWidth + 12 && sy > -12 && sy < innerHeight + 12){ seen.add(url); continue; }")
# chỉ một mũi tên: việc gần nhất ngoài màn hình, số là tổng việc đang chờ ngoài màn hình (khỏi chồng mũi tên ở góc)
rep("  for (const side of ['l', 'r', 't', 'b']){ const B = best[side];", "  { let k0 = null, tot = 0; for (const k in best){ tot += best[k].n; if (!k0 || best[k].d < best[k0].d) k0 = k; } for (const k in best) if (k !== k0) delete best[k]; if (k0) best[k0].n = tot; }\n  for (const side of ['l', 'r', 't', 'b']){ const B = best[side];")
# ---------- 1. điện thoại: cột nút bên phải ----------
rep("const W = innerWidth, H = innerHeight, mx = 18,", "const W = innerWidth - (matchMedia('(max-width:560px)').matches ? 78 : 0), H = innerHeight, mx = 18,")
css = r"""

/* mũi tên chỉ đường cùng kiểu ghim sticker: đĩa kem, vòng cam, viền nâu, mũi nhọn liền viền */
.nava{box-shadow:0 0 0 4px #F2A23A,0 0 0 7px #4A2F1E,0 6px 12px rgba(43,52,70,.3)!important}
.nava .nap::after{right:-19px!important;top:50%!important;margin-top:-7px!important;border:7px solid transparent!important;border-left:11px solid #F2A23A!important;border-right:0!important;filter:none!important}
.nava .nap::before{content:'';position:absolute;right:-23px;top:50%;margin-top:-11px;border:11px solid transparent;border-left:17px solid #4A2F1E;border-right:0}
.nava b{right:-14px!important;top:-12px!important;min-width:20px!important;height:20px!important;font-size:12px!important;line-height:20px!important;box-shadow:0 0 0 2px #4A2F1E!important}
/* ===== v97 điện thoại: cột nút mép phải, dải dưới cho lời Ngoại ===== */
@media (max-width:560px){
  .ui.bot>.row{position:fixed!important;left:auto!important;right:max(8px,env(safe-area-inset-right,0px))!important;bottom:calc(12px + env(safe-area-inset-bottom,0px))!important;top:auto!important;margin:0!important;flex-direction:column!important;flex-wrap:nowrap!important;justify-content:flex-end!important;gap:4px!important;width:66px!important;z-index:3}
  .ui.bot>.row .bt{flex:none!important;width:66px!important}
  .ui.bot .ngoai{left:calc(max(10px,env(safe-area-inset-left,0px)) + 70px)!important;right:82px!important;bottom:calc(12px + env(safe-area-inset-bottom,0px))!important;max-width:none!important}
  .tray{bottom:calc(12px + env(safe-area-inset-bottom,0px))!important;left:max(8px,env(safe-area-inset-left,0px))!important}
  .fan{left:8px!important;right:80px!important;bottom:calc(150px + env(safe-area-inset-bottom,0px))!important}
  body.fanon .ui.bot .ngoai{bottom:calc(150px + var(--fanH,110px) + 6px + env(safe-area-inset-bottom,0px))!important}
  #tstw{left:16px!important;right:82px!important;transform:none!important;width:auto!important;bottom:calc(160px + env(safe-area-inset-bottom,0px))!important}
}
"""
i = s.rindex('</style>'); s = s[:i] + css + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
