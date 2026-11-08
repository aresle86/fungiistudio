# gieng120: giếng cần vọt -> giếng khoan bơm tay đúng kiểu miền Tây (anh Ares 8/11: "người miền Tây khoan giếng để có nước
# sinh hoạt"). Chạy sau dish120.py. Thay mô hình, tên món, lời Ngoại (Việt + Anh).
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a))
    s = s.replace(a, b)

NEW = r"""  gieng(){ // giếng khoan bơm tay miền Tây: nền gạch tàu có rãnh thoát nước; bệ xi măng có gờ, ống khoan sắt, cây bơm tay gang sơn xanh, cần bơm dài ra sau, vòi chảy xuống thau nhôm; xô nhựa đỏ, gáo nhựa, ghế đẩu nhựa ngồi giặt; lu da lươn chứa nước, thau đồ giặt, chuối và môn nước sát bờ
    const TILE = ['#B5634C', '#A85A44', '#C06E54', '#AE5E48'].map(c => MS(c, { roughness: .9 })), XM = MS('#BDB7A6', { roughness: .95 }), XM2 = MS('#A9A392', { roughness: .95 }), REU = MS('#5E8F48'), XANH = MS('#3F7F5C', { roughness: .55, metalness: .2 }), XANHD = MS('#2F6347', { roughness: .55, metalness: .2 }), SAT = MS('#5A5F63', { roughness: .6, metalness: .3 }), NHOM = '#C4C6C2';
    for (let c = 0; c < 6; c++) for (let r = 0; r < 5; r++){ const x = -.72 + c * .25, z = -.48 + r * .25; if ((c === 0 || c === 5) && (r === 0 || r === 4)) continue; M(box(.24, .025, .24), TILE[(c * 3 + r * 5) % 4], x, .0125, z, { cast: false }); } M(box(.05, .012, .72), '#6E5A44', .55, .027, .08, { cast: false }); M(box(.62, .012, .05), '#6E5A44', .25, .027, .44, { cast: false });
    // bệ xi măng: mặt bệ, gờ bốn phía (hở một khe bên phải cho nước chảy ra rãnh), lớp nước mỏng, rêu chân bệ
    const BX = -.25, BZ = -.08, BW = .72, BD = .66, BH = .07; M(box(BW, BH, BD), XM, BX, .025 + BH / 2, BZ); const TOP = .025 + BH;
    M(box(BW, .05, .05), XM2, BX, TOP + .025, BZ - BD / 2 + .025); M(box(BW, .05, .05), XM2, BX, TOP + .025, BZ + BD / 2 - .025); M(box(.05, .05, BD - .1), XM2, BX - BW / 2 + .025, TOP + .025, BZ);
    M(box(.05, .05, .36), XM2, BX + BW / 2 - .025, TOP + .025, BZ - .1); M(box(.05, .05, .1), XM2, BX + BW / 2 - .025, TOP + .025, BZ + BD / 2 - .1);
    for (const [x, z, w, d] of [[-.33, .1, .3, .2], [-.12, .13, .2, .1], [.02, .13, .2, .07]]) M(box(w, .004, d), MS('#8F8B7E', { roughness: .4 }), x, TOP + .003, z, { cast: false }); M(box(.16, .004, .07), water, BX + BW / 2 + .03, .03, BZ + .13, { cast: false });   /* mặt bệ khô, chỉ sẫm ướt quanh thau và vệt chảy ra khe */
    for (let i = 0; i < 12; i++){ const t = i / 12, side = i % 4, x = side < 2 ? BX - BW / 2 + t * BW * 4 % BW : BX + (side === 2 ? -1 : 1) * BW / 2, z = side < 2 ? BZ + (side ? 1 : -1) * BD / 2 : BZ - BD / 2 + t * BD * 4 % BD; M(ico(.028, 0), REU, x, .04, z, { s: [1.5, .5, .7], cast: false }); }
    // cây bơm tay: ống khoan, bích nối, thân bơm có đai, nắp, vòi, cần bơm, tay nắm cao su
    const PX = BX - .08, PZ = BZ - .16; M(cyl(.038, .038, .1, 8), SAT, PX, TOP + .05, PZ); M(cyl(.068, .068, .022, 10), SAT, PX, TOP + .1, PZ); for (let i = 0; i < 4; i++) M(cyl(.008, .008, .03, 4), '#3A3F44', PX + Math.cos(i * 1.57 + .78) * .055, TOP + .11, PZ + Math.sin(i * 1.57 + .78) * .055, { cast: false });
    const B0 = TOP + .11, B1 = B0 + .36; M(cyl(.058, .064, B1 - B0, 10), XANH, PX, (B0 + B1) / 2, PZ); for (const y of [B0 + .03, B1 - .03]) ring(.064, .009, PX, y, PZ, '#2F6347'); M(cyl(.074, .068, .035, 10), XANHD, PX, B1 + .017, PZ); M(sph(.05, 8, 5, 0, 6.283, 0, Math.PI / 2), XANH, PX, B1 + .035, PZ, { s: [1, .55, 1] });
    lim([PX, B1 - .1, PZ + .04], [PX, B1 - .12, PZ + .2], .026, .022, XANH); lim([PX, B1 - .12, PZ + .2], [PX, B1 - .17, PZ + .23], .022, .02, XANH); ring(.02, .006, PX, B1 - .175, PZ + .232, '#2F6347');
    for (const sx of [-1, 1]) M(box(.01, .07, .04), XANHD, PX + sx * .028, B1 + .07, PZ - .045); M(cyl(.007, .007, .07, 5), '#3A3F44', PX, B1 + .09, PZ - .045, { r: [0, 0, hz] });
    lim([PX, B1 + .09, PZ - .045], [PX, B1 + .25, PZ - .47], .016, .013, XANHD); lim([PX, B1 + .232, PZ - .42], [PX, B1 + .26, PZ - .5], .022, .022, '#2A2A2A'); lim([PX, B1 + .08, PZ - .02], [PX, B1 + .035, PZ + .005], .009, .009, '#3A3F44');
    // dòng nước từ vòi xuống thau nhôm, gợn nước
    const TX = PX, TZ = PZ + .26; M(lathe([[0, 0], [.1, 0], [.14, .07], [.15, .075], [.135, .075], [.095, .012], [0, .012]], 13), NHOM, TX, TOP, TZ, { ds: true }); M(cyl(.128, .128, .006, 13), water, TX, TOP + .058, TZ, { cast: false });
    lim([PX, B1 - .18, PZ + .235], [TX, TOP + .06, TZ + .005], .011, .014, '#A9D8E8'); for (const r of [.04, .085]) ring(r, .004, TX, TOP + .063, TZ, '#BFE0EA'); spark(TX + .05, TOP + .1, TZ + .03, .09);
    // xô nhựa đỏ có quai, gáo nhựa xanh, ghế đẩu nhựa
    { const x = BX + .2, z = BZ - .17; M(lathe([[0, 0], [.072, 0], [.092, .17], [.085, .17], [.068, .012], [0, .012]], 12), '#C8443A', x, TOP, z, { ds: true }); ring(.09, .007, x, TOP + .17, z, '#A8342C'); M(cyl(.083, .083, .006, 12), water, x, TOP + .14, z, { cast: false }); M(new T.TorusGeometry(.09, .004, 3, 10, Math.PI), '#8A8A86', x, TOP + .17, z, { r: [0, .5, 0], cast: false }); }
    { const x = BX + .22, z = BZ + .15, g0 = G(x, TOP + .012, z, .7, ROOT); M(sph(.045, 8, 4, 0, 6.283, Math.PI / 2, Math.PI / 2), '#3F7FC0', 0, .04, 0, { p: g0, ds: true }); lim([.04, .03, 0], [.13, .06, 0], .008, .007, '#3F7FC0', g0); }
    { const x = BX + .02, z = BZ + .2, y = TOP + .13; M(box(.13, .014, .13), '#3D8FC4', x, y, z); for (const [dx, dz] of [[-1, -1], [1, -1], [-1, 1], [1, 1]]) lim([x + dx * .052, y, z + dz * .052], [x + dx * .062, TOP, z + dz * .062], .011, .011, '#3D8FC4'); }
    // lu da lươn chứa nước, nắp gỗ, gáo dừa
    { const lx = .3, lz = .28; M(lathe([[0, 0], [.09, 0], [.135, .12], [.11, .22], [.065, .25], [.075, .27], [0, .27]], 11), '#6E4126', lx, .02, lz); for (const y of [.1, .17]) ring(.128 - (y - .1) * .08, .006, lx, .02 + y, lz, '#C9952A'); M(cyl(.072, .072, .012, 9), '#8A5D3B', lx, .295, lz); M(sph(.05, 8, 5, 0, 6.283, Math.PI / 2, Math.PI / 2), '#5A3A22', lx, .35, lz, { ds: true, cast: false }); lim([lx, .32, lz], [lx + .16, .345, lz + .1], .008, .008, C.bamboo); }
    // thau đồ giặt, cục xà bông
    M(lathe([[0, 0], [.09, 0], [.13, .06], [.14, .065], [.125, .065], [.085, .012], [0, .012]], 13), NHOM, -.12, .026, .44, { ds: true }); for (const [x, z, c] of [[-.15, .43, '#3F6FA8'], [-.09, .47, '#EDE6D6'], [-.12, .4, '#C2473A']]) M(box(.09, .022, .07), c, x, .062, z, { r: [0, x * 8, 0], cast: false }); M(box(.05, .018, .03), '#E8D27A', .05, .034, .45, { cast: false });
    // chuối và môn nước
    { const g0 = G(-.66, 0, -.42, .6, ROOT); lim([0, 0, 0], [.02, .5, 0], .055, .04, '#7A9A4A', g0); for (let i = 0; i < 6; i++){ const h = G(.02, .5, 0, i * 1.05, g0); h.rotation.z = .35 + (i % 2) * .3; M(box(.42, .007, .13), i % 2 ? '#4F8A44' : '#5E9A4E', .2, 0, 0, { p: h }); M(box(.42, .009, .012), '#8FBE6A', .2, .006, 0, { p: h, cast: false }); } }
    { const cx = .62, cz = -.2; for (let i = 0; i < 6; i++){ const a = i * 1.05, h = .1 + (i % 3) * .05; lim([cx, .02, cz], [cx + Math.cos(a) * .07, h + .03, cz + Math.sin(a) * .07], .007, .005, '#7FAE5A'); M(ico(.055, 0), i % 2 ? '#3F7A3A' : '#4F8A44', cx + Math.cos(a) * .1, h + .06, cz + Math.sin(a) * .1, { s: [1.3, .28, 1], r: [.4, -a, 0], cast: false }); } } tuft(-.62, .3, 5); tuft(.42, -.4, 5);
    // rau má: lá tròn nhỏ như đồng xu trên cọng mảnh, mọc từng đám chỗ ẩm (chân bệ, khe nước chảy ra rãnh, chân lu, gần thau giặt)
    const RM = ['#4E9A3E', '#5DAA48', '#6BB652', '#47903A'].map(c => MS(c, { roughness: .7 })); const rauMa = (cx, cz, n, w = .09) => { for (let i = 0; i < n; i++){ const x = cx + R(-w, w), z = cz + R(-w * .7, w * .7), h = R(.03, .085), r = R(.034, .05); lim([x, .026, z], [x + R(-.01, .01), h, z + R(-.01, .01)], .003, .003, '#7FAE5A'); M(cyl(r, r, .005, 9), pick(RM), x, h + .002, z, { r: [R(-.35, .35), R(0, 3), R(-.35, .35)], cast: false }); } };
    rauMa(.2, .06, 9, .07); rauMa(-.63, -.05, 8, .07); rauMa(-.4, .33, 8, .07); rauMa(.42, .37, 6, .05); rauMa(-.02, -.47, 5, .06); },
"""
i = s.index("  gieng(){ // giếng cần vọt"); j = s.index("  choi_la(){", i)
assert s.count("  gieng(){ // giếng cần vọt") == 1
s = s[:i] + NEW + s[j:]

OLD_SAY = 'Giếng cần vọt! Nhỏ xíu Ngoại đã kéo cần này, đá dằn nặng mà gàu lên nhẹ hều.'
NEW_SAY = 'Giếng khoan! Hồi đó cả xóm xài chung một cây bơm, sáng sớm xếp hàng bơm nước về đổ lu. Giờ nhà mình có riêng rồi con.'
rep("gieng: '" + OLD_SAY + "'", "gieng: '" + NEW_SAY + "'")
rep('"' + OLD_SAY + '": "A sweep well! I pulled one as a tiny girl. Heavy stone, but the bucket comes up light as air."',
    '"' + NEW_SAY + '": "A tube well! Back then the whole hamlet shared one pump, queuing at dawn to fill our jars. Now we have our own, dear."')
rep("name: 'Giếng cần vọt'", "name: 'Giếng khoan bơm tay'")
rep('"Giếng cần vọt": "Sweep well"', '"Giếng khoan bơm tay": "Hand-pump well"')
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
