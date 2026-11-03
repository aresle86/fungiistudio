import mkboards as MB
B=MB.B; B.update({'coin':'01eafef7c0f7f05fbae74e95bea6f8a8','clock':'8edef4f3df8acc302702564a9f552b8a','sprout':'84ad9615c261f44eb9729d2dd3dd4764','yield':'5c64e0c5e1b26964d3fdcabf7b13807f','drop':'122ca5e0932d772002f13c1f26634eca','seedbag':'d9b83d86587f442227bbba3498f9933d','task':'07bfbd8297d7d91625509d7e881b9294','lu':'ff7c8ad2969f1d681bf32bc529b2c58f'})
C4={'s': {'cai': '2054bf7292b9ffcd61159c27fb3f257e', 'hanh': 'cd3d1ca9306316e6d2338b7627b29f8a', 'ot': '3c1dc7ffd512d68bd3d31f22b47391f1', 'bap': '7a62a3b11f9b7009f44fd213eeea1545', 'cachua': '8363481f05c789b22513e4ad69ead4ae', 'khoqua': '8a86783f1b06b0bf8ee5f5e17ce3d9de'}, 'f': {'cai': '9ffe7781c356a2eb448594c08d6af72d', 'hanh': '750ef7ab71450ed4d1dcda478b0f1684', 'ot': '36580649ae479da38b4ff46fe0c11598', 'bap': '5c6c49cb56e133d9b9890c8de61f571d', 'cachua': 'ad64311c713c4c2322a9d96a2717d960', 'khoqua': 'fba92e71f98c3abb3024ecd58b0d7046'}}
C5={'cai': 'b7b858e23f072bf1d0efeeb397591036', 'hanh': '72661a9038c17f5d08a0f9f7df078e44', 'ot': '757b8a3362cbfbe559167bf971091758', 'bap': '93324be6452aab513d8478da02ffc733', 'cachua': '0d6b42e41ff7d278d11baa6f534933aa', 'khoqua': 'bd982cb2e17762c5c9688cd86fff9741'}
UI={'coin','clock','sprout','yield','drop','seedbag','task','lu'}
def img(k,L):
  if k.startswith('F:'):
    k=k[2:]; return ('board/c4f_'+k+'.png') if L else '/_blob/'+C4['f'][k]
  if k in C5: return ('board/c5_'+k+'.png') if L else '/_blob/'+C5[k]
  if not L: return '/_blob/'+B[k]
  if k in UI: return 'board/ui_'+k+'.png'
  return MB.img(k,True)
OUT=lambda c,w=2.5: ','.join(f'{x}px {y}px 0 {c}' for x,y in [(w,0),(-w,0),(0,w),(0,-w),(w*.7,w*.7),(-w*.7,w*.7),(w*.7,-w*.7),(-w*.7,-w*.7)])
CSS=r'''
.paper{position:relative;background:#FBF7EE;box-sizing:border-box;padding:28px 30px}
.paper.l{border-radius:16px 4px 4px 16px;box-shadow:inset -20px 0 24px -20px rgba(74,47,30,.35)}
.paper.r{border-radius:4px 16px 16px 4px;box-shadow:inset 20px 0 24px -20px rgba(74,47,30,.35)}
.stitch{position:absolute;left:50%;top:22px;bottom:22px;width:0;border-left:3px dashed #D2A57E;margin-left:-1.5px;z-index:3}
.vtabs{position:absolute;right:-118px;top:46px;display:flex;flex-direction:column;gap:12px;align-items:flex-start;z-index:0}
.vt{display:flex;flex-direction:column;align-items:center;justify-content:center;border-radius:0 22px 22px 0;box-shadow:inset 0 -6px 0 rgba(0,0,0,.16);padding-left:16px;box-sizing:border-box}
.vt img{display:block;filter:brightness(1.12) drop-shadow(2px 0 0 #fff) drop-shadow(-2px 0 0 #fff) drop-shadow(0 2px 0 #fff) drop-shadow(0 -2px 0 #fff)}
.vt span{font-family:"Paytone One";color:#FBF7EE;line-height:1.05;text-align:center}
.vt.on{width:150px;height:150px}.vt.on img{width:78px;height:78px}.vt.on span{font-size:20px}
.vt.off{width:112px;height:112px}.vt.off img{width:54px;height:54px}.vt.off span{font-size:14px}
.hd{display:inline-flex;align-items:center;gap:10px;padding:6px 22px 6px 8px;border-radius:999px;box-shadow:inset 0 -5px 0 rgba(0,0,0,.15)}
.hd img{width:52px;height:52px;margin:-12px 0;filter:brightness(1.12) drop-shadow(2px 0 0 #fff) drop-shadow(-2px 0 0 #fff) drop-shadow(0 2px 0 #fff) drop-shadow(0 -2px 0 #fff)}
.hd b{font-family:"Paytone One";font-weight:400;font-size:28px;color:#FBF7EE}
.stk{text-align:center}
.stk .pic{height:168px;display:flex;align-items:flex-end;justify-content:center}
.stk .pic img{width:162px;height:162px;filter:drop-shadow(3.5px 0 0 #fff) drop-shadow(-3.5px 0 0 #fff) drop-shadow(0 3.5px 0 #fff) drop-shadow(0 -3.5px 0 #fff) drop-shadow(0 3px 1.2px rgba(74,47,30,.3))}
.stk.lock .pic img{filter:brightness(0) invert(.82) sepia(.25) drop-shadow(3px 0 0 #fff) drop-shadow(-3px 0 0 #fff) drop-shadow(0 3px 0 #fff) drop-shadow(0 -3px 0 #fff) drop-shadow(0 3px 1.2px rgba(74,47,30,.2))}
.stk b{display:block;font-family:"Paytone One";font-weight:400;font-size:18px;color:#6B4529;margin-top:4px}
.stk.sel .pic{background:radial-gradient(closest-side,#F6E3C4,transparent)}
.stats{display:flex;justify-content:center;gap:8px;margin-top:4px}
.st{display:inline-flex;align-items:center;gap:2px;vertical-align:middle;font-family:"Paytone One";font-size:16px;color:#4A2F1E}
.st img{width:26px;height:26px}
.lockb{display:inline-block;margin-top:4px;font-family:"Paytone One";font-size:13px;color:#FBF7EE;background:#B48560;border-radius:9px;padding:2px 10px}
.big .st{font-size:24px;gap:4px}.big .st img{width:44px;height:44px}
.chip{display:inline-flex;align-items:center;gap:4px;font-family:"Paytone One";font-size:15px;color:#4A2F1E;background:#E8DFCC;border-radius:12px;padding:3px 12px 3px 4px}
.chip img{width:30px;height:30px}
.row{display:grid;grid-template-columns:62px 1fr 64px;align-items:center;padding:6px 4px;border-bottom:2px dashed #E3D3BC}
.row img{width:56px;height:56px}
.row .n{font-family:"Paytone One";font-size:19px;color:#4A2F1E}
.row .q{font-family:"Paytone One";font-size:26px;color:#C24A2E;text-align:right;font-variant-numeric:tabular-nums}
.htab{position:absolute;bottom:calc(100% - 14px);right:18px;display:flex;gap:8px;align-items:flex-end;z-index:1}
.ht{border-radius:16px 16px 0 0;display:flex;align-items:center;justify-content:center;gap:6px;box-shadow:inset 0 -4px 0 rgba(0,0,0,.14)}
.ht.off{width:58px;height:52px;padding-bottom:12px;box-sizing:border-box}.ht.off img{width:38px;height:38px}
.ht.on{height:68px;padding:0 14px 12px 8px;box-sizing:border-box}.ht img{filter:brightness(1.12) drop-shadow(2px 0 0 #fff) drop-shadow(-2px 0 0 #fff) drop-shadow(0 2px 0 #fff) drop-shadow(0 -2px 0 #fff)}.ht.on img{width:48px;height:48px}.ht.on span{font-family:"Paytone One";font-size:16px;color:#FBF7EE}
.tk{display:grid;grid-template-columns:34px 1fr auto;gap:10px;align-items:center;margin-bottom:10px;font-family:"Patrick Hand";font-size:22px;color:#2B3446;line-height:1.15}
.tk .box{width:26px;height:26px;border:3px solid #6B4529;border-radius:7px;position:relative;margin:0}
.tk.done .box{background:#86B06A;border-color:#6E9F57}
.tk.done .box:after{content:"";position:absolute;left:6px;top:0;width:8px;height:15px;border:solid #FBF7EE;border-width:0 4px 4px 0;transform:rotate(40deg)}
.tk.done .tx{color:#9a8a7a;text-decoration:line-through;text-decoration-color:#C24A2E;text-decoration-thickness:3px}
'''
GREEN,YEL,COR='#86B06A','#EDB940','#F08A6E'
def so(L):
  I=lambda k: img(k,L)
  st=lambda k,v: f'<span class="st"><img src="{I(k)}" alt="">{v}</span>'
  seeds=[('cai','Cải xanh',12,'30p',6,True,False),('hanh','Hành lá',10,'45p',8,False,False),('ot','Ớt',20,'3h',10,False,False),('bap','Bắp',30,'4h',8,False,False),('cachua','Cà chua',28,'4h',12,False,False),('khoqua','Khổ qua',24,'3h',8,False,True)]
  stk=''.join(f'<div class="stk{" sel" if s else ""}{" lock" if lk else ""}"><div class="pic"><img src="{I(k)}" alt=""></div><b>{n if not lk else "???"}</b>'+(f'<span class="lockb">Mở ở cấp 3</span>' if lk else f'<div class="stats">{st("coin",p)}{st("clock",t)}{st("yield",y)}</div>')+'</div>' for k,n,p,t,y,s,lk in seeds)
  tabsV=f'''<div class="vtabs"><div class="vt on" style="background:{GREEN}"><img src="{I('seedbag')}" alt=""><span style="text-shadow:{OUT('#4F7D44',2)}">Sổ giống</span></div><div class="vt off" style="background:{YEL}"><img src="{I('lu')}" alt=""><span style="text-shadow:{OUT('#C9952A',1.6)}">Kho</span></div><div class="vt off" style="background:{COR}"><img src="{I('task')}" alt=""><span style="text-shadow:{OUT('#C24A2E',1.6)}">Việc của<br>Ngoại</span></div></div>'''
  hd=lambda k,t,c,dc: f'<div class="hd" style="background:{c}"><img src="{I(k)}" alt=""><b style="text-shadow:{OUT(dc,2.2)},0 3px 0 {dc}">{t}</b></div>'
  spread=f'''<div style="position:relative;margin:30px 0 0 16px;width:1240px;height:740px">
<div class="cover"></div>{tabsV}
<div class="book" style="height:740px">
<div class="paper l" style="width:620px;height:740px">{hd('seedbag','Sổ giống',GREEN,'#4F7D44')}<div class="hn" style="margin:8px 0 0;font-size:21px">Chọn hạt, kéo thả xuống liếp là gieo.</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px 6px;margin-top:4px">{stk}</div>
<div style="display:flex;gap:16px;justify-content:center;margin-top:12px;font-family:Patrick Hand;font-size:19px;color:#6B4529">{st('coin','giá hạt')}{st('clock','thời gian lớn')}{st('yield','thu được')}</div></div>
<div class="paper r" style="width:620px;height:740px"><div style="display:flex;gap:22px;align-items:center"><div class="stk" style="width:190px"><div class="pic" style="height:180px;background:radial-gradient(closest-side,#F6E3C4,transparent)"><img src="{I('cai')}" style="width:170px;height:170px" alt=""></div></div><div><div class="ph" style="margin:0 0 6px;font-size:34px">Cải xanh</div><div style="display:flex;gap:8px;flex-wrap:wrap"><span class="chip"><img src="{I('sprout')}" alt="">Trồng liếp</span><span class="chip"><img src="{I('drop')}" alt="">Ưa ẩm</span></div></div></div>
<div class="big" style="display:flex;justify-content:space-around;margin:20px 0 8px;padding:12px 0;background:#F3EADB;border-radius:18px">{st('coin','12')}{st('clock','30p')}{st('yield','6')}</div>
<div class="hn" style="margin-top:14px;font-size:22px;line-height:1.45">Ngoại dặn:<br>· Tưới sáng sớm với chiều mát, trưa nắng đừng tưới.<br>· Phủ rơm lên liếp giữ ẩm, đỡ phải tưới.<br>· Rải dày được, cải mọc sát nhau không sao.</div>
<div style="display:flex;gap:12px;margin-top:22px;align-items:center"><span class="chip" style="font-size:18px;padding:6px 14px 6px 6px"><img src="{I('seedbag')}" alt="">Có 3 bao</span><span class="btn g">Mua 1 bao · 12 xu</span></div>
<img src="{I('dan')}" style="position:absolute;right:-6px;bottom:0;width:160px" alt=""></div>
<div class="stitch"></div></div>
<div class="label" style="border-color:#6E9F57"><div class="hand" style="font-size:26px;color:#2B3446;line-height:1">Sổ vườn của Ngoại</div></div>
</div>'''
  htab=lambda on: '<div class="htab">'+''.join((f'<div class="ht on" style="background:{c}"><img src="{I(k)}" alt=""><span style="text-shadow:{OUT(dc,1.6)}">{t}</span></div>' if k==on else f'<div class="ht off" style="background:{c}"><img src="{I(k)}" alt=""></div>') for k,t,c,dc in [('seedbag','Sổ giống',GREEN,'#4F7D44'),('lu','Kho',YEL,'#C9952A'),('task','Việc',COR,'#C24A2E')])+'</div>'
  kho_items=[('cai','Cải xanh',12),('cachua','Cà chua',7),('ot','Ớt',4),('bap','Bắp',15),('rom','Rơm',3)]
  rows=''.join(f'<div class="row"><img src="{I(k)}" alt=""><span class="n">{n}</span><span class="q">{q}</span></div>' for k,n,q in kho_items)
  frame=lambda inner,tab: f'''<div class="phone"><div class="scr"><div style="position:absolute;inset:0;background:rgba(74,47,30,.25)"></div><div style="position:absolute;left:14px;right:14px;top:84px;bottom:24px"><div class="paper" style="z-index:2;height:100%;border-radius:22px;padding:22px 20px;box-shadow:0 8px 0 #8A5D3B, inset 0 0 0 3px #B48560">{inner}</div>{htab(tab)}</div></div></div>'''
  phone1=frame(f'''{hd('lu','Kho',YEL,'#C9952A')}<div style="margin-top:14px">{rows}</div>
<div style="margin-top:16px;display:flex;align-items:center;gap:8px"><img src="{I('lu')}" style="width:40px" alt=""><span style="font-family:Paytone One;font-size:16px;color:#6B4529">Sức chứa</span><span style="margin-left:auto;font-family:Paytone One;font-size:18px;color:#4A2F1E">41 / 60</span></div>
<div style="height:16px;border-radius:8px;background:#E8DFCC;box-shadow:inset 0 0 0 2px #D2A57E;margin:6px 0 18px"><div style="width:68%;height:100%;border-radius:8px;background:{YEL}"></div></div>
<div style="display:flex;gap:10px;flex-wrap:wrap"><span class="btn g">Đem ra chợ</span><span class="btn">Thêm lu · 50 xu</span></div>''','lu')
  tasks=[('Tưới liếp cải buổi sáng',True,'coin','5'),('Phủ rơm cho luống ớt',True,'rom','1'),('Hái 10 trái cà chua',False,'coin','12'),('Bán 5 bó cải cho cô Ba',False,'coin','8'),('Cho gà ăn lúa',False,'coin','3')]
  tk=''.join(f'<div class="tk{" done" if d else ""}"><div class="box"></div><span class="tx">{t}</span><span class="chip" style="padding:2px 10px 2px 2px"><img src="{I(k)}" style="width:28px;height:28px" alt="">+{v}</span></div>' for t,d,k,v in tasks)
  phone2=frame(f'''{hd('task','Việc của Ngoại',COR,'#C24A2E')}<div class="hn" style="font-size:19px;margin:10px 0 12px">Hôm nay · thứ Tư · xong 2/5</div>{tk}
<div style="margin-top:14px;background:#F3EADB;border-radius:16px;padding:10px 12px;display:flex;align-items:center;gap:10px"><img src="{I('khoqua')}" style="width:56px;filter:drop-shadow(2px 0 0 #fff) drop-shadow(-2px 0 0 #fff) drop-shadow(0 2px 0 #fff) drop-shadow(0 -2px 0 #fff)" alt=""><span class="hn" style="font-size:19px;line-height:1.2">Xong hết: Ngoại tặng 1 bao hạt khổ qua</span></div>
<img src="{I('vui')}" style="position:absolute;right:-6px;bottom:-4px;width:120px" alt="">''','task')
  notes=f'''<div class="note"><b>Thẻ có icon</b><br>Thẻ đang mở to hơn, thò ra nhiều hơn, chữ và icon to. Thẻ khác nhỏ lại, hơi nhạt. Mỗi mục một màu: Sổ giống xanh lá, Kho vàng, Việc của Ngoại cam.</div>
<div class="note"><b>Bỏ dòng ô li</b><br>Trang giấy trơn màu kem, giữ bìa giấy kraft và đường chỉ khâu giữa gáy sổ.</div>
<div class="note"><b>Hạt giống là sticker</b><br>Hình cây có viền trắng như sticker bóc dán. Cây chưa mở chỉ có bóng xám, tên để ???, ghi cấp mở.</div>
<div class="note"><b>Số liệu bằng icon</b><br>{st('coin','')} giá hạt · {st('clock','')} thời gian lớn · {st('yield','')} thu được. Chỉ để số, đọc lướt là nắm.</div>'''
  body=f'''<div class="bd" style="width:2060px;height:2330px"><div class="h">Sổ vườn của Ngoại · v2</div><p class="sub">Sửa theo góp ý: thẻ có icon và lớn nhỏ theo mục đang mở, bỏ dòng ô li, hạt giống thành sticker, số liệu bằng icon, kho canh số thẳng hàng, mỗi mục có màu và icon riêng.</p>
<div style="display:flex;gap:150px;align-items:flex-start">{spread}<div style="display:flex;flex-direction:column;gap:16px;width:330px;margin-top:20px">{notes}</div></div>
<div class="h2" style="margin-top:50px">Bản điện thoại</div>
<div style="display:flex;gap:40px;align-items:flex-start;margin-top:40px">{phone1}{phone2}
<div style="display:flex;flex-direction:column;gap:16px;width:560px"><div class="note"><b>Kho là gì, thêm lu là gì</b><br>Kho là chỗ cất đồ hái về. Sức chứa là kho chứa tối đa bao nhiêu món. Đầy rồi thì bấm <b>Thêm lu</b>: mua thêm một cái lu sành, kho chứa được nhiều hơn. Bản trước ghi "Nới lu" dễ hiểu lầm nên đổi tên.</div>
<div class="note"><b>Kho bỏ đơn vị</b><br>Không ghi bó, trái, nắm nữa. Chỉ có hình, tên và con số canh lề phải thẳng hàng.</div>
<div class="note"><b>Thẻ trên điện thoại</b><br>Thẻ nằm trên đầu trang. Thẻ đang mở có icon và chữ, thẻ khác chỉ có icon.</div>
<div class="note"><b>Phần thưởng</b><br>Xu hay rơm đều hiện bằng icon kèm con số.</div></div></div>
<div class="h2" style="margin-top:50px">Tạo hình icon cây · low-poly như game</div><p class="sub" style="margin-bottom:10px;max-width:1900px">Học từ pack low-poly: một khối chính rõ dáng, đặt nghiêng 3/4; mặt to, ít mặt, mỗi mặt một màu phẳng; các phần chồng lên nhau mà không đâm xuyên (lá nằm ngoài trái); món nhiều trái thì xếp song song so le trước sau, không chĩa ra hai bên. Bắp có ô hạt so le hai tông vàng, ớt hai trái song song cùng chiều cong, hành thân trắng ngắn lá xanh dài, khổ qua gân nổi và gai sần.</p>
<div style="display:flex;gap:26px;background:#3a3530;border-radius:24px;padding:20px 28px;width:fit-content">'''+''.join([f'<img src="{I(k)}" style="width:220px;height:220px" alt="">' for k in ['cai','hanh','ot','bap','cachua','khoqua']])+'''</div></div></div>'''
  return MB.HEAD.replace('{t}','Miệt Vườn 2.0 · Sổ vườn').replace('</style></helmet>',CSS+'</style></helmet>')+body+MB.FOOT
P=MB.P
pub=so(False); open(P+'SoVuon.dc.html','w').write(pub)
loc=so(True).replace('<x-dc>','<link rel="stylesheet" href="node_modules/@fontsource/patrick-hand/index.css"><link rel="stylesheet" href="node_modules/@fontsource/paytone-one/index.css"><link rel="stylesheet" href="node_modules/@fontsource/baloo-2/600.css"><link rel="stylesheet" href="node_modules/@fontsource/baloo-2/700.css">').replace('</x-dc>','').replace('<helmet>','').replace('</helmet>','').replace('<script src="./support.js"></script>','')
open('lp/so_prev.html','w').write(loc)
