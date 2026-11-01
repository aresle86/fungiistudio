# QC v84c: lỗi logic nhỏ đã xác minh bằng code (chạy sau v84, v84b).
import sys
P = sys.argv[1] if len(sys.argv) > 1 else 'live/vuon3d.html'
s = open(P, encoding='utf-8').read(); log = []
def rep(old, new, n=1, tag=''):
    global s
    c = s.count(old)
    if c != n: sys.exit(f'FAIL [{tag}] khớp {c} lần, cần {n}: {old[:80]!r}')
    s = s.replace(old, new); log.append(tag)

# Trồng cây trái: đòi đủ xu dù đang có cây giống Ngoại tặng
rep("if (!y || !c || !c.tree || !unlocked(k)) return; if (ST.xu < c.seed) return toast(",
    "if (!y || !c || !c.tree || !unlocked(k)) return; if (!((ST.seeds[k] || 0) > 0) && ST.xu < c.seed) return toast(", tag='cây giống tặng')

# Vú sữa, trầu cau: kho đầy vẫn khóa cả ngày; giới hạn nói bằng bark (hay bị nuốt) thay vì toast
rep("if (F.fd === dayKey()) return bark('Hôm nay hái rồi, mai cây ra trái tiếp.'); const n = Math.max(0, Math.min(2, 6 - (ST.inv.vusua || 0))); F.fd = dayKey(); if (!n) return bark('Còn trái vú sữa trong kho, đem biếu bạn bè trước nghe.');",
    "if (F.fd === dayKey()) return toast('Hôm nay hái rồi, mai cây ra trái tiếp.', 'dan'); const n = Math.max(0, Math.min(2, 6 - (ST.inv.vusua || 0))); if (!n) return toast('Còn trái vú sữa trong kho, đem biếu bạn bè trước nghe.', 'dan'); F.fd = dayKey();", tag='vú sữa')
rep("if (F.fd === dayKey()) return bark('Hôm nay têm trầu rồi, mai têm tiếp.'); const n = Math.max(0, Math.min(3, 6 - (ST.inv.trau || 0))); F.fd = dayKey(); if (!n) return bark('Còn miếng trầu trong kho, đem mời khách trước nghe.');",
    "if (F.fd === dayKey()) return toast('Hôm nay têm trầu rồi, mai têm tiếp.', 'dan'); const n = Math.max(0, Math.min(3, 6 - (ST.inv.trau || 0))); if (!n) return toast('Còn miếng trầu trong kho, đem mời khách trước nghe.', 'dan'); F.fd = dayKey();", tag='trầu cau')

open(P, 'w', encoding='utf-8').write(s); print('OK', ', '.join(log))
