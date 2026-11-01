# QC v84e: mục "Bản thử nghiệm" chỉ hiện khi URL có ?dev (theo anh Ares chốt 1/11).
import sys
P = sys.argv[1] if len(sys.argv) > 1 else 'live/vuon3d.html'
s = open(P, encoding='utf-8').read(); log = []
def rep(old, new, n=1, tag=''):
    global s
    c = s.count(old)
    if c != n: sys.exit(f'FAIL [{tag}] khớp {c} lần, cần {n}: {old[:80]!r}')
    s = s.replace(old, new); log.append(tag)
rep('h += `<details class="dev"', 'if (DEVQ) h += `<details class="dev"', tag='ẩn Bản thử nghiệm')
# Người đã lỡ bật ×60 hay xem thử Tết thì tắt được nữa → không có ?dev thì trả về bình thường lúc tải
rep("function sheetSoft(){",
    "const DEVQ = /[?&]dev\\b/.test(location.search); if (!DEVQ && !VISIT){ try { if (ST.spd > 1) ST.spd = 1; if (ST.muaTest){ ST.muaTest = null; ST.tetDayTest = null; } } catch (e) {} }\nfunction sheetSoft(){", tag='reset cờ thử nghiệm')
open(P, 'w', encoding='utf-8').write(s); print('OK', ', '.join(log))
