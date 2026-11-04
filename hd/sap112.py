# v112a · Sắp vườn (anh Ares duyệt mock 4/11/2026)
#  1. Nhấn giữ một món đang đặt (nong, khạp, lò, hố ủ, thùng ong, đồ kiểng, cây cổ tích) là nhấc lên kéo đi:
#     ô hợp lệ viền xanh nét đứt, ô không được tô đỏ kèm lý do; thả vào chỗ xanh hiện 3 nút Đặt / Hủy / Cất (cây cổ tích: Về chỗ cũ).
#  2. Chế độ Sắp vườn (nút dưới "Về giữa", từ cấp 8): ẩn HUD và bong bóng, thanh trên "Đang sắp vườn · Xong",
#     ô trống có nút +, chạm thì bung Liếp / Cây; khay Túi đồ dưới đáy: kéo đồ ra vườn, kéo đồ vô khay để cất, món chưa mua có giá.
#  3. Chạm ô đất trống ngoài chế độ: bảng gọn (Đắp liếp + một dòng dẫn sang Sắp vườn), từ cấp 8.
#  4. Đồ được cất vô túi (nong, khạp… lúc chưa đặt): đồ đang phơi, muối giữ nguyên tiến độ.
#  5. Ao/khai hoang báo "còn 1 phút" hoài: phút cuối đếm giây, hết giờ chạm vô là xong liền; mỗi việc trong vòng vẽ chạy riêng, một việc lỗi không chặn việc khác.
# Dùng: python3 sap112.py live/v110e.html live/v112a.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:90], c, n); s = s.replace(a, b)

LAYSVG = '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M4 9l8-4 8 4-8 4zM4 15l8-4 8 4-8 4z" fill="#FFF8EA" stroke="#4A2F1E" stroke-width="1.8" stroke-linejoin="round"/></svg>'

# ---------- HTML ----------
rep('<span class="tg">Sửa vườn</span>', '<span class="tg">Sắp vườn</span>')
rep('id="bSua" aria-label="Sửa vườn"', 'id="bSua" aria-label="Sắp vườn"')
rep('<div class="card vbar sbar" id="suaBar" hidden><div><b id="suaHd">Đặt đồ</b><span id="suaTx"></span></div><button class="btn" id="suaOk">Hủy</button></div>',
    '<div class="card vbar sbar" id="suaBar" hidden><div><b id="suaHd">Đặt đồ</b><span id="suaTx"></span></div><button class="btn" id="suaOk">Hủy</button></div>'
    '<svg id="sapSvg" hidden aria-hidden="true"></svg><div id="sapLay"></div><div id="sapChips" hidden></div><div id="sapTip" hidden></div><div id="sapBtns" hidden></div><img id="sapGhost" hidden alt="">'
    '<div id="sapBar" hidden role="toolbar" aria-label="Sắp vườn"><span class="ic">' + LAYSVG + '</span><b>Đang sắp vườn</b><button class="btn g" id="sapOk">Xong</button></div>'
    '<div id="sapTray" hidden aria-label="Túi đồ"></div>')

# ---------- CSS ----------
CSS = r'''
/* v112 Sắp vườn */
#sapSvg{position:fixed;left:0;top:0;width:100vw;height:100vh;z-index:3;pointer-events:none;overflow:visible}
#sapSvg[hidden]{display:none}
#sapSvg polygon{stroke-width:3;stroke-linejoin:round}
#sapSvg .em{fill:rgba(255,248,234,.22);stroke:#FFF8EA;stroke-dasharray:7 5}
#sapSvg .sel{fill:rgba(242,198,74,.4);stroke:#C08A12}
#sapSvg .ok{fill:rgba(125,184,74,.28);stroke:#4F7D44;stroke-dasharray:7 5}
#sapSvg .no{fill:rgba(217,72,58,.26);stroke:#9C3620}
#sapSvg .fit{fill:rgba(125,184,74,.5);stroke:#2F5A2A;stroke-width:4}
#sapSvg .bad{fill:rgba(217,72,58,.45);stroke:#9C3620;stroke-width:4}
#sapLay{position:fixed;left:0;top:0;width:0;height:0;z-index:4}
.sapplus{position:absolute;left:0;top:0;width:44px;height:44px;box-sizing:border-box;border-radius:50%;background:#7DB84A;border:2px solid #4A2F1E;box-shadow:0 3px 0 #4A2F1E;color:#fff;display:flex;align-items:center;justify-content:center;padding:0;cursor:pointer;-webkit-tap-highlight-color:transparent}
.sapplus.on{background:#F2C64A;color:#4A2F1E}
.sapplus svg{display:block;flex:none}
#sapChips{position:fixed;left:0;top:0;z-index:5;display:flex;gap:6px}
#sapChips[hidden],#sapTip[hidden],#sapBtns[hidden],#sapGhost[hidden]{display:none}
#sapChips button{display:flex;align-items:center;gap:5px;box-sizing:border-box;min-height:44px;background:#fff;border:2px solid #4A2F1E;border-radius:10px;box-shadow:0 3px 0 #4A2F1E;padding:4px 12px 4px 8px;font:400 15px var(--f-game);color:#4A2F1E;cursor:pointer;white-space:nowrap}
#sapChips img{width:26px;height:26px;flex:none}
#sapTip{position:fixed;left:0;top:0;z-index:6;background:#fff;border:2px solid #4A2F1E;border-radius:6px;box-shadow:0 2px 0 #4A2F1E;padding:3px 8px;font:600 13px var(--f-body);color:#9C3620;white-space:nowrap;pointer-events:none}
#sapBtns{position:fixed;left:0;top:0;z-index:6;display:flex;gap:10px}
#sapBtns button{width:48px;height:48px;box-sizing:border-box;border-radius:50%;border:2px solid #4A2F1E;box-shadow:0 3px 0 #4A2F1E;display:flex;align-items:center;justify-content:center;padding:0;cursor:pointer}
#sapBtns button svg{display:block;flex:none}
#sapBtns .y{background:#7DB84A}#sapBtns .n{background:#D9483A}#sapBtns .s{background:#FFF8EA}
#sapGhost{position:fixed;left:0;top:0;z-index:9;width:84px;height:84px;transform:translate(-50%,-118%);pointer-events:none;filter:drop-shadow(0 6px 0 rgba(43,52,70,.25))}
#sapGhost.bad{opacity:.55}
#sapBar{position:fixed;left:50%;top:calc(12px + env(safe-area-inset-top,0px));transform:translateX(-50%);z-index:8;display:flex;align-items:center;gap:10px;box-sizing:border-box;max-width:calc(100vw - 32px);background:#FFF8EA;border:2px solid #4A2F1E;border-radius:16px;box-shadow:0 3px 0 #4A2F1E;padding:6px 6px 6px 8px;white-space:nowrap}
#sapBar[hidden],#sapTray[hidden]{display:none}
#sapBar .ic{width:32px;height:32px;box-sizing:border-box;border-radius:10px;background:#F2C64A;border:2px solid #4A2F1E;display:flex;align-items:center;justify-content:center;flex:none}
#sapBar b{font:400 16px var(--f-game);color:#4A2F1E}
#sapBar .btn{min-height:40px;margin:0;padding:4px 18px}
#sapTray{position:fixed;left:8px;right:8px;margin:0 auto;max-width:max-content;box-sizing:border-box;bottom:calc(10px + env(safe-area-inset-bottom,0px));z-index:8;background:#FFF8EA;border:2px solid #4A2F1E;border-radius:16px;box-shadow:0 3px 0 #4A2F1E;padding:14px 8px 8px}
#sapTray .sth small{position:absolute;top:-13px;left:12px;background:#F2C64A;border:2px solid #4A2F1E;border-radius:6px;padding:2px 9px;font:400 12px/1.3 var(--f-game);color:#4A2F1E;white-space:nowrap}
#sapTray .sth .xu{position:absolute;top:-13px;right:12px;display:flex;align-items:center;gap:4px;background:#fff;border:2px solid #4A2F1E;border-radius:6px;padding:1px 8px 1px 4px;font:400 12px/1.3 var(--f-game);color:#4A2F1E}
#sapTray .sth .xu img{width:16px;height:16px}
#sapTray .row{display:flex;flex-wrap:wrap;gap:12px 8px;padding:9px 8px 2px 2px;max-height:38vh;overflow-y:auto}
#sapTray .it{flex:none;width:86px;min-height:74px;box-sizing:border-box;background:#fff;border:2px solid #4A2F1E;border-radius:10px;box-shadow:0 3px 0 #4A2F1E;padding:6px 3px 5px;display:flex;flex-direction:column;align-items:center;gap:3px;font:400 12px/1.15 var(--f-game);color:#4A2F1E;text-align:center;position:relative;touch-action:none;cursor:grab;user-select:none;-webkit-user-select:none}
#sapTray .it>img{width:36px;height:36px;flex:none;pointer-events:none;-webkit-user-drag:none}
#sapTray .it>span{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
#sapTray .it .n{position:absolute;top:-8px;right:-7px;min-width:22px;height:22px;box-sizing:border-box;border-radius:11px;background:#D9483A;color:#fff;border:2px solid #4A2F1E;font:400 12px/18px var(--f-game);text-align:center;padding:0 4px}
#sapTray .it em{display:flex;align-items:center;gap:3px;font:400 12px/1 var(--f-game);font-style:normal;color:#6B4529}
#sapTray .it em img{width:14px;height:14px}
#sapTray .it.buy{background:#FBF3DF}
#sapTray .it.poor{opacity:.55}
#sapTray .it.more{background:#F3FBE9;cursor:pointer}
#sapTray .it .pl{width:36px;height:36px;flex:none;box-sizing:border-box;border-radius:50%;background:#7DB84A;border:2px solid #4A2F1E;color:#fff;display:flex;align-items:center;justify-content:center}
#sapTray .emp{font:600 13px var(--f-body);color:#6B4529;padding:6px 4px;max-width:260px}
body.sap .ui.bot,body.sap .ui.top,body.sap #nxq,body.sap #tray,body.sap #bCtr,body.sap #bSua,body.sap #fan,body.sap .nava{visibility:hidden!important}
body.sapdrag #nxq,body.sapdrag #tray,body.sapdrag #ring{visibility:hidden!important}
body.sheeton #sapBar,body.sheeton #sapTray,body.sheeton #sapLay,body.sheeton #sapChips,body.sheeton #sapBtns{visibility:hidden!important}
.bt.ctr .tg{font-size:12px!important}
body.sap #tstw{top:calc(76px + env(safe-area-inset-top,0px))!important;bottom:auto!important;left:16px!important;right:16px!important;transform:none!important;width:auto!important}
/* Sổ: mép trên, mép dưới của trang cuộn mờ dần cùng màu giấy, thẻ trôi vô là tan dần chứ không bị cắt ngang */
#bk .bkpg::before,#bk .bkpg::after{content:'';display:block;flex:none;position:sticky;z-index:6;pointer-events:none;align-self:stretch}
#bk .bkpg::before{top:-18px;height:26px;margin:-18px 0 -8px;background:linear-gradient(#FBF7EE 25%,rgba(251,247,238,0))}
#bk .bkpg::after{bottom:-22px;height:26px;margin:-8px 0 -22px;background:linear-gradient(rgba(251,247,238,0),#FBF7EE 75%)}
/* tiêu đề mục trong Sổ: chữ nhỏ xuống dòng dưới, thẳng mép trái với tiêu đề */
#bk .uxt{flex-wrap:wrap;row-gap:2px}
#bk .uxt>small{flex-basis:100%;margin:0!important;text-align:left!important;font:600 12px/1.3 var(--f-body)!important;color:#6B4529!important}
.sapalt{display:flex;align-items:center;gap:8px;margin-top:10px;font:600 13px var(--f-body);color:#4A2F1E}
.sapalt .ics{display:flex;flex:none}
.sapalt .ics img{width:28px;height:28px;box-sizing:border-box;margin-right:-6px;background:#fff;border:2px solid #4A2F1E;border-radius:50%;padding:2px}
.sapalt .tx{flex:1;margin-left:10px;min-width:0}
.sapalt .btn{flex:none;margin:0;min-height:40px;padding:4px 12px;background:#F2C64A}
'''
rep("body.sheeton #suaBar{display:none!important}", "body.sheeton #suaBar{display:none!important}" + CSS)

# ---------- JS ----------
JS = r'''
/* ===== v112 Sắp vườn: nhấn giữ để nhấc đồ, chế độ Sắp vườn (nút + trên ô trống, khay Túi đồ), một cách đặt cho mọi món ===== */
let SAP = false, DRAG = null, DROP = null, SAPSEL = null, SHSUB = null, SAPON = false, SAPITEMS = [], TRAYP = null;
const SAPLV = 8;
const sapOk = () => (ST.lv || 1) >= SAPLV && !VISIT && baiOn();
const SAPSV = { ok: '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#fff" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  no: '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke="#fff" stroke-width="3.6" stroke-linecap="round"/></svg>',
  box: '<svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path d="M3 8l9-4 9 4v9l-9 4-9-4z" fill="#E0A95C" stroke="#4A2F1E" stroke-width="2" stroke-linejoin="round"/><path d="M3 8l9 4 9-4M12 12v9" fill="none" stroke="#4A2F1E" stroke-width="2"/></svg>',
  home: '<svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path d="M3 11l9-7 9 7" fill="none" stroke="#4A2F1E" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M6 10v10h12V10" fill="#E0A95C" stroke="#4A2F1E" stroke-width="2" stroke-linejoin="round"/><path d="M10 20v-5h4v5" fill="#FFF8EA" stroke="#4A2F1E" stroke-width="2"/></svg>',
  plus: '<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="4" stroke-linecap="round"/></svg>' };
const SAPIC = 'data:image/svg+xml;utf8,' + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect x="5" y="5" width="54" height="54" rx="14" fill="#F2C64A" stroke="#4A2F1E" stroke-width="4"/><path d="M14 26l18-9 18 9-18 9z" fill="#FFF8EA" stroke="#4A2F1E" stroke-width="3.5" stroke-linejoin="round"/><path d="M14 38l18-9 18 9-18 9z" fill="#B9D79F" stroke="#4A2F1E" stroke-width="3.5" stroke-linejoin="round"/></svg>');
function sapIc(it){ if (it.t === 'obj') return ICON[it.k === 'ong' ? 'matong' : it.k] || UIC.task; if (it.t === 'dc') return UIC['dc_' + it.k] || UIC.task; if (it.t === 'ao') return ICON.caro; return UIC['ft_' + it.k] || UIC.task; }
function sapName(it){ return it.t === 'obj' ? OBJD[it.k].title : it.t === 'dc' ? DCK[it.k].name : it.t === 'ao' ? BIGD.ao.title : BIGD[it.k].title; }
// món đang nằm ở ô id, nhấc lên được
function sapItemAt(id){ const P = id && PL[id]; if (!P || !P.bai || hidP(P)) return null; const ok = objAt(id); if (ok) return bldOn(ok) ? null : { t: 'obj', k: ok, from: id }; const di = decoAt(id); if (di >= 0) return { t: 'dc', k: ST.dc.items[di].k, from: id }; const bk = bigAt(id); if (bk && BIGD[bk] && BIGD[bk].fairy) return { t: 'big', k: bk, from: ST.big[bk].at }; return null; }
// ô id còn trống cho món it (ô món đang đứng tính là trống)
function sapFree(id, it){ const P = PL[id]; if (!P || !P.bai || hidP(P) || !landOwn(id) || !locked(P) || pairHost(id) || (ST.pairs || {})[id]) return false; const bk = bigAt(id); if (bk && !(it && it.t === 'big' && bk === it.k)) return false; if (decoAt(id) >= 0 && !(it && it.t === 'dc' && id === it.from)) return false; const ok = objAt(id); if (ok && !(it && it.t === 'obj' && ok === it.k)) return false; return true; }
function sapWhy(id, it){ const P = PL[id]; if (!P || !P.bai) return ''; if (!landOwn(id)) return 'Chưa khai hoang'; if (!locked(P)) return 'Đang có liếp'; if (pairHost(id) || (ST.pairs || {})[id]) return 'Đang có cây trái'; if ((it.t === 'big' || it.t === 'ao') && sapFree(id, it)) return 'Cần 4 ô trống, 2 ngang 2 dọc'; return 'Đang có đồ'; }
const sapBk = it => it.t === 'ao' ? 'ao' : it.k;
function sapFit(id, it){ if (!id) return null; if (it.t === 'big' || it.t === 'ao'){ const a = bigFit(id, sapBk(it)); return a ? block4(a) : null; } return sapFree(id, it) ? [id] : null; }
function sapCellXY(cx, cy){ const g = groundAt(cx, cy); if (!g) return null; const x = g.x, z = g.z; let best = null, bd = .2; for (const P of PLOTS){ if (!P.bai || hidP(P)) continue; const [u0, v0, u1, v1] = P.b, d = Math.hypot(Math.max(u0 - x, 0, x - u1), Math.max(v0 - z, 0, z - v1)); if (d < bd){ bd = d; best = P.id; } } return best; }
function sapGrab(cx, cy, id){ if (!sapOk()) return null; try { const fh = ftHitAt(cx, cy); if (fh && fh.k && BIGD[fh.k] && BIGD[fh.k].fairy && ST.ft[fh.k] && ST.ft[fh.k].st >= 1) return { t: 'big', k: fh.k, from: (ST.big[fh.k] || {}).at || null }; } catch (e) {} return sapItemAt(id || sapCellXY(cx, cy)); }
// đặt món it vào ô id (mua luôn nếu chưa có)
function sapPut(it, id){
  if (it.t === 'obj'){ const O = ST[it.k]; if (!O.own){ if (!sapFree(id, it)) return false; buyObj(it.k, id); return !!(O.own && O.at === id); } if (O.at === id) return true; return placeObj(it.k, id); }
  if (it.t === 'dc'){ if (it.from){ const D = (ST.dc.items || []).find(x => x.at === it.from && x.k === it.k); if (!D || !sapFree(id, it)) return false; if (D.at === id) return true; const old = D.at; D.at = id; save(); refreshPlot(old); refreshPlot(id); objPuff(id); sfx('pop'); buzz(12); return true; } return dcPlace(it.k, id); }
  if (it.t === 'ao'){ const had = !!(ST.big.ao && ST.big.ao.own); aoBuy(id); return !had && !!(ST.big.ao && ST.big.ao.own); }
  if (it.t === 'big') return bigPlace(it.k, id);
  return false; }
function sapStore(it){
  if (it.t === 'obj'){ const O = ST[it.k], old = O.at; if (!old) return false; O.at = null; save(); refreshPlot(old); objPuff(old); sfx('pop'); return true; }
  if (it.t === 'dc'){ const i = (ST.dc.items || []).findIndex(x => x.at === it.from && x.k === it.k); if (i < 0) return false; ST.dc.items.splice(i, 1); ST.dc.bag[it.k] = (ST.dc.bag[it.k] || 0) + 1; save(); refreshPlot(it.from); sfx('pop'); return true; }
  if (it.t === 'big'){ if (!(ST.big[it.k] || {}).at) return false; bigHome(it.k); return true; }
  return false; }
function sapNow(it, id){ if (it.t === 'obj') return { t: 'obj', k: it.k, from: ST[it.k].at }; if (it.t === 'dc') return { t: 'dc', k: it.k, from: id }; if (it.t === 'big') return { t: 'big', k: it.k, from: (ST.big[it.k] || {}).at || null }; return null; }
// kéo
function sapDragStart(it, cx, cy){ DROP = null; window.__sapLift = it.from || it.t === 'big' ? it.t + ':' + it.k : null; DRAG = { it, x: cx, y: cy, hov: null, fit: null, tray: false }; try { ctl.enabled = false; } catch (e) {} SAPSEL = null; if (SHEET) closeSheet(); buzz(20); sfx('pick'); const gh = $('#sapGhost'); gh.src = sapIc(it); gh.hidden = false; document.body.classList.add('sapdrag'); sapDragMove(cx, cy); }
function sapTrayHit(cx, cy){ const t = $('#sapTray'); if (!t || t.hidden) return false; const r = t.getBoundingClientRect(); return cx >= r.left && cx <= r.right && cy >= r.top - 8 && cy <= r.bottom; }
function sapDragMove(cx, cy){ if (!DRAG) return; DRAG.x = cx; DRAG.y = cy; const gh = $('#sapGhost'); gh.style.left = cx + 'px'; gh.style.top = cy + 'px'; DRAG.tray = SAP && sapTrayHit(cx, cy); const id = DRAG.tray ? null : sapCellXY(cx, cy); DRAG.hov = id; DRAG.fit = id ? sapFit(id, DRAG.it) : null; gh.classList.toggle('bad', !!id && !DRAG.fit); }
function sapDragEnd(){ const D = DRAG; DRAG = null; window.__sapLift = null; $('#sapGhost').hidden = true; document.body.classList.remove('sapdrag'); try { ctl.enabled = !FM.on; } catch (e) {} if (!D) return; const it = D.it;
  if (D.tray){ if (it.from && sapStore(it)) toast(`Đã cất ${sapName(it).toLowerCase()} vô túi`); sapTrayDraw(); return; }
  if (!D.fit){ if (D.hov && D.hov !== it.from) toast(sapWhy(D.hov, it), 'dan', { now: true }); return; }
  if (it.from && (it.t === 'big' ? bigFit(D.hov, it.k) === it.from : D.fit[0] === it.from)) return;   // thả lại chỗ cũ
  const prev = it.t === 'big' ? ((ST.big[it.k] || {}).at || null) : (it.from || null), buy = (it.t === 'obj' && !ST[it.k].own) || it.t === 'ao';
  if (!sapPut(it, D.hov)) return; sapTrayDraw(); hud();
  if (buy) return;   // mua xong là đặt luôn, khỏi hỏi lại
  const now = sapNow(it, D.fit[0]); if (now && now.from) DROP = { it: now, prev }; }
function sapDropAct(a){ const D = DROP; DROP = null; $('#sapBtns').hidden = true; if (!D) return; if (a === 'no'){ if (D.prev) sapPut(D.it, D.prev); else sapStore(D.it); } else if (a === 'box') sapStore(D.it); else sfx('pop'); sapTrayDraw(); }
// chế độ Sắp vườn
function sapMode(on){ if (on && !sapOk()) return; SAP = !!on; DROP = null; SAPSEL = null; document.body.classList.toggle('sap', SAP); $('#sapBar').hidden = !SAP; $('#sapTray').hidden = !SAP; placeSua();
  if (SAP){ if (SHEET) closeSheet(); try { if (SUA) suaOn(false); } catch (e) {} sapTrayDraw(); try { camTo(new T.Vector3(BAIC.x + .4, .3, BAIC.z + .6), Math.max(cam.zoom, DEFZ() * 1.05)); } catch (e) {} sayOnce('sap1', 'Đất của con, muốn đặt gì ở đâu cũng được. Nhấn giữ món nào là nhấc lên kéo đi, kéo vô túi là cất.', 'vui'); }
  else { $('#sapChips').hidden = true; sapClear(); } }
function sapBag(){ const L = [], B = []; for (const k of OBJK){ const O = ST[k]; if (!O || !objOn(k)) continue; if (O.own && !O.at) L.push({ t: 'obj', k, n: 1 }); else if (!O.own) B.push({ t: 'obj', k, buy: OBJD[k].buy }); }
  for (const k in (ST.dc.bag || {})) if (ST.dc.bag[k] > 0 && DCK[k]) L.push({ t: 'dc', k, n: ST.dc.bag[k] });
  if (((ST.lv || 1) >= BIGD.ao.lv || (ST.keep || {}).ao) && !(ST.big.ao && ST.big.ao.own)) B.push({ t: 'ao', k: 'ao', buy: BIGD.ao.buy }); return [...L, ...B]; }
function sapTrayDraw(){ const t = $('#sapTray'); if (!t || !SAP) return; SAPITEMS = sapBag();
  let h = `<div class="sth"><small>TÚI ĐỒ · kéo ra vườn</small><span class="xu"><img src="${UIC.coin}" alt="">${ST.xu.toLocaleString('vi-VN')}</span></div><div class="row">`;
  h += SAPITEMS.map((it, i) => `<div class="it${it.buy ? ' buy' : ''}${it.buy && ST.xu < it.buy ? ' poor' : ''}" data-i="${i}"><img src="${sapIc(it)}" alt=""><span>${sapName(it)}</span>${it.n > 1 ? `<b class="n">${it.n}</b>` : ''}${it.buy ? `<em><img src="${UIC.coin}" alt="">${it.buy}</em>` : ''}</div>`).join('');
  if (dcOn()) h += `<div class="it more" data-a="more"><span class="pl">${SAPSV.plus}</span><span>Mua thêm</span></div>`;
  if (!SAPITEMS.length && !dcOn()) h += `<div class="emp">Túi đang trống. Nhấn giữ món nào ngoài vườn rồi kéo vô đây là cất.</div>`;
  t.innerHTML = h + '</div>'; }
function sapChipsDraw(){ const ch = $('#sapChips'); const tree = Object.keys(CROPS).filter(k => CROPS[k].tree && !CROPS[k].rare && unlocked(k));
  ch.innerHTML = `<button data-c="liep"><img src="${ICON.cai}" alt="">Liếp</button>` + (tree.length ? `<button data-c="cay"><img src="${ICON[tree[tree.length - 1]] || ICON.xoai}" alt="">Cây</button>` : ''); }
function sapPick(id){ SAPSEL = SAPSEL === id ? null : id; if (SAPSEL){ sapChipsDraw(); sfx('pick'); } }
function sapTap(cx, cy){ if (DROP){ DROP = null; return; } const id = sapCellXY(cx, cy); if (id && sapFree(id, null)) return sapPick(id); SAPSEL = null; if (id && sapItemAt(id)) toast('Nhấn giữ rồi kéo để dời, kéo vô túi để cất'); }
function sapAltHTML(){ const tree = Object.keys(CROPS).filter(k => CROPS[k].tree && !CROPS[k].rare && unlocked(k)), ics = [tree.length ? ICON[tree[tree.length - 1]] : null, ICON.nong, dcOn() ? UIC.dc_mai_chieu_thuy : ICON.khap].filter(Boolean);
  return `<div class="sapalt"><span class="ics">${ics.map(u => `<img src="${u}" alt="">`).join('')}</span><span class="tx">${tree.length ? 'Trồng cây, đặt đồ ở đây' : 'Đặt đồ ở đây'}</span><button class="btn" data-a="sapgo"><span>Sắp vườn</span></button></div>`; }
// lớp vẽ: chạy trong vòng vẽ, ngay trước khi vẽ cảnh
const sapV = new T.Vector3();
function sapPj(x, z, y = .03){ sapV.set(x, y, z).project(cam); return [(sapV.x + 1) / 2 * innerWidth, (1 - sapV.y) / 2 * innerHeight]; }
function sapPoly(b, i = .04){ return [[b[0] + i, b[1] + i], [b[2] - i, b[1] + i], [b[2] - i, b[3] - i], [b[0] + i, b[3] - i]].map(([x, z]) => sapPj(x, z).map(v => v.toFixed(1)).join(',')).join(' '); }
function sapUnion(ids){ const bs = ids.map(x => PL[x].b); return [Math.min(...bs.map(b => b[0])), Math.min(...bs.map(b => b[1])), Math.max(...bs.map(b => b[2])), Math.max(...bs.map(b => b[3]))]; }
const sapMid = P => sapPj((P.b[0] + P.b[2]) / 2, (P.b[1] + P.b[3]) / 2);
const sapX = (x, w) => Math.max(8, Math.min(innerWidth - w - 8, x - w / 2));
function sapClear(){ SAPON = false; const sv = $('#sapSvg'); sv.innerHTML = ''; sv.dataset.h = ''; sv.setAttribute('hidden', ''); $('#sapLay').innerHTML = ''; for (const k of ['#sapChips', '#sapTip', '#sapBtns']) $(k).hidden = true; }
function sapTick(){ if (VISIT){ if (SAP) sapMode(false); DRAG = null; DROP = null; sapClear(); return; } SAPON = true; const sv = $('#sapSvg'), lay = $('#sapLay'); sv.removeAttribute('hidden'); let h = ''; const cells = PLOTS.filter(P => P.bai && !hidP(P) && landOwn(P.id));
  if (DRAG){ const it = DRAG.it; for (const P of cells){ if (DRAG.fit && DRAG.fit.includes(P.id)) continue; const ok = it.t === 'big' || it.t === 'ao' ? !!bigFit(P.id, sapBk(it)) : sapFree(P.id, it); h += `<polygon class="${ok ? 'ok' : 'no'}" points="${sapPoly(P.b)}"/>`; }
    if (DRAG.fit) h += `<polygon class="fit" points="${sapPoly(sapUnion(DRAG.fit), .03)}"/>`; else if (DRAG.hov && DRAG.hov !== DRAG.it.from) h += `<polygon class="bad" points="${sapPoly(PL[DRAG.hov].b)}"/>`; }
  else if (DROP){ const cs = DROP.it.t === 'big' ? bigCells(DROP.it.k) : [DROP.it.from]; if (cs.length && cs[0] && PL[cs[0]]) h += `<polygon class="fit" points="${sapPoly(sapUnion(cs), .03)}"/>`; else DROP = null; }
  else if (SAP){ for (const P of cells) if (sapFree(P.id, null)) h += `<polygon class="${P.id === SAPSEL ? 'sel' : 'em'}" points="${sapPoly(P.b)}"/>`; }
  if (sv.dataset.h !== h){ sv.innerHTML = h; sv.dataset.h = h; }
  // nút + trên ô trống
  let n = 0; if (SAP && !DRAG && !DROP) for (const P of cells){ if (!sapFree(P.id, null)) continue; let b = lay.children[n++]; if (!b){ b = document.createElement('button'); b.className = 'sapplus'; b.innerHTML = SAPSV.plus; b.setAttribute('aria-label', 'Đặt gì ở ô này'); lay.appendChild(b); } b.dataset.id = P.id; b.classList.toggle('on', P.id === SAPSEL); const [x, y] = sapMid(P); b.style.transform = `translate(${(x - 22).toFixed(1)}px,${(y - 22).toFixed(1)}px)`; }
  while (lay.children.length > n) lay.lastChild.remove();
  if (SAPSEL && !sapFree(SAPSEL, null)) SAPSEL = null;
  const ch = $('#sapChips'); if (SAP && SAPSEL && !DRAG && !DROP){ const [x, y] = sapMid(PL[SAPSEL]); ch.hidden = false; const w = ch.offsetWidth || 200, bar = $('#sapBar').getBoundingClientRect().bottom + 8; ch.style.transform = `translate(${sapX(x, w).toFixed(1)}px,${Math.max(bar, y - 76).toFixed(1)}px)`; } else ch.hidden = true;
  const tp = $('#sapTip'); if (DRAG && DRAG.hov && !DRAG.fit && DRAG.hov !== DRAG.it.from){ const [x, y] = sapMid(PL[DRAG.hov]), tx = sapWhy(DRAG.hov, DRAG.it); if (tp.textContent !== tx) tp.textContent = tx; tp.hidden = false; const w = tp.offsetWidth || 100; tp.style.transform = `translate(${sapX(x, w).toFixed(1)}px,${(y + 16).toFixed(1)}px)`; } else tp.hidden = true;
  const bt = $('#sapBtns'); if (DROP && !DRAG){ const cs = DROP.it.t === 'big' ? bigCells(DROP.it.k) : [DROP.it.from], B = sapUnion(cs), pts = [[B[0], B[1]], [B[2], B[1]], [B[2], B[3]], [B[0], B[3]]].map(([x, z]) => sapPj(x, z)), xs = pts.map(p => p[0]), ys = pts.map(p => p[1]);
    const k = DROP.it.t === 'big' ? 'home' : 'box', lbl = DROP.it.t === 'big' ? 'Về chỗ cũ' : 'Cất vô túi'; if (bt.dataset.k !== k){ bt.dataset.k = k; bt.innerHTML = `<button class="y" data-d="ok" aria-label="Đặt ở đây">${SAPSV.ok}</button><button class="n" data-d="no" aria-label="Hủy">${SAPSV.no}</button><button class="s" data-d="box" aria-label="${lbl}">${SAPSV[k]}</button>`; }
    bt.hidden = false; const w = bt.offsetWidth || 164, lim = SAP ? $('#sapTray').getBoundingClientRect().top - 58 : innerHeight - 120; bt.style.transform = `translate(${sapX((Math.min(...xs) + Math.max(...xs)) / 2, w).toFixed(1)}px,${Math.max(8, Math.min(lim, Math.max(...ys) + 10)).toFixed(1)}px)`; } else bt.hidden = true; }
function tk(n, f){ try { f(); } catch (e) { const E = window.__tke = window.__tke || {}; if (!E[n]){ E[n] = 1; console.warn('tick ' + n, e); } } }   /* mỗi việc trong vòng vẽ chạy riêng, một việc lỗi không chặn việc khác */
'''
rep("await LDY(69);\n/* ===== UX kit", JS + "await LDY(69);\n/* ===== UX kit")

# sự kiện: thanh, khay, nút, phím
rep("$('#bSua').addEventListener('click', () => { suaOn(!SUA); });",
    "$('#bSua').addEventListener('click', () => { sapMode(!SAP); }); $('#sapOk').addEventListener('click', () => { sfx('pop'); sapMode(false); });\n"
    "$('#sapLay').addEventListener('click', e => { const b = e.target.closest('.sapplus'); if (b) sapPick(b.dataset.id); });\n"
    "$('#sapChips').addEventListener('click', e => { const b = e.target.closest('[data-c]'); if (!b || !SAPSEL) return; const id = SAPSEL; SAPSEL = null; if (b.dataset.c === 'liep'){ act.openBed(id); sfx('pop'); } else if (b.dataset.c === 'cay'){ if (!treeSpot(id)) return toast('Cây trái chiếm hai ô, ô ngay dưới cũng phải trống', 'dan', { now: true }); SHSUB = 'cay'; openSheet('plot', id); } });\n"
    "$('#sapBtns').addEventListener('click', e => { const b = e.target.closest('[data-d]'); if (b) sapDropAct(b.dataset.d); });\n"
    "$('#sapTray').addEventListener('pointerdown', e => { const c = e.target.closest('.it'); if (!c || c.dataset.a === 'more') return; const it = SAPITEMS[+c.dataset.i]; if (!it) return; if (it.buy && ST.xu < it.buy) return toast(`${sapName(it)} ${it.buy} xu, con còn thiếu ${it.buy - ST.xu} xu.`, 'dan', { now: true }); TRAYP = { pid: e.pointerId, x: e.clientX, y: e.clientY, it: { t: it.t, k: it.k } }; try { c.releasePointerCapture(e.pointerId); } catch (er) {} });\n"
    "$('#sapTray').addEventListener('click', e => { if (e.target.closest('[data-a=\"more\"]')){ openSheet('cho'); SHEET.tab = 'tiem'; renderSheet(); } });\n"
    "addEventListener('pointermove', e => { if (DRAG){ sapDragMove(e.clientX, e.clientY); return; } if (TRAYP && e.pointerId === TRAYP.pid && Math.hypot(e.clientX - TRAYP.x, e.clientY - TRAYP.y) > 8){ const it = TRAYP.it; TRAYP = null; sapDragStart(it, e.clientX, e.clientY); } });\n"
    "addEventListener('pointerup', e => { if (TRAYP && e.pointerId === TRAYP.pid){ TRAYP = null; toast('Kéo món này ra một ô đất trống của con'); } if (DRAG) sapDragEnd(); });\n"
    "addEventListener('pointercancel', () => { TRAYP = null; if (DRAG) sapDragEnd(); });\n"
    "addEventListener('keydown', e => { if (e.key === 'Escape' && SAP && !SHEET) sapMode(false); });\n"
    "setInterval(() => { try { placeSua(); } catch (e) {} }, 1500);")
rep("function placeSua(){ const b = $('#bCtr'), s2 = $('#bSua'); if (!b || !s2) return; s2.hidden = true; if (s2.hidden) return;",
    "function placeSua(){ const b = $('#bCtr'), s2 = $('#bSua'); if (!b || !s2) return; s2.hidden = !sapOk() || SAP || !!SUA; if (s2.hidden) return;")
rep("try { $('#icSua').src = ICON.cuoc; } catch (e) {}", "try { $('#icSua').src = SAPIC; } catch (e) {}")

# nhấn giữ: món đang đặt thì nhấc lên kéo; trong chế độ thì giữ ngắn hơn, không mở bảng
rep("const wg = (() => { if (VISIT) return null;", "const wg = (() => { if (VISIT || SAP) return null;")
rep("need = wg ? 'weed' : id && needOf(id);", "need = SAP ? null : wg ? 'weed' : id && needOf(id);")
rep("G0.tm = setTimeout(() => { if (G0 && !G0.moved && !FM.on && (id || gk)){",
    "G0.tm = setTimeout(() => { if (G0 && !G0.moved && !FM.on){ const it = sapGrab(G0.x, G0.y, id); if (it){ G0.held = true; sapDragStart(it, G0.x, G0.y); return; } if (SAP) return; } if (G0 && !G0.moved && !FM.on && (id || gk)){")
rep("}, 520); }, { capture: true });", "}, SAP ? 300 : 520); }, { capture: true });")
rep("if (g.moved || g.held) return;\n  if (g.wg){",
    "if (g.moved || g.held) return;\n  try { landCheck(); } catch (er) {}\n  if (DROP){ DROP = null; if (!SAP) return; }\n  if (SAP){ sapTap(e.clientX, e.clientY); return; }\n  if (g.wg){")

# bảng ô trống gọn (từ cấp 8) + bảng chỉ trồng cây (chip Cây)
rep("h += UX.hero(ICON.cuoc || UIC.sickle, 'Đất của con',",
    "if (SHSUB === 'cay'){ const ks = Object.keys(CROPS).filter(k => CROPS[k].tree && !CROPS[k].rare && unlocked(k)); return UX.title('Trồng cây trái · chiếm ô này và ô ngay dưới') + '<div class=\"upg\">' + ks.map(k => UX.upc('treeplant', ICON[k], 'Cây ' + CROPS[k].name.toLowerCase(), CROPS[k].seed, { k, dis: ST.xu < CROPS[k].seed })).join('') + '</div>'; }\n"
    "    h += UX.hero(ICON.cuoc || UIC.sickle, 'Đất của con',")
rep("h += UX.cta([UX.btn('openbed', 'Đắp liếp', { g: 1, img: UIC.seedbag })]);",
    "h += UX.cta([UX.btn('openbed', 'Đắp liếp', { g: 1, img: UIC.seedbag })]); if (sapOk()) return h + sapAltHTML();")
rep("const closeSheet = () => { SHEET = null;", "const closeSheet = () => { SHEET = null; try { SHSUB = null; } catch (e) {}")
rep("else if (a === 'openbed'){ act.openBed(id); }", "else if (a === 'openbed'){ act.openBed(id); } else if (a === 'sapgo'){ closeSheet(); sapMode(true); return; }")
rep("a === 'dcput'){ closeSheet(); suaOn(true, 'dc:' + b.dataset.k); return; }",
    "a === 'dcput'){ closeSheet(); if (sapOk()){ if (!SAP) sapMode(true); else sapTrayDraw(); return; } suaOn(true, 'dc:' + b.dataset.k); return; }")

# vẽ: ẩn bong bóng khi sắp vườn / đang kéo, vẽ lớp ô
rep("r.render(S, cam);\n  // UI",
    "const SAPH = []; try { if (SAP || DRAG){ for (const g of (window.__BUBALL || [])) if (g.visible){ g.visible = false; SAPH.push(g); } } if (SAP || DRAG || DROP) sapTick(); else if (SAPON) sapClear(); } catch (e) { if (!window.__sape){ window.__sape = 1; console.warn('sap', e); } }\n"
    "  r.render(S, cam); for (const g of SAPH) g.visible = true;\n  // UI")

rep("const O = ST[k], on = !!(O && O.own && O.at && PV[O.at] && !hidP(PL[O.at]));", "const O = ST[k], on = !!(O && O.own && O.at && PV[O.at] && !hidP(PL[O.at])) && window.__sapLift !== 'obj:' + k;")
rep("const V = FTV[k], F = ST.ft[k], on = !!F; V.root.visible = on;", "const V = FTV[k], F = ST.ft[k], on = !!F; V.root.visible = on && window.__sapLift !== 'big:' + k;")
# ao, lò, chuồng: phút cuối đếm giây; hết giờ chạm vô là xong liền
rep("function bldTell(k){ const l = bldLeft(k), h = Math.floor(l / 3600e3), m = Math.max(1, Math.ceil((l % 3600e3) / 60000)); toast(`${BLDN[k].replace('Bắt đầu', 'Đang')} · còn ${h ? h + ' tiếng ' : ''}${m} phút · bạn ghé phụ bớt 1 tiếng`); }",
    "function bldTell(k){ const l = bldLeft(k); if (l <= 0 && !VISIT){ bldDone(k); return; } const h = Math.floor(l / 3600e3), m = Math.ceil((l % 3600e3) / 60000), tt = l < 60000 ? `${Math.max(1, Math.ceil(l / 1000))} giây` : `${h ? h + ' tiếng' : ''}${h && m ? ' ' : ''}${m ? m + ' phút' : ''}`; toast(`${BLDN[k].replace('Bắt đầu', 'Đang')} · còn ${tt} · bạn ghé phụ bớt 1 tiếng`); }")
# vòng vẽ: mỗi việc chạy riêng
OLD = "try { nongTick(t); khapTick(t); hoTick(t); ongTick(t); loTick(t); cauTick(t, dt); kcaTick(t); kbenTick(); ftTick(t); aoTick(t); dcTick(); buTick(t, dt); muongTick(); boTick(); sayTick(t, dt); gioTick(t); gheTick(t); tbTick(t); treTick(); try { landTick(t);"
NEW = ("try { tk('nong', () => nongTick(t)); tk('khap', () => khapTick(t)); tk('ho', () => hoTick(t)); tk('ong', () => ongTick(t)); tk('lo', () => loTick(t)); tk('cau', () => cauTick(t, dt)); tk('kca', () => kcaTick(t)); tk('kben', () => kbenTick()); tk('ft', () => ftTick(t)); tk('ao', () => aoTick(t)); tk('dc', () => dcTick()); tk('bu', () => buTick(t, dt)); tk('muong', () => muongTick()); tk('bo', () => boTick()); tk('say', () => sayTick(t, dt)); tk('gio', () => gioTick(t)); tk('ghe', () => gheTick(t)); tk('tb', () => tbTick(t)); tk('tre', () => treTick()); try { landTick(t);")
rep(OLD, NEW)
# thùng ong đang cất thì không lấy mật
rep("function ongTake(){ const O = ST.ong; if (!O || !O.honey) return false;", "function ongTake(){ const O = ST.ong; if (!O || !O.honey || !O.at) return false;")

rep("const BUILD = 'v110e'", "const BUILD = 'v112a'")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
