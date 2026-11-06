# qc115: lỗi QC cũ. python3 qc115.py live/v114f.html live/v115_1.html
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
# hộp thư: báo nhận lỗi mạng thì lần sau không cộng quà lần nữa
rep("catch (e) { return; } if (!L || !L.length) return;\n  const by = {}, ids = []; for (const e of L){ ids.push(e.id);","catch (e) { return; } if (!L || !L.length) return; const seenIn = new Set(ST.inboxIds || []), allIds = L.map(e => e.id), fresh = L.filter(e => !seenIn.has(e.id)); if (!fresh.length){ try { await rpc('mv2_ack', { p_code: CLOUD.cred.code, p_secret: CLOUD.cred.secret, p_ids: allIds }); } catch (e) {} return; }\n  const by = {}, ids = []; for (const e of fresh){ ids.push(e.id);")
rep("save(); for (const P of PLOTS) refreshPlot(P.id); hud(); try { await rpc('mv2_ack', { p_code: CLOUD.cred.code, p_secret: CLOUD.cred.secret, p_ids: ids }); } catch (e) {}","ST.inboxIds = [...seenIn, ...ids].slice(-300); save(); for (const P of PLOTS) refreshPlot(P.id); hud(); try { await rpc('mv2_ack', { p_code: CLOUD.cred.code, p_secret: CLOUD.cred.secret, p_ids: allIds }); } catch (e) {}")
# khôi phục từ mạng: giữ mốc lần chơi cuối để đồ đang phơi, đang nấu tính đủ thời gian
rep("localStorage.setItem('mv2-state', JSON.stringify({ ...r.data, rev: r.rev ?? r.data.rev ?? 0, real: Date.now() }));","localStorage.setItem('mv2-state', JSON.stringify({ ...r.data, rev: r.rev ?? r.data.rev ?? 0, real: Math.min(Date.now(), r.data.real || Date.now()) }));")
# món không bán được thì không bán
rep("sell(k, n){ const SRC = STORE(k);","sell(k, n){ if (GD(k) && GD(k).nosell) return; const SRC = STORE(k);")
rep("const items = Object.entries(ST.inv).filter(([k, n]) => n > 0 && GD(k)),","const items = Object.entries(ST.inv).filter(([k, n]) => n > 0 && GD(k) && !GD(k).nosell),")
# đổi, dời đồ trang trí: bỏ mô hình cũ khỏi bộ nhớ đồ họa
rep("function dcTick(){ const D = ST.dc;","function dcDrop(g, par = S){ if (!g) return; par.remove(g); g.traverse(o => { if (o.isMesh && o.geometry) o.geometry.dispose(); }); }\nfunction dcTick(){ const D = ST.dc;")
rep("if (DCV.ga) S.remove(DCV.ga); DCV.ga = null;","dcDrop(DCV.ga); DCV.ga = null;")
rep("if (DCV.vit) VITV.root.remove(DCV.vit); DCV.vit = null;","dcDrop(DCV.vit, VITV.root); DCV.vit = null;")
rep("if (DCV.rao) S.remove(DCV.rao); DCV.rao = null;","dcDrop(DCV.rao); DCV.rao = null;")
rep("for (const g of DCV.items.values()) S.remove(g); DCV.items.clear();","for (const g of DCV.items.values()) dcDrop(g); DCV.items.clear();")
# việc Cho ăn, Lượm trứng: chuồng đã sửa thì dẫn tới máng, tới ổ, không mở bảng sửa chuồng
rep("function penGo(k){ const c = PENS[k].at(); camTo(new T.Vector3(c.x, .3, c.z), Math.max(cam.zoom, DEFZ() * 1.1)); setTimeout(() => penRing(k), 500); }","function penGo(k, spot){ const c = PENS[k].at(), fixed = !!PENS[k].st().fixed, p = spot || c; camTo(new T.Vector3(p.x, .3, p.z), Math.max(cam.zoom, DEFZ() * 1.1)); setTimeout(() => { if (!fixed) penRing(k); else pingAt(p.x, p.z); }, 500); }")
rep("else if (t === 'feed' || t === 'egg'){ try { penGo(vitOn() ? 'vit' : 'ga'); } catch (e) {} return; }","else if (t === 'feed' || t === 'egg'){ try { const useGa = gaOn() && (!vitOn() || t === 'feed' || ST.ga.eggs > 0); if (useGa) penGo('ga', t === 'feed' ? FEEDP : NEST); else penGo(vitOn() ? 'vit' : 'ga'); } catch (e) {} return; }")
rep("x.t === 'feed' ? (ICON.lucbinh || ICON.bap)","x.t === 'feed' ? (ICON.bap || ICON.lucbinh)")
# trang không được trôi, không được phóng to: HUD luôn nằm đúng chỗ
rep("html,body{height:100%}","html,body{height:100%;width:100%;position:fixed;inset:0;overflow:hidden;overscroll-behavior:none;-webkit-text-size-adjust:100%;text-size-adjust:100%}")
rep("async function cloudRestore(txt, opt = {}){","{ const reset = () => { if (window.scrollX || window.scrollY) window.scrollTo(0, 0); }; addEventListener('scroll', reset, { passive: true }); addEventListener('orientationchange', () => setTimeout(reset, 300)); if (window.visualViewport) visualViewport.addEventListener('resize', reset); for (const n of ['gesturestart', 'gesturechange']) addEventListener(n, e => e.preventDefault(), { passive: false }); let lastT = 0; addEventListener('touchend', e => { const n = Date.now(); if (n - lastT < 320 && !e.target.closest('input,textarea')) e.preventDefault(); lastT = n; }, { passive: false }); }\nasync function cloudRestore(txt, opt = {}){")
rep('en=!/^vi/i.test(navigator.language||"vi");try{','en=false;try{en=localStorage.getItem("mv2-lang")==="en";')
# đồng hồ hẹn giờ chạy lúc đang tải có thể đụng BOOK chưa khai báo
rep("const bkov = $('#book'), bkEl = $('#bk'); let BOOK = null;","const bkov = $('#book'), bkEl = $('#bk'); BOOK = null;")
rep("let LDT = performance.now(); const LDY =","let BOOK = null; let LDT = performance.now(); const LDY =")
# điện thoại xoay ngang: thẻ Ngoại nhờ lên cạnh đồng hồ, khỏi che Mua hạt, Tưới
rep("</style>","@media (min-width:600px) and (max-height:520px){.nxq{left:calc(env(safe-area-inset-left,0px) + 340px)!important;right:auto!important;top:calc(env(safe-area-inset-top,0px) + 8px)!important;bottom:auto!important;width:230px!important;max-width:230px!important}}\n</style>",1) if False else None
i=s.rindex("</style>"); s=s[:i]+"@media (min-width:600px) and (max-height:520px){.nxq{left:calc(env(safe-area-inset-left,0px) + 340px)!important;right:auto!important;top:calc(env(safe-area-inset-top,0px) + 8px)!important;bottom:auto!important;width:230px!important;max-width:230px!important}}\n"+s[i:]
rep("get: () => ({ openSheet,","get: () => ({ cloudInbox, act, openSheet,")
open(dst,'w',encoding='utf-8').write(s); print('ok',len(s))
