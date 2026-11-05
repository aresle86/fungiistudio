# ao114: chèn mô hình ba bậc ao và đồ trang trí ao vào bản thử (chưa vào game). python3 ao114.py live/v113t.html live/ao114.html
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
a="  return {\n  bu_nhin_do(){"
assert s.count(a)==1
s=s.replace(a,"  return {\n"+open('ao114_models.js',encoding='utf-8').read()+"  bu_nhin_do(){")
a='window.__DCX0 = {'
assert s.count(a)==1
s=s.replace(a,'window.__SC = S; window.__R = r; '+a)
open(dst,'w',encoding='utf-8').write(s); print('ok',len(s))
