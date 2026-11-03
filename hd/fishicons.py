#!/usr/bin/env python3
"""Thay 30 icon cá bằng khuôn cá v2 (fish2/tom2 + FSPEC). Dùng: python3 fishicons.py <vào> <ra>. Mỗi chỗ khớp đúng 1 lần."""
import sys, re
s = open(sys.argv[1], encoding='utf8').read()
K = 'caro sacran sacbuom rophi diec mevinh chot bongcat tep he caloc catre thatlat keo chach luon linh lang ngat chep tomcang chanhduc bongtuong bonglau tra cadua hu rodauvang locbong caho'.split()
lines = s.split('\n'); first = None
for k in K:
    idx = [i for i, l in enumerate(lines) if l.startswith(f"  icon('{k}', ")]
    assert len(idx) == 1, (k, len(idx)); i = idx[0]
    assert lines[i].rstrip().endswith(');'), k
    lines[i] = f"  icon('{k}', p => FSPEC.{k}(p));"
    first = i if first is None else min(first, i)
lib = open('fish2.js', encoding='utf8').read().rstrip('\n') + '\n' + open('fishspec.js', encoding='utf8').read().rstrip('\n')
assert '//' not in lib
lines.insert(first, '  /* ===== icon cá v2 (dựng lại 30 loài, 11/2026) ===== */\n' + '\n'.join('  ' + l if l.strip() else l for l in lib.split('\n')))
open(sys.argv[2], 'w', encoding='utf8').write('\n'.join(lines))
print('ok', len(K))
