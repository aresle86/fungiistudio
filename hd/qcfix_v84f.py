# QC v84f: cây bị comment (2 cây bóng mát, cây dừa, bụi sả) đặt lại ở bãi cỏ trống bên phải (anh Ares chốt 1/11).
import sys
P = sys.argv[1] if len(sys.argv) > 1 else 'live/vuon3d.html'
s = open(P, encoding='utf-8').read(); log = []
def rep(old, new, n=1, tag=''):
    global s
    c = s.count(old)
    if c != n: sys.exit(f'FAIL [{tag}] khớp {c} lần, cần {n}: {old[:80]!r}')
    s = s.replace(old, new); log.append(tag)
rep("// cây dời ra sau, chừa chỗ chái bếp tree(7.6, .7, .8, false); tree(-.8, 1.1, .9, false); const PALM = palm(4.4, .75);",
    "// cây dời ra sau, chừa chỗ chái bếp\n"
    "/* QC v84: 2 cây bóng mát + cây dừa đặt ở bãi cỏ phải ngoài hàng rào góc vườn mới (cả khi đã mở góc), không đè ô đất, không che nhà, liếp hay cây cổ tích.\n"
    "   Giữ nguyên chuỗi số ngẫu nhiên (sd) để cỏ, bụi dựng phía sau không xê dịch. */\n"
    "{ const sd0 = sd; tree(12.6, 5.9, .85, false); tree(12.9, 4.3, .75, false); palm(13.9, 8.2); sd = sd0; }", tag='đặt lại cây')
rep("// mở góc vườn mới thì dời hàng rào ra ngoài sway(.45, () => { for (let k = 0; k < 12; k++){ const x = R(8.5, 11), z = R(2.4, 6.1); if (EXP && x > D1[0] - .3 && x < D1[2] + .3 && z > D1[1] - .8 && z < D1[3] + .8) continue; sa(x, z, .55, false); } }); bush(9.6, 6.0, .9);",
    "// mở góc vườn mới thì dời hàng rào ra ngoài\n"
    "{ const sd0 = sd; sway(.45, () => { for (const [x, z] of [[12.2, 5.1], [13.3, 5.4], [12.2, 6.9], [13.2, 6.6], [13.5, 4.0], [12.4, 3.7], [12.9, 7.7], [14.6, 7.7]]) sa(x, z, .55, false); }); sd = sd0; }", tag='đặt lại bụi sả')
rep("const t = [[4.4, .75], [6.95, -1.15], [7.6, .7], [7.4, 2.3], [-.8, 1.1]][Math.floor(Math.random() * 5)]",
    "const t = [[6.95, -1.15], [7.4, 2.3], [12.6, 5.9], [12.9, 4.3], [13.9, 8.2]][Math.floor(Math.random() * 5)]", tag='củi rơi đúng gốc cây')
rep("const t = [[6.95, -1.15], [7.6, .7], [-.8, 1.1]][Math.floor(Math.random() * 3)]",
    "const t = [[6.95, -1.15], [12.6, 5.9], [12.9, 4.3]][Math.floor(Math.random() * 3)]", tag='lá rơi đúng gốc cây')
open(P, 'w', encoding='utf-8').write(s); print('OK', ', '.join(log))
