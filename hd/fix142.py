# v142: sửa theo tin anh Ares 12/11.
# (1) Cây trái (ổi, đu đủ...) chạm bong bóng không tưới, không hái được: cây chiếm 2 ô, tâm cây nằm ngay ranh 2 ô
#     nên tưới/hái theo tâm thì không trúng ô nào. Chạm bong bóng giờ tính điểm giữa ô chủ của cây.
# (3) Mùa nước nổi theo lịch thật: tháng 8 tới hết tháng 11 (anh Ares chốt 12/11). Cá linh, cá he, cá lăng, cá hu ra trong mùa này.
# (4) Cá linh đi theo bầy như tép: câu một lần được 3-5 con (anh Ares chốt 12/11).
# (2) Bù nhìn rơm 150 xu ở tab Mua: anh Ares bỏ (tab Mua dành cho muối, đường; đồ trang trí đã có bù nhìn rơm riêng).
#     Ai đã mua rồi vẫn giữ con bù nhìn đứng giữa vườn.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v141a'", "BUILD = 'v142'")

# (1)
rep("cutAt(PV[m].cx, PV[m].cz); } STROKE = null; }", "cutAt(...tapXZ(m)); } STROKE = null; }")
rep("for (const m of CLM) waterAt(PV[m].cx, PV[m].cz, 0); STROKE = null; }", "for (const m of CLM) waterAt(...tapXZ(m), 0); STROKE = null; }")
rep("function cutAt(x, z){", "function tapXZ(m){ const b = PL[m].b; return ST.pairs && ST.pairs[m] ? [(b[0] + b[2]) / 2, (b[1] + b[3]) / 2] : [PV[m].cx, PV[m].cz]; }   /* v142: cây trái 2 ô thì chạm theo ô chủ, tâm cây nằm trên ranh */\nfunction cutAt(x, z){")

# (2)
rep('<div class="sic"><img src="${UIC.task}" alt=""></div><div class="sn"><b>Bù nhìn rơm</b>', '<div class="sic"><img src="${UIC.dc_bu_nhin}" alt=""></div><div class="sn"><b>Bù nhìn rơm</b>')
rep("buyFx(b, UIC.task, 'Bù nhìn đứng gác vườn', BUNHIN.price)", "buyFx(b, UIC.dc_bu_nhin, 'Bù nhìn đứng gác vườn', BUNHIN.price)")

# (3) mùa nước nổi tháng 8-11
rep("const NN_ON = false;   // mùa nước nổi chưa làm", "const nnOn = () => { const m = new Date().getMonth() + 1; return m >= 8 && m <= 11; };   // v142: mùa nước nổi theo lịch thật, tháng 8 tới hết tháng 11")
rep("(f.mua === 'nn' ? NN_ON : f.mua === muaSong())", "(f.mua === 'nn' ? nnOn() : f.mua === muaSong())", 2)
rep("if (f.mua === 'nn' && !NN_ON && !got)", "if (f.mua === 'nn' && !nnOn() && !got)")
assert 'NN_ON' not in s

# (2) bỏ hàng bù nhìn 150 xu khỏi tab Mua
a = s.find('    if ((ST.lv || 1) >= NB2.lv) h += `<div class="srow"><div class="sic"><img src="${UIC.dc_bu_nhin}"'); assert a > 0
b = s.find('</button></div>`;\n', a) + len('</button></div>`;\n'); assert 'data-a="buybn"' in s[a:b] and s[a:b].count('srow') == 1
s = s[:a] + s[b:]
assert s.count('data-a="buybn"') == 0 and s.count('bunhinSync(); }') + s.count('function bunhinSync') >= 1

# (4) cá linh 3-5 con một lần câu
rep("const nGot = k === 'tep' ? 3 + Math.floor(Math.random() * 3) : 1;", "const nGot = k === 'tep' || k === 'linh' ? 3 + Math.floor(Math.random() * 3) : 1;   /* v142: cá linh đi bầy như tép */")

# (5) Ngoại cho 5 nắm cơm nguội mỗi ngày thay vì 2 (anh Ares 13/11: 9 loài cá ăn cơm, 2 nắm không đủ số lần câu)
rep("M.com = Math.max(M.com || 0, 2); }", "M.com = Math.max(M.com || 0, 5); }   /* v142: 2 -> 5 nắm */")
# (6) Kho đầy mà đã mở Bến bà con thì Ngoại nhắc luôn lối đem hàng ra Bến (bài học Hay Day: kho chật đẩy người chơi đi bán)
rep("'Kho chật rồi. Mình bán bớt rồi hái tiếp.', 'lo', { now: true }); KFT = now;",
    "((ST.lv || 1) >= CNX.lv ? 'Kho chật rồi. Mình bán bớt, hay bày ra Bến bà con rồi hái tiếp.' : 'Kho chật rồi. Mình bán bớt rồi hái tiếp.'), 'lo', { now: true }); KFT = now;")
rep("u >= cp ? 'Kho đầy rồi, ra chợ bán bớt hay mua thêm lu' :",
    "u >= cp ? ((ST.lv || 1) >= CNX.lv ? 'Kho đầy rồi. Bán bớt ở chợ, bày ra Bến bà con hay mua thêm lu' : 'Kho đầy rồi, ra chợ bán bớt hay mua thêm lu') :")
rep('"Kho chật rồi. Mình bán bớt rồi hái tiếp.": "Storage is full. Let\'s sell some, then keep picking.", ',
    '"Kho chật rồi. Mình bán bớt rồi hái tiếp.": "Storage is full. Let\'s sell some, then keep picking.", "Kho chật rồi. Mình bán bớt, hay bày ra Bến bà con rồi hái tiếp.": "Storage is full. Sell some, or lay goods out at the Neighbours\' pier, then keep picking.", "Kho đầy rồi. Bán bớt ở chợ, bày ra Bến bà con hay mua thêm lu": "Storage is full. Sell at the market, lay goods out at the Neighbours\' pier, or buy more jars", ')
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
