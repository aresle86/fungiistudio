# en115: biển gỗ trong cảnh, chữ bay, chữ cạnh túi xu và thẻ kỷ niệm cũng dịch tiếng Anh. python3 en115.py vào ra
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
rep("lines.forEach(([t, f, col, yy]) => { g.font = f;","lines.forEach(([t0, f, col, yy]) => { const t = fxT(t0); g.font = f;")
rep("function floatAt(x, y, z, txt, col = '#FBF7EE'){","function floatAt(x, y, z, txt, col = '#FBF7EE'){ txt = fxT(txt);")
rep("function coinPop(txt, col = '#F5D27A'){","function coinPop(txt, col = '#F5D27A'){ txt = fxT(txt);")
rep("x.fillText('Ba mươi bữa ở vườn Ngoại', W / 2, 82);","x.fillText(fxT('Ba mươi bữa ở vườn Ngoại'), W / 2, 82);")
rep("x.fillText('Vườn nhà mình sau ba mươi bữa', 0, 262);","x.fillText(fxT('Vườn nhà mình sau ba mươi bữa'), 0, 262);")
rep("x.fillText(`Vườn ${ST.player.garden || ''} · Kỷ niệm ngày thứ 30`, W / 2, 126);","x.fillText(EN ? `${ST.player.garden || ''} garden · Day 30 keepsake` : `Vườn ${ST.player.garden || ''} · Kỷ niệm ngày thứ 30`, W / 2, 126);")
rep("<small>Về đủ bảy ngày liền có quà lớn. Vắng một ngày là thẻ làm lại từ đầu.</small>`; el.classList.add('on');","<small>Về đủ bảy ngày liền có quà lớn. Vắng một ngày là thẻ làm lại từ đầu.</small>`; if (EN) enWalk(el); el.classList.add('on');")
open(dst,'w',encoding='utf-8').write(s)
