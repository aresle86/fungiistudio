#!/usr/bin/env python3
"""v100: điện thoại — Sổ gọn lại: Sổ giống 3 cột icon vừa (64px), bỏ câu hướng dẫn dài; tab Sổ nhỏ lại; nhân vật Ngoại khi nói nhỏ lại."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep("""let h = hdr('giong') + `<div class="bkhn">Mở bao hạt""", """let h = hdr('giong') + `<div class="bkhn ghint">Mở bao hạt""")
CSS = r"""
/* ===== v100 điện thoại: Sổ gọn ===== */
@media (max-width:560px){
  .stg{grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:4px 2px!important}
  .stk{padding:4px 2px!important}
  .stk .pic{height:68px!important}
  .stk .pic img{width:64px!important;height:64px!important;filter:drop-shadow(2px 0 0 #fff) drop-shadow(-2px 0 0 #fff) drop-shadow(0 2px 0 #fff) drop-shadow(0 -2px 0 #fff) drop-shadow(0 2px 1px rgba(74,47,30,.3))!important}
  .stk b{font-size:13px!important;line-height:1.15}
  .stk .sts{transform:scale(.85);transform-origin:top center;margin-bottom:-6px}
  .bkhn.ghint{display:none}
  .bkhd{transform:scale(.8);transform-origin:left center;margin:-4px 0 0}
  .bkt.on{width:84px!important;height:84px!important}
  .fcard img{width:110px!important;height:110px!important;margin:-8px 0 -10px!important}
  .ngoai .pt{width:86px!important;height:100px!important}
}
"""
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
