# v136a: iPhone rút bộ vẽ hình (máy nóng, nhiều tab, chuyển app) thì không hiện lỗi đáng sợ nữa.
# Ngừng vẽ, lưu vườn, hiện lời nhẹ nhàng + nút "Mở lại vườn"; máy trả bộ vẽ hình thì tự mở lại.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v136'", "BUILD = 'v136a'")
# lời nhắc khi mất bộ vẽ hình; lỗi vẽ đi kèm thì không hiện hộp "Có lỗi khi dựng cảnh"
rep("window.addEventListener('error', e => { showErr('Có lỗi khi dựng cảnh: ' + (e.message || e));",
    "const glLostMsg = () => { if (window.__glMsg) return; window.__glMsg = 1; let en = false; try { en = !!EN; } catch (x) {} const e = $('#err'); e.textContent = en ? 'Your phone needed a little rest, so the garden stopped drawing. Everything is saved.' : 'Máy cần nghỉ chút nên vườn tạm ngừng vẽ. Đồ đạc vẫn còn nguyên.'; e.style.display = 'block'; const b = document.createElement('button'); b.className = 'btn'; b.style.minHeight = '44px'; b.textContent = en ? 'Reopen garden' : 'Mở lại vườn'; b.addEventListener('click', () => location.reload()); e.appendChild(b); };\n"
    "const glLostErr = m => /WebGLShader|WebGLProgram|context (was )?lost|CONTEXT_LOST/i.test(String(m || ''));\n"
    "window.addEventListener('error', e => { if (window.__glLost || glLostErr(e.message)){ window.__glLost = 1; glLostMsg(); errSend('GL lost: ' + String(e.message || '').slice(0, 120)); return; } showErr('Có lỗi khi dựng cảnh: ' + (e.message || e));")
rep("new T.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });",
    "new T.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });\n"
    "canvas.addEventListener('webglcontextlost', e => { e.preventDefault(); window.__glLost = 1; try { save(); } catch (x) {} glLostMsg(); try { errSend('GL lost (event)'); } catch (x) {} }, false);\n"
    "canvas.addEventListener('webglcontextrestored', () => { try { save(); } catch (x) {} location.reload(); }, false);")
# mất bộ vẽ hình thì vòng vẽ đứng yên, không quăng lỗi liên tục
rep("function tickIn(){ const dt = Math.min(clock.getDelta(), .05)", "function tickIn(){ if (window.__glLost) return; const dt = Math.min(clock.getDelta(), .05)")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
