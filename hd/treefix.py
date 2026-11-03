#!/usr/bin/env python3
"""v102: đếm vụ cây trái mỗi lần hái (cây trái hái mãi không hết nên trước đây không bao giờ được đếm)."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep("const k0 = p.crop, story = STORY[k0] && !ST.seen['story_' + k0]; p.fast = 0; const left = (c.cuts || 1) - (p.cut || 0) - 1;",
    "const k0 = p.crop, story = STORY[k0] && !ST.seen['story_' + k0]; p.fast = 0; const left = (c.cuts || 1) - (p.cut || 0) - 1; if (c.tree){ if (k0 === 'khe') ST.kheHv = (ST.kheHv || 0) + 1; if (k0 === 'dua') ST.duaHv = (ST.duaHv || 0) + 1; ST.treeHv = (ST.treeHv || 0) + 1; }   /* mỗi lần hái cây trái là một vụ */")
rep("if (k0 === 'khe') ST.kheHv = (ST.kheHv || 0) + 1; if (k0 === 'dua') ST.duaHv = (ST.duaHv || 0) + 1; if (c.tree) ST.treeHv = (ST.treeHv || 0) + 1;", "")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
