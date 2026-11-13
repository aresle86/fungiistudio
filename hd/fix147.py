# v147: nhãn "Mới" ở nút Hạt và nút Chợ không còn đè lên hình (anh Ares báo 13/11).
# Nút Hạt: nhãn nằm phía trên bên trái bao hạt, số hạt nằm bên phải, hai cái không chạm nhau. Nút Chợ: PC nhích lên trên mái sạp;
# điện thoại (nút Sổ nằm ngay trên) thì nhãn nằm bên trái sạp, không che chữ "Sổ".
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v146'", "BUILD = 'v147'")
A = "i.moi{font-style:normal;font:800 12px/1.3 var(--f-body);"
rep(A, "#tSeed.moi::after{top:auto;bottom:calc(100% - 7px);left:-2px;right:auto}"
    "#bCho.moi::after{top:-14px;right:-4px}"
    "@media (max-width:560px){#bCho.moi::after{top:8px;right:calc(100% - 9px)}}" + A)
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
