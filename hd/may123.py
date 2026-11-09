# may123: nền cho tiệm may cô Ba (hình mẫu, chưa có giao diện tiệm). Chạy sau fix122.py.
# - FABM(vải, màu, hoa văn): vật liệu vải có kết cấu: bong (vải bông, mặt sợi), xita (màu tươi), lua (lụa, có vệt bóng),
#   lanh (lãnh Mỹ A: đen tuyền, bóng). Hoa văn: tron, bongnhi (bông nhí), soc (sọc).
# - avBuild nhận thêm: cut 'om' (bà ba ôm eo, tà dài, không túi) | 'suong' (suông, cổ trụ, 2 túi); tay 'dai';
#   fab/pat cho áo, pfab cho quần; khan [màu 1, màu 2] (khăn rằn quàng cổ); hat 'nonla' | 'taibeo' | 'phot'.
# - Ngoại: NGOAIB(OF) dựng lại bộ hình Ngoại theo đồ: ao, fab, pat, khan [2 màu], hat 'non' | 'khan', quan 'lanh'.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a))
    s = s.replace(a, b)

FAB = r"""const FABC = {}; function FABM(fab, col, pat = 'tron'){ const key = fab + col + pat; if (FABC[key]) return FABC[key];
  const cv = document.createElement('canvas'); cv.width = cv.height = 64; const x = cv.getContext('2d'), base = fab === 'lanh' ? '#1A181E' : col; x.fillStyle = base; x.fillRect(0, 0, 64, 64);
  const lt = new T.Color(base).lerp(new T.Color('#ffffff'), .6).getStyle(), dkc = new T.Color(base).multiplyScalar(.82).getStyle();
  if (fab === 'bong'){ x.fillStyle = dkc; for (let i = 0; i < 64; i += 4) x.fillRect(0, i, 64, 1); x.globalAlpha = .5; for (let i = 0; i < 64; i += 4) x.fillRect(i, 0, 1, 64); x.globalAlpha = 1; }   /* mặt sợi vải bông */
  if (pat === 'bongnhi') for (let i = 0; i < 9; i++){ const px = (i * 23 + (i % 3) * 7) % 60 + 2, py = (i * 37 + 5) % 60 + 2; x.fillStyle = lt; for (let k = 0; k < 5; k++){ const a = k / 5 * 6.283; x.beginPath(); x.arc(px + Math.cos(a) * 2.6, py + Math.sin(a) * 2.6, 1.8, 0, 6.283); x.fill(); } x.fillStyle = '#F2C850'; x.beginPath(); x.arc(px, py, 1.3, 0, 6.283); x.fill(); }
  if (pat === 'soc'){ x.fillStyle = lt; for (let i = 0; i < 64; i += 16) x.fillRect(i, 0, 4, 64); x.fillStyle = dkc; for (let i = 8; i < 64; i += 16) x.fillRect(i, 0, 1, 64); }
  if (fab === 'lua' || fab === 'lanh'){ const g = x.createLinearGradient(0, 0, 64, 64); const hi = fab === 'lanh' ? 'rgba(150,150,175,.32)' : 'rgba(255,255,255,.3)'; g.addColorStop(0, 'rgba(255,255,255,0)'); g.addColorStop(.25, 'rgba(255,255,255,0)'); g.addColorStop(.5, hi); g.addColorStop(.75, 'rgba(255,255,255,0)'); g.addColorStop(1, 'rgba(255,255,255,0)'); x.fillStyle = g; x.fillRect(0, 0, 64, 64); }   /* vệt bóng của lụa, lãnh */
  const tx = new T.CanvasTexture(cv); tx.colorSpace = T.SRGBColorSpace; tx.wrapS = tx.wrapT = T.RepeatWrapping; tx.repeat.set(pat === 'soc' ? 3 : fab === 'lua' || fab === 'lanh' ? 1 : 2, pat === 'soc' || pat === 'bongnhi' || fab === 'bong' ? 2 : 1);
  return FABC[key] = new T.MeshStandardMaterial({ color: '#ffffff', map: tx, flatShading: true, roughness: fab === 'lua' || fab === 'lanh' ? .45 : .9, side: T.DoubleSide }); }
"""
rep("const NGOAI = (() => { const OUT = {};", FAB + "const NGOAIB = (OF = {}) => { const OUT = {};")
rep("ri.renderLists.dispose(); return OUT; })();\n\n $('#icCho')", "ri.renderLists.dispose(); return OUT; }; const NGOAI = NGOAIB();\n\n $('#icCho')")
rep("AO = '#8A5D3B', AOD = '#6B4529', QUAN = '#2B3446';",
    "AO0 = OF.ao || '#8A5D3B', AO = OF.fab ? FABM(OF.fab, AO0, OF.pat) : AO0, AOD = '#6B4529', QUAN = OF.quan === 'lanh' ? FABM('lanh', '#1A181E') : '#2B3446', KA = (OF.khan || [])[0] || '#2B3446', KB = (OF.khan || [])[1] || '#FBF7EE';")
rep("k % 2 ? QUAN : '#FBF7EE'", "k % 2 ? KA : KB", 3)
rep("const h = head(j, HAIRS.non)", "const h = head(j, HAIRS[OF.hat || 'non'])", 2)
rep("const h = head(g, HAIRS.non)", "const h = head(g, HAIRS[OF.hat || 'non'])", 2)

# nhân vật người chơi
rep("btn = a.shirt === '#EFE6D2' ? '#8A5D3B' : '#FBF7EE';",
    "btn = a.shirt === '#EFE6D2' ? '#8A5D3B' : '#FBF7EE', SH = a.fab ? FABM(a.fab, a.shirt, a.pat) : a.shirt, PN = a.pfab ? FABM(a.pfab, a.pants) : a.pants, OM = a.cut === 'om', SU = a.cut === 'suong';")
rep("M(cyl(.095, .125, .26, 8), a.pants, 0, -.12, 0, { p: lg });", "M(cyl(.095, OM ? .135 : .125, .26, 8), PN, 0, -.12, 0, { p: lg });")
rep("else { M(ball(.24, 1), a.shirt, 0, .46, 0, { p: g, s: [1, .95, .86] }); M(cyl(.21, .245, .1, 9), a.shirt, 0, .31, 0, { p: g });",
    "else { M(ball(.24, 1), SH, 0, .46, 0, { p: g, s: OM ? [.95, .97, .84] : [1, .95, .86] }); M(cyl(OM ? .185 : .21, OM ? .215 : .245, .1, 9), SH, 0, .31, 0, { p: g });\n"
    "      if (SU) M(new T.CylinderGeometry(.078, .084, .055, 14, 1, true), dk, 0, .655, .03, { p: g, r: [-.3, 0, 0], ds: true, cast: false });   /* cổ trụ áo bà ba nam */")
rep("for (const sx of [-1, 1]){ M(box(.075, .065, .014), dk, sx * .11, .32, .198,", "if (!OM) for (const sx of [-1, 1]){ M(box(.075, .065, .014), dk, sx * .11, .32, .198,")
rep("M(box(.36, .12, .03), a.open ? a.shirt : a.shirt, 0, .225, fz * .155, { p: g, r: [fz * -.12, 0, 0] });",
    "M(box(OM ? .3 : .36, OM ? .17 : .12, .03), a.open ? a.shirt : SH, 0, OM ? .2 : .225, fz * (OM ? .118 : .155), { p: g, r: [fz * (OM ? -.03 : -.12), 0, 0] });")
rep("M(ball(.075, 1), a.shirt, 0, 0, 0, { p: ar }); M(cyl(.058, .066, .2, 7), SKN, 0, -.11, 0, { p: ar }); M(cyl(.072, .076, .1, 8), a.shirt, 0, -.05, 0, { p: ar });",
    "M(ball(.075, 1), a.open ? a.shirt : SH, 0, 0, 0, { p: ar }); M(cyl(.058, .066, .2, 7), SKN, 0, -.11, 0, { p: ar }); M(cyl(.072, .076, .1, 8), a.open ? a.shirt : SH, 0, -.05, 0, { p: ar }); if (a.tay === 'dai') M(cyl(.07, OM ? .088 : .078, .19, 8), SH, 0, -.13, 0, { p: ar });   /* tay dài (bà ba nữ hơi loe) */")
rep("if (a.prop === 'khan'){", "if (a.prop === 'khan' || a.khan){ const KA = (a.khan || [])[0] || '#2B2522', KB = (a.khan || [])[1] || '#F2EEE4';")
rep("(k % 2) ? '#2B2522' : '#F2EEE4', .1 + Math.sin(k * .3) * .01", "(k % 2) ? KA : KB, .1 + Math.sin(k * .3) * .01")
rep("M(ball(.045, 1), k % 2 ? '#2B2522' : '#F2EEE4', -.08 + k * .07, .64", "M(ball(.045, 1), k % 2 ? KA : KB, -.08 + k * .07, .64")
rep("if (o.hatOn){ const n = G(0, 1.23, -.02, 0, g);", "if (o.hatOn || a.hat === 'nonla'){ const n = G(0, 1.23, -.02, 0, g);")
rep("M(new T.TorusGeometry(.405, .012, 3, 24), '#B8862E', 0, -.105, 0, { p: n, r: [Math.PI / 2, 0, 0], cast: false }); }\n",
    "M(new T.TorusGeometry(.405, .012, 3, 24), '#B8862E', 0, -.105, 0, { p: n, r: [Math.PI / 2, 0, 0], cast: false }); }\n"
    "  if (a.hat === 'taibeo'){ const n = G(0, 1.13, -.03, 0, g); n.rotation.set(-.12, 0, -.04); M(cyl(.27, .3, .16, 12), '#6E7A4A', 0, .08, 0, { p: n }); M(cyl(.27, .27, .02, 12), '#5E6A3E', 0, .165, 0, { p: n }); M(new T.CylinderGeometry(.3, .44, .08, 16, 1, true), '#6E7A4A', 0, -.02, 0, { p: n, ds: true }); for (let k = 0; k < 2; k++) M(new T.TorusGeometry(.3 + k * .07, .006, 3, 16), '#4E5A30', 0, .0 - k * .035, 0, { p: n, r: [Math.PI / 2, 0, 0], cast: false }); }   /* nón tai bèo */\n"
    "  if (a.hat === 'phot'){ const n = G(0, 1.15, -.03, 0, g); n.rotation.set(-.1, 0, -.04); M(cyl(.23, .27, .19, 12), '#5A4030', 0, .1, 0, { p: n }); M(box(.2, .03, .3), '#4A3326', 0, .2, 0, { p: n }); M(cyl(.272, .272, .045, 12), '#2B2522', 0, .03, 0, { p: n }); M(cyl(.42, .42, .02, 18), '#5A4030', 0, .0, 0, { p: n, s: [1, 1, .9] }); }   /* mũ phớt */\n")
s = s.replace("BUILD = 'v122a'", "BUILD = 'v123a'")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
