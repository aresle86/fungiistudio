#!/usr/bin/env python3
"""v102: bỏ cầu ván chuồng vịt (thò ra đất, đè lò ấp) thay bằng thau nước; thanh Sửa vườn không đè bảng; nút cho ăn ghi rõ đổ đầy máng."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep("    for (let k = 0; k < 7; k++) M(box(.07, .018, .3), k % 2 ? '#B48560' : '#A07450', -.62 - k * .075, .06 - k * .03, .05, { p: up1, r: [0, 0, -.38] });   /* cầu ván tre thả xuống mương cho vịt lội */\n",
    "    M(new T.CylinderGeometry(.16, .13, .07, 12), '#8A6A4A', .74, .035, .46, { p: up1 }); M(new T.CylinderGeometry(.14, .14, .01, 12), '#7FB6C9', .74, .066, .46, { p: up1, cast: false });   /* thau nước cho vịt vầy */\n")
rep("    for (const z2 of [-.11, .21]) M(cyl(.012, .014, .62, 4), '#8A5D3B', -.8, .0, z2, { p: up1, r: [0, 0, Math.PI / 2 - .38], cast: false });\n", "")
rep("sub: food >= tcap ? '' : rm ? `dùng ${rm} bó rau muống` : `mua cám ${VIT.cam} xu/phần` })",
    "sub: food >= tcap ? '' : rm ? `đổ đầy máng · ${rm} bó rau muống` : `mua cám ${VIT.cam} xu/phần` })")
rep("sub: food >= tcap ? '' : bap ? `dùng ${bap} bắp trong kho` : `mua cám ${GA.cam} xu/phần` })",
    "sub: food >= tcap ? '' : bap ? `đổ đầy máng · ${bap} trái bắp` : `mua cám ${GA.cam} xu/phần` })")
i = s.rindex('</style>'); s = s[:i] + "\nbody.sheeton #suaBar{display:none!important}   /* bảng đang mở thì ẩn thanh Sửa vườn cho khỏi đè nút */\n" + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
