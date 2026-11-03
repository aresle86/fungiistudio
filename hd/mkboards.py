import re
P='/tmp/claude-0/-home-claude/7603b55f-8cb0-541e-b9b6-341bfe50c7c8/scratchpad/mv-styles/project/'
src=open(P+'Ngoai2.dc.html').read()
style=src[src.index('<style>'):src.index('</style>')+8]
style=style.replace('</style>','')
B={'stallA':'45c67615853e38abacd6fa8d8cba8dff','stallB':'a097f17114fc8fa880dd338a25ee0096','cai':'4451b2de157fa59f88261ece686b698d','hanh':'4fe0d5d3879d9b4eee2a90a5a3588f0e','ot':'56a1ba546e4e97c7c7464dcda462b8ba','bap':'3c21ce8e596dbc33979fd04df2b3ff6f','cachua':'d35a63cbee1e1839a47f19b584e3624d','khoqua':'21addd5ae78f13d50ad6ae1aca4ef7df','rom':'f1653e55d362043bff8a6e2b4bc425be','vui':'0570e247c223b955c12807c95f958781','dan':'3766ed8056ff9d25afee9815df869d21','nhay':'bf3e57b8db6611970d132e2fee6739bd','bat':'d5824006a080411ee889ac406e7e1f1f'}
LOCAL={'bap':'c3_bap','ot':'c3_ot','hanh':'c3_hanh','stallA':'stall_ac','stallB':'stall_bc','vui':'ng_ex_vui','dan':'ng_ex_dan','nhay':'ng_ex_nhay','bat':'ng_ex_bat'}
def img(k,local): return ('board/'+LOCAL.get(k,'ic_'+k)+'.png') if local else '/_blob/'+B[k]
EXTRA=r'''
.hand{font-family:"Patrick Hand",cursive}
.book{position:relative;display:flex;filter:drop-shadow(0 10px 0 #6B4529) drop-shadow(0 18px 24px rgba(74,47,30,.25))}
.cover{position:absolute;inset:-14px -16px -14px -16px;background:#B48560;border-radius:22px;box-shadow:inset 0 0 0 4px #8A5D3B,inset 0 -8px 0 rgba(0,0,0,.12)}
.pg{position:relative;background-color:#FBF7EE;background-image:linear-gradient(90deg,transparent 54px,#E8A090 54px,#E8A090 56px,transparent 56px),repeating-linear-gradient(0deg,transparent 0 31px,#C9C2E0 31px 32px),repeating-linear-gradient(0deg,transparent 0 7px,#ECE6F2 7px 8px),repeating-linear-gradient(90deg,transparent 0 31px,#ECE6F2 31px 32px);padding:26px 26px 26px 70px;box-sizing:border-box}
.pg.l{border-radius:14px 4px 4px 14px;box-shadow:inset -18px 0 22px -18px rgba(74,47,30,.35)}
.pg.r{border-radius:4px 14px 14px 4px;box-shadow:inset 18px 0 22px -18px rgba(74,47,30,.35)}
.staple{position:absolute;left:50%;width:6px;height:34px;margin-left:-3px;background:linear-gradient(90deg,#9aa0a6,#e6e8ea,#9aa0a6);border-radius:3px;z-index:3}
.tabs{position:absolute;right:-58px;top:40px;display:flex;flex-direction:column;gap:10px;z-index:0}
.tab{width:74px;padding:12px 0 12px 22px;box-sizing:border-box;border-radius:0 14px 14px 0;font-family:"Paytone One";font-size:14px;color:#FBF7EE;writing-mode:vertical-rl;text-orientation:mixed;height:120px;box-shadow:inset 0 -5px 0 rgba(0,0,0,.15)}
.label{position:absolute;left:50%;top:-58px;transform:translateX(-50%) rotate(-1.5deg);background:#FBF7EE;border:3px solid #C24A2E;border-radius:12px;padding:6px 22px;text-align:center;box-shadow:0 3px 0 #8A5D3B;z-index:4}
.ph{font-family:"Paytone One";font-size:30px;color:#6B4529;margin:0 0 6px}
.hn{font-family:"Patrick Hand";font-size:23px;color:#2B3446;line-height:32px}
.pkt{position:relative;background:#E3BC97;border-radius:6px 6px 12px 12px;padding:10px 8px 8px;text-align:center;box-shadow:0 4px 0 #B48560}
.pkt:before{content:"";position:absolute;left:0;right:0;top:0;height:12px;background:repeating-linear-gradient(90deg,#D2A57E 0 6px,#E3BC97 6px 12px);border-radius:6px 6px 0 0}
.pkt img{width:78px;height:78px;margin-top:4px}
.pkt b{display:block;font-family:"Paytone One";font-size:16px;color:#6B4529}
.pkt span{display:block;font-family:"Patrick Hand";font-size:17px;color:#4A2F1E;line-height:1.15}
.pkt.sel{outline:4px dashed #C24A2E;outline-offset:4px}
.pkt.lock{filter:grayscale(.8) brightness(1.05);opacity:.75}
.clip{position:absolute;top:-10px;right:14px;width:12px;height:30px;border:3px solid #9aa0a6;border-radius:8px}
.chk{display:flex;align-items:flex-start;gap:12px;font-family:"Patrick Hand";font-size:23px;color:#2B3446;line-height:32px}
.box{flex:none;width:24px;height:24px;border:2.5px solid #2B3446;border-radius:5px;margin-top:4px;position:relative}
.done .box:after{content:"";position:absolute;left:3px;top:-6px;width:9px;height:18px;border:solid #C24A2E;border-width:0 4px 4px 0;transform:rotate(40deg)}
.done .tx{text-decoration:line-through;text-decoration-color:#C24A2E;text-decoration-thickness:3px;color:#8A7A6A}
.rw{font-family:"Paytone One";font-size:14px;color:#FBF7EE;background:#EDB940;border-radius:10px;padding:2px 9px;box-shadow:0 2px 0 #C9952A;margin-left:auto;white-space:nowrap;line-height:22px;align-self:center}
.phone{width:400px;height:820px;border-radius:46px;background:#2B3446;padding:12px;box-sizing:border-box;box-shadow:0 10px 0 #1c2230}
.scr{width:100%;height:100%;border-radius:36px;overflow:hidden;position:relative;background:linear-gradient(#a9cf86,#7fbc52)}
.note{background:#FBF7EE;border-radius:20px;box-shadow:0 5px 0 #D2A57E;padding:16px 20px;font-size:17px;font-weight:600;line-height:1.45}
.note b{font-family:"Paytone One";font-weight:400;color:#6B4529}
.tag{display:inline-block;font-family:"Paytone One";font-size:13px;color:#FBF7EE;border-radius:9px;padding:2px 9px;margin-right:6px}
.chalk{background:#2F3B33;border:12px solid #8A5D3B;border-radius:12px;padding:16px 22px;box-shadow:inset 0 0 30px rgba(0,0,0,.35),0 6px 0 #6B4529;font-family:"Patrick Hand";color:#F2EEE4;font-size:26px;line-height:1.35}
.chalk .up{color:#9fd36a}.chalk .dn{color:#F08A6E}
.order{background:#FBF7EE;border-radius:22px;box-shadow:0 0 0 4px #6B4529,0 8px 0 #6B4529;padding:14px 16px 12px;position:relative}
.order:after{content:"";position:absolute;bottom:-20px;left:44px;border:14px solid transparent;border-top-color:#6B4529}
.order .who{font-family:"Paytone One";font-size:18px;color:#6B4529}
.order .its{display:flex;gap:10px;margin:8px 0}
.order .it{width:70px;text-align:center;font-family:"Paytone One";font-size:16px;color:#4A2F1E;background:#E8DFCC;border-radius:14px;padding:4px 0}
.order .it img{width:58px;height:58px;display:block;margin:0 auto}
.order .it.ok{background:#d9ecc6}.order .it.no{background:#f6d6cc}
.step{display:flex;gap:16px;align-items:flex-start}
.num{flex:none;width:44px;height:44px;border-radius:50%;background:#C24A2E;color:#FBF7EE;font-family:"Paytone One";font-size:22px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 0 #8f2f1c}
'''
HEAD='<!doctype html>\n<html lang="vi"><head><meta charset="utf-8"><title>{t}</title><script src="./support.js"></script></head><body><x-dc>\n<helmet><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700&family=Paytone+One&family=Patrick+Hand&subset=vietnamese&display=swap">\n'+style+EXTRA+'</style></helmet>\n'
FOOT='\n</x-dc></body></html>\n'

def so(L):
  I=lambda k: img(k,L)
  seeds=[('cai','Cải xanh','12 xu','30 phút','6 bó',True,False),('hanh','Hành lá','10 xu','45 phút','8 bó',False,False),('ot','Ớt','20 xu','3 giờ','10 nắm',False,False),('bap','Bắp','30 xu','4 giờ','8 trái',False,False),('cachua','Cà chua','28 xu','4 giờ','12 trái',False,False),('khoqua','Khổ qua','24 xu','3 giờ','8 trái',False,True)]
  pk=''.join(f'<div class="pkt{" sel" if s else ""}{" lock" if lk else ""}"><div class="clip"></div><img src="{I(k)}" alt=""><b>{n}</b><span>{p} · lớn {t}</span><span>thu ~{y}</span>{"<span style=\'color:#C24A2E\'>cần giàn · cấp 3</span>" if lk else ""}</div>' for k,n,p,t,y,s,lk in seeds)
  spread=f'''<div style="position:relative;margin:70px 0 0 16px;width:1240px;height:740px">
<div class="cover"></div>
<div class="tabs"><div class="tab" style="background:#86B06A">Sổ giống</div><div class="tab" style="background:#EDB940;margin-left:-8px">Kho</div><div class="tab" style="background:#F08A6E;margin-left:-8px">Việc của Ngoại</div></div>
<div class="book" style="height:740px">
<div class="pg l" style="width:620px;height:740px"><div class="ph">Sổ giống</div><div class="hn" style="margin:-2px 0 12px">Chọn bao hạt, kéo thả xuống liếp là gieo.</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px 18px">{pk}</div></div>
<div class="pg r" style="width:620px;height:740px"><div style="display:flex;gap:18px;align-items:center"><img src="{I('cai')}" style="width:150px;height:150px;background:#E8DFCC;border-radius:24px" alt=""><div><div class="ph" style="margin:0">Cải xanh</div><div><span class="tag" style="background:#86B06A">Liếp</span><span class="tag" style="background:#6E95C4">Ưa ẩm</span><span class="tag" style="background:#EDB940">Mau lớn</span></div></div></div>
<div class="hn" style="margin-top:16px">Ngoại dặn:<br>· Tưới sáng sớm với chiều mát, trưa nắng đừng tưới.<br>· Phủ rơm lên liếp giữ ẩm, đỡ phải tưới.<br>· Rải dày được, cải mọc sát nhau không sao.<br>· 30 phút là hái, để lâu cải già, ra ngồng.</div>
<div style="display:flex;gap:10px;margin-top:20px;align-items:center"><div style="font-family:Patrick Hand;font-size:22px;color:#4A2F1E;width:150px">Bao hạt trong túi:<br><b style="font-family:Paytone One;font-size:28px;color:#6B4529">3 bao</b></div><span class="btn g">Mua 1 bao · 12 xu</span><span class="btn">Mua 5 bao</span></div>
<img src="{I('dan')}" style="position:absolute;right:-6px;bottom:0;width:170px" alt=""></div>
<div class="staple" style="top:150px"></div><div class="staple" style="top:540px"></div>
</div>
<div class="label"><div style="font-family:Paytone One;font-size:13px;color:#C24A2E;letter-spacing:.5px">VỞ Ô LI</div><div class="hand" style="font-size:26px;color:#2B3446;line-height:1">Sổ vườn của Ngoại</div></div>
</div>'''
  kho_items=[('cai','Cải xanh','12 bó'),('cachua','Cà chua','7 trái'),('ot','Ớt','4 nắm'),('rom','Rơm','3 bó')]
  kho=''.join(f'<div style="display:flex;align-items:center;gap:10px;border-bottom:2px dashed #C9C2E0;padding:4px 0"><img src="{I(k)}" style="width:60px;height:60px" alt=""><span class="hn" style="flex:1">{n}</span><span class="hn" style="font-size:28px;color:#C24A2E">{c}</span></div>' for k,n,c in kho_items)
  phone1=f'''<div class="phone"><div class="scr"><div style="position:absolute;inset:0;background:rgba(74,47,30,.25)"></div>
<div style="position:absolute;left:14px;right:14px;top:70px;bottom:24px;">
<div class="pg r" style="height:100%;border-radius:20px;padding:20px 16px 16px 66px;box-shadow:0 8px 0 #8A5D3B, inset 0 0 0 3px #B48560">
<div class="ph" style="font-size:26px">Kho</div><div class="hn" style="font-size:20px;margin-bottom:8px">Đồ hái về cất ở đây.</div>{kho}
<div class="hn" style="font-size:20px;margin-top:12px">Lu chứa: 26 / 40</div><div style="height:16px;border-radius:8px;background:#E8DFCC;box-shadow:inset 0 0 0 2px #B48560;margin:4px 0 16px"><div style="width:65%;height:100%;border-radius:8px;background:#86B06A"></div></div>
<div style="display:flex;gap:10px"><span class="btn g">Đem ra chợ</span><span class="btn">Nới lu</span></div></div>
<div style="position:absolute;top:-30px;right:16px;display:flex;gap:6px"><div style="width:54px;height:40px;border-radius:12px 12px 0 0;background:#86B06A"></div><div style="width:54px;height:48px;border-radius:12px 12px 0 0;background:#EDB940;box-shadow:inset 0 -4px 0 rgba(0,0,0,.12)"></div><div style="width:54px;height:40px;border-radius:12px 12px 0 0;background:#F08A6E"></div></div>
</div></div></div>'''
  tasks=[('Tưới liếp cải buổi sáng',True,'+5 xu'),('Phủ rơm cho luống ớt',True,'+1 bó rơm'),('Hái 10 trái cà chua',False,'+12 xu'),('Bán 5 bó cải cho cô Ba',False,'+8 xu'),('Cho gà ăn lúa',False,'+3 xu')]
  tk=''.join(f'<div class="chk{" done" if d else ""}" style="margin-bottom:6px"><div class="box"></div><span class="tx" style="flex:1">{t}</span><span class="rw">{r}</span></div>' for t,d,r in tasks)
  phone2=f'''<div class="phone"><div class="scr"><div style="position:absolute;inset:0;background:rgba(74,47,30,.25)"></div>
<div style="position:absolute;left:14px;right:14px;top:70px;bottom:24px;">
<div class="pg r" style="height:100%;border-radius:20px;padding:20px 16px 16px 66px;box-shadow:0 8px 0 #8A5D3B, inset 0 0 0 3px #B48560">
<div class="ph" style="font-size:26px">Việc của Ngoại</div><div class="hn" style="font-size:20px;margin-bottom:10px">Hôm nay · thứ Tư</div>{tk}
<div class="hn" style="font-size:20px;margin-top:14px;color:#6B4529">Xong hết 5 việc: Ngoại cho thêm 1 bao hạt khổ qua.</div></div>
<img src="{I('vui')}" style="position:absolute;left:-14px;bottom:-14px;width:150px" alt="">
<div style="position:absolute;top:-30px;right:16px;display:flex;gap:6px"><div style="width:54px;height:40px;border-radius:12px 12px 0 0;background:#86B06A"></div><div style="width:54px;height:40px;border-radius:12px 12px 0 0;background:#EDB940"></div><div style="width:54px;height:48px;border-radius:12px 12px 0 0;background:#F08A6E;box-shadow:inset 0 -4px 0 rgba(0,0,0,.12)"></div></div>
</div></div></div>'''
  notes='''<div class="note"><b>Vì sao là vở ô li</b><br>Vở học trò bao giấy kraft, có nhãn vở, đóng ghim giữa. Ai lớn lên ở Việt Nam cũng từng có, nhìn là thấy nhà. Thay hẳn mấy bảng popup hiện tại.</div>
<div class="note"><b>Mở, đóng</b><br>Nút sổ ở góc dưới. Sổ trượt lên rồi lật mở, nền vườn tối nhẹ phía sau. Bấm ra ngoài là đóng. Tiếng lật giấy nhẹ, không bass.</div>
<div class="note"><b>Ba thẻ giấy dán mép</b><br>Sổ giống · Kho · Việc của Ngoại. Trên điện thoại sổ chỉ mở một trang, thẻ nằm trên đầu trang.</div>
<div class="note"><b>Chữ</b><br>Tiêu đề và nút dùng Paytone One như game. Lời Ngoại ghi dùng chữ viết tay Patrick Hand, có đủ dấu tiếng Việt.</div>
<div class="note"><b>Gieo hạt</b><br>Bao hạt mua xong nằm trong túi. Kéo bao từ sổ thả xuống liếp là gieo luôn, nối sang bước khay hạt, bình tưới, liềm.</div>'''
  body=f'''<div class="bd" style="width:2060px;height:1900px"><div class="h">Sổ vườn của Ngoại</div><p class="sub">Đề xuất giao diện mới: mọi bảng chọn giống, xem kho, việc trong ngày gom vào một cuốn vở ô li bìa giấy kraft. Bên trái là bản máy tính (mở hai trang), giữa là bản điện thoại (một trang).</p>
<div style="display:flex;gap:70px;align-items:flex-start">{spread}<div style="display:flex;flex-direction:column;gap:16px;width:330px;margin-top:20px">{notes}</div></div>
<div class="h2" style="margin-top:44px">Bản điện thoại</div>
<div style="display:flex;gap:40px;align-items:flex-start">{phone1}{phone2}
<div style="display:flex;flex-direction:column;gap:16px;width:520px"><div class="note"><b>Kho</b><br>Đồ hái về xếp hàng như ghi sổ, số đếm viết đỏ. Có thanh "lu chứa" để sau này nới kho. Nút "Đem ra chợ" mở thẳng sạp chợ.</div>
<div class="note"><b>Việc của Ngoại</b><br>Mỗi ngày Ngoại ghi 4–5 việc nhỏ. Làm xong tự gạch bằng mực đỏ, nhận xu hoặc rơm. Xong hết thì Ngoại nhảy cẫng, tặng bao hạt.</div>
<div class="note"><b>Màu thẻ</b><br>Xanh lá, vàng, cam lấy từ bảng màu game, khớp màu nút Kho và Chợ đang có.</div></div></div></div>'''
  return HEAD.replace('{t}','Miệt Vườn 2.0 · Sổ vườn')+body+FOOT

def cho(L):
  I=lambda k: img(k,L)
  od=lambda who,its,xu,pose: f'''<div style="display:flex;gap:14px;align-items:flex-end"><div style="flex:none;width:64px;height:64px;border-radius:50%;background:#E3BC97;box-shadow:inset 0 -5px 0 #D2A57E;display:flex;align-items:center;justify-content:center;font-family:Paytone One;font-size:24px;color:#6B4529">{who.split(' ')[1][0].upper()}</div><div class="order" style="flex:1"><div class="who">{who}</div><div class="its">{''.join(f'<div class="it {c}"><img src="{I(k)}" alt="">{n}</div>' for k,n,c in its)}</div><div style="display:flex;align-items:center;gap:10px"><span style="font-family:Paytone One;font-size:20px;color:#C9952A">{xu}</span><span class="btn g" style="margin-left:auto">Giao</span></div></div></div>'''
  body=f'''<div class="bd" style="width:2060px;height:1500px"><div class="h">Sạp chợ ven sông</div><p class="sub">Đề xuất thay cái quầy che sọc đỏ trắng bằng sạp tre mái lá dừa nước đặt cạnh bến. Đồ bán bày trong thúng và nia, có cân đồng hồ, bảng giá viết phấn, buồng chuối treo xà, nón lá máng cột, đòn gánh dựng bên cạnh.</p>
<div style="display:flex;gap:30px;align-items:flex-start">
<div style="background:#C3DDD5;border-radius:24px;padding:20px;width:780px;height:760px;box-sizing:border-box;display:flex;align-items:center;justify-content:center"><img src="{I('stallA')}" style="max-width:100%;max-height:100%" alt="Sạp tre nhìn chính diện"></div>
<div style="background:#C3DDD5;border-radius:24px;padding:20px;width:560px;height:760px;box-sizing:border-box;display:flex;align-items:center;justify-content:center"><img src="{I('stallB')}" style="max-width:100%;max-height:100%" alt="Sạp tre nhìn từ góc game"></div>
<div style="display:flex;flex-direction:column;gap:14px;width:560px">
<div class="note"><b>Đúng miền Tây</b><br>Sạp tre chẻ, mái lá dừa nước, thúng, nia, cân đồng hồ, bảng phấn, đòn gánh, ghế đẩu gỗ. Không còn đồ lạ.</div>
<div class="note"><b>Đặt ở đâu</b><br>Trên bờ sông kế bến ghe, để khách đi bộ ghé sạp và ghe thương lái cập bến mua sỉ.</div>
<div class="note"><b>Khách</b><br>Khách là người trong xóm, làm chibi cùng kiểu Ngoại (nón lá, áo bà ba, khăn rằn), thiết kế ở vòng sau. Ở đây tạm để vòng tròn chữ cái.</div>
<div class="note"><b>Đồ trên sạp đổi theo kho</b><br>Kho có cà chua thì thúng có cà chua, hết thì thúng trống. Nhìn sạp là biết còn gì để bán.</div></div></div>
<div class="h2" style="margin-top:34px">Cách bán</div>
<div style="display:grid;grid-template-columns:640px 640px 640px;gap:30px">
<div style="display:flex;flex-direction:column;gap:18px"><div class="step"><div class="num">1</div><div class="sub" style="margin:0">Khách ghé sạp, trên đầu hiện bong bóng đơn hàng. Đủ hàng thì ô xanh, thiếu thì ô đỏ. Bấm Giao là xong.</div></div>
{od('Cô Ba hàng xóm',[('cai','5 bó','ok'),('hanh','3 bó','ok')],'+29 xu','vui')}
{od('Chú Tư xóm dưới',[('cachua','8 trái','ok'),('ot','6 nắm','no')],'+78 xu','bat')}</div>
<div style="display:flex;flex-direction:column;gap:18px"><div class="step"><div class="num">2</div><div class="sub" style="margin:0">Bảng giá viết phấn đổi mỗi ngày. Mũi tên xanh là giá lên, đỏ là giá xuống. Gần Tết, mùa mưa giá đổi theo mùa.</div></div>
<div class="chalk"><div style="font-size:30px;text-align:center;margin-bottom:6px">Giá hôm nay</div><div style="display:grid;grid-template-columns:1fr auto auto;gap:2px 16px"><span>Cải xanh</span><span>4 xu</span><span class="up">▲</span><span>Hành lá</span><span>3 xu</span><span>–</span><span>Ớt</span><span>6 xu</span><span class="up">▲</span><span>Bắp</span><span>8 xu</span><span class="dn">▼</span><span>Cà chua</span><span>6 xu</span><span>–</span><span>Khổ qua</span><span>7 xu</span><span class="dn">▼</span></div></div></div>
<div style="display:flex;flex-direction:column;gap:18px"><div class="step"><div class="num">3</div><div class="sub" style="margin:0">Vài giờ một lần có ghe thương lái cập bến, lấy sỉ số lượng lớn. Giá mỗi món thấp hơn bán lẻ nhưng bán một lần được nhiều.</div></div>
{od('Ghe thương lái · ghé 20 phút',[('bap','30 trái','no'),('khoqua','20 trái','ok'),('cai','25 bó','ok')],'+390 xu','nhay')}
<div class="note"><b>Sau này</b><br>Khi có chơi chung, bạn bè ghé vườn cũng mua được ở sạp này.</div></div></div></div>'''
  return HEAD.replace('{t}','Miệt Vườn 2.0 · Sạp chợ')+body+FOOT

for L in (False,True):
  a=so(L); b=cho(L)
  if L:
    open('lp/so_prev.html','w').write(a.replace('<x-dc>','<link rel="stylesheet" href="node_modules/@fontsource/patrick-hand/index.css"><link rel="stylesheet" href="node_modules/@fontsource/paytone-one/index.css"><link rel="stylesheet" href="node_modules/@fontsource/baloo-2/600.css"><link rel="stylesheet" href="node_modules/@fontsource/baloo-2/700.css">').replace('</x-dc>','').replace('<helmet>','').replace('</helmet>','').replace('<script src="./support.js"></script>',''))
    open('lp/cho_prev.html','w').write(b.replace('<x-dc>','<link rel="stylesheet" href="node_modules/@fontsource/patrick-hand/index.css"><link rel="stylesheet" href="node_modules/@fontsource/paytone-one/index.css"><link rel="stylesheet" href="node_modules/@fontsource/baloo-2/600.css"><link rel="stylesheet" href="node_modules/@fontsource/baloo-2/700.css">').replace('</x-dc>','').replace('<helmet>','').replace('</helmet>','').replace('<script src="./support.js"></script>',''))
  else:
    open(P+'SoVuon.dc.html','w').write(a); open(P+'ChoSong.dc.html','w').write(b)
