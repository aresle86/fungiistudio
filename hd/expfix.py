#!/usr/bin/env python3
"""v102: mở góc vườn mới tại chỗ, không tải lại trang. Dựng sẵn cả hai trạng thái, bật tắt khi trả xu."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

rep("const EXP = (() => { try {", "let EXP = (() => { try {")
# liếp + mương góc vườn: luôn dựng vào nhóm riêng, ẩn khi chưa mở (giữ chuỗi ngẫu nhiên như cũ)
rep("if (EXP){ HOLES.value[4].set(...M4); bed(D1[0], D1[1], D1[0] + LW, D1[3]); bed(D1[0] + LW + LGAP, D1[1], D1[2], D1[3]); ditch(...M4); }",
    "const EXPG = DYN(G(0, 0, 0)), EXPN = DYN(G(0, 0, 0)); EXPG.visible = EXP; EXPN.visible = !EXP;   /* góc vườn mới: EXPG hiện khi đã mở, EXPN là bãi cỏ cũ */\n"
    "{ const sd0 = sd, pr = ROOT; ROOT = EXPG; if (EXP) HOLES.value[4].set(...M4); bed(D1[0], D1[1], D1[0] + LW, D1[3]); bed(D1[0] + LW + LGAP, D1[1], D1[2], D1[3]); ditch(...M4); ROOT = pr; if (!EXP) sd = sd0; }")
rep("if (EXP){ lily(7.6, (M4[1] + M4[3]) / 2, 0); lily(9.0, (M4[1] + M4[3]) / 2, 1); }",
    "{ const sd0 = sd, pr = ROOT; ROOT = EXPG; lily(7.6, (M4[1] + M4[3]) / 2, 0); lily(9.0, (M4[1] + M4[3]) / 2, 1); ROOT = pr; if (!EXP) sd = sd0; }")
rep("sway(.45, () => { for (const [x, v] of EXP ? [[10.45, 3.7], [10.7, 4.85], [10.25, 5.85]] : [[7.35, 3.3], [7.35, 4.6], [7.35, 5.9]]) sa(x, v); sa(1.2, 7.3, .8); });",
    "sway(.45, () => { const SA = [[10.45, 3.7], [10.7, 4.85], [10.25, 5.85]], SB = [[7.35, 3.3], [7.35, 4.6], [7.35, 5.9]], pr = ROOT; ROOT = EXP ? pr : EXPN; for (const [x, v] of EXP ? SA : SB) sa(x, v); ROOT = pr; sa(1.2, 7.3, .8); if (!EXP){ const sd0 = sd; ROOT = EXPG; for (const [x, v] of SA) sa(x, v); ROOT = pr; sd = sd0; } });")
rep("bush(EXP ? 10.9 : 8.2, EXP ? 2.5 : 3.2, .9);",
    "{ const pr = ROOT; if (!EXP) ROOT = EXPN; bush(EXP ? 10.9 : 8.2, EXP ? 2.5 : 3.2, .9); ROOT = pr; if (!EXP){ const sd0 = sd; ROOT = EXPG; bush(10.9, 2.5, .9); TREES.pop(); ROOT = pr; sd = sd0; } }")
rep("if (EXP && x > 6.9 && x < 9.7 && z > 2.7 && z < 4.25) continue;",
    "if (x > 6.9 && x < 9.7 && z > 2.7 && z < 4.25){ if (EXP) continue; const pr = ROOT; ROOT = EXPN; tuft(x, z); ROOT = pr; continue; }")
# hai ô liếp góc vườn luôn có trong danh sách, ẩn tới khi mở
rep("if (EXP) PLOTS.push({ id: 'D1',", "PLOTS.push({ id: 'D1',")
rep("name: 'Góc vườn mới · ô 1' }", "name: 'Góc vườn mới · ô 1', exp: 1 }")
rep("name: 'Góc vườn mới · ô 2' }", "name: 'Góc vườn mới · ô 2', exp: 1 }")
rep("hidP = P => P.bai && (", "hidP = P => (P.exp && !EXP) || P.bai && (")
rep("userData.plot = P.id; } }\nawait LDY(0);\nconst TEXC", "userData.plot = P.id; } if (P.exp && !EXP) sd = sdX; }\nawait LDY(0);\nconst TEXC")
rep("for (const P of PLOTS){ const [u0, v0, u1, v1] = P.b, cx = (u0 + u1) / 2, cz = (v0 + v1) / 2, w = u1 - u0, l = v1 - v0, root = DYN(G(0, 0, 0)), v = PV[P.id] = { root, crop: G(0, 0, 0, 0, root), key: null };",
    "for (const P of PLOTS){ const sdX = sd; const [u0, v0, u1, v1] = P.b, cx = (u0 + u1) / 2, cz = (v0 + v1) / 2, w = u1 - u0, l = v1 - v0, root = DYN(G(0, 0, 0)), v = PV[P.id] = { root, crop: G(0, 0, 0, 0, root), key: null };")
rep("function refreshPlot(id){ const p = ST.plots[id], v = PV[id], P = PL[id]; buildCrop(id);",
    "function refreshPlot(id){ const p = ST.plots[id], v = PV[id], P = PL[id]; if (P.exp){ v.root.visible = EXP; if (!EXP){ if (v.weed) v.weed.visible = false; v.want = null; return; } } buildCrop(id);")
# trả xu dọn góc vườn: bật cảnh mới tại chỗ
rep("setTimeout(() => { save(); location.reload(); }, 1600); } }",
    "setTimeout(() => expOn(), 900); } }\n"
    "function expOn(){ if (EXP) return; EXP = true; ST.exp = 1; HOLES.value[4].set(...M4); EXPG.visible = true; EXPN.visible = false; if (!DITCH.includes(M4)) DITCH.push(M4);   /* mở góc vườn ngay trên màn hình */\n"
    "  for (const m of [...FENCE0.children]) FENCE0.remove(m); { const pr0 = ROOT; ROOT = FENCE0; fence(11.75, 2.2, 6.0); ROOT = pr0; }\n"
    "  for (const hs of SIGN) if (hs.parent) hs.parent.visible = false; SIGN.length = 0; try { DCV.raoK = null; } catch (e) {}\n"
    "  for (const P of PLOTS) if (P.exp){ if (!ST.plots[P.id]) ST.plots[P.id] = pl0(null, 0, .5); refreshPlot(P.id); }\n"
    "  for (let i = 0; i < 44; i++) puff('leaf', 7.1 + Math.random() * 2.6, .25, 2.8 + Math.random() * 1.4, 1, ['#5a8e3a', '#7aa84a', '#8A5D3B', '#B48560'][i % 4], .9);\n"
    "  try { sfx('up'); } catch (e) {} try { camTo(new T.Vector3(8.3, .3, 3.5), Math.max(cam.zoom, DEFZ() * 1.1)); } catch (e) {} save(); hud(); }")
rep("const SIGN = []; if (!EXP){ const g = G(9.2, 0, 4.6, Math.PI / 4);", "const SIGN = []; if (!EXP){ const g = DYN(G(9.2, 0, 4.6, Math.PI / 4));")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
