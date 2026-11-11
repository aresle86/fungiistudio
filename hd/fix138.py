# v138: giảm nóng máy điện thoại (anh Ares đo iPhone 14 Pro 11/11: v137 mức Vừa 53,6 khung/giây, 5,2 ms mỗi khung, 408 lượt vẽ).
# Máy dư sức, nóng vì vẽ liên tục gần 60 khung/giây. Bóng đổ đã vẽ thưa (160 ms) từ trước, không đổi.
# (1) Điện thoại ở mức Thấp/Vừa: lúc đang chạm vẽ ~40 khung/giây (2 trên 3 nhịp màn hình), mức Cao giữ 60.
# (2) Điện thoại mức Vừa: độ nét ×1,5 → ×1,3. Máy tính giữ nguyên.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v137'", "BUILD = 'v138'")
rep(": PIN ? 30 : MOBILE ? 15 : 0;   /* v130: tiết kiệm pin thì 30 khung/giây */ if (gap && fn - FRL < gap){ requestAnimationFrame(tick); return; } FRL = fn;",
    ": PIN ? 30 : MOBILE ? (QI >= 2 ? 15 : 25) : 0, g40 = !idle && gap === 25;   /* v130: tiết kiệm pin thì 30 khung/giây; v138: điện thoại mức Thấp/Vừa ~40 khung/giây lúc đang chạm */ if (gap && fn - FRL < gap - (g40 ? 5 : 0)){ requestAnimationFrame(tick); return; } FRL = g40 && fn - FRL < gap * 2 ? FRL + gap : fn;")
rep("{ pr: Math.min(devicePixelRatio, 1.5), sh: 2048, fx: .75 }", "{ pr: Math.min(devicePixelRatio, MOBILE ? 1.3 : 1.5), sh: 2048, fx: .75 }")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
