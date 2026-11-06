# load115: màn tải bền hơn, chuyển http sang https. python3 load115.py live/v115_1.html live/v115_2.html
import re,sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
# http: chuyển sang https, mang theo vườn
assert s.startswith('<title>')
s=open('load115_head.html',encoding='utf-8').read()+s
# màn tải: tự tải lại một lần khi kẹt, có nút Tải lại
i=s.index('/* Theo dõi lúc mở:'); j=s.index('</script>',i)
s=s[:i]+open('load115_watch.js',encoding='utf-8').read()+s[j:]
# vẽ biểu tượng: dùng chung một bộ vẽ thay vì mười mấy cái lúc mở game; lỗi một hình không làm chết cả game
NEW="new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true })"
keep="aoIc.ri = "+NEW
assert s.count(keep)==1
s=s.replace(keep,"aoIc.ri = @@AO@@")
print('bộ vẽ đổi',s.count(NEW))
s=s.replace(NEW,"ICR()").replace("@@AO@@",NEW)
n0=s.count("ri.dispose(); ri.forceContextLoss();")
s=s.replace("ri.dispose(); ri.forceContextLoss();","ri.renderLists.dispose();")
rep("ri.dispose(); return OUT; };","ri.renderLists.dispose(); return OUT; };")
print('chỗ trả bộ vẽ',n0)
rep("function toonRender(ri, sc, cm){ toonify(sc);","const ICR = () => { let R = ICR.r; if (!R || R.getContext().isContextLost()){ R = ICR.r = new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true }); } R.setRenderTarget(null); R.setPixelRatio(1); R.setClearColor(0, 0); R.toneMapping = T.NoToneMapping; R.toneMappingExposure = 1; R.shadowMap.enabled = false; return R; };\nICR.free = () => { const R = ICR.r; ICR.r = null; if (R){ R.dispose(); R.forceContextLoss(); } };\nfunction toonRender(ri, sc, cm){ try { toonRender0(ri, sc, cm); } catch (e) { console.warn('toon', e); try { TOONLAST = ri.domElement.toDataURL('image/png'); } catch (e2) { TOONLAST = 'data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='; } } }\nfunction toonRender0(ri, sc, cm){ toonify(sc);")
rep("window.__ready = true","window.__ready = true; try { ICR.free(); } catch (e) {}")
open(dst,'w',encoding='utf-8').write(s)
