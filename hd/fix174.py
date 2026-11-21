#!/usr/bin/env python3
"""v174: bản chống mất vườn + hai chỗ máy nóng.

Cứu bản lưu (5 chỗ):
1. Đọc bản lưu không ra thì KHÔNG lặng lẽ dựng vườn mới đè lên. Giữ nguyên bản cũ, mở Cài đặt,
   Ngoại nói một câu, người chơi chọn: lấy lại bản sao lưu / nhập mã khôi phục / bắt đầu vườn mới.
   Chừng nào chưa chọn thì save() không ghi gì hết.
2. localStorage đầy hoặc bị chặn: trước đây hỏng trong im lặng vĩnh viễn. Giờ dọn bớt sao lưu rồi
   thử lại, vẫn hỏng thì báo một lần bằng toast.
3. Số thứ tự bản lưu (rev) tăng trước khi gửi, gửi hỏng thì không trả về -> máy mất mạng lâu sẽ
   đè vườn của máy kia. Giờ gửi hỏng là trả rev về chỗ cũ.
4. Mã khôi phục: lần đầu máy chủ cấp mã, Ngoại nói cho người chơi biết chỗ lấy (trước đây giấu
   trong Cài đặt, không ai thấy).
5. Nút "Chơi lại" sao lưu trước khi xoá (bản tự lưu gần nhất có thể đã cũ 3 tiếng).

Máy nóng (2 chỗ):
6. Hạ nhịp vẽ khi để yên: trước chỉ bật cho điện thoại, máy tính vẫn vẽ hết công suất mãi mãi.
7. refreshPlot đánh dấu "bóng cần tính lại" vô điều kiện, mà lượt soát chạy mỗi 0,4 giây ->
   bóng cả vườn vẽ lại 2-3 lần/giây dù không có gì đổi. Giờ chỉ đánh dấu khi liếp thật sự đổi.

python3 fix174.py live/v173.html live/v174.html"""
import sys
src, dst = sys.argv[1], sys.argv[2]
t = open(src, encoding='utf8').read()


def rep(a, b, n=1):
    global t
    c = t.count(a)
    assert c == n, (c, n, a[:90])
    t = t.replace(a, b)


rep("BUILD = 'v173'", "BUILD = 'v174'")

# ---------------------------------------------------------------- 1. store.set trả lời được/không
rep("const store = { get(k){ try { return localStorage.getItem(k); } catch (e) { return null; } }, "
    "set(k, v){ try { localStorage.setItem(k, v); } catch (e) {} } };",
    "const store = { get(k){ try { return localStorage.getItem(k); } catch (e) { return null; } }, "
    "set(k, v){ try { localStorage.setItem(k, v); return true; } catch (e) { return false; } } };\n"
    "let BADSAVE = null, SAVEERR = 0, LOSTSAID = 0;   "
    "/* v174: BADSAVE giữ nguyên văn bản lưu đọc không ra, chưa đè lên; SAVEERR: đã báo hết chỗ chứa chưa; "
    "LOSTSAID: đã báo mất mã vườn trên mạng chưa */")

# ---------------------------------------------------------------- 2. save() biết khi lưu hỏng
rep("const save = () => { if (VISIT) return; try { gqSold(); } catch (e) {} ST.real = Date.now(); "
    "store.set('mv2-state', JSON.stringify(ST)); try { CLOUD.dirty = true; } catch (e) {} };",
    "const save = () => { if (VISIT || BADSAVE) return; try { gqSold(); } catch (e) {} ST.real = Date.now(); "
    "const s = JSON.stringify(ST);\n"
    "  if (!store.set('mv2-state', s)){   /* v174: máy hết chỗ chứa — dọn bớt sao lưu rồi thử lại, vẫn hỏng thì báo một lần */\n"
    "    try { const L = JSON.parse(localStorage.getItem('mv2-bak') || '[]'); if (L.length > 1) localStorage.setItem('mv2-bak', JSON.stringify(L.slice(0, 1))); } catch (e) {}\n"
    "    if (!store.set('mv2-state', s) && !SAVEERR){ SAVEERR = 1; try { toast(L135('Máy hết chỗ chứa nên Ngoại chưa lưu vườn được. Con dọn bớt trong máy rồi mở lại giùm Ngoại nghe.', "
    "'This device is out of storage, so the garden could not be saved. Free up some space and reload.')); } catch (e) {} } }\n"
    "  try { CLOUD.dirty = true; } catch (e) {} };")

# ---------------------------------------------------------------- 3. đọc bản lưu hỏng thì không đè
rep("let ST; try { ST = VISIT ? VISIT.state : JSON.parse(store.get('mv2-state') || 'null'); } catch (e) { ST = null; }",
    "let ST; const RAWST = VISIT ? null : store.get('mv2-state'); "
    "try { ST = VISIT ? VISIT.state : JSON.parse(RAWST || 'null'); } catch (e) { ST = null; }")
rep("if (!ST || ST.v !== 1 || !ST.plots) ST = NEWST();",
    "if (!VISIT && RAWST && (!ST || ST.v !== 1 || !ST.plots)) BADSAVE = RAWST;   "
    "/* v174: có bản lưu mà đọc không ra — giữ nguyên, hỏi người chơi, đừng lặng lẽ dựng vườn mới đè lên */\n"
    "if (!ST || ST.v !== 1 || !ST.plots) ST = NEWST();")

# ---------------------------------------------------------------- 4. bảng hỏi khi bản lưu đọc không ra
rep("const bakScroll = k => setTimeout(() => { const e = document.querySelector(`[data-a=${k}]`); "
    "if (e) e.scrollIntoView({ block: 'center', behavior: 'smooth' }); }, 60);",
    "const bakScroll = k => setTimeout(() => { const e = document.querySelector(`[data-a=${k}]`); "
    "if (e) e.scrollIntoView({ block: 'center', behavior: 'smooth' }); }, 60);\n"
    "function badSaveAsk(){ if (!BADSAVE) return; if (!SHEET || SHEET.kind !== 'set') openSheet('set'); else renderSheet(); "
    "say(L135('Ngoại tìm hoài mà không thấy vườn của con đâu hết. Vườn cũ Ngoại còn giữ nguyên, chưa đụng tới. "
    "Con lấy lại một bản Ngoại cất sẵn, hay nhập mã khôi phục cũng được nghe.', "
    "'Grandma looked everywhere but could not find your garden. The old save is still here, untouched. "
    "Restore one of the backups, or enter your recovery code.'), 'dan', { now: true }); }   "
    "/* v174: bản lưu đọc không ra — hỏi chứ không xoá */")

rep("greetWant()){ const oi = () => window.__ready ? setTimeout(greetStart, 300) : setTimeout(oi, 100); oi(); } "
    "else if (AWAY > 5 * 60) setTimeout(welcome, 900);",
    "greetWant() && !BADSAVE){ const oi = () => window.__ready ? setTimeout(greetStart, 300) : setTimeout(oi, 100); oi(); } "
    "else if (BADSAVE) setTimeout(badSaveAsk, 900); "
    "else if (AWAY > 5 * 60) setTimeout(welcome, 900);")

# lời nhắc nằm NGAY ĐẦU bảng Cài đặt (không để lọt xuống đáy, dưới thanh âm lượng)
rep("kind === 'set'){ shT.textContent = 'Cài đặt'; h += `<div class=\"acts\" style=\"margin-top:4px\">"
    "<button class=\"btn\" data-a=\"bug\">Báo lỗi, góp ý</button></div>`;",
    "kind === 'set'){ shT.textContent = 'Cài đặt';\n"
    "    if (BADSAVE) h += `<div class=\"sub\">"
    "${L135('Ngoại chưa thấy vườn của con', 'Grandma could not find your garden')}</div>"
    "<div class=\"note\">${L135('Bản lưu trong máy này đọc không ra. Ngoại giữ nguyên, chưa đụng tới. "
    "Con lấy lại một bản Ngoại cất sẵn ở cuối trang, hay nhập mã khôi phục. "
    "Chừng nào con chưa chọn thì Ngoại chưa ghi đè gì hết.', "
    "'The save on this device could not be read. Grandma has left it untouched. Restore one of the backups "
    "at the bottom of this page, or enter your recovery code. Nothing is overwritten until you choose.')}</div>"
    "<div class=\"acts\"><button class=\"btn\" data-a=\"badnew\">"
    "${L135('Thôi, bắt đầu vườn mới', 'Start a new garden instead')}</button></div>`;\n"
    "    h += `<div class=\"acts\" style=\"margin-top:4px\">"
    "<button class=\"btn\" data-a=\"bug\">Báo lỗi, góp ý</button></div>`;")

rep("a === 'cldres'){ SHEET.restore = 1; SHEET.rerr = ''; }",
    "a === 'badnew'){ try { const L = JSON.parse(localStorage.getItem('mv2-bak') || '[]'); "
    "L.unshift({ at: Date.now(), why: L135('Bản đọc không ra', 'Unreadable save'), lv: 0, xu: 0, s: BADSAVE }); "
    "localStorage.setItem('mv2-bak', JSON.stringify(L.slice(0, BAK.MAX))); } catch (e) {} "
    "BADSAVE = null; save(); renderSheet(); "
    "toast(L135('Ngoại cất bản cũ vô sao lưu rồi. Mình bắt đầu lại nghe con.', "
    "'Grandma tucked the old save into the backups. Let us start fresh.')); }   "
    "/* v174: người chơi tự chọn bỏ bản cũ, bản cũ vẫn được cất lại */\n"
    "  else if (a === 'cldres'){ SHEET.restore = 1; SHEET.rerr = ''; }")

# ---------------------------------------------------------------- 5. rev không phóng khi gửi hỏng
rep("CLOUD.busy = true;\n  try { const c = await cloudEnsure(); if (!c) return; "
    "const rev = Math.max(ST.rev || 0, CLOUD.rev || 0) + 1;",
    "CLOUD.busy = true; const rev0 = ST.rev || 0, crev0 = CLOUD.rev || 0;   "
    "/* v174: gửi hỏng thì trả số thứ tự về chỗ cũ, đừng để máy mất mạng phóng số lên rồi đè vườn máy kia */\n"
    "  try { const c = await cloudEnsure(); if (!c) return; const rev = Math.max(rev0, crev0) + 1;")

rep("catch (e) { CLOUD.err = String(e && e.message || e); netLog('save', e); CLOUD.at = Date.now() - 30000; "
    "if (/not allowed/.test(CLOUD.err)){",
    "catch (e) { CLOUD.err = String(e && e.message || e); netLog('save', e); CLOUD.at = Date.now() - 30000; "
    "ST.rev = rev0; CLOUD.rev = crev0; try { localStorage.setItem('mv2-rev', String(crev0)); } catch (x) {} "
    "if (/not allowed/.test(CLOUD.err)){")

# ---------------------------------------------------------------- 6. Ngoại chỉ chỗ lấy mã khôi phục
rep("CLOUD.cred = { code: r.code, secret: r.secret }; "
    "try { localStorage.setItem('mv2-cloud', JSON.stringify(CLOUD.cred)); } catch (e) {} return CLOUD.cred; }",
    "CLOUD.cred = { code: r.code, secret: r.secret }; "
    "try { localStorage.setItem('mv2-cloud', JSON.stringify(CLOUD.cred)); } catch (e) {}\n"
    "  try { if (ST.seen && !ST.seen.rcode){ ST.seen.rcode = 1; "
    "say(L135('Ngoại ghi cái mã vườn của con trong Cài đặt rồi đó. Đổi máy hay lỡ xoá trình duyệt, "
    "con nhập mã đó là vườn về y nguyên. Chép ra để dành giùm Ngoại nghe.', "
    "'Grandma wrote your garden code down in Settings. If you change device or clear your browser, "
    "enter that code and the garden comes back just as it was. Keep a copy somewhere safe.'), 'dan', { idle: true }); } } catch (e) {}\n"
    "  return CLOUD.cred; }   /* v174: đưa mã khôi phục ra chỗ người chơi thấy */")

# ---------------------------------------------------------------- 7. Chơi lại: sao lưu trước khi xoá
rep("a === 'reset2'){ const pl = ST.player; ST = NEWST();",
    "a === 'reset2'){ BAK.take(L135('Trước khi chơi lại', 'Before starting over'));   "
    "/* v174: bản tự lưu gần nhất có thể đã cũ 3 tiếng */ const pl = ST.player; ST = NEWST();")

# ---------------------------------------------------------------- 8. máy tính cũng hạ nhịp khi để yên
rep("const idle = MOBILE && !window.__stop && fn >= FRH,",
    "const idle = !window.__stop && fn >= FRH,   "
    "/* v174: máy tính cũng hạ nhịp khi để yên, trước đây chỉ điện thoại được */")

# ---------------------------------------------------------------- 9. bóng chỉ tính lại khi liếp đổi
rep("function refreshPlot(id){ SHDIRTY = 1; const p = ST.plots[id], v = PV[id], P = PL[id];",
    "function vSig(v){ if (!v) return ''; let s = v.key || ''; for (const k in v){ const o = v[k]; "
    "if (o && o.isObject3D) s += ';' + k + (o.visible ? 1 : 0) + (o.children ? o.children.length : 0); } return s; }   "
    "/* v174: khai báo bằng function để hàm gọi sớm lúc đang tải không chạm biến chưa khai báo */\n"
    "function refreshPlot(id){ const s0 = vSig(PV[id]); const r = refreshPlot0(id); "
    "if (vSig(PV[id]) !== s0) SHDIRTY = 1; return r; }   "
    "/* v174: chỉ tính lại bóng khi liếp thật sự đổi — lượt soát chạy mỗi 0,4 giây, trước đây lượt nào cũng bắt vẽ lại bóng cả vườn */\n"
    "function refreshPlot0(id){ const p = ST.plots[id], v = PV[id], P = PL[id];")

# ================================================================ gộp thêm 3 chỗ (Ares chốt 21/11)

# ---------------------------------------------------------------- 10. không tự đẻ vườn mới khi máy chủ từ chối
# Máy chủ từ chối một lần lưu -> code cũ vứt mã vườn rồi lần sau tự đăng ký vườn mới.
# Thử lưu mỗi 15 giây nên mỗi vòng hỏng là thêm một vườn trùng tên. Trên máy chủ thật:
# 195 dòng / 34 người, một người bị nhân thành 118 bản.
rep("CLOUD.cred = null; CLOUD.rev = 0; ST.rev = 0; "
    "try { localStorage.removeItem('mv2-cloud'); localStorage.removeItem('mv2-rev'); } catch (x) {} }",
    "CLOUD.cred = null; CLOUD.lost = 1; CLOUD.rev = 0; ST.rev = 0; "
    "try { localStorage.removeItem('mv2-cloud'); localStorage.removeItem('mv2-rev'); } catch (x) {} "
    "try { lostSay(); } catch (y) {} }   "
    "/* v174: không tự lập vườn mới nữa — hỏi người chơi trước */")

rep("async function cloudEnsure(){ if (CLOUD.cred) return CLOUD.cred; if (!ST.player || greetWant()) return null;",
    "async function cloudEnsure(){ if (CLOUD.cred) return CLOUD.cred; if (CLOUD.lost) return null;   "
    "/* v174: mã vườn cũ không mở được — chờ người chơi chọn, đừng lặng lẽ đẻ vườn mới */ "
    "if (!ST.player || greetWant()) return null;")

rep("function badSaveAsk(){",
    "function lostSay(){ if (LOSTSAID) return; LOSTSAID = 1; "
    "say(L135('Mã vườn của con trên mạng Ngoại mở không ra nữa. Vườn trong máy vẫn còn nguyên, con cứ chơi bình thường. "
    "Khi nào rảnh vô Cài đặt, có mã khôi phục thì nhập vô, không thì nhờ Ngoại lập sổ mới cho nghe.', "
    "'Grandma can no longer open your garden on the server. The garden on this device is untouched, so keep playing. "
    "When you have a moment, open Settings: enter your recovery code if you have one, or ask Grandma to start a new record.'), "
    "'dan', { idle: true }); }\n"
    "function badSaveAsk(){")

# lời nhắc + nút trong bảng Cài đặt
rep("    if (BADSAVE) h += `<div class=\"sub\">",
    "    if (CLOUD.lost) h += `<div class=\"sub\">"
    "${L135('Sổ vườn trên mạng không mở được', 'Your garden record cannot be opened')}</div>"
    "<div class=\"note\">${L135('Vườn trong máy vẫn còn nguyên. Có mã khôi phục thì nhập ở cuối trang. "
    "Không có thì bấm nút dưới đây, Ngoại lập sổ mới cho máy này.', "
    "'The garden on this device is untouched. If you have a recovery code, enter it at the bottom of this page. "
    "If not, tap below and Grandma will start a new record for this device.')}</div>"
    "<div class=\"acts\"><button class=\"btn\" data-a=\"cldnew\">"
    "${L135('Lập sổ vườn mới cho máy này', 'Start a new record for this device')}</button></div>`;\n"
    "    if (BADSAVE) h += `<div class=\"sub\">")

rep("a === 'badnew'){",
    "a === 'cldnew'){ CLOUD.lost = 0; CLOUD.err = ''; CLOUD.at = 0; CLOUD.dirty = true; "
    "cloudSave(true).catch(e => {}); renderSheet(); "
    "toast(L135('Ngoại lập sổ mới rồi. Chút nữa vô Cài đặt chép mã khôi phục để dành nghe.', "
    "'Grandma started a new record. Copy the recovery code from Settings and keep it safe.')); }\n"
    "  else if (a === 'badnew'){")

# ---------------------------------------------------------------- 11. giống quý không thành "thứ gieo lần trước"
# Bong bóng hạt trên liếp trống là trồng NGAY, không hỏi — nó trồng thứ gieo lần trước.
# Gieo một hạt quý xong là mọi liếp trống thành nút trồng hạt quý, bấm nhầm là mất.
rep("const quickSeed = P => { const k = ST.lastSeed; "
    "return k && CROPS[k] && unlocked(k) && fits(k, P) && (ST.seeds[k] || 0) > 0 ? k : null; };",
    "const quickSeed = P => { const k = ST.lastSeed; "
    "return k && CROPS[k] && CROPS[k].rare !== 'quy' && unlocked(k) && fits(k, P) && (ST.seeds[k] || 0) > 0 ? k : null; };   "
    "/* v174: giống quý không bao giờ gieo một chạm — phải nhấn giữ chọn trong vòng hạt */")

rep("if (!c.tree) ST.lastSeed = k;",
    "if (!c.tree && c.rare !== 'quy') ST.lastSeed = k;   "
    "/* v174: gieo giống quý không làm đổi thứ gieo nhanh */")

# ---------------------------------------------------------------- 12. danh sách bà con: mỗi người chỉ hiện một lần
rep("function nbSugHTML(){ const F = NB2.list || [], "
    "L = (NB2.sug || []).filter(n => !F.some(x => x.code === n.code && x.followed)).slice(0, 5); "
    "if (!L.length) return '';",
    "function nbSugHTML(){ const F = NB2.list || [], M = new Map();   "
    "/* v174: cùng tên cùng vườn thì gom lại một dòng, giữ bản cấp cao nhất */\n"
    "  for (const n of (NB2.sug || [])){ if (F.some(x => x.code === n.code && x.followed)) continue;\n"
    "    const kk = (n.name || '') + '\\u0000' + (n.garden || ''), o = M.get(kk); "
    "if (!o || (n.lv || 0) > (o.lv || 0)) M.set(kk, n); }\n"
    "  const L = [...M.values()].slice(0, 5); if (!L.length) return '';")

open(dst, 'w', encoding='utf8').write(t)
print('ok', len(t))
