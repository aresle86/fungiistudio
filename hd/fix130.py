# -*- coding: utf-8 -*-
# v130 sau v129: đợt 2 "Vững", phần 2 (giảm nóng máy).
# Số đo iPhone 14 Pro của anh Ares (Đồ hoạ Cao, ×1.8, bóng 4096): 56-57 khung hình/giây, vẽ 4.8 ms mỗi khung, game không phải tự hạ hình.
# Tức là máy dư sức, nóng là do vẽ đủ 60 khung/giây ở mức hình cao suốt lúc chơi, không phải do giật.
# 1. Cài đặt có nút "Tiết kiệm pin" (mặc định tắt): vẽ 30 khung/giây, điểm ảnh tối đa ×1.5, bóng tối đa 2048, lúc không chạm thì nghỉ sớm hơn.
# 2. Trên điện thoại đang chọn Đồ hoạ Cao: có dòng nhắc Cao làm máy ấm nhanh hơn.
# 3. Kết quả Đo máy ghi thêm "tiết kiệm pin" khi đang bật; lời khen "mượt" tính theo mốc 30 khi bật.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v129'", "BUILD = 'v130'")

# ---------- 1. tiết kiệm pin ----------
rep("""let QI = +(store.get('mv3d-q') ?? (MOBILE ? 1 : 2)); if (!(QI >= 0 && QI <= 2)) QI = 1;""",
    """let QI = +(store.get('mv3d-q') ?? (MOBILE ? 1 : 2)); if (!(QI >= 0 && QI <= 2)) QI = 1;
let PIN = store.get('mv3d-pin') === '1';   /* v130: tiết kiệm pin, người chơi tự bật trong Cài đặt */""")
rep("""if (L >= 1 && q.sh > 1024) q.sh = 1024;""", """if (PIN){ q.pr = Math.min(q.pr, 1.5); if (q.sh > 2048) q.sh = 2048; } if (L >= 1 && q.sh > 1024) q.sh = 1024;""")
rep("""gap = idle ? (fn - FRH > 60000 ? 80 : AQ.lv >= 1 || fn - FRH > 8000 ? 45 : 30) : MOBILE ? 15 : 0;""",
    """gap = idle ? (fn - FRH > 60000 ? 80 : PIN || AQ.lv >= 1 || fn - FRH > 8000 ? 45 : 30) : PIN ? 30 : MOBILE ? 15 : 0;   /* v130: tiết kiệm pin thì 30 khung/giây */""")
rep("""    h += dmHTML();
""", """    h += `<div class="acts"><span class="meta" style="min-width:64px">${DML('Pin', 'Battery')}</span><button class="btn${PIN ? ' g' : ''}" data-a="pin" aria-pressed="${PIN}">${PIN ? DML('Tiết kiệm pin: bật', 'Battery saver: on') : DML('Tiết kiệm pin: tắt', 'Battery saver: off')}</button></div><div class="meta">${PIN ? DML('Đang vẽ 30 khung hình mỗi giây, hình bớt nét một chút. Máy mát hơn, pin lâu hơn.', 'Drawing 30 frames per second with slightly softer graphics. The phone stays cooler and the battery lasts longer.') : MOBILE && QI === 2 ? DML('Đồ hoạ Cao làm máy ấm nhanh hơn. Muốn mát máy thì chọn Vừa hoặc bật Tiết kiệm pin.', 'High graphics warm the phone faster. To keep it cool, choose Medium or turn on Battery saver.') : DML('Chơi lâu thấy máy ấm thì bật lên: game vẽ nhẹ lại, máy mát hơn, pin lâu hơn.', 'If the phone gets warm in long sessions, turn this on: the game draws less, the phone stays cooler and the battery lasts longer.')}</div>`;
    h += dmHTML();
""")
rep("""  else if (a === 'q'){ QI = +b.dataset.v;""", """  else if (a === 'pin'){ PIN = !PIN; store.set('mv3d-pin', PIN ? '1' : '0'); applyQ(); }
  else if (a === 'q'){ QI = +b.dataset.v;""")

# nút Đồ hoạ đang chọn tô xanh như nút Ngôn ngữ (trước giờ ba nút nhìn y nhau, không biết đang ở mức nào)
rep("""${QL.map((n, i) => `<button class="btn" data-a="q" data-v="${i}" aria-pressed="${QI === i}">""", """${QL.map((n, i) => `<button class="btn${QI === i ? ' g' : ''}" data-a="q" data-v="${i}" aria-pressed="${QI === i}">""")

# ---------- 3. đo máy biết tiết kiệm pin ----------
rep("""'Đồ hoạ: ' + QL[QI] + ' · điểm ảnh ×'""", """'Đồ hoạ: ' + QL[QI] + (PIN ? ' · tiết kiệm pin' : '') + ' · điểm ảnh ×'""")
rep("""DMR = { fps, lo, aq0: D.aq0, aq1: AQ.lv, txt };""", """DMR = { fps, lo, aq0: D.aq0, aq1: AQ.lv, txt, pin: PIN };""")
rep("""tone = f >= 50 ? DML('Máy chạy mượt', 'Runs smoothly') : f >= 30 ?""", """tone = f >= (R.pin ? 27 : 50) ? DML('Máy chạy mượt', 'Runs smoothly') : f >= (R.pin ? 20 : 30) ?""")

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
