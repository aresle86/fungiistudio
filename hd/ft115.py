# ft115: Sổ cổ tích chưa mở thì không lộ tên truyện, giữ hình bóng cây; câu ẩn gợi về sự tích chứ không chỉ cách làm. python3 ft115.py vào ra
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
R={'vusua':'Có người ra đầu ngõ đứng chờ hoài, chờ tới hóa thân mà đứa con vẫn chưa về.',
'tretramdot':'Một lời hứa gả con bị nuốt lời. Một câu thần chú. Trăm khúc rời nhau bỗng nối liền.',
'traucau':'Hai anh em giống nhau như đúc, một tảng đá bên sông, một người vợ đi tìm chồng tới cùng.',
'duahau':'Một nhà bị đày ra đảo hoang. Bầy chim bay ngang thả xuống mấy hột đen nhánh.',
'khevang':'Một con chim lớn biết nói, một cái túi ba gang, và một người anh tham lam.',
'sodua':'Đứa nhỏ sinh ra tròn lông lốc, không tay không chân, mà tiếng sáo hay nhứt xóm.'}
js='const FTRID = '+repr(R).replace("': '","': '")+';'
import json
js='const FTRID = '+json.dumps(R,ensure_ascii=False)+';'
rep("function pgCotich(part){",js+" function pgCotich(part){")
rep("if (!F || F.st < 1) return `<div class=\"ftc no\"><img src=\"${img}\" alt=\"\"><div><b>${F ? 'Đốm sáng lạ' : '???'}</b><small>${D.story}</small><p>${F ? 'Có đốm sáng trong vườn, lại chạm thử đi con.' : D.hint}</p>",
"if (!F || F.st < 1) return `<div class=\"ftc no\"><img src=\"${img}\" alt=\"\"><div><b>${F ? 'Đốm sáng lạ' : '???'}</b><small>${fxT('Chuyện Ngoại chưa kể')}</small><p>${F ? 'Có đốm sáng trong vườn, lại chạm thử đi con.' : fxT(FTRID[k] || '…')}</p>")
open(dst,'w',encoding='utf-8').write(s)
