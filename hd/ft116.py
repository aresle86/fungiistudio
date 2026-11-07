# ft116: cây cổ tích thành sự kiện lớn. python3 ft116.py vào ra
#  - Lời đồn: Ngoại kể nhỏ bằng thẻ riêng (khung vàng, đom đóm, nhạc cổ tích), không tự tắt, có câu rủ làm.
#    Ba nấc: tới cấp (nấc 1), 3 ngày sau (nấc 2), 7 ngày sau (nấc 3, có điềm báo trong vườn), rồi cứ 4 ngày nhắc lại nấc 3.
#    Không hết hạn: tính theo ngày từ lúc tới cấp, người lên cấp xa vẫn được nhắc. Mỗi ngày tối đa một thẻ.
#  - Sổ cổ tích ghi lại "Ngoại có nói" + tiến độ; nút Sổ và thẻ Cổ tích có đốm sáng khi có lời mới.
#  - Điềm báo: đom đóm xoay ở chỗ cây sẽ mọc, chạm vô là Ngoại kể lại.
#  - Mở cây: trời ngả chạng vạng, đom đóm tụ về, cảnh riêng từng cây, nhạc cổ tích viết bằng code (điệu Oán), lật trang Sổ hiện tên truyện.
import sys, json
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:80], s.count(a))
    s = s.replace(a, b)

RUM = {
 'vusua': ['Hồi xưa có người má ngày nào cũng ra đầu ngõ ngóng con. Người ta nói đứa nào về thăm vườn đủ bảy bữa liền, chỗ người má đứng chờ sẽ có chuyện lạ. Con về với Ngoại mỗi ngày nghe.',
           'Con ráng về vườn mỗi ngày nghe. Đủ bảy ngày liền, không sót bữa nào, coi chuyện gì xảy ra.',
           'Thẻ về vườn đó con, đóng đủ bảy dấu liền một hơi. Sót một bữa là phải đếm lại từ đầu.'],
 'tretramdot': ['Ông bà mình nói, ai siêng như anh Khoai, mấy mùa cắm cúi bên giàn, là trong vườn có cây tre lạ mọc lên. Con siêng trồng khổ qua trên giàn coi.',
                'Giàn khổ qua đó con. Thu đủ ba vụ khổ qua trên giàn, Ngoại nghe nói vậy đó.',
                'Trồng khổ qua trên giàn, hái đủ ba lứa nghe con. Tre lạ nó chờ người siêng.'],
 'traucau': ['Chuyện trầu cau là chuyện anh em, vợ chồng thương nhau. Nhà nào bạn bè qua lại thăm nhau đông, Ngoại nghe nói có cây cau quấn dây trầu. Con chèo qua vườn bạn chơi đi.',
             'Con chèo xuồng qua vườn bạn, rủ bạn qua vườn mình nữa. Qua lại cho đủ năm lần coi.',
             'Thăm vườn bạn, hay bạn ghé vườn mình, đủ năm lần nghe con. Có qua có lại mới thương.'],
 'duahau': ['Hồi xưa có nhà bị đày ra đảo hoang, sống nhờ mấy hột chim thả xuống. Đất mé sông mà bỏ trống qua đêm, Ngoại hay thấy chim đáp lắm. Con chừa một ô coi.',
            'Con để trống một ô đất mé sông, tối ghé vườn ngó chim, sáng ra ghé lại coi thử.',
            'Chừa một ô mé sông đừng trồng gì hết. Tối nay sau tám giờ ghé vườn một chút, sáng mai ghé lại. Chim nó thả hạt ban đêm đó con.'],
 'khevang': ['Hồi xưa có cây khế, con chim lớn bay tới ăn rồi trả vàng. Cây khế nhà mình mà sai trái, biết đâu chim lạ cũng ghé. Con hái khế cho đều tay nghe.',
             'Hái khế cho đều tay nghe con, đủ năm vụ coi chim lạ có ghé không.',
             'Cây khế đó con, hái đủ năm vụ. Chim lớn nó canh cây nào sai trái.'],
 'sodua': ['Có đứa nhỏ sinh ra tròn như trái dừa mà thổi sáo hay nhứt xóm. Dừa mé sông mà cho trái đều, nghe đâu có trái biết nói. Con hái dừa đi.',
           'Con hái dừa đủ ba vụ coi, Ngoại nghe trái dừa nó lăn lộc cộc ban đêm.',
           'Cây dừa mé sông, hái đủ ba vụ nghe con. Có trái dừa nó đang chờ con đó.'],
}
EN = {
 RUM['vusua'][0]: "Long ago a mother waited at the lane's end for her child every day. They say whoever visits the garden seven days in a row will see something strange where she stood. Come see Grandma every day, dear.",
 RUM['vusua'][1]: 'Try to come to the garden every day, dear. Seven days in a row, not one missed, and see what happens.',
 RUM['vusua'][2]: 'The visit card, dear: stamp all seven in a row. Miss one day and it starts over.',
 RUM['tretramdot'][0]: 'The old folks say whoever works as hard as Khoai, seasons bent over the trellis, will see a strange bamboo grow in the garden. Try growing bitter melon on the trellis.',
 RUM['tretramdot'][1]: "The bitter melon trellis, dear. Harvest bitter melon three times on the trellis, that's what Grandma heard.",
 RUM['tretramdot'][2]: 'Grow bitter melon on the trellis and harvest it three times, dear. The strange bamboo waits for the hardworking.',
 RUM['traucau'][0]: 'The betel and areca tale is about brothers, husband and wife who love each other. In homes where friends visit often, Grandma heard, an areca palm wrapped in betel grows. Row over to a friend\'s garden.',
 RUM['traucau'][1]: 'Row over to a friend\'s garden, and invite them to ours too. Back and forth, five times.',
 RUM['traucau'][2]: 'Visit friends, or have them visit, five times, dear. Giving and receiving is how love grows.',
 RUM['duahau'][0]: 'Long ago a family was exiled to a desert island and lived on seeds the birds dropped. Leave riverbank soil bare overnight and Grandma often sees birds land. Leave one plot empty.',
 RUM['duahau'][1]: 'Leave one riverbank plot empty, come watch the birds at night, and check again in the morning.',
 RUM['duahau'][2]: "Leave one riverbank plot unplanted. Stop by after eight tonight, then again tomorrow morning. Birds drop seeds at night, dear.",
 RUM['khevang'][0]: 'Long ago a great bird ate from a starfruit tree and paid in gold. If our starfruit bears well, maybe a strange bird will come too. Keep harvesting the starfruit, dear.',
 RUM['khevang'][1]: 'Keep harvesting starfruit, dear. Five harvests, and see if the strange bird comes.',
 RUM['khevang'][2]: 'The starfruit tree, dear: harvest it five times. The great bird watches for a tree heavy with fruit.',
 RUM['sodua'][0]: "There was a child born round as a coconut who played the best flute in the hamlet. If the riverside coconut bears well, they say one coconut can talk. Go pick coconuts.",
 RUM['sodua'][1]: 'Harvest the coconut three times, dear. Grandma hears a coconut rolling about at night.',
 RUM['sodua'][2]: 'The riverside coconut: harvest it three times, dear. A coconut is waiting for you.',
 'Ngoại nghe đồn': 'Grandma heard a tale', 'Dạ, để con thử': "I'll try, Grandma", 'Coi Sổ cổ tích': 'Open the tale book', 'Ngoại có nói': 'Grandma said',
 'Nhà mình chưa có cây khế. Trồng một cây khế đi con, rồi hái đủ năm vụ.': "We don't have a starfruit tree yet. Plant one, dear, then harvest it five times.",
 'Nhà mình chưa có cây dừa. Trồng một cây dừa mé sông đi con, rồi hái đủ ba vụ.': "We don't have a coconut tree yet. Plant one by the river, dear, then harvest it three times.",
 'Ô mé sông đang trống, tối nay ghé vườn coi nghe.': 'A riverbank plot is empty. Stop by tonight, dear.',
 'Ô mé sông nào cũng đang trồng.': 'Every riverbank plot is planted.',
 'Ghi vô Sổ cổ tích': 'Written into the tale book', 'Chạm để nghe Ngoại kể': 'Tap to hear Grandma tell it',
}
RX = [['^Thẻ về vườn đang (\\d+)/7 ngày liền\\.$', 'Visit card: $1/7 days in a row.'],
      ['^Đã thu (\\d+)/3 vụ khổ qua trên giàn\\.$', 'Bitter melon on the trellis: $1/3 harvests.'],
      ['^Đã qua lại (\\d+)/5 lần\\.$', 'Visits back and forth: $1/5.'],
      ['^Đã hái (\\d+)/5 vụ khế\\.$', 'Starfruit harvests: $1/5.'],
      ['^Đã hái (\\d+)/3 vụ dừa\\.$', 'Coconut harvests: $1/3.']]
json.dump(EN, open('i18n/en_v116.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
json.dump(RX, open('i18n/rx_a116.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

CSS = r"""
.ftr{position:fixed;inset:0;z-index:90;display:flex;align-items:center;justify-content:center;padding:16px;background:rgba(24,16,34,.58);opacity:0;transition:opacity .35s}.ftr.on{opacity:1}
.ftrc{position:relative;max-width:350px;width:100%;background:linear-gradient(#FFFBF0,#FBF2DC);border:3px solid #D9A93A;border-radius:20px;padding:18px 18px 14px;text-align:center;box-shadow:0 0 0 5px rgba(255,214,110,.28),0 0 46px rgba(255,214,110,.6);transform:translateY(14px) scale(.96);transition:transform .45s cubic-bezier(.2,1.4,.4,1)}.ftr.on .ftrc{transform:none}
.ftrc img{width:96px;height:96px;filter:brightness(0) opacity(.55) drop-shadow(0 0 6px #FFD86A) drop-shadow(0 0 14px #FFE9A0);animation:ftrB 3s ease-in-out infinite}
.ftrc small{display:block;font:15px/1 var(--f-game);color:#9A6A1A;letter-spacing:.04em;margin:4px 0 8px}
.ftrc p{margin:0 0 8px;font-size:16px;line-height:1.5;color:#3E2716}.ftrc em{display:block;font-style:normal;font-size:13px;color:#7A4E96;margin-bottom:10px}
.ftrb{display:flex;gap:8px;justify-content:center;flex-wrap:wrap}.ftrb button{min-height:44px;padding:0 16px;border-radius:99px;border:2px solid #C08A2A;background:#FFF6DC;font:16px var(--f-game);color:#5A3A1A}.ftrb button.go{background:#E8B848;color:#3E2716;border-color:#B07A1A}
.ftff{position:absolute;inset:0;pointer-events:none;overflow:hidden;border-radius:18px}.ftff i{position:absolute;width:6px;height:6px;border-radius:50%;background:#FFE88A;box-shadow:0 0 8px 3px rgba(255,226,120,.8);animation:ftrF 5s ease-in-out infinite}
@keyframes ftrF{0%,100%{transform:translate(0,0);opacity:.2}50%{transform:translate(14px,-22px);opacity:1}}@keyframes ftrB{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
.ftb{position:absolute;top:-3px;left:-3px;width:12px;height:12px;border-radius:50%;background:#FFE36A;box-shadow:0 0 8px 3px rgba(255,214,90,.9);animation:ftrB 1.6s ease-in-out infinite;pointer-events:none}
.ftrs{margin-top:6px;padding:6px 8px;border-left:3px solid #E2B84A;background:#FFF8E4;border-radius:6px}.ftrs i{display:block;font-size:12px;color:#9A6A1A;font-style:normal}.ftc.no .ftrs p{font-style:normal;color:#4A2F1E}.ftrs span{display:block;font-size:12px;color:#7A4E96}
.ftv{position:fixed;inset:0;z-index:91;display:flex;align-items:center;justify-content:center;pointer-events:auto;opacity:0;transition:opacity .5s}.ftv.on{opacity:1}
.ftvc{text-align:center;padding:22px 26px;border-radius:22px;background:radial-gradient(circle,rgba(255,246,214,.97),rgba(251,236,196,.94));border:3px solid #E2B84A;box-shadow:0 0 70px rgba(255,214,110,.8);transform:rotateY(80deg);transition:transform .8s cubic-bezier(.2,1.2,.4,1)}.ftv.on .ftvc{transform:none}
.ftvc img{width:120px;height:120px;filter:brightness(0) opacity(.5) drop-shadow(0 0 0 #FFD86A);transition:filter 1.4s .5s}.ftv.on .ftvc img{filter:drop-shadow(0 0 14px #FFD86A)}
.ftvc b{display:block;font:24px/1.2 var(--f-game);color:#4A2F1E;margin-top:6px}.ftvc small{display:block;font-size:13px;color:#9A6A1A;margin-top:4px}.ftvc em{display:block;font-style:normal;font-size:12px;color:#7A4E96;margin-top:10px}
.ftblk{position:fixed;inset:0;z-index:89}
"""
rep('.ftc{display:flex;', CSS.replace('\n', ' ') + ' .ftc{display:flex;')

JS = r"""
const FTRUM = %RUM%;
const FTCOL = { vusua: '#FFF4D8', tretramdot: '#C8F08A', traucau: '#FF8A7A', duahau: '#9BE07A', khevang: '#FFD24A', sodua: '#BFEFFF' };
var FTDUSK = null, CERE = null;
function ftOwnTree(c){ return PLOTS.some(P => P.tree === c && ST.plots[P.id] && ST.plots[P.id].crop); }
function ftrPrg(k){ try {
  if (k === 'vusua') return `Thẻ về vườn đang ${(ST.dd && ST.dd.n) || 0}/7 ngày liền.`;
  if (k === 'tretramdot') return `Đã thu ${Math.min(3, ST.kqHv || 0)}/3 vụ khổ qua trên giàn.`;
  if (k === 'traucau') return `Đã qua lại ${Math.min(5, (ST.guestN || 0) + (ST.visitOut || 0))}/5 lần.`;
  if (k === 'duahau') return PLOTS.some(P => P.zone === 'song' && ST.open.includes(P.id) && !ST.plots[P.id].crop) ? 'Ô mé sông đang trống, tối nay ghé vườn coi nghe.' : 'Ô mé sông nào cũng đang trồng.';
  if (k === 'khevang') return ftOwnTree('khe') ? `Đã hái ${Math.min(5, ST.kheHv || 0)}/5 vụ khế.` : 'Nhà mình chưa có cây khế. Trồng một cây khế đi con, rồi hái đủ năm vụ.';
  if (k === 'sodua') return ftOwnTree('dua') ? `Đã hái ${Math.min(3, ST.duaHv || 0)}/3 vụ dừa.` : 'Nhà mình chưa có cây dừa. Trồng một cây dừa mé sông đi con, rồi hái đủ ba vụ.';
} catch (e) {} return ''; }
/* lời đồn: còn chờ cây nào (tới cấp, chưa mọc) */
const ftrWait = k => !VISIT && (ST.lv || 1) >= FT[k].lv && !ST.ft[k] && !(k === 'vusua' && ST.vsReady);
const ftrDue = R => { const d = 864e5 / (ST.spd || 1); return !R.n ? R.t0 + 40000 / (ST.spd || 1) : R.n === 1 ? R.last + 3 * d : R.n === 2 ? R.last + 4 * d : R.last + 4 * d; };
function ftOmen(k){ const R = ST.ftr && ST.ftr[k]; return !!(R && R.n >= 3 && ftrWait(k)); }
function ftrCheck(){ if (VISIT) return; ST.ftr = ST.ftr || {}; ftrBadge(); const now = Date.now(); let pick = null;
  for (const k of FTK){ if (!ftrWait(k)) continue; const R = ST.ftr[k] = ST.ftr[k] || { t0: now, n: 0, last: 0, h: [] }; if (!pick && now >= ftrDue(R)) pick = k; }
  if (!pick || ST.ftrD === dayKey() || CERE) return; let b = true; try { b = busy() || !ng.hidden; } catch (e) {} if (b) return; ftrShow(pick); }
function ftrShow(k, again){ const R = ST.ftr[k] = ST.ftr[k] || { t0: Date.now(), n: 0, last: 0, h: [] }; const i = Math.min(2, again ? 2 : R.n), txt = FTRUM[k][i];
  if (!again){ R.n++; R.last = Date.now(); ST.ftrD = dayKey(); }
  if (!R.h.includes(i)) R.h.push(i); ST.ftrNew = 1; save(); ftrBadge();
  let el = document.querySelector('.ftr'); if (el) el.remove(); el = document.createElement('div'); el.className = 'ftr';
  const img = UIC['ft_' + k] || ICON.la, pg = i ? ftrPrg(k) : '';
  el.innerHTML = `<div class="ftrc"><div class="ftff">${[...Array(9)].map((_, j) => `<i style="left:${8 + j * 10}%;top:${15 + (j * 37) % 70}%;animation-delay:${-j * .6}s"></i>`).join('')}</div><img src="${img}" alt=""><small>Ngoại nghe đồn</small><p>${txt}</p>${pg ? `<em>${pg}</em>` : ''}<div class="ftrb"><button data-a="so">Coi Sổ cổ tích</button><button class="go" data-a="ok">Dạ, để con thử</button></div></div>`;
  document.body.appendChild(el); if (EN) enWalk(el); requestAnimationFrame(() => el.classList.add('on'));
  el.addEventListener('click', e => { const a = e.target.closest('button'); if (!a) return; el.classList.remove('on'); setTimeout(() => el.remove(), 350); sfx('pop'); if (a.dataset.a === 'so') openBook('cotich'); });
  ftMotif(); }
function ftrBadge(){ const b = $('#bSo'); if (!b) return; let d = b.querySelector('.ftb'); if (ST.ftrNew && !d){ d = document.createElement('i'); d.className = 'ftb'; b.appendChild(d); } else if (!ST.ftrNew && d) d.remove(); }
function ftrSo(k){ const R = ST.ftr && ST.ftr[k]; if (!R || !R.h || !R.h.length || !ftrWait(k)) return ''; const pg = ftrPrg(k);
  return `<div class="ftrs"><i>Ngoại có nói</i>${R.h.map(i => `<p>${fxT(FTRUM[k][i])}</p>`).join('')}${pg ? `<span>${fxT(pg)}</span>` : ''}</div>`; }
/* ---- nhạc cổ tích: điệu Oán (hò xự xang xê cống), xự với cống hơi lệch như đàn ca tài tử, có nhấn ---- */
const OAN = [392, 460, 523.25, 631, 698.46, 783.99, 920, 1046.5, 1262, 1396.9, 1569.98, 1840, 2093];
function ftA(){ if (ST.snd === false) return null; try { AC = AC || new (window.AudioContext || window.webkitAudioContext)(); if (AC.state === 'suspended') AC.resume(); return AC; } catch (e) { return null; } }
function ftPad(t, dur, fs, v){ const d = out(); for (const f of fs) tone(t, dur, f, null, v, d, 'sine', Math.min(1.2, dur * .35)); }
function ftFlute(t, dur, f, v){ const d = out(), o = AC.createOscillator(), lf = AC.createOscillator(), lg = AC.createGain(), g = AC.createGain(); o.type = 'sine'; o.frequency.setValueAtTime(f, t); lf.frequency.value = 5.4; lg.gain.setValueAtTime(0, t); lg.gain.linearRampToValueAtTime(f * .012, t + Math.min(.35, dur * .5)); lf.connect(lg).connect(o.frequency); g.gain.setValueAtTime(.0001, t); g.gain.linearRampToValueAtTime(v, t + .07); g.gain.setValueAtTime(v, t + dur * .75); g.gain.exponentialRampToValueAtTime(.0001, t + dur); o.connect(g).connect(d); o.start(t); lf.start(t); o.stop(t + dur + .05); lf.stop(t + dur + .05); nzz(t, Math.min(.25, dur), f * 2, 2, v * .18, d); }
function ftChirp(t, v){ const d = out(); tone(t, .09, 2700 + Math.random() * 500, 3600, v, d, 'sine', .005); tone(t + .1, .07, 3000, 2500, v * .7, d, 'sine', .005); }
function ftMotif(){ const A = ftA(); if (!A) return; try { const t = A.currentTime + .03; ftPad(t, 2.8, [1046.5, 1569.98], .022); pluck(OAN[4], t + .05, .3, .995); pluck(OAN[3], t + .38, .32, .995, .03); pluck(OAN[2], t + .8, .34, .996, -.02); tone(t + 1.25, 1.2, 2093, null, .028, out(), 'sine', .01); [8, 9, 10].forEach((i, j) => pluck(OAN[i], t + 1.5 + j * .07, .14, .99)); } catch (e) {} }
function ftDuck(sec){ try { const B = bus(); if (!B) return; const g = B.mus.dk.gain, t = AC.currentTime; g.cancelScheduledValues(t); g.setTargetAtTime(.18, t, .3); g.setTargetAtTime(1, t + sec, .8); } catch (e) {} }
function ftCue(k, pop){ const A = ftA(); if (!A) return; try { ftDuck(pop + 4); const t = A.currentTime + .03, d = out(), P = t + pop;
  ftPad(t, pop + 1.2, [523.25, 783.99, 1046.5], .016); pluck(OAN[4], t + .1, .3, .995); pluck(OAN[3], t + .45, .32, .995, .03); pluck(OAN[2], t + .9, .34, .996, -.02);
  const m = t + 1.3;
  if (k === 'vusua'){ [[0, 7, 0], [.45, 6, -.03], [.9, 5, 0], [1.3, 3, .035], [1.7, 4, -.02]].forEach(([dt, i, b]) => pluck(OAN[i], m + dt, .36, .997, b)); }
  else if (k === 'tretramdot'){ let x = 0; [.3, .26, .22, .19, .16, .14, .12, .1, .09, .08].forEach((g, j) => { x += g; songlang(m + x, .45); pluck(OAN[2 + Math.min(9, j)], m + x + .02, .2, .992); }); }
  else if (k === 'traucau'){ [2, 4, 5, 7].forEach((i, j) => { pluck(OAN[i], m + j * .42, .32, .996, j === 1 ? .03 : 0); pluck(OAN[i + 2], m + j * .42 + .21, .22, .995); }); }
  else if (k === 'duahau'){ for (let j = 0; j < 7; j++) ftChirp(m + j * .26 + Math.random() * .08, .035); [2, 3, 4, 5, 6, 7, 8].forEach((i, j) => pluck(OAN[i], m + .2 + j * .22, .26, .994)); }
  else if (k === 'khevang'){ for (let j = 0; j < 3; j++) nzz(m + j * .6, .5, 500, 1, .07, d, 2200); for (let j = 0; j < 9; j++) tone(m + .1 + j * .2, .9, OAN[8 + (j * 3) % 5] * 1.5, null, .022, d, 'sine', .005); }
  else if (k === 'sodua'){ [[0, 5, .5], [.55, 6, .3], [.9, 7, .7], [1.65, 5, .35], [2.05, 7, .9]].forEach(([dt, i, du]) => ftFlute(m + dt * .9, du, OAN[i], .05)); }
  [2, 3, 4, 5, 6, 7, 8, 9, 10].forEach((i, j) => pluck(OAN[i], P + j * .035, .28, .996)); tone(P, 2.4, 2093, null, .045, d, 'sine', .01); tone(P + .05, 2, 3136, null, .02, d, 'sine', .01); ftPad(P, 3.2, [523.25, 698.46, 1046.5, 1396.9], .02);
  pluck(OAN[7], P + 1.3, .3, .997, .03); pluck(OAN[5], P + 1.8, .28, .997); pluck(OAN[7], P + 2.4, .3, .998);
} catch (e) {} }
/* ---- trời ngả chạng vạng trong lúc mở cây ---- */
function ftSkyH(h){ if (!FTDUSK) return h; const t = (performance.now() - FTDUSK.t0) / 1000, D = FTDUSK.dur; if (t > D){ FTDUSK = null; return h; } const w = t < 1.2 ? t / 1.2 : t > D - 1.5 ? (D - t) / 1.5 : 1, e = w * w * (3 - 2 * w); return h + (18.35 - h) * e; }
/* ---- điềm báo: đom đóm xoay ở chỗ cây sẽ mọc ---- */
const OMV = {};
function omTick(k, V, t){ let O = OMV[k]; const on = ftOmen(k) && !VISIT; if (!on){ if (O) O.g.visible = false; return; } if (!O){ const g = new T.Group(), ms = []; const mat = new T.MeshBasicMaterial({ color: FTCOL[k], transparent: true, opacity: .9, blending: T.AdditiveBlending, depthWrite: false }); for (let i = 0; i < 14; i++){ const m = new T.Mesh(new T.SphereGeometry(.035, 6, 4), mat); g.add(m); ms.push(m); } const halo = new T.Mesh(new T.CylinderGeometry(.5, .5, .04, 20), new T.MeshBasicMaterial({ color: FTCOL[k], transparent: true, opacity: .18, blending: T.AdditiveBlending, depthWrite: false })); halo.position.y = .03; g.add(halo); S.add(g); O = OMV[k] = { g, ms, halo }; }
  const pp = ftPos(k); O.g.visible = true; O.g.position.set(pp[0], 0, pp[1]); V.hit.position.set(pp[0], 1.2, pp[1]);
  O.ms.forEach((m, i) => { const a = t * (.6 + (i % 3) * .15) + i * 2.4, r = .35 + (i % 4) * .12; m.position.set(Math.cos(a) * r, .3 + (i % 5) * .22 + Math.sin(t * 1.3 + i) * .12, Math.sin(a) * r); m.scale.setScalar(.7 + .5 * Math.sin(t * 3 + i)); });
  O.halo.material.opacity = .12 + .08 * Math.sin(t * 2); if (Math.random() < .01) puff('spark', pp[0] + R(-.3, .3), .5, pp[1] + R(-.3, .3), 1, FTCOL[k], .4); }
/* ---- cảnh mở cây: chung + riêng từng cây ---- */
function ftAdd(geo, col, op = 1, add = true){ const m = new T.Mesh(geo, new T.MeshBasicMaterial({ color: col, transparent: true, opacity: op, blending: add ? T.AdditiveBlending : T.NormalBlending, depthWrite: !add })); m.userData.own = 1; S.add(m); CERE.objs.push(m); return m; }
function ftStd(geo, col){ const m = new T.Mesh(geo, new T.MeshStandardMaterial({ color: col, flatShading: true, roughness: .8 })); m.userData.own = 1; S.add(m); CERE.objs.push(m); return m; }
/* chim lớn ăn khế: đúng mẫu đậu ngọn cây khế vàng (mình đỏ, đầu vàng, cánh bốn màu, đuôi dài) */
function ftKvBird(){ const bd = new T.Group(), pr = ROOT; ROOT = bd; M(sph(.12, 8, 6), '#C24A2E', 0, 0, 0, { p: bd, s: [1.5, .9, .9] }); M(sph(.075, 7, 5), '#E3B23C', .18, .1, 0, { p: bd }); M(sph(.015, 5, 4), '#1A1A1A', .22, .12, .05, { p: bd }); M(sph(.015, 5, 4), '#1A1A1A', .22, .12, -.05, { p: bd }); M(cone(.03, .1, 4), '#F5D27A', .28, .09, 0, { p: bd, r: [0, 0, -Math.PI / 2] }); M(cone(.02, .08, 4), '#C24A2E', .17, .2, 0, { p: bd, r: [0, 0, .4] }); bd.userData.w = []; for (const sg of [-1, 1]){ const w = G(0, .06, sg * .08, 0, bd); w.rotation.x = sg * .9; w.userData.sg = sg; bd.userData.w.push(w); for (let i = 0; i < 4; i++) M(box(.28 - i * .04, .015, .07), ['#9E3B24', '#C24A2E', '#E3B23C', '#2E5585'][i], -.04 - i * .02, i * .005, sg * (.04 + i * .05), { p: w }); } for (let i = 0; i < 3; i++) M(box(.3, .01, .05), ['#E3B23C', '#2E5585', '#C24A2E'][i], -.28, -.02 + i * .02, (i - 1) * .04, { p: bd, r: [0, (i - 1) * .2, .3] }); ROOT = pr; S.add(bd); CERE.objs.push(bd); return bd; }
/* chim sáo ngậm hạt: đúng mẫu bay quanh trái dưa Mai An Tiêm */
function ftSao(){ const bird = new T.Group(), pr = ROOT; ROOT = bird; bird.userData.wg = []; M(sph(.05, 8, 6), '#2B3446', 0, .05, 0, { p: bird, s: [1.5, 1, 1.05] }); M(sph(.036, 7, 5), '#2B3446', .07, .095, 0, { p: bird }); M(cone(.012, .045, 5), '#F2C230', .115, .09, 0, { p: bird, r: [0, 0, -Math.PI / 2] }); for (const sx of [-1, 1]){ M(sph(.008, 4, 3), '#FBF7EE', .09, .105, sx * .025, { p: bird, cast: false }); const wg = G(-.01, .075, sx * .03, 0, bird); wg.userData.sx = sx; bird.userData.wg.push(wg); M(box(.09, .012, .07), '#3E4A5E', 0, 0, sx * .04, { p: wg, r: [0, 0, .1] }); M(box(.03, .008, .025), '#FBF7EE', -.02, .003, sx * .065, { p: wg, cast: false }); } M(box(.07, .01, .04), '#2B3446', -.09, .06, 0, { p: bird, r: [0, 0, .35] }); M(sph(.01, 5, 4), '#3A2A1A', .14, .085, 0, { p: bird, cast: false }); ROOT = pr; bird.scale.setScalar(2.2); S.add(bird); CERE.objs.push(bird); return bird; }
const ftFace = (o, vx, vz) => { o.rotation.y = -Math.atan2(vz, vx); };
function ftCere(k){ const pp = ftPos(k), col = FTCOL[k], c = new T.Vector3(pp[0], 0, pp[1]); CERE = { k, t: 0, pop: 3.3, end: 6.4, objs: [], c, col, x: {} }; FTDUSK = { t0: performance.now(), dur: 9.5 };
  try { camTo(new T.Vector3(pp[0], .6, pp[1]), Math.max(cam.zoom, DEFZ() * 1.35)); } catch (e) {} ftCue(k, CERE.pop); buzz(15);
  const blk = document.createElement('div'); blk.className = 'ftblk'; document.body.appendChild(blk); CERE.blk = blk; try { ng.hidden = true; sayT = 0; } catch (e) {}
  const X = CERE.x; X.ff = []; for (let i = 0; i < 30; i++) X.ff.push({ m: ftAdd(new T.SphereGeometry(.04, 6, 4), col, .95), a: i * .9, r: 2.2 + (i % 5) * .25, y: .2 + (i % 7) * .3 });
  X.col = ftAdd(new T.CylinderGeometry(.32, .45, 3.4, 18, 1, true), col, 0); X.col.position.set(pp[0], 1.7, pp[1]);
  X.ring = ftAdd(new T.TorusGeometry(.5, .04, 6, 32), col, 0); X.ring.rotation.x = Math.PI / 2; X.ring.position.set(pp[0], .05, pp[1]);
  if (k === 'vusua'){ X.pet = []; for (let i = 0; i < 40; i++){ const m = ftAdd(new T.PlaneGeometry(.07, .05), '#FFFFFF', .9, false); const a = R(0, 6.28), r = R(.2, 1.6); X.pet.push({ m, x: Math.cos(a) * r, z: Math.sin(a) * r, y: R(2.4, 4.2), s: R(.25, .5), w: R(0, 6) }); } }
  if (k === 'tretramdot'){ X.seg = []; let d = 1.3; [.3, .26, .22, .19, .16, .14, .12, .1].forEach((g2, i) => { d += g2; const [sx, sz] = FTDOT.spots[(i * 3) % FTDOT.spots.length], m = ftStd(new T.CylinderGeometry(.06, .066, .13, 7), '#D9B24A'); m.position.set(sx, .07, sz); m.rotation.set(0, i, Math.PI / 2); m.scale.setScalar(.001); X.seg.push({ m, d }); }); }
  if (k === 'traucau'){ X.o = [ftAdd(new T.SphereGeometry(.09, 10, 8), '#F2ECDA', 1), ftAdd(new T.SphereGeometry(.09, 10, 8), '#B8E08A', 1), ftAdd(new T.SphereGeometry(.08, 10, 8), '#5FBF4A', 1)]; }
  if (k === 'duahau'){ X.b = []; for (let i = 0; i < 5; i++) X.b.push({ g: ftSao(), dz: (i - 2) * .4, dt: i * .16 }); X.sd = []; for (let i = 0; i < 6; i++){ const m = ftAdd(new T.SphereGeometry(.05, 8, 6), '#FFE9A0', .95); m.visible = false; X.sd.push({ m, t0: 1.6 + i * .18, x: R(-.4, .4), z: R(-.4, .4) }); } }
  if (k === 'khevang'){ X.bird = ftKvBird(); X.bird.scale.setScalar(1.3); }
  if (k === 'sodua'){ X.coco = soDua(true); X.coco.scale.setScalar(1.4); S.add(X.coco); CERE.objs.push(X.coco); }
  CERE.last = CERE.t0 = performance.now(); }
function cereTick(){ const C = CERE; if (!C) return; const now = performance.now(), dt = Math.min(.1, (now - C.last) / 1000); C.last = now; C.t += dt; const t = C.t, P = C.pop, c = C.c, X = C.x, k = C.k, e = Math.min(1, t / P), ee = e * e * (3 - 2 * e);
  X.ff.forEach((f, i) => { if (t < P){ const a = f.a + t * (1.2 + ee * 3), r = f.r * (1 - ee) + .05; f.m.position.set(c.x + Math.cos(a) * r, f.y * (1 - ee) + .6 * ee + Math.sin(t * 3 + i) * .08, c.z + Math.sin(a) * r); f.m.visible = true; } else f.m.visible = false; });
  X.col.material.opacity = t < P ? .05 + .25 * ee : Math.max(0, .55 - (t - P) * .22); X.col.scale.set(1, t < P ? .3 + .7 * ee : 1 + (t - P) * .1, 1);
  if (t >= P){ const q = t - P; X.ring.material.opacity = Math.max(0, .8 - q * .5); X.ring.scale.setScalar(1 + q * 4); }
  if (!C.popped && t >= P){ C.popped = 1; for (let i = 0; i < 40; i++) puff('spark', c.x + R(-.2, .2), R(.3, 1.6), c.z + R(-.2, .2), 1, i % 2 ? C.col : '#FFF6C8', 1.6); for (let i = 0; i < 10; i++) puff('leaf', c.x, .4, c.z, 1, '#86B06A', 1); buzz(30); setTimeout(() => ftReveal(k), 450); }
  if (k === 'vusua') X.pet.forEach(p => { if (t < .8) { p.m.visible = false; return; } p.m.visible = true; p.y -= dt * p.s; p.w += dt * 2; p.m.position.set(c.x + p.x + Math.sin(p.w) * .15, Math.max(.02, p.y), c.z + p.z); p.m.rotation.set(p.w, p.w * .7, 0); });
  if (k === 'tretramdot') X.seg.forEach(s => { const u = (t - s.d) / 1.1; if (u < 0 || u > 1){ s.m.scale.setScalar(.001); return; } s.m.scale.setScalar(Math.sin(u * Math.PI) * 1.2 + .001); s.m.position.y = .07 + Math.sin(u * Math.PI) * .12; if (!s.hit){ s.hit = 1; for (let i = 0; i < 6; i++) puff('spark', s.m.position.x, .15, s.m.position.z, 1, '#FFE36A', .6); } });   /* đốt tre lóe lên rải rác quanh vườn, mai mốt phải đi lượm */
  if (k === 'traucau') X.o.forEach((o, i) => { const a = t * 3.2 + i * 2.09, r = (i === 2 ? 1.1 : .9) * (1 - ee) + .02; o.position.set(c.x + Math.cos(a) * r, .3 + ee * 1.7, c.z + Math.sin(a) * r); o.visible = t < P + .2; if (Math.random() < .3) puff('spark', o.position.x, o.position.y, o.position.z, 1, ['#F2ECDA', '#B8E08A', '#5FBF4A'][i], .2); if (t >= P && !C.red){ C.red = 1; for (let j = 0; j < 24; j++) puff('spark', c.x, R(.4, 1.6), c.z, 1, '#D2402E', 1.1); } });   /* hai anh em với người vợ quấn quýt, tụ lại thành đá, cau, trầu; lóe đỏ màu miếng trầu */
  if (k === 'duahau'){ X.b.forEach(b => { const u = (t - b.dt) / 3; b.g.visible = u > 0 && u < 1; if (!b.g.visible) return; b.g.position.set(c.x - 5 + u * 10, 2.6 + Math.sin(u * 6 + b.dt * 4) * .15, c.z - 1 + b.dz + u * 1); ftFace(b.g, 10, 1); const f = Math.sin(t * 14 + b.dt * 9); for (const w of b.g.userData.wg) w.rotation.x = w.userData.sx * (f * .9 - .2); });   /* bầy sáo ngậm hạt bay ngang, nhả hạt xuống */ X.sd.forEach(s => { const u = (t - s.t0) / 1.3; s.m.visible = u > 0 && u < 1; if (!s.m.visible) return; s.m.position.set(c.x + s.x * (1 - u), 3 * (1 - u * u) + .05, c.z + s.z * (1 - u)); }); }
  if (k === 'khevang'){ const b = X.bird, u = t < P ? t : P + (t - P) * 1.8, a = u * 1.4, r = t < P ? 1.5 - ee * .5 : 1 + (t - P) * 1.6; b.position.set(c.x + Math.cos(a) * r, 1.5 + Math.sin(u * 2) * .2 + (t > P ? (t - P) * 1.1 : 0), c.z + Math.sin(a) * r); ftFace(b, -Math.sin(a), Math.cos(a)); const f = Math.sin(t * 6); for (const w of b.userData.w) w.rotation.x = w.userData.sg * (.9 + f * .55);   /* chim lớn ăn khế lượn vòng báo điềm, vỗ cánh rồi bay đi */ if (t > .8 && Math.random() < .5) puff('spark', b.position.x + R(-.3, .3), b.position.y - .1, b.position.z + R(-.3, .3), 1, '#FFD24A', .5); }
  if (k === 'sodua'){ if (t < P){ const a = t * 2.2, r = 1.3 * (1 - ee) + .02, roll = (1 - ee); X.coco.position.set(c.x + Math.cos(a) * r, .05 + Math.abs(Math.sin(t * 8)) * .07 * roll, c.z + Math.sin(a) * r); X.coco.rotation.set(Math.sin(t * 8) * .5 * roll, .75 + (1 - ee) * t * 5, Math.cos(t * 8) * .4 * roll); } else X.coco.visible = false; }   /* Sọ Dừa đang ngủ lăn lộc cộc vòng vòng rồi nằm yên vô ổ rơm */
  if (t >= C.end) cereEnd(); }
function cereEnd(){ const C = CERE; if (!C) return; for (const o of C.objs){ S.remove(o); o.traverse(m => { if (m.userData.own){ if (m.geometry) m.geometry.dispose(); if (m.material) m.material.dispose(); } }); } CERE = null; }
function ftReveal(k){ const D = FT[k]; let el = document.createElement('div'); el.className = 'ftv'; el.innerHTML = `<div class="ftvc"><img src="${UIC['ft_' + k] || ICON.la}" alt=""><b>${D.story}</b><small>Ghi vô Sổ cổ tích</small><em>Chạm để nghe Ngoại kể</em></div>`; document.body.appendChild(el); if (EN) enWalk(el); requestAnimationFrame(() => el.classList.add('on')); try { const r = el.querySelector('.ftvc').getBoundingClientRect(); setTimeout(() => confettiAt(r.left + r.width / 2, r.top + 40, 40, 1.2), 500); } catch (e) {}
  let done = false; const fin = () => { if (done) return; done = true; el.classList.remove('on'); setTimeout(() => el.remove(), 500); if (CERE && CERE.blk) CERE.blk.remove(); document.querySelectorAll('.ftblk').forEach(b => b.remove()); setTimeout(() => ftTell(k), 400); }; el.addEventListener('click', fin); setTimeout(fin, 5200); }
"""
JS = JS.replace('%RUM%', json.dumps(RUM, ensure_ascii=False))
rep("function ftTick(t){", JS + " function ftTick(t){")
# đom đóm điềm báo, hit cho điềm báo, giữ đốm sáng tới lúc bung, ẩn bong bóng lúc diễn
rep("V.hit.visible = on && !VISIT; V.b.visible = false; if (!on) continue;", "V.hit.visible = (on || ftOmen(k)) && !VISIT; V.b.visible = false; if (!on){ omTick(k, V, t); continue; } if (OMV[k]) OMV[k].g.visible = false;")
rep("const st = F.st === 3 && k === 'tretramdot' ? 3 : F.st, key = k + st;", "const st = CERE && CERE.k === k && CERE.t < CERE.pop ? 0 : (F.st === 3 && k === 'tretramdot' ? 3 : F.st), key = k + st;")
rep("if (st === 0) objBub(V, v, UIC['ft_' + k] || ICON.la, t, .9);", "if (CERE && CERE.k === k) V.b.visible = false; else if (st === 0) objBub(V, v, UIC['ft_' + k] || ICON.la, t, .9);")
rep("if (VISIT) return; fdBuild();", "cereTick(); if (VISIT) return; fdBuild();")
rep("function ftTap(k){ const F = ST.ft[k], D = FT[k], V = FTV[k]; if (!F) return; sfx('pick');", "function ftTap(k){ const F = ST.ft[k], D = FT[k], V = FTV[k]; if (!F){ if (ftOmen(k)) ftrShow(k, 1); return; } if (CERE) return; sfx('pick');")
rep("if (F.st === 0){ F.st = 1; F.t = Date.now(); for (let i = 0; i < 16; i++) puff('spark', AT[0], .2, AT[1], 1, '#FFE36A', 1.2); save(); stepMark('tree_ft'); setTimeout(() => ftTell(k), 500); return; }",
    "if (F.st === 0){ F.st = 1; F.t = Date.now(); save(); stepMark('tree_ft'); ftCere(k); return; }")
rep("sdHelp();\n  for (const k of FTK){", "sdHelp(); ftrCheck();\n  for (const k of FTK){")
rep("HOUR = hourAt(Date.now()); sky(HOUR);", "HOUR = hourAt(Date.now()); sky(ftSkyH(HOUR));")
rep(".ddt.on, .lvup:not([hidden])", ".ddt.on, .ftr, .ftv, .lvup:not([hidden])")
# Sổ: ghi lời Ngoại đã nói + tiến độ, xem rồi thì tắt đốm sáng
rep("<p>${F ? 'Có đốm sáng trong vườn, lại chạm thử đi con.' : fxT(FTRID[k] || '…')}</p>", "<p>${F ? 'Có đốm sáng trong vườn, lại chạm thử đi con.' : fxT(FTRID[k] || '…')}</p>${F ? '' : ftrSo(k)}")
rep("function pgCotich(part){", "function pgCotich(part){ if (ST.ftrNew){ ST.ftrNew = 0; save(); setTimeout(ftrBadge, 0); }")
rep("${BSTN[k]}</button>", "${BSTN[k]}${k === 'cotich' && ST.ftrNew ? '<i class=\"ftb\"></i>' : ''}</button>")
rep("if (!txt) return; if (!sayOkNow(o)) return;", "if (!txt) return; if (CERE && !o.now) return; if (!sayOkNow(o)) return;")
rep("tg.x = Math.max(-6.6, Math.min(11.5, tg.x));", "{ const mn = CERE ? -11 : -6.6; tg.x = !CERE && tg.x < mn - .01 ? tg.x + (mn - tg.x) * .06 : Math.max(mn, Math.min(11.5, tg.x)); }")
# Sọ Dừa: chỗ mọc cũ lấn ra sông, dời vô bờ
rep("sodua: { name: 'Sọ Dừa', story: 'Sọ Dừa', lv: 18, at: [-7.3, 8.5],", "sodua: { name: 'Sọ Dừa', story: 'Sọ Dừa', lv: 18, at: [-8.0, 7.5],")
# dưa hấu: chỗ cũ trùng lò ấp (cùng cấp 14), dời ra bãi mé sông giữa vú sữa với trầu cau
rep("duahau: { name: 'Dưa hấu', story: 'Mai An Tiêm', lv: 14, at: [-1.4, 6.2],", "duahau: { name: 'Dưa hấu', story: 'Mai An Tiêm', lv: 14, at: [-5.0, 5.3],")
# test hook
rep("get: () => ({ cloudInbox,", "get: () => ({ ftrCheck, ftrShow, ftOmen, ftCere, ftTap, ftrSo, OMV, get CERE(){ return CERE; }, cloudInbox,")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
