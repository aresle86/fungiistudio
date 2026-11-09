# fix122: hai lỗi anh Ares bắt trên điện thoại (9/11). Chạy sau bal121.py.
# 1) Chợ › Bán: bấm nút "1" liên tục thì khựng, nhiều lần bấm mất. Do đoạn chống phóng to khi chạm đúp chặn mọi lần chạm
#    thứ hai trong 0,32 giây (preventDefault ở touchend làm trình duyệt không bắn click). Chừa nút ra, chống phóng to trên nút
#    bằng touch-action: manipulation.
# 2) Kho đầy: đặt ngón lên liếp chín thì khoá kéo màn hình và cầm liềm, mà hái không được; vườn nhiều liếp chín thì
#    không kéo đi đâu được. Nay kho không đủ chỗ cho vụ đó thì liếp chín không khoá màn hình, không cầm liềm.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a))
    s = s.replace(a, b)

rep("if (n - lastT < 320 && !e.target.closest('input,textarea')) e.preventDefault(); lastT = n;",
    "if (n - lastT < 320 && !e.target.closest('input,textarea,button,[data-a],a,label,select')) e.preventDefault(); lastT = n;")
rep(".btn{appearance:none;", "button,[data-a],.btn{touch-action:manipulation} .btn{appearance:none;")
rep("const gk = VISIT || wg ? null : gaHit(e.clientX, e.clientY), id = gk || wg ? null : plotHit(e.clientX, e.clientY), need = SAP ? null : wg ? 'weed' : id && needOf(id);",
    "const gk = VISIT || wg ? null : gaHit(e.clientX, e.clientY), id = gk || wg ? null : plotHit(e.clientX, e.clientY), need0 = SAP ? null : wg ? 'weed' : id && needOf(id), need = need0 === 'cut' && !cutRoom(id) ? null : need0;")
rep("let TAPT = 0;", "function cutRoom(id){ try { return harvestN(ST.plots[id]) <= kCap() - kUsed(); } catch (e) { return true; } } let TAPT = 0;")
s = s.replace("BUILD = 'v121a'", "BUILD = 'v122a'")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
