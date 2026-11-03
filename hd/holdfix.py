#!/usr/bin/env python3
"""v98: câu cá — lúc giựt trúng không còn tự đặt 'đang kéo' (lỗi: click GIỰT xảy ra sau khi đã nhấc tay nên kéo hoài, dây căng tới đứt dù không bấm).
Kéo chỉ khi tay đang thật sự giữ; nhấc tay, trượt khỏi màn, mất focus đều thả."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep("FM.tAll = 14 + FISHK[FM.tgt.k].tier * 5; FM.hold = true;", "FM.tAll = 14 + FISHK[FM.tgt.k].tier * 5; FM.hold = !!window.__PDN;")
rep("addEventListener('pointerdown', e => { if (FM.on && FM.ph === 'reel' && !e.target.closest('[data-f]')) FM.hold = true; }, true);",
    "addEventListener('pointerdown', e => { window.__PDN = true; if (FM.on && FM.ph === 'reel' && !e.target.closest('[data-f]')) FM.hold = true; }, true);")
rep("addEventListener('pointerup', () => { if (FM.on) FM.hold = false; }, true);",
    "{ const up = () => { window.__PDN = false; if (FM.on) FM.hold = false; }; addEventListener('pointerup', up, true); addEventListener('pointercancel', up, true); addEventListener('blur', up); document.addEventListener('visibilitychange', () => { if (document.hidden) up(); }); }   /* nhấc tay, vuốt lệch thành cuộn, đổi app: đều thả dây */")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
