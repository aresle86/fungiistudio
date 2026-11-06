# chau115: vẽ lại chậu cúc, chậu mai. python3 chau115.py live/v115_1.html live/v115_1b.html
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
i=s.index("  icon('cuc', p =>"); j=s.index("  icon('lixi', p =>",i)
s=s[:i]+open('chau115_ic.js',encoding='utf-8').read()+s[j:]
i=s.index("const maiTree = (x, z, s = 1, p = root) =>"); j=s.index("  const st = G(0, 0, 0, 0, root); ROOT = st; maiTree(",i)
s=s[:i]+open('chau115_tree.js',encoding='utf-8').read()+s[j:]
open(dst,'w',encoding='utf-8').write(s)
