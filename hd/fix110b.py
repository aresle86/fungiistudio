# v110b (anh Ares 4/11 chiều)
#  1. Ghé vườn bạn: thẻ Ngoại nhờ trống vẫn hiện (CSS display:block!important đè thuộc tính hidden) → ẩn đúng.
#  2. Lời báo lỗi bị lặp chữ ("Chưa chưa hái giùm được con được") → câu gọn.
#  3. Thẻ việc: 3 ô chiếm chỗ, rối mắt → trở lại một việc như trước (icon trái, tên, thanh) + dòng nhỏ "Việc hôm nay N/5 ›"
#     (có quà chờ nhận thì dòng đó vàng "· có quà nhận"); vẫn giữ nét mới (viền, ghim, thanh vàng, nhãn CẤP).
# Dùng: python3 fix110b.py live/v110a.html live/v110b.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:80], c, n); s = s.replace(a, b)

# 1 + 3: CSS
rep(".nxq{display:block!important;max-width:none!important;width:min(392px,calc(100vw - 24px))!important;padding:18px 8px 8px!important;border-radius:16px!important}",
    ".nxq{display:block!important;max-width:none!important;width:min(300px,calc(100vw - 110px))!important;padding:16px 8px 6px!important;border-radius:16px!important}\n.nxq[hidden],body.sheeton .nxq,body.tooling .nxq,body.visit .nxq{display:none!important}\n.nxq .q.one{flex-direction:row;align-items:center;text-align:left;gap:8px;padding:6px 8px}\n.nxq .q.one>img{width:34px;height:34px;flex:none}\n.nxq .q.one .qt{flex:1;min-width:0;display:flex;flex-direction:column;gap:4px}\n.nxq .q.one .qt>b{font:400 13px/1.15 var(--f-game);color:var(--vgK);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}\n.nxq .q.one .tag{left:auto;right:-6px}\n.nxq .nqd2{display:block;margin:5px 2px 0;font:600 12px var(--f-body);color:#8A5D3B;cursor:pointer}\n.nxq .nqd2.gift{color:#9A6E12}")
rep("@media (max-width:560px){ .nxq{left:12px!important;right:12px!important;width:auto!important} }", "")
# 3: một ô
rep("""  const h = `<small>${go ? 'LÀM LIỀN' : lab}</small><span class="qrow">${slots.join('')}</span>`;""",
    """  let foot = ''; try { ensureTasks(); const L3 = ST.tasks.list, dn = L3.filter(x => x.done).length, gift = L3.some(x => x.done && x.cl === false); foot = `<span class="nqd2${gift ? ' gift' : ''}" data-d="1">Việc hôm nay ${dn}/${L3.length}${gift ? ' · có quà nhận' : ''} ›</span>`; } catch (e) {}
  const one = `<span class="q one" data-a="${act}"><img src="${ic}" alt=""><span class="qt"><b>${tShort(t)}</b>${chips ? `<span class="nqcs">${chips}</span>` : barH(f, em)}${steps}</span>${lab === 'NGOẠI NHỜ' ? '<span class="tag">CẤP</span>' : ''}</span>`;   /* một việc, như trước: đỡ rối mắt */
  const h = `<small>${go ? 'LÀM LIỀN' : lab}</small><span class="qrow">${one}</span>${isTask ? '' : foot}`;""")
# 2: câu báo lỗi
rep("netDown(e) ? `Mạng chập chờn quá${what ? ', ' + what : ''}.` : `Chưa ${what || 'làm'} được, thử lại chút nữa nghe con.`; };",
    "netDown(e) ? `Mạng chập chờn quá${what ? ', ' + what : ''}.` : `${what ? what[0].toUpperCase() + what.slice(1) : 'Chưa làm được'}, thử lại chút nữa nghe con.`; };")

# 4. Bình tưới trên khay: luôn có, số liếp đang khô dần (độ ẩm < 60%), chạm là tưới hết một lượt (anh Ares: tưới trước khi thoát game)
rep('<span class="tg">Tưới</span></button>', '<span class="tg">Tưới</span><span class="tn" id="tCanN"></span></button>')
rep("TRAY.water.addEventListener('click', () => setTool(TOOL && TOOL.kind === 'water' ? null : { kind: 'water' }))",
    "TRAY.water.addEventListener('click', () => { if (TOOL) clearTool(); if (VISIT){ const id = visWaterIds()[0]; if (!id) return toast('Vườn bạn liếp nào cũng ướt rồi, hái giùm liếp chín cũng được đổi công nghe con.', 'vui', { now: true }); try { camTo(new T.Vector3(PV[id].cx, .3, PV[id].cz)); } catch (e) {} visitTap(id); return; } const ids = dryIds(); if (!ids.length) return toast('Liếp nào cũng còn ẩm, chưa cần tưới con.', 'vui', { now: true }); ids.forEach((id, i) => setTimeout(() => { try { act.water(id); } catch (e) {} }, i * 140)); toast(`Tưới ${ids.length} liếp`, 'vui', { now: true }); })")
rep("try { const sn = Object.values(ST.seeds || {})",
    "try { const nw = VISIT ? visWaterIds().length : dryIds().length; TRAY.water.hidden = false; TRAY.water.classList.toggle('zero', !nw); $('#tCanN').textContent = nw || ''; } catch (e) {} try { const sn = Object.values(ST.seeds || {})")
rep("const TRAY = { seed: $('#tSeed'),", "const visWaterIds = () => VISIT ? PLOTS.filter(P => { const p = ST.plots[P.id]; return p && p.crop && !P.trellis && !p.helped && !ripe(p) && p.moist < .9; }).map(P => P.id) : [];   /* ghé vườn bạn: liếp tưới giùm được, mỗi liếp một công */\nconst dryIds = () => PLOTS.filter(P => { const p = ST.plots[P.id]; return p && p.crop && !p.dead && !P.trellis && !(CROPS[p.crop] && CROPS[p.crop].tree) && !ripe(p) && p.moist < .6; }).map(P => P.id);   /* liếp đang khô dần: ẩm dưới 60% */\nconst TRAY = { seed: $('#tSeed'),")
rep(".tl .tn:empty,.tl.zero .tn{display:none!important}", ".tl .tn:empty,.tl.zero .tn{display:none!important} #tCan.zero img{opacity:.55} html body.visit #tray{display:flex!important} html body.visit #tray>.tl:not(#tCan){display:none!important}")

rep("$('#nxq').addEventListener('click', e => { sfx('pick');", "$('#nxq').addEventListener('click', e => { if (VISIT) return; sfx('pick');")
# 5. hái trộm (hái ké) vườn bạn: 3 món/ngày (anh Ares 4/11); server mv2_act steal 5 → 3
rep("DOICONG = 5", "DOICONG = 3")
rep("const BUILD = 'v110a'", "const BUILD = 'v110b'")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
