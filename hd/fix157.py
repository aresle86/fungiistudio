# v156 -> v157: bao hạt lạ (túi mù). Bước 1: hình bao vẽ bằng code.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), n, a[:60])
    s = s.replace(a, b)

rep("BUILD = 'v156'", "BUILD = 'v157'")
BAO = r"""shot('baola', () => { const g = G(0, 0, 0), MM = {}, X = c => MM[c] || (MM[c] = new T.MeshStandardMaterial({ color: c, flatShading: true, roughness: .85, side: T.DoubleSide }));   /* v157: bao hạt lạ, vải nhuộm chàm, cột kín miệng */
    const pf = [[0, 0], [.2, .006], [.3, .07], [.335, .2], [.32, .34], [.27, .46], [.17, .56], [.1, .61], [.1, .65], [.16, .71], [.22, .76], [.24, .775]].map(([r, y]) => new T.Vector2(r, y)), lg = new T.LatheGeometry(pf, 22), P = lg.attributes.position;
    for (let i = 0; i < P.count; i++){ const y = P.getY(i); if (y > .64){ const a = Math.atan2(P.getZ(i), P.getX(i)), k = 1 + Math.sin(a * 6) * .2 * (y - .64) / .135; P.setX(i, P.getX(i) * k); P.setZ(i, P.getZ(i) * k); P.setY(i, y + Math.sin(a * 6 + 1) * .03 * (y - .64) / .135); } }
    lg.computeVertexNormals(); M(lg, X('#3E7C8F'), 0, 0, 0, { p: g });
    for (const y of [.12, .22, .32, .42]){ const t = new T.TorusGeometry(.3 + (y < .3 ? .03 : -.01) - (y > .4 ? .03 : 0), .005, 3, 28); M(t, X('#2C5F70'), 0, y, 0, { p: g, r: [Math.PI / 2, 0, 0], cast: false }); }
    M(new T.CircleGeometry(.1, 14), X('#24495A'), 0, .66, 0, { p: g, r: [-Math.PI / 2, 0, 0] });
    M(new T.TorusGeometry(.11, .024, 6, 24), X('#C24A2E'), 0, .625, 0, { p: g, r: [Math.PI / 2, 0, 0] }); for (const sx of [-1, 1]){ M(new T.TorusGeometry(.055, .017, 5, 12), X('#C24A2E'), sx * .06, .635, .135, { p: g, r: [0, 0, sx * .5], s: [1, .7, 1] }); const e = M(cyl(.013, .013, .14, 5), X('#C24A2E'), sx * .04, .55, .14, { p: g }); e.rotation.z = sx * .35; } M(sph(.03, 6, 5), X('#9A3520'), 0, .635, .135, { p: g });   /* dây đỏ thắt nơ */
    M(new T.CylinderGeometry(.338, .338, .26, 16, 1, true, -.5, 1), X('#F5D27A'), 0, .25, 0, { p: g }); for (const y of [.374, .126]) M(new T.CylinderGeometry(.34, .34, .012, 16, 1, true, -.5, 1), X('#B9803F'), 0, y, 0, { p: g, cast: false });   /* nhãn vàng */
    M(new T.TorusGeometry(.045, .016, 5, 14, Math.PI * 1.5), X('#4A2F1E'), 0, .295, .343, { p: g, r: [0, 0, -Math.PI / 2], cast: false }); M(box(.03, .05, .012), X('#4A2F1E'), 0, .225, .343, { p: g, cast: false }); M(sph(.02, 6, 5), X('#4A2F1E'), 0, .165, .343, { p: g, s: [1, 1, .4], cast: false });   /* dấu hỏi */
    for (const [x, z, c] of [[.3, .24, '#E8C27A'], [.37, .13, '#8FCB4E'], [-.28, .26, '#C24A2E']]) M(sph(.028, 6, 4), X(c), x, .02, z, { p: g, s: [1, .55, .75] });   /* ba hạt ba màu */
  }, new T.Vector3(.45, .5, 1));
  shot('task',"""
rep("shot('task',", BAO)
# ---- v157: hình 5 giống quý mới, vẽ bằng code trong crop5 ----
END5 = "lfi(p, .5, .07, '#7AA858', .02, .2, -.12, [0, .2, -.6]); }, V(.2, .3, 1));\n  ri.renderLists.dispose(); return OUT; };"
QUY5 = r"""lfi(p, .5, .07, '#7AA858', .02, .2, -.12, [0, .2, -.6]); }, V(.2, .3, 1));
  // ---- MƯỚP HƯƠNG: trái thon dài, vỏ trơn xanh lợt, sọc mảnh xanh đậm ----
  shot('muophuong', p => { const pf = t => .095 * Math.pow(Math.sin(Math.PI * Math.min(1, .03 + t)), .4) * (1 - .22 * t) + .014;
    const mk = (x, y, z, rz, s, c) => { const g = new T.Group(); g.position.set(x, y, z); g.rotation.z = rz; p.add(g); add(g, fin(lathe(pf, 12, 12)), c, 0, -.42 * s, 0, null, [s, .84 * s, s]);
      for (let k = 0; k < 10; k++){ const a = k / 10 * 6.283 + .3; add(g, fin(tube([0, 1, 2, 3, 4, 5, 6, 7].map(i => { const t = .05 + i / 7 * .88, r = pf(t) * s; return V(Math.cos(a) * r, -.42 * s + t * .84 * s, Math.sin(a) * r); }), t => .0065 * s, 10, 4)), '#3F7A32'); }
      add(g, fin(tube([V(0, .42 * s, 0), V(.02, .49 * s, 0), V(.06, .54 * s, 0)], t => .015, 3, 5)), '#6E9A3A'); add(g, fin(new T.ConeGeometry(.06, .06, 5)), '#F2C83A', .08, .56 * s, 0, [0, 0, -.6]); };
    mk(-.12, .03, -.1, .6, 1, '#74B352'); mk(.13, -.03, .12, .3, .94, '#84C060'); }, V(.15, .25, 1));
  // ---- MÍA LAU: cây ốm, lóng dài, vỏ vàng xanh ----
  shot('mialau', p => { const cane = (x, z, rz, L, c) => { const g = new T.Group(); g.position.set(x, 0, z); g.rotation.z = rz; p.add(g); const n = 5; for (let i = 0; i < n; i++){ const y = -L / 2 + (i + .5) * L / n; add(g, fin(new T.CylinderGeometry(.04, .043, L / n - .01, 7)), c, 0, y, 0); add(g, fin(new T.CylinderGeometry(.047, .047, .016, 7)), '#8E9A40', 0, y + L / n / 2, 0); add(g, fin(new T.CylinderGeometry(.045, .045, .01, 7)), '#EEE9B8', 0, y + L / n / 2 - .014, 0); }
      add(g, fin(new T.CircleGeometry(.039, 7)), '#F6F0D0', 0, L / 2 + .009, 0, [-Math.PI / 2, 0, 0]); };
    cane(-.13, -.06, .42, .84, '#C6D06A'); cane(.0, .02, .26, .9, '#D2D878'); cane(.13, .1, .1, .8, '#BCC85E'); lfi(p, .46, .06, '#7AA858', .1, .2, .03, [0, .2, -.75]); }, V(.2, .3, 1));
  // ---- BẦU HỒ LÔ: hai bầu thắt eo, bầu dưới to bầu trên nhỏ ----
  shot('bauholo', p => { const sq = v => Math.sqrt(Math.max(0, v)); const pf = t => Math.max(.26 * sq(1 - Math.pow((t - .3) / .31, 2)), .15 * sq(1 - Math.pow((t - .78) / .19, 2)), t > .45 && t < .7 ? .085 : 0, t > .9 ? .03 : 0, .01);
    const mk = (x, y, z, rz, s, c) => { const g = new T.Group(); g.position.set(x, y, z); g.rotation.z = rz; p.add(g); add(g, fin(jit(lathe(pf, 24, 12), .004)), c, 0, -.38 * s, 0, null, [s, .78 * s, s]);
      for (let k = 0; k < 10; k++){ const a = rn() * 6.28, t = .1 + rn() * .35, r = pf(t) * s * 1.006, y = -.38 * s + t * .78 * s; add(g, fin(new T.CircleGeometry(.01, 5)), '#F1F6DE', Math.cos(a) * r, y, Math.sin(a) * r).lookAt(Math.cos(a) * 9, y, Math.sin(a) * 9); }
      add(g, fin(tube([V(0, .39 * s, 0), V(.02, .46 * s, 0), V(.07, .5 * s, 0)], t => .017, 3, 5)), '#6E9A3A'); };
    mk(-.16, .03, -.12, .4, 1, '#A4CF74'); mk(.2, -.08, .12, .12, .72, '#B6DA88'); }, V(.15, .25, 1));
  // ---- HÀNH HƯƠNG: bó lùn xoè quạt, cọng nhỏ xíu nhiều tép, củ ửng tím, không cột ----
  shot('hanhhuong', p => { const g = new T.Group(); g.rotation.z = -.2; p.add(g);
    for (let k = 0; k < 13; k++){ const u = (k - 6) / 6, x = u * .13, z = (k % 3 - 1) * .05, h = .62 + (k * 37 % 10) * .014 - Math.abs(u) * .1; const s = new T.Group(); s.position.set(x, 0, z); s.rotation.z = -u * .5; g.add(s);
      add(s, fin(new T.CylinderGeometry(.017, .02, .2, 6)), '#FBF7EE', 0, -.3, 0); add(s, fin(new T.IcosahedronGeometry(.036, 0)), k % 2 ? '#D9A9C6' : '#E7C3D8', 0, -.42, 0, null, [1, .95, 1]);
      add(s, fin(new T.CylinderGeometry(.015, .017, .1, 6)), '#cfe8a0', 0, -.15, 0);
      add(s, fin(tube([V(0, -.1, 0), V(u * .02, .3 * h, 0), V(u * .08, .65 * h, .01), V(u * .2, .95 * h, .02)], t => .015 * (1 - Math.pow(t, 2.5)) + .003, 6, 5)), k % 2 ? '#3F8F36' : '#4A9A3C');
      for (let j = 0; j < 2; j++) add(s, fin(tube([V(0, -.45, 0), V((j - .5) * .02, -.49, 0), V((j - .5) * .04, -.53, .01)], t => .004, 2, 3)), '#E3D3BC'); } }, V(.2, .3, 1));
  // ---- RAU MUỐNG TÍA: bó cọng tím, lá mũi tên xanh đậm, buộc lạt đỏ ----
  shot('raumuongtia', p => { const g = new T.Group(); g.rotation.z = -.35; p.add(g);
    for (let k = 0; k < 7; k++){ const x = (k - 3) * .05, z = (k % 2) * .04 - .02, sp = (k - 3) * .06; const s = new T.Group(); s.position.set(x, 0, z); s.rotation.z = -sp * .5; g.add(s);
      add(s, fin(new T.CylinderGeometry(.026, .03, .75, 6)), k % 2 ? '#7A4466' : '#8E5478', 0, 0, 0); add(s, fin(new T.CylinderGeometry(.012, .012, .02, 6)), '#F0DCE6', 0, -.38, 0);
      for (const [y, a] of [[.32, .5], [.42, -.6], [.5, .2]]){ const lg = new T.Group(); lg.position.set(0, y, 0); lg.rotation.y = a + k; s.add(lg); add(lg, fin(new T.ConeGeometry(.07, .26, 3)), k % 2 ? '#3F8A3A' : '#4A9642', .06, .09, 0, [0, 0, -.5], [1, 1, .25]); } }
    add(g, fin(new T.TorusGeometry(.17, .028, 4, 10)), '#C24A2E', 0, -.15, 0, [Math.PI / 2, 0, 0], [1.05, .55, 1]); }, V(.1, .2, 1));
  ri.renderLists.dispose(); return OUT; };"""
rep(END5, QUY5)
# ---- v157: mướp thường, khía ôm sát vỏ (trước đây khía lòi ra ngoài trái) ----
rep("""for (let k = 0; k < 10; k += 2){ const a = k / 10 * 6.283; add(g, fin(lathe(t => pf(t) * .22, 10, 3)), '#6E9A52', Math.cos(a) * .1 * s, -.36 * s, Math.sin(a) * .1 * s, null, [.6 * s, .72 * s, .6 * s]); }""",
"""for (let k = 0; k < 8; k++){ const a = k / 8 * 6.283 + .25; add(g, fin(tube([0, 1, 2, 3, 4, 5, 6, 7].map(i => { const t = .05 + i / 7 * .88, r = pf(t) * s; return V(Math.cos(a) * r, -.36 * s + t * .72 * s, Math.sin(a) * r); }), t => .013 * s, 10, 4)), '#6E9A52'); }""")

# ================= v157: nối 5 giống quý mới vô game =================
rep("""hai: 'chieu' } };
for (const k in QUY){ const q = QUY[k]; q.k = k;""", """hai: 'chieu' },
  muophuong: { base: 'muop', name: 'Mướp hương', en: 'Fragrant luffa', col: '#74B352', dat: 'bon', cham: 'am', mua: 'mua', hai: 'sang' },
  mialau: { base: 'mia', name: 'Mía lau', en: 'Slender sugarcane', col: '#C6D06A', dat: 'tot', cham: 'rom', mua: 'kho', hai: 'chieu' },
  bauholo: { base: 'bau', name: 'Bầu hồ lô', en: 'Calabash gourd', col: '#A4CF74', dat: 'tot', cham: 'am', mua: 'kho', hai: 'sang' },
  hanhhuong: { base: 'hanh', name: 'Hành hương', en: 'Fragrant scallion', col: '#D9A9C6', dat: 'tot', cham: 'rom', mua: 'mua', hai: 'thuan' },
  raumuongtia: { base: 'raumuong', name: 'Rau muống tía', en: 'Purple water spinach', col: '#7A4466', dat: 'bon', cham: 'lua2', mua: 'mua', hai: 'chieu' } };
for (const k in QUY){ const q = QUY[k]; q.k = k;""")
# màu ngoài liếp: đổi đúng màu trái/cọng/củ của cây gốc
rep("""  return (QTM[key] = hit ? new T.MeshStandardMaterial({ color: qtC.clone(), flatShading: true, roughness: .92""",
"""  else if (QT5[k]){ const v = QT5[k][String(c).toLowerCase()]; if (v){ qtC.set(v); hit = 1; } }
  return (QTM[key] = hit ? new T.MeshStandardMaterial({ color: qtC.clone(), flatShading: true, roughness: .92""")
rep("""const QTM = {}, qtC = new T.Color()""", """const QT5 = { muophuong: { '#3f7a34': '#6FA84E', '#4a8a3a': '#84BC5E' }, mialau: { '#5e3a4e': '#B9C45C', '#6c4458': '#CBD472', '#8a6a4a': '#A9B860', '#7a6a4a': '#9CAE58' }, bauholo: { '#9ccb6a': '#C4DE8E', '#b5d88a': '#D6E8A8' }, hanhhuong: { '#f4f1e0': '#D9A9C6' }, raumuongtia: { '#7cb050': '#7A4466', '#9fc860': '#8E5478' } };
const QTM = {}, qtC = new T.Color()""")
# chuyện Ngoại kể
rep("""ai dè vườn mình còn giữ được.' };""", """ai dè vườn mình còn giữ được.', muophuong: 'Mướp hương đó con. Nấu canh thơm tới ngoài ngõ, hồi xưa ông ngoại con ngửi mùi là biết tới giờ cơm.', mialau: 'Mía lau nè con. Cây nhỏ mà ngọt thanh, hồi đó trời nắng Ngoại hay nấu nước mía lau cho cả nhà uống mát.', bauholo: 'Bầu hồ lô, trái thắt eo ngộ ghê. Hồi xưa ông cố để trái già phơi khô, làm bình đựng nước mang ra đồng.', hanhhuong: 'Hành hương, củ nhỏ xíu mà thơm nồng. Má Ngoại nói phi mỡ hành phải lựa giống này mới dậy mùi.', raumuongtia: 'Rau muống tía, cọng tím mà giòn. Hồi nhỏ Ngoại hay chẻ cọng ngâm nước cho nó cong lại, ăn với bún.' };""")
rep("""so the neighbors know our garden still keeps the old variety.") };""", """so the neighbors know our garden still keeps the old variety."),
  muophuong: L135('Mướp hương con trồng thơm thiệt. Ngoại nấu nồi canh, mùi bay qua tới nhà kế bên, ai cũng hỏi giống ở đâu ra.', "Your fragrant luffa smells wonderful. I made a pot of soup and the scent reached next door; everyone asked where the seed came from."),
  mialau: L135('Mía lau ngọt thanh quá con. Ngoại nấu một nồi nước mát, mời bà con đi ngang ghé uống cho đỡ nắng.', "Your slender cane is so mildly sweet. I brewed a pot of cooling tea and offered it to neighbors passing by in the heat."),
  bauholo: L135('Bầu hồ lô con trồng tròn trịa ghê. Trái non Ngoại nấu canh, còn trái già Ngoại để phơi khô treo trước hiên cho vui nhà.', "Your calabash is so nicely shaped. I cooked the young one in soup and I'll dry an old one to hang on the porch."),
  hanhhuong: L135('Hành hương thơm nức mũi. Ngoại phi một chén mỡ hành, cả xóm ngửi là biết nhà mình sắp có cơm ngon.', "This fragrant scallion smells so good. I fried up a bowl of scallion oil; the whole hamlet knew a good meal was coming."),
  raumuongtia: L135('Rau muống tía giòn thiệt con. Ngoại chẻ một rổ đem cho mấy nhà trong xóm ăn bún, ai cũng khen cọng tím đẹp.', "Your purple water spinach is so crisp. I split a basketful for the neighbors' noodle bowls; everyone praised the purple stems.") };""")
# trang Đồ quý: số đếm theo số giống thật
rep("""${ng + nc}/11</div>` + UX.title('Giống quý', ng + '/6')""", """${ng + nc}/${QGI.length + QCA.length}</div>` + UX.title('Giống quý', ng + '/' + QGI.length)""")
rep("""'Hand all 6 rare crops to Uncle Bảy · ') + sg + '/6'""", """'Hand 6 rare crops to Uncle Bảy · ') + Math.min(6, sg) + '/6'""")
# ông Bảy: giàn trái giống vẫn ở mốc 6 giống (bất kỳ), thêm mốc 8 và 11
rep("""!B.set.giong && QGI.every(k => B.stamp[k])""", """!B.set.giong && QGI.filter(k => B.stamp[k]).length >= 6""")
rep("""const BAYMOC = [[2, 300], [4, 600]];""", """const BAYMOC = [[2, 300], [4, 600], [8, 900], [11, 1200]];""")
rep("""if (S && !(B.set.giong && n >= 6)){ S.pose = 'kha'; S.line = L135(`Được ${got} giống quý rồi đó. Qua gửi cháu chút quà dọc đường, ráng tìm cho đủ bộ nghe.`, `That's ${got} rare crops now. Here's a little something along the way. Keep looking for the full set.`); }""",
"""if (S){ S.pose = 'kha'; S.line = n >= QGI.length ? L135(`Đủ hết ${n} giống quý rồi. Qua đi ghe mấy chục năm, chưa thấy vườn nào giữ giống kỹ như vườn cháu.`, `All ${n} rare crops. In decades on this boat I've never seen a garden keep its seeds like yours.`) : L135(`Được ${got} giống quý rồi đó. Qua gửi cháu chút quà dọc đường, ráng tìm cho đủ bộ nghe.`, `That's ${got} rare crops now. Here's a little something along the way. Keep looking for the full set.`); }""")
rep("""held = BAYK.filter(k => bayN(k) > 0), fresh = [...BAYK, 'caho'].find(""", """held = [...BAYK, ...BAYK5].filter(k => bayN(k) > 0), fresh = [...BAYK, ...BAYK5, 'caho'].find(""")
# ---- nút Chợ: chữ "Mới" không đè nhãn kho nữa ----
rep("""@media (max-width:560px){#bCho.moi::after{top:8px;right:calc(100% - 9px)}}""", """@media (max-width:560px){#bCho.moi::after{top:8px;right:calc(100% - 9px)}#bCho.moi .kb:not([hidden]){top:34px!important;right:calc(100% - 8px)!important}}""")
rep("""const BAYK = ['mongtoitia', 'otvang', 'cachuavang', 'khoquarung', 'baptim', 'khommat', 'cadua', 'hu', 'rodauvang', 'locbong'];""",
"""const BAYK = ['mongtoitia', 'otvang', 'cachuavang', 'khoquarung', 'baptim', 'khommat', 'cadua', 'hu', 'rodauvang', 'locbong'], BAYK5 = ['muophuong', 'mialau', 'bauholo', 'hanhhuong', 'raumuongtia'];""")
rep("""h += UX.title('Sổ tìm mua', nst + '/11')""", """h += UX.title('Sổ tìm mua', nst + '/' + (QGI.length + QCA.length))""")
rep("{}).moc || {})[4] ? ' ok' : ''}", "{}).moc || {})[11] ? ' ok' : ''}")
rep("""L135('Giao 2 giống: 300 xu · giao 4 giống: 600 xu', 'Hand over 2 crops: 300 coins · 4 crops: 600 coins')""", """L135('Giao 2, 4, 8, 11 giống: 300, 600, 900, 1.200 xu', 'Hand over 2, 4, 8, 11 crops: 300, 600, 900, 1,200 coins')""")

# ---- Bao hạt lạ: sạp cô Út ở chợ huyện ----
BL_JS = r"""
const BLA = { gia: 40, ngay: 3, pQuy: .08, pDon: .20, chac: 5 };
function blS(){ const B = ST.bl || (ST.bl = { d: '', n: 0, miss: 0 }); if (B.d !== dayKey()){ B.d = dayKey(); B.n = 0; } return B; }
function blPool(){ return Object.keys(CROPS).filter(c => unlocked(c) && !CROPS[c].tree && !CROPS[c].rare && !QUY[c]); }
function blGot(){ const Q = quyQ(); return Object.keys(QUY).filter(k => Q.got && Q.got[k]); }
function blRoll(rnd = Math.random){ const B = blS(), pool = blPool(), got = blGot(), out = [], r = rnd();
  const hat = n => { for (let i = 0; i < n; i++){ const k = pool[Math.floor(rnd() * pool.length)], o = out.find(x => x.k === k && !x.q); if (o) o.n++; else out.push({ k, n: 1 }); ST.seeds[k] = (ST.seeds[k] || 0) + 1; } };
  let kind = got.length && (B.miss >= BLA.chac || r < BLA.pQuy) ? 'quy' : r < BLA.pQuy + BLA.pDon ? 'don' : 'thuong';
  if (kind === 'quy'){ const k = got[Math.floor(rnd() * got.length)]; ST.seeds[k] = (ST.seeds[k] || 0) + 1; out.push({ k, n: 1, q: 1 }); hat(2); B.miss = 0; }
  else { if (got.length) B.miss++; let d = null; if (kind === 'don'){ try { d = quyDon(); } catch (e) {} } if (d){ hat(2); out.push({ don: d.txt }); } else { kind = 'thuong'; hat(3); } }
  return { kind, out }; }
function blBuy(b){ const B = blS(); if (B.n >= BLA.ngay) return; if (!blPool().length) return;
  if (ST.xu < BLA.gia) return toast(L135(`Bao hạt lạ ${BLA.gia} xu, con còn thiếu ${BLA.gia - ST.xu} xu.`, `A mystery seed bag is ${BLA.gia} coins, you need ${BLA.gia - ST.xu} more.`), 'dan');
  ST.xu -= BLA.gia; B.n++; const R = blRoll(); SHEET.bl = R; SHEET.blA = 1; save(); hud();
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches, tq = still ? 0 : BLT.mo + (R.out.length - 1) * BLT.cach;
  blDone(); try { shB.classList.remove('blskip'); } catch (e) {} try { coinPop(`-${BLA.gia} xu`, '#F08A6E'); sfx('coin'); buzz(18); } catch (e) {}
  const sh = SHEET; BLQ.f = () => { BLQ.f = null; try { shB.classList.remove('blrun'); } catch (e) {} if (SHEET !== sh) return; try { if (R.kind === 'quy'){ sfx('lvl'); buzz(60); const e = shB.querySelector('.blr.ok'), r = e && e.getBoundingClientRect(); confettiAt(r ? r.left + r.width / 2 : innerWidth / 2, r ? r.top + r.height / 2 : innerHeight * .5, 36, 1.1); } } catch (e) {} };
  renderSheet(); SHEET.blA = 0; try { shB.scrollTop = 0; if (!still) shB.classList.add('blrun'); } catch (e) {}
  BLQ.t = setTimeout(() => BLQ.f && BLQ.f(), tq * 1000 + (R.kind === 'quy' ? 180 : 300)); }
const BLT = { mo: .62, cach: .24 }, BLQ = { t: 0, f: null };
function blDone(){ clearTimeout(BLQ.t); if (BLQ.f) BLQ.f(); }
function blSkip(){ if (!BLQ.f) return; try { shB.classList.add('blskip'); } catch (e) {} blDone(); }
addEventListener('pointerdown', e => { if (BLQ.f && e.target && e.target.closest && e.target.closest('#sheet'))  blSkip(); }, true);
function blHTML(){ const B = blS(), left = BLA.ngay - B.n, got = blGot(), R = SHEET.bl, A = SHEET.blA, nm = k => fxT(CROPS[k].name).toLowerCase();
  let h = `<div class="tmsay"><b>${fxT('Cô Út')}</b>${L135('Hạt cô gom của bà con trong xóm, bỏ chung một bao. Xé ra mới biết hạt gì, mà bao nào cũng gieo được hết.', 'Seeds I gather from the neighbours, all in one bag. You only know once you open it, but every bag can be sown.')}</div>`;
  h += UX.hero(UIC.baola, L135('Bao hạt lạ', 'Mystery seed bag'), left > 0 ? L135(`Hôm nay còn ${left} bao`, `${left} left today`) : L135('Hôm nay hết bao rồi, mai con ghé nghe', 'Sold out today, come back tomorrow'), A ? 'blop' + (R.kind === 'quy' ? ' blq' : '') : '');
  h += `<div class="acts">${left > 0 ? UX.btn('blbuy', L135(`${R ? 'Mua thêm' : 'Mua'} 1 bao · ${BLA.gia} xu`, `Buy 1 bag · ${BLA.gia} coins`), { g: 1 }) : UX.btn('noop', L135('Mai ghé lại nghe', 'Come back tomorrow'), { dis: 1 })}</div>`;
  if (R){ h += UX.title(L135('Trong bao vừa xé', 'Inside this bag'));
    R.out.slice().sort((a, b) => (a.q ? 2 : a.don ? 1 : 0) - (b.q ? 2 : b.don ? 1 : 0)).forEach((o, i) => { const st = A ? ` style="animation-delay:${(BLT.mo + i * BLT.cach).toFixed(2)}s"` : '';
      h += o.don ? `<div class="qset${A ? ' blr' : ''}"${st}><img src="${UIC.task}" alt=""><div><b>${L135('Lời đồn đồ quý', 'A rumour')}</b><span>${esc(fxT(o.don))}</span></div></div>`
        : `<div class="qset${A ? ' blr' : ''}${o.q ? ' ok' : ''}"${st}><img src="${ICON[o.k]}" alt=""><div><b>${o.n} ${L135('hạt', 'seed' + (o.n > 1 ? 's' : ''))} ${nm(o.k)}</b><span>${o.q ? L135('Hạt giống quý, hiếm lắm đó', 'A rare seed') : L135('Đã bỏ vô túi hạt', 'Added to your seeds')}</span></div></div>`; }); }
  h += `<div class="note">${!got.length ? L135('Con chưa gặp giống quý nào nên trong bao chưa có hạt quý. Thay vô đó là lời đồn chỉ chỗ tìm.', 'You have not found a rare crop yet, so bags hold rumours instead of rare seeds.') : B.miss >= BLA.chac ? L135('Bao kế tiếp chắc chắn có hạt giống quý.', 'The next bag is sure to hold a rare seed.') : L135(`Trễ lắm là ${BLA.chac + 1 - B.miss} bao nữa sẽ có hạt giống quý.`, `A rare seed within ${BLA.chac + 1 - B.miss} more bags at most.`)}</div>`;
  h += UX.title(L135('Trong bao có gì', 'What is inside'), L135('mỗi lần xé', 'each bag'));
  const row = (img, a, b2) => `<div class="qset"><img src="${img}" alt=""><div><b>${a}</b><span>${b2}</span></div></div>`;
  h += row(UIC.seedbag, L135('72%: 3 hạt rau', '72%: 3 vegetable seeds'), L135('Rau củ con đã trồng được', 'Crops you can already grow'));
  h += row(UIC.task, L135('20%: 2 hạt rau, 1 lời đồn', '20%: 2 seeds, 1 rumour'), L135('Lời đồn chỉ cách gặp giống quý', 'A rumour on how to find a rare crop'));
  h += row(UIC.sprout, L135('8%: 1 hạt giống quý, 2 hạt rau', '8%: 1 rare seed, 2 seeds'), L135('Chỉ ra giống quý con đã từng gặp', 'Only rare crops you have found before'));
  return h; }
"""
rep("function bayAct(a, b){", BL_JS.strip() + "\nfunction bayAct(a, b){")
rep("""  if (kind === 'bay'){ shT.textContent = 'Ông Bảy Kiếng'; h += bayHTML(); }""", """  if (kind === 'baola'){ shT.textContent = L135('Sạp cô Út', "Auntie Ut's stall"); h += blHTML(); }
  if (kind === 'bay'){ shT.textContent = 'Ông Bảy Kiếng'; h += bayHTML(); }""")
rep("""if (a === 'chgo'){ chEnter(); return; }""", """if (a === 'chgo'){ chEnter(); return; } if (a === 'blbuy'){ blBuy(b); return; }""")
rep(""".qset.ok{box-shadow:0 0 0 2px #E2B04A;background:#FFF6DC}""", """.qset.ok{box-shadow:0 0 0 2px #E2B04A;background:#FFF6DC}.qset.blr{animation:blra .34s cubic-bezier(.2,.9,.3,1.25) both}.qset.blr.ok{animation:blrq .62s cubic-bezier(.2,.9,.3,1.2) both}
@keyframes blra{from{opacity:0;transform:translateY(-28px) scale(.7)}}
@keyframes blrq{0%{opacity:0;transform:translateY(-28px) scale(.7)}45%{opacity:1;transform:scale(1.08);box-shadow:0 0 0 4px #EDB940,0 0 24px 8px rgba(237,185,64,.75);background:#FFE9A8}100%{transform:none}}
.uxh.blop .hi{position:relative}.uxh.blop .hi img{transform-origin:50% 88%;animation:blsh .62s ease-in-out both}
@keyframes blsh{0%{transform:none}12%{transform:rotate(-9deg)}26%{transform:rotate(9deg)}40%{transform:rotate(-7deg)}54%{transform:rotate(7deg)}68%{transform:rotate(0) scale(.92,1.06)}84%{transform:scale(1.16,.9)}100%{transform:none}}
.uxh.blop.blq .hi{animation:blgl .62s ease-in both}
@keyframes blgl{0%,25%{box-shadow:0 0 0 0 rgba(237,185,64,0)}80%{box-shadow:0 0 0 4px #EDB940,0 0 16px 8px rgba(237,185,64,.8)}100%{box-shadow:0 0 0 2px #EDB940,0 0 8px 4px rgba(237,185,64,.4)}}
.blskip .blr,.blskip .uxh.blop .hi,.blskip .uxh.blop .hi img{animation-duration:.01s!important;animation-delay:0s!important}
@media (prefers-reduced-motion:reduce){ .qset.blr,.qset.blr.ok,.uxh.blop .hi,.uxh.blop .hi img{animation:none} }""")
# sạp nhỏ trước nhà lồng chợ: thùng gỗ, ba bao chàm, bảng HẠT LẠ
rep("""  try { if (quyOn()){ const t = G(6.75, 0, 1.2, -.35, g); t.userData.tag = 'bay'; bayStall(t); } } catch (e) {}""", """  try { if (quyOn()){ const t = G(6.75, 0, 1.2, -.35, g); t.userData.tag = 'bay'; bayStall(t); } } catch (e) {}
  try { if (quyOn()){ const t = G(-.2, 0, 1.86, .12, g); t.userData.tag = 'baola'; t.scale.setScalar(1.3);
    M(box(.52, .2, .32), '#8A6A44', 0, .1, 0, { p: t }); M(box(.56, .03, .36), '#6B4A2E', 0, .215, 0, { p: t });
    const bao = (x, y, z, k) => { M(cyl(.08 * k, .1 * k, .15 * k, 10), '#3E7C8F', x, y + .075 * k, z, { p: t }); M(cyl(.035 * k, .08 * k, .04 * k, 10), '#3E7C8F', x, y + .17 * k, z, { p: t }); M(cyl(.04 * k, .04 * k, .02 * k, 8), '#E9D9B0', x, y + .195 * k, z, { p: t }); M(cyl(.065 * k, .035 * k, .04 * k, 8), '#2C5F70', x, y + .225 * k, z, { p: t }); };
    bao(-.15, .23, .02, 1); bao(.13, .23, .03, 1.1); bao(-.01, .23, -.08, .9); bao(.4, 0, -.02, 1.1);
    sign('HẠT LẠ', .46, .19, '#FBF2DA', '#2C5F70', t, 0, .105, .165, 112); } } catch (e) { console.warn('baola', e); }""")
rep("""t === 'đò' || t === 'bay'){ const bb = new T.Box3().setFromObject(o); hits.push([t, bb]); }""", """t === 'đò' || t === 'bay' || t === 'baola'){ const bb = new T.Box3().setFromObject(o); if (t === 'baola') bb.expandByScalar(.25); hits.push([t, bb]); }""")
rep("""else if (best === 'bay'){ sfx('pick'); $('#chSay').hidden = true; openSheet('bay'); }""", """else if (best === 'bay'){ sfx('pick'); $('#chSay').hidden = true; openSheet('bay'); } else if (best === 'baola'){ sfx('pick'); $('#chSay').hidden = true; openSheet('baola'); }""")

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
