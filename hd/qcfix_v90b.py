# QC v90b (anh Ares chốt 1/11): sửa icon cuốc dựng lỗi; icon việc đúng nghĩa; bỏ mọi chỗ báo trước cấp sau.
import sys
P = sys.argv[1] if len(sys.argv) > 1 else 'live/vuon3d.html'
s = open(P, encoding='utf-8').read(); log = []
def rep(old, new, n=1, tag=''):
    global s
    c = s.count(old)
    if c != n: sys.exit(f'FAIL [{tag}] khớp {c} lần, cần {n}: {old[:90]!r}')
    s = s.replace(old, new); log.append(tag)

# A. Icon cuốc: cán xoay ngược chiều nên cán và lưỡi nằm rời nhau
rep("icon('cuoc', p => { add(p, new T.CylinderGeometry(.032, .038, .95, 6), '#B48560', -.05, -.05, 0, [0, 0, .75]); add(p, new T.CylinderGeometry(.05, .05, .1, 6), '#6B4529', .27, .27, 0, [0, 0, .75]);",
    "icon('cuoc', p => { add(p, new T.CylinderGeometry(.032, .038, .95, 6), '#B48560', -.05, -.05, 0, [0, 0, -.75]); add(p, new T.CylinderGeometry(.05, .05, .1, 6), '#6B4529', .27, .27, 0, [0, 0, -.75]);", tag='icon cuốc liền cán')

# B. Icon việc Ngoại nhờ đúng nghĩa: cắm giàn tre dùng bó tre; việc đào đắp giữ cuốc
rep("7: { t: 'pay', xu: 100, txt: 'Cắm giàn tre',", "7: { t: 'pay', xu: 100, ic: 'tre', txt: 'Cắm giàn tre',", tag='việc cắm giàn tre: icon tre')
rep("else if (q && q.t === 'pay' && ready){ ic = ICON.cuoc || UIC.task;", "else if (q && q.t === 'pay' && ready){ ic = (q.ic && ICON[q.ic]) || ICON.cuoc || UIC.task;", tag='thẻ: icon theo việc')
rep("const qi = q.t === 'weed' ? UIC.sickle : q.t === 'pay' ? (ICON.cuoc || UIC.task) : UIC.task;", "const qi = q.t === 'weed' ? UIC.sickle : q.t === 'pay' ? ((q.ic && ICON[q.ic]) || ICON.cuoc || UIC.task) : UIC.task;", tag='Sổ: icon theo việc')

# C. Túi hạt: bỏ ô giống kế tiếp bị khoá "Cấp N"
rep("if (nxt) h += `<div class=\"sk lock\"", "if (false && nxt) h += `<div class=\"sk lock\"", tag='túi hạt: bỏ giống chưa mở')
# D. Sổ giống: ẩn giống chưa tới cấp (giống quý mùa Tết vẫn hiện vì theo mùa, không theo cấp)
rep("for (const [k, c] of Object.entries(CROPS)) h += !unlocked(k) ? `<div class=\"stk lock\">",
    "for (const [k, c] of Object.entries(CROPS)) h += !unlocked(k) ? '' : !unlocked(k) ? `<div class=\"stk lock\">", tag='Sổ giống: ẩn giống chưa mở')
# E. Danh sách món (bếp, khạp, lò, nong…): ẩn món chưa tới cấp
rep("+ Object.keys(R).map(k => { const d = R[k], lk = (ST.lv || 1) < (d.lv || 1), can = !lk && canIn(d.in);",
    "+ Object.keys(R).filter(k => (ST.lv || 1) >= (R[k].lv || 1)).map(k => { const d = R[k], lk = (ST.lv || 1) < (d.lv || 1), can = !lk && canIn(d.in);", tag='danh sách món: ẩn món chưa mở')

# F. Liếp cỏ: không nói số cấp; bong bóng liềm chỉ hiện khi đủ xu đắp
rep("`Tới cấp ${bedNext()} Ngoại với con đắp thêm liếp ở đây.`", "'Chăm mấy liếp đang có trước, mai mốt Ngoại với con đắp thêm.'", tag='liếp cỏ: chữ')
rep("`<div class=\"acts\"><span class=\"lockb\">Mở ở cấp ${bedNext()}</span></div>`", "''", tag='liếp cỏ: bỏ nhãn cấp')
rep("return toast(`Tới cấp ${bedNext()} mới đắp thêm được con.`, 'dan');", "return toast('Vườn đủ liếp chăm rồi, mai mốt mình đắp thêm nghe con.', 'dan');", tag='liếp cỏ: toast')
rep("v.want = nOpen() < bedCap() ? 'd' : null;", "v.want = nOpen() < bedCap() && ST.xu >= bedCost() ? 'd' : null;", tag='bong bóng liềm khi đủ xu')

# G. Câu báo khoá: không nói số cấp
rep("`${c.name} tới cấp ${UNLOCK[k]} mới trồng được con.`", "`Giống ${c.name.toLowerCase()} Ngoại chưa có, mai mốt Ngoại cho con nghe.`", n=2, tag='giống chưa có: chữ')
rep(", tới cấp ${UNLOCK[k]} Ngoại cho giống nghe con.`", ", mai mốt Ngoại cho giống nghe con.`", tag='chỗ trồng: chữ')
rep("return toast(`Tới cấp ${GA.buyLv} mới mua thêm gà được con.`, 'dan');", "return toast('Nuôi mấy con gà này cho quen tay trước nghe con.', 'dan');", tag='mua gà: chữ')
rep(" : `Tới cấp ${GA.buyLv} mua thêm gà, nâng chuồng và ấp trứng được.`}`);", " : ''}`);", tag='bảng gà: bỏ báo trước')
rep("Tới cấp ${UNLOCK[P.tree]} Ngoại cho con cây giống.", "Mai mốt Ngoại cho con cây giống.", tag='góc cây trái: chữ')
rep("`Tới cấp ${BEP.lv} Ngoại chỉ con nấu bếp củi nghe`", "'Mai mốt Ngoại chỉ con nấu bếp củi nghe'", tag='bếp: chữ')
# H. Bảng gỗ đất chưa mở: bỏ số cấp
rep("`${z.name}|Cấp ${z.Z.lv} mới mở`", "`${z.name}|Đất còn hoang`", tag='bảng đất: chữ')

open(P, 'w', encoding='utf-8').write(s); print('OK', len(log), 'chỗ vá:', ', '.join(log))

# I. Phần còn sót (vá đợt 2)
s = open(P, encoding='utf-8').read(); log = []
rep(": UX.upc('noop', ICON[k], U.name, null, { k, why: `Mở ở cấp ${U.lv}` }))", ": '')", tag='nâng cấp: ẩn mục chưa mở')
rep(": UX.upc('noop', ICON[k], CROPS[k].name, null, { k, why: 'Mở ở cấp ' + UNLOCK[k] })).join('')", ": '').join('')", tag='cây giống sửa vườn: ẩn cây chưa mở')
rep("`Tới cấp ${UNLOCK[p.crop]} con trồng được.`", "'Mai mốt vườn mình cũng trồng được.'", tag='thăm vườn: chữ')
rep("Tới cấp ${NB2.lv} con mới chèo qua vườn bạn bè được.", "Mai mốt con chèo xuồng qua vườn bạn bè được.", tag='hàng xóm: chữ')
rep("`Tới cấp ${NB2.lv} chèo qua vườn người ta được.`", "'Mai mốt chèo xuồng qua vườn người ta chơi nghe.'", tag='hàng xóm mới: chữ')
open(P, 'w', encoding='utf-8').write(s); print('OK đợt 2', len(log), 'chỗ vá:', ', '.join(log))
