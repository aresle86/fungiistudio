#!/usr/bin/env python3
"""Icon tô hoạt hình: lúc chụp mọi icon (rau, cá, đồ, nút, nhân vật), đổi chất liệu sang MeshToonMaterial 4 tông dứt khoát,
tông sáng nhất nằm trên mặt khối hướng về đèn (vệt sáng theo dáng từng vật), màu tươi hơn nhưng giữ đúng hue.
Dùng: python3 toonfix.py <vào> <ra>."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

rep("const FR = (() => { const OUT = {};", r"""/* --- tô hoạt hình cho icon: gom bóng thành 4 tông, tông trên cùng là vệt sáng nằm trên mặt hướng đèn, màu tươi hơn giữ hue --- */
const TOONG = (() => { const d = new Uint8Array([92, 92, 92, 255, 150, 150, 150, 255, 214, 214, 214, 255, 255, 255, 255, 255]), t = new T.DataTexture(d, 4, 1, T.RGBAFormat); t.minFilter = t.magFilter = T.NearestFilter; t.generateMipmaps = false; t.needsUpdate = true; return t; })();
const TOONC = new Map(), TOONH = {};
function toonMat(m){ if (!m || m.isMeshBasicMaterial || m.isLineBasicMaterial || m.isSpriteMaterial || m.isPointsMaterial || !m.color) return m; if (TOONC.has(m)) return TOONC.get(m);
  const c = m.color.clone(); c.getHSL(TOONH); if (TOONH.s > .04 && TOONH.s < .62) c.setHSL(TOONH.h, Math.min(.66, TOONH.s * 1.2 + .03), Math.min(.92, TOONH.l * 1.03 + .01)); else if (TOONH.s >= .62) c.setHSL(TOONH.h, TOONH.s * .9, TOONH.l);   /* màu vốn đã chói (cà chua, ớt) thì dịu lại chút, không đẩy thêm */
  const t = new T.MeshToonMaterial({ color: c, gradientMap: TOONG, side: m.side, transparent: m.transparent, opacity: m.opacity, vertexColors: m.vertexColors, map: m.map || null, depthWrite: m.depthWrite, alphaTest: m.alphaTest || 0 });
  if (m.emissive){ t.emissive = m.emissive.clone(); t.emissiveIntensity = m.emissiveIntensity; } TOONC.set(m, t); return t; }
let TOONLAST = '';
function toonRender(ri, sc, cm){ toonify(sc); const W = ri.domElement.width, H = ri.domElement.height, saved = []; let n = 0;   /* nét tách các khối lớn như ref: mỗi khối một mã riêng, chỉ kẻ ranh giới giữa hai khối đủ lớn (3 trái cà chua, 2 quả trứng, lá với trái); khối nhỏ (cọng rơm, hạt, mắt) và vùng sáng tối không kẻ */
  sc.traverse(o => { if (!o.isMesh || !o.visible) return; const m = Array.isArray(o.material) ? o.material[0] : o.material; if (!m || (m.transparent && m.opacity < .85)) return; n++; saved.push([o, o.material]); const c = new T.Color(); c.setRGB((n % 256) / 255, (Math.floor(n / 256) % 256) / 255, 1, T.LinearSRGBColorSpace); o.material = new T.MeshBasicMaterial({ color: c, side: T.DoubleSide, toneMapped: false }); });
  const rt = new T.WebGLRenderTarget(W, H), tm = ri.toneMapping, cc = new T.Color(), ca = ri.getClearAlpha(); ri.getClearColor(cc); ri.toneMapping = T.NoToneMapping; ri.setRenderTarget(rt); ri.setClearColor(0, 0); ri.clear(); ri.render(sc, cm); const idb = new Uint8Array(W * H * 4); ri.readRenderTargetPixels(rt, 0, 0, W, H, idb); ri.setRenderTarget(null); rt.dispose();
  for (const [o, m] of saved){ o.material.dispose(); o.material = m; } ri.toneMapping = tm; ri.setClearColor(cc, ca); ri.render(sc, cm);
  const co = document.createElement('canvas'); co.width = W; co.height = H; const xo = co.getContext('2d'); xo.drawImage(ri.domElement, 0, 0); const im = xo.getImageData(0, 0, W, H), D = im.data, out = new Uint8ClampedArray(D);
  const ID = new Int32Array(W * H), cnt = new Map(); let tot = 0; for (let y = 0; y < H; y++) for (let x = 0; x < W; x++){ const s0 = ((H - 1 - y) * W + x) * 4, v = idb[s0 + 3] > 0 ? idb[s0] + idb[s0 + 1] * 256 : 0; ID[y * W + x] = v; if (v){ cnt.set(v, (cnt.get(v) || 0) + 1); tot++; } }
  const big = v => v > 0 && cnt.get(v) >= tot * .04;
  for (let y = 0; y < H - 1; y++) for (let x = 0; x < W - 1; x++){ const k = y * W + x, a = ID[k]; if (!big(a)) continue; for (const k2 of [k + 1, k + W]){ const b = ID[k2]; if (!big(b) || a === b) continue; for (const j of [k * 4, k2 * 4]){ if (D[j + 3] < 100) continue; out[j] = D[j] * .38 + 22; out[j + 1] = D[j + 1] * .38 + 14; out[j + 2] = D[j + 2] * .38 + 9; } } }
  im.data.set(out); xo.putImageData(im, 0, 0); TOONLAST = co.toDataURL('image/png'); }
const toonURL = () => TOONLAST;
function toonify(sc){ sc.traverse(o => { if (!o.isMesh) return; o.material = Array.isArray(o.material) ? o.material.map(toonMat) : toonMat(o.material); }); return sc; }
const FR = (() => { const OUT = {};""")
import re
n0 = len(re.findall(r"ri\.render\(sc, cm\);([^;]*?)ri\.domElement\.toDataURL\('image/png'\)", s))
assert n0 == 13, n0
s = re.sub(r"ri\.render\(sc, cm\);([^;]*?)ri\.domElement\.toDataURL\('image/png'\)", r"toonRender(ri, sc, cm);\1toonURL()", s)
# hướng dẫn nuôi gà: tách từng ý, nói rõ vì sao cần gà trống
rep("""  h += UX.more('Cách nuôi gà', `Gà đẻ mỗi ${GA.cyc / 3600} tiếng một trứng nếu máng còn thức ăn. Cho ăn dùng bắp trong kho trước (1 trái = ${GA.bapPhan} phần), thiếu thì mua cám ${GA.cam} xu một phần. ${lvOk ? `Ấp trứng cần gà trống và một trứng trong kho, nở ra mái thì đẻ thêm, trống thì Ngoại bán giùm ${GA.roosterSell} xu.` : ''}`);""",
"""  h += UX.more('Cách nuôi gà', `<div class="gdl"><p><img src="${ICON.trungga}" alt=""><span><b>Đẻ trứng</b>Máng còn thức ăn thì mỗi gà mái đẻ một trứng, chừng ${GA.cyc / 3600} tiếng một lần.</span></p><p><img src="${ICON.bap}" alt=""><span><b>Cho ăn</b>Một trái bắp trong kho đổ được ${GA.bapPhan} phần máng. Hết bắp thì mua cám, ${GA.cam} xu một phần.</span></p>${lvOk ? `<p><img src="${ICON.trungga}" alt=""><span><b>Ấp trứng</b>Một gà mái nằm ổ ấp trứng, nên chuồng cần ít nhất hai mái: một con ấp, một con vẫn đẻ. Trứng phải là trứng có trống mới nở ra gà con, nên chuồng cần một con gà trống.</span></p><p><img src="${ICON.gamai || ICON.ga || ICON.trungga}" alt=""><span><b>Gà con lớn</b>Gà mái thì giữ lại nuôi, đẻ thêm trứng. Gà trống dư thì Ngoại bán giùm, được ${GA.roosterSell} xu.</span></p>` : ''}</div>`);""")
rep("const UIC = (() => { const OUT = {}; const ps = sd; const ri = new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true }); ri.setPixelRatio(1); ri.setSize(120, 120);",
    "const UIC = (() => { const OUT = {}; const ps = sd; const ri = new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true }); ri.setPixelRatio(1); ri.setSize(180, 180);")
i = s.rindex('</style>'); s = s[:i] + '.gdl p{display:flex;gap:10px;align-items:flex-start;margin:6px 0}.gdl img{width:34px;height:34px;flex:none}.gdl b{display:block;font:400 15px var(--f-game);color:#4A2F1E}.gdl span{font-size:14px;line-height:1.35}\n' + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s)
print('ok')
