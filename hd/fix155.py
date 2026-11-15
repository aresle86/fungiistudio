# NHÁP v155: (1) nhân vật qua rạch thì đi trên cầu (cầu khỉ / cầu ván), hết lội thẳng qua nước;
# (2) bong bóng xu ở khạp nuôi cá tự né xuống dưới khi nằm sau thẻ "Ngoại nhờ".
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v154'", "BUILD = 'v155'")

# ---- (1) đường qua cầu ----
rep("function avTick(dt){ if (!AVW) return;",
    "/* v155: qua rạch thì vòng ra đầu cầu, đi dọc cầu, cao theo mặt cầu */\n"
    "function avVia(to){ if (!((ST.kia || {}).n >= 1)) return null; const p = AVW.position, zA = KIA.z0 - .12, zB = KIA.z0 + KIA.len + .12, far = to.z > KIA.z0 + KIA.len / 2;\n"
    "  if (far ? p.z >= zB - .005 : p.z <= zA + .005) return null; const V = avVia.v || (avVia.v = new T.Vector3());\n"
    "  if (Math.abs(p.x - KIA.x) < .02 && p.z >= zA - .01 && p.z <= zB + .01) return V.set(KIA.x, 0, far ? zB : zA);\n"
    "  return V.set(KIA.x, 0, p.z > KIA.z0 + KIA.len / 2 ? zB : zA); }\n"
    "function avKiaY(){ const n = (ST.kia || {}).n || 0, p = AVW.position, L = KIA.len, z = p.z - KIA.z0; if (!n || Math.abs(p.x - KIA.x) > .1 || z < -.12 || z > L + .12) return 0;\n"
    "  if (n >= 2){ const e = z < 0 ? (z + .12) / .12 : z > L ? (L + .12 - z) / .12 : 1; return e * (.06 + .42 * Math.sin(Math.PI * Math.min(1, Math.max(0, z / L)))); }\n"
    "  const P = [[-.12, 0], [.42, .59], [2.32, .59], [L + .12, 0]]; for (let i = 0; i < 3; i++) if (z <= P[i + 1][0]) return P[i][1] + (P[i + 1][1] - P[i][1]) * (z - P[i][0]) / (P[i + 1][0] - P[i][0]); return 0; }\n"
    "function avTick(dt){ if (!AVW) return;")
rep("const to = AVT || AVHOME, d = new T.Vector3().subVectors(to, AVW.position); d.y = 0; const L = d.length();",
    "const via = avVia(AVT || AVHOME), to = via || AVT || AVHOME, d = new T.Vector3().subVectors(to, AVW.position); d.y = 0; const L = d.length();")
rep("d.normalize(); AVW.position.addScaledVector(d, Math.min(L, dt * 1.5));",
    "d.normalize(); const ky0 = avKiaY(); AVW.position.addScaledVector(d, Math.min(L, dt * (ky0 > .01 && ST.kia.n === 1 ? .8 : 1.5)));")
rep("AVW.position.y = Math.abs(Math.sin(performance.now() / 90)) * .02; return; }",
    "AVW.position.y = avKiaY() + Math.abs(Math.sin(performance.now() / 90)) * .02; return; }\n"
    "  if (via){ AVW.position.x = via.x; AVW.position.z = via.z; return; }")

# ---- (2) bong bóng khạp cá né thẻ Ngoại nhờ ----
rep("function bubHit(V, cx, cy){",
    "/* v155: bong bóng nằm sau thẻ Ngoại nhờ thì trượt xuống ngay dưới thẻ cho thấy và bấm được */\n"
    "function bubDodge(b, t){ const el = document.getElementById('nxq'); if (!el || el.hidden) return; const D = bubDodge; if (!(D.t0 <= t && D.t0 > t - .5)){ D.t0 = t; D.r = el.getBoundingClientRect(); } const r = D.r; if (!r || !r.width) return;\n"
    "  const p = (D.v || (D.v = new T.Vector3())).copy(b.position).project(cam), sx = (p.x + 1) / 2 * innerWidth, sy = (1 - p.y) / 2 * innerHeight, wpp = (cam.top - cam.bottom) / cam.zoom / innerHeight, rad = .27 * b.scale.x / wpp, bot = r.bottom + 8;\n"
    "  if (sx < r.left - rad || sx > r.right + rad || sy < r.top - rad || sy - rad >= bot) return; const need = (bot + rad - sy) * wpp; if (need > 1.2) return;\n"
    "  b.position.addScaledVector((D.u || (D.u = new T.Vector3())).set(0, 1, 0).applyQuaternion(cam.quaternion), -need); }\n"
    "function bubHit(V, cx, cy){")
rep("if (ST.kcaXu > 0 && KCAV.b) objBub(KCAV, { cx: KCA.at[0], cz: KCA.at[1] }, UIC.coin, t, .78);",
    "if (ST.kcaXu > 0 && KCAV.b){ objBub(KCAV, { cx: KCA.at[0], cz: KCA.at[1] }, UIC.coin, t, .78); try { bubDodge(KCAV.b, t); } catch (e) {} }")

# ---- (3) mặc cả với ông Bảy: giữ ngón cho giá leo, coi mặt ông mà buông (thay nút Nói thách ăn may) ----
rep("(!first && (bayS().th[k] || 1) > 1 ? 1.2 : 1)", "(!first && (bayS().th[k] || 1) > 1 ? bayS().th[k] : 1)")
rep("UX.btn('baythach', 'Nói thách', { k, dis: B.th[k] != null })", "UX.btn('baythach', 'Mặc cả', { k, dis: B.th[k] != null })")
rep('"Nói thách": "Haggle",', '"Nói thách": "Haggle", "Mặc cả": "Haggle", "Mối quen": "Regular", "Giữ để nâng giá": "Hold to raise the price", "Thôi, để sau": "Not now", "Giữ nút cho giá leo lên. Thấy ông Bảy lau kiếng là sắp tới ngưỡng, buông tay kẻo lố.": "Hold the button and the price climbs. When Uncle Bảy wipes his glasses you are near his limit, so let go in time.", "Ừa, chừng nào muốn thì nói qua.": "Sure, tell me whenever you like.",')
rep("  h += UX.title('Món quý cháu đang có');",
    "  if (S.mc && bayN(S.mc) > 0 && B.stamp[S.mc] && B.th[S.mc] == null) return bayMcHTML(S.mc); delete S.mc;\n"
    "  h += UX.title('Món quý cháu đang có');")
rep("function bayAct(a, b){",
    "/* v155: mặc cả. Giá leo 8% mỗi giây tới +40%; ngưỡng ẩn 15 tới 35% đổi theo ngày; lố ngưỡng vẫn được +5% */\n"
    "function mcK(){ return mcK.c || (mcK.c = { max: .4, rate: .08, lo: .15, hi: .35, quen: 5, over: 1.05, warn: .7 }); }\n"
    "function mcQuen(){ return ((ST.bay || {}).vis || 0) >= mcK().quen; }\n"
    "function mcLim(){ const B = bayS(), K = mcK(), d = dayKey(); if (!B.ml || B.ml[0] !== d) B.ml = [d, +(K.lo + Math.random() * (K.hi - K.lo)).toFixed(3)]; return Math.min(K.max, +(B.ml[1] + (mcQuen() ? .05 : 0)).toFixed(3)); }\n"
    "function mcTxt(st){ return st ? L135('Ủa, giá đó hả... để qua coi lại cái đã.', 'Hm, that much... let me take another look.') : L135('Ờ, hàng coi cũng được đó.', 'Well, it does look good.'); }\n"
    "function bayMcHTML(k){ let pic = ''; try { pic = bayArt().pic('xem'); } catch (e) {} const S = SHEET.bay, p0 = bayPrice(k, 0);\n"
    "  return `<div class=\"bayh\"><img id=\"mcPic\" src=\"${pic}\" alt=\"\"><div class=\"bayq\" id=\"mcSay\">${S.line}</div></div>` + UX.title('Mặc cả', mcQuen() ? 'Mối quen' : '')\n"
    "    + `<div class=\"qset\"><img src=\"${ICON[k]}\" alt=\"\"><div><b>${bayName(k)} · ${bayN(k)}</b><span id=\"mcGia\">${L135('Qua mua ' + p0 + ' xu một ' + bayU(k), 'I buy at ' + p0 + ' coins each')}</span></div></div>`\n"
    "    + '<div class=\"mcm\"><i id=\"mcBar\"></i></div><p class=\"bayn\">Giữ nút cho giá leo lên. Thấy ông Bảy lau kiếng là sắp tới ngưỡng, buông tay kẻo lố.</p>'\n"
    "    + `<div class=\"cta\"><button class=\"btn g mch\" id=\"mcHold\" data-mc=\"${k}\"><span>Giữ để nâng giá</span></button></div>` + UX.cta([UX.btn('baymcx', 'Thôi, để sau')]); }\n"
    "function mcDraw(H){ const K = mcK(), $ = id => document.getElementById(id), bar = $('mcBar'), gia = $('mcGia'); if (bar) bar.style.transform = `scaleX(${(H.pct / K.max).toFixed(3)})`;\n"
    "  if (gia) gia.textContent = H.pct > 0 ? L135(`${H.p0} lên ${Math.round(H.p0 * (1 + H.pct))} xu · thêm ${Math.round(H.pct * 100)}%`, `${H.p0} up to ${Math.round(H.p0 * (1 + H.pct))} coins · +${Math.round(H.pct * 100)}%`) : L135('Qua mua ' + H.p0 + ' xu một ' + bayU(H.k), 'I buy at ' + H.p0 + ' coins each');\n"
    "  const st = H.pct / H.lim >= K.warn ? 1 : 0; if (st !== H.st){ H.st = st; const im = $('mcPic'), sy = $('mcSay'); try { if (im) im.src = bayArt().pic(st ? 'lau' : 'xem'); } catch (e) {} if (sy) sy.textContent = mcTxt(st); if (st) try { buzz(12); } catch (e) {} } }\n"
    "function mcStart(b){ if (mcStart.H) return; const k = b.dataset.mc, B = bayS(); if (!k || !bayN(k) || B.th[k] != null) return; const K = mcK(), H = mcStart.H = { k, b, t0: performance.now(), lim: mcLim(), p0: bayPrice(k, 0), st: -1, pct: 0 };\n"
    "  b.classList.add('ing'); try { sfx('pick'); } catch (e) {} const step = () => { if (mcStart.H !== H) return; H.pct = Math.min(K.max, (performance.now() - H.t0) / 1000 * K.rate); if (H.pct > H.lim + 1e-6){ mcEnd(1); return; } mcDraw(H); if (H.pct >= K.max){ mcEnd(0); return; } H.raf = requestAnimationFrame(step); }; step(); }\n"
    "function mcEnd(over){ const H = mcStart.H; if (!H) return; mcStart.H = null; cancelAnimationFrame(H.raf); H.b.classList.remove('ing'); const B = bayS(), K = mcK(), S = SHEET && SHEET.bay, pc = Math.round(H.pct * 100);\n"
    "  if (!over && pc < 2){ H.pct = 0; H.st = -1; mcDraw(H); return; }\n"
    "  B.th[H.k] = over ? K.over : 1 + pc / 100;\n"
    "  if (S){ delete S.mc; S.pose = over ? 'kha' : 'xem'; S.line = over ? L135('Khà khà, cháu hét giá quá tay rồi. Thôi qua thêm chút đỉnh lấy thảo.', 'Ha ha, you pushed too far. Fine, a little extra for goodwill.') : L135(`Ừa, hàng đẹp vậy thì qua trả thêm ${pc}% cho cháu.`, `All right, goods this fine, I will pay ${pc}% more.`); }\n"
    "  try { sfx(over ? 'pick' : 'up'); buzz(over ? 30 : 18); } catch (e) {} save(); hud(); if (S) renderSheet(); }\n"
    "function bayAct(a, b){")
rep("else if (a === 'baythach'){ if (B.th[k] != null) return; if (Math.random() < .6){ B.th[k] = 1.2; S.pose = 'xem'; S.line = 'Ừa, hàng đẹp vậy thì qua trả thêm cho cháu.'; try { sfx('up'); } catch (e) {} } else { B.th[k] = 1; S.pose = 'kha'; S.line = 'Khà khà, cháu nói thách còn non lắm.'; try { sfx('pick'); } catch (e) {} } }",
    "else if (a === 'baythach'){ if (B.th[k] != null) return; S.mc = k; S.pose = 'xem'; S.line = L135('Cháu muốn nhiêu thì nói qua nghe coi.', 'Name your price, let me hear it.'); try { sfx('pick'); } catch (e) {} }\n"
    "  else if (a === 'baymcx'){ delete S.mc; S.pose = 'xem'; S.line = 'Ừa, chừng nào muốn thì nói qua.'; try { sfx('pick'); } catch (e) {} }")
rep("S.pose = 'xem'; S.line = 'Món này qua chở lên chợ huyện, người ta quý lắm.'; }",
    "S.pose = 'xem'; S.line = 'Món này qua chở lên chợ huyện, người ta quý lắm.';\n"
    "    if (B.vd !== dayKey()){ B.vd = dayKey(); B.vis = (B.vis || 0) + 1; if (B.vis === mcK().quen){ S.pose = 'kha'; S.line = L135('Cháu bán cho qua riết thành mối quen rồi. Từ rày qua chịu giá rộng tay hơn.', 'You have sold to me so often we are regulars now. From here on I will go a bit higher.'); } } }")
rep("/* hết xu, hết hạt, vườn trống: Ngoại cho hạt, mỗi ngày một lần */",
    "/* v155: giữ nút mặc cả */\n"
    "shB.addEventListener('pointerdown', e => { const b = e.target.closest('[data-mc]'); if (!b) return; e.preventDefault(); mcStart(b); });\n"
    "addEventListener('pointerup', () => mcEnd(0)); addEventListener('pointercancel', () => mcEnd(0)); addEventListener('blur', () => mcEnd(0));\n"
    "shB.addEventListener('contextmenu', e => { if (e.target.closest('[data-mc]')) e.preventDefault(); });\n"
    "shB.addEventListener('keydown', e => { if ((e.key === ' ' || e.key === 'Enter') && !e.repeat){ const b = e.target.closest('[data-mc]'); if (b){ e.preventDefault(); mcStart(b); } } });\n"
    "shB.addEventListener('keyup', e => { if (e.key === ' ' || e.key === 'Enter') mcEnd(0); });\n"
    "/* hết xu, hết hạt, vườn trống: Ngoại cho hạt, mỗi ngày một lần */")
rep(".bayn{margin:0 0 8px;text-align:center;font:600 12px/1.4 var(--f-body);color:#8A6A4A}",
    ".bayn{margin:0 0 8px;text-align:center;font:600 12px/1.4 var(--f-body);color:#8A6A4A}\n"
    ".mcm{height:16px;border-radius:999px;background:#EADFC8;box-shadow:inset 0 0 0 2px #E3C9A6;overflow:hidden;margin:0 0 8px}.mcm i{display:block;width:100%;height:100%;border-radius:999px;background:linear-gradient(90deg,#E9B23A,#E0803A);transform:scaleX(0);transform-origin:0 50%}\n"
    ".mch{touch-action:none;-webkit-user-select:none;user-select:none;-webkit-touch-callout:none}.mch.ing{transform:translateY(3px);box-shadow:0 1px 0 var(--woodD)}")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
