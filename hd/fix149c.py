# v149c (nháp): thang khoảng cách 4/8/12/16/24 (hud-hethong.md mục 10), áp mẫu cho Sổ.
# Sửa luôn lỗi nút "Góp xu" dính sát hàng ô vật phẩm.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:60], s.count(a))
    s = s.replace(a, b)
rep("BUILD = 'v149b'", "BUILD = 'v149c'")
A = ".tkc.bonus{background:#FFF8E0!important}"
rep(A, A + """
/* v149c: thang khoảng cách. Chỉ dùng --s1..--s6, không viết số lẻ */
:root{--s1:4px;--s2:8px;--s3:12px;--s4:16px;--s6:24px}
.uxbk .uxt{margin:var(--s4) 0 var(--s2);gap:var(--s2)}
.uxbk .tkc{margin-bottom:var(--s3)!important;padding:var(--s2) var(--s3)!important;gap:var(--s3)}
.uxbk .uxh{margin:0 0 var(--s3);padding:var(--s3);gap:var(--s3)}
.uxbk .qcd{padding:var(--s3)}
.uxbk .qgp{margin-top:var(--s3);gap:var(--s2)}
.uxbk .qgp+.cta{margin-top:var(--s3)}
.uxbk .cta{margin-bottom:var(--s3);gap:var(--s2)}
.uxbk .uxm{margin-top:var(--s3)}
.uxbk .smo{gap:var(--s2)}""")
# đổi mọi khoảng cách, cỡ chữ, bo góc lệch luật về nấc gần nhất (uiluat.py), rồi soát lại
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from uiluat import chuyen, soat
s = chuyen(s)
assert not soat(s), soat(s)[:5]
# --- chỗ bấm: mọi nút cao tối thiểu 44, hai chỗ bấm cách nhau tối thiểu 8 (mục 10.2) ---
st = [m.start() for m in __import__('re').finditer('</style>', s)]
assert len(st) >= 4, len(st)
i = st[3]
s = s[:i] + """
/* v149c: khoá chỗ bấm. Đặt cuối cùng để thắng mọi luật cũ */
.btn{min-height:44px!important}
.bkchip{min-height:44px!important;padding:4px 12px 4px 4px!important}
.bkchip img{width:24px!important;height:24px!important}
.tkc .tkgo::after{content:"";position:absolute;inset:-12px -8px}
.rgh{gap:16px!important}
.rgb{width:36px!important;height:36px!important;line-height:36px!important;position:relative}
.rgb::after{content:"";position:absolute;inset:-4px}
.fbar>.x{position:relative}
.fbar>.x::after{content:"";position:absolute;inset:-4px}
.stg{gap:8px!important}
.seg{gap:8px!important}
.rmap .mp{width:calc(50% - 8px)!important;height:calc(33.34% - 8px)!important;margin:4px!important}
.ui.bot>.row{gap:8px!important}
.volr input{height:44px;margin:0}
.uxm summary{min-height:44px;display:flex;align-items:center;box-sizing:border-box}
@media (max-width:760px){ body.sheeton #bCtr,body.sheeton #bSua{visibility:hidden!important} }
/* thanh trên: giờ + xu nằm chung một hàng trên máy hẹp */
@media (max-width:560px){ .clock{padding:8px 12px 8px 8px!important;gap:8px!important} }
@media (max-width:380px){ .bkpg{padding-left:16px!important;padding-right:16px!important} .stk .sts .st img{width:16px!important;height:16px!important} .stk .sts{column-gap:4px!important} }
.bkpg.r .acts:has(+ .bkng){padding-right:136px}
/* bản đồ bến: tên nằm sát ngay dưới hình của chính nó, cách xa hình ô dưới */
.rmap .mp{padding:0!important}
.rmap .lb{position:absolute;left:0;right:0;top:50%;margin:0 auto;width:max-content;max-width:100%;box-sizing:border-box;background:none!important;box-shadow:none!important}
/* đơn mới tới */
.leadt.moi{background:#C24A2E}
.ordr.vua{animation:ordin .45s ease-out}
@keyframes ordin{from{opacity:0;transform:translateY(8px)}}
@media (prefers-reduced-motion:reduce){ .ordr.vua{animation:none} }
""" + s[i:]
rep("s2.style.top = Math.round(r.bottom + (PHONE() ? 6 : 10)) + 'px'", "s2.style.top = Math.round(r.bottom + (PHONE() ? 8 : 12)) + 'px'")
# --- bản đồ bến: vòng chọn ôm gọn hình, không đè lên tên ---
rep("""${k === sel ? `<ellipse cx="2" cy="1" rx="50" ry="27" fill="#FFF8E8" fill-opacity=".7" stroke="#C24A2E" stroke-width="2.4" stroke-dasharray="7 5"/>` : ''}""", "")   # miếng nền đã viền đỏ chỗ đang chọn, bỏ vòng nét đứt
rep("""<g transform="translate(318 280)" stroke="${ink}" stroke-width="1.4"><path d="M0 -13L4 0 0 13 -4 0Z" fill="#F5D27A"/><path d="M-11 0H11"/></g>""", "")   # la bàn nằm đè góc miếng Vườn Ngoại
# mỗi chỗ một miếng nền riêng: hình với tên nằm chung một miếng, nhìn là biết của nhau
rep("""g += `<g transform="translate(${x} ${y})"${o ? '' : ' opacity=".34"'}>""", """g += `<rect x="${cx * 170 + 7}" y="${cy * 100 + 6}" width="156" height="88" rx="14" fill="#FFFBF2" fill-opacity="${k === sel ? .92 : .6}" stroke="${k === sel ? '#C24A2E' : '#D9C3A2'}" stroke-width="${k === sel ? 2.4 : 1.4}"/><g transform="translate(${x} ${y})"${o ? '' : ' opacity=".34"'}>""")
# --- đơn nhà bên: có xuồng ghé là báo, không tới lặng lẽ nữa ---
rep("""ST.ord.acc = 0; try { ST.ord.list.push(leadMake('nb') || ordMake()); } catch (e) {} }""",
    """ST.ord.acc = 0; try { const o = leadMake('nb') || ordMake(); ST.ord.list.push(o); ordCome(o); } catch (e) {} }
var ORDAW, ORDAWT, ORDPOP = 0;   /* số xuồng ghé lúc con đi vắng; lúc giỏ bật lên */
function ordPop(){ ORDPOP = performance.now(); try { sfx('goi'); } catch (e) {} try { const b = $('#icCho'); if (b && !matchMedia('(prefers-reduced-motion: reduce)').matches) b.animate([{ transform: 'scale(1)' }, { transform: 'scale(1.18) rotate(-6deg)' }, { transform: 'scale(1) rotate(4deg)' }, { transform: 'scale(1)' }], { duration: 500, easing: 'ease-out' }); } catch (e) {} }   /* có người ghé gọi mua: giỏ bật lên + tiếng gõ gọi, không chữ */
function ordCome(o){ o.moi = 1; let live = 0; try { live = KHLIVE; } catch (e) {} if (!live){ ORDAW = (ORDAW || 0) + 1; return; } ordPop(); }
function ordNew(o){ if (!o.moi) return 0; if (!o.seen) o.seen = Date.now(); const d = Date.now() - o.seen; return d < 600 ? 2 : d < 90e3 ? 1 : 0; }   /* 2: vừa mở ra thấy lần đầu */
const ordNewN = () => ((ST.ord && ST.ord.list) || []).filter(o => o.moi && !o.seen);""")
rep("""if ((ST.ord.done || 0) <= 5){ try { if (ST.ord.list.length < ordMax()) ST.ord.list.push(leadMake('nb') || ordMake()); } catch (e) {} }""",
    """if ((ST.ord.done || 0) <= 5){ try { if (ST.ord.list.length < ordMax()){ const o = leadMake('nb') || ordMake(); o.moi = 1; ST.ord.list.push(o); } } catch (e) {} }""")
rep("""const ok = ST.ord.list.some(ordCan);
  ORDV.b.quaternion""", """const ok = ST.ord.list.some(ordCan), nw = ST.ord.list.some(o => o.moi && !o.seen);
  if (ORDAW){ const n = performance.now(); if (!ORDAWT) ORDAWT = n + 3000; else if (n > ORDAWT){ ORDAW = 0; if (ordNewN().length) ordPop(); } }
  ORDV.b.quaternion""")
rep("""ORDV.b.position.set(BOAT.position.x, .95 + Math.sin(t * 2) * .035, BOAT.position.z); ORDV.b.scale.setScalar(.85 * BUBS * (1 + (ok ? .08 : .03) * Math.abs(Math.sin(t * 3))));""",
    """const pp = (performance.now() - ORDPOP) / 1000, pk = pp < 1.2 ? 1 - Math.exp(-7 * pp) * Math.cos(16 * pp) * .6 : 1, hop = pp < .45 ? .3 * Math.sin(pp / .45 * Math.PI) : nw && (t % 6) < .4 ? .1 * Math.sin((t % 6) / .4 * Math.PI) : 0;
  ORDV.b.position.set(BOAT.position.x, .95 + hop + Math.sin(t * 2) * .035, BOAT.position.z); ORDV.b.scale.setScalar(.85 * BUBS * pk * (1 + (ok ? .08 : .03) * Math.abs(Math.sin(t * 3))));""")
rep("""    else if (k === 'cut'){""", """    else if (k === 'goi'){ songlang(t0, .4); songlang(t0 + .15, .34); pluck(NGU.at(5) * 2, t0 + .32, .3, .99); pluck(NGU.at(3) * 2, t0 + .5, .34, .99); }   // có người ghé gọi mua: gõ hai tiếng rồi "ơi ới"
    else if (k === 'cut'){""")
rep("""const ok = ordCan(o); return `<div class="ordr${ok ? ' ok' : ''}"><div class="ow">${ok ? '' : `<i class="oxu">${o.xu} xu</i>`}<b>${o.who}""",
    """const ok = ordCan(o), nw = ordNew(o); return `<div class="ordr${ok ? ' ok' : ''}${nw === 2 ? ' vua' : ''}"><div class="ow">${ok ? '' : `<i class="oxu">${o.xu} xu</i>`}<b>${o.who}${nw ? `<em class="leadt moi">${L135('Mới tới', 'New')}</em>` : ''}""")
rep("""nOk = ST.ord ? ST.ord.list.filter(ordCan).length : 0, lv = ST.lv || 1, left = mauLeft(), gh = gheOn() && ST.ghe.o; let h = '';""",
    """nOk = ST.ord ? ST.ord.list.filter(ordCan).length : 0, lv = ST.lv || 1, left = mauLeft(), gh = gheOn() && ST.ghe.o, nwL = lv >= ORD.lv ? ordNewN() : []; let h = '';""")
rep("""  else if (nOk) h += UX.hero(ICON.cho, `${nOk} đơn giao được rồi`, 'Hàng xóm đang chờ ở bến', 'go');""",
    """  else if (nwL.length) h += UX.hero(ICON.cho, L135(nwL.length === 1 ? 'Có đơn mới' : `${nwL.length} đơn mới`, nwL.length === 1 ? 'New order' : `${nwL.length} new orders`), nwL.length === 1 ? nwL[0].who : L135('Bà con ghé đặt hàng', 'Neighbours ordering'), 'go');
  else if (nOk) h += UX.hero(ICON.cho, `${nOk} đơn giao được rồi`, 'Hàng xóm đang chờ ở bến', 'go');""")
rep("""{ g: !!(nOk || gh), img: ICON.cho }) : '']);
  h += benMap();""", """{ g: !!(nOk || gh || nwL.length), img: ICON.cho }) : '']);
  h += benMap();""")
# lò ấp mở ở cấp 14 (từ v102), câu trong bảng chuồng vịt còn ghi từ cấp 9 → người cấp 9-13 tưởng có lò ấp mà không thấy
rep("""${(ST.lv || 1) >= 9 ? ' Lò ấp trấu cạnh chuồng ấp trứng vịt ra vịt con.' : ''}""", """${loOn() ? ' Lò ấp trấu cạnh chuồng ấp trứng vịt ra vịt con.' : ''}""")
assert not soat(s), soat(s)[:5]

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
