#!/usr/bin/env python3
"""v100: mũi tên chỉ đường né bong bóng đang thấy trên màn: nếu chỗ đặt sát một bong bóng thì trượt dọc mép cho thoáng."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep("const seen = new Set(), off = [];", "const seen = new Set(), off = [], visP = [];")
rep("if (sx > -12 && sx < innerWidth + 12 && sy > -12 && sy < innerHeight + 12){ seen.add(url); continue; }",
    "if (sx > -12 && sx < innerWidth + 12 && sy > -12 && sy < innerHeight + 12){ seen.add(url); visP.push([sx, sy]); continue; }")
rep("e.style.left = Math.max(mx + 30, Math.min(W - mx - 30, px)) + 'px'; e.style.top = Math.max(top + 30, Math.min(H - bot - 30, py)) + 'px';",
    """let fx = Math.max(mx + 30, Math.min(W - mx - 30, px)), fy = Math.max(top + 30, Math.min(H - bot - 30, py)); { const free = (x, y) => visP.every(([a, b]) => Math.hypot(a - x, b - y) > 70), along = side === 'l' || side === 'r'; if (!free(fx, fy)) for (const o of [70, -70, 140, -140, 210, -210]){ const x2 = along ? fx : Math.max(mx + 30, Math.min(W - mx - 30, fx + o)), y2 = along ? Math.max(top + 30, Math.min(H - bot - 30, fy + o)) : fy; if (free(x2, y2)){ fx = x2; fy = y2; break; } } }   /* né bong bóng đang thấy: trượt dọc mép */
    e.style.left = fx + 'px'; e.style.top = fy + 'px';""")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
