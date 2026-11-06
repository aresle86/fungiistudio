/* Theo dõi lúc mở: có lỗi mà màn tải đứng yên thì tự tải lại một lần, vẫn đứng thì hiện nút Tải lại. */
(function(){ var errs = [], stallT = 0;
  var pct = function(){ var b = document.querySelector('#load .lbar i'); return b ? +b.dataset.p || 0 : 0; };
  var msg = function(){ return errs.length ? 'Lỗi: ' + errs[errs.length - 1] : 'Chưa dựng xong sau 15 giây.'; };
  function btn(){ var s = document.querySelector('#load small'); if (!s || document.getElementById('ldRe')) return; var b = document.createElement('button'), en = false; try { en = localStorage.getItem('mv2-lang') === 'en'; } catch (e) {} b.id = 'ldRe'; b.type = 'button'; b.textContent = en ? 'Reload' : 'Tải lại'; b.style.cssText = "display:block;margin:12px auto 0;min-height:44px;padding:8px 26px;border:0;border-radius:999px;background:#5f3a1e;color:#fff7e6;font:700 17px 'Baloo 2',sans-serif;pointer-events:auto;cursor:pointer"; b.addEventListener('click', function(){ location.reload(); }); s.parentNode.insertBefore(b, s.nextSibling); }
  function stall(){ if (window.__ready) return; var t = 0, now = Date.now(); try { t = +sessionStorage.getItem('mv2-ldre') || 0; } catch (e) {} if (now - t > 120000){ var ok = false; try { sessionStorage.setItem('mv2-ldre', String(now)); ok = true; } catch (e) {} if (ok){ location.reload(); return; } } btn(); }
  function note(m){ errs.push(String(m).slice(0, 160)); var s = document.querySelector('#load small'); if (s) s.textContent = msg(); if (window.__ready) return; var p = pct(); clearTimeout(stallT); stallT = setTimeout(function(){ if (pct() === p) stall(); }, 10000); }
  window.addEventListener('error', function(e){ note(e.message || (e.target && e.target.src ? 'Không tải được ' + e.target.src : 'lỗi không rõ')); }, true);
  window.addEventListener('unhandledrejection', function(e){ note(e.reason && (e.reason.message || e.reason)); });
  setTimeout(function(){ if (window.__ready) return; var s = document.querySelector('#load small'); if (!s) return;
    var gl2 = false; try { gl2 = !!document.createElement('canvas').getContext('webgl2'); } catch (e) {}
    var ua = navigator.userAgent.match(/OS (\d+)_(\d+)/); var ios = ua ? ' · iOS ' + ua[1] + '.' + ua[2] : '';
    s.textContent = msg() + ' · WebGL2: ' + (gl2 ? 'có' : 'không') + ios; setTimeout(function(){ if (!window.__ready) btn(); }, 15000); }, 15000); })();
