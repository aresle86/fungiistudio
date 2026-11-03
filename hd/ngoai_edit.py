import re
p='live/vuon3d.html'; s=open(p).read()
def rep(a,b,cnt=1):
    global s
    n=s.count(a)
    assert n==cnt,(a[:80],n); s=s.replace(a,b)
# ---- toast + css
rep("function sayOnce(key, txt, mood){", "function toast(txt, kind){ try { let w = document.getElementById('tstw'); if (!w){ w = document.createElement('div'); w.id = 'tstw'; document.body.appendChild(w); } if ([...w.children].some(c => c.textContent === txt)) return; const d = document.createElement('div'); d.className = 'tst' + (kind === 'lo' || kind === 'dan' ? ' lo' : ''); d.textContent = txt; w.appendChild(d); while (w.children.length > 2) w.firstChild.remove(); setTimeout(() => d.classList.add('out'), 2600); setTimeout(() => d.remove(), 3100); } catch (e) {} }   /* thông báo ngắn kiểu giao diện, không phải lời Ngoại: thiếu xu, hết chỗ, đã làm hôm nay, mạng… */\nfunction sayOnce(key, txt, mood){")
rep(".ddt.on{", "#tstw{position:fixed;left:50%;transform:translateX(-50%);top:calc(env(safe-area-inset-top,0px) + 92px);z-index:70;display:flex;flex-direction:column;gap:6px;align-items:center;pointer-events:none;width:max-content;max-width:calc(100vw - 32px)}.tst{background:#FBF7EE;color:#4A2F1E;border:2px solid #E3C995;border-radius:999px;padding:7px 16px;font:600 14px/1.3 var(--f-body);box-shadow:0 4px 0 rgba(74,47,30,.18);text-align:center;animation:tstin .25s ease-out;transition:opacity .4s,transform .4s}.tst.lo{border-color:#E8A08A;background:#FFF1EC}.tst.out{opacity:0;transform:translateY(-8px)}@keyframes tstin{from{opacity:0;transform:translateY(-8px)}}.ddt.on{")
# ---- popup-aware busy + budget
rep("const busy = () => !!(window.LVON || TOOL || STROKE || (typeof G0 !== 'undefined' && G0) || SHEET || BOOK || !fan.hidden || document.body.classList.contains('drag'));",
    "const busy = () => !!(window.LVON || TOOL || STROKE || (typeof G0 !== 'undefined' && G0) || SHEET || BOOK || !fan.hidden || document.body.classList.contains('drag') || popOn());\nconst popOn = () => { try { return !!(document.querySelector('.ddt.on, .lvup:not([hidden]), #fui:not([hidden]) .fcard, #tstw .tst') || (typeof RING !== 'undefined' && !RING.hidden) || (document.getElementById('intro') && !document.getElementById('intro').hidden) || (typeof SUA !== 'undefined' && SUA && SUA.on)); } catch (e) { return false; } };   /* đang có bảng, thẻ, vòng chọn hay thông báo nổi thì Ngoại không tự nói */")
rep("if (IDLEQ.length && performance.now() - IDLE0 > 1200 && performance.now() - (SAYH.length ? SAYH[SAYH.length - 1].at : 0) > 6000 && !(sayT > 0 && !ng.hidden)){",
    "if (IDLEQ.length && performance.now() - IDLE0 > 2500 && performance.now() - (SAYH.length ? SAYH[SAYH.length - 1].at : 0) > 15000 && !(sayT > 0 && !ng.hidden)){")
rep("function bark(txt, mood = 'vui'){ try { if (VISIT || busy() || (sayT > 0 && !ng.hidden) || (window.LVON)) return; if (SAYH.slice(-6).some(h => h.t === txt)) return; }",
    "function bark(txt, mood = 'vui'){ try { if (VISIT || busy() || (sayT > 0 && !ng.hidden) || (window.LVON)) return; if (SAYH.slice(-6).some(h => h.t === txt)) return; if (SAYH.length && performance.now() - SAYH[SAYH.length - 1].at < 20000) return; }")
# ---- Bỏ: lines that repeat what the UI already shows
rep("p.crop ? 'Liếp này đang có cây rồi, chọn liếp trống con.' :", "p.crop ? null :")
rep("if (ST.player && !ST.seen.hello){ ST.seen.hello = 1; setTimeout(() => say('Chỗ nào có hình nhảy trên liếp là chỗ cần làm. Nhấn giữ liếp thì xem kỹ hơn.'), 800); }", "if (ST.player && !ST.seen.hello) ST.seen.hello = 1;")
rep("ST.fg[k] = 1; p.fast = 1; sayOnce('fast', 'Hạt giống tốt Ngoại để dành đó, vụ đầu lên mau lắm. Chờ chút xíu là hái được.', 'vui'); }", "ST.fg[k] = 1; p.fast = 1; }")
rep(" sayOnce('bed1', 'Liếp mới đắp đất còn tơi, gieo gì cũng lên. Đắp thêm thì tốn hơn chút đó con.', 'vui'); },", " },")
rep("if (on && g.eggs > 0 && ST.seen.sold && !ST.seen.gaintro){ sayOnce('gaintro', 'Gà của Ngoại đẻ trứng rồi kìa. Chạm vô ổ mà lượm. Máng hết thóc thì chạm máng tre cho gà ăn nghe.', 'vui'); }", "")
rep(", la: 'Lá rụng đầy gốc cây. Gom lại ủ, bữa sau có cái bón cho liếp.' }[o.k], 'dan'); }", " }[o.k], 'dan'); }")
rep("  if (n === GA.lv) say('Từ giờ Ngoại giao con chăm đàn gà nghe. Chạm máng tre cho gà ăn, ổ có trứng thì chạm mà lượm. Chạm vô chuồng là coi gà.', 'vui', { idle: true });\n", "")
rep(" sayOnce('vitfeed1', 'Vịt mê rau muống lắm. Hết rau thì vớt lục bình dưới mương cho ăn, khỏi tốn xu.', 'vui'); },", " },")
rep("say(mk === 'nong' ? 'Để đây được đó, chỗ này có nắng.' : `Đặt ${OBJD[mk].name} ở đây rồi nè.`, 'vui', { now: true });", "sfx('pop');", 1)
rep("say(`Đặt ${DCK[dk].name.toLowerCase()} ở đây rồi nè.`, 'vui', { now: true });", "sfx('pop');")
rep("say(`Đặt ${BIGD[mk].name} ở đây rồi nè.`, 'vui', { now: true });", "sfx('pop');")
rep("if (!c) return say(fr ? 'Liếp này đang để trống.' : 'Liếp này Ngoại để trống cho đất nghỉ đó con.', 'vui', { now: true });", "if (!c) return;")
rep("sayOnce('sold', 'Có đồng ra đồng vô rồi hen.', 'vui'); },", "ST.seen.sold = 1; },")
rep("else if (n >= 10) bark(pick(['Chà, được cả rổ!', 'Bữa nay trúng mùa dữ hen!', `Trời, được tới ${n} ${c.unit} lận!`]), 'nhay'); else if (k0 === 'cai' && Math.random() < .3) bark(pick(['Mớ cải này lá non mướt.', 'Chừa một ít nấu canh là vừa.'])); else if (Math.random() < .12) bark('Mớ rau này mà nấu nồi canh, khỏi đi chợ luôn.'); return true; },",
    "else if (n >= 10 && Math.random() < .3) bark('Chà, được cả rổ!', 'nhay'); return true; },")
rep("bark(pick([`Xong việc \"${x.txt.toLowerCase()}\" rồi.`, 'Được rồi đó, việc đó xong rồi.', 'Lẹ tay ghê!'])); } }", "toast(`Xong việc: ${x.txt}`); } }")
rep("say(pick([`${o.who} cảm ơn con nè, khen rau nhà mình tươi.`, `${o.who} gửi tiền, dặn bữa sau còn ghé.`, `Giao rồi đó con. ${o.who} vui lắm.`]), 'vui', { now: true });", "if (!ST.seen.don1){ ST.seen.don1 = 1; say(`${o.who} cảm ơn con nè, khen rau nhà mình tươi.`, 'vui', { now: true }); }")
rep("say(got ? `Về tới nhà rồi. Con đem ${got} từ ${from} về, cất trong kho rồi đó.` : (L.water ? 'Về rồi đó con. Tưới giùm hàng xóm vậy là giỏi lắm.' : 'Về tới nhà rồi con.'), 'vui', { now: true });", "if (got) toast(`Đem về: ${got}`);")
rep(" xoai: 'Mùa xoài cả xóm qua phụ hái, rồi chia nhau ăn. Có của thì chia, vậy mới vui.',", "")
rep("if (n) sayOnce('khap1', 'Dưa muối chua vừa tới nè. Hồi đó nhà mình ăn dưa cải với thịt kho cả tuần Tết.', 'vui'); return n; } };", "return n; } };")
rep(" sayOnce('gio1', 'Giỏ lục bình đi chợ nổi bán chạy lắm, khách nước ngoài cũng mua.', 'vui'); } };", " } };")
rep("say(pick(['Ghe bẹo nhổ sào đi rồi, mai lại ghé. Hàng nhà mình đem ra chợ nổi bán chạy lắm con.', 'Cô Sáu khen hàng nhà mình đẹp, dặn mai để dành thêm.']), 'vui', { now: true });", "toast('Ghe bẹo nhổ sào đi rồi, mai lại ghé.');")
rep(" bark(d.cat === 'rao' ? 'Hàng rào mới nhìn vườn sáng sủa hẳn.' : d.cat === 'ga' ? 'Chuồng mới, gà chắc đẻ siêng hơn.' : 'Vịt có chỗ ở mới rồi đó.'); }", " }")
rep(" sayOnce('tetseed_' + k, k === 'duahau' ? 'Dưa hấu ruột vàng hiếm lắm, bổ ra vàng ươm. Chưng Tết là đẹp nhất xóm.' : 'Cúc mâm xôi Sa Đéc nở tròn như mâm xôi, chưng Tết cho có lộc.', 'vui'); }", " }")
rep("setTimeout(() => bark(pick(['Ủa, mới đó mà có trứng rồi!', 'Lại thêm một ổ nữa nè.'])), 700); return r; };", "return r; };")
rep("if (ST.ga.trough > t0 && Math.random() < .3) setTimeout(() => bark('Coi kìa, mới nghe khua máng là chạy tới hết trơn.'), 700); return r; };", "return r; };")
rep("if (dead) setTimeout(() => bark('Hổng sao, mình gieo lại một liếp khác.'), 600); return r; };", "return r; };")
rep(" if (Object.entries(ST.inv).some(([k, n]) => n > 0 && CROPS[k] && CROPS[k].kind === 'patch')) pool.push('Mớ rau này mà nấu nồi canh, khỏi đi chợ luôn.');", " if (Object.entries(ST.inv).some(([k, n]) => n > 0 && CROPS[k] && CROPS[k].kind === 'patch')) pool.push('Mớ rau này mà nấu nồi canh, khỏi đi chợ luôn.'); if (popOn()) return;")
rep("now - LASTIN < 50000 || now - lastSay < 90000 || busy()) return;", "now - LASTIN < 50000 || now - lastSay < 180000 || busy()) return;")
# ---- checkTips: no ripe/thirst chatter; wilt/dead summarized in one line
rep("function checkTips(){ for (const P of PLOTS){", "function checkTips(){ const TIPW = []; for (const P of PLOTS){")
rep("if (s === 'thirst') say(`Liếp ${n} khô rồi, tưới chút nước nghen.`, 'dan', { idle: true }); else if (s === 'wilt') say(`${N} hơi héo rồi. Tưới một chút cho cây tỉnh lại.`, 'lo'); else if (s === 'dead') say(`${N} khô mất rồi. Thôi, mình dọn liếp trồng lại.`, 'lo'); else if (s === 'ripe') bark(pick([`${N} chín rồi đó.`, `${N} tới lứa hái rồi.`])); } }",
    "if (s === 'thirst') sayOnce('thirst1', `Liếp ${n} khô rồi, tưới chút nước nghen. Thấy giọt nước nhảy trên liếp là liếp cần tưới.`, 'dan'); else if (s === 'wilt' || s === 'dead') TIPW.push([s, N]); }\n  if (TIPW.length){ const w = TIPW.filter(x => x[0] === 'wilt').length, d = TIPW.length - w; say(TIPW.length === 1 ? (w ? `${TIPW[0][1]} hơi héo rồi. Tưới một chút cho cây tỉnh lại.` : `${TIPW[0][1]} khô mất rồi. Thôi, mình dọn liếp trồng lại.`) : `Có ${[w ? w + ' liếp héo' : '', d ? d + ' liếp khô mất' : ''].filter(Boolean).join(', ')} rồi. Héo thì tưới, khô thì dọn trồng lại.`, 'lo'); } }")
# ---- error / limit / confirm lines -> toast
pat=re.compile(r"\bsay\((`[^`]*`|'[^']*')")
kw=re.compile(r"thiếu|Mạng chập chờn|hết chỗ|Hết chỗ|chật rồi|còn đầy|Còn đầy|Hôm nay (con )?(hái|tưới|tặng|xin|để quà|têm|hái ké)|tưới giùm nhiều rồi|tới cấp \$|Tới cấp|đủ bốn cái|Hố đầy|Đổi xong|Nhắn xin hạt|Mua thêm cái lu|Ghi vô Sổ cổ tích|Hết rơm|Chạm xuống mặt sông|Cần bốn ô|Ao cá cần|Chỉ đặt được|Đồ kiểng đặt|Vườn này chưa có gì|Gốc này để trồng|Chưa có cá|Cá lì quá|vắng cá|Giàn hai tầng|Bốn khạp|đất cũng tốt hết|Hôm nay hái")
out=[];last=0;n=0
for m in pat.finditer(s):
    t=m.group(1)
    if kw.search(t) and 'thành hàng xóm rồi đó con. ${' not in t:
        out.append(s[last:m.start()]); out.append('toast('); last=m.start()+4; n+=1
out.append(s[last:]); s=''.join(out)
print('toasts',n)
open(p,'w').write(s)
