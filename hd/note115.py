# note115: mật thư bụi chuối. python3 note115.py live/v115_3b.html live/v115_3c.html
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
i=s.rfind('</style>',0,s.find('<script type="module">')); s=s[:i]+open('note115.css',encoding='utf-8').read()+s[i:]
js=open('note115.js',encoding='utf-8').read()
rep("function bepHitAt(cx, cy){",js+"function bepHitAt(cx, cy){")
# biểu tượng lá thư
rep("  shot('cai', () => { cai(0, 0, 1.4);","  shot('thu', () => { const g = G(0, 0, 0, .25); M(box(.5, .03, .34), '#FBF1DC', 0, 0, 0, { p: g }); for (const sg of [-1, 1]){ M(box(.31, .012, .02), '#C9A97A', sg * .125, .022, -.075, { p: g, r: [0, sg * .6, 0] }); } M(box(.5, .012, .02), '#C9A97A', 0, .022, .16, { p: g }); M(sph(.05, 8, 6), '#C24A2E', 0, .03, .01, { p: g, s: [1, .5, 1] }); }, new T.Vector3(.2, 1.2, .55));\n  shot('cai', () => { cai(0, 0, 1.4);")
# chạm mở, tick
rep("  if (bepHitAt(e.clientX, e.clientY)){ if ((ST.lv || 1) >= BEP.lv","  if (noteHit(e.clientX, e.clientY)) return;\n  if (bepHitAt(e.clientX, e.clientY)){ if ((ST.lv || 1) >= BEP.lv")
rep("bepTick(t); vitTick(t); }","bepTick(t); vitTick(t); noteTick(t); }")
# bảng
rep("if (kind === 'visit'){ shT.textContent = 'Quà và hạt giống'; h += visitSheetHTML(); }","if (kind === 'visit'){ shT.textContent = SHEET.nc ? 'Giấu mật thư' : 'Quà và mật thư'; h += SHEET.nc ? noteComposeHTML() : visitSheetHTML(); }\n  if (kind === 'thu'){ shT.textContent = 'Mật thư'; h += thuHTML(arg); }")
rep("function visitSheetHTML(){ const V = VISIT; let h = `<div class=\"note\">Mỗi ngày xin hạt một lần, để quà một món cho ${esc(V.owner)}.</div>`;","function visitSheetHTML(){ const V = VISIT; let h = `<div class=\"sub\">Mật thư</div>` + (V.noted ? `<div class=\"note\">Con giấu thư rồi, ${esc(V.owner)} về là kiếm ra.</div>` : `<div class=\"note\">Mỗi ngày giấu một lá thư trong vườn ${esc(V.owner)}, kẹp quà nhỏ cũng được.</div><div class=\"acts\"><button class=\"btn g\" data-a=\"vnote\">Giấu mật thư</button></div>`) + `<div class=\"sub\">Hạt giống</div><div class=\"note\">Mỗi ngày xin hạt một lần, để quà một món cho ${esc(V.owner)}.</div>`;")
rep("id=\"vMore\">Quà · xin hạt</button>","id=\"vMore\">Quà · mật thư</button>")
rep("  else if (a === 'buybn'){","  else if (a === 'vnote'){ SHEET.nc = { spot: 'chuoi', t: -1, st: 0, g: -1 }; renderSheet(); shB.scrollTop = 0; return; }\n  else if (a === 'nback'){ SHEET.nc = null; renderSheet(); return; }\n  else if (a === 'nsp' && SHEET.nc){ SHEET.nc.spot = b.dataset.k; renderSheet(); return; }\n  else if (a === 'ntx' && SHEET.nc){ SHEET.nc.t = +b.dataset.k; renderSheet(); return; }\n  else if (a === 'nst' && SHEET.nc){ SHEET.nc.st = +b.dataset.k; renderSheet(); return; }\n  else if (a === 'ngf' && SHEET.nc){ SHEET.nc.g = +b.dataset.k; renderSheet(); return; }\n  else if (a === 'nsend'){ noteSend(); return; }\n  else if (a === 'thuok'){ closeSheet(); return; }\n  else if (a === 'thugo'){ closeSheet(); visitFriend(b.dataset.k); return; }\n  else if (a === 'buybn'){")
# hộp thư
rep("gift: [], ask: 0, visit: 0 };","gift: [], ask: 0, visit: 0, note: null };")
rep("    else if (e.kind === 'ask'){ NB2.ask[e.code] = 1; b.ask = 1; } else b.visit = 1; }","    else if (e.kind === 'ask'){ NB2.ask[e.code] = 1; b.ask = 1; }\n    else if (e.kind === 'note'){ (ST.notes = ST.notes || []).push({ id: e.id, code: e.code, name: e.name || 'Hàng xóm', t: +pl.t || 0, st: +pl.st || 0, spot: pl.spot, gk: pl.gk && (pl.gs ? CROPS[pl.gk] : GD(pl.gk)) ? pl.gk : '', gs: pl.gs ? 1 : 0 }); b.note = pl.spot; } else b.visit = 1; }")
rep("if (b.ask) bits.push('xin con ít hạt giống');","if (b.ask) bits.push('xin con ít hạt giống'); if (b.note && NOTE.spots[b.note]) bits.push(`giấu lá thư ở ${noteSp(b.note)}`);")
# Sổ
rep("const BSTK = ['giong', 'ca', 'buom', 'cotich'], BSTN = { giong: 'Giống', ca: 'Cá', buom: 'Bướm', cotich: 'Cổ tích' };","const BSTK = ['giong', 'ca', 'buom', 'cotich', 'thu'], BSTN = { giong: 'Giống', ca: 'Cá', buom: 'Bướm', cotich: 'Cổ tích', thu: 'Thư' };")
rep("const tabOn = k => { const lv = ST.lv || 1; if (k === 'ca')","const tabOn = k => { const lv = ST.lv || 1; if (k === 'thu') return (ST.notes || []).length > 0; if (k === 'ca')")
rep("buom: ['Sổ bướm', '#E8B850', '#B0702A', 'bu_phuong'] };","buom: ['Sổ bướm', '#E8B850', '#B0702A', 'bu_phuong'], thu: ['Thư bạn bè', '#E8A98E', '#B5553A', 'thu'] };")
rep("else if (tab === 'cotich'){ L = pgCotich(nr ? 0 : 1); Rr = nr ? '' : pgCotich(2); }","else if (tab === 'cotich'){ L = pgCotich(nr ? 0 : 1); Rr = nr ? '' : pgCotich(2); } else if (tab === 'thu'){ L = pgThu(nr ? 0 : 1); Rr = nr ? '' : pgThu(2); }")
rep("'1 ' + GD(g.k).unit + ' ' + GD(g.k).name.toLowerCase()","noteItem({ gk: g.k })")
open(dst,'w',encoding='utf-8').write(s)
