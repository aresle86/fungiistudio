# v110d (anh Ares 4/11 tối)
#  1. "còn 1 giờ 23.8342499 phút": fmtMin không làm tròn phút lẻ → làm tròn.
#  2. Thẻ việc to quá: giữ nguyên thẻ (cả hộp trong), hẹp còn ~70% và các phần nhỏ lại; chữ vẫn ≥12px (thu bằng scale thì chữ còn 8px, sai quy tắc).
#  3. Mái chuồng vịt (bậc 12 con) nhấp nháy: các tấm lá chồng mí cùng độ cao → nâng mỗi tấm một chút.
#  4. Câu được cá mà thẻ biến mất liền: chỉ nhận bấm nút trên thẻ cá khi ngón tay chạm xuống sau lúc thẻ hiện (cú bấm kéo cá dở không tính).
# Dùng: python3 fix110d.py live/v110c.html live/v110d.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:80], c, n); s = s.replace(a, b)

rep("const fmtMin = m => m >= 60 ?", "const fmtMin = m => (m = Math.round(m), m >= 60) ?")
rep(".nxq{display:block!important;max-width:none!important;width:min(300px,calc(100vw - 110px))!important;padding:16px 8px 6px!important;border-radius:16px!important}",
    ".nxq{display:block!important;max-width:none!important;width:min(210px,calc(70vw - 77px))!important;padding:16px 8px 6px!important;border-radius:16px!important;padding:13px 6px 5px!important}\n.nxq>small{font-size:10px!important;padding:2px 7px!important;top:-9px!important}\n.nxq .q.one{padding:5px 6px!important;gap:6px!important}\n.nxq .q.one>img{width:26px!important;height:26px!important}\n.nxq .q.one .qt>b{font-size:12px!important;white-space:normal!important;display:-webkit-box!important;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;line-height:1.15!important}\n.nxq .q.one .bar{height:10px!important}\n.nxq .q.one .bar em{font-size:9px!important}\n.nxq .q.one .tag{font-size:8px!important;line-height:11px!important;padding:0 4px!important;top:-7px!important}\n.nxq .nqd2{margin-top:4px!important;font-size:12px!important}\n.nxq::before{width:11px!important;height:11px!important;top:-6px!important}")   # giữ nguyên thẻ, thu còn 68%
rep("for (let k = 0; k < 4; k++) M(box(1.18, .025, .13), k % 2 ? C.thatch : C.thatchD, 0, 0, sz * (-.16 + k * .105), { p: r2 }); }",
    "for (let k = 0; k < 4; k++) M(box(1.18, .025, .13), k % 2 ? C.thatch : C.thatchD, 0, k * .007, sz * (-.16 + k * .105), { p: r2 }); }   /* tấm sau cao hơn tấm trước một chút: hết nhấp nháy */")
rep("function fuiSet(html){", "let FUIT = 0, FUIDN = 0; function fuiSet(html){ FUIT = performance.now();")
rep("FUI.addEventListener('click', e => { const b = e.target.closest('[data-f]'); if (!b) return; e.stopPropagation();",
    "FUI.addEventListener('pointerdown', () => { FUIDN = performance.now(); }, true); FUI.addEventListener('click', e => { const b = e.target.closest('[data-f]'); if (!b) return; e.stopPropagation(); if (b.closest('.fcard') && FUIDN < FUIT + 120) return;")   # cú bấm bắt đầu trước khi thẻ cá hiện thì bỏ qua
rep("const BUILD = 'v110c'", "const BUILD = 'v110d'")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
