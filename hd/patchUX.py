import re
p='live/vuon3d.html';s=open(p,encoding='utf8').read()
def cut_func(name):
    global s
    i=s.index('function '+name+'(')
    # find end: function ends at line containing 'return h; }' after start
    j=s.index('return h; }',i)+len('return h; }')
    s=s[:i]+s[j:]
cut_func('vitHTML'); cut_func('nongHTML')
def rep(a,b,cnt=1):
    global s
    n=s.count(a); assert n==cnt,(n,a[:100]); s=s.replace(a,b)
# ga sheet
i=s.index("  if (kind === 'ga'){ const g = ST.ga, cap = gaCap()")
j=s.index("  if (kind === 'bep'){",i)
s=s[:i]+"  if (kind === 'ga'){ shT.textContent = 'Chuồng gà'; h += gaHTML(); }\n"+s[j:]
# plot sheet body
i=s.index("    if (c){ const left = (c.grow - p.g) / (p.mulch > ST.gt ? 1.08 : 1) / fastK(p);")
j=s.index("  if (kind === 'kho'){",i)
s=s[:i]+"    h += plotHTML(P, p, arg); }\n"+s[j:]
# actions
rep("  else if (a === 'nput'){ nong.put(+b.dataset.n, b.dataset.k); }","  else if (a === 'nput'){ nong.put(+b.dataset.n, b.dataset.k); SHEET.pick = null; } else if (a === 'npick'){ SHEET.pick = +b.dataset.n; } else if (a === 'pickback'){ SHEET.pick = null; } else if (a === 'ntakeall'){ nong.takeAll(); } else if (a === 'noop'){ }")
# ux kit vào trước đơn hàng
a="/* ===== đơn hàng nhà bên:"
assert s.count(a)==1
s=s.replace(a,open('ux_js.js',encoding='utf8').read()+'\n'+a)
# css
a="\n.vbar.sbar{"
assert s.count(a)==1
s=s.replace(a,"\n"+open('ux_css.txt',encoding='utf8').read()+".vbar.sbar{")
# icons gà vịt
a="  icon('trungvit', p => {"
s=s.replace(a,"""  const bird = (p, body, wing, head, comb, s2 = 1) => { blob(p, .26 * s2, body, -.02, -.08, 0, [1.25, 1, 1]); blob(p, .16 * s2, wing, -.06, -.04, .16 * s2, [1.3, .7, .4]); blob(p, .14 * s2, head, .22 * s2, .16 * s2, 0); add(p, new T.ConeGeometry(.045, .1, 4), '#F2B23A', .37 * s2, .14 * s2, 0, [0, 0, -Math.PI / 2]); add(p, new T.SphereGeometry(.022, 5, 4), '#1a1a1a', .28 * s2, .21 * s2, .1); if (comb) for (let k = 0; k < 3; k++) blob(p, .05, comb, .16 * s2 + k * .05, .3 * s2 + (k % 2) * .02, 0); };
  icon('mai', p => { bird(p, '#C98A45', '#A86A35', '#C98A45', '#E8453A'); add(p, new T.ConeGeometry(.08, .18, 4), '#8A5530', -.3, .05, 0, [0, 0, Math.PI / 2.4]); }, V(.15, .25, 1));
  icon('trong', p => { bird(p, '#B5452A', '#2F5A3A', '#D9822E', '#E8253A', 1.05); for (let k = 0; k < 3; k++) add(p, new T.ConeGeometry(.05, .34, 4), ['#2F5A3A', '#1F3F2A', '#4A2F1E'][k], -.32, .14 + k * .05, (k - 1) * .05, [0, 0, Math.PI / 2.6 + k * .2]); }, V(.15, .25, 1));
  icon('vitmai', p => { bird(p, '#F7F3EA', '#E3DCCB', '#F7F3EA', null); add(p, new T.BoxGeometry(.14, .035, .08), '#F2A23A', .37, .13, 0); }, V(.15, .25, 1));
"""+a,1)
open(p,'w',encoding='utf8').write(s); print('ok')
