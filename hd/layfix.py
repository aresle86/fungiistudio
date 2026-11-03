#!/usr/bin/env python3
"""Góc vườn mới nối liền vườn cũ: 2 liếp nằm ngay bên phải giàn khổ qua, thẳng hàng liếp giữa, hai mương thẳng hàng mương cũ.
Bụi sả, bụi cây chỗ đó dời ra bãi cỏ trống phía ngoài (chỉ khi đã mở góc vườn)."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep("D1 = [8.5, 3.0, 8.5 + LW * 2 + LGAP, 3.8];", "D1 = [7.0, B2[1], 7.0 + LW * 2 + LGAP, B2[3]];   /* nối liền vườn cũ: sát giàn khổ qua, thẳng hàng liếp giữa */")
rep("const M4 = [D1[0], D1[3], D1[2], D1[3] + .5], M5 = [D1[0], D1[1] - .5, D1[2], D1[1]]",
    "const M4 = [D1[0], M2[1], D1[2], M2[3]], M5 = [D1[0], M1[1], D1[2], M1[3]]")
rep("if (EXP){ lily(9.1, (M4[1] + M4[3]) / 2, 0); lily(10.5, (M4[1] + M4[3]) / 2, 1); lily(9.8, (M5[1] + M5[3]) / 2, 1); }",
    "if (EXP){ lily(7.6, (M4[1] + M4[3]) / 2, 0); lily(9.0, (M4[1] + M4[3]) / 2, 1); lily(8.3, (M5[1] + M5[3]) / 2, 1); }")
rep("sway(.45, () => { for (const v of [3.3, 4.6, 5.9]) sa(7.35, v); sa(1.2, 7.3, .8); });",
    "sway(.45, () => { for (const [x, v] of EXP ? [[10.35, 3.2], [10.7, 4.75], [10.25, 5.95]] : [[7.35, 3.3], [7.35, 4.6], [7.35, 5.9]]) sa(x, v); sa(1.2, 7.3, .8); });   /* mở góc vườn thì bụi sả dời ra bãi cỏ trống */")
rep("bush(8.2, 3.2, .9);", "bush(EXP ? 10.9 : 8.2, EXP ? 2.75 : 3.2, .9);")
rep("for (let i = 0; i < n; i++){ const x = R(-2, 10), z = R(-1, 9); if (x > .8 && x < 7.0 && z > 2.6 && z < 6.4) continue;",
    "for (let i = 0; i < n; i++){ const x = R(-2, 10), z = R(-1, 9); if (x > .8 && x < 7.0 && z > 2.6 && z < 6.4) continue; if (EXP && x > 6.9 && x < 9.7 && z > 3.5 && z < 5.55) continue;")

# ---- góc vườn mới: chỉ 1 mương phía dưới, liếp bắt đầu ngang mép trên liếp trước nhà (như vườn trước nhà) ----
rep("D1 = [7.0, B2[1], 7.0 + LW * 2 + LGAP, B2[3]];", "D1 = [7.0, B1[1], 7.0 + LW * 2 + LGAP, B1[3]];")
rep("const M4 = [D1[0], M2[1], D1[2], M2[3]], M5 = [D1[0], M1[1], D1[2], M1[3]], DITCH = EXP ? [M1, M2, M3, M4, M5] : [M1, M2, M3];",
    "const M4 = [D1[0], M1[1], D1[2], M1[3]], M5 = M4, DITCH = EXP ? [M1, M2, M3, M4] : [M1, M2, M3];")
rep("if (EXP){ HOLES.value[4].set(...M4); HOLES.value[5].set(...M5);", "if (EXP){ HOLES.value[4].set(...M4);")
rep("ditch(...M4); ditch(...M5); }", "ditch(...M4); }")
rep("lily(8.3, (M5[1] + M5[3]) / 2, 1); }", "}")
rep("const DD = EXP ? [M1, M2, M4, M5] : [M1, M2]", "const DD = EXP ? [M1, M2, M4] : [M1, M2]")
rep("if (EXP && x > 6.9 && x < 9.7 && z > 3.5 && z < 5.55) continue;", "if (EXP && x > 6.9 && x < 9.7 && z > 2.7 && z < 4.25) continue;")
rep("bush(EXP ? 10.9 : 8.2, EXP ? 2.75 : 3.2, .9);", "bush(EXP ? 10.9 : 8.2, EXP ? 2.5 : 3.2, .9);")
rep("for (const [x, v] of EXP ? [[10.35, 3.2], [10.7, 4.75], [10.25, 5.95]]", "for (const [x, v] of EXP ? [[10.45, 3.7], [10.7, 4.85], [10.25, 5.85]]")

# ---- mé sông: giữ 8 ô, dời sang phải thẳng hàng góc vườn mới (chừa khoảng dưới giàn khổ qua); hàng rào, cây, bụi sả chỗ đó lùi ra ----
rep("const SONG = { lv: 9, cost: 60, x0: 6.3, z0: 6.32,", "const SONG = { lv: 9, cost: 60, x0: 7.0, z0: 6.32,")
rep("if (x > 6.2 && x < 11.6 && z > 6.32 && z < 8.3) continue;", "if (x > 6.9 && x < 12.3 && z > 6.2 && z < 8.3) continue;")
rep("fence(EXP ? 11.75 : 8.1, 2.2, 7.0);", "fence(EXP ? 11.75 : 8.1, 2.2, EXP ? 6.0 : 7.0);")
rep("tree(12.6, 5.9, .85, false);", "tree(13.1, 5.55, .85, false);")
rep("[12.2, 6.9], [13.2, 6.6]", "[12.85, 6.95], [13.2, 6.6]")
rep("for (let i = 0; i < 4; i++){ const m = dcModel(D.rao); m.rotation.y = Math.PI / 2; m.position.set(u, 0, 2.82 + i * 1.24);", "for (let i = 0; i < (EXP ? 3 : 4); i++){ const m = dcModel(D.rao); m.rotation.y = Math.PI / 2; m.position.set(u, 0, (EXP ? 2.6 : 2.82) + i * 1.24);")
rep("chuoi(7.4, 2.3);", "chuoi(7.35, 1.6);")   # bụi chuối lùi ra sau cho thoáng liếp góc vườn mới
rep("[7.4, 2.3]", "[7.35, 1.6]")
rep("bush(12.2, 7.2, .8);", "bush(12.85, 7.3, .8);")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
