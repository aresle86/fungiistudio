/* Thông số 30 loài cá cho khuôn fish2/tom2. prof: [u, nửa cao, nửa dày, tâm y] từ cuống đuôi tới mũi.
   Mỗi loài có một nét nhận dạng riêng (ghi ở chú thích) để nhìn hình là biết, không lẫn nhau. */
const FHZ = (u, t) => { const x = Math.sin(u * 91.7 + t * 47.3) * 43758.5; return x - Math.floor(x); };
const FBAR = (n, c, u0 = .15, u1 = .75, yMin = -.4, w = .45) => (u, t, y) => y > yMin && u > u0 && u < u1 && ((u - u0) / (u1 - u0) * n) % 1 < w ? c : null;
const FSCALE = (c, a = 22, b = 3.2) => (u, t, y) => ((Math.floor(u * a) + Math.floor((t + 3) * b)) % 2 === 0 && y > -.5) ? c : null;
const FANY = (...fs) => (u, t, y) => { for (const f of fs){ const c = f(u, t, y); if (c) return c; } return null; };
const DEEP = [[0, .035, .02, 0], [.15, .055, .03, .005], [.45, .13, .055, .015], [.7, .13, .058, .01], [.88, .09, .052, 0], [1, .05, .036, -.01]];
const SLIM = [[0, .03, .02, 0], [.2, .045, .032, 0], [.55, .075, .045, .004], [.8, .068, .045, 0], [.94, .045, .036, -.006], [1, .025, .024, -.01]];
const LONG = [[0, .026, .022, 0], [.2, .04, .034, 0], [.5, .05, .042, 0], [.8, .05, .046, 0], [.94, .038, .04, -.004], [1, .02, .026, -.008]];
const CATF = [[0, .03, .02, 0], [.2, .048, .032, 0], [.55, .085, .055, .006], [.8, .075, .062, -.004], [.93, .05, .058, -.012], [1, .028, .04, -.018]];
const FSPEC = {
  /* rô đồng: thân dày, vây lưng gai, đuôi tròn, sọc mờ, đốm đen cuống đuôi */
  caro: o => fish2(o, { back: '#55633A', side: '#87955A', belly: '#E2D9A4', fin: '#7E8A55', nose: .86, prof: [[0, .035, .02, 0], [.15, .052, .03, .005], [.45, .12, .056, .012], [.7, .118, .06, .01], [.88, .088, .055, 0], [1, .05, .04, -.01]],
    pat: FBAR(5, '#6A7844', .18, .7), spots: [[.08, .15, .02, '#22281A']], dorsal: [[.3, .68, .07, .055, 'spiny'], [.18, .3, .06, .05, 'round']], anal: [[.12, .38, .05, .04, 'round']], tail: 'round', tailL: .17,
    pect: [.7, -.2, .1, .06], pelv: [.62, -.8, .07, .04], eye: .03, eyeU: .87, eyeT: .35, gillU: .74, mouthT: -.2 }),
  /* sặc rằn: thân bầu dục dẹp, sọc rằn ri chạy dọc giữa hông, sợi vây bụng dài */
  sacran: o => fish2(o, { back: '#5C6A3E', side: '#9AA46C', belly: '#E4DCA8', fin: '#7A8458', nose: .88, prof: [[0, .03, .016, 0], [.15, .06, .024, .004], [.45, .135, .04, .01], [.72, .125, .042, .006], [.9, .08, .036, 0], [1, .04, .026, -.01]],
    pat: (u, t, y) => Math.abs(y - .05 - Math.sin(u * 40) * .1) < .09 && u > .08 && u < .82 && (u * 22) % 1 < .7 ? '#56603A' : (y > -.4 && (u * 11) % 1 < .18 && u > .1 && u < .8 ? '#6E7A4A' : null), dorsal: [[.32, .5, .05, .045, 'round']], anal: [[.08, .62, .06, .05, 'round']], tail: 'fork', tailL: .14,
    pect: [.72, -.15, .08, .05], threads: [.66, .34], eye: .03, eyeU: .88, eyeT: .3, mouthT: .1, mouthL: .04 }),
  /* sặc bướm: xanh lam óng, vạch sóng mờ, hai đốm đen (giữa thân và cuống đuôi), sợi vây bụng */
  sacbuom: o => fish2(o, { back: '#3E5E72', side: '#7FA2B6', belly: '#D8E2E2', fin: '#6A8EA4', nose: .88, prof: [[0, .03, .016, 0], [.15, .058, .024, .004], [.45, .13, .04, .01], [.72, .12, .042, .006], [.9, .078, .036, 0], [1, .04, .026, -.01]],
    pat: FBAR(7, '#5A7C92', .12, .78, -.6, .3), spots: [[.46, .05, .028, '#141E26'], [.1, .05, .022, '#141E26']], dorsal: [[.32, .5, .05, .045, 'round']], anal: [[.08, .62, .06, .05, 'round']], analEdge: '#E8A050', tail: 'fork', tailL: .14,
    pect: [.72, -.15, .08, .05], threads: [.66, .34], threadCol: '#E8A050', eye: .03, eyeU: .88, eyeT: .3, eyeRim: '#E86A4A', mouthT: .1, mouthL: .04 }),
  /* rô phi: thân sâu, vây lưng gai dài liền, sọc đứng sẫm, đuôi bằng có vạch */
  rophi: o => fish2(o, { back: '#56636A', side: '#8A9698', belly: '#D6DAD2', fin: '#6E7A80', nose: .86, prof: DEEP,
    pat: FBAR(6, '#606C72', .15, .72, -.55, .4), dorsal: [[.24, .74, .075, .06, 'spiny']], anal: [[.12, .36, .055, .045, 'round']], tail: 'round', tailL: .15, tailRay: '#3A4448', tailEdge: '#C9584A',
    pect: [.7, -.15, .11, .06], pelv: [.64, -.8, .08, .04], eye: .032, eyeU: .87, eyeT: .38, mouthT: -.05, gillU: .73 }),
  /* diếc: thân sâu ánh đồng, vảy to, đuôi chẻ, vây lưng dài */
  diec: o => fish2(o, { back: '#7A6A3E', side: '#C2A868', belly: '#ECDDB0', fin: '#A88E58', nose: .85, prof: DEEP,
    pat: FSCALE('#AE9458', 20, 3), dorsal: [[.3, .68, .07, .04, 'round']], anal: [[.14, .3, .055, .03, 'round']], tail: 'fork', tailL: .17,
    pect: [.72, -.25, .09, .05], pelv: [.6, -.85, .07, .04], eye: .028, eyeU: .88, eyeT: .3, mouthT: -.1 }),
  /* mè vinh: thân rất sâu dẹp bạc trắng, vây lưng cao phía trước, đuôi chẻ sâu, vây cam */
  mevinh: o => fish2(o, { back: '#8A949A', side: '#D2D8DA', belly: '#F2F2EC', fin: '#E89A4A', nose: .86, prof: [[0, .032, .016, 0], [.15, .065, .022, .006], [.45, .16, .038, .02], [.7, .15, .04, .012], [.88, .095, .034, 0], [1, .05, .024, -.01]],
    pat: FSCALE('#C2C8CA', 22, 3.4), dorsal: [[.5, .66, .14, 0, 'sail']], anal: [[.12, .28, .06, .03, 'round']], tail: 'fork', tailL: .2, tailCol: '#E2A24E',
    pect: [.72, -.35, .1, .05], pelv: [.56, -.85, .08, .04], pelvCol: '#E2A24E', eye: .03, eyeU: .88, eyeT: .25, mouthT: -.05 }),
  /* chốt: mảnh vàng nâu, vây lưng có gai nhọn, vây mỡ dài, 4 đôi râu, đốm sẫm sau mang */
  chot: o => fish2(o, { back: '#8A6E30', side: '#C9A44A', belly: '#ECDCAA', fin: '#B08C48', nose: .9, prof: CATF,
    spots: [[.7, .25, .022, '#4A3A1A']], dorsal: [[.6, .68, .1, 0, 'sail'], [.14, .4, .025, .022, 'round']], anal: [[.12, .28, .05, .03, 'round']], tail: 'fork', tailL: .2,
    pect: [.78, -.4, .1, .045], pelv: [.52, -.85, .06, .03], eye: .024, eyeU: .9, eyeT: .25, mouthT: -.4, gillU: .78, barbels: [[.99, -.15, .2, -.2], [.985, -.55, .12, -.5], [.98, -.8, .09, -.6], [.975, -1, .08, -.6]] }),
  /* bống cát: tròn dài màu cát, hàng đốm nâu dọc hông, 2 vây lưng, mắt cao, môi dày */
  bongcat: o => fish2(o, { back: '#9C8A60', side: '#CDB98C', belly: '#EFE4C6', fin: '#B8A47A', nose: .9, prof: [[0, .03, .025, 0], [.2, .045, .038, 0], [.55, .062, .05, 0], [.8, .062, .055, 0], [.93, .05, .05, .004], [1, .03, .03, -.004]],
    pat: (u, t, y) => Math.abs(y - .05) < .18 && u > .08 && u < .8 && (u * 11) % 1 < .38 ? '#7A5A34' : (y > .5 && FHZ(u, t) > .7 ? '#8A7448' : null), dorsal: [[.55, .7, .06, .05, 'round'], [.2, .48, .055, .05, 'round']], anal: [[.18, .45, .045, .04, 'round']], tail: 'round', tailL: .15,
    pect: [.72, -.4, .1, .06], pelv: [.68, -.95, .06, .04], eye: .03, eyeU: .9, eyeT: .7, mouthT: -.25, mouthL: .07 }),
  /* tép bạc: tôm nhỏ màu trong ngà, càng ngắn */
  tep: o => tom2(o, { tep: true, body2: '#F0E6D4', body: '#E8DCC6', dark: '#CDBEA2', claw: '#D8C8AC', joint: '#F0A07A', leg: '#E2D4BC' }),
  /* he: bạc ánh vàng, vây đỏ tươi, đuôi và vây lưng viền đen */
  he: o => fish2(o, { back: '#9A9466', side: '#D8D2A4', belly: '#F2EED6', fin: '#E0503A', nose: .86, prof: [[0, .032, .016, 0], [.15, .062, .022, .006], [.45, .145, .038, .018], [.7, .14, .04, .012], [.88, .09, .034, 0], [1, .05, .024, -.01]],
    pat: FSCALE('#C8C090', 22, 3.4), dorsal: [[.5, .66, .13, 0, 'sail']], dorsalEdge: '#1E1E1E', anal: [[.12, .28, .06, .03, 'round']], tail: 'fork', tailL: .2, tailEdge: '#1E1E1E',
    pect: [.72, -.35, .1, .05], pelv: [.56, -.85, .08, .04], eye: .03, eyeU: .88, eyeT: .25, mouthT: -.05 }),
  /* lóc: thân dài khúc cây, vây lưng và hậu môn chạy dài, hoa văn sẫm, miệng rộng */
  caloc: o => fish2(o, { back: '#353D2C', side: '#5E6A46', belly: '#C9C6A4', fin: '#4A543A', nose: .9, prof: [[0, .036, .026, 0], [.2, .05, .04, 0], [.5, .066, .056, 0], [.8, .06, .06, -.005], [.93, .045, .056, -.01], [1, .026, .036, -.012]],
    pat: (u, t, y) => y > -.35 && y < .55 && u > .05 && u < .82 && (Math.floor(u * 13 + y * 1.6) % 2 === 0) ? '#262B1E' : null,
    dorsal: [[.06, .76, .05, .05, 'round']], anal: [[.06, .5, .045, .045, 'round']], tail: 'round', tailL: .14,
    pect: [.77, -.3, .08, .05], pelv: [.6, -.85, .05, .03], eye: .024, eyeU: .925, eyeT: .45, gillU: .8, mouthL: .09, mouthT: -.1, gillCol: '#1A1E15' }),
  /* trê vàng: đầu dẹp, vây lưng và hậu môn dài gần tới đuôi, đuôi tròn tách rời, 4 đôi râu, vàng nâu */
  catre: o => fish2(o, { back: '#6E5A26', side: '#A88C40', belly: '#E2D2A0', fin: '#8A7034', nose: .92, prof: [[0, .03, .024, 0], [.2, .045, .036, 0], [.5, .058, .05, 0], [.8, .052, .06, -.004], [.93, .04, .06, -.008], [1, .022, .04, -.01]],
    pat: (u, t, y) => y > -.2 && FHZ(u, t) > .78 ? '#8A7232' : null, dorsal: [[.08, .72, .04, .04, 'round']], anal: [[.08, .5, .035, .035, 'round']], tail: 'round', tailL: .13,
    pect: [.82, -.45, .08, .04], pelv: [.58, -.9, .05, .03], eye: .02, eyeU: .93, eyeT: .45, mouthT: -.3, gillU: .82, barbels: [[.99, -.1, .17, -.1], [.985, -.4, .14, -.3], [.98, -.75, .12, -.5], [.975, -1.05, .1, -.6]] }),
  /* thát lát: lưng gù, vây lưng bé xíu, vây hậu môn rất dài nối liền đuôi nhỏ, chấm đen hàng dưới */
  thatlat: o => fish2(o, { back: '#6E7676', side: '#A8B0AE', belly: '#E0E2DA', fin: '#8A9290', nose: .9, prof: [[0, .02, .012, -.01], [.2, .045, .022, -.012], [.5, .1, .034, .01], [.7, .11, .038, .022], [.88, .075, .034, .006], [1, .035, .022, -.01]],
    spots: [[.42, -.6, .018, '#1E2222'], [.34, -.62, .016, '#1E2222'], [.26, -.62, .014, '#1E2222']], dorsal: [[.56, .62, .045, .03, 'round']], anal: [[.02, .62, .055, .03, 'round']], tail: 'round', tailL: .07,
    pect: [.76, -.4, .08, .04], eye: .028, eyeU: .9, eyeT: .3, mouthT: -.15, gillU: .78 }),
  /* kèo: dài mảnh, mắt nằm sát đỉnh đầu, vây lưng sau dài, đuôi nhọn như mũi giáo, chấm nâu */
  keo: o => fish2(o, { back: '#6A5A42', side: '#9C8A6A', belly: '#DCD0B4', fin: '#8A7A5A', nose: .9, prof: LONG,
    pat: (u, t, y) => y > -.1 && FHZ(u * 3, t) > .72 ? '#4A3E2C' : null, dorsal: [[.58, .7, .045, .035, 'spiny'], [.08, .54, .04, .04, 'round']], anal: [[.08, .48, .035, .035, 'round']], tail: 'point', tailL: .14,
    pect: [.76, -.4, .07, .045], pelv: [.7, -1.1, .05, .035], eye: .024, eyeU: .93, eyeT: 1.05, mouthT: -.2 }),
  /* chạch: dài, mõm thịt nhọn, hàng gai lưng nhỏ, đốm mắt tròn ở chân vây lưng, sọc sáng dọc */
  chach: o => fish2(o, { back: '#6A5232', side: '#9A7E52', belly: '#DCCAA2', fin: '#8A7048', nose: .78, prof: [[0, .022, .018, 0], [.2, .036, .026, 0], [.5, .05, .034, 0], [.75, .045, .034, 0], [.9, .025, .022, -.002], [1, .008, .008, -.002]],
    pat: (u, t, y) => Math.abs(y - .1) < .1 && u > .05 && u < .85 ? '#C8B080' : null, spots: [[.32, 1.0, .018, '#1A1612'], [.22, 1.0, .016, '#1A1612'], [.42, 1.0, .016, '#1A1612']], dorsal: [[.4, .72, .025, .02, 'spiny'], [.06, .38, .035, .035, 'round']], anal: [[.06, .36, .03, .03, 'round']], tail: 'round', tailL: .08,
    pect: [.72, -.3, .05, .03], eye: .018, eyeU: .86, eyeT: .45, mouthT: -.3, mouthL: .03, gill: false }),
  /* lươn: thân tròn dài uốn sóng, không vây, đuôi nhọn, vàng nâu bụng sáng */
  luon: o => fish2(o, { back: '#6A4E1C', side: '#9A7428', belly: '#D8B868', fin: '#8A6A28', nose: .94, prof: [[0, .008, .008, .03], [.12, .022, .022, .05], [.3, .03, .03, -.02], [.5, .034, .034, -.05], [.7, .034, .034, .01], [.86, .034, .034, .04], [.95, .03, .03, .03], [1, .018, .02, .025]],
    pat: (u, t, y) => y > .2 && FHZ(u, t) > .8 ? '#5A4012' : null, dorsal: [], anal: [], tail: 'point', tailL: .02, eye: .014, eyeU: .955, eyeT: .5, mouthT: -.2, mouthL: .03, gill: false }),
  /* linh: cá nhỏ trắng bạc, đuôi chẻ ánh vàng, đốm sẫm cuống đuôi, vảy nhỏ */
  linh: o => fish2(o, { back: '#8C9898', side: '#D6DCD8', belly: '#F4F4EE', fin: '#D8C890', nose: .86, prof: SLIM,
    pat: FSCALE('#C4CCC8', 26, 3.6), spots: [[.08, .05, .018, '#4A5254']], dorsal: [[.48, .6, .08, 0, 'sail']], anal: [[.14, .28, .04, .025, 'round']], tail: 'fork', tailL: .17, tailCol: '#E2CC80',
    pect: [.74, -.35, .08, .04], pelv: [.55, -.85, .06, .035], eye: .028, eyeU: .88, eyeT: .2, mouthT: -.05 }),
  /* lăng: đầu dẹp, râu hàm rất dài, vây mỡ to, đuôi chẻ, xám nâu */
  lang: o => fish2(o, { back: '#5A6068', side: '#8C9298', belly: '#DCDCD4', fin: '#70767E', nose: .9, prof: CATF,
    dorsal: [[.6, .68, .1, 0, 'sail'], [.12, .42, .05, .04, 'round']], anal: [[.12, .26, .05, .03, 'round']], tail: 'fork', tailL: .2,
    pect: [.78, -.4, .1, .045], pelv: [.5, -.85, .06, .03], eye: .022, eyeU: .9, eyeT: .3, mouthT: -.4, gillU: .78, barbels: [[.99, -.1, .36, -.15], [.985, -.55, .12, -.5], [.98, -.85, .09, -.6]] }),
  /* ngát: nâu sẫm, vây lưng sau, vây hậu môn và đuôi liền thành một dải nhọn, 4 đôi râu */
  ngat: o => fish2(o, { back: '#3A3632', side: '#5E5852', belly: '#CFC8BC', fin: '#4A4540', nose: .9, prof: [[0, .02, .014, 0], [.2, .045, .028, 0], [.5, .068, .046, .004], [.8, .065, .058, -.004], [.93, .045, .055, -.012], [1, .025, .036, -.016]],
    dorsal: [[.62, .7, .08, 0, 'sail'], [0, .5, .045, .03, 'round']], anal: [[0, .44, .045, .03, 'round']], tail: 'point', tailL: .1,
    pect: [.78, -.45, .09, .04], pelv: [.5, -.9, .05, .03], eye: .02, eyeU: .92, eyeT: .35, mouthT: -.35, gillU: .79, barbels: [[.99, -.1, .14, -.1], [.985, -.45, .12, -.3], [.98, -.8, .1, -.5], [.975, -1.1, .09, -.6]] }),
  /* chép: vàng đồng, vảy to rõ, vây lưng dài, 2 đôi râu ngắn ở mép, đuôi chẻ */
  chep: o => fish2(o, { back: '#8A6418', side: '#D29A30', belly: '#F2D898', fin: '#B47A28', nose: .86, prof: [[0, .035, .02, 0], [.15, .056, .03, .005], [.45, .12, .054, .016], [.7, .118, .058, .012], [.88, .085, .052, 0], [1, .045, .036, -.012]],
    pat: FSCALE('#B47E24', 16, 2.6), dorsal: [[.28, .66, .07, .035, 'round']], anal: [[.14, .26, .05, .03, 'round']], tail: 'fork', tailL: .18, tailCol: '#C27A30',
    pect: [.72, -.3, .1, .05], pelv: [.58, -.85, .07, .04], eye: .026, eyeU: .88, eyeT: .3, mouthT: -.25, barbels: [[.99, -.25, .04, -.4], [.975, -.4, .035, -.5]] }),
  /* tôm càng xanh */
  tomcang: o => tom2(o),
  /* chành dục: lóc nhỏ nâu hoa, vây viền cam */
  chanhduc: o => fish2(o, { back: '#4E3E2A', side: '#7E6646', belly: '#D4C4A0', fin: '#5E4A34', nose: .9, prof: [[0, .036, .026, 0], [.2, .05, .04, 0], [.5, .066, .056, 0], [.8, .06, .06, -.005], [.93, .045, .056, -.01], [1, .026, .036, -.012]],
    pat: (u, t, y) => y > -.4 && (FHZ(u * 2, t) > .62 || (u * 9) % 1 < .12) ? '#3A2C1C' : null, dorsal: [[.06, .74, .05, .05, 'round']], dorsalEdge: '#E8803A', anal: [[.06, .5, .045, .045, 'round']], analEdge: '#E8803A', tail: 'round', tailL: .14, tailEdge: '#E8803A',
    pect: [.77, -.3, .08, .05], pelv: [.6, -.85, .05, .03], eye: .026, eyeU: .925, eyeT: .45, gillU: .8, mouthL: .08, mouthT: -.1 }),
  /* bống tượng: đầu to bè, miệng rộng, hoa vân đá nâu, 2 vây lưng, đuôi tròn */
  bongtuong: o => fish2(o, { back: '#4E3E26', side: '#86704A', belly: '#D8C8A0', fin: '#6A5838', nose: .88, prof: [[0, .036, .026, 0], [.2, .05, .04, 0], [.5, .07, .06, .004], [.75, .085, .08, .004], [.9, .075, .078, -.004], [1, .042, .05, -.012]],
    pat: (u, t, y) => y > -.5 && FHZ(Math.floor(u * 14), Math.floor(t * 3)) > .55 ? '#3A2C18' : null, dorsal: [[.48, .62, .06, .05, 'round'], [.16, .44, .06, .055, 'round']], anal: [[.16, .4, .05, .045, 'round']], tail: 'round', tailL: .16,
    pect: [.72, -.35, .12, .07], pelv: [.68, -.95, .07, .05], eye: .028, eyeU: .9, eyeT: .6, gillU: .74, mouthL: .11, mouthT: -.15 }),
  /* bông lau: tra mảnh bạc sáng, mõm dài, vây lưng và đuôi chót vàng */
  bonglau: o => fish2(o, { back: '#7A8894', side: '#B8C2CA', belly: '#F0F2F0', fin: '#C8B860', nose: .84, prof: [[0, .028, .016, 0], [.2, .046, .028, 0], [.55, .085, .048, .006], [.78, .078, .05, 0], [.92, .05, .04, -.012], [1, .022, .022, -.02]],
    dorsal: [[.58, .67, .11, 0, 'sail'], [.2, .26, .02, .016, 'round']], anal: [[.1, .4, .04, .03, 'round']], tail: 'fork', tailL: .23, tailCol: '#C8B860',
    pect: [.74, -.35, .1, .045], pelv: [.5, -.85, .06, .03], eye: .022, eyeU: .89, eyeT: 0, mouthT: -.4, gillU: .76, barbels: [[.985, -.3, .05, -.3]] }),
  /* tra lớn: vây lưng cao nhọn, vây mỡ nhỏ, đuôi chẻ sâu, bụng trắng, 2 đôi râu ngắn, mắt thấp */
  tra: o => fish2(o, { back: '#46525C', side: '#8C98A2', belly: '#E6EAEA', fin: '#7C8892', nose: .88, prof: [[0, .03, .018, 0], [.2, .05, .03, 0], [.55, .1, .055, .006], [.78, .09, .055, 0], [.93, .06, .045, -.01], [1, .035, .03, -.016]],
    dorsal: [[.6, .69, .12, 0, 'sail'], [.2, .27, .022, .018, 'round']], anal: [[.08, .46, .04, .03, 'round']], tail: 'fork', tailL: .23,
    pect: [.75, -.35, .11, .05], pelv: [.5, -.85, .06, .03], eye: .022, eyeU: .905, eyeT: -.05, gillU: .78, mouthT: -.35,
    barbels: [[.985, -.3, .06, -.3], [.975, -.65, .045, -.6]] }),
  /* cá dứa: lưng xanh rêu, sọc sẫm chạy dọc giữa hông, mõm nhọn, râu ngắn */
  cadua: o => fish2(o, { back: '#4E6A42', side: '#B4C0B6', belly: '#F2F4EE', fin: '#8A9A80', nose: .84, prof: [[0, .028, .016, 0], [.2, .046, .028, 0], [.55, .088, .05, .006], [.78, .08, .05, 0], [.92, .05, .04, -.012], [1, .022, .022, -.02]],
    pat: (u, t, y) => Math.abs(y - .1) < .085 && u > .02 && u < .8 ? '#2A3830' : null, dorsal: [[.58, .67, .11, 0, 'sail'], [.2, .26, .02, .016, 'round']], anal: [[.1, .4, .04, .03, 'round']], tail: 'fork', tailL: .23,
    pect: [.74, -.35, .1, .045], pelv: [.5, -.85, .06, .03], eye: .022, eyeU: .89, eyeT: .1, mouthT: -.4, gillU: .76, barbels: [[.985, -.3, .06, -.3]] }),
  /* cá hú: đầu tròn, xám sẫm, mỗi thùy đuôi có sọc đen, đốm đen chân vây ngực */
  hu: o => fish2(o, { back: '#363E44', side: '#6E7A82', belly: '#E0E4E2', fin: '#5E6A72', nose: .8, prof: [[0, .032, .018, 0], [.2, .058, .032, .002], [.5, .108, .058, .008], [.75, .108, .064, .004], [.9, .09, .062, -.004], [1, .07, .05, -.01]],
    extra: (g, k) => { const x0 = -k.L + .03, cy = k.at(0, 3), hp = k.at(0, 1), Lt = .23; for (const sg of [-1, 1]){ const a = [x0 - Lt * .15, cy + sg * hp * 1.05], b = [x0 - Lt * .92, cy + sg * (hp + Lt * .72)], dx = b[0] - a[0], dy = b[1] - a[1], l = Math.hypot(dx, dy); for (const z of [-.0024, .0024]){ const q = add(g, new T.PlaneGeometry(l, .018), '#12171A', (a[0] + b[0]) / 2, (a[1] + b[1]) / 2, z); q.rotation.z = Math.atan2(dy, dx); } } },
    spots: [[.76, -.45, .022, '#141A1E']], dorsal: [[.6, .68, .1, 0, 'sail'], [.2, .27, .022, .018, 'round']], anal: [[.08, .44, .04, .03, 'round']], tail: 'fork', tailL: .23, tailRay: '#141A1E',
    pect: [.72, -.4, .1, .05], pelv: [.5, -.85, .06, .03], eye: .026, eyeU: .88, eyeT: .1, mouthT: -.35, gillU: .78, barbels: [[.985, -.3, .06, -.3], [.975, -.65, .045, -.6]] }),
  /* rô đầu vàng: dáng rô đồng, đầu vàng óng, vây đỏ cam */
  rodauvang: o => fish2(o, { back: '#4A5A2E', side: '#7E8E4C', belly: '#E8DCA0', fin: '#D8603A', nose: .86, prof: [[0, .035, .02, 0], [.15, .052, .03, .005], [.45, .12, .056, .012], [.7, .118, .06, .01], [.88, .088, .055, 0], [1, .05, .04, -.01]],
    pat: (u, t, y) => u > .76 ? (y > -.2 ? '#F0C030' : '#F6DA70') : FBAR(5, '#5E6E3A', .18, .7)(u, t, y), spots: [[.08, .15, .02, '#22281A']], dorsal: [[.3, .68, .07, .055, 'spiny'], [.18, .3, .06, .05, 'round']], anal: [[.12, .38, .05, .04, 'round']], tail: 'round', tailL: .17,
    pect: [.7, -.2, .1, .06], pelv: [.62, -.8, .07, .04], eye: .03, eyeU: .87, eyeT: .35, eyeRim: '#F8E8A0', gillU: .74, gillCol: '#B88A20', mouthT: -.2 }),
  /* lóc bông khổng lồ: đầu to, đen tuyền điểm mảng trắng ngà, vây viền cam */
  locbong: o => fish2(o, { back: '#22201A', side: '#3A372E', belly: '#C8C0A8', fin: '#2E2B24', nose: .9, prof: [[0, .036, .026, 0], [.2, .052, .042, 0], [.5, .072, .062, 0], [.8, .07, .07, -.005], [.93, .055, .066, -.01], [1, .03, .042, -.012]],
    pat: (u, t, y) => y > -.3 && y < .7 && FHZ(Math.floor(u * 16), Math.floor(t * 4)) > .72 ? '#D8D0B8' : null, dorsal: [[.06, .76, .055, .055, 'round']], dorsalEdge: '#E0702E', anal: [[.06, .5, .05, .05, 'round']], analEdge: '#E0702E', tail: 'round', tailL: .15, tailEdge: '#E0702E',
    pect: [.77, -.3, .09, .055], pelv: [.6, -.85, .06, .035], eye: .028, eyeU: .925, eyeT: .45, eyeRim: '#E0702E', gillU: .79, mouthL: .1, mouthT: -.1 }),
  /* cá hô: khổng lồ đầu rất to (gần nửa thân), miệng hớt lên, vảy lớn ánh đồng xám */
  caho: o => fish2(o, { back: '#5E6A64', side: '#9AA49C', belly: '#E0E2D6', fin: '#6E7A72', nose: .82, prof: [[0, .035, .02, 0], [.15, .055, .03, .005], [.4, .11, .055, .012], [.62, .14, .07, .01], [.82, .135, .075, .01], [.94, .1, .065, .02], [1, .06, .045, .03]],
    pat: FSCALE('#848E88', 14, 2.4), dorsal: [[.36, .58, .09, .04, 'round']], anal: [[.12, .26, .05, .03, 'round']], tail: 'fork', tailL: .19,
    pect: [.66, -.4, .11, .06], pelv: [.5, -.85, .08, .045], eye: .026, eyeU: .9, eyeT: .3, gillU: .66, mouthT: .35, mouthL: .07 }) };
