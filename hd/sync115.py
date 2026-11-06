# sync115: cùng một vườn thì tự chọn bản xa hơn, không hỏi người chơi. python3 sync115.py live/v115_1e.html live/v115_1f.html
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
# ghi số lần lưu trước khi gửi: tắt app giữa chừng không còn bị tưởng là máy khác
rep("const rev = Math.max(ST.rev || 0, CLOUD.rev || 0) + 1; ST.rev = rev; const r = await rpc('mv2_save2',","const rev = Math.max(ST.rev || 0, CLOUD.rev || 0) + 1; ST.rev = rev; CLOUD.rev = rev; try { localStorage.setItem('mv2-rev', String(rev)); } catch (e) {} const r = await rpc('mv2_save2',")
i=s.index("if (r && r.ok === false && r.stale){ ST.rev = rev - 1;"); j=s.index("CLOUD.rev = rev; try { localStorage.setItem('mv2-rev', String(rev)); } catch (e) {} CLOUD.at = Date.now();",i)
s=s[:i]+"if (r && r.ok === false && r.stale){ ST.rev = rev - 1; CLOUD.rev = rev - 1; CLOUD.stale = r.rev; CLOUD.err = ''; setTimeout(() => cloudSettle(c).catch(err => { netLog('pull', err); staleWarn(); }), 0); return; }   /* trên mạng có bản khác của cùng vườn: tự chọn bản xa hơn, bản kia vô sao lưu */ "+s[j:]
rep("async function cloudSave(force, keep){","""const cloudBetter = d => (d.lv || 1) > (ST.lv || 1) || ((d.lv || 1) === (ST.lv || 1) && ((d.xp || 0) > (ST.xp || 0) || ((d.xp || 0) === (ST.xp || 0) && (d.real || 0) > (ST.real || 0))));
async function cloudSettle(c){ const r = await rpc('mv2_restore', { p_code: c.code, p_secret: c.secret }); if (!r || !r.data || !r.data.plots){ CLOUD.stale = 0; CLOUD.rev = Math.max(CLOUD.rev || 0, r && r.rev || 0); CLOUD.dirty = true; return cloudSave(true); } if (cloudBetter(r.data)){ toast('Vườn đã chơi xa hơn ở máy khác, đang tải bản đó…', 'vui', { now: true }); return cloudRestore(RCODE(c), { ok: 1 }); } CLOUD.ask = { r, cred: c }; pullKeep(); }
async function cloudSave(force, keep){""")
# chỉ hỏi khi nhập mã của một vườn khác
rep("if (!opt.ok && pullWorse(r.data)) return pullAsk(r, cred);","if (!opt.ok && CLOUD.cred && cred.code === CLOUD.cred.code && !cloudBetter(r.data)){ CLOUD.ask = { r, cred }; pullKeep(); toast('Bản trong máy này là mới nhất rồi con.', 'vui', { now: true }); if (SHEET && SHEET.kind === 'set') renderSheet(); return; } if (!opt.ok && pullWorse(r.data)) return pullAsk(r, cred);")
open(dst,'w',encoding='utf-8').write(s)
