#!/usr/bin/env python3
"""v106 phần A: Sổ còn 3 tab (Việc · Kho · Bộ sưu tập có chip Giống/Cá/Bướm/Cổ tích); Chợ: tab Trang trí thành Tiệm (có chip);
bỏ chế độ Sửa vườn — chạm thẳng ô đất, đồ, đồ kiểng; chỉ còn thanh đặt đồ "Chạm một ô trống để đặt X · Hủy"."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# ================= SỔ: 3 tab, Bộ sưu tập có chip =================
rep("const tabOn = k => {", "const BSTK = ['giong', 'ca', 'buom', 'cotich'], BSTN = { giong: 'Giống', ca: 'Cá', buom: 'Bướm', cotich: 'Cổ tích' };   /* chip trong Bộ sưu tập */\nconst tabOn = k => {")
rep("""  const tabs = Object.entries(BTAB).filter(([k]) => tabOn(k)).map(([k, [n, c, dc, ic]]) => `<button class="bkt ${k === tab ? 'on' : 'off'}" data-b="tab" data-k="${k}" style="background:${c};text-shadow:${ring(dc, 1.6)}" aria-label="${n}" aria-pressed="${k === tab}"><img src="${UIC[ic] || ICON[ic]}" alt=""><span>${nr ? (k === 'viec' ? 'Việc' : k === 'ca' ? 'Cá' : k === 'cotich' ? 'Cổ tích' : k === 'buom' ? 'Bướm' : k === 'giong' && k !== tab ? 'Giống' : n) : n.replace('Việc của Ngoại', 'Việc của<br>Ngoại')}</span></button>`).join('');""",
    """  const inB = BSTK.includes(tab); if (inB) BOOK.sub = tab; const bsub = BOOK.sub && tabOn(BOOK.sub) ? BOOK.sub : 'giong', BC = BTAB[inB ? tab : bsub];
  const TOP = [['viec', ...BTAB.viec], ['kho', ...BTAB.kho], [bsub, 'Bộ sưu tập', BC[1], BC[2], BC[3]]];
  const tabs = TOP.map(([k, n, c, dc, ic]) => { const on = k === tab || (inB && BSTK.includes(k)); return `<button class="bkt ${on ? 'on' : 'off'}" data-b="tab" data-k="${k}" style="background:${c};text-shadow:${ring(dc, 1.6)}" aria-label="${n}" aria-pressed="${on}"><img src="${UIC[ic] || ICON[ic]}" alt=""><span>${nr ? (k === 'viec' ? 'Việc' : n) : n.replace('Việc của Ngoại', 'Việc của<br>Ngoại').replace('Bộ sưu tập', 'Bộ sưu<br>tập')}</span></button>`; }).join('');
  if (inB && !(nr && tab === 'giong' && BOOK.sel)){ const cs = BSTK.filter(tabOn); if (cs.length > 1) L = `<div class="bkchips">${cs.map(k => `<button class="bkchip${k === tab ? ' on' : ''}" data-b="tab" data-k="${k}" style="--c:${BTAB[k][1]};--d:${BTAB[k][2]}" aria-pressed="${k === tab}"><img src="${UIC[BTAB[k][3]] || ICON[BTAB[k][3]]}" alt="">${BSTN[k]}</button>`).join('')}</div>` + L; }""")
# cây cổ tích dời chỗ từ sổ
rep("return `<div class=\"ftc\"><img src=\"${img}\" alt=\"\"><div><b>${D.name}</b><small>${D.story}${F.told >= D.max ? ' · đã lớn' : ` · giai đoạn ${F.st}/${D.max}`}</small>${D.parts.slice(0, F.told).map(x => `<p>${x}</p>`).join('')}</div></div>`; }).join(''); }",
    "return `<div class=\"ftc\"><img src=\"${img}\" alt=\"\"><div><b>${D.name}</b><small>${D.story}${F.told >= D.max ? ' · đã lớn' : ` · giai đoạn ${F.st}/${D.max}`}</small>${D.parts.slice(0, F.told).map(x => `<p>${x}</p>`).join('')}${BIGD[k] && !VISIT && baiOn() ? `<button class=\"bkmv\" data-b=\"bigmove\" data-k=\"${k}\">Dời cây qua chỗ khác</button>` : ''}</div></div>`; }).join(''); }")
rep("  else if (a === 'sel'){ BOOK.sel = k; BOOK.keep = !narrow(); } else if (a === 'back'){ BOOK.sel = null; }",
    "  else if (a === 'sel'){ BOOK.sel = k; BOOK.keep = !narrow(); } else if (a === 'back'){ BOOK.sel = null; }\n  else if (a === 'bigmove'){ closeBook(); suaOn(true, k); return; }")

# ================= CHỢ: Trang trí -> Tiệm (chip) =================
rep("dcOn() ? ['tt', 'Trang trí', 0] : null", "dcOn() ? ['tiem', 'Tiệm', 0] : null")
rep("    if (SHEET.tab === 'tt') h += dcHTML();",
    "    if (SHEET.tab === 'tt') SHEET.tab = 'tiem';\n"
    "    if (SHEET.tab === 'tiem'){ const TC = [['kieng', 'Đồ kiểng', UIC.dc_mai_chieu_thuy]].filter(Boolean); if (!TC.some(c => c[0] === SHEET.sub)) SHEET.sub = TC[0][0];   /* chip Tiệm: tiệm may, thợ nhà, bảng tên thêm sau */\n"
    "      if (TC.length > 1) h += `<div class=\"tchips\">${TC.map(([k, n, im]) => `<button class=\"tchip${SHEET.sub === k ? ' on' : ''}\" data-a=\"tsub\" data-k=\"${k}\"><img src=\"${im}\" alt=\"\">${n}</button>`).join('')}</div>`;\n"
    "      if (SHEET.sub === 'kieng') h += dcHTML(); }")
rep("else if (a === 'gocho3'){ openSheet('cho'); SHEET.tab = 'mua'; renderSheet(); return; }",
    "else if (a === 'gocho3'){ openSheet('cho'); SHEET.tab = 'mua'; renderSheet(); return; } else if (a === 'tsub'){ SHEET.sub = b.dataset.k; renderSheet(); return; }")
# việc "đặt đồ kiểng" đi thẳng vô Tiệm
rep("lo: 'lo', gio: 'gio', mat: 'ong', tb: 'tb', dc: 'deco' }[t]){ try { openSheet({ ord: 'ben', bon: 'ho', lo: 'lo', gio: 'gio', mat: 'ong', tb: 'tb', dc: 'deco' }[t]); } catch (e) {} return; }",
    "lo: 'lo', gio: 'gio', mat: 'ong', tb: 'tb', dc: 'cho' }[t]){ try { openSheet({ ord: 'ben', bon: 'ho', lo: 'lo', gio: 'gio', mat: 'ong', tb: 'tb', dc: 'cho' }[t]); if (t === 'dc'){ SHEET.tab = 'tiem'; SHEET.sub = 'kieng'; renderSheet(); } } catch (e) {} return; }")

# ================= BỎ SỬA VƯỜN =================
# nút Sửa vườn không hiện nữa; thanh còn lại là thanh đặt đồ
rep("function placeSua(){ const b = $('#bCtr'), s2 = $('#bSua'); if (!b || !s2) return; s2.hidden = !!VISIT || !baiOn();",
    "function placeSua(){ const b = $('#bCtr'), s2 = $('#bSua'); if (!b || !s2) return; s2.hidden = true;")
rep('<div class="card vbar sbar" id="suaBar" hidden><div><b>Sửa vườn</b><span id="suaTx"></span></div><button class="btn g" id="suaOk">Xong</button></div>',
    '<div class="card vbar sbar" id="suaBar" hidden><div><b id="suaHd">Đặt đồ</b><span id="suaTx"></span></div><button class="btn" id="suaOk">Hủy</button></div>')
# suaOn: chỉ còn chế độ đặt (có move); gọi không có món thì chỉ đưa camera tới bãi
rep("function suaOn(on, move){ if (on && (VISIT || !baiOn())) return; SUA = on ? { move: move || null } : null;",
    "function suaOn(on, move){ if (on && (VISIT || !baiOn())) return; if (on && !move){ try { camTo(new T.Vector3(BAIC.x + .4, .3, BAIC.z + .3), Math.max(cam.zoom, DEFZ() * 1.15)); } catch (e) {} return; } if (!on && SUA && SUA.move && SUA.move.startsWith('dc:')) toast('Ngoại cất món kiểng trong nhà, lúc nào đặt cũng được.'); SUA = on ? { move: move || null } : null;")
rep("sayOnce('sua1', 'Ô nào là đất của con thì đắp liếp hay đặt đồ tùy con. Ô cỏ thì khai hoang trước. Chạm từng ô mà sửa nghe.', 'vui'); } }",
    "} }")
rep("function suaTx(){ const t = $('#suaTx'); if (t && SUA) t.textContent = SUA.move ? `Chạm một ô đất trống để đặt",
    "function suaTx(){ const t = $('#suaTx'); if (t && SUA) t.textContent = SUA.move ? `Chạm một ô trống để đặt")
# đặt xong là tắt thanh
rep("if (HP && HP.bai && dcPlace(dk, hid)){ SUA.move = null; suaTx(); sfx('pop'); }", "if (HP && HP.bai && dcPlace(dk, hid)){ SUA.move = null; suaOn(false); sfx('pop'); }")
rep("if (HP && HP.bai && bigPlace(mk, hid)){ SUA.move = null; suaTx(); for (const P of PLOTS) if (P.bai) refreshPlot(P.id); sfx('pop'); }",
    "if (HP && HP.bai && bigPlace(mk, hid)){ SUA.move = null; suaOn(false); sfx('pop'); }")
rep("placeObj(mk, hid)){ SUA.move = null; suaTx(); for (const P of PLOTS) if (P.bai) refreshPlot(P.id); sfx('pop'); }",
    "placeObj(mk, hid)){ SUA.move = null; suaOn(false); sfx('pop'); }")
# chạm thẳng đồ kiểng, ao
rep("if (di >= 0){ if (SUA) openSheet('deco', di); else bark(DCK[ST.dc.items[di].k].name); return; }", "if (di >= 0){ openSheet('deco', di); return; }")
rep("if (bk){ if (SUA) openSheet('big', bk); else if (bk === 'ao') openBook('ca'); else ftTap(bk); return; }", "if (bk){ if (bk === 'ao') openSheet('big', 'ao'); else ftTap(bk); return; }")
rep("if (aoHit(e.clientX, e.clientY) && !(SUA && SUA.move)){ if (SUA) openSheet('big', 'ao'); else { sfx('pick'); openBook('ca'); } return; }",
    "if (aoHit(e.clientX, e.clientY) && !(SUA && SUA.move)){ sfx('pick'); openSheet('big', 'ao'); return; }")
rep("let h = UX.hero(k === 'ao' ? ICON.caro : UIC['ft_' + k], D.title, onGrid ? 'Đang chiếm 2×2 ô đất' : 'Đang ở bãi cỏ cạnh nhà');\n  h += UX.cta([UX.btn('bigmove', 'Dời qua chỗ khác', { g: 1, k }),",
    "let h = UX.hero(k === 'ao' ? ICON.caro : UIC['ft_' + k], D.title, onGrid ? 'Đang chiếm 2×2 ô đất' : 'Đang ở bãi cỏ cạnh nhà');\n  h += UX.cta([k === 'ao' ? UX.btn('aobook', 'Xem sổ cá', { g: 1, img: ICON.caro }) : '', UX.btn('bigmove', 'Dời qua chỗ khác', { g: k !== 'ao', k }),")
rep("else if (a === 'bigmove'){ closeSheet(); suaOn(true, b.dataset.k); return; }", "else if (a === 'bigmove'){ closeSheet(); suaOn(true, b.dataset.k); return; } else if (a === 'aobook'){ closeSheet(); openBook('ca'); return; }")
# thùng ong cũng dời được
rep("Có ong thì cây trái mỗi vụ ra thêm một trái.'); }", "Có ong thì cây trái mỗi vụ ra thêm một trái.') + `<div class=\"acts\">${moveBtn('ong')}</div>`; }")
# liếp trống ở bãi: san thành đất trống ngay trong vòng gieo + bảng liếp
rep("hint = ks.length > 0 ? 'Chạm để gieo liếp này · kéo xuống qua nhiều liếp' : ''; }",
    "hint = ks.length > 0 ? 'Chạm để gieo liếp này · kéo xuống qua nhiều liếp' : ''; if (P.bai && !ST.plots[id].crop) hint += `<button class=\"rgsan\" data-r=\"san\">San thành đất trống</button>`; }")
rep("if (a === 'x'){ closeRing(); return; } if (a === 'info'){", "if (a === 'x'){ closeRing(); return; } if (a === 'san'){ closeRing(); baiSan(id); return; } if (a === 'info'){")
rep("    h += plotHTML(P, p, arg); }", "    h += plotHTML(P, p, arg); if (P.bai && !p.crop) h += `<div class=\"acts\"><button class=\"btn\" data-a=\"bsan\"><span>San thành đất trống</span></button></div>`; }")
# lời dặn không còn nhắc nút Sửa vườn
rep("how: 'Bấm Sửa vườn, đắp 2 liếp ở bãi hông nhà.", "how: 'Chạm ô cỏ ở bãi hông nhà, khai hoang rồi đắp 2 liếp.")
rep("['cuoc', 'Bãi hông nhà · Sửa vườn']", "['cuoc', 'Bãi hông nhà']")
rep("else if (t === 'own'){ try { suaOn(true); } catch (e) {} toast(`Chạm một ô đất trống để đặt", "else if (t === 'own'){ try { suaOn(true); } catch (e) {} toast(`Chạm một ô đất trống ở bãi để đặt")

# avHud gọi lúc đang tải (việc xong trong lúc tính bù giờ vắng) khi hình avatar chưa dựng: bỏ qua, hud vẽ lại sau
rep("$('#avbImg').src = AVIMG.face[P.av];", "try { $('#avbImg').src = AVIMG.face[P.av]; } catch (e) { return; }")

# ================= CSS =================
CSS = """
.bkchips{display:flex;gap:6px;flex-wrap:wrap;margin:2px 0 10px;position:sticky;top:-2px;z-index:2;padding:4px 0;background:inherit}
.bkchip{appearance:none;border:0;cursor:pointer;display:flex;align-items:center;gap:5px;min-height:40px;padding:4px 14px 4px 6px;border-radius:999px;background:#EDE3D1;color:#8A5D3B;font:400 15px var(--f-game);box-shadow:inset 0 -3px 0 rgba(0,0,0,.08)}
.bkchip img{width:30px;height:30px}
.bkchip.on{background:var(--c);color:#FBF7EE;text-shadow:0 1px 0 var(--d);box-shadow:inset 0 -3px 0 var(--d)}
.bkchip:focus-visible,.tchip:focus-visible{outline:3px solid var(--sun);outline-offset:2px}
.bkmv{appearance:none;border:0;cursor:pointer;margin-top:6px;padding:6px 12px;border-radius:999px;background:#EDE3D1;color:#7A4E96;font:400 13px var(--f-game)}
.tchips{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0 6px}
.tchip{appearance:none;border:0;cursor:pointer;display:flex;align-items:center;gap:5px;min-height:38px;padding:3px 12px 3px 5px;border-radius:999px;background:#EDE3D1;color:#8A5D3B;font:400 14px var(--f-game)}
.tchip img{width:28px;height:28px}.tchip.on{background:#6E9F57;color:#fff}
.rgsan{display:block;margin:6px auto 0;appearance:none;border:0;cursor:pointer;padding:5px 12px;border-radius:999px;background:#EDE3D1;color:#8A5D3B;font:400 13px var(--f-game)}
#suaOk{min-width:72px}
"""
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
