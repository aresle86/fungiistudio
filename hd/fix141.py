# v141: bản đồ sông ở Bến nhà (anh Ares duyệt 12/11). Thay danh sách điểm đến bằng một tấm bản đồ vẽ tay:
# Vườn nhà, Vườn Ngoại, Vườn bà con, Chợ nổi, Bến bà con, Chợ huyện. Mỗi chỗ một dòng trạng thái ngắn.
# Chỗ chưa mở làm mờ, không ghi số cấp. Chạm một chỗ thì thẻ chi tiết (nút chèo đi) hiện ngay dưới bản đồ.
# Bán hàng và đơn ghe bẹo vẫn ở đầu bảng Bến nhà như cũ.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v140a'", "BUILD = 'v141'")

MAP = r'''
/* v141: bản đồ sông vẽ tay ở Bến nhà */
function benMap(){ const lv = ST.lv || 1, left = mauLeft(), L = cnL, ink = '#6B4529';
  const rowCn = cnoBen(), rowCh = chRow();   /* gọi luôn để Ngoại vẫn nhắc lúc mới mở chỗ mới */
  const ok = { nha: 1, ngoai: lv >= MAU.lv, bacon: lv >= NB2.lv, chono: lv >= CNX.lv, benbc: lv >= CNX.lv, huyen: lv >= CHM.lv };
  let nBay = 0; if (ok.benbc) try { nBay = (cnbS().my || []).reduce((a, it) => a + (it.q || 0), 0); } catch (e) {}
  const nNb = NB2.list ? NB2.list.length : -1, nSt = Object.keys(NB2.steal || {}).length, lk = L('chưa tới được', 'not yet');
  const P = { huyen: [0, 0, 72, 30, L('Chợ huyện', 'District market'), L(`đò máy ${CHM.fare} xu`, `ferry ${CHM.fare} coins`)],
    benbc: [1, 0, 262, 30, L('Bến bà con', "Neighbours' pier"), nBay ? L(`đang bày ${nBay} món`, `${nBay} on display`) : L('chưa bày hàng', 'nothing on display')],
    chono: [0, 1, 92, 128, L('Chợ nổi', 'Floating market'), ok.chono && cnoS().temd === cnoS().d ? L('hôm nay ghé rồi', 'visited today') : L('ghe đang treo hàng', 'boats are buying')],
    bacon: [1, 1, 262, 130, L('Vườn bà con', "Neighbours' farms"), nSt ? L('có người mới đổi công', 'someone traded work') : nNb > 0 ? L(`${nNb} hàng xóm`, `${nNb} neighbours`) : L('thêm hàng xóm', 'add neighbours')],
    nha: [0, 2, 72, 230, L('Vườn nhà', 'Home'), L('con ở đây', 'you are here')],
    ngoai: [1, 2, 262, 230, L('Vườn Ngoại', "Grandma's garden"), left > 0 ? L(`còn hái ${left} món`, `${left} picks left`) : L('hôm nay hái đủ rồi', 'done for today')] };
  const sel = P[SHEET.mp] ? SHEET.mp : ok.ngoai && left > 0 ? 'ngoai' : 'nha';
  const nhaD = (x, y, c1, sc = 1) => `<g transform="translate(${x} ${y}) scale(${sc})"><path d="M-13 9V-3M13 9V-3M-6 9V2M6 9V2" stroke="${ink}" stroke-width="1.6"/><rect x="-14" y="-9" width="28" height="12" rx="1.5" fill="#F3DFB8" stroke="${ink}" stroke-width="1.6"/><path d="M-19 -8 L0 -22 L19 -8Z" fill="${c1}" stroke="${ink}" stroke-width="1.6" stroke-linejoin="round"/><rect x="-3" y="-5" width="6" height="8" fill="#B48560" stroke="${ink}" stroke-width="1.2"/></g>`;
  const cay = (x, y, sc = 1) => `<g transform="translate(${x} ${y}) scale(${sc})"><path d="M0 10V-2" stroke="${ink}" stroke-width="2"/><circle cx="0" cy="-8" r="8" fill="#9CC27A" stroke="${ink}" stroke-width="1.5"/><circle cx="-6" cy="-3" r="5" fill="#9CC27A" stroke="${ink}" stroke-width="1.5"/><circle cx="6" cy="-3" r="5" fill="#8DB56A" stroke="${ink}" stroke-width="1.5"/></g>`;
  const dua = (x, y, sc = 1) => `<g transform="translate(${x} ${y}) scale(${sc})" fill="none" stroke="${ink}" stroke-width="1.6" stroke-linecap="round"><path d="M0 12C-1 2 2 -6 5 -14" stroke-width="2.2"/><path d="M5 -14C-2 -20 -10 -18 -13 -12M5 -14C0 -22 -4 -25 -9 -25M5 -14C8 -22 13 -24 18 -22M5 -14C12 -16 17 -12 19 -7M5 -14C4 -8 0 -5 -4 -5" stroke="#5E8A4A" stroke-width="2.4"/></g>`;
  const xuong = (x, y, sc = 1, c1 = '#B48560', beo = 0) => `<g transform="translate(${x} ${y}) scale(${sc})">${beo ? `<path d="M2 -2V-17" stroke="${ink}" stroke-width="1.3"/><circle cx="2" cy="-18" r="2.6" fill="#E8704A" stroke="${ink}" stroke-width="1"/><circle cx="2" cy="-12" r="2.2" fill="#F5D27A" stroke="${ink}" stroke-width="1"/>` : ''}<path d="M-14 -2Q0 7 14 -2L10 -4H-10Z" fill="${c1}" stroke="${ink}" stroke-width="1.5" stroke-linejoin="round"/></g>`;
  const D = { nha: nhaD(-8, 0, '#C98A5A') + dua(18, -3) + xuong(52, 16, .8),
    ngoai: nhaD(8, 0, '#C98A5A') + cay(-20, 2, 1.05) + `<path d="M-34 14h14M-32 19h14M26 14h12M28 19h12" stroke="#6E9F57" stroke-width="2.4" stroke-linecap="round"/>`,
    bacon: nhaD(-20, 3, '#D9A25A', .78) + nhaD(4, -4, '#C98A5A', .78) + nhaD(26, 5, '#B8704A', .78) + cay(-38, 4, .7) + cay(42, 2, .7),
    chono: xuong(-14, 0, 1.15, '#B48560', 1) + xuong(14, 8, 1, '#C98A5A', 1) + xuong(10, -12, .8, '#D9A25A', 1),
    benbc: `<path d="M-24 6H24" stroke="${ink}" stroke-width="5" stroke-linecap="round"/><path d="M-24 6H24" stroke="#D9B98A" stroke-width="2.6" stroke-linecap="round"/><path d="M-18 6V14M0 6V14M18 6V14" stroke="${ink}" stroke-width="1.6"/>` + xuong(-12, 20, .8, '#3F9C8F') + xuong(14, 21, .8, '#E0A526') + nhaD(0, -8, '#C98A5A', .7),
    huyen: `<rect x="-24" y="-4" width="48" height="14" rx="1.5" fill="#F3DFB8" stroke="${ink}" stroke-width="1.6"/><path d="M-30 -4L-22 -14H22L30 -4Z" fill="#B8553A" stroke="${ink}" stroke-width="1.6" stroke-linejoin="round"/><path d="M-14 -14L-9 -22H9L14 -14Z" fill="#C96A4A" stroke="${ink}" stroke-width="1.6" stroke-linejoin="round"/><path d="M-12 10V0M0 10V0M12 10V0" stroke="${ink}" stroke-width="1.4"/><path d="M34 10V-8" stroke="${ink}" stroke-width="1.4"/><path d="M34 -8h9l-3 3 3 3h-9Z" fill="#E8704A" stroke="${ink}" stroke-width="1"/>` };
  const RV = 'M172 310C170 283 176 259 168 235C158 199 96 180 96 134C96 94 160 86 172 55C178 36 186 14 184 -10', RC = 'M172 60C205 74 250 55 345 67';
  let g = '', bt = '';
  for (const k of ['huyen', 'benbc', 'chono', 'bacon', 'nha', 'ngoai']){ const [cx, cy, x, y, nm, st] = P[k], o = ok[k];
    g += `<g transform="translate(${x} ${y})"${o ? '' : ' opacity=".34"'}>${k === sel ? `<ellipse cx="2" cy="1" rx="50" ry="27" fill="#FFF8E8" fill-opacity=".7" stroke="#C24A2E" stroke-width="2.4" stroke-dasharray="7 5"/>` : ''}${D[k]}</g>`;
    bt += `<button class="mp${k === sel ? ' on' : ''}${o ? '' : ' lk'}" data-a="mpsel" data-k="${k}" style="left:${cx * 50}%;top:${cy * 33.34}%" aria-pressed="${k === sel}"><span class="lb"><b>${nm}</b><i>${o ? st : lk}</i></span></button>`; }
  const svg = `<svg viewBox="0 0 340 300" aria-hidden="true"><defs><filter id="mpw" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".045" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="2.6"/></filter></defs>
<g filter="url(#mpw)" fill="none" stroke-linecap="round"><path d="${RC}" stroke="${ink}" stroke-width="15" opacity=".55"/><path d="${RV}" stroke="${ink}" stroke-width="37" opacity=".55"/><path d="${RC}" stroke="#A9D8CF" stroke-width="12"/><path d="${RV}" stroke="#A9D8CF" stroke-width="33"/><path d="${RV}" stroke="#C9EAE3" stroke-width="9" stroke-dasharray="16 22" opacity=".8"/>
<path d="M160 274q4 -3 8 0t8 0M150 168q4 -3 8 0t8 0M120 96q4 -3 8 0t8 0M176 17q4 -3 8 0t8 0M236 64q4 -3 8 0t8 0" stroke="#5E9C92" stroke-width="1.5"/>
<path d="M22 180l3 -7 3 7M30 182l3 -7 3 7M306 180l3 -7 3 7M128 36l3 -7 3 7M320 112l3 -7 3 7M20 84l3 -7 3 7" stroke="#8DB56A" stroke-width="1.8"/>
<g stroke-linejoin="round">${g}</g>
<g transform="translate(318 280)" stroke="${ink}" stroke-width="1.4"><path d="M0 -13L4 0 0 13 -4 0Z" fill="#F5D27A"/><path d="M-11 0H11"/></g></g></svg>`;
  const lock = `<div class="note">${L('Xuồng mình chưa chèo tới đó được. Cứ chăm vườn đi con, mai mốt Ngoại chỉ đường cho.', "Our boat can't reach that place yet. Keep tending the garden and Grandma will show you the way.")}</div>`;
  let d = '';
  if (sel === 'nha') d = `<div class="chrow"><div><b>${L('Vườn nhà', 'Home')}</b><span>${L('Xuồng nhà mình đậu ở bến. Chạm một chỗ trên bản đồ để chèo đi.', 'Our boat is moored here. Tap a place on the map to row there.')}</span></div></div>`;
  else if (sel === 'bacon') d = nbHTML();
  else if (!ok[sel]) d = lock + (sel === 'huyen' ? rowCh : '');
  else if (sel === 'ngoai') d = `<div class="vcard"><img src="${ICON.xoai || ICON.cai}" alt=""><div><b>Vườn mẫu của Ngoại</b><span>Ngoại cho hái ${MAU.picks} món mỗi ngày${left < MAU.picks ? `, hôm nay còn ${left}` : ''}</span>${UX.pips(ICON.cai, left, MAU.picks)}</div><button class="btn g" data-a="gomau">Chèo qua</button></div>`;
  else if (sel === 'chono') d = rowCn;
  else if (sel === 'benbc') d = `<div class="chrow"><div><b>${L('Bến bà con', "Neighbours' pier")}</b><span>${L('Bày đồ nhà làm cho bà con mua, ghé xuồng bà con mua món mình thiếu', 'Lay out your goods for neighbours, and buy what you are short of')}</span></div><button class="btn g" data-a="cnofind">${L('Chèo ra bến', 'Row out')}</button></div>`;
  else if (sel === 'huyen') d = rowCh;
  return UX.title(L('Chèo xuồng đi đâu', 'Where to row')) + `<div class="rmap">${svg}${bt}</div><div id="mpDet">${d}</div>`; }
'''
rep("function benHTML(){ return cnoBen() + chRow() + benHTML0(); }", MAP.strip('\n') + "\nfunction benHTML(){ return benHTML0(); }")
rep("""  h += UX.title('Đi ghé vườn') + `<div class="vcard"><img src="${ICON.xoai || ICON.cai}" alt=""><div><b>Vườn mẫu của Ngoại</b><span>Ngoại cho hái ${MAU.picks} món mỗi ngày${left < MAU.picks ? `, hôm nay còn ${left}` : ''}</span>${UX.pips(ICON.cai, left, MAU.picks)}</div><button class="btn g" data-a="gomau">Chèo qua</button></div>`;
  if (cauOn() && !ST.kca)""", "  h += benMap();\n  if (cauOn() && !ST.kca)")
rep("KCA.xu - ST.xu} xu` : '' }) + '</div>';\n  return h + nbHTML(); }", "KCA.xu - ST.xu} xu` : '' }) + '</div>';\n  return h; }")
rep("if (a === 'chgo'){ chEnter(); return; }", "if (a === 'mpsel'){ SHEET.mp = b.dataset.k; sfx('pick'); renderSheet(); setTimeout(() => { try { const e = document.getElementById('mpDet'); if (e) e.scrollIntoView({ block: 'nearest', behavior: 'smooth' }); } catch (e2) {} }, 40); return; } if (a === 'chgo'){ chEnter(); return; }")
rep(".chrow{display:flex;align-items:center;gap:10px;", ".rmap{position:relative;margin:6px 0 8px;border-radius:16px;background:#F6EBD3;box-shadow:inset 0 0 0 2px #D9C3A2,0 3px 0 #E3D3BC;overflow:hidden}.rmap svg{display:block;width:100%;height:auto}"
    ".rmap .mp{position:absolute;width:50%;height:33.34%;appearance:none;border:0;background:none;margin:0;padding:0 4px 5px;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;cursor:pointer;color:var(--ink);-webkit-tap-highlight-color:transparent}"
    ".rmap .lb{display:block;max-width:100%;background:rgba(251,247,238,.86);border-radius:10px;padding:1px 8px 2px;text-align:center;white-space:nowrap}.rmap .lb b{display:block;font:400 17px/1.1 var(--f-hand);color:#4A2F1E}.rmap .lb i{display:block;font:400 13px/1.15 var(--f-hand);font-style:normal;color:#6B4529}"
    ".rmap .mp.on .lb{background:#FFF8E8;box-shadow:0 0 0 2px #C24A2E}.rmap .mp.lk .lb{background:rgba(251,247,238,.8)}.rmap .mp.lk .lb b,.rmap .mp.lk .lb i{color:#75604E}.rmap .mp:active .lb{transform:scale(.96)}.rmap .mp:focus-visible .lb{outline:3px solid #3E7FC4;outline-offset:2px}#mpDet{scroll-margin:8px}@media (max-width:374px){.rmap .lb{padding:0 6px 1px}.rmap .lb b{font-size:15px}.rmap .lb i{font-size:12px}}"
    ".chrow{display:flex;align-items:center;gap:10px;")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
