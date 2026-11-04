# v110d (anh Ares 4/11 tối)
#  1. "còn 1 giờ 23.8342499 phút": fmtMin không làm tròn phút lẻ → làm tròn.
#  2. Thẻ việc (LÀM LIỀN / NGOẠI NHỜ) to quá: gọn lại, bỏ hộp lồng trong hộp, bỏ nhãn CẤP, chữ và icon nhỏ hơn.
#  3. Mái chuồng vịt (bậc 12 con) nhấp nháy: các tấm lá chồng mí cùng độ cao → nâng mỗi tấm một chút.
#  4. Câu được cá mà thẻ biến mất liền (người chơi đang bấm kéo nên bấm trúng nút "Cất vô kho" ngay): khóa nút 1,2 giây sau khi thẻ hiện.
# Dùng: python3 fix110d.py live/v110c.html live/v110d.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:80], c, n); s = s.replace(a, b)

rep("const fmtMin = m => m >= 60 ?", "const fmtMin = m => (m = Math.round(m), m >= 60) ?")
rep(".nxq{display:block!important;max-width:none!important;width:min(300px,calc(100vw - 110px))!important;padding:16px 8px 6px!important;border-radius:16px!important}",
    ".nxq{display:block!important;max-width:none!important;width:min(250px,calc(100vw - 120px))!important;padding:14px 10px 6px!important;border-radius:14px!important}\n.nxq .q.one{background:none!important;border:0!important;box-shadow:none!important;padding:0!important}\n.nxq .q.one .tag{display:none!important}\n.nxq .q.one>img{width:28px!important;height:28px!important}\n.nxq .q.one .qt{gap:3px!important}\n.nxq .q.one .qt>b{font-size:12px!important}\n.nxq .q.one .bar{height:10px!important}\n.nxq .q.one .bar em{font-size:9px!important}\n.nxq .nqd2{margin-top:4px!important;font-size:11px!important}")
rep("for (let k = 0; k < 4; k++) M(box(1.18, .025, .13), k % 2 ? C.thatch : C.thatchD, 0, 0, sz * (-.16 + k * .105), { p: r2 }); }",
    "for (let k = 0; k < 4; k++) M(box(1.18, .025, .13), k % 2 ? C.thatch : C.thatchD, 0, k * .007, sz * (-.16 + k * .105), { p: r2 }); }   /* tấm sau cao hơn tấm trước một chút: hết nhấp nháy */")
rep("function fuiSet(html){", "function fuiSet(html){ setTimeout(() => { const c = FUI && FUI.querySelector('.fcard'); if (c && !c.dataset.lk){ c.dataset.lk = 1; c.classList.add('lock'); setTimeout(() => c.classList.remove('lock'), 1200); } }, 0);")
rep("</style><style id=\"s108\">", "</style><style id=\"s108\">\n.fui .fcard.lock .btn{pointer-events:none;opacity:.55}")
rep("const BUILD = 'v110c'", "const BUILD = 'v110d'")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
