p='live/vuon3d.html';s=open(p,encoding='utf8').read()
def rep(a,b,cnt=1):
    global s
    n=s.count(a); assert n==cnt,(n,a[:90]); s=s.replace(a,b)
rep('<button class="bt ctr" id="bCtr" aria-label="Về giữa vườn"><img id="icCtr" alt=""><span class="tg">Về giữa</span></button>',
'<button class="bt ctr" id="bCtr" aria-label="Về giữa vườn"><img id="icCtr" alt=""><span class="tg">Về giữa</span></button><button class="bt ctr" id="bSua" aria-label="Sửa vườn" hidden><img id="icSua" alt=""><span class="tg">Sửa vườn</span></button><div class="card vbar sbar" id="suaBar" hidden><div><b>Sửa vườn</b><span id="suaTx"></span></div><button class="btn g" id="suaOk">Xong</button></div>')
rep("#bCtr{right:max(16px,env(safe-area-inset-right,0px));width:72px}",
"#bCtr{right:max(16px,env(safe-area-inset-right,0px));width:72px}\n#bSua{right:max(16px,env(safe-area-inset-right,0px));width:72px;bottom:auto!important}body.sua #bSua{box-shadow:0 0 0 3px #F5D27A,0 4px 0 #4A2F1E!important}\n.vbar.sbar{top:auto;bottom:calc(104px + env(safe-area-inset-bottom,0px))}body.sua .tray,body.sua #fan{visibility:hidden}\n@media (max-width:560px){ .vbar.sbar{top:auto!important;bottom:calc(104px + env(safe-area-inset-bottom,0px))!important} }")
# đặt nút Sửa vườn ngay dưới nút Về giữa
rep("function placeCtr(){ const c = VISIT ? document.querySelector('.vbar') : document.querySelector('.top .coin'), b = $('#bCtr'); if (!c || !b) return; const r = c.getBoundingClientRect(); b.style.top = Math.round(r.bottom + 12) + 'px'; }",
"function placeCtr(){ const c = VISIT ? document.querySelector('.vbar') : document.querySelector('.top .coin'), b = $('#bCtr'); if (!c || !b) return; const r = c.getBoundingClientRect(); b.style.top = Math.round(r.bottom + 12) + 'px'; placeSua(); }\nfunction placeSua(){ const b = $('#bCtr'), s2 = $('#bSua'); if (!b || !s2) return; s2.hidden = !!VISIT || !baiOn(); if (s2.hidden) return; const r = b.getBoundingClientRect(); s2.style.top = Math.round(r.bottom + 10) + 'px'; }\n$('#bSua').addEventListener('click', () => { suaOn(!SUA); }); $('#suaOk').addEventListener('click', () => { suaOn(false); });")
rep("$('#icCtr').src = UIC.center;","$('#icCtr').src = UIC.center; try { $('#icSua').src = ICON.cuoc; } catch (e) {}")
# icon
a="  icon('trungvit', p => {"
assert s.count(a)==1
s=s.replace(a,"""  icon('cuoc', p => { add(p, new T.CylinderGeometry(.032, .038, .95, 6), '#B48560', -.05, -.05, 0, [0, 0, .75]); add(p, new T.CylinderGeometry(.05, .05, .1, 6), '#6B4529', .27, .27, 0, [0, 0, .75]); add(p, new T.BoxGeometry(.36, .06, .26), '#8C8F94', .36, .16, 0, [0, 0, -.55]); add(p, new T.BoxGeometry(.36, .02, .27), '#C9CDD2', .37, .19, 0, [0, 0, -.55]); }, V(.2, .3, 1));
  icon('nong', p => { add(p, new T.CylinderGeometry(.48, .45, .05, 16), '#C9A66B', 0, 0, 0); add(p, new T.TorusGeometry(.48, .035, 4, 18), '#A07A45', 0, .03, 0, [Math.PI / 2, 0, 0]); for (const r of [.17, .32]) add(p, new T.TorusGeometry(r, .012, 3, 16), '#B48C55', 0, .028, 0, [Math.PI / 2, 0, 0]); for (let k = 0; k < 16; k++){ const a = k * 2.4, r = Math.sqrt((k + .5) / 16) * .3; add(p, new T.CapsuleGeometry(.03, .1, 2, 6), k % 3 ? '#E0402A' : '#C2301E', Math.cos(a) * r, .06, Math.sin(a) * r, [Math.PI / 2, a, 0]); } }, V(.3, 1, .9));
  icon('otkho', p => { add(p, new T.BoxGeometry(.42, .5, .22), '#E3D3B0', 0, -.04, 0); add(p, new T.BoxGeometry(.44, .06, .24), '#C9B27A', 0, .22, 0); add(p, new T.BoxGeometry(.3, .16, .01), '#F5ECD6', 0, -.05, .115); for (let k = 0; k < 6; k++) add(p, new T.CapsuleGeometry(.028, .12, 2, 6), k % 2 ? '#8E2A1C' : '#A8321E', -.15 + k * .06, .3 + (k % 2) * .03, R(-.05, .05), [0, 0, R(-.6, .6)]); }, V(.3, .3, 1));
  icon('chuoiphoi', p => { add(p, new T.CylinderGeometry(.008, .008, .9, 4), '#B48560', 0, .05, 0, [0, 0, Math.PI / 2]); for (let k = 0; k < 4; k++){ const x = -.3 + k * .2; blob(p, .1, k % 2 ? '#8A5A2E' : '#9A6A36', x, -.12, 0, [.55, 1.7, .32]); add(p, new T.CylinderGeometry(.006, .006, .12, 3), '#C9B27A', x, .0, 0); } }, V(.1, .2, 1));
  icon('lucbinhkho', p => { for (let k = 0; k < 9; k++) add(p, new T.CylinderGeometry(.018, .018, .8, 4), pick(['#B8A070', '#A89060', '#C9B27A']), (k % 3 - 1) * .04, 0, Math.floor(k / 3) * .04 - .04, [0, 0, .9 + R(-.08, .08)]); add(p, new T.TorusGeometry(.08, .02, 4, 10), '#6E9F57', 0, 0, 0, [0, Math.PI / 2, .9]); }, V(.2, .4, 1));
"""+a)
open(p,'w',encoding='utf8').write(s); print('ok')
