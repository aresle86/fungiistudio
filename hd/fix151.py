# NHÁP v151: công trình lớn đợt 2 · cầu qua rạch (cầu khỉ rồi cầu ván) và 12 khoảnh đất bên kia rạch.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v150'", "BUILD = 'v151'")

# ---- vùng đất mới: 12 ô bên kia rạch (tiền tố R) ----
rep("zone: 'sau', lv: SAU.lv, cost: SAU.cost }); }\nawait LDY(0);\nconst ZW = Z =>",
    "zone: 'sau', lv: SAU.lv, cost: SAU.cost }); }\n"
    "// bên kia rạch (cấp 20): 12 ô, phải bắc cầu khỉ mới qua khai hoang được; có cầu ván mới trồng cây trái\n"
    "const BKR = { lv: 20, cost: 90, x0: -0.3, z0: 11.3, cw: 1.225, cl: .8, gap: .1, rg: .3, cols: 6 };\n"
    "for (let i = 0; i < 12; i++){ const c = i % BKR.cols, r = Math.floor(i / BKR.cols), u0 = BKR.x0 + c * (BKR.cw + BKR.gap), v0 = BKR.z0 + r * (BKR.cl + BKR.rg); PLOTS.push({ id: 'R' + (i + 1), b: [u0, v0, u0 + BKR.cw, v0 + BKR.cl], name: `Bên kia rạch · ô ${i + 1}`, bai: true, zone: 'kia', lv: BKR.lv, cost: BKR.cost }); }\n"
    "await LDY(0);\nconst ZW = Z =>")
rep("const isBed = P => /^[ABCHSN]/.test(P.id)", "const isBed = P => /^[ABCHSNR]/.test(P.id)")
rep("(P.zone === 'sau' && !(ST.qd || {})[12])), nOpen = () => ST.open.filter(i => !/^[HSN]/.test(i)).length;",
    "(P.zone === 'sau' && !(ST.qd || {})[12]) || (P.zone === 'kia' && !((ST.kia || {}).n >= 1))), nOpen = () => ST.open.filter(i => !/^[HSNR]/.test(i)).length;")
rep("sau: { base: 900, g: 1.18, ai: [60, 120], cong: ['Chặt gốc tre', 'Cuốc đất'], drop: 'tre' } };",
    "sau: { base: 900, g: 1.18, ai: [60, 120], cong: ['Chặt gốc tre', 'Cuốc đất'], drop: 'tre' }, kia: { base: 2000, g: 1.2, ai: [120, 240], cong: ['Phát cỏ', 'Cuốc đất'], drop: 'rom' } };")
rep("const TREEZ = { song: 1, sau: 1 };", "const TREEZ = { song: 1, sau: 1, get kia(){ return (ST.kia || {}).n >= 2 ? 1 : 0; } };")
rep("const Z = zoneOf(P) === 'song' ? SONG : SAU", "const Z = zoneOf(P) === 'song' ? SONG : zoneOf(P) === 'kia' ? BKR : SAU", 2)
rep("{ k: 'sau', Z: SAU, pre: 'N', n: 10, name: 'Sau nhà', base: 200 }];",
    "{ k: 'sau', Z: SAU, pre: 'N', n: 10, name: 'Sau nhà', base: 200 }, { k: 'kia', Z: BKR, pre: 'R', n: 12, name: 'Bên kia rạch', base: 300 }];")
rep("sau: [SAU, 'N', 10], ...Object.fromEntries(", "sau: [SAU, 'N', 10], kia: [BKR, 'R', 12], ...Object.fromEntries(")
rep("P.zone === 'sau' ? 'Đất sau nhà' : 'Bãi cỏ';", "P.zone === 'sau' ? 'Đất sau nhà' : P.zone === 'kia' ? 'Đất bên kia rạch' : 'Bãi cỏ';")
rep("(lv < z.Z.lv ? `${z.name}|Đất còn hoang` : `${z.name}|Dọn tre gai trước`)",
    "(lv < z.Z.lv ? `${z.name}|Đất còn hoang` : z.k === 'kia' ? `${z.name}|Bắc cầu qua trước` : `${z.name}|Dọn tre gai trước`)")

# ---- cầu qua rạch ----
KIA = r"""
/* --- cầu qua rạch (cấp 20): cầu khỉ mở đất bên kia rạch, cầu ván cho trồng cây trái bên đó --- */
const KIA = { lv: 20, x: -1.25, z0: 8.12, len: 2.74, st: [
  { name: 'cầu khỉ', title: 'Bắc cầu khỉ', doing: 'Đang bắc cầu khỉ', btn: 'Bắc cầu', sub: 'Qua được bên kia rạch, khai hoang thêm 12 khoảnh đất', xu: 8000, need: [['bap', 20], ['chuoi', 10]], h: 8, help: 4 },
  { name: 'cầu ván', title: 'Lót cầu ván', doing: 'Đang lót cầu ván', btn: 'Lót cầu', sub: 'Cầu chắc, gánh được cây giống qua · bên kia rạch trồng được cây trái', xu: 25000, need: [['dua', 15], ['xoai', 10]], h: 16, help: 6 }] };
if (!ST.kia) ST.kia = { n: 0, b: null };
function cauKia(kind, part){ const g = new T.Group(), pr = ROOT; ROOT = g; const L = KIA.len, BA = '#cdb46a', BA2 = '#B9A45A', BA3 = '#A08A4A', WD = '#8A5D3B', WD2 = '#6B4529';
  if (kind === 0){   /* chỗ định bắc cầu: hai cọc tre cắm sẵn, cờ đuôi nheo, bó tre nằm chờ */
    for (const x of [-.16, .16]) M(cyl(.02, .024, .62, 6), BA2, x, .31, .06);
    stick(g, -.16, .5, .06, .16, .5, .06, .012, BA3); M(box(.2, .12, .012), '#C24A2E', .28, .55, .06, { cast: false }); M(cyl(.008, .008, .3, 4), WD2, .17, .6, .06);
    for (let i = 0; i < 5; i++) stick(g, -.55 + i * .012, .035 + (i % 2) * .05, -.32 + i * .045, .5 + i * .012, .035 + (i % 2) * .05, -.34 + i * .045, .024, i % 2 ? BA : BA2);
    ROOT = pr; return g; }
  const TZ = [.42, 1.02, 1.72, 2.32];
  if (kind === 1 || part){   /* cầu khỉ: chân tre bắt chéo, một cây tre làm lối đi, một tay vịn */
    const khi = kind === 1 && part ? 0 : 1;
    for (const z of TZ){ stick(g, -.24, -.42, z, .12, .98, z, .024, BA2); stick(g, .24, -.42, z, -.12, .98, z, .024, BA); M(new T.TorusGeometry(.04, .01, 3, 8), WD2, 0, .52, z, { r: [0, 0, 0], cast: false }); }
    if (khi){ const P = [[-.12, .07], [TZ[0], .56], [TZ[3], .56], [L + .12, .07]]; for (let i = 0; i < 3; i++) stick(g, 0, P[i][1], P[i][0], 0, P[i + 1][1], P[i + 1][0], .03, i === 1 ? BA : BA2);
      stick(g, .12, .96, TZ[0], .12, .96, TZ[3], .014, BA3); stick(g, .12, .96, TZ[0], .12, .46, -.1, .014, BA3); stick(g, .12, .96, TZ[3], .12, .46, L + .1, .014, BA3);
      for (const z of [-.1, L + .1]) M(cyl(.018, .02, .5, 5), BA2, .12, .25, z); }
    else { for (let i = 0; i < 4; i++) stick(g, -.5 + i * .012, .035 + (i % 2) * .05, -.3 + i * .05, .55, .035 + (i % 2) * .05, -.32 + i * .05, .024, i % 2 ? BA : BA2); } }
  if (kind === 2){   /* cầu ván: cột gỗ, ván lót cong nhẹ cho ghe chui lọt, hai tay vịn */
    const yU = u => .05 + .42 * Math.sin(Math.PI * u), N = 26, X = .27, PZ = [.1, .62, 1.14, 1.6, 2.12, 2.64];
    for (const z of PZ) for (const x of [-X, X]){ const top = part ? .34 : yU(z / L) + .4, bot = z > .3 && z < L - .3 ? -.42 : 0; M(cyl(.03, .034, top - bot, 6), WD, x, (top + bot) / 2, z); }
    if (part){ for (let i = 0; i < 6; i++) M(box(.5, .022, .11), i % 2 ? '#C9A27E' : '#B98F68', .62 + (i % 2) * .03, .03 + i * .024, -.3, { r: [0, .1 * (i % 3 - 1), 0] }); }
    else { for (const x of [-X + .06, X - .06]) for (let i = 0; i < 10; i++) stick(g, x, yU(i / 10) - .03, i / 10 * L, x, yU((i + 1) / 10) - .03, (i + 1) / 10 * L, .02, WD2);
      for (let i = 0; i < N; i++){ const u = (i + .5) / N, sl = Math.atan(.42 * Math.PI * Math.cos(Math.PI * u) / L); M(box(.5, .02, L / N * .9), i % 2 ? '#C9A27E' : '#B98F68', 0, yU(u), u * L, { r: [-sl, 0, 0] }); }
      for (const x of [-X, X]) for (let i = 0; i < 5; i++) stick(g, x, yU(PZ[i] / L) + .36, PZ[i], x, yU(PZ[i + 1] / L) + .36, PZ[i + 1], .016, WD); } }
  ROOT = pr; return g; }
const KIAV = (() => { const root = DYN(G(KIA.x, 0, KIA.z0)); root.visible = false; const hit = new T.Mesh(new T.BoxGeometry(.8, 1.1, KIA.len + .4), new T.MeshBasicMaterial({ visible: false })); hit.position.set(0, .45, KIA.len / 2); root.add(hit); return { root, hit, m: null, sig: '', ...mkBub() }; })();
const kiaOn = () => !VISIT && (ST.lv || 1) >= KIA.lv, kiaS = () => KIA.st[(ST.kia || {}).n || 0];
function kiaLeft(){ const B = ST.kia.b, S = kiaS(); if (!B || !S) return 0; return Math.max(0, (S.h - Math.min(S.help, B.help || 0)) * 3600e3 / (ST.spd || 1) - (Date.now() - B.t)); }
const kiaCan = () => { const S = kiaS(); return !!S && ST.xu >= S.xu && S.need.every(([k, q]) => has(k) >= q); };
function kiaBuild(){ const S = kiaS(); if (!kiaOn() || !S || ST.kia.b) return; if (ST.xu < S.xu) return toast(`Còn thiếu ${S.xu - ST.xu} xu nữa con.`, 'dan'); if (!S.need.every(([k, q]) => has(k) >= q)) return toast('Chưa đủ đồ đãi thợ con ơi.', 'dan');
  for (const [k, q] of S.need) STORE(k)[k] -= q; ST.xu -= S.xu; coinPop(`-${S.xu} xu`, '#F08A6E'); ST.kia.b = { t: Date.now(), help: 0 }; save(); closeSheet(); hud();
  camTo(new T.Vector3(KIA.x, .3, KIA.z0 + KIA.len / 2), Math.max(cam.zoom, DEFZ() * 1.1)); for (let i = 0; i < 14; i++) puff('leaf', KIA.x + R(-.3, .3), .4, KIA.z0 + R(0, KIA.len), 1, pick(['#cdb46a', '#B9A45A']), .7); sfx('pop'); toast(`Bắt đầu ${S.title.toLowerCase()} · xong sau ${S.h} tiếng`); }
function kiaDone(){ const K = ST.kia; K.b = null; K.n = (K.n || 0) + 1; save(); for (let i = 0; i < 28; i++) puff('spark', KIA.x + R(-.4, .4), .7, KIA.z0 + R(0, KIA.len), 1, pick(['#F5D27A', '#FBF7EE']), .9); sfx('up'); hud();
  if (K.n === 1){ try { for (const P of PLOTS) if (P.zone === 'kia') refreshPlot(P.id); } catch (e) {} setTimeout(() => say('Cầu khỉ bắc xong rồi con! Đất bên kia rạch còn hoang lắm, con qua khai hoang từng khoảnh mà trồng nghe.', 'nhay', { idle: true }), 400); }
  else setTimeout(() => say('Cầu ván lót xong, chắc chắn rồi đó con. Giờ gánh cây giống qua được, bên kia rạch trồng cây trái được rồi.', 'nhay', { idle: true }), 400); }
function kiaHTML(){ const K = ST.kia, S = kiaS(); let h = '';
  if (!S) return UX.hero(UIC.cauvan || ICON.cuoc, 'Cầu ván', 'Cầu chắc rồi, bên kia rạch trồng được cây trái');
  if (K.b){ const l = kiaLeft(), T0 = S.h * 3600e3 / (ST.spd || 1); return UX.hero(ICON.cuoc || UIC.task, S.doing, `Còn ${fmtMin(Math.ceil(l / 60000))} · bạn ghé phụ bớt 1 tiếng`, '', [1 - l / T0, '#EDB940']); }
  h += UX.hero((K.n ? UIC.cauvan : UIC.caukhi) || ICON.cuoc, S.title, S.sub) + UX.title('Cơm nước đãi thợ') + '<div class="oi" style="display:flex;gap:8px;flex-wrap:wrap">' + S.need.map(([k, q]) => { const hv = Math.min(q, has(k)); return `<span class="oit${hv >= q ? ' got' : ''}"><img src="${ICON[k]}" alt=""><i>${hv}/${q}</i></span>`; }).join('') + '</div>';
  return h + UX.cta([UX.btn('kiabuild', S.btn, { g: 1, img: UIC.coin, dis: !kiaCan(), sub: `${S.xu} xu` })]) + `<div class="note">Làm chừng ${S.h} tiếng, bạn ghé vườn phụ thì mau hơn.</div>`; }
function kiaTick(t){ const K = ST.kia || {}, on = kiaOn(), show = (on || VISIT) && (on || K.n >= 1 || !!K.b); KIAV.b.visible = false; KIAV.root.visible = show; if (!show) return;
  if (on && K.b && kiaLeft() <= 0) kiaDone();
  const sig = (K.n || 0) + (K.b ? 'b' : ''); if (sig !== KIAV.sig){ KIAV.sig = sig; if (KIAV.m){ KIAV.root.remove(KIAV.m); KIAV.m = null; } const n = K.n || 0, g = new T.Group();
    if (n === 0) g.add(cauKia(K.b ? 1 : 0, !!K.b)); else if (n === 1){ g.add(cauKia(1, false)); if (K.b) g.add(cauKia(2, true)); } else g.add(cauKia(2, false)); KIAV.m = g; KIAV.root.add(g); }
  if (!on) return; const v = { cx: KIA.x, cz: KIA.z0 + (K.n || K.b ? KIA.len / 2 : .1) };
  if (K.b){ const S = kiaS(); objBub(KIAV, v, ICON.cuoc || UIC.task, t, 1.35, 1 - kiaLeft() / Math.max(1, (S.h - Math.min(S.help, K.b.help || 0)) * 3600e3 / (ST.spd || 1)), kiaLeft()); }
  else if (!K.n){ objBub(KIAV, v, UIC.caukhi || ICON.cuoc, t, .95); sayOnce('kia', 'Con thấy miếng đất bên kia rạch hông? Bắc cây cầu khỉ qua là có thêm đất trồng. Ngoại cắm cọc sẵn ở mé rạch rồi đó.', 'vui'); }
  else if (K.n === 1 && kiaCan()) objBub(KIAV, v, UIC.cauvan || ICON.cuoc, t, 1.35); }
function kiaHit(cx, cy){ if (!kiaOn()) return false; ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); return ray.intersectObjects([KIAV.hb, KIAV.hit].filter(h => h && h.visible !== false && (h !== KIAV.hit || KIAV.root.visible) && (h !== KIAV.hb || KIAV.b.visible)), false).length > 0; }
"""
rep("\n/* --- tre gai sau nhà (cấp 11)", KIA.rstrip('\n') + "\n/* --- tre gai sau nhà (cấp 11)")
rep("  if (kind === 'tb'){ shT.textContent = 'Ghe tam bản'; h += tbHTML(); }",
    "  if (kind === 'tb'){ shT.textContent = 'Ghe tam bản'; h += tbHTML(); }\n  if (kind === 'kia'){ shT.textContent = 'Cầu qua rạch'; h += kiaHTML(); }")
rep("else if (a === 'tbbuild'){ tbBuild(); return; }", "else if (a === 'tbbuild'){ tbBuild(); return; } else if (a === 'kiabuild'){ kiaBuild(); return; }")
rep("  { const th = tbHit(OX, OY); if (th){", "  if (kiaHit(OX, OY)){ openSheet('kia'); hud(); return; }\n  { const th = tbHit(OX, OY); if (th){")
rep("tk('tb', () => tbTick(t));", "tk('tb', () => tbTick(t)); tk('kia', () => kiaTick(t));")
rep("if (ST.tb && !ST.tb.done) ST.tb.help = Math.min(TB.help, (ST.tb.help || 0) + Object.keys(by).length);",
    "if (ST.tb && !ST.tb.done) ST.tb.help = Math.min(TB.help, (ST.tb.help || 0) + Object.keys(by).length); if (ST.kia && ST.kia.b && KIA.st[ST.kia.n]) ST.kia.b.help = Math.min(KIA.st[ST.kia.n].help, (ST.kia.b.help || 0) + Object.keys(by).length);")
# hình cây cầu cho bảng: chụp từ chính mô hình
rep("  ri.renderLists.dispose(); }\nconst FTRID",
    "  for (const [nm, kd] of [['caukhi', 1], ['cauvan', 2]]){ const ps = sd, nL = LIGHTS.length, sc = new T.Scene(), m = cauKia(kd, false); sd = ps; LIGHTS.length = nL; sc.add(m); sc.add(new T.HemisphereLight('#fff6e6', '#9aaa78', 1.9)); const l = new T.DirectionalLight('#fff0d0', 1.9); l.position.set(-2, 6, 3); sc.add(l); const bb = new T.Box3().setFromObject(m), c = bb.getCenter(new T.Vector3()), sz = bb.getSize(new T.Vector3()).length() * .4; const cm = new T.OrthographicCamera(-sz, sz, sz, -sz, .01, 100); cm.position.copy(c).add(new T.Vector3(1, .6, .45).normalize().multiplyScalar(20)); cm.lookAt(c); toonRender(ri, sc, cm); UIC[nm] = toonURL(); }\n"
    "  ri.renderLists.dispose(); }\nconst FTRID")
# tiếng Anh
rep("(LVFEAT[22] = LVFEAT[22] || []).push(['chesaurieng', 'Chè sầu riêng']);",
    "(LVFEAT[22] = LVFEAT[22] || []).push(['chesaurieng', 'Chè sầu riêng']); try { Object.assign(UIEN, { 'Cầu qua rạch': 'Creek bridge', 'Bắc cầu khỉ': 'Build a monkey bridge', 'Lót cầu ván': 'Lay a plank bridge', 'Đang bắc cầu khỉ': 'Building the monkey bridge', 'Đang lót cầu ván': 'Laying the plank bridge', 'Bắc cầu': 'Build', 'Lót cầu': 'Build', 'Cầu ván': 'Plank bridge', 'Qua được bên kia rạch, khai hoang thêm 12 khoảnh đất': 'Cross the creek and clear 12 more plots of land', 'Cầu chắc, gánh được cây giống qua · bên kia rạch trồng được cây trái': 'A sturdy bridge for carrying saplings · fruit trees can grow across the creek', 'Cầu chắc rồi, bên kia rạch trồng được cây trái': 'The bridge is sturdy. Fruit trees can grow across the creek.', 'Cơm nước đãi thợ': 'Food for the builders', 'Chưa đủ đồ đãi thợ con ơi.': 'Not enough food for the builders yet, dear.', 'Bên kia rạch': 'Across the creek', 'Bắc cầu qua trước': 'Build a bridge first', 'Đất bên kia rạch': 'Land across the creek', 'Cầu khỉ bắc xong rồi con! Đất bên kia rạch còn hoang lắm, con qua khai hoang từng khoảnh mà trồng nghe.': 'The monkey bridge is up, dear! The land across the creek is still wild. Go clear it plot by plot and plant.', 'Cầu ván lót xong, chắc chắn rồi đó con. Giờ gánh cây giống qua được, bên kia rạch trồng cây trái được rồi.': 'The plank bridge is done and sturdy, dear. Now saplings can be carried over, so fruit trees can grow across the creek.', 'Con thấy miếng đất bên kia rạch hông? Bắc cây cầu khỉ qua là có thêm đất trồng. Ngoại cắm cọc sẵn ở mé rạch rồi đó.': 'See that land across the creek, dear? Build a monkey bridge and you get more land to plant. Grandma already set the stakes by the bank.' }); } catch (e) {}")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
