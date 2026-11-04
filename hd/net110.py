# v110 phần mạng (danh sách trước quảng bá A2, A3)
#  A2: ghé vườn bạn mà server từ chối thì nói đúng lý do (mã lệch / vườn không còn / bản cũ), chỉ khi mất mạng thật
#      mới nói "mạng chập chờn"; lỗi mạng (hết 9 giây, rớt kết nối) tự thử lại một lần; lưu 10 lỗi gần nhất (mv2-neterr).
#  A3: mở game hay quay lại tab mà bản trên mạng mới hơn (đã chơi ở máy khác) thì tự tải bản mới, không bắt bấm.
# Dùng: python3 net110.py live/v109a.html live/v110a.html
import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:80], c, n); s = s.replace(a, b)

# --- A2 ---
rep("const vact = (kind, payload) => rpc('mv2_act', { p_code: CLOUD.cred.code, p_secret: CLOUD.cred.secret, p_other: VISIT.code, p_kind: kind, p_payload: payload || {} });",
    """const netDown = e => { const m = String(e && (e.name + ' ' + e.message) || e); return /Abort|Failed to fetch|NetworkError|Load failed|network/i.test(m); };
const netLog = (fn, e) => { try { const L = JSON.parse(localStorage.getItem('mv2-neterr') || '[]'); L.unshift([new Date().toISOString(), fn, String(e && e.message || e).slice(0, 120)]); localStorage.setItem('mv2-neterr', JSON.stringify(L.slice(0, 10))); } catch (x) {} try { console.warn('mv2', fn, e); } catch (x) {} };
const vErr = (e, what) => { const m = String(e && e.message || e); netLog('visit', e); return /not allowed/.test(m) ? 'Mã vườn trên máy này lệch rồi con. Vô Cài đặt › Vườn online bấm Lưu ngay một lần rồi ghé lại nghe.' : /no farm/.test(m) ? 'Vườn này không còn nữa con, chắc bạn đã đổi mã vườn.' : /bad kind|bad payload/.test(m) ? 'Bản game trong máy cũ rồi, tải lại trang nghe con.' : netDown(e) ? `Mạng chập chờn quá${what ? ', ' + what : ''}.` : `Chưa ${what || 'làm'} được, thử lại chút nữa nghe con.`; };
const vact = async (kind, payload) => { const a = { p_code: CLOUD.cred.code, p_secret: CLOUD.cred.secret, p_other: VISIT.code, p_kind: kind, p_payload: payload || {} }; try { return await rpc('mv2_act', a); } catch (e) { if (!netDown(e)) throw e; return await rpc('mv2_act', a); } };   /* rớt mạng thì thử lại một lần */""")
rep("return toast('Mạng chập chờn quá, chưa hái giùm được con.', 'lo', { now: true });", "return toast(vErr(e, 'chưa hái giùm được con'), 'lo', { now: true });")
rep("return toast('Mạng chập chờn quá, chưa hái được con.', 'lo', { now: true });", "return toast(vErr(e, 'chưa hái được con'), 'lo', { now: true });")
rep("return toast('Mạng chập chờn quá, chưa tưới được con.', 'lo', { now: true });", "return toast(vErr(e, 'chưa tưới được con'), 'lo', { now: true });")
rep("} catch (e) { toast('Mạng chập chờn, chưa chèo qua được con.', 'lo', { now: true }); } }", "} catch (e) { toast(vErr(e, 'chưa chèo qua được con'), 'lo', { now: true }); } }")
rep(".catch(() => toast('Mạng chập chờn, chưa tặng được.', 'lo', { now: true }))", ".catch(e => toast(vErr(e, 'chưa tặng được'), 'lo', { now: true }))")
rep(".catch(() => toast('Mạng chập chờn quá.', 'lo', { now: true }))", ".catch(e => toast(vErr(e, ''), 'lo', { now: true }))", 2)
rep("catch (e) { CLOUD.err = String(e && e.message || e); CLOUD.at = Date.now() - 30000;", "catch (e) { CLOUD.err = String(e && e.message || e); netLog('save', e); CLOUD.at = Date.now() - 30000;")

# --- A3 ---
rep("if (r && r.ok === false && r.stale){ ST.rev = rev - 1; CLOUD.stale = r.rev; CLOUD.err = ''; staleWarn(); return; }",
    "if (r && r.ok === false && r.stale){ ST.rev = rev - 1; CLOUD.stale = r.rev; CLOUD.err = ''; if (!CLOUD.acted && !(() => { try { return sessionStorage.getItem('mv2-autopull'); } catch (x) { return 1; } })()){ try { sessionStorage.setItem('mv2-autopull', '1'); } catch (x) {} toast('Vườn đã chơi tiếp ở máy khác, đang tải bản mới nhất…', 'vui', { now: true }); cloudRestore(RCODE(c)).catch(err => { netLog('pull', err); staleWarn(); }); return; } staleWarn(); return; }   /* chưa chạm gì từ lúc mở game hay quay lại: tự tải bản mới; đã chơi giữa chừng thì hỏi */")
rep("setInterval(() => cloudSave(false), 15000); setTimeout(() => cloudSave(true), 4000);",
    "CLOUD.back = Date.now(); addEventListener('pointerdown', () => { CLOUD.acted = 1; }, true); addEventListener('keydown', () => { CLOUD.acted = 1; }, true); setInterval(() => cloudSave(false), 15000); setTimeout(() => cloudSave(true), 4000);")
rep("addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden' && CLOUD.dirty) cloudSave(true, true); });",
    "addEventListener('visibilitychange', () => { if (document.visibilityState === 'hidden' && CLOUD.dirty) cloudSave(true, true); else if (document.visibilityState === 'visible' && Date.now() - (CLOUD.hid || 0) > 120000){ CLOUD.back = Date.now(); CLOUD.acted = 0; try { sessionStorage.removeItem('mv2-autopull'); } catch (x) {} setTimeout(() => cloudSave(true), 600); } if (document.visibilityState === 'hidden') CLOUD.hid = Date.now(); });   /* quay lại sau 2 phút: kiểm bản mới ở máy khác */")

rep("const BUILD = 'v109a'", "const BUILD = 'v110a'")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
