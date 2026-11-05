# sv114: sao lưu vườn trên máy, lấy lại bản cũ, hỏi trước khi bản cũ hơn ghi đè. python3 sv114.py live/v113w.html live/v114a.html
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
rep("const BUILD = 'v113w'","const BUILD = 'v114a'")
BAK=open('sv114.js',encoding='utf-8').read()
rep("async function cloudRestore(txt){",BAK+"async function cloudRestore(txt, opt = {}){")
rep("throw new Error('Vườn này chưa có gì để chuyển');\n  localStorage.setItem('mv2-state',","throw new Error('Vườn này chưa có gì để chuyển');\n  if (!opt.ok && pullWorse(r.data)) return pullAsk(r, cred); CLOUD.ask = null; BAK.take('Trước khi tải từ mạng');\n  localStorage.setItem('mv2-state',")
rep("let h = `<div class=\"sub\">Vườn online</div>`; if (c && CLOUD.stale)","let h = askHTML() + `<div class=\"sub\">Vườn online</div>`; if (c && CLOUD.stale && !CLOUD.ask)")
rep("data-a=\"cldres\">Khôi phục vườn từ máy khác</button></div>`;\n  return h; }","data-a=\"cldres\">Khôi phục vườn từ máy khác</button></div>`;\n  return h + bakHTML(); }")
rep("'cldsave'){ cloudSave(true); } else if (a === 'cldpull'){","'cldsave'){ cloudSave(true); } else if (a === 'bakopen'){ SHEET.bakOpen = !SHEET.bakOpen; SHEET.bakI = null; } else if (a === 'bakpick'){ SHEET.bakI = +b.dataset.i; bakScroll('bakgo'); } else if (a === 'bakno'){ SHEET.bakI = null; } else if (a === 'bakgo'){ bakRestore(+b.dataset.i); return; } else if (a === 'bakkeep'){ pullKeep(); } else if (a === 'bakpull'){ const A = CLOUD.ask; if (A) cloudRestore(RCODE(A.cred), { ok: 1 }).catch(e => { SHEET.rerr = String(e && e.message || e); renderSheet(); }); return; } else if (a === 'cldpull'){")
rep("get: () => ({ cauCap,","get: () => ({ BAK, CLOUD, cloudRestore, pullAsk, cauCap,")
open(dst,'w',encoding='utf-8').write(s); print('ok',len(s))
