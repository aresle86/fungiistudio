# aq117: máy nóng. Giữ nguyên chất lượng đồ hoạ anh chọn; game tự đo số hình mỗi giây, chỉ hạ khi máy đuối kéo dài, máy mát lại thì nâng lên.
#  Bậc 1: bóng đổ 1024 (nếu đang cao hơn), để yên thì vẽ thưa hơn (24 hình/giây trên điện thoại)
#  Bậc 2: độ nét tối đa 1,25
#  Bậc 3: độ nét 1, tắt bóng đổ
#  Đo mỗi 2 giây; 4 lần liền dưới 55% mức bình thường thì hạ một bậc; 30 lần liền (1 phút) trên 85% thì nâng một bậc.
#  Mỗi lần mở game bắt đầu lại ở chất lượng cao nhất của mức đã chọn trong Cài đặt.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:80], s.count(a))
    s = s.replace(a, b)

AQ = r"""
var AQ = { lv: 0, n: 0, t0: 0, bad: 0, good: 0, fps: 0, log: [] };
function aqQ(){ const q = { ...QS[QI] }, L = (typeof AQ === 'object' && AQ) ? AQ.lv : 0; if (L >= 1 && q.sh > 1024) q.sh = 1024; if (L >= 2) q.pr = Math.min(q.pr, 1.25); if (L >= 3){ q.pr = 1; q.sh = 0; } return q; }
function aqSet(lv){ lv = Math.max(0, Math.min(3, lv)); if (lv === AQ.lv) return; AQ.log.push([Math.round(performance.now() / 1000), AQ.lv, lv, Math.round(AQ.fps)]); if (AQ.log.length > 20) AQ.log.shift(); AQ.lv = lv; try { applyQ(); } catch (e) {} }
function aqTick(fn, idleCap){ if (document.hidden || fn < 15000){ AQ.t0 = 0; return; } if (!AQ.t0){ AQ.t0 = fn; AQ.n = 0; return; } AQ.n++; const el = fn - AQ.t0; if (el < 2000) return; const fps = AQ.n * 1000 / el; AQ.t0 = fn; AQ.n = 0; if (el > 4000) return;
  const cap = idleCap ? 1000 / idleCap : 60; AQ.fps = fps;
  if (fps < cap * .55){ AQ.bad++; AQ.good = 0; if (AQ.bad >= 4){ AQ.bad = 0; aqSet(AQ.lv + 1); } }
  else { AQ.bad = 0; if (fps > cap * .85){ if (++AQ.good >= 30){ AQ.good = 0; aqSet(AQ.lv - 1); } } else AQ.good = 0; } }
"""
i = s.find("const QS = [")
j = s.find(";", s.find("}];", i)) + 1
s = s[:j] + AQ + s[j:]
rep("function applyQ(){ const q = QS[QI];", "function applyQ(){ const q = aqQ();")
rep("r.setPixelRatio(QS[QI].pr); r.setSize(w, h, false);", "r.setPixelRatio(aqQ().pr); r.setSize(w, h, false);")
rep("function tick(){ const fn = performance.now(); if (MOBILE && QI < 2 && !window.__stop && fn >= FRH && fn - FRL < 28){ requestAnimationFrame(tick); return; } FRL = fn;",
    "function tick(){ const fn = performance.now(), idle = MOBILE && QI < 2 && !window.__stop && fn >= FRH, gap = idle ? (AQ.lv >= 1 ? 41 : 28) : 0; if (gap && fn - FRL < gap){ requestAnimationFrame(tick); return; } FRL = fn; aqTick(fn, gap);")
rep("get: () => ({ sapMode,", "get: () => ({ AQ, aqSet, aqQ, aqTick, sapMode,")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
