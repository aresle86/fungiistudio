# nm116: thêm món phơi, sấy, muối từ rau cá đã có trong vườn. python3 nm116.py vào ra
#  Nong phơi: trà khổ qua (9), tép phơi (10), bắp phơi (11), khô cá lóc (14)
#  Lò sấy: ổi sấy dẻo (11), chuối sấy giòn (13), khế sấy (14)
#  Khạp muối: mắm tép (12), mắm cá linh (15, cá linh chỉ có mùa nước nổi)
#  Giá: khoảng 1,45 lần giá đồ tươi bỏ vô, giống các món cũ.
import sys, json
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:80], s.count(a))
    s = s.replace(a, b)

PHOI = {
 'trakhoqua': ("Trà khổ qua", 'bịch', 9, {'khoqua': 3}, 5, 110, 'Khổ qua xắt lát mỏng phơi ba nắng, nấu nước uống mát trong người. Sáng nào Ngoại cũng uống một ly.'),
 'tepphoi': ("Tép phơi", 'bịch', 10, {'tep': 6, 'muoi': 1}, 4, 75, 'Tép bạc luộc sơ rồi phơi, để dành rang mặn hay nấu canh bí đao.'),
 'bapphoi': ("Bắp phơi", 'bịch', 11, {'bap': 3}, 6, 140, 'Bắp già lột vỏ phơi giòn hột, để dành nấu chè bắp hay rang ăn chơi.'),
 'khocaloc': ("Khô cá lóc", 'xâu', 14, {'caloc': 2, 'muoi': 1}, 8, 135, 'Cá lóc xẻ bướm ướp muối phơi một nắng. Nướng than ăn với xoài băm, ai đi xa cũng nhớ.'),
}
SAY = {
 'oisay': ("Ổi sấy dẻo", 'bịch', 11, {'oi': 5}, 6, 110, 'Ổi xá lị xắt miếng sấy dẻo, chua chua ngọt ngọt, tụi nhỏ ăn hoài không chán.'),
 'chuoisay': ("Chuối sấy giòn", 'bịch', 13, {'chuoi': 2, 'duong': 1}, 6, 135, 'Chuối xiêm xắt lát mỏng, rim chút đường rồi sấy giòn rụm.'),
 'khesay': ("Khế sấy", 'bịch', 14, {'khe': 6}, 7, 105, 'Khế ngọt xắt lát hình ngôi sao sấy khô, nhìn đẹp như bánh kẹo Tết.'),
}
MUOI = {
 'mamtep': ("Mắm tép", 'hũ', 12, {'tep': 8, 'muoi': 2}, 18, 55, 'Tép bạc trộn muối với thính, ủ trong khạp đủ ngày. Chưng với thịt ba rọi, ăn cơm nóng là hết nồi.'),
 'mamcalinh': ("Mắm cá linh", 'hũ', 15, {'linh': 6, 'muoi': 2}, 24, 70, 'Mùa nước nổi cá linh về đầy đồng, Ngoại làm mắm để dành ăn cả năm.'),
}
def js(D, out=0):
    xs = []
    for k, (n, u, lv, i, h, sell, st) in D.items():
        sell_js = str(sell) if sell else "Math.round(CROPS.bap.sell * 4 * 1.45 / 5) * 5"
        xs.append(f"{k}: {{ name: '{n}', unit: '{u}', lv: {lv}, in: {json.dumps(i)}, t: {h} * 3600, sell: {sell_js}{', out: 2' if out else ''}, story: '{st}' }}")
    return '{ ' + ', '.join(xs) + ' }'
rep("story: 'Cọng lục bình phơi khô để đan giỏ, đan đệm. Ngoại ngồi hiên đan cho con coi.' } };",
    "story: 'Cọng lục bình phơi khô để đan giỏ, đan đệm. Ngoại ngồi hiên đan cho con coi.' } }; Object.assign(PHOI, " + js(PHOI) + ");")
rep("story: 'Giỏ lục bình đan tay, đem ra chợ nổi bán cho khách phương xa.' } };",
    "story: 'Giỏ lục bình đan tay, đem ra chợ nổi bán cho khách phương xa.' } }; { const G0 = SAY.gio; delete SAY.gio; Object.assign(SAY, " + js(SAY) + "); SAY.gio = G0; }")
i = s.find("const MUOI = {"); j = s.find("} };", i) + 4
s = s[:j] + " Object.assign(MUOI, " + js(MUOI, 1) + ");" + s[j:]
rep("const SAYR = { mutkhe: SAY.mutkhe,", "const SAYR = { mutkhe: SAY.mutkhe, oisay: SAY.oisay, chuoisay: SAY.chuoisay, khesay: SAY.khesay,")
rep("otkho: 'giã muối ớt',", "otkho: 'giã muối ớt', trakhoqua: 'pha trà uống', tepphoi: 'rang mặn', bapphoi: 'nấu chè bắp', khocaloc: 'nướng than', oisay: 'cho tụi nhỏ ăn vặt', chuoisay: 'cho tụi nhỏ ăn vặt', khesay: 'bày mâm Tết', mamtep: 'chưng thịt ba rọi', mamcalinh: 'kho với thịt',")
# hình trên nong lúc phơi
rep("  else if (t.k === 'chuoiphoi') for", """  else if (t.k === 'trakhoqua') for (let k = 0; k < 12; k++){ const a = rnd() * 6.28, r = Math.sqrt(rnd()) * .12; M(new T.TorusGeometry(.018, .007, 3, 8), mix('#7FB04A', '#9A9A5A'), Math.cos(a) * r, .01, Math.sin(a) * r, { r: [Math.PI / 2, 0, 0], cast: false }); }
  else if (t.k === 'tepphoi') for (let k = 0; k < 18; k++){ const a = rnd() * 6.28, r = Math.sqrt(rnd()) * .12; M(new T.CapsuleGeometry(.007, .02, 2, 4), mix('#F0C8B0', '#E0805A'), Math.cos(a) * r, .01, Math.sin(a) * r, { r: [Math.PI / 2, R(0, 3), 0], cast: false }); }
  else if (t.k === 'bapphoi') for (let k = 0; k < 30; k++){ const a = rnd() * 6.28, r = Math.sqrt(rnd()) * .13; M(sph(.011, 4, 3), mix('#F2D24A', '#E0A82A'), Math.cos(a) * r, .01, Math.sin(a) * r, { cast: false }); }
  else if (t.k === 'khocaloc') for (let k = 0; k < 2; k++){ M(sph(.05, 7, 5), mix('#8A8A6A', '#9A6E3A'), (k - .5) * .1, .01, 0, { s: [2.4, .2, .9], r: [0, .3, 0], cast: false }); }
  else if (t.k === 'chuoiphoi') for""")
# hình món
rep("  icon('lucbinhkho', p =>", """  icon('trakhoqua', p => { add(p, new T.BoxGeometry(.42, .5, .22), '#E3D3B0', 0, -.04, 0); add(p, new T.BoxGeometry(.44, .06, .24), '#C9B27A', 0, .22, 0); for (let k = 0; k < 5; k++) add(p, new T.TorusGeometry(.06, .022, 4, 10), k % 2 ? '#6E9F3A' : '#86B84A', -.14 + k * .07, .3 + (k % 2) * .03, 0, [R(-.3, .3), 0, R(0, 1)]); }, V(.3, .3, 1));
  icon('tepphoi', p => { add(p, new T.BoxGeometry(.42, .5, .22), '#E3D3B0', 0, -.04, 0); add(p, new T.BoxGeometry(.3, .2, .01), '#F5ECD6', 0, -.05, .115); for (let k = 0; k < 9; k++) add(p, new T.CapsuleGeometry(.025, .07, 2, 5), k % 2 ? '#E8906A' : '#F0B090', R(-.14, .14), .3 + R(0, .06), R(-.05, .05), [R(0, 3), 0, R(0, 3)]); }, V(.3, .3, 1));
  icon('bapphoi', p => { add(p, new T.BoxGeometry(.42, .5, .22), '#E3D3B0', 0, -.04, 0); for (let k = 0; k < 16; k++) add(p, new T.SphereGeometry(.035, 5, 4), k % 3 ? '#F2C83A' : '#E8A82A', R(-.15, .15), .27 + R(0, .06), R(-.06, .06)); }, V(.3, .3, 1));
  icon('khocaloc', p => { p.rotation.set(.6, 0, 0); for (const [z, x] of [[-.12, -.02], [.1, .03]]){ const g = new T.Group(); g.position.set(x, 0, z); p.add(g); add(g, new T.SphereGeometry(.15, 8, 6), '#9A7448', 0, 0, 0, null, [2.3, .13, .8]); add(g, new T.ConeGeometry(.08, .12, 4), '#7A5A34', -.38, 0, 0, [0, 0, -Math.PI / 2], [1, 1, .2]); add(g, new T.SphereGeometry(.016, 5, 4), '#2A1A10', .26, .02, .035); } add(p, new T.CylinderGeometry(.008, .008, .5, 4), '#B48560', .32, .02, 0, [Math.PI / 2, 0, 0]); });
  icon('oisay', p => { add(p, new T.BoxGeometry(.5, .56, .08), '#F4EEDD', 0, -.04, 0); add(p, new T.BoxGeometry(.34, .32, .01), '#C8E0A0', 0, -.06, .045); for (let k = 0; k < 3; k++) blob(p, .09, k % 2 ? '#F2C8C0' : '#E8F0C8', -.1 + k * .1, -.04, .06, [1.3, .8, .2]); add(p, new T.BoxGeometry(.52, .05, .09), '#86B06A', 0, .24, 0); }, V(.2, .2, 1));
  icon('chuoisay', p => { add(p, new T.BoxGeometry(.5, .56, .08), '#F4EEDD', 0, -.04, 0); for (let k = 0; k < 7; k++) add(p, new T.CylinderGeometry(.06, .06, .015, 10), k % 2 ? '#E8C060' : '#F2D27A', R(-.15, .15), R(-.2, .08), .05, [Math.PI / 2, 0, 0]); add(p, new T.BoxGeometry(.52, .05, .09), '#E3B23C', 0, .24, 0); }, V(.2, .2, 1));
  icon('khesay', p => { add(p, new T.BoxGeometry(.5, .56, .08), '#F4EEDD', 0, -.04, 0); for (let k = 0; k < 3; k++){ const s2 = new T.Shape(); for (let j = 0; j < 10; j++){ const a = j / 10 * 6.28, r = j % 2 ? .045 : .1; j ? s2.lineTo(Math.cos(a) * r, Math.sin(a) * r) : s2.moveTo(r, 0); } add(p, new T.ExtrudeGeometry(s2, { depth: .015, bevelEnabled: false }), k % 2 ? '#E8B83A' : '#F2CC5A', -.12 + k * .12, -.08 + (k % 2) * .1, .05, [0, 0, k]); } add(p, new T.BoxGeometry(.52, .05, .09), '#C9A66B', 0, .24, 0); }, V(.2, .2, 1));
  icon('lucbinhkho', p =>""")
rep("icon('mutkhe', p => { hu(p, '#F2C94A');", """icon('mamtep', p => { hu(p, '#D88A6A'); for (let k = 0; k < 4; k++) add(p, new T.CapsuleGeometry(.02, .05, 2, 4), '#E8906A', -.1 + k * .07, .22, R(-.05, .05), [0, 0, R(0, 3)]); });   icon('mamcalinh', p => { hu(p, '#B89A60'); for (let k = 0; k < 3; k++) add(p, new T.SphereGeometry(.05, 6, 4), '#D8D8C8', -.08 + k * .08, .22, 0, null, [1.8, .5, .6]); });   icon('mutkhe', p => { hu(p, '#F2C94A');""")
open(dst, 'w', encoding='utf-8').write(s)

EN = {
 'Khổ qua xắt lát mỏng phơi ba nắng, nấu nước uống mát trong người. Sáng nào Ngoại cũng uống một ly.': 'Bitter melon sliced thin and sun-dried for three days, brewed into a cooling tea. Grandma drinks a cup every morning.',
 'Tép bạc luộc sơ rồi phơi, để dành rang mặn hay nấu canh bí đao.': 'Tiny shrimp blanched and sun-dried, saved for salty stir-fries or winter melon soup.',
 'Bắp già lột vỏ phơi giòn hột, để dành nấu chè bắp hay rang ăn chơi.': 'Mature corn husked and sun-dried until the kernels crunch, saved for corn pudding or roasting.',
 'Cá lóc xẻ bướm ướp muối phơi một nắng. Nướng than ăn với xoài băm, ai đi xa cũng nhớ.': 'Snakehead butterflied, salted and dried one sunny day. Grilled over charcoal with shredded mango, everyone far from home misses it.',
 'Ổi xá lị xắt miếng sấy dẻo, chua chua ngọt ngọt, tụi nhỏ ăn hoài không chán.': 'Guava sliced and dried soft, sweet and tangy. The kids never tire of it.',
 'Chuối xiêm xắt lát mỏng, rim chút đường rồi sấy giòn rụm.': 'Thin slices of banana glazed with a little sugar and dried crisp.',
 'Khế ngọt xắt lát hình ngôi sao sấy khô, nhìn đẹp như bánh kẹo Tết.': 'Sweet starfruit cut into stars and dried, pretty as Tết candy.',
 'Tép bạc trộn muối với thính, ủ trong khạp đủ ngày. Chưng với thịt ba rọi, ăn cơm nóng là hết nồi.': 'Tiny shrimp mixed with salt and toasted rice, aged in the jar. Steamed with pork belly, a whole pot of rice disappears.',
 'Mùa nước nổi cá linh về đầy đồng, Ngoại làm mắm để dành ăn cả năm.': 'In the flood season linh fish fill the fields, and Grandma ferments them to last the whole year.',
 'pha trà uống': 'to brew tea', 'rang mặn': 'for a salty stir-fry', 'nấu chè bắp': 'for corn pudding', 'nướng than': 'to grill', 'chưng thịt ba rọi': 'to steam with pork belly', 'kho với thịt': 'to braise with pork',
}
json.dump(EN, open('i18n/en_v116n.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('ok', len(s))
