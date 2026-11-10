# -*- coding: utf-8 -*-
# v129 sau v128: đợt 2 "Vững", phần 1.
# 1. Cài đặt có nút "Đo máy": đo 30 giây (khung hình/giây, thời gian vẽ, hình có tự hạ không, tên máy), rồi "Chép kết quả".
#    Kết quả chỉ nằm trên máy người chơi, không gửi đi đâu. Trong lúc đo, vòng vẽ giữ nhịp như đang chơi (không ngủ nghỉ).
# 2. Túi hạt đậm màu hơn (bong bóng gieo, thẻ Ngoại chỉ, nút Hạt) cho khỏi chìm vào nền kem.
# 3. Tiếng Anh: chữ tab Sổ và chữ "coins" lên 12px; thêm 2 câu còn sót tiếng Việt.
# 4. Sổ trên điện thoại: hàng tab lùi vô, không còn bị nút đóng đè góc.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v128'", "BUILD = 'v129'")

# ---------- 1. đo máy ----------
rep("""  else { AQ.bad = 0; if (fps > cap * .85){ if (++AQ.good >= 30){ AQ.good = 0; aqSet(AQ.lv - 1); } } else AQ.good = 0; } }
""", """  else { AQ.bad = 0; if (fps > cap * .85){ if (++AQ.good >= 30){ AQ.good = 0; aqSet(AQ.lv - 1); } } else AQ.good = 0; } }
/* v129: đo máy. Kết quả chỉ nằm trên máy này (bộ nhớ trang), người chơi tự chép rồi dán gửi. */
var DM = null, DMR = null; const DML = (vi, en) => EN ? en : vi, DMSEC = 30;
function dmPill(){ let p = document.getElementById('dmp'); if (!DM){ if (p) p.hidden = true; return; } if (!p){ p = document.createElement('div'); p.id = 'dmp'; p.className = 'tst'; p.setAttribute('role', 'status'); document.body.appendChild(p); }
  const left = Math.max(0, DMSEC - DM.sec.length); p.hidden = false; p.textContent = DML('Đang đo máy, còn ' + left + ' giây', 'Measuring… ' + left + ' s left'); }
function dmStart(){ if (DM) return; closeSheet(); const now = performance.now(); DM = { t0: now, n: 0, sec: [], sn: 0, st: now, ms: 0, mx: 0, raf: 0, aq0: AQ.lv }; dmPill(); }
function dmStop(){ if (!DM) return; DM = null; dmPill(); toast(DML('Đo bị ngắt giữa chừng, con đo lại nghe', 'Measuring was interrupted, please run it again'), 'lo'); }
addEventListener('visibilitychange', () => { if (document.hidden) dmStop(); });
function dmFrame(fn){ const D = DM, ms = performance.now() - fn; D.n++; D.ms += ms; if (ms > D.mx) D.mx = ms; D.sn++;
  if (fn - D.st >= 1000){ D.sec.push(Math.round(D.sn * 1000 / (fn - D.st))); D.sn = 0; D.st = fn; dmPill(); } if (D.sec.length >= DMSEC) dmEnd(fn); }
function dmEnd(fn){ const D = DM; DM = null; dmPill(); const el = (fn - D.t0) / 1000, q = aqQ(), f1 = v => Math.round(v * 10) / 10; let gpu = '', inf = { calls: 0, tri: 0, geo: 0, tex: 0 };
  try { const g = r.getContext(), e = g.getExtension('WEBGL_debug_renderer_info'); gpu = String(e ? g.getParameter(e.UNMASKED_RENDERER_WEBGL) : g.getParameter(g.RENDERER)); } catch (e) {}
  try { inf = { calls: r.info.render.calls, tri: r.info.render.triangles, geo: r.info.memory.geometries, tex: r.info.memory.textures }; } catch (e) {}
  let beds = 0, open = 0; try { for (const k in ST.plots){ open++; if (ST.plots[k].crop) beds++; } } catch (e) {}
  const fps = D.n / el, lo = Math.min(...D.sec), raf = D.raf / el;
  const txt = ['Miệt Vườn ' + BUILD + ' · đo máy ' + Math.round(el) + ' giây',
    'Khung hình/giây: trung bình ' + f1(fps) + ' · thấp nhất ' + lo + ' · màn hình ' + Math.round(raf),
    'Vẽ 1 khung: trung bình ' + f1(D.ms / D.n) + ' ms · lâu nhất ' + Math.round(D.mx) + ' ms',
    'Hình tự hạ: bậc ' + D.aq0 + ' → ' + AQ.lv + (AQ.log.length ? ' · nhật ký ' + AQ.log.slice(-6).map(x => x[0] + 's:' + x[1] + '>' + x[2] + '@' + x[3]).join(' ') : ''),
    'Đồ hoạ: ' + QL[QI] + ' · điểm ảnh ×' + f1(q.pr) + ' · bóng ' + q.sh,
    'Cảnh: ' + inf.calls + ' lượt vẽ · ' + Math.round(inf.tri / 1000) + ' nghìn tam giác · ' + inf.geo + ' khối · ' + inf.tex + ' ảnh',
    'Màn hình: ' + innerWidth + '×' + innerHeight + ' ×' + f1(devicePixelRatio || 1),
    'Mở game được ' + Math.round(fn / 60000) + ' phút · ' + beds + '/' + open + ' liếp có cây',
    'Máy: ' + (gpu || '?') + ' · ' + navigator.userAgent].join('\\n');
  DMR = { fps, lo, aq0: D.aq0, aq1: AQ.lv, txt }; openSheet('set'); setTimeout(() => { try { document.getElementById('dmr').scrollIntoView({ block: 'center' }); } catch (e) {} }, 60); }
function dmCopy(){ if (!DMR) return; const ok = () => toast(DML('Đã chép kết quả', 'Result copied')), old = () => { try { const ta = document.createElement('textarea'); ta.value = DMR.txt; ta.setAttribute('readonly', ''); ta.style.cssText = 'position:fixed;left:0;top:0;opacity:0'; document.body.appendChild(ta); ta.select(); ta.setSelectionRange(0, 99999); const k = document.execCommand('copy'); ta.remove(); if (!k) throw 0; ok(); }
    catch (e) { const d = document.getElementById('dmd'); if (d) d.open = true; toast(DML('Máy không cho chép tự động. Con nhấn giữ vô chữ bên dưới để chép nghe', 'Could not copy automatically. Press and hold the text below to copy it'), 'lo'); } };
  try { navigator.clipboard.writeText(DMR.txt).then(ok, old); } catch (e) { old(); } }
function dmHTML(){ const R = DMR; let h = `<div class="acts"><span class="meta" style="min-width:64px">${DML('Máy', 'Device')}</span><button class="btn" data-a="domay">${R ? DML('Đo lại', 'Measure again') : DML('Đo máy', 'Measure device')}</button></div>`;
  if (!R) return h + `<div class="meta">${DML('Máy nóng hay giật? Đo 30 giây rồi chép kết quả, dán vô Báo lỗi, góp ý. Kết quả chỉ nằm trên máy con.', 'Phone running hot or choppy? Measure for 30 seconds, copy the result and paste it into Report a bug. The result stays on your device.')}</div>`;
  const f = Math.round(R.fps), tone = f >= 50 ? DML('Máy chạy mượt', 'Runs smoothly') : f >= 30 ? DML('Máy chạy tạm được', 'Runs okay') : DML('Máy chạy nặng', 'Runs heavy');
  return h + `<div class="dmr" id="dmr"><b>${f} ${DML('khung hình/giây', 'frames per second')}</b><span>${tone} · ${DML('chậm nhất', 'lowest')} ${R.lo}${R.aq1 > R.aq0 ? ' · ' + DML('game đã tự hạ hình cho nhẹ máy', 'the game lowered graphics to keep up') : ''}</span><div class="acts"><button class="btn g" data-a="dmcopy">${DML('Chép kết quả', 'Copy result')}</button></div><details class="uxm" id="dmd"><summary>${DML('Xem chi tiết', 'Show details')}</summary><div class="dmt">${esc(R.txt)}</div></details></div>`; }
""")
rep("""function tick(){ const fn = performance.now(), idle = MOBILE""", """function tick(){ const fn = performance.now(); if (DM){ DM.raf++; FRH = fn + 1500; }   /* v129: đang đo máy thì giữ nhịp vẽ như lúc đang chơi */ const idle = MOBILE""")
rep("""FRL = fn; aqTick(fn, gap); try { tickIn(); } catch (e) {""", """FRL = fn; aqTick(fn, gap); try { tickIn(); if (DM) dmFrame(fn); } catch (e) {""")
rep("""aria-pressed="${QI === i}">${n}</button>`).join('')}</div>`;
    h += `<div class="sub">Ngôn ngữ · Language</div>""", """aria-pressed="${QI === i}">${n}</button>`).join('')}</div>`;
    h += dmHTML();
    h += `<div class="sub">Ngôn ngữ · Language</div>""")
rep("""  else if (a === 'q'){ QI = +b.dataset.v;""", """  else if (a === 'domay'){ dmStart(); return; } else if (a === 'dmcopy'){ dmCopy(); return; }
  else if (a === 'q'){ QI = +b.dataset.v;""")

# ---------- 2. túi hạt đậm hơn ----------
rep("""lg.computeVertexNormals(); M(lg, X('#D8AE72'), 0, 0, 0, { p: g });""", """lg.computeVertexNormals(); M(lg, X('#B9803F'), 0, 0, 0, { p: g });   /* v129: vải bố đậm hơn, khỏi chìm vào nền kem */""")
rep("""M(t, X('#C29560'), 0, y, 0, { p: g, r: [Math.PI / 2, 0, 0], cast: false }); }   /* thớ vải */""", """M(t, X('#8F5F2C'), 0, y, 0, { p: g, r: [Math.PI / 2, 0, 0], cast: false }); }   /* thớ vải */""")

# ---------- 3. tiếng Anh ----------
rep("""html[lang=en] .bkt span{font-size:11px!important;letter-spacing:-.01em} html[lang=en] .coin small{font-size:10px!important}""",
    """html[lang=en] .bkt span{font-size:12px!important;letter-spacing:-.02em} html[lang=en] .coin small{font-size:12px!important}""")
rep("""const UIEN = {"Buồng thay đồ · sửa soạn về vườn Ngoại":""",
    """const UIEN = {"Xong rồi, nhận thưởng nè": "Done, claim your reward", "Mỗi lu chứa thêm 20 món tươi. Mỗi kệ tre chứa thêm 10 món khô, món nấu. Kho nào đầy thì món đó không cất được nữa.": "Each jar holds 20 more fresh items. Each bamboo shelf holds 10 more dried goods and dishes. When a store is full, nothing more of that kind fits.", "Buồng thay đồ · sửa soạn về vườn Ngoại":""")

# ---------- 4. kiểu ----------
rep("""</style><style id="s110e">""", """
/* v129 */
@media (max-width:560px){ .bktabs{right:46px!important} }   /* hàng tab Sổ lùi vô, nút đóng không đè góc tab */
#dmp{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(env(safe-area-inset-bottom,0px) + 26px);z-index:80;pointer-events:none;white-space:nowrap}   /* giữa đáy màn hình: không đè xu, thẻ Ngoại chỉ, nút hai bên */
.dmr{margin-top:8px;padding:12px 14px;background:#FBF7EE;border-radius:var(--r2);box-shadow:0 3px 0 #E3D3BC}
.dmr>b{display:block;font:400 20px/1.2 var(--f-game);color:#4A2F1E}.dmr>span{display:block;font-size:14px;font-weight:600;color:#8A5D3B;line-height:1.35;margin-top:2px}
.dmr .dmt{padding:0 12px 10px;font:600 12px/1.5 var(--f-body);color:#6B4529;white-space:pre-wrap;overflow-wrap:anywhere;-webkit-user-select:text;user-select:text}
</style><style id="s110e">""")

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
