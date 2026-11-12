# v140 (anh Ares 11/11: bạn vô chợ nổi bấm không thấy chỗ trang trí ghe, sơn ghe chưa vui, màn chuyển cảnh chỉ là một màu xanh).
# (1) Xưởng sơn ngay trên xuồng: chạm xuồng mình hoặc ghe chú Chín -> máy quay lại gần xuồng, dải màu thấp phía dưới,
#     chạm màu là sơn thử (không tốn xu), bấm "Sơn · N xu" mới trả tiền. Sơn thiệt: cọ quẹt từ mũi tới lái, xuồng nhún.
# (2) Giá sơn, vẽ mắt mắc hơn (anh Ares: một ngày ra chợ lời nhiều xu rồi). Màu đã mua giữ nguyên, đổi qua lại không tốn.
# (3) Màn chuyển cảnh: xuồng mình (đúng màu sơn) chèo trên sông ra chợ nổi; đò máy nhả khói lên chợ huyện; về thì quay ngược.
# (4) Bỏ số cấp tương lai ở Bến nhà và tiệm chụp hình.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v139'", "BUILD = 'v140'")

# (2) giá
rep("eye: 500, zoom: 1.06,", "eye: 2000, zoom: 1.06,")
rep("ngoc: ['Xanh ngọc', 'Jade green', 300,", "ngoc: ['Xanh ngọc', 'Jade green', 1200,")
rep("son: ['Đỏ son', 'Vermilion', 600,", "son: ['Đỏ son', 'Vermilion', 2500,")
rep("nghe: ['Vàng nghệ', 'Turmeric gold', 1000,", "nghe: ['Vàng nghệ', 'Turmeric gold', 4000,")
rep("cham: ['Xanh chàm', 'Indigo', 1500,", "cham: ['Xanh chàm', 'Indigo', 6000,")

# (1) xưởng sơn
rep("shell(0, 0, hm); shell(.014, .016, MS('#D2A57E'));", "const sh0 = shell(0, 0, hm); shell(.014, .016, MS('#D2A57E'));")
rep("return { hm, tm, eye }; }", "return { hm, tm, eye, sh: sh0 }; }")
rep("function cnoRepaint(){ const c = cnoS(), p = CNX.P[c.paint] || CNX.P.moc, B = CHM.B; if (B && B.hl){ B.hl.hm.color.set(p[3]); B.hl.tm.color.set(p[4]); B.hl.eye.visible = !!c.eye; } cnoHome(); }",
r"""function cnoRepaint(){ const c = cnoS(), p = CNX.P[c.paint] || CNX.P.moc; cnoLook(p, !!c.eye); cnoHome(); }
/* v140: xưởng sơn ngay trên xuồng. Màu vỏ xuồng nằm ở màu từng đỉnh để cọ quẹt tới đâu đổi màu tới đó (mũi là +x). */
function cnoSweep(hl, c0, c1, f){ const g = hl.sh.geometry, P = g.attributes.position; let C = g.attributes.color; if (!C){ C = new T.Float32BufferAttribute(new Float32Array(P.count * 3), 3); g.setAttribute('color', C); hl.hm.vertexColors = true; hl.hm.color.set('#ffffff'); hl.hm.needsUpdate = true; }
  const a = new T.Color(c0), b = new T.Color(c1), L = .62, xe = L - f * (2 * L + .14); for (let i = 0; i < P.count; i++){ const k = Math.max(0, Math.min(1, (P.getX(i) - xe) / .14)); C.setXYZ(i, a.r + (b.r - a.r) * k, a.g + (b.g - a.g) * k, a.b + (b.b - a.b) * k); } C.needsUpdate = true; }
function cnoLook(p, eye){ const B = CHM.B; if (!B || !B.hl || !B.hl.sh) return; cnoSweep(B.hl, p[3], p[3], 1); B.hl.tm.color.set(p[4]); B.hl.eye.visible = !!eye; try { const e2 = B.meM && B.meM.children[B.me.children.indexOf(B.hl.eye)]; if (e2 && e2.isGroup && e2.children.length === B.hl.eye.children.length) e2.visible = !!eye; } catch (e) {} }
function cnoSon(on){ const B = CHM.B; if (!B || CHM.kind !== 'cn') return; if (on && CNX.ben) cnoBenV(0); const c = cnoS(); CNX.son = on ? 1 : 0; CNX.pa = null; CNX.sel = c.paint; CNX.msg = ''; if (B.br) B.br.visible = false; $('#chUi').classList.toggle('son', !!on); $('#cnSon').hidden = !on; $('#chSay').hidden = true; cnoRepaint(); if (on){ sfx('pick'); cnoSonUI(); } }
function cnoSonUI(){ const c = cnoS(), sel = CNX.sel, isE = sel === 'eye', q = CNX.P[sel], busy = !!CNX.pa; let h = '';
  for (const id in CNX.P){ const p = CNX.P[id], own = c.own[id] || !p[2], cur = c.paint === id; h += `<button class="sc${sel === id ? ' on' : ''}" data-k="${id}" aria-label="${esc(cnL(p[0], p[1]))}"><i style="background:linear-gradient(135deg,${p[3]} 62%,${p[4]} 62%)"></i><em>${cur ? cnL('Đang sơn', 'In use') : own ? cnL('Đã có', 'Owned') : p[2]}</em></button>`; }
  h += `<button class="sc${isE ? ' on' : ''}" data-k="eye" aria-label="${cnL('Vẽ mắt ghe', 'Boat eyes')}"><i class="ey"></i><em>${c.eye ? cnL('Đã vẽ', 'Done') : CNX.eye}</em></button>`; $('#cnSonW').innerHTML = h;
  let say, lab, off = busy;
  if (isE){ if (c.eye){ say = cnL('Xuồng con có mắt rồi, sáng trưng, thấy đường về bến.', 'Your boat has its eyes now, bright enough to find the way home.'); lab = cnL('Đã vẽ mắt', 'Eyes done'); off = true; } else { say = cnL(`Vẽ cặp mắt cho xuồng thấy đường. Ưng thì chú vẽ thiệt, ${CNX.eye} xu.`, `A pair of eyes so the boat sees its way. ${CNX.eye} coins if you like them.`); lab = cnL(`Vẽ mắt · ${CNX.eye} xu`, `Paint eyes · ${CNX.eye}`); } }
  else if (c.paint === sel){ say = cnL('Con lựa màu đi, chú sơn thử lên xuồng cho coi trước.', 'Pick a colour and I will try it on your boat first.'); lab = cnL('Đang sơn màu này', 'Current colour'); off = true; }
  else if (c.own[sel] || !q[2]){ say = cnL(`${q[0]} con có sẵn rồi, sơn lại chú không tính tiền.`, `You already own ${q[1]}. Repainting is free.`); lab = cnL('Sơn lại', 'Repaint'); }
  else { say = cnL(`${q[0]} đó con. Ưng thì chú sơn thiệt, ${q[2]} xu.`, `That is ${q[1]}. ${q[2]} coins if you like it.`); lab = cnL(`Sơn · ${q[2]} xu`, `Paint · ${q[2]}`); }
  $('#cnSonT').innerHTML = `<b>${cnL('Chú Chín', 'Uncle Chín')}</b>${esc(CNX.msg || say)}`; const go = $('#cnSonGo'); go.textContent = busy ? cnL('Đang sơn…', 'Painting…') : lab; go.disabled = off; $('#cnSonX').textContent = cnL('Xong', 'Done'); }
function cnoSonPick(k){ if (CNX.pa || (k !== 'eye' && !CNX.P[k])) return; const c = cnoS(); CNX.sel = k; CNX.msg = ''; cnoLook(CNX.P[k === 'eye' ? c.paint : k] || CNX.P.moc, c.eye || k === 'eye'); sfx('pop'); try { CHM.B.me.userData.hit = performance.now() / 1000 - .45; } catch (e) {} cnoSonUI(); }
function cnoSonGo(){ if (CNX.pa) return; const c = cnoS(), sel = CNX.sel, t0 = performance.now() / 1000;
  if (sel === 'eye'){ if (c.eye) return; if (ST.xu < CNX.eye) return toast(cnL(`Vẽ mắt ghe ${CNX.eye} xu, con để dành thêm nghe.`, `Boat eyes cost ${CNX.eye} coins. Save up a little more.`), 'dan'); ST.xu -= CNX.eye; c.eye = 1; coinPop(cnL(`-${CNX.eye} xu · vẽ mắt ghe`, `-${CNX.eye} coins · boat eyes`), '#F5D27A'); CNX.pa = { t0, d: .9, eye: 1 }; }
  else { const p = CNX.P[sel]; if (!p || c.paint === sel) return; if (!c.own[sel] && p[2]){ if (ST.xu < p[2]) return toast(cnL(`Màu này ${p[2]} xu, con để dành thêm nghe.`, `This colour is ${p[2]} coins. Save up a little more.`), 'dan'); ST.xu -= p[2]; c.own[sel] = 1; coinPop(cnL(`-${p[2]} xu · sơn ${p[0].toLowerCase()}`, `-${p[2]} coins · ${p[1]}`), '#F5D27A'); } const o = CNX.P[c.paint] || CNX.P.moc; c.paint = sel; CNX.pa = { t0, d: 1.25, a: o, b: p }; cnoHome(); }
  sfx('coin'); save(); hud(); cnoSonUI(); }
function cnoPaFrame(B, t){ const pa = CNX.pa; if (!pa || !B.hl || !B.hl.sh) return; const f = Math.max(0, Math.min(1, (t - pa.t0) / pa.d)), L = .62;
  if (!B.br){ const g = new T.Group(), mk = (w, h, d, c, y) => { const o = new T.Mesh(new T.BoxGeometry(w, h, d), new T.MeshStandardMaterial({ color: c, roughness: .9 })); o.position.y = y; o.castShadow = false; g.add(o); return o; }; mk(.035, .2, .035, '#8A5D3B', .15); g.userData.tip = mk(.12, .08, .05, '#ffffff', .02); g.scale.setScalar(1.25); B.me.add(g); B.br = g; }
  const br = B.br; br.visible = f < 1;
  if (pa.eye){ const k = f < 1 ? 1 + 2.2 * Math.pow(f - 1, 3) + 1.2 * Math.pow(f - 1, 2) : 1; B.hl.eye.visible = true; for (const o of B.hl.eye.children){ const q = o.userData; if (!q.s0) q.s0 = o.scale.clone(); o.scale.copy(q.s0).multiplyScalar(Math.max(.01, k)); } br.userData.tip.material.color.set('#F4F0E4'); br.position.set(.74 * L + Math.sin(t * 18) * .03, .2 + Math.abs(Math.sin(t * 9)) * .05, .2); br.rotation.set(.9, 0, Math.sin(t * 18) * .25); }
  else { const e = f * f * (3 - 2 * f); cnoSweep(B.hl, pa.a[3], pa.b[3], e); B.hl.tm.color.set(pa.a[4]).lerp(new T.Color(pa.b[4]), e); br.userData.tip.material.color.set(pa.b[3]); br.position.set(L - e * 2 * L, .16 + Math.sin(t * 20) * .045, .21); br.rotation.set(.9, 0, Math.sin(t * 20) * .35); }
  if (f >= 1){ CNX.pa = null; B.me.userData.hit = t; sfx('up'); CNX.msg = pa.eye ? cnL('Rồi đó, xuồng con có mắt rồi. Đi đâu cũng thấy đường về.', 'There, your boat has eyes now. It will always find the way home.') : cnL('Đẹp rồi đó con. Ra chợ ai cũng nhớ mặt xuồng mình.', 'Looks grand. Everyone at the market will remember your boat.'); cnoRepaint(); if (CNX.son) cnoSonUI(); } }""")
rep("if (B.meM){ B.meM.position.copy(me.position); B.meM.rotation.copy(me.rotation); }",
    "if (B.meM){ B.meM.position.copy(me.position); B.meM.rotation.copy(me.rotation); } cnoPaFrame(B, t);")
# máy quay lại gần xuồng mình
rep("b: [5, 9.2, -5.6, 5, .3, -16.2, 58] }, l: {", "b: [5, 9.2, -5.6, 5, .3, -16.2, 58], s: [.3, 2.2, 3.6, 0, -.3, 0, 46] }, l: {")
rep("b: [5, 5.8, -8.0, 5, .3, -16.4, 50] } };", "b: [5, 5.8, -8.0, 5, .3, -16.4, 50], s: [1.0, 1.35, 3.5, .8, .12, 0, 30] } };")
rep("C.fov = v[6]; C.aspect = innerWidth / innerHeight;",
    "{ let q = CNX.sk || 0; const g = CNX.son ? 1 : 0; q += (g - q) * .09; if (Math.abs(g - q) < .002) q = g; CNX.sk = q; if (q > 0 && CHM.B && CHM.B.me){ const m = CHM.B.me.position, o = V.s, es = q * q * (3 - 2 * q), w = [m.x + o[0], o[1], m.z + o[2], m.x + o[3], o[4], m.z + o[5], o[6]]; for (let i = 0; i < 7; i++) v[i] += (w[i] - v[i]) * es; } }\n  C.fov = v[6]; C.aspect = innerWidth / innerHeight;")
rep("if (d.ax && !CNX.ben)", "if (d.ax && !CNX.ben && !CNX.son)")
# chạm xuồng mình / ghe thợ sơn -> xưởng sơn
rep("function cnoTap(best){ if (!best) return; let a = best.slice(3);", "function cnoTap(best){ if (CNX.son){ if (best && best !== 'cn:so' && best !== 'cn:son' && !CNX.pa) cnoSon(0); return; } if (!best) return; let a = best.slice(3);")
rep("if (CNX.ben && a === 'so') a = 'ben'; CNX.t0 = performance.now();", "if (CNX.ben && a === 'so') a = 'ben'; else if (a === 'so' || a === 'son'){ cnoSon(1); return; } CNX.t0 = performance.now();")
rep("CNX.dl = 0; CNX.ben = 0; CNX.bk = 0;", "CNX.dl = 0; CNX.ben = 0; CNX.bk = 0; CNX.son = 0; CNX.sk = 0; CNX.pa = null; $('#chUi').classList.remove('son'); $('#cnSon').hidden = true;")
rep("if (!ST.seen.cn1){ ST.seen.cn1 = 1; save(); setTimeout(() => chSay(cnL('Chợ nổi đông vui ghê.",
    "if (ST.seen.cn1 && !ST.seen.cnson){ ST.seen.cnson = 1; save(); setTimeout(() => { if (CHM.on && CHM.kind === 'cn' && !CNX.son && !CNX.ben) chSay(cnL('Muốn sơn xuồng, vẽ mắt ghe thì chạm vô xuồng mình nghe con. Chú sơn thử cho coi trước, ưng mới tính tiền.', 'Tap your own boat when you want it painted. I will try the colour on first, and you only pay if you like it.'), cnL('Chú Chín', 'Uncle Chín')); }, 900); }\n    if (!ST.seen.cn1){ ST.seen.cn1 = 1; ST.seen.cnson = 1; save(); setTimeout(() => chSay(cnL('Chợ nổi đông vui ghê.")
rep("function cnoLeave(){ chFade(", "function cnoLeave(){ CNX.son = 0; CNX.pa = null; $('#chUi').classList.remove('son'); $('#cnSon').hidden = true; chFade(")
rep('<button class="btn g" id="chBack">Về vườn</button></div><div id="chFade" hidden><b></b></div>',
    '<button class="btn g" id="chBack">Về vườn</button><div id="cnSon" hidden><div class="sh" id="cnSonT"></div><div class="sw" id="cnSonW"></div><div class="sa"><button class="btn" id="cnSonX">Xong</button><button class="btn g" id="cnSonGo"></button></div></div></div><div id="chFade" hidden><div class="tv"></div><b></b></div>')
rep("$('#chBack').addEventListener('click', () => chLeave());",
    "$('#chBack').addEventListener('click', () => chLeave()); $('#cnSonW').addEventListener('click', e => { const b = e.target.closest('.sc'); if (b) cnoSonPick(b.dataset.k); }); $('#cnSonGo').addEventListener('click', () => cnoSonGo()); $('#cnSonX').addEventListener('click', () => { if (!CNX.pa){ sfx('pick'); cnoSon(0); } });")

# (3) màn chuyển cảnh
rep("function chFade(txt, mid){ const f = $('#chFade'); f.querySelector('b').textContent = fxT(txt); f.hidden = false; f.classList.remove('out'); void f.offsetWidth; f.classList.add('in'); setTimeout(() => { try { mid(); } catch (e) { console.warn('ch', e); } f.classList.remove('in'); f.classList.add('out'); setTimeout(() => { f.hidden = true; }, 520); }, 900); }",
r"""function chScene(kind, home){ const c = ST.cn || {}, P = CNX.P[c.paint] || CNX.P.moc;
  const palm = (x, h) => { const y = 100 - h, tx = x + 3; let f = ''; for (const [dx, dy] of [[-28, 12], [-25, -6], [-10, -19], [11, -19], [26, -6], [29, 12]]) f += `<path d="M${tx} ${y}Q${tx + dx * .55} ${y + dy - 9} ${tx + dx} ${y + dy}"/>`; return `<path d="M${x} 104Q${x + 5} ${100 - h / 2} ${tx} ${y}" stroke="#7A5A3A" stroke-width="4"/><g stroke="#4F8E52" stroke-width="4.5">${f}</g>`; };
  const bank = `<svg viewBox="0 0 600 120" aria-hidden="true"><path d="M0 120V80Q40 62 90 74T190 68T300 76T420 64T520 74T600 80V120Z" fill="#A4CBA0"/><g fill="none" stroke-linecap="round">${palm(64, 64)}${palm(112, 46)}${palm(412, 70)}${palm(548, 50)}</g><path d="M286 102v-15h34v15z" fill="#E3C894"/><path d="M279 89l24-15 24 15z" fill="#A8834F"/><path d="M0 120V98Q30 84 60 94T130 90T210 96T290 88T370 96T450 90T530 96T600 98V120Z" fill="#5F8F5A"/></svg>`;
  const foam = w => { let d = 'M-6 0'; for (let x = 0; x < w; x += 28) d += 'q7 -7 14 0t14 0'; return d; };
  const xuong = `<svg viewBox="0 0 240 130" aria-hidden="true"><path d="M65 76Q63 51 78 47Q93 51 93 76Z" fill="#7A5568"/><circle cx="79" cy="39" r="9" fill="#E8B98F"/><path d="M57 37L79 15L101 37Q79 43 57 37Z" fill="#EBD9A8" stroke="#C9B078" stroke-width="1.5"/>${home ? '' : '<circle cx="158" cy="50" r="7" fill="#6FAE4A"/><circle cx="168" cy="45" r="8" fill="#E8453A"/><circle cx="178" cy="50" r="7" fill="#F2C230"/>'}<path d="M149 53h38l-5 20h-28z" fill="#B8935A"/><path d="M6 62Q120 86 236 50Q204 96 152 98L84 98Q32 96 6 62Z" fill="${P[3]}"/><path d="M6 62Q120 86 236 50" fill="none" stroke="${P[4]}" stroke-width="6" stroke-linecap="round"/>${c.eye ? '<ellipse cx="205" cy="71" rx="8" ry="5.5" fill="#F4F0E4"/><circle cx="207" cy="71" r="2.8" fill="#1E1A16"/>' : ''}<g class="toar"><path d="M88 54L130 112" stroke="#8A5D3B" stroke-width="4" stroke-linecap="round"/><path d="M125 105l9 13" stroke="#8A5D3B" stroke-width="9" stroke-linecap="round"/></g><path d="${foam(250)}" transform="translate(0 101)" fill="none" stroke="#EAF6F0" stroke-width="5" stroke-linecap="round" opacity=".85"/></svg>`;
  const domay = `<svg viewBox="0 0 300 150" aria-hidden="true"><g class="tsm" fill="#F4F0E4"><circle cx="40" cy="56" r="8"/><circle cx="40" cy="56" r="8" style="animation-delay:.36s"/><circle cx="40" cy="56" r="8" style="animation-delay:.72s"/></g><rect x="37" y="60" width="6" height="26" fill="#5A4A40"/><path d="M252 44V16" stroke="#6B4529" stroke-width="3"/><path d="M252 17l-20 6 20 6z" fill="#F2C230"/><rect x="72" y="50" width="154" height="40" fill="#F6EBD0"/>${[84, 120, 156, 192].map(x => `<rect x="${x}" y="58" width="24" height="18" rx="3" fill="#7DB7C6"/>`).join('')}<rect x="62" y="40" width="174" height="11" rx="5.5" fill="#B8402E"/><path d="M8 88L292 80Q282 124 244 126L52 126Q20 122 8 88Z" fill="#2F6F8F"/><path d="M10 89L290 81" stroke="#F4F0E4" stroke-width="7" stroke-linecap="round"/><path d="M17 102L285 95" stroke="#E0A526" stroke-width="3.5" stroke-linecap="round"/><ellipse cx="266" cy="106" rx="9" ry="6" fill="#F4F0E4"/><circle cx="268" cy="106" r="3" fill="#1E1A16"/>${[92, 152, 212].map(x => `<circle cx="${x}" cy="112" r="6.5" fill="none" stroke="#2B2522" stroke-width="4"/>`).join('')}<path d="${foam(330)}" transform="translate(-22 129)" fill="none" stroke="#EAF6F0" stroke-width="6" stroke-linecap="round" opacity=".9"/></svg>`;
  const lb = `<svg viewBox="0 0 60 30" aria-hidden="true"><ellipse cx="20" cy="20" rx="17" ry="7" fill="#4F8E52"/><ellipse cx="40" cy="22" rx="15" ry="6" fill="#62A25C"/><ellipse cx="30" cy="16" rx="10" ry="5" fill="#74B36A"/><circle cx="26" cy="9" r="5" fill="#B79AE0"/><circle cx="26" cy="9" r="2" fill="#F2E3A0"/></svg>`;
  let h = '<div class="tsky"></div><div class="tsun"></div><i class="tcl" style="left:12%;top:11%;width:22vh"></i><i class="tcl" style="left:58%;top:24%;width:15vh;--d:-14vw"></i>';
  h += `<div class="tbank">${bank.repeat(5)}</div><div class="twat"></div>`;
  for (const [l, t2, w] of [[8, 52, 44], [46, 55, 60], [80, 51, 36], [22, 61, 52], [66, 64, 70], [104, 58, 48]]) h += `<i class="twv" style="left:${l}%;top:${t2}%;width:${w}px"></i>`;
  h += kind === 'cn' ? `<div class="tboat"><div class="tbob">${xuong}</div></div>` : `<div class="tboat fr"><div class="tbob">${domay}</div></div>`;
  for (const [l, t2, w, d] of [[30, 76, 58, -46], [78, 82, 76, -60], [118, 72, 50, -52], [58, 90, 90, -70]]) h += `<i class="twv" style="left:${l}%;top:${t2}%;width:${w}px;--d:${d}vw;opacity:.55;height:4px"></i>`;
  for (const [l, t2, d] of [[62, 79, -58], [104, 87, -74], [18, 91, -66]]) h += `<div class="tlb" style="left:${l}%;top:${t2}%;--d:${d}vw">${lb}</div>`;
  return h; }
function chFade(txt, mid, kind, home){ const f = $('#chFade'), tv = f.querySelector('.tv'); f.querySelector('b').textContent = fxT(txt); try { tv.innerHTML = chScene(kind || 'ch', home); tv.classList.toggle('hm', !!home); } catch (e) { console.warn('ch scene', e); } f.hidden = false; f.classList.remove('out'); void f.offsetWidth; f.classList.add('in'); setTimeout(() => { try { mid(); } catch (e) { console.warn('ch', e); } setTimeout(() => { f.classList.remove('in'); f.classList.add('out'); setTimeout(() => { f.hidden = true; tv.innerHTML = ''; }, 480); }, 600); }, 1000); }""")
rep("chFade('Đò máy chạy lên chợ huyện…', () => {", "chFade('Đò máy chạy lên chợ huyện…', () => {")
a = s.index("function chEnter("); b = s.index("function chCamSync(")
seg = s[a:b]
assert seg.count("$('#chUi').hidden = true; $('#chSay').hidden = true; chFree(); }); }") == 1
seg = seg.replace("$('#chUi').hidden = true; $('#chSay').hidden = true; chFree(); }); }", "$('#chUi').hidden = true; $('#chSay').hidden = true; chFree(); }, 'ch', 1); }")
i = seg.index("function chLeave("); j = seg.rindex("}); }", 0, i); assert j > 0
seg = seg[:j] + "}, 'ch', 0); }" + seg[j + 5:]
s = s[:a] + seg + s[b:]
a = s.index("function cnoEnter("); b = s.index("function cnoLeave("); c2 = s.index("try { cnoHome(); } catch (e) {}", b)
seg = s[a:b]; j = seg.rindex("}); }"); seg = seg[:j] + "}, 'cn', 0); }" + seg[j + 5:]
seg2 = s[b:c2]; j = seg2.rindex("}); }"); seg2 = seg2[:j] + "}, 'cn', 1); }" + seg2[j + 5:]
s = s[:a] + seg + seg2 + s[c2:]
assert s.count("}, 'cn', 0); }") == 1 and s.count("}, 'cn', 1); }") == 1 and s.count("}, 'ch', 0); }") == 1 and s.count("}, 'ch', 1); }") == 1

rep("#chFade b{font-family:var(--f-game);color:#FBF2DA;font-size:22px}",
    "#chFade b{font-family:var(--f-game);color:#FBF2DA;font-size:22px}"
    "#chFade{background:#5FA9A8;overflow:hidden;transition:opacity .35s}"
    "#chFade .tv{position:absolute;inset:0;overflow:hidden}#chFade .tv.hm{transform:scaleX(-1)}"
    "#chFade .tsky{position:absolute;left:0;right:0;top:0;height:47%;background:linear-gradient(#BCE2EC,#F5ECCB)}"
    "#chFade .tsun{position:absolute;right:13%;top:8%;width:11vh;height:11vh;border-radius:50%;background:#FFF6D8;box-shadow:0 0 0 2.4vh rgba(255,246,216,.4)}"
    "#chFade .tcl{position:absolute;height:3.6vh;border-radius:99px;background:#FFFDF6;opacity:.9;--d:-9vw;animation:tsl 3s linear both}"
    "#chFade .tbank{position:absolute;left:0;bottom:53%;height:20vh;display:flex;--d:-22vh;animation:tsl 3s linear both}"
    "#chFade .tbank svg{height:100%;width:auto;flex:none;display:block;margin-right:-1px}"
    "#chFade .twat{position:absolute;left:0;right:0;top:47%;bottom:0;background:linear-gradient(#7CC0B8,#4A979C 55%,#3C858F)}"
    "#chFade .twv{position:absolute;height:3px;border-radius:3px;background:#EAF6F0;opacity:.42;--d:-26vw;animation:tsl 3s linear both}"
    "#chFade .tboat{position:absolute;left:0;top:49%;width:min(60vw,320px);--a:-8vw;--b:40vw;animation:tgo 2.9s cubic-bezier(.2,.1,.5,1) both}"
    "#chFade .tboat.fr{width:min(64vw,380px);top:45%;--a:-24vw;--b:26vw}"
    "#chFade .tbob{transform-origin:50% 80%;animation:tbob .8s ease-in-out infinite alternate}"
    "#chFade .tbob svg{display:block;width:100%;height:auto;overflow:visible}"
    "#chFade .toar{transform-box:fill-box;transform-origin:0 0;animation:toar .62s ease-in-out infinite alternate}"
    "#chFade .tsm circle{transform-box:fill-box;transform-origin:center;opacity:0;animation:tsm 1.08s ease-out infinite}"
    "#chFade .tlb{position:absolute;width:min(22vw,110px);animation:tsl 3s linear both}#chFade .tlb svg{display:block;width:100%;height:auto}"
    "#chFade b{position:absolute;left:50%;bottom:calc(11% + env(safe-area-inset-bottom,0px));transform:translateX(-50%);background:#FFF8EA;color:#4A2F1E;font-size:18px;font-weight:400;padding:9px 18px;border-radius:999px;box-shadow:0 3px 0 #E3D3BC,0 8px 20px rgba(43,52,70,.22);white-space:nowrap;max-width:calc(100vw - 32px)}"
    "@keyframes tsl{from{transform:translateX(0)}to{transform:translateX(var(--d,-30vw))}}"
    "@keyframes tgo{from{transform:translateX(var(--a))}to{transform:translateX(var(--b))}}"
    "@keyframes tbob{from{transform:rotate(-2deg)}to{transform:rotate(2deg) translateY(4px)}}"
    "@keyframes toar{from{transform:rotate(-15deg)}to{transform:rotate(13deg)}}"
    "@keyframes tsm{from{transform:translate(0,0) scale(.6);opacity:.8}to{transform:translate(-36px,-30px) scale(1.9);opacity:0}}"
    "@media (orientation:landscape) and (max-height:540px){#chFade .tboat{width:min(60vw,58vh);top:47%}#chFade .tboat.fr{width:min(64vw,74vh);top:40%}#chFade b{bottom:calc(3% + env(safe-area-inset-bottom,0px))}}"
    "@media (prefers-reduced-motion:reduce){#chFade .tv *{animation:none!important}}"
    # xưởng sơn
    "#chUi.son > :not(#cnSon){display:none!important}#cnSon[hidden]{display:none}"
    "#cnSon{width:min(430px,calc(100vw - 20px));box-sizing:border-box;background:#FFF8EA;border-radius:20px;padding:10px 12px 12px;box-shadow:0 4px 0 #E3D3BC,0 10px 24px rgba(43,52,70,.25);color:var(--ink)}"
    "#cnSon .sh{font-size:14px;line-height:1.35;min-height:38px}#cnSon .sh b{font-family:var(--f-game);font-weight:400;font-size:14px;color:#B02A1A;margin-right:6px}"
    "#cnSon .sw{display:flex;gap:2px;margin:8px 0 10px}"
    "#cnSon .sc{appearance:none;-webkit-appearance:none;border:0;background:none;padding:6px 0 4px;flex:1 1 0;min-width:44px;min-height:72px;display:flex;flex-direction:column;align-items:center;gap:5px;font:inherit;border-radius:14px;touch-action:manipulation}"
    "#cnSon .sc i{width:42px;height:42px;border-radius:50%;box-shadow:inset 0 0 0 2px rgba(0,0,0,.14);display:block}"
    "#cnSon .sc i.ey{background:radial-gradient(ellipse 34% 26% at 54% 50%,#1E1A16 0 38%,transparent 40%),radial-gradient(ellipse 34% 24% at 50% 50%,#F4F0E4 0 98%,transparent 100%),#B48560}"
    "#cnSon .sc.on{background:#F1E2BF}#cnSon .sc.on i{box-shadow:0 0 0 3px #FFF8EA,0 0 0 6px #6E9A54}"
    "#cnSon .sc em{font-style:normal;font-size:12px;line-height:1.1;font-weight:800;color:#6B4529;white-space:nowrap}"
    "#cnSon .sa{display:flex;gap:8px}#cnSon .sa .btn{height:52px;font-size:17px;min-width:0}#cnSonX{flex:0 0 92px}#cnSonGo{flex:1 1 auto}#cnSonGo:disabled{opacity:.6}"
    "@media (orientation:landscape) and (max-height:540px){#chUi.son{justify-content:flex-end!important;align-items:flex-end!important;padding-right:calc(12px + env(safe-area-inset-right,0px));box-sizing:border-box}#cnSon{width:340px;padding:8px 10px 10px}#cnSon .sw{margin:4px 0 6px}#cnSon .sc{min-height:66px;padding:4px 0 2px}#cnSon .sc i{width:38px;height:38px}#cnSon .sa .btn{height:46px}}")

# (4) bỏ số cấp tương lai
rep("return lv >= 18 ? `<div class=\"meta\">Lên cấp ${CHM.lv} có đò máy lên chợ huyện.</div>` : ''; }", "return lv >= 18 ? `<div class=\"meta\">${fxT('Nghe nói bến mình sắp có đò máy lên chợ huyện.')}</div>` : ''; }")
rep("'Tiệm chụp hình đang sửa sang. Lên cấp 25 rủ Ngoại lên chụp chung một tấm.'", "'Tiệm chụp hình đang sửa sang. Bữa nào mở cửa rủ Ngoại lên chụp chung một tấm nghe.'")
rep('"Tiệm chụp hình đang sửa sang. Lên cấp 25 rủ Ngoại lên chụp chung một tấm.": "The photo studio is being done up. At level 25 bring Grandma for a picture together.",',
    '"Tiệm chụp hình đang sửa sang. Bữa nào mở cửa rủ Ngoại lên chụp chung một tấm nghe.": "The photo studio is being done up. Bring Grandma for a picture together once it opens.", "Nghe nói bến mình sắp có đò máy lên chợ huyện.": "They say a motor ferry to the district market is coming to our pier soon.",')

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
