# -*- coding: utf-8 -*-
# v133 sau v132 (anh Ares gop y + doan 3 "Choi lau"):
# 1. Goc cay trai trong tren hai liep: lop co cat (v.mow) nam trung mat voi tam dat tran (v.bare) nen nhap nhay. An lop co di.
# 2. Cay co tich dua hau doi cho ra xa cay vu sua (truoc chi cach 1.4).
# 3. Gop bong bong: tu 3 liep lien nhau cung khu, cung viec (hai cung loai cay / tuoi / heo) thi chi hien MOT bong bong
#    co so dem; cham bong bong do la lam ca cum. Cham thang vao liep van chi lam liep do. Chi bat sau khi ban chuyen dau.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)

rep("BUILD = 'v132'", "BUILD = 'v133'")

# 1. nhap nhay
rep("if (host || guest){ v.root.visible = on; v.bedG.visible = false; if (v.weed) v.weed.visible = false; if (v.bare){",
    "if (host || guest){ v.root.visible = on; v.bedG.visible = false; if (v.weed) v.weed.visible = false; if (v.mow) v.mow.visible = false; if (v.bare){")

# 2. dua hau
rep("lv: 14, at: [-5.0, 5.3], max: 3,", "lv: 14, at: [-8.8, 5.2], max: 3,")

# 3. gop bong bong
rep("for (const k in v.bub) v.bub[k].visible = v.want === k;", "for (const k in v.bub) v.bub[k].visible = v.want === k; window.__CLD = 1;")
rep("function plotHit0(cx, cy){",
    """function clBadge(g, n){ const u = g.userData; if (!u.bdg){ if (!n) return; const m = new T.Mesh(new T.PlaneGeometry(.21, .21), new T.MeshBasicMaterial({ transparent: true, depthTest: false, toneMapped: false })); m.position.set(.2, .2, .03); m.renderOrder = 21.5; g.add(m); u.bdg = m; } if (!n){ u.bdg.visible = false; u.bdgOn = 0; return; }
  if (u.bdgN !== n){ u.bdgN = n; const C0 = clBadge.c = clBadge.c || {}; let tx = C0[n]; if (!tx){ const cv = document.createElement('canvas'); cv.width = cv.height = 96; const x = cv.getContext('2d'); x.fillStyle = '#4A2F1E'; x.beginPath(); x.arc(48, 48, 47, 0, 7); x.fill(); x.fillStyle = '#E8453A'; x.beginPath(); x.arc(48, 48, 40, 0, 7); x.fill(); x.fillStyle = '#fff'; x.font = (n > 9 ? 44 : 52) + 'px "Paytone One", sans-serif'; x.textAlign = 'center'; x.textBaseline = 'middle'; x.fillText(String(n), 48, 52); tx = C0[n] = new T.CanvasTexture(cv); tx.colorSpace = T.SRGBColorSpace; } u.bdg.material.map = tx; u.bdg.material.needsUpdate = true; } u.bdg.visible = true; u.bdgOn = 1; }
/* gop bong bong: tu 3 liep lien nhau, cung khu, cung viec thi hien mot bong bong co so dem tren liep giua cum */
function clPass(){ window.__CLD = 0; const on = !VISIT && ST.seen && ST.seen.sold, L = []; for (const P of PLOTS){ const v = PV[P.id]; v.clH = false; v.clM = null; if (!on || !v.want || P.tree || P.trellis || !'hwu'.includes(v.want)) continue; const p = ST.plots[P.id]; if (!p || (ST.pairs && ST.pairs[P.id])) continue; L.push({ P, v, k: zoneOf(P) + '|' + v.want + (v.want === 'h' ? p.crop : ''), g: -1 }); }
  const adj = (a, b) => { const A = a.P.b, B = b.P.b, dx = Math.max(0, A[0] - B[2], B[0] - A[2]), dz = Math.max(0, A[1] - B[3], B[1] - A[3]); return dx + dz < .45 && (dx < .01 || dz < .01); };
  let gi = 0; const GR = []; for (const a of L){ if (a.g >= 0) continue; a.g = gi; const q = [a], m = [a]; while (q.length){ const c = q.pop(); for (const b of L) if (b.g < 0 && b.k === c.k && adj(c, b)){ b.g = gi; q.push(b); m.push(b); } } GR.push(m); gi++; }
  for (const m of GR){ if (m.length < 3) continue; let x = 0, z = 0; for (const a of m){ x += a.v.cx; z += a.v.cz; } x /= m.length; z /= m.length; let ld = m[0], bd = 1e9; for (const a of m){ const d = (a.v.cx - x) ** 2 + (a.v.cz - z) ** 2; if (d < bd){ bd = d; ld = a; } } for (const a of m) a.v.clH = a !== ld; ld.v.clM = m.map(a => a.P.id); }
  for (const P of PLOTS){ const v = PV[P.id]; if (!v.want || !v.bub || !v.bub[v.want]) continue; v.bub[v.want].visible = !v.clH; if ('hwu'.includes(v.want)) clBadge(v.bub[v.want], v.clM ? v.clM.length : 0); } }
function plotHit0(cx, cy){""")
rep("for (const P of PLOTS){ const v = PV[P.id]; if (v.want) bubs.push(", "for (const P of PLOTS){ const v = PV[P.id]; if (v.want && !v.clH) bubs.push(")
rep("const KFNOW = kFull(); for (const P of PLOTS){ const v = PV[P.id]; if (!v.want) continue; const bg = v.bub[v.want];",
    "const KFNOW = kFull(); if (window.__CLD) try { clPass(); } catch (e) { window.__CLD = 0; if (!window.__cle){ window.__cle = 1; console.warn('cl', e); } } for (const P of PLOTS){ const v = PV[P.id]; if (!v.want || v.clH) continue; const bg = v.bub[v.want];")
rep("bubDot(bg, far); if (far){", "bubDot(bg, far); if (bg.userData.bdg) bg.userData.bdg.visible = !!bg.userData.bdgOn && !far; if (far){")
rep("const id = g.id; if (!id){ fan.hidden = true; PEND = null; return; }\n  if (g.need === 'cut'){ STROKE = { hits: new Set(), warned: new Set(), combo: 0 }; cutAt(PV[id].cx, PV[id].cz); STROKE = null; }\n  else if (g.need === 'water'){ STROKE = { hits: new Set(), warned: new Set(), combo: 0 }; waterAt(PV[id].cx, PV[id].cz, 0); STROKE = null; }",
    "const id = g.id; if (!id){ fan.hidden = true; PEND = null; return; } const CLM = g.bub && PV[id].clM ? PV[id].clM : [id];   /* cham bong bong gop: lam ca cum */\n  if (g.need === 'cut'){ STROKE = { hits: new Set(), warned: new Set(), combo: 0 }; for (const m of CLM){ const pm = ST.plots[m]; if (STROKE.hits.size && ripe(pm) && harvestN(pm) > kCap() - kUsed()) break; cutAt(PV[m].cx, PV[m].cz); } STROKE = null; }\n  else if (g.need === 'water'){ STROKE = { hits: new Set(), warned: new Set(), combo: 0 }; for (const m of CLM) waterAt(PV[m].cx, PV[m].cz, 0); STROKE = null; }")

# ---------- đoạn 3: việc ngày không ép mua khi chưa đủ xu ----------
rep("if (!ownObj(k)) F.push({ lv: d.lv + .5, t: 'own', k,", "if (!ownObj(k) && ST.xu >= (d.buy || 0)) F.push({ lv: d.lv + .5, t: 'own', k,")
rep("if (cauOn() && !ST.kca) F.push(", "if (cauOn() && !ST.kca && ST.xu >= KCA.xu) F.push(")
rep("  try { if (cauOn()) F.push({ lv: CAU.lv, t: 'fish',",
    "  try { if (lv >= BEP.lv && Object.keys(DISH).some(k => DISH[k].lv <= lv && !(ST.bep && ST.bep.made && ST.bep.made[k]))) F.push({ lv: BEP.lv + .3, t: 'newdish', txt: 'Nấu 1 món chưa từng nấu', need: 1, rw: ['coin', 30] }); } catch (e) {}\n"
    "  try { const ks = Object.keys(CROPS).filter(k => unlocked(k) && !CROPS[k].tree && !CROPS[k].rare && mastS(k) < 3); if (lv >= 5 && ks.length){ const dk = dayKey(); let h = 0; for (const ch of dk) h = (h * 31 + ch.charCodeAt(0)) % 9973; const k = ks[h % ks.length]; F.push({ lv: 5.2, t: 'mast', k, txt: `Hái 3 vụ ${CROPS[k].name.toLowerCase()} cho quen tay`, need: 3, rw: ['coin', 25] }); } } catch (e) {}\n"
    "  try { if (cauOn()) F.push({ lv: CAU.lv, t: 'fish',")
rep("B.made[p.k] = (B.made[p.k] || 0) + 1;", "if (!B.made[p.k]) setTimeout(() => { try { bump('newdish'); } catch (e) {} }, 0); B.made[p.k] = (B.made[p.k] || 0) + 1;")

# ---------- đoạn 3: sao thuần thục từng giống ----------
rep("ST.inv[p.crop] = (ST.inv[p.crop] || 0) + n; p.stolen = 0;", "ST.inv[p.crop] = (ST.inv[p.crop] || 0) + n; p.stolen = 0; try { mastUp(p.crop); } catch (e) {}")
rep("function pgGiong(){", r"""function mastT(k){ return CROPS[k].tree ? [4, 12, 30] : [8, 30, 80]; }
function mastN(k){ return (ST.hvK && ST.hvK[k]) || 0; }
function mastS(k){ const n = mastN(k), M = mastT(k); return n >= M[2] ? 3 : n >= M[1] ? 2 : n >= M[0] ? 1 : 0; }
function mastSt(s, z){ let h = ''; for (let i = 0; i < 3; i++) h += `<svg viewBox="0 0 24 24" width="${z}" height="${z}" aria-hidden="true"><path d="M12 2.6l2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 17.4l-5.8 3.1 1.1-6.5L2.6 9.4l6.5-.9z" fill="${i < s ? '#EDB940' : '#E3D3BC'}" stroke="${i < s ? '#C9952A' : '#CDBBA0'}" stroke-width="1.4" stroke-linejoin="round"/></svg>`; return h; }
function mastUp(k){ if (!ST.hvK) ST.hvK = {}; const a = mastS(k); ST.hvK[k] = mastN(k) + 1; try { bump('mast', 1, k); } catch (e) {} const b = mastS(k); if (b > a){ const c = CROPS[k], xu = Math.min(600, Math.max(20, Math.round(c.seed * b * 2 / 5) * 5)); ST.xu += xu; setTimeout(() => { try { gainXP(5 * b); sfx('up'); toast(`${c.name} lên ${b} sao thuần thục · +${xu} xu`); hud(); if (b === 3) say('Giống này con trồng thuần tay rồi đó. Ngoại khỏi dặn nữa.', 'vui', { idle: true }); } catch (e) {} }, 1300); } }
function mastRow(k){ const n = mastN(k), s = mastS(k), M = mastT(k); return `<div class="mast"><span class="msts">${mastSt(s, 24)}</span><div><b>Thuần thục</b><small>${s >= 3 ? `Đã hái ${n} vụ · đủ ba sao rồi` : `Đã hái ${n} vụ · còn ${M[s] - n} vụ nữa lên sao`}</small></div></div>`; }
function pgGiong(){""")
rep("""data-b="sel" data-k="${k}"><div class="pic"><img src="${ICON[k]}" alt=""></div><b>${c.name}</b><div class="sts">${stI('coin', c.seed)}""", """data-b="sel" data-k="${k}"><div class="pic"><img src="${ICON[k]}" alt=""></div><b>${c.name}</b><i class="mstt"${c.rare ? ' style="visibility:hidden"' : ''}>${mastSt(mastS(k), 13)}</i><div class="sts">${stI('coin', c.seed)}""")
rep("""${stI('yield', yS(c))}</div>`;
  if (c.tree) h += `<div class="bkhn" style="font-size:18px;color:#6B4529">Trồng một lần""", """${stI('yield', yS(c))}</div>` + (c.rare ? '' : mastRow(k));
  if (c.tree) h += `<div class="bkhn" style="font-size:18px;color:#6B4529">Trồng một lần""")
rep(".stk{appearance:none;", ".mast{display:flex;gap:10px;align-items:center;background:#FBF7EE;border:2px solid #E8DFCC;border-radius:14px;padding:8px 12px;margin:6px 0}.mast .msts{display:flex;gap:2px;flex:none}.mast b{display:block;font:16px/1.2 var(--f-game);color:#4A2F1E}.mast small{display:block;font-size:13px;color:#8A5D3B}.mstt{display:flex;justify-content:center;gap:1px;margin:1px 0 2px}\n.stk{appearance:none;")

# ---------- đoạn 3: Sổ món của Ngoại ----------
rep("const BSTK = ['giong', 'ca', 'buom', 'cotich', 'thu'], BSTN = { giong: 'Giống',", "const BSTK = ['giong', 'mon', 'ca', 'buom', 'cotich', 'thu'], BSTN = { mon: 'Món ăn', giong: 'Giống',")
rep("const tabOn = k => { const lv = ST.lv || 1; if (k === 'thu')", "const tabOn = k => { const lv = ST.lv || 1; if (k === 'mon') return lv >= BEP.lv || Object.keys((ST.bep && ST.bep.made) || {}).length > 0; if (k === 'thu')")
rep("const BTAB = { giong: ['Sổ giống', '#86B06A', '#4F7D44', 'seedbag'],", "const BTAB = { mon: ['Sổ món', '#E9A46A', '#B5622A', 'canhchua'], giong: ['Sổ giống', '#86B06A', '#4F7D44', 'seedbag'],")
rep("else if (tab === 'cotich'){ L = pgCotich(nr ? 0 : 1); Rr = nr ? '' : pgCotich(2); }", "else if (tab === 'cotich'){ L = pgCotich(nr ? 0 : 1); Rr = nr ? '' : pgCotich(2); } else if (tab === 'mon'){ L = pgMon(nr ? 0 : 1); Rr = nr ? '' : pgMon(2); }")
rep("function pgCotich(part){", r"""function pgMon(part){ const lv = ST.lv || 1, M = (ST.bep && ST.bep.made) || {}, ks = Object.keys(DISH), half = Math.ceil(ks.length / 2), list = part === 1 ? ks.slice(0, half) : part === 2 ? ks.slice(half) : ks, got = ks.filter(k => M[k]).length;
  let h = part === 2 ? '' : `<div class="bkhn" style="color:#B5622A">Sổ món của Ngoại · ${got}/${ks.length} món</div><div class="bkhn" style="font-size:13px;opacity:.8">Nấu món nào lần đầu, Ngoại kể chuyện món đó rồi chép vô đây.</div>`;
  return h + list.map(k => { const d = DISH[k], n = M[k] || 0, img = ICON[k] || ICON.la;
    if (n) return `<div class="ftc mon"><img src="${img}" alt=""><div><b>${d.name}</b><small>Đã nấu ${n} lần</small><p>${d.story}</p></div></div>`;
    if (lv >= d.lv) return `<div class="ftc mon no"><img src="${img}" alt=""><div><b>${d.name}</b><small>Chưa nấu lần nào</small><p>Nấu thử một lần, Ngoại kể chuyện món này cho nghe.</p></div></div>`;
    return `<div class="ftc mon no"><img src="${img}" alt=""><div><b>???</b><small>Món Ngoại chưa dạy</small><p>Vườn lớn thêm, Ngoại dạy thêm món.</p></div></div>`; }).join(''); }
function pgCotich(part){""")
rep(".ftc{display:flex;", ".ftc.mon small{color:#B5622A}.ftc.mon.no b{color:#8A7A66}\n.ftc{display:flex;")

# ---------- chữ tiếng Anh cho đoạn 3 ----------
rep('}, UIRX = [[', ', "Thuần thục": "Mastery", "Món ăn": "Dishes", "Sổ món": "Recipe book", "Chưa nấu lần nào": "Not cooked yet", "Nấu thử một lần, Ngoại kể chuyện món này cho nghe.": "Cook it once and Grandma will tell you its story.", "Món Ngoại chưa dạy": "Grandma has not taught this one yet", "Vườn lớn thêm, Ngoại dạy thêm món.": "As the garden grows, Grandma teaches more dishes.", "Nấu món nào lần đầu, Ngoại kể chuyện món đó rồi chép vô đây.": "The first time you cook a dish, Grandma tells its story and writes it down here.", "Nấu 1 món chưa từng nấu": "Cook 1 dish you have never made", "Giống này con trồng thuần tay rồi đó. Ngoại khỏi dặn nữa.": "You have this crop down pat now. Grandma has nothing left to remind you."}, UIRX = [["^Đã hái (\\\\d+) vụ · còn (\\\\d+) vụ nữa lên sao$", "Harvested $1 times · $2 more to the next star"], ["^Đã hái (\\\\d+) vụ · đủ ba sao rồi$", "Harvested $1 times · all three stars"], ["^Đã nấu (\\\\d+) lần$", "Cooked $1 times"], ["^Sổ món của Ngoại · (\\\\d+)/(\\\\d+) món$", "Grandma\'s recipe book · $1/$2 dishes"], ["^(.+) lên (\\\\d) sao thuần thục · \\\\+(\\\\d+) xu$", "$1 reached $2-star mastery · +$3 coins"], ["^Hái 3 vụ (.+) cho quen tay$", "Harvest $1 3 times for practice"], [')


open(DST, 'w', encoding='utf-8').write(s)
print('ok', DST, len(s))
