# nc118: mô hình 12 cây mới (chưa mở bán; chỉ thêm hình). Cây trái đi vào FR (cùng bộ dựng ổi, khế, xoài), rau giàn/cọc/liếp đi vào CB.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:80], s.count(a))
    s = s.replace(a, b)
T = open('nc118_tree.js', encoding='utf-8').read()
P = open('nc118_plot.js', encoding='utf-8').read()
rep("  ri.renderLists.dispose(); return { icons: OUT, build, mound }; })();",
    T + "  ri.renderLists.dispose(); return { icons: OUT, build, buildN, mound }; })();")
a = "for (const k of ['chuoi', 'oi', 'khe', 'xoai', 'dua']) CB[k] = (b, st) => { const g = G((b[0] + b[2]) / 2, .06, (b[1] + b[3]) / 2, 0); g.scale.setScalar({ chuoi: 1.05, dua: 1.15 }[k] || 1.35); FR.build(k, g, st); };"
rep(a, a + "\nfor (const k of ['dudu', 'mangcau', 'sung', 'buoi', 'vusua', 'saurieng', 'duasap']) CB[k] = (b, st) => { const g = G((b[0] + b[2]) / 2, .06, (b[1] + b[3]) / 2, 0); g.scale.setScalar({ dudu: 1.2, duasap: 1.15, mangcau: 1.3 }[k] || 1.35); FR.buildN(k, g, st); };\n" + P)
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
