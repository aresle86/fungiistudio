# perf115: điện thoại đỡ nóng. Lúc không chạm vẽ 30 hình/giây, bóng cập nhật thưa hơn. python3 perf115.py live/v115_1d.html live/v115_1e.html
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
rep("function tick(){ try { tickIn(); } catch (e) {","let FRL = 0, FRH = 0; addEventListener('pointerdown', () => { FRH = performance.now() + 1500; }, true); addEventListener('pointermove', () => { if (FRH) FRH = Math.max(FRH, performance.now() + 800); }, true);\nfunction tick(){ const fn = performance.now(); if (MOBILE && QI < 2 && !window.__stop && fn >= FRH && fn - FRL < 28){ requestAnimationFrame(tick); return; } FRL = fn; try { tickIn(); } catch (e) {")
rep("if (QI < 2 && (SHF = (SHF + 1) % 2) === 0) r.shadowMap.needsUpdate = true;","if (QI < 2 && (SHF = (SHF + 1) % (MOBILE ? 4 : 2)) === 0) r.shadowMap.needsUpdate = true;")
open(dst,'w',encoding='utf-8').write(s)
