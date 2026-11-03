#!/usr/bin/env python3
"""v101: điện thoại màn thấp — nút Về giữa/Sửa vườn luôn bám dưới ô xu (đo lại liên tục), cột nút phải gọn theo chiều cao, huy hiệu không đè nút."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep("const r = c.getBoundingClientRect(); b.style.top = Math.round(r.bottom + 12) + 'px'; placeSua(); }",
    "const r = c.getBoundingClientRect(); b.style.top = Math.round(r.bottom + (PHONE() ? 8 : 12)) + 'px'; placeSua(); }\n"
    "function PHONE(){ return matchMedia('(max-width:560px)').matches; }\n"
    "function mobLay(){ const ph = PHONE(), H = innerHeight; document.body.classList.toggle('mshort', ph && H < 740); document.body.classList.toggle('mtiny', ph && H < 600); const vv = window.visualViewport; const lift = (vv && Math.abs(vv.scale - 1) < .02) ? Math.max(0, Math.min(120, Math.round(innerHeight - vv.height - vv.offsetTop))) : 0; document.documentElement.style.setProperty('--vvb', lift + 'px'); try { placeCtr(); } catch (e) {} }   /* đo lại vị trí nút theo ô xu mỗi khi khung đổi, khỏi chồng nhau */\n"
    "addEventListener('resize', mobLay); addEventListener('orientationchange', () => setTimeout(mobLay, 300)); if (window.visualViewport) visualViewport.addEventListener('resize', mobLay); setInterval(mobLay, 1200); setTimeout(mobLay, 100);\n"
    "try { const ro = new ResizeObserver(mobLay); const tp = document.querySelector('.ui.top'); if (tp) ro.observe(tp); } catch (e) {}")
rep("const r = b.getBoundingClientRect(); s2.style.top = Math.round(r.bottom + 10) + 'px'; }",
    "const r = b.getBoundingClientRect(); s2.style.top = Math.round(r.bottom + (PHONE() ? 6 : 10)) + 'px'; }")
css = r"""
/* ===== v101 điện thoại màn thấp ===== */
@media (max-width:560px){
  .ui.bot>.row{bottom:calc(12px + var(--vvb,0px) + env(safe-area-inset-bottom,0px))!important}
  .tray{bottom:calc(12px + var(--vvb,0px) + env(safe-area-inset-bottom,0px))!important}
  .ui.bot .ngoai{bottom:calc(12px + var(--vvb,0px) + env(safe-area-inset-bottom,0px))!important}
  .ui.bot .row .kb,.bvn{top:4px!important;right:2px!important;left:auto!important;transform:scale(.9)}
  .tray .tn{right:-8px!important;top:2px!important}
  body.mshort .ui.bot>.row{gap:2px!important}
  body.mshort .ui.bot>.row .bt{height:56px!important;padding-bottom:4px!important}
  body.mshort .ui.bot>.row .bt img{width:46px!important;height:46px!important}
  body.mshort .ui.bot>.row .tg{font-size:11px!important;margin-top:-7px!important}
  body.mtiny .ui.bot>.row .bt{height:52px!important}
  body.mtiny .ui.bot>.row .bt img{width:42px!important;height:42px!important}
}
"""
i = s.rindex('</style>'); s = s[:i] + css + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
