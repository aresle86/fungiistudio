# rad114: radio trong chòi. Tự đọc hd/nhac: giut_*, cailuong_*, chieu_*, tin_*. Không có file thì không hiện radio. python3 rad114.py live/v114d.html live/v114e.html [thư mục nhạc]
import sys,json,os,glob
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
dr=sys.argv[3] if len(sys.argv)>3 else 'nhac'
def fs(pre): return sorted(os.path.basename(f) for f in glob.glob(os.path.join(dr,pre+'_*')))
R={'dir':'nhac/','dai':{'giut':{'name':'Nhạc giựt','files':fs('giut')},'cailuong':{'name':'Cải lương','files':fs('cailuong')},'chieu':{'name':'Chiều vườn','files':fs('chieu')}},'tin':fs('tin')}
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
rep("const BUILD = 'v114d'","const BUILD = 'v114e'")
JS=open('rad114.js',encoding='utf-8').read().replace('__RADIO__',json.dumps(R,ensure_ascii=False))

rep("function VOL(){",JS+"function VOL(){")
rep("if (VOL().mus > 0 && now >= MUSN){","if (VOL().mus > 0 && !RAD.on && now >= MUSN){")
rep("if (ST.dc.items[di].k === 'mieu' && diaCall()) return; openSheet('deco', di); return;","if (ST.dc.items[di].k === 'mieu' && diaCall()) return; if (ST.dc.items[di].k === 'choi_la' && radOn() && !SUA && !VISIT){ sfx('pick'); openSheet('radio', di); return; } openSheet('deco', di); return;")
rep("if (kind === 'big'){ shT.textContent = BIGD[arg].title; h += bigHTML(arg); }","if (kind === 'radio'){ shT.textContent = 'Radio'; h += radHTML(); } if (kind === 'big'){ shT.textContent = BIGD[arg].title; h += bigHTML(arg); }")
rep("else if (a === 'aotha'){ aoTha(b.dataset.k); return; }","else if (a === 'radon'){ radStart(b.dataset.k); renderSheet(); return; } else if (a === 'radde'){ openSheet('deco', radItem()); return; } else if (a === 'radoff'){ radStop(); renderSheet(); return; } else if (a === 'radtin'){ ST.radTin = ST.radTin === false; save(); renderSheet(); return; } else if (a === 'aotha'){ aoTha(b.dataset.k); return; }")
rep("tk('ao', () => aoTick(t));","tk('ao', () => aoTick(t)); tk('rad', () => radTick(t));")
rep("get: () => ({ gheTaskFix,","get: () => ({ RAD, RADIO, gheTaskFix,")
open(dst,'w',encoding='utf-8').write(s); print('ok',len(s),{k:len(v['files']) for k,v in R['dai'].items()},len(R['tin']))
