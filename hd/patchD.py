p='live/vuon3d.html';s=open(p,encoding='utf8').read()
def rep(a,b,cnt=1):
    global s
    n=s.count(a)
    assert n==cnt,(n,a[:80])
    s=s.replace(a,b)

# 1. ô bãi hông nhà
rep("const PL = Object.fromEntries(PLOTS.map(p => [p.id, p]));",
"""// bãi hông nhà (cấp 7): 12 ô cỏ bên trái nhà, con tự chọn ô nào đắp liếp, ô nào để cỏ, ô nào đặt nong phơi
const BAI = { lv: 7, cost: 50, x0: -4.35, z0: -1.35, cw: .8, cl: .7, gap: .1, cols: 4 };
for (let i = 0; i < 12; i++){ const c = i % BAI.cols, r = Math.floor(i / BAI.cols), u0 = BAI.x0 + c * (BAI.cw + BAI.gap), v0 = BAI.z0 + r * (BAI.cl + BAI.gap); PLOTS.push({ id: 'H' + (i + 1), b: [u0, v0, u0 + BAI.cw, v0 + BAI.cl], name: `Bãi hông nhà · ô ${i + 1}`, bai: true }); }
const BAIC = { x: BAI.x0 + (BAI.cols * (BAI.cw + BAI.gap) - BAI.gap) / 2, z: BAI.z0 + (3 * (BAI.cl + BAI.gap) - BAI.gap) / 2 };
const PL = Object.fromEntries(PLOTS.map(p => [p.id, p]));""")
rep("const isBed = P => /^[ABC]/.test(P.id), locked = P => isBed(P) && !ST.open.includes(P.id);",
"const isBed = P => /^[ABCH]/.test(P.id), locked = P => isBed(P) && !ST.open.includes(P.id);\nconst baiOn = () => (ST.lv || 1) >= BAI.lv, hidP = P => P.bai && !baiOn(), nOpen = () => ST.open.filter(i => i[0] !== 'H').length;")
rep("bedCost = () => 60 + 30 * Math.max(0, ST.open.length - 6);","bedCost = () => 60 + 30 * Math.max(0, nOpen() - 6);")
# cỏ không mọc chồng lên bãi
rep("if (x > 1 && x < 3.9 && z > -.6 && z < 2.5) continue; if (z > 7.9) continue; tuft(x, z);","if (x > 1 && x < 3.9 && z > -.6 && z < 2.5) continue; if (x > BAI.x0 - .1 && x < BAI.x0 + 3.6 && z > BAI.z0 - .1 && z < BAI.z0 + 2.4) continue; if (z > 7.9) continue; tuft(x, z);")
# 2. PV: liếp bãi gom vào nhóm riêng (ẩn khi còn là cỏ)
rep("  v.bub = { s: bubbleK('s'), w: bubbleK('w'), u: bubbleK('u'), h: bubbleK('h'), p: bubbleK('p'), d: bubbleK('h') }; v.bubY = .3; v.cx = cx; v.cz = cz;",
"""  if (P.bai){ const bg = new T.Group(); for (const ch of [...root.children]) if (ch !== v.weed) bg.add(ch); root.add(bg); v.bedG = bg; const pr = ROOT; ROOT = bg; bed(u0, v0, u1, v1); ROOT = pr; if (v.weed) v.weed.position.y = -.035; }
  v.bub = { s: bubbleK('s'), w: bubbleK('w'), u: bubbleK('u'), h: bubbleK('h'), p: bubbleK('p'), d: bubbleK('h') }; v.bubY = .3; v.cx = cx; v.cz = cz;""")
rep("  if (v.weed){ const lk = locked(P); v.weed.visible = lk; if (lk){ v.want = ST.open.length < bedCap() ? 'd' : null; v.bubY = .55; try { bubIcon(v.bub.d, UIC.sickle); } catch (e) {} } }",
"""  if (v.weed){ const lk = locked(P); v.weed.visible = lk; if (lk){ v.want = nOpen() < bedCap() ? 'd' : null; v.bubY = .55; try { bubIcon(v.bub.d, UIC.sickle); } catch (e) {} } }
  if (P.bai){ const on = baiOn(), lk = locked(P), nh = ST.nong && ST.nong.own && ST.nong.at === id; v.root.visible = on; v.bedG.visible = on && !lk; if (v.weed) v.weed.visible = on && lk && !nh; if (!on || nh) v.want = null; else if (lk){ v.want = SUA && !SUA.move ? 'd' : null; v.bubY = .4; try { bubIcon(v.bub.d, ICON.cuoc || UIC.sickle); } catch (e) {} } }""")
# chạm: bỏ ô bãi khi chưa tới cấp
rep("const plotAt = (x, z) => PLOTS.find(P => { const [u0, v0, u1, v1] = P.b; return x > u0 && x < u1 && z > v0 && z < v1; });",
"const plotAt = (x, z) => PLOTS.find(P => { if (hidP(P)) return false; const [u0, v0, u1, v1] = P.b; return x > u0 && x < u1 && z > v0 && z < v1; });")
rep("const plotNear = (x, z, tol) => plotAt(x, z) || PLOTS.map(P =>","const plotNear = (x, z, tol) => plotAt(x, z) || PLOTS.filter(P => !hidP(P)).map(P =>")
# đắp liếp ở bãi: giá cố định, không tính trần liếp
rep("  openBed(id){ const P = PL[id]; if (!locked(P)) return; if (ST.open.length >= bedCap()) return say(`Tới cấp ${bedNext()} mới đắp thêm được con.`, 'dan'); const c0 = bedCost();",
"  openBed(id){ const P = PL[id]; if (!locked(P)) return; if (P.bai && ST.nong && ST.nong.at === id) return say('Ô này đang đặt nong phơi. Dời nong đi rồi mới đắp liếp được con.', 'dan'); if (!P.bai && nOpen() >= bedCap()) return say(`Tới cấp ${bedNext()} mới đắp thêm được con.`, 'dan'); const c0 = P.bai ? BAI.cost : bedCost();")
rep("    if (locked(P)){ shT.textContent = 'Cỏ rậm'; const can = ST.open.length < bedCap(), c0 = bedCost();",
"    if (P.bai){ shT.textContent = suaTitle(arg); h += suaHTML(arg); shB.innerHTML = h; return; }\n    if (locked(P)){ shT.textContent = 'Cỏ rậm'; const can = nOpen() < bedCap(), c0 = bedCost();")
s=s.replace("<b>${ST.open.length} / ${bedCap()} liếp ở cấp này</b>","<b>${nOpen()} / ${bedCap()} liếp ở cấp này</b>")
# 3. đồ phơi + kho gác bếp
rep("const GD = k => CROPS[k] || EXTRA[k] || DISH[k];",
"""// nong phơi (cấp 7): phơi bằng nắng giờ thật, đồ khô cất gác bếp
const PHOI = {
  otkho: { name: 'Ớt khô', unit: 'bịch', lv: 7, in: { ot: 4 }, t: 4 * 3600, sell: 90, story: 'Ớt phơi khô giã với muối hột, để dành chấm trái cây cả năm.' },
  chuoiphoi: { name: 'Chuối phơi', unit: 'xâu', lv: 8, in: { chuoi: 2 }, t: 8 * 3600, sell: 130, story: 'Chuối xiêm chín ép dẹp, phơi ba nắng là dẻo ngọt. Tụi nhỏ xóm này mê lắm.' },
  lucbinhkho: { name: 'Lục bình khô', unit: 'bó', lv: 10, in: { lucbinh: 5 }, t: 6 * 3600, sell: 20, story: 'Cọng lục bình phơi khô để đan giỏ, đan đệm. Cấp 10 Ngoại dạy con đan.' } };
const GD = k => CROPS[k] || EXTRA[k] || DISH[k] || PHOI[k];""")
rep("const STORE = k => (DISH[k] || k === 'cui') ? (ST.gb = ST.gb || {}) : ST.inv;","const STORE = k => (DISH[k] || PHOI[k] || k === 'cui') ? (ST.gb = ST.gb || {}) : ST.inv;")
s=s.replace("Object.entries(ST.gb || {}).some(([k, n]) => n > 0 && DISH[k])","Object.entries(ST.gb || {}).some(([k, n]) => n > 0 && (DISH[k] || PHOI[k]))")
rep("const gbi = Object.entries(ST.gb || {}).filter(([k, n]) => n > 0 && DISH[k]);","const gbi = Object.entries(ST.gb || {}).filter(([k, n]) => n > 0 && (DISH[k] || PHOI[k]));")
# 4. sim
rep("try { if (ST.vit) vitSim(dt); } catch (e) {}","try { if (ST.vit) vitSim(dt); } catch (e) {} try { nongSim(dt); } catch (e) {}")
rep("try { oddSim(s2); ordSim(s2); bepSim(s2); } catch (e) { break; } off -= s2; } }",
"try { oddSim(s2); ordSim(s2); bepSim(s2); } catch (e) { break; } try { nongSim(s2, Date.now() - off * 1000); } catch (e) {} off -= s2; } }")
open(p,'w',encoding='utf8').write(s)
print('ok')
