# v146: thứ tự mới cho người mới (anh Ares duyệt 13/11): vô thẳng vườn, Ngoại đón 3 câu, chơi trước, thay đồ sau.
# (1) Lần đầu KHÔNG mở buồng thay đồ. Tạo sẵn người chơi mặc định (dáng 1, "Con", "Vườn nhà Ngoại", cờ tmp).
# (2) "Ngoại đón ở cổng": 3 câu trong bong bóng Ngoại, máy quay lướt mé sông -> góc vườn -> liếp trống.
#     Chạm để nghe tiếp, có nút "Bỏ qua", tự qua câu nếu để lâu. Ghi stepMark intro_done / intro_skip.
# (3) Sau lần bán đầu tiên Ngoại mời vô buồng thay đồ (đóng được bằng "Để sau", vẫn vô lại từ nút hình người chơi).
# (4) Vườn tmp chỉ ghi lên máy chủ sau khi nghe xong / bỏ qua lời đón (khách lướt ngang không tạo vườn rác).
import sys, json
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v145'", "BUILD = 'v146'")

L1 = 'Về tới rồi hả con! Trên phố mệt lắm phải hông con. Thôi, về đây với Ngoại.'
L2 = 'Vườn này Ngoại giữ mấy chục năm rồi. Giờ tay chân yếu, làm hông xuể, mấy góc cỏ mọc um hết trơn.'
L3 = 'Ngoại chừa cho con mấy liếp đó. Con phụ Ngoại gầy lại từ từ, hông gấp gì hết. Mai mốt vườn mình lại đẹp nhứt xóm cho coi.'
SOW = 'Con chạm vô liếp trống để gieo hạt nghe.'
INV = 'Vô thay đồ đi con, rồi nói Ngoại nghe tên con, đặt tên cho vườn luôn.'
LATER = 'Hông sao. Chừng nào rảnh con chạm vô hình của con là vô thay đồ được nghe.'
EN = {
    L1: "You made it home, dear! The city wears you out, doesn't it. Come, stay with Grandma.",
    L2: "I've kept this garden for decades. My hands are getting weak now, and the weeds have taken over the corners.",
    L3: "I saved a few beds for you. Help me bring it back, little by little, no rush at all. One day our garden will be the prettiest in the village again.",
    SOW: 'Tap an empty bed to sow seeds.',
    INV: 'Come get changed, dear. Then tell Grandma your name, and name the garden too.',
    LATER: "That's fine. Whenever you like, tap your picture to get changed.",
    'Bỏ qua': 'Skip', 'Chạm để nghe tiếp': 'Tap to continue', 'Để sau': 'Later',
}
EN = {k: v for k, v in EN.items() if ('"' + k + '":') not in s}   # câu nào bảng dịch có sẵn thì thôi
assert L1 in EN and INV in EN
rep('const UIEN = {', 'const UIEN = {' + ', '.join(json.dumps(k, ensure_ascii=False) + ': ' + json.dumps(v, ensure_ascii=False) for k, v in EN.items()) + ', ')
rep('UIRX = [[', 'UIRX = [["^Coi bảnh quá ta, (.+)! Từ nay vườn mình kêu là (.+) nghe\\\\.$", "Looking sharp, $1! From now on our garden is called $2."], [')

# máy quay lướt chậm được
rep("function camTo(tg, zm){ CAMGO = { t: 0, a: ctl.target.clone(), z0: cam.zoom, off: cam.position.clone().sub(ctl.target), to: tg, zm }; }",
    "function camTo(tg, zm, d){ CAMGO = { t: 0, a: ctl.target.clone(), z0: cam.zoom, off: cam.position.clone().sub(ctl.target), to: tg, zm, d }; }")
rep("CAMGO.t + dt / .6", "CAMGO.t + dt / (CAMGO.d || .6)")

# lúc Ngoại đón: không câu nào khác chen vô
rep("if (CERE && !o.now) return;", "if (GREET && !o.greet) return; if (CERE && !o.now) return;")
rep("!document.getElementById('intro').hidden){ el.hidden = true; return; }", "!document.getElementById('intro').hidden || GREET){ el.hidden = true; return; }")

# (2) lời đón
GREETJS = r"""var GREET;
const GREETL = [__L1__, __L2__, __L3__], GREETS = [[3.4, 8.6, 1.15], [8.3, 6.7, 1.05], [2.9, 3.9, 1.3]];
const greetWant = () => !VISIT && (!ST.player || (ST.player.tmp && !(ST.steps && (ST.steps.intro_done || ST.steps.intro_skip || ST.steps.seed1))));
function greetShow(){ const g = GREET; if (!g) return; const t = GREETL[g.i], sp = GREETS[g.i]; say(t, g.i ? 'vui' : 'nhay', { now: true, love: true, greet: true }); sayT = 1e9; g.at = performance.now(); g.len = t.length;
  try { camTo(new T.Vector3(sp[0], .3, sp[1]), DEFZ() * sp[2], 2.4); } catch (e) {} $('#gtN').textContent = (g.i + 1) + '/' + GREETL.length; }
function greetNext(){ const g = GREET; if (!g || performance.now() - g.at < 600) return; if (++g.i >= GREETL.length) return greetEnd('intro_done'); try { sfx('pick'); } catch (e) {} greetShow(); }
function greetEnd(k){ const g = GREET; if (!g) return; clearInterval(g.tm); GREET = null; $('#gt').hidden = true; document.body.classList.remove('greet'); stepMark(k); save();
  try { camTo(new T.Vector3(GREETS[2][0], .3, GREETS[2][1]), DEFZ(), 1); } catch (e) {} say(__SOW__, 'vui', { now: true }); try { nxq(); } catch (e) {} }
function greetStart(){ if (GREET || !greetWant()) return; if (!ST.player){ ST.player = { av: 0, name: EN ? 'Dear' : 'Con', garden: EN ? "Grandma's Garden" : 'Vườn nhà Ngoại', tmp: 1 }; ST.seen.hello = 1; save(); }
  try { avHud(); placeAvatar(); } catch (e) { console.error(e); }
  $('#gtSkip').textContent = L135('Bỏ qua', 'Skip'); $('#gtT').textContent = L135('Chạm để nghe tiếp', 'Tap to continue');
  GREET = { i: 0, at: 0, len: 0, tm: setInterval(() => { const g = GREET; if (g && performance.now() - g.at > Math.max(8000, g.len * 110)) greetNext(); }, 500) };
  $('#gt').hidden = false; document.body.classList.add('greet'); try { nxq(); } catch (e) {} greetShow(); }
$('#gt').addEventListener('click', e => { if (e.target.closest('#gtSkip')){ try { sfx('pick'); } catch (er) {} greetEnd('intro_skip'); } else greetNext(); });
/* (3) bán được lần đầu: Ngoại mời vô buồng thay đồ, chờ lúc tay con rảnh */
function dressInvite(){ if (VISIT || !ST.player || !ST.player.tmp || ST.seen.dress1) return; let n = 0, said = 0;
  const w = () => { if (!ST.player || !ST.player.tmp) return; if (GREET || !intro.hidden || busy()){ if (++n < 360) setTimeout(w, 500); return; }
    if (!said){ said = 1; ST.seen.dress1 = 1; save(); say(__INV__, 'vui', { now: true, love: true }); setTimeout(w, 3000); return; }
    stepMark('dress_open'); openIntro(); };
  setTimeout(w, 1500); }
$('#inLater').addEventListener('click', () => { intro.hidden = true; stepMark('dress_later'); try { sfx('pick'); } catch (e) {} say(__LATER__, 'vui', { now: true }); });
function tutStep(){ if (VISIT || !ST.player ||"""
for k, v in (('__L1__', L1), ('__L2__', L2), ('__L3__', L3), ('__SOW__', SOW), ('__INV__', INV), ('__LATER__', LATER)):
    assert GREETJS.count(k) == 1; GREETJS = GREETJS.replace(k, json.dumps(v, ensure_ascii=False))
rep("function tutStep(){ if (VISIT || !ST.player ||", GREETJS)

# (1) mở đầu: không mở buồng thay đồ nữa
rep("if (!ST.player){ const oi = () => window.__ready ? setTimeout(() => { if (!ST.player) openIntro(); }, 300) : setTimeout(oi, 100); oi(); } else if (AWAY > 5 * 60) setTimeout(welcome, 900);",
    "if (greetWant()){ const oi = () => window.__ready ? setTimeout(greetStart, 300) : setTimeout(oi, 100); oi(); } else if (AWAY > 5 * 60) setTimeout(welcome, 900); "
    "if (ST.player && ST.player.tmp && ST.steps && ST.steps.sell1 && !ST.seen.dress1) setTimeout(dressInvite, 4000);")

# (3) buồng thay đồ cho người chơi tmp
rep("ST.soldN = (ST.soldN || 0) + n; stepMark('sell1');", "ST.soldN = (ST.soldN || 0) + n; stepMark('sell1'); try { dressInvite(); } catch (e) {}")
rep("const first = !ST.player, name = (", "const tmp0 = !!(ST.player && ST.player.tmp), first = !ST.player, name = (")
rep("} else toast('Đổi xong rồi nghe con.', 'vui', { now: true }); });",
    "} else if (tmp0){ stepMark('dress1'); setTimeout(() => say(`Coi bảnh quá ta, ${name === 'Con' ? 'con' : name}! Từ nay vườn mình kêu là ${garden} nghe.`, 'nhay', { now: true, love: true }), 400); } else toast('Đổi xong rồi nghe con.', 'vui', { now: true }); });")
rep("go.textContent = ST.player ? 'Lưu' : 'Về vườn';", "go.textContent = ST.player ? (ST.player.tmp ? L135('Xong rồi', 'Done') : 'Lưu') : 'Về vườn';")
rep("intro.hidden = false; ng.hidden = true; mirUpd(); }", "if (P && P.tmp){ $('#inName').value = ''; $('#inGarden').value = ''; } $('#inLater').hidden = !(P && P.tmp); $('#inLater').textContent = L135('Để sau', 'Later'); intro.hidden = false; ng.hidden = true; mirUpd(); }")
rep('<button class="btn g" id="inGo">Về vườn</button>', '<button class="btn g" id="inGo">Về vườn</button><button type="button" id="inLater" hidden>Để sau</button>')
rep('<div class="intro" id="intro"', '<div id="gt" hidden><button type="button" id="gtSkip">Bỏ qua</button><span id="gtHint"><span id="gtT">Chạm để nghe tiếp</span> · <span id="gtN">1/3</span></span></div><div class="intro" id="intro"')

# (4) vườn tmp chưa nghe xong lời đón thì chưa ghi máy chủ
rep("if (!ST.player) return null; const r = await rpc('mv2_register'", "if (!ST.player || greetWant()) return null; const r = await rpc('mv2_register'")

rep(".nxq .nqd2.gift{color:#9A6E12}",
    ".nxq .nqd2.gift{color:#9A6E12}\n"
    "body.greet .ui.top,body.greet .ui.bot .row,body.greet #tray,body.greet #bCtr{visibility:hidden}"
    "#gt{position:fixed;inset:0;z-index:6;cursor:pointer;-webkit-tap-highlight-color:transparent;touch-action:manipulation}"
    "#gtSkip{position:absolute;right:calc(14px + env(safe-area-inset-right,0px));top:calc(14px + env(safe-area-inset-top,0px));min-height:44px;min-width:92px;padding:0 18px;border:0;border-radius:999px;background:#5F3A1E;color:#FFF7E6;font:700 16px/1 var(--f-body,'Baloo 2'),sans-serif;box-shadow:0 3px 0 #3E2512;cursor:pointer}"
    "#gtHint{position:absolute;left:50%;top:calc(22px + env(safe-area-inset-top,0px));transform:translateX(-50%);padding:7px 16px;border-radius:999px;background:#FBF7EE;color:#6B4529;font:700 14px/1.2 var(--f-body,'Baloo 2'),sans-serif;white-space:nowrap;box-shadow:0 2px 0 #D2A57E;animation:gtP 1.8s ease-in-out infinite}"
    "@keyframes gtP{0%,100%{opacity:1}50%{opacity:.82}}@media (prefers-reduced-motion:reduce){#gtHint{animation:none}}"
    "#inLater{display:block;margin:6px auto 0;min-height:44px;padding:0 22px;border:0;background:none;color:#6B4529;font:700 16px/1 var(--f-body,'Baloo 2'),sans-serif;text-decoration:underline;text-underline-offset:3px;cursor:pointer}#inLater[hidden]{display:none}@media (max-width:640px){.inbox{position:relative}#inLater{position:absolute;top:4px;right:4px;margin:0;padding:0 12px;font-size:14px}}")

# (5) thẻ Đơn hàng bớt rối (anh Ares 13/11): "Còn thiếu" là dòng chữ chớ không giả làm nút; tiền thưởng lên góc tên; một hàng nút.
rep("""<div class="ordr${ok ? ' ok' : ''}"><div class="ow"><b>${o.who}${o.lead ?""", """<div class="ordr${ok ? ' ok' : ''}"><div class="ow">${ok ? '' : `<i class="oxu">${o.xu} xu</i>`}<b>${o.who}${o.lead ?""")
rep("""<div class="ordr ghe${full ? ' ok' : ''}"><div class="ow"><b>""", """<div class="ordr ghe${full ? ' ok' : ''}"><div class="ow">${full ? '' : `<i class="oxu">${o.xu} xu</i>`}<b>""")
rep("q - has(k)), 0)} món · ${o.xu} xu`}</button>", "q - has(k)), 0)} món`}</button>")
rep("q - gheGot(o, k) - has(k)), 0)} món · ${o.xu} xu`}</button>", "q - gheGot(o, k) - has(k)), 0)} món`}</button>")
rep('UIRX = [[', 'UIRX = [["^Còn thiếu (\\\\d+) món$", "$1 more needed"], [')
rep(".nxq .nqd2.alld{color:#4F7D44;font-weight:700}",
    ".nxq .nqd2.alld{color:#4F7D44;font-weight:700}\n"
    "#sheet .ordr .oa .btn.g:disabled,.sheet .ordr .oa .btn.g:disabled{background:none!important;background-image:none!important;box-shadow:none!important;border:0!important;padding:0 2px!important;min-height:44px;flex:1 1 auto!important;text-align:left;justify-content:flex-start;font:700 14px/1.2 var(--f-body,'Baloo 2'),sans-serif!important;color:#B0492B!important;transform:none!important;cursor:default}"
    "#sheet .ordr .oa .btn.g:disabled::before,#sheet .ordr .oa .btn.g:disabled::after,.sheet .ordr .oa .btn.g:disabled::before,.sheet .ordr .oa .btn.g:disabled::after{display:none!important}"
    ".ordr .ow .oxu{float:right;margin-left:8px;padding:1px 10px;border-radius:999px;background:#FBE9B4;color:#7A4E0E;font:400 15px/1.5 var(--f-game);font-style:normal;white-space:nowrap}"
    ".ordr:has([data-a=cnofind]) .oa{flex-wrap:nowrap!important}.ordr .oa [data-a=cnofind]{order:3;margin-left:0!important;flex:0 0 auto}"
    ".ordr{margin-top:10px;padding-bottom:10px}.ordr .oa .btn{min-height:44px}")

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
