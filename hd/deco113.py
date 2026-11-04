# deco113 · 10 món đồ trang trí mới (bản vẽ để anh Ares duyệt, chưa ship)
# Giá trải từ rẻ tới rất mắc, nhắm người chơi dư xu (bot dư ~118.000 xu ngày 30):
#   rẻ: đèn bão 250, lu nước mưa 450, bù nhìn rơm 900
#   vừa: bộ ván ngựa 2.200, giàn bông giấy 3.500
#   mắc: cối xay lúa 6.000, xuồng ba lá 9.000, giếng gạch có tời 14.000
#   rất mắc: chòi lá có võng 25.000, miếu Ông Địa 45.000
# Dùng: python3 deco113.py live/v112a.html live/v113d.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:90], c, n); s = s.replace(a, b)

rep("ghe_da: { cat: 'k', name: 'Ghế đá', price: 150 },",
    "ghe_da: { cat: 'k', name: 'Ghế đá', price: 150 }, den_bao: { cat: 'k', name: 'Đèn bão trụ tre', price: 250, tier: 1 }, lu_mua: { cat: 'k', name: 'Lu hứng nước mưa', price: 450, tier: 1 }, bu_nhin: { cat: 'k', name: 'Bù nhìn rơm', price: 900, tier: 1 }, van_ngua: { cat: 'k', name: 'Bộ ván ngựa, bình trà', price: 2200, tier: 2 }, gian_bg: { cat: 'k', name: 'Vòm bông giấy', price: 3500, tier: 2 }, coi_xay: { cat: 'k', name: 'Cối xay lúa', price: 6000, tier: 3 }, xuong: { cat: 'k', name: 'Xuồng ba lá trên giá', price: 9000, tier: 3 }, gieng: { cat: 'k', name: 'Giếng gạch có tời', price: 14000, tier: 3 }, choi_la: { cat: 'k', name: 'Chòi lá có võng', price: 25000, tier: 4 }, mieu: { cat: 'k', name: 'Miếu Ông Địa', price: 45000, tier: 4 },")

JS = r'''
/* ===== deco113: 10 món mới, dựng trong 1 ô đất (rộng ~1.2, sâu ~0.8), gốc ở mặt đất ===== */
const DCX = (() => { const MS = (c, o = {}) => new T.MeshStandardMaterial(Object.assign({ color: c, flatShading: true, roughness: .8 }, o));
  const glow = MS('#FFE3A0', { emissive: '#FFB84A', emissiveIntensity: .9, roughness: .4 }), brick = MS('#B85C3A'), mortar = MS('#D8CDB8'), tile = MS('#B4432E'), tileD = MS('#8E3222'), gold = MS('#D9A93A', { metalness: .4, roughness: .45 });
  const hz = Math.PI / 2;
  const leaves = (x, y, z, n, r, cols) => { for (let i = 0; i < n; i++) M(ico(r * R(.7, 1.1), 0), pick(cols), x + R(-r, r) * 1.6, y + R(-r, r), z + R(-r, r), { r: [R(0, 3), R(0, 3), 0], cast: false }); };
  return {
  den_bao(){ // trụ tre cắm đế đá, móc ngang, đèn bão (bầu dầu, chụp kính sáng, lồng thép, quai)
    M(box(.22, .07, .22), '#9A968C', 0, .035, 0); M(cyl(.035, .042, 1.25, 7), C.bamboo, 0, .66, 0); for (const y of [.35, .7, 1.05]) M(cyl(.045, .045, .025, 7), '#B48A50', 0, y, 0);
    M(box(.34, .03, .03), C.bamboo, .15, 1.2, 0); M(cyl(.004, .004, .1, 3), '#4A2F1E', .28, 1.14, 0);
    const L = G(.28, .9, 0, 0, ROOT); M(cyl(.07, .08, .06, 9), '#4F7A63', 0, 0, 0, { p: L }); M(sph(.065, 9, 7), glow, 0, .09, 0, { p: L, s: [1, 1.2, 1] });
    for (const a of [0, 1.05, 2.1]) M(box(.006, .16, .15), '#3A4A42', 0, .09, 0, { p: L, r: [0, a, 0], cast: false }); M(cone(.08, .07, 9), '#4F7A63', 0, .2, 0, { p: L }); M(new T.TorusGeometry(.05, .006, 3, 10, Math.PI), '#3A4A42', 0, .23, 0, { p: L }); },
  lu_mua(){ // lu da lươn lớn kê gạch, đai men vàng, nắp gỗ, gáo dừa cán tre
    for (const [x, z] of [[-.12, -.08], [.12, -.08], [0, .12]]) M(box(.18, .07, .1), brick, x, .035, z, { r: [0, x * 3, 0] });
    M(sph(.33, 12, 9), '#6E4126', 0, .42, 0, { s: [1, 1.12, 1] }); M(new T.TorusGeometry(.3, .02, 4, 16), '#C9952A', 0, .5, 0, { r: [hz, 0, 0] }); M(new T.TorusGeometry(.2, .04, 5, 14), '#5A3420', 0, .79, 0, { r: [hz, 0, 0] });
    M(cyl(.24, .24, .04, 14), '#8A5D3B', 0, .82, 0); M(cyl(.03, .03, .04, 6), '#6B4529', 0, .86, 0); M(sph(.08, 8, 5, 0, Math.PI * 2, 0, Math.PI / 2), '#5A3A22', .13, .88, .05, { r: [Math.PI, 0, 0] }); M(cyl(.012, .012, .34, 5), C.bamboo, .02, .9, .02, { r: [0, .4, hz] }); },
  bu_nhin(){ // bù nhìn: cọc chữ thập, áo bà ba xanh, khăn rằn, đầu bao bố, nón lá, rơm thò tay chân
    M(cyl(.03, .035, 1.35, 6), '#8A5D3B', 0, .67, 0); M(cyl(.025, .025, .8, 6), '#8A5D3B', 0, 1.0, 0, { r: [0, 0, hz] });
    M(box(.32, .38, .14), '#4F6FA8', 0, .86, 0); for (const sg of [-1, 1]){ M(box(.24, .1, .12), '#4F6FA8', sg * .26, 1.0, 0); for (let i = 0; i < 4; i++) M(cone(.025, .14, 4), '#E3C46A', sg * (.4 + R(0, .04)), 1.0 + R(-.04, .04), R(-.04, .04), { r: [0, 0, sg * -hz + R(-.4, .4)], cast: false }); }
    for (let i = 0; i < 6; i++) M(cone(.03, .2, 4), '#E3C46A', R(-.12, .12), .58, R(-.05, .05), { r: [Math.PI + R(-.3, .3), 0, R(-.3, .3)], cast: false });
    for (let i = 0; i < 4; i++) M(box(.035, .02, .15), i % 2 ? '#2B2B2B' : '#EDE6D6', -.1 + i * .066, 1.07, .0, { cast: false }); M(box(.06, .12, .02), '#2B2B2B', .08, 1.0, .08, { r: [0, 0, .3] });
    M(sph(.11, 8, 6), '#D9B87A', 0, 1.22, 0); for (const x of [-.04, .04]) M(sph(.014, 4, 3), '#4A2F1E', x, 1.24, .1, { cast: false }); M(box(.06, .012, .01), '#9C3620', 0, 1.19, .105, { cast: false });
    M(cone(.24, .14, 14), '#E8D7A8', 0, 1.36, 0); M(new T.TorusGeometry(.235, .008, 3, 16), '#C9A66B', 0, 1.29, 0, { r: [hz, 0, 0] }); },
  van_ngua(){ // bộ ván ngựa gỗ gõ bóng, chân tiện, chiếu cói một nửa, khay trà: ấm, bốn tách, dĩa bánh
    const wd = MS('#5A3220', { roughness: .45 }), wl = MS('#4A2A1A');
    for (const x of [-.46, .46]) for (const z of [-.26, .26]){ M(box(.08, .38, .08), wl, x, .19, z); M(box(.11, .04, .11), wl, x, .03, z); }
    for (const z of [-.26, .26]) M(box(.9, .06, .04), wl, 0, .32, z); M(box(1.05, .07, .66), wd, 0, .42, 0); M(box(1.05, .015, .02), '#7A4A2E', 0, .46, .33, { cast: false });
    M(box(.5, .012, .62), '#D9C08A', -.24, .462, 0); for (let i = 0; i < 6; i++) M(box(.5, .004, .02), '#B89A5E', -.24, .47, -.25 + i * .1, { cast: false });
    M(box(.34, .025, .22), '#8A5D3B', .26, .47, 0); M(sph(.065, 9, 7), '#E8E4DA', .2, .54, 0, { s: [1, .85, 1] }); M(cyl(.01, .014, .08, 5), '#E8E4DA', .27, .55, 0, { r: [0, 0, -.9] }); M(new T.TorusGeometry(.04, .008, 3, 8, Math.PI), '#E8E4DA', .14, .55, 0, { r: [0, 0, hz] }); M(cyl(.02, .02, .02, 6), '#E8E4DA', .2, .6, 0);
    for (const [x, z] of [[.32, -.07], [.38, -.02], [.32, .07], [.38, .04]]) M(cyl(.022, .016, .035, 7), '#F2EFE6', x, .5, z);
    M(cyl(.07, .07, .012, 10), '#EDE6D6', -.28, .475, .18); for (let i = 0; i < 3; i++) M(box(.04, .025, .04), '#E3A84A', -.3 + i * .03, .49, .18 + (i - 1) * .02, { cast: false }); },
  gian_bg(){ // vòm tre phủ bông giấy hồng tím, hai chân đặt chậu gạch
    for (const sg of [-1, 1]){ M(cyl(.18, .14, .22, 8), brick, sg * .5, .11, 0); M(cyl(.03, .035, 1.1, 6), C.bamboo, sg * .5, .7, 0); leaves(sg * .5, .55, 0, 7, .1, ['#3F7A3A', '#4F8A44']); }
    for (let i = 0; i < 2; i++) M(new T.TorusGeometry(.5, .025, 4, 16, Math.PI), C.bamboo, 0, 1.2, (i - .5) * .12);
    for (let i = 0; i < 26; i++){ const a = R(0, Math.PI), x = Math.cos(a) * .5, y = 1.2 + Math.sin(a) * .5; leaves(x, y, R(-.08, .08), 1, .09, ['#3F7A3A', '#4F8A44', '#5E9A4E']); M(ico(.055, 0), pick(['#D6337A', '#E0559A', '#B8287A', '#F07BB5']), x + R(-.05, .05), y + R(-.03, .06), R(-.12, .12), { r: [R(0, 3), R(0, 3), 0], cast: false }); }
    for (let i = 0; i < 8; i++) M(ico(.03, 0), pick(['#D6337A', '#F07BB5']), R(-.5, .5), .02, R(-.25, .25), { s: [1, .3, 1], cast: false }); },
  coi_xay(){ // cối xay lúa tre đan trét đất: thớt dưới, thớt trên, cần ngang treo dây lên đòn tre, thúng lúa
    M(cyl(.3, .32, .1, 12), '#8A5D3B', -.1, .05, 0); M(cyl(.24, .27, .26, 12), '#A57250', -.1, .23, 0); M(cyl(.23, .24, .22, 12), '#B48560', -.1, .47, 0);
    for (const y of [.15, .3, .42, .55]) M(new T.TorusGeometry(.25, .012, 3, 14), '#C9A66B', -.1, y, 0, { r: [hz, 0, 0], cast: false }); M(cyl(.12, .1, .06, 10), '#6B4529', -.1, .61, 0);
    M(box(.07, .05, .05), '#6B4529', .16, .5, 0); M(box(.95, .04, .04), '#8A5D3B', .6, .5, 0); M(cyl(.004, .004, .62, 3), '#4A2F1E', .9, .81, 0);
    for (const x of [.35, 1.05]) M(cyl(.03, .035, 1.25, 6), C.bamboo, x, .62, -.3); M(cyl(.025, .025, .78, 6), C.bamboo, .7, 1.12, -.3, { r: [0, 0, hz] }); M(cyl(.004, .004, .35, 3), '#4A2F1E', .9, 1.0, -.15, { r: [.9, 0, 0] });
    M(cyl(.17, .13, .12, 12), '#C9A66B', -.42, .06, .28); M(sph(.15, 9, 5), '#E3C46A', -.42, .1, .28, { s: [1, .35, 1], cast: false }); },
  xuong(){ // xuồng ba lá gác trên giá tre: đáy trét chai, hai be ván, mũi có mắt ghe, mái chèo dựng
    const W = MS('#7A5232'), D = MS('#3A2A20');
    for (const x of [-.32, .32]){ M(cyl(.025, .025, .5, 5), C.bamboo, x, .22, -.12, { r: [.35, 0, 0] }); M(cyl(.025, .025, .5, 5), C.bamboo, x, .22, .12, { r: [-.35, 0, 0] }); M(cyl(.02, .02, .36, 5), C.bamboo, x, .4, 0, { r: [hz, 0, 0] }); }
    const b = G(0, .48, 0, 0, ROOT); M(box(1.0, .03, .2), D, 0, 0, 0, { p: b }); for (const sg of [-1, 1]){ M(box(1.12, .14, .025), W, 0, .07, sg * .13, { p: b, r: [sg * -.38, 0, 0] }); M(box(1.12, .025, .03), '#5A3A22', 0, .135, sg * .16, { p: b }); }
    for (const sg of [-1, 1]) M(cone(.11, .26, 4), W, sg * .62, .08, 0, { p: b, r: [0, 0, sg * -hz], s: [1, 1, .9] });
    for (const sg of [-1, 1]){ M(cyl(.03, .03, .01, 10), '#EDE6D6', .52, .1, sg * .145, { p: b, r: [hz, 0, 0], cast: false }); M(cyl(.016, .016, .012, 8), '#2B2B2B', .53, .1, sg * .15, { p: b, r: [hz, 0, 0], cast: false }); M(box(.18, .02, .005), '#9C3620', .45, .12, sg * .15, { p: b, cast: false }); }
    for (let i = 0; i < 3; i++) M(box(.025, .03, .26), '#5A3A22', -.3 + i * .3, .03, 0, { p: b });
    M(cyl(.014, .014, 1.0, 5), '#B48560', -.62, .5, .26, { r: [0, 0, .25] }); M(box(.09, .25, .015), '#8A5D3B', -.73, .1, .26, { r: [0, 0, .25] }); },
  gieng(){ // giếng xây gạch tô vữa, mặt nước, hai trụ gỗ, mái ngói nhỏ, tời quay, dây gàu, rêu chân giếng
    M(cyl(.36, .38, .46, 14), brick, 0, .23, 0); for (const y of [.12, .26, .4]) M(new T.TorusGeometry(.37, .008, 3, 18), '#9A4A2E', 0, y, 0, { r: [hz, 0, 0], cast: false }); M(new T.TorusGeometry(.35, .05, 4, 18), mortar, 0, .48, 0, { r: [hz, 0, 0] });
    M(cyl(.3, .3, .02, 14), MS('#3E7FA0', { roughness: .2 }), 0, .4, 0, { cast: false });
    for (const sg of [-1, 1]) M(box(.07, 1.05, .07), '#6B4529', sg * .42, .55, 0); M(cyl(.045, .045, .78, 8), '#8A5D3B', 0, .95, 0, { r: [0, 0, hz] }); for (let i = 0; i < 5; i++) M(new T.TorusGeometry(.05, .008, 3, 8), '#C9A66B', -.1 + i * .05, .95, 0, { r: [0, hz, 0], cast: false });
    M(box(.03, .14, .03), '#6B4529', .5, .9, .05); M(cyl(.012, .012, .1, 5), '#6B4529', .52, .83, .1, { r: [hz, 0, 0] });
    M(cyl(.005, .005, .35, 3), '#C9A66B', .12, .76, 0); M(cyl(.08, .065, .11, 9), '#8C8C88', .12, .55, 0); M(new T.TorusGeometry(.06, .006, 3, 8, Math.PI), '#6E6E6A', .12, .61, 0);
    for (const sg of [-1, 1]) M(box(1.05, .035, .36), tile, 0, 1.2, sg * .15, { r: [sg * .55, 0, 0] }); M(box(1.08, .05, .05), tileD, 0, 1.3, 0); for (const sg of [-1, 1]) M(cone(.04, .1, 5), tileD, sg * .55, 1.33, 0, { r: [0, 0, sg * -.6] });
    leaves(0, .03, .33, 6, .05, ['#4F7A3A', '#5E8F48']); },
  choi_la(){ // chòi lá nghỉ mát: sàn ván, bốn cột tre, mái lá dừa nước hai lớp, võng dù, đèn lồng, bậc thang
    for (const x of [-.48, .48]) for (const z of [-.3, .3]) M(cyl(.035, .04, 1.25, 6), C.bamboo, x, .62, z);
    M(box(1.1, .07, .72), '#8A5D3B', 0, .3, 0); for (let i = 0; i < 7; i++) M(box(1.1, .005, .01), '#6B4529', 0, .337, -.3 + i * .1, { cast: false }); for (let i = 0; i < 2; i++) M(box(.3, .04, .14), '#8A5D3B', 0, .1 + i * .1, .42 + (1 - i) * .1);
    M(cone(.95, .55, 4), C.thatch, 0, 1.5, 0, { r: [0, Math.PI / 4, 0], s: [1, 1, .72] }); M(cone(.82, .5, 4), C.thatchD, 0, 1.6, 0, { r: [0, Math.PI / 4, 0], s: [1, 1, .72] }); M(cone(.12, .18, 4), '#8A6A3A', 0, 1.9, 0, { r: [0, Math.PI / 4, 0] });
    for (let i = 0; i < 16; i++){ const a = i / 16 * Math.PI * 2; M(box(.1, .14, .01), C.thatch, Math.cos(a) * .66, 1.19, Math.sin(a) * .47, { r: [0, -a + hz, 0], cast: false }); }
    const hm = G(0, .78, 0, 0, ROOT); for (let i = 0; i < 9; i++){ const t = i / 8, x = -.4 + t * .8, y = -Math.sin(t * Math.PI) * .16; M(box(.11, .015, .24), i % 2 ? '#D9483A' : '#2E6FA8', x, y, 0, { p: hm, r: [0, 0, Math.cos(t * Math.PI) * .45] }); }
    for (const sg of [-1, 1]) M(cyl(.004, .004, .2, 3), '#4A2F1E', sg * .45, .06, 0, { p: hm, r: [0, 0, sg * .5] });
    M(cyl(.004, .004, .1, 3), '#4A2F1E', .4, 1.12, .3); M(sph(.06, 8, 6), MS('#D9483A', { emissive: '#B4432E', emissiveIntensity: .35 }), .4, 1.03, .3, { s: [1, 1.2, 1] }); M(cyl(.03, .03, .02, 6), gold, .4, .96, .3); },
  mieu(){ // miếu Ông Địa: bệ hai cấp tô đá, thân vàng nhạt, cửa đỏ, hai cột đỏ, mái ngói hai tầng đầu đao cong, hồ lô vàng, bát nhang, đĩa trái cây, cây chuối nhỏ
    M(box(.95, .14, .66), mortar, 0, .07, 0); M(box(.78, .12, .54), '#E8DCC2', 0, .2, 0); M(box(.36, .05, .14), mortar, 0, .025, .36);
    M(box(.56, .46, .4), '#EAD9A8', 0, .49, -.02); M(box(.24, .32, .02), '#5A2A1A', 0, .44, .19); M(box(.28, .04, .03), gold, 0, .62, .19); for (const x of [-.13, .13]) M(box(.01, .3, .015), gold, x, .44, .2, { cast: false });
    for (const sg of [-1, 1]){ M(cyl(.035, .04, .48, 8), '#B4432E', sg * .3, .5, .19); M(box(.05, .3, .01), '#F2D27A', sg * .3, .52, .23, { cast: false }); }
    const roof = (y, w, d, k) => { for (const sg of [-1, 1]) M(box(w, .04, d), k ? tileD : tile, 0, y, sg * d * .38, { r: [sg * .5, 0, 0] }); M(box(w + .04, .05, .05), tileD, 0, y + .1, 0); for (const sx of [-1, 1]) for (const sz of [-1, 1]) M(cone(.035, .14, 5), gold, sx * w / 2, y + .02, sz * d * .62, { r: [sz * .7, 0, sx * -.9] }); };
    roof(.8, .78, .56, 0); roof(.98, .56, .42, 1); M(sph(.05, 8, 6), gold, 0, 1.13, 0, { s: [1, 1.3, 1] }); M(sph(.035, 8, 6), gold, 0, 1.2, 0);
    M(cyl(.06, .05, .06, 10), gold, 0, .29, .36); for (const x of [-.02, 0, .02]){ M(cyl(.003, .003, .14, 3), '#9C3620', x, .37, .36, { cast: false }); M(sph(.008, 4, 3), glow, x, .44, .36, { cast: false }); }
    M(cyl(.07, .06, .02, 10), '#EDE6D6', -.2, .27, .32); for (let i = 0; i < 4; i++) M(sph(.025, 6, 5), pick(['#E8C23A', '#D9483A', '#7DB84A', '#F08A3A']), -.2 + (i % 2 - .5) * .04, .3 + (i > 1 ? .03 : 0), .32 + (i % 2) * .02, { cast: false });
    M(cyl(.03, .035, .45, 6), '#7A9A4A', .52, .22, -.2); for (let i = 0; i < 5; i++) M(box(.07, .006, .32), pick(['#4F8A44', '#5E9A4E']), .52, .45 + i * .015, -.2, { r: [R(-.6, .6), i * 1.25, .7], cast: false }); }
  }; })();
'''
rep("function dcModel(k){ const g = new T.Group(), pr = ROOT; ROOT = g;", JS + "function dcModel(k){ const g = new T.Group(), pr = ROOT; ROOT = g;\n  if (DCX[k]){ DCX[k](); ROOT = pr; return g; }")
rep("const BUILD = 'v112a'", "const BUILD = 'v113d'")
rep("const DCV = { ga: null,", "window.__UIC = UIC; const DCV = { ga: null,")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
