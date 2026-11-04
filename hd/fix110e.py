# v110e — lưới thẻ trong Sổ căn theo mép trên (anh Ares 4/11): nút bấm mặc định căn giữa dọc nên ô ít thông số bị đẩy xuống,
# tên rau trồi sụt. Quy tắc: mọi ô trong một hàng bắt đầu từ cùng mép trên; hình khung cố định, tên ngay dưới, thông số không rớt dòng.
# Dùng: python3 fix110e.py live/v110d.html live/v110e.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:80], c, n); s = s.replace(a, b)
CSS = """<style id="s110e">
.stg{align-items:start!important}
.stk{display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:flex-start!important;height:auto!important}
.stk b{min-height:2.3em;line-height:1.15!important;display:flex!important;align-items:flex-start;justify-content:center}
.stk .sts{display:grid!important;grid-template-columns:auto auto;justify-content:center;column-gap:8px;row-gap:2px;transform:none!important;margin:0!important}
.stk .sts .st:nth-child(3){grid-column:1/-1;justify-self:center}   /* luôn 2 hàng: giá + thời gian, rồi sản lượng */
.stk .sts .st{white-space:nowrap}
</style>"""
i = s.rfind('</style>'); s = s[:i + 8] + CSS + s[i + 8:]
rep("const BUILD = 'v110d'", "const BUILD = 'v110e'")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
