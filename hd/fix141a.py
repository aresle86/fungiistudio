# v141a: thẻ "Việc tiếp theo" — dòng "còn 1655 kinh nghiệm" tràn ra ngoài thẻ (hình anh Ares 12/11, cấp 17).
# Anh chọn ghi phần trăm cho gọn: "được 12%" thay cho "còn 1655 kinh nghiệm" (khớp với thanh, không ghi số cấp).
# Phòng xa: chữ nào không vừa cạnh thanh thì xuống dòng dưới thanh, không tràn ra ngoài thẻ.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v141'", "BUILD = 'v141a'")
rep(".nxq .pbar{display:flex;align-items:center;gap:6px;margin-top:3px;width:100%}", ".nxq .pbar{display:flex;flex-wrap:wrap;align-items:center;gap:3px 6px;margin-top:3px;width:100%;min-width:0}")
rep(".nxq .pbar>em{font:700 12px/1 var(--f-body,'Baloo 2'),sans-serif;", ".nxq .pbar>em{max-width:100%;font:700 12px/1.15 var(--f-body,'Baloo 2'),sans-serif;")
rep(".nxq .q .stp{", ".nxq .pbar>em{white-space:normal!important}\n.nxq .q .stp{")
rep("t = 'Chăm vườn thêm'; em = `còn ${need - xp} kinh nghiệm`; f = (xp - prev) / (need - prev); }",
    "t = 'Chăm vườn thêm'; f = (xp - prev) / (need - prev); em = `được ${Math.max(0, Math.min(100, Math.floor(f * 100)))}%`; }")
rep('["^Về vườn ngày (\\\\d+)/7$", "Back at the garden: day $1/7"]', '["^Về vườn ngày (\\\\d+)/7$", "Back at the garden: day $1/7"], ["^được (\\\\d+)%$", "$1% there"]')
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
