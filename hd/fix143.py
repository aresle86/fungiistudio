# v143: giữ người chơi mới (anh Ares duyệt 13/11).
# (1) Cấp 1-4: lứa nào gieo cũng chín nhanh (cờ p.fast sẵn có, trước chỉ lứa đầu mỗi giống), kể cả đợt ra lại. Từ cấp 5 về bình thường.
# (2) Quét lá, bắt sâu: +3 kinh nghiệm (trước +1).
# (3) Củi vẫn phải lụm nhưng ra đều hơn: chưa nhóm bếp 3 phút một bó, nhóm rồi 6 phút (trước 15 phút).
# (4) Hai món rau cho bếp cấp 4: Cải xanh xào (3 cải, 1 hành, 1 củi; 5 phút; 50 xu), Rau muống luộc (4 rau muống, 1 củi; 4 phút; 35 xu).
import sys
ICONS = "  icon('caixao', p => { dia(p); for (let k = 0; k < 11; k++){ const a2 = k * 1.7, r2 = .04 + (k % 4) * .05; const l = add(p, new T.CylinderGeometry(.09, .09, .02, 7), ['#3F8F35', '#5FAE3F', '#2F7A33'][k % 3], Math.cos(a2) * r2, -.07 + k * .012, Math.sin(a2) * r2 * .8, [R(-.45, .45), R(0, 3), R(-.45, .45)]); l.scale.set(1.3, 1, .65); } for (let k = 0; k < 6; k++) add(p, new T.BoxGeometry(.13, .03, .045), '#EEF4D4', R(-.2, .2), -.03 + R(0, .08), R(-.15, .15), [R(-.3, .3), R(0, 3), R(-.3, .3)]); for (let k = 0; k < 9; k++) add(p, new T.BoxGeometry(.03, .012, .022), pick(['#E3A23A', '#C9822A']), R(-.2, .2), .07 + R(0, .03), R(-.15, .15), [0, R(0, 3), 0]); });\n  icon('rmluoc', p => { dia(p); for (let k = 0; k < 9; k++){ const y2 = -.07 + k * .014; add(p, new T.TorusGeometry(R(.12, .2), .016, 4, 10, R(2.2, 3.4)), k % 3 ? '#5FA83E' : '#86C25A', -.06 + R(-.07, .07), y2, R(-.05, .05), [Math.PI / 2 + R(-.15, .15), 0, R(0, 6.28)]); } for (let k = 0; k < 7; k++){ const l = add(p, new T.ConeGeometry(.035, .16, 3), '#2F7F33', -.06 + R(-.2, .2), .03 + R(0, .04), R(-.16, .16), [Math.PI / 2, R(0, 3), R(-.3, .3)]); l.scale.set(1, 1, .4); } add(p, new T.CylinderGeometry(.11, .07, .07, 10), '#FBF7EE', .25, -.05, .14); add(p, new T.CylinderGeometry(.095, .095, .012, 10), '#B86A2A', .25, -.012, .14); add(p, new T.TorusGeometry(.025, .01, 3, 7), '#E8453A', .23, -.002, .13, [Math.PI / 2, 0, 0]); add(p, new T.TorusGeometry(.022, .01, 3, 7), '#E8453A', .28, -.002, .16, [Math.PI / 2, 0, 0]); });\n"
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v142'", "BUILD = 'v143'")

# (1) chín nhanh ở cấp 1-4
rep("if (!c.tree && !ST.fg[k]){ ST.fg[k] = 1; p.fast = 1; }", "if (!c.tree && (!ST.fg[k] || (ST.lv || 1) <= 4)){ ST.fg[k] = 1; p.fast = 1; }   /* v143: cấp 1-4 lứa nào cũng chín nhanh */")
rep("if (left > 0){ p.cut = (p.cut || 0) + 1; p.g = c.grow - c.re;", "if (left > 0){ p.cut = (p.cut || 0) + 1; p.g = c.grow - c.re; if (!c.tree && (ST.lv || 1) <= 4) p.fast = 1;")

# (2) quét lá, bắt sâu +3 kinh nghiệm
rep("sfx('pop'); buzz(12); gainXP(1); bump('odd');", "sfx('pop'); buzz(12); gainXP(o.k === 'la' || o.k === 'sau' ? 3 : 1); bump('odd');")

# (3) củi ra đều hơn
rep("cui: { lv: 4, max: 3, every: 15 * 60, name: 'Nhặt củi' }", "cui: { lv: 4, max: 3, every: (ST.bep && ST.bep.lit ? 6 : 3) * 60, name: 'Nhặt củi' }")

# (4) hai món rau
rep("  canhchua: { name: 'Canh chua', sell: 105,",
    "  caixao: { name: 'Cải xanh xào', sell: 50, unit: 'dĩa', lv: 4, in: { cai: 3, hanh: 1, cui: 1 }, t: 5 * 60, story: 'Cải xanh xào lửa lớn với hành, vừa chín tới là nhắc xuống liền cho còn giòn. Cơm nhà quê chỉ vậy mà hết nồi.' },\n"
    "  rmluoc: { name: 'Rau muống luộc', sell: 35, unit: 'dĩa', lv: 4, in: { raumuong: 4, cui: 1 }, t: 4 * 60, story: 'Rau muống luộc chấm nước mắm ớt. Nước luộc để nguội chan cơm cũng ngọt. Một bó rau mà được hai món đó con.' },\n"
    "  canhchua: { name: 'Canh chua', sell: 105,")
rep("  icon('chuoimat', p => { dia(p);", ICONS + "  icon('chuoimat', p => { dia(p);")
rep('"trungchien": "Scallion omelette",', '"trungchien": "Scallion omelette", "caixao": "Stir-fried mustard greens", "rmluoc": "Boiled water spinach",')
rep('"Trứng gà ta chiên với hành lá, rưới chút nước mắm.', '"Cải xanh xào lửa lớn với hành, vừa chín tới là nhắc xuống liền cho còn giòn. Cơm nhà quê chỉ vậy mà hết nồi.": "Mustard greens tossed over high heat with green onion, off the fire the moment they are done so they stay crisp. That is all a country meal needs to empty the rice pot.", "Rau muống luộc chấm nước mắm ớt. Nước luộc để nguội chan cơm cũng ngọt. Một bó rau mà được hai món đó con.": "Boiled water spinach dipped in chili fish sauce. The cooled broth is sweet over rice too. One bunch of greens, two dishes, dear.", "Trứng gà ta chiên với hành lá, rưới chút nước mắm.')

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
