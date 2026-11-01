# QC v84d: giao diện màn ngang điện thoại + tên đồ trang trí bị cắt.
import sys
P = sys.argv[1] if len(sys.argv) > 1 else 'live/vuon3d.html'
s = open(P, encoding='utf-8').read(); log = []
def rep(old, new, n=1, tag=''):
    global s
    c = s.count(old)
    if c != n: sys.exit(f'FAIL [{tag}] khớp {c} lần, cần {n}: {old[:80]!r}')
    s = s.replace(old, new); log.append(tag)
rep("  .bkt.on{flex-direction:row}\n}\n</style>",
    "  .bkt.on{flex-direction:row}\n}\n"
    "/* QC v84: điện thoại nằm ngang (rộng > 760, thấp) — tab Sổ dọc bị tràn khỏi đáy màn hình */\n"
    "@media (min-width:761px) and (max-height:520px){\n"
    "  .bk{height:calc(100vh - 36px);height:calc(100dvh - 36px - env(safe-area-inset-bottom,0px));margin-top:0}\n"
    "  .bklab{display:none}\n"
    "  .bktabs{top:6px;gap:3px}\n"
    "  .bkt.on{width:88px;height:62px;font-size:12px}.bkt.on img{width:38px;height:38px}\n"
    "  .bkt.off{width:62px;height:48px;font-size:0}.bkt.off img{width:32px;height:32px}\n"
    "}\n"
    "/* tên đồ trang trí dài (Chuồng gà giàn thiên lý…) được xuống dòng thay vì bị cắt */\n"
    ".dcr .sn b{white-space:normal;line-height:1.15}\n"
    "</style>", tag='css màn ngang + tên trang trí')
open(P, 'w', encoding='utf-8').write(s); print('OK', ', '.join(log))
