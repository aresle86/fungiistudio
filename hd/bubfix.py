#!/usr/bin/env python3
"""Bong bóng trên vật thể kiểu ghim sticker: đĩa kem tròn mịn, vòng màu dày theo nghĩa (xanh có đồ lấy, cam việc cần làm, đỏ gấp),
viền nâu đậm ngoài, mũi nhọn nằm đúng giữa cùng màu vòng; dưới bong bóng có thanh tiến độ cho việc đang chờ (dựng, lợp mái, sửa nhà, đóng ghe).
Dùng: python3 bubfix.py <vào> <ra>."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b):
    global s
    c = s.count(a); assert c == 1, (c, a[:100]); s = s.replace(a, b)
rep("""function bubbleK(kind){ const g = DYN(G(0, 0, 0)); g.scale.setScalar(.9); const hot = kind === 'h', col = kind === 'h' ? '#C9952A' : kind === 's' ? '#6E9F57' : kind === 'u' || kind === 'p' ? '#C24A2E' : '#D2A57E';
  M(cyl(.19, .19, .05, 10), '#FBF7EE', 0, 0, 0, { p: g, r: [Math.PI / 2, 0, 0], cast: false }); M(new T.TorusGeometry(.19, .025, 4, 10), col, 0, 0, 0, { p: g, cast: false }).rotation.z = Math.PI / 10;
  M(cone(.06, .13, 4), col, 0, -.24, 0, { p: g, r: [Math.PI, 0, 0], cast: false }); const ic = G(0, 0, .05, 0, g);""",
"""function bubbleK(kind){ const g = DYN(G(0, 0, 0)); g.scale.setScalar(.9); const hot = kind === 'h', col = BUBC[kind === 'h' ? 'lay' : kind === 'u' || kind === 'p' ? 'gap' : 'lam'], BN = '#4A2F1E', MB = c => new T.MeshBasicMaterial({ color: c });   /* màu phẳng như sticker, không bị đèn làm xám */   /* ghim sticker: màu vòng nói nghĩa */
  M(new T.CircleGeometry(.205, 32), MB('#FFFBF2'), 0, 0, .012, { p: g, cast: false }).userData.ro = 2; const ring = M(new T.RingGeometry(.2, .245, 40), MB(col), 0, 0, .014, { p: g, cast: false }); ring.userData.ro = 3; M(new T.CircleGeometry(.268, 40), MB(BN), 0, 0, 0, { p: g, cast: false }).userData.ro = 0;
  const tri = (w, h, y, c, z) => { const sh = new T.Shape(); sh.moveTo(-w, 0); sh.lineTo(w, 0); sh.lineTo(0, -h); sh.lineTo(-w, 0); return M(new T.ShapeGeometry(sh), MB(c), 0, y, z, { p: g, cast: false }); };
  tri(.095, .13, -.2, BN, .001).userData.ro = 0; const tail = tri(.07, .1, -.215, col, .015); tail.userData.ro = 3;   /* mũi nhọn nằm đúng giữa, liền vòng, viền nâu */
  { const bar = G(0, -.42, .012, 0, g); bar.visible = false; M(new T.PlaneGeometry(.42, .085), MB(BN), 0, 0, 0, { p: bar, cast: false }).userData.ro = 0; M(new T.PlaneGeometry(.39, .055), MB('#6B4529'), 0, 0, .002, { p: bar, cast: false }).userData.ro = 2; const fg = new T.PlaneGeometry(.39, .055); fg.translate(.195, 0, 0); const fill = M(fg, MB('#F2C64A'), -.195, 0, .004, { p: bar, cast: false }); fill.userData.ro = 3; g.userData.bar = bar; g.userData.fill = fill; }   /* thanh tiến độ dưới bong bóng */
  g.userData.ring = ring; g.userData.tail = tail; g.userData.col = col; const ic = G(0, 0, .05, 0, g);""")
import re
old = re.search(r"  g\.traverse\(o => \{ if \(o\.isMesh && o\.userData\.icon\)\{ o\.renderOrder = 21; return; \} if \(o\.isMesh\)\{ o\.material = o\.material\.clone\(\); o\.material\.depthTest = false; o\.material\.emissive = o\.material\.color\.clone\(\)\.multiplyScalar\(\.5\); o\.material\.emissiveIntensity = 0; o\.renderOrder = 20;", s)
assert old
s = s.replace(old.group(0), old.group(0)[:-len("o.renderOrder = 20;")] + "o.renderOrder = 20 + (o.userData.ro != null ? o.userData.ro * .1 : .45);   /* lớp: viền nâu, đĩa kem, vòng màu, rồi icon */")
rep("""  const hit = new T.Mesh(new T.SphereGeometry(.24, 8, 6), new T.MeshBasicMaterial({ visible: false })); g.add(hit); hit.userData.bub = kind; g.visible = false; return g; }""",
    """  const hit = new T.Mesh(new T.SphereGeometry(.24, 8, 6), new T.MeshBasicMaterial({ visible: false })); g.add(hit); hit.userData.bub = kind; g.visible = false; return g; }
function bubCol(g, c){ if (!g || g.userData.col === c) return; g.userData.col = c; for (const m of [g.userData.ring, g.userData.tail]) if (m){ m.material.color.set(c); if (m.material.emissive) m.material.emissive.set(c).multiplyScalar(.5); } }""")
rep("const BUBM = [];", "const BUBM = [], BUBC = { lay: '#7DB84A', lam: '#F2A23A', gap: '#D9483A' };   /* xanh: có đồ để lấy · cam: việc cần làm · đỏ: gấp */")
# objBub: màu theo nghĩa (icon cuốc/việc = cam, còn lại xanh) + thanh tiến độ tuỳ chọn
rep("""function objBub(V, v, url, t, y = .62){ const b = V.b; b.visible = true; try { bubIcon(b, url); } catch (e) {}""",
    """function objBub(V, v, url, t, y = .62, f){ const b = V.b; b.visible = true; try { bubIcon(b, url); } catch (e) {} bubCol(b, url === ICON.cuoc || url === UIC.task || url === UIC.sickle ? BUBC.lam : BUBC.lay); { const br = b.userData.bar; if (br){ br.visible = f != null; if (f != null) b.userData.fill.scale.x = Math.max(.02, Math.min(1, f)); } }""")
# ô đất cỏ rậm: việc cần làm (cam)
rep("v.bub = { s: bubbleK('s'), w: bubbleK('w'), u: bubbleK('u'), h: bubbleK('h'), p: bubbleK('p'), d: bubbleK('h') };",
    "v.bub = { s: bubbleK('s'), w: bubbleK('w'), u: bubbleK('u'), h: bubbleK('h'), p: bubbleK('p'), d: bubbleK('h') }; bubCol(v.bub.d, BUBC.lam);")
# truyền tiến độ cho các việc đang chờ
rep("""if (!VISIT) objBub(V, { cx: at[0], cz: at[1] }, ICON.cuoc || UIC.task, t, 1.25); } }""",
    """if (!VISIT) objBub(V, { cx: at[0], cz: at[1] }, ICON.cuoc || UIC.task, t, 1.25, 1 - bldLeft(k) / Math.max(1, (BLDH[k] - Math.min(BLDH[k] / 2, (ST.bld[k].help || 0))) * 3600e3 / (ST.spd || 1))); } }""")
rep("""if (st === 1 && !VISIT) objBub(MAIV, { cx: 2.4, cz: 1.0 }, ICON.cuoc || UIC.task, t, 2.35); }""",
    """if (st === 1 && !VISIT) objBub(MAIV, { cx: 2.4, cz: 1.0 }, ICON.cuoc || UIC.task, t, 2.35, 1 - maiLeft() / Math.max(1, (MAI.h - Math.min(MAI.help, ST.mai.help || 0)) * 3600e3 / (ST.spd || 1))); }""")
rep("""if (st === 1 && !VISIT) objBub(NHAV, { cx: 4.15, cz: 2.25 }, ICON.cuoc || UIC.task, t, 1.3); }""",
    """if (st === 1 && !VISIT) objBub(NHAV, { cx: 4.15, cz: 2.25 }, ICON.cuoc || UIC.task, t, 1.3, 1 - nhaLeft() / Math.max(1, (NHA.h - Math.min(NHA.help, ST.nha.help || 0)) * 3600e3 / (ST.spd || 1))); }""")
rep("""else if (st === 2) objBub(TBV, { cx: x, cz: z }, ICON.cuoc || UIC.task, t, .8);""",
    """else if (st === 2) objBub(TBV, { cx: x, cz: z }, ICON.cuoc || UIC.task, t, .8, 1 - tbLeft() / Math.max(1, (TB.h - Math.min(TB.help, ST.tb.help || 0)) * 3600e3 / (ST.spd || 1)));""")
rep("new T.PlaneGeometry(kind === 'h' ? .36 : .3, kind === 'h' ? .36 : .3)", "new T.PlaneGeometry(.38, .38)")
rep("o.material.depthTest = false; o.material.emissive = o.material.color.clone().multiplyScalar(.5); o.material.emissiveIntensity = 0;", "o.material.depthTest = false; if (o.material.isMeshBasicMaterial){ o.renderOrder = 20 + (o.userData.ro != null ? o.userData.ro * .1 : .45); return; } o.material.emissive = o.material.color.clone().multiplyScalar(.5); o.material.emissiveIntensity = 0;")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
