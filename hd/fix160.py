# v159 -> v160:
# 1) cá nhỏ trên ghe ông Bảy treo đầu lên, miệng chạm móc (trước treo ngang gốc đuôi, vây đuôi lòi lên trên móc).
#    Chỉ đổi trong mini(); hình mFish giữ nguyên vì còn dùng ở 2 chỗ khác.
# 2) bảng "Ngoại nghe đồn" không tự nhảy ra khi đang mở buồng thay đồ.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), n, a[:60])
    s = s.replace(a, b)
rep("BUILD = 'v159'", "BUILD = 'v160'")
rep(": mFish(q, 0, -.13, 0, 1.25, ...(FC[k] || FC.locbong));",
    ": (w => { w.rotation.z = Math.PI; mFish(w, -.017, .15, 0, 1.25, ...(FC[k] || FC.locbong)); })(G(0, 0, 0, 0, q));")
rep("try { b = busy() || !ng.hidden; } catch (e) {} if (b) return; ftrShow(pick); }",
    "try { b = busy() || !ng.hidden || !document.getElementById('intro').hidden; } catch (e) {} if (b) return; ftrShow(pick); }")
# 3) bộ nhớ icon: icon vẽ từ khối 3D lúc tải chiếm chừng 1/3 thời gian. Vẽ xong cất vô IndexedDB theo "dấu tay" của khối
#    (cỡ hình, máy quay, toạ độ, màu); lần tải sau (và mỗi lần qua vườn bạn) lấy lại, khỏi vẽ. Khác bản thì bỏ hết.
rep("const toonLost = r => {", r"""const TC = { k: BUILD + ':' + [...document.scripts].reduce((n, x) => n + x.textContent.length, 0), m: {}, use: {}, hit: 0, miss: 0, skip: 0, t: 0 };
window.__tc = TC;
const tcDB = () => new Promise((res, rej) => { const q = indexedDB.open('mv2-ic', 1); q.onupgradeneeded = () => q.result.createObjectStore('k'); q.onsuccess = () => res(q.result); q.onerror = q.onblocked = () => rej(q.error); });
try { await Promise.race([(async () => { const db = await tcDB(); const v = await new Promise((res, rej) => { const g = db.transaction('k').objectStore('k').get('ic'); g.onsuccess = () => res(g.result); g.onerror = () => rej(g.error); }); db.close(); if (v && v.k === TC.k && v.m) TC.m = v.m; })(), new Promise(r => setTimeout(r, 600))]); } catch (e) {}
function tcSave(){ clearTimeout(TC.t); TC.t = setTimeout(async () => { try { let m = Object.assign({}, TC.m, TC.use); if (Object.keys(m).length > 1200) m = TC.use; const db = await tcDB(), tx = db.transaction('k', 'readwrite'); tx.objectStore('k').put({ k: TC.k, m }, 'ic'); tx.oncomplete = tx.onerror = tx.onabort = () => db.close(); } catch (e) {} }, 3000); }
const TCF = new Float32Array(1), TCU = new Uint32Array(TCF.buffer), TCV = new T.Vector2(), TCC = new T.Color();
/* dấu tay của một hình: khối nào có ảnh dán hay shader riêng thì không cất (trả null) */
function tcKey(ri, sc, cm){ let a = 2166136261, b = 5381, n = 0, bad = false;
  const u1 = u => { a = Math.imul(a ^ u, 16777619); b = (Math.imul(b, 33) + u) | 0; }, f = v => { TCF[0] = v; u1(TCU[0]); }, st = x => { x = '' + x; for (let i = 0; i < x.length; i++) u1(x.charCodeAt(i)); };
  const at = t => { if (!t) return; const r = t.array; if (!r || t.isInterleavedBufferAttribute){ bad = true; return; } u1(r.length); if (r instanceof Float32Array){ const u = new Uint32Array(r.buffer, r.byteOffset, r.length); for (let i = 0; i < u.length; i++) u1(u[i]); } else for (let i = 0; i < r.length; i++) u1(r[i]); };
  const mt = m => { if (!m) return; if (m.map || m.alphaMap || m.emissiveMap || m.isShaderMaterial || m.gradientMap && m.gradientMap !== TOONG){ bad = true; return; } st(m.type); f(m.color ? m.color.getHex() : -1); f(m.emissive ? m.emissive.getHex() : -1); f(m.emissiveIntensity || 0); f(m.opacity); f(m.side); f(m.blending); f(m.alphaTest || 0); f((m.transparent ? 1 : 0) + (m.vertexColors ? 2 : 0) + (m.depthWrite ? 4 : 0) + (m.depthTest ? 8 : 0) + (m.visible ? 16 : 0) + (m.flatShading ? 32 : 0) + (m.wireframe ? 64 : 0)); };
  sc.updateMatrixWorld(true); cm.updateMatrixWorld(true); const z = ri.getSize(TCV); ri.getClearColor(TCC);
  for (const v of [z.x, z.y, ri.getPixelRatio(), ri.getClearAlpha(), TCC.getHex(), ri.toneMapping, ri.toneMappingExposure, ri.shadowMap.enabled ? 1 : 0]) f(v);
  for (const e of cm.matrixWorld.elements) f(e); for (const e of cm.projectionMatrix.elements) f(e);
  if (sc.background){ if (sc.background.isColor) f(sc.background.getHex()); else bad = true; } if (sc.fog) bad = true;
  sc.traverseVisible(o => { if (bad) return;
    if (o.isLight){ st(o.type); f(o.color.getHex()); f(o.intensity); if (o.groundColor) f(o.groundColor.getHex()); for (const e of o.matrixWorld.elements) f(e); if (o.target){ o.target.updateMatrixWorld(); for (const e of o.target.matrixWorld.elements) f(e); } if (o.castShadow) f(7); return; }
    const g = o.geometry; if (!g && !o.isSprite) return; n++; st(o.type); f(o.renderOrder); for (const e of o.matrixWorld.elements) f(e);
    if (o.isSkinnedMesh || o.morphTargetInfluences && o.morphTargetInfluences.length){ bad = true; return; }
    if (g){ at(g.attributes.position); at(g.attributes.normal); at(g.attributes.color); if (g.index) at(g.index); f(g.drawRange.start); f(g.drawRange.count === Infinity ? -1 : g.drawRange.count); }
    if (o.isInstancedMesh){ f(o.count); at(o.instanceMatrix); at(o.instanceColor); }
    if (Array.isArray(o.material)) o.material.forEach(mt); else mt(o.material); });
  return bad || !n ? null : (a >>> 0).toString(36) + '.' + (b >>> 0).toString(36) + '.' + n; }
const toonLost = r => {""")
rep("function toonRender(ri, sc, cm){ const prev = TOONLAST; let r2 = ri, ok = false, drew = false;",
    "function toonRender(ri, sc, cm){ let key = null; try { key = tcKey(ri, sc, cm); } catch (e) {} if (key && TC.m[key]){ TOONLAST = TC.use[key] = TC.m[key]; TC.hit++; return; }\n  const prev = TOONLAST; let r2 = ri, ok = false, drew = false;")
rep("  if (!ok) TOONLAST = TOONBLANK; }\nfunction toonRender0(",
    "  if (!ok) TOONLAST = TOONBLANK; else if (key){ TC.use[key] = TOONLAST; TC.miss++; tcSave(); } else TC.skip++; }\nfunction toonRender0(")
# 4) sổ hái ké trong ngày (cất trong máy, khoá 'mv2-vd'): nhớ hôm nay đã hái ké mấy món ở vườn nào, còn mấy công chưa dùng.
#    Trước đây mỗi lần ghé lại là đếm lại từ 3 nên không biết còn hái được không. Số của máy chủ không đổi (3 món mỗi vườn mỗi ngày).
rep("function mauLeft(){",
    """function vdGet(){ let o = null; try { o = JSON.parse(localStorage.getItem('mv2-vd') || 'null'); } catch (e) {} const d = dayKey(); if (!o || o.d !== d || !o.by) o = { d, by: {} }; return o; }
function vdOf(code, o){ return Object.assign({ s: 0, c: 0 }, (o || vdGet()).by[code]); }
function vdPut(code, v){ const o = vdGet(); o.by[code] = Object.assign(vdOf(code, o), v); try { localStorage.setItem('mv2-vd', JSON.stringify(o)); } catch (e) {} }
function vdSync(){ if (!VISIT) return; if (VISIT.kind === 'ban') vdPut(VISIT.code, { s: Math.max(0, DOICONG - VISIT.left), c: VISIT.cong || 0 }); else vdPut('mau', { s: Math.max(0, MAU.picks - VISIT.left) }); }
const hkTag = (code, o) => { const lf = Math.max(0, DOICONG - vdOf(code, o).s); return `<span class="nbk">${UX.pips(ICON.gio || ICON.cai, lf, DOICONG)}<i>${lf ? `Còn hái ké ${lf} món` : 'Hôm nay hái ké đủ rồi'}</i></span>`; };
const myInvList = () => [...Object.entries(ST.inv).filter(([k, n]) => n > 0 && GD(k) && k !== 'rom').map(([k, n]) => ({ k, n })), ...Object.entries(ST.seeds).filter(([k, n]) => n > 0).map(([k, n]) => ({ k, n, seed: 1 }))];
const visitMe = () => VISIT ? { myLv: VISIT.myLv, myInv: VISIT.myInv || [], me: VISIT.me || { realTime: ST.realTime, ovr: ST.ovr, tm: ST.tm, clk0: ST.clk0 } } : { myLv: ST.lv || 1, myInv: myInvList(), me: { realTime: ST.realTime, ovr: ST.ovr, tm: ST.tm, clk0: ST.clk0 } };
/* đang ở vườn bạn mà qua thẳng vườn khác: món đã hái cất vô hàng chờ, về nhà cộng một lượt */
function visitBank(){ try { const q = JSON.parse(sessionStorage.getItem('mv2-lootq') || '[]'); q.push(VISIT.loot); sessionStorage.setItem('mv2-lootq', JSON.stringify(q)); } catch (e) {} }
function vquaHTML(){ const o = vdGet(), lv = VISIT.myLv || 1; let h = '';
  if (VISIT.kind !== 'mau'){ const left = Math.max(0, MAU.picks - vdOf('mau', o).s); h += `<div class="vcard"><img src="${ICON.xoai || ICON.cai}" alt=""><div><b>Vườn mẫu của Ngoại</b><span>${left ? `Hôm nay còn hái ${left} món` : 'Hôm nay hái đủ rồi'}</span>${UX.pips(ICON.cai, left, MAU.picks)}</div><button class="btn g" data-a="gomau">Chèo qua</button></div>`; }
  h += `<div class="sub">Hàng xóm</div>`;
  if (!CLOUD.cred) return h + `<div class="note">Chưa kết nối mạng được nên chưa qua vườn bạn bè được.</div>`;
  if (NB2.list == null){ setTimeout(() => nbLoad(), 0); return h + `<div class="meta">${NB2.err ? 'Chưa tải được danh sách hàng xóm.' : 'Đang tải hàng xóm…'}</div>`; }
  const L = NB2.list.filter(n => n.code !== VISIT.code); if (!L.length) return h + `<div class="note">Chưa có hàng xóm nào khác. Về vườn mình gửi link cho bạn bè nghe con.</div>`;
  return h + L.map(n => `<div class="vcard nb"><img src="${AVIMG.face[n.av] || AVIMG.face[0]}" alt="" class="nbav"><div><b>${esc(n.name || 'Hàng xóm')}</b><span>${esc(n.garden || '')} · cấp ${n.lv}</span>${lv >= NB2.lv ? hkTag(n.code, o) : ''}</div><div class="nbb"><button class="btn g" data-a="nbgo" data-k="${n.code}" ${lv < NB2.lv ? 'disabled' : ''}>Chèo qua</button></div></div>`).join(''); }
function mauLeft(){""")
rep("m.realTime = ST.realTime; m.ovr = ST.ovr; m.tm = ST.tm; m.clk0 = ST.clk0;",
    "{ const H = VISIT && VISIT.me || ST; m.realTime = H.realTime; m.ovr = H.ovr; m.tm = H.tm; m.clk0 = H.clk0; }")
rep("function visitGo(){ stepMark('visit1'); closeSheet(); save(); const v = { kind: 'mau', name: 'Vườn mẫu của Ngoại', myLv: ST.lv || 1, left: mauLeft(), state: mauState(), loot: { inv: {}, xp: 0, water: 0 } };",
    "function visitGo(){ const hop = !!VISIT; closeSheet(); if (hop) visitBank(); else { stepMark('visit1'); save(); vdPut('mau', { s: MAU.picks - mauLeft() }); } const v = { kind: 'mau', name: 'Vườn mẫu của Ngoại', ...visitMe(), left: hop ? Math.max(0, MAU.picks - vdOf('mau').s) : mauLeft(), state: mauState(), loot: { inv: {}, xp: 0, water: 0 } };")
rep("function visitPersist(){ try { sessionStorage.setItem('mv2-visit', JSON.stringify(VISIT)); } catch (e) {} }",
    "function visitPersist(){ try { sessionStorage.setItem('mv2-visit', JSON.stringify(VISIT)); } catch (e) {} try { vdSync(); } catch (e) {} }")
# thanh trên đầu lúc thăm vườn: thêm nút qua thẳng vườn khác
rep("${fr ? '<button class=\"btn\" id=\"vMore\">Quà · mật thư</button>' : ''}<button class=\"btn g\" id=\"vHome\">Về vườn mình</button>`;",
    "${fr ? '<button class=\"btn\" id=\"vMore\">Quà · mật thư</button>' : ''}${hopOk ? '<button class=\"btn\" id=\"vHop\">Vườn khác</button>' : ''}<button class=\"btn g\" id=\"vHome\">${fr && hopOk ? 'Về nhà' : 'Về vườn mình'}</button>`;")
rep("function visitStart(){ document.body.classList.add('visit'); const fr = VISIT.kind === 'ban';", "function visitStart(){ document.body.classList.add('visit'); const fr = VISIT.kind === 'ban', hopOk = (VISIT.myLv || 1) >= NB2.lv && !!CLOUD.cred;")
# điện thoại: ba nút nằm một hàng; mở bảng thì thanh trên đầu tạm ẩn để khỏi đè lên tựa bảng
rep("body.visit .vbar{flex-wrap:wrap} body.visit .vbar>div{flex:1 1 100%} }", "body.visit .vbar{flex-wrap:wrap;gap:8px} body.visit .vbar>div{flex:1 1 100%} body.visit .vbar .btn{flex:1 1 auto;padding-left:8px;padding-right:8px} body.visit.sheeton .vbar{visibility:hidden} }")
rep("$('#vHome').addEventListener('click', visitHome);", "$('#vHome').addEventListener('click', visitHome); { const vh = $('#vHop'); if (vh) vh.addEventListener('click', () => openSheet('vqua')); }")
rep("function visitMode(){ if (VISIT.repay) return 've'; if ((VISIT.cong || 0) > 0 && VISIT.left > 0) return 've';",
    "function visitMode(){ if (VISIT.repay) return 've'; if (VISIT.left <= 0) return 'het'; if ((VISIT.cong || 0) > 0) return 've';")
rep(": m === 'phu' ? `Hái giùm ${VISIT.owner}` : 'Hôm nay phụ đủ rồi'; }",
    ": m === 'het' ? 'Hôm nay hái ké đủ rồi' : m === 'phu' ? `Hái giùm ${VISIT.owner}` : 'Hôm nay phụ đủ rồi'; }")
rep(": 'Mai qua phụ tiếp nghe con'; const col", ": m === 'het' ? 'Mai qua hái ké tiếp nghe con' : 'Mai qua phụ tiếp nghe con'; const col")
rep("if (fr && !repay && !(VISIT.cong > 0)){", "if (fr && !repay && !(VISIT.cong > 0 && VISIT.left > 0)){")
rep("floatAt(v.cx, .6, v.cz, `Rau về kho ${VISIT.owner} · được hái ké 1 món`, '#9fd36a');", "floatAt(v.cx, .6, v.cz, `Rau về kho ${VISIT.owner} · ${VISIT.left > 0 ? 'được hái ké 1 món' : '+2 kinh nghiệm'}`, '#9fd36a');")
rep("sayOnce('haigium', `Xong công rồi.", "if (VISIT.left > 0) sayOnce('haigium', `Xong công rồi.")
rep("fr ? 'Tưới giùm · được hái ké 1 món' : 'Tưới giùm · +2 kinh nghiệm'", "fr && VISIT.left > 0 ? 'Tưới giùm · được hái ké 1 món' : 'Tưới giùm · +2 kinh nghiệm'")
rep("else { VISIT.left = 0; visitInfo(); } return toast('Hôm nay hái đủ rồi con.'", "else { VISIT.left = 0; visitPersist(); visitInfo(); } return toast('Hôm nay hái đủ rồi con.'")
# về nhà: cộng hết các vườn đã ghé trong chuyến
rep("function visitBack(){ let L = null; try { L = JSON.parse(sessionStorage.getItem('mv2-loot') || 'null'); sessionStorage.removeItem('mv2-loot'); sessionStorage.removeItem('mv2-back'); } catch (e) {} if (!L) return;",
    "function visitBack(){ let L = null; try { const q = JSON.parse(sessionStorage.getItem('mv2-lootq') || '[]'), l = JSON.parse(sessionStorage.getItem('mv2-loot') || 'null'); if (l) q.push(l); sessionStorage.removeItem('mv2-lootq'); sessionStorage.removeItem('mv2-loot'); sessionStorage.removeItem('mv2-back');\n    if (q.length){ L = { inv: {}, xp: 0, giftOut: [], picks: 0, hop: 0, friend: q.every(x => x.friend) ? q[q.length - 1].friend : '' }; for (const x of q){ for (const [k, n] of Object.entries(x.inv || {})) L.inv[k] = (L.inv[k] || 0) + n; L.xp += x.xp || 0; L.giftOut.push(...(x.giftOut || [])); if (!x.friend) L.picks += x.picks || 0; L.hop += x.hop || 0; } } } catch (e) {} if (!L) return;")
rep("  save(); hud(); const from = L.friend ?", "  if (L.hop) ST.visitOut = (ST.visitOut || 0) + L.hop; save(); hud(); const from = L.friend ?")
rep("    const myInv = [...Object.entries(ST.inv).filter(([k, n]) => n > 0 && GD(k) && k !== 'rom').map(([k, n]) => ({ k, n })), ...Object.entries(ST.seeds).filter(([k, n]) => n > 0).map(([k, n]) => ({ k, n, seed: 1 }))];", "    const hop = !!VISIT, D = vdOf(code);")
rep("myLv: ST.lv || 1, left: DOICONG, repay: !!repay, myInv, state: st,", "...visitMe(), left: Math.max(0, DOICONG - D.s), cong: D.c, repay: !!repay, state: st,")
rep("    ST.visitOut = (ST.visitOut || 0) + 1; save(); sessionStorage.setItem('mv2-visit', JSON.stringify(v));", "    if (hop){ v.loot.hop = 1; visitBank(); } else { ST.visitOut = (ST.visitOut || 0) + 1; save(); } sessionStorage.setItem('mv2-visit', JSON.stringify(v));")
# danh sách hàng xóm ở nhà: mỗi vườn có dấu hiệu còn hái ké mấy món
rep("</span>${tag}</div><div class=\"nbb\">${btns}</div></div>`; }).join('') + nbSugHTML(); }", "</span>${tag}${lv >= NB2.lv ? hkTag(n.code, VD) : ''}</div><div class=\"nbb\">${btns}</div></div>`; }).join('') + nbSugHTML(); }")
rep("  return h + NB2.list.map(n => { const ask = NB2.ask[n.code],", "  const VD = vdGet(); return h + NB2.list.map(n => { const ask = NB2.ask[n.code],")
rep("const openSheet = (kind, arg) => { if (VISIT && kind !== 'visit' && kind !== 'bug') return;", "const openSheet = (kind, arg) => { if (VISIT && kind !== 'visit' && kind !== 'bug' && kind !== 'vqua') return;")
rep("if (kind === 'ben' || kind === 'vuon') setTimeout(() => nbLoad(), 0); SHEET = { kind, arg };", "if (kind === 'ben' || kind === 'vuon' || kind === 'vqua') setTimeout(() => nbLoad(), 0); SHEET = { kind, arg };")
rep("if (SHEET && (SHEET.kind === 'ben' || SHEET.kind === 'vuon')) renderSheet(); vuonBadge(); } }", "if (SHEET && (SHEET.kind === 'ben' || SHEET.kind === 'vuon' || SHEET.kind === 'vqua')) renderSheet(); vuonBadge(); } }")
rep("  if (kind === 'visit'){ shT.textContent = SHEET.nc ?", "  if (kind === 'vqua'){ shT.textContent = 'Qua vườn khác'; h += vquaHTML(); }\n  if (kind === 'visit'){ shT.textContent = SHEET.nc ?")
rep(".nbb{display:flex;flex-direction:column;gap:8px;align-items:flex-end}", ".nbk{display:flex!important;align-items:center;gap:8px;margin-top:4px}.nbk .pips{display:inline-flex!important;margin:0;flex:none}.nbk i{font-style:normal;font-size:13px}.nbb{display:flex;flex-direction:column;gap:8px;align-items:flex-end}")
# ô nhập mã vườn bạn cao 37, chưa đủ 44 (bài kiểm cũ không tới được màn này vì cần có mã vườn)
rep(".rin{font:600 15px ui-monospace,monospace;text-transform:uppercase;padding:8px 12px;", ".rin{font:600 15px ui-monospace,monospace;text-transform:uppercase;padding:8px 12px;min-height:44px;box-sizing:border-box;")

# ===== đợt 3 (17/11): giỏ ở vườn Ngoại, đài chuyện ma, chợ tự cập nhật =====
# vườn Ngoại cũng đếm bằng hình giỏ như hàng xóm
rep("UX.pips(ICON.cai, left, MAU.picks)", "UX.pips(ICON.gio || ICON.cai, left, MAU.picks)", 3)
# đài: thêm đài Chuyện ma (3 tệp trong hd/nhac, phát lần lượt), đài Nhạc giựt phát bài anh Ares gửi
rep('const RADIO = {"dir": "nhac/", "dai": {"giut": {"name": "Nhạc giựt", "files": []}, "cailuong": {"name": "Cải lương", "files": []}, "chieu": {"name": "Chiều vườn", "files": []}}, "tin": []};',
    'const RADIO = {"dir": "nhac/", "dai": {"giut": {"name": "Nhạc giựt", "files": ["giut_01_dam_cuoi_miet_vuon.m4a"]}, "cailuong": {"name": "Cải lương", "files": []}, "chieu": {"name": "Chiều vườn", "files": []}, "ma": {"name": "Chuyện ma", "seq": 1, "files": ["ma_04_khap_nuoc_can.m4a", "ma_15_chuyen_do_cuoi.m4a", "ma_18_con_cho_sua.m4a"], "ten": ["Khạp nước cạn", "Chuyến đò cuối", "Con chó sủa vào vườn trống"]}}, "tin": []};\nconst radHas = k => RADIO.dai[k].files.length;')
rep("const radOn = () => Object.keys(RADIO.dai).some(k => RADIO.dai[k].files.length),", "const radOn = () => Object.keys(RADIO.dai).some(radHas),")
rep("const D = RADIO.dai[RAD.st]; if (!D || !D.files.length) return radStop(); RAD.n++;", "const D = RADIO.dai[RAD.st]; if (!D || !D.files.length) return radStop(); RAD.n++;")
rep(": RAD.q.shift(); RAD.el.src = RADIO.dir + f;", ": D.seq ? D.files[RAD.mi = (RAD.mi == null ? (ST.radMa || 0) : RAD.mi + 1) % D.files.length] : RAD.q.shift(); if (D.seq && !tin){ ST.radMa = RAD.mi; save(); } RAD.el.src = RADIO.dir + f;")
rep("RAD.el.onplaying = () => { RAD.fail = 0; }; }", "RAD.el.onplaying = () => { RAD.fail = 0; try { if (SHEET && SHEET.kind === 'radio') renderSheet(); } catch (e) {} }; }")
rep("RAD.on = true; RAD.st = k; RAD.q = []; RAD.n = 0; ST.radSt = k;", "RAD.on = true; RAD.st = k; RAD.q = []; RAD.n = 0; RAD.mi = null; ST.radSt = k;")
rep("keys = Object.keys(RADIO.dai).filter(k => RADIO.dai[k].files.length), cur = RAD.st || ST.radSt || keys[0];", "keys = Object.keys(RADIO.dai).filter(radHas), cur = keys.includes(RAD.st || ST.radSt) ? (RAD.st || ST.radSt) : keys[0], MA = RADIO.dai.ma, mi = RAD.mi == null ? (ST.radMa || 0) % MA.files.length : RAD.mi;")
rep("on ? `Đang phát ${RADIO.dai[RAD.st].name.toLowerCase()}` : 'Đang tắt');", "on ? (RAD.st === 'ma' ? `Đang kể chuyện ${MA.ten[mi]}` : `Đang phát ${RADIO.dai[RAD.st].name.toLowerCase()}`) : 'Đang tắt');")
rep("if (RADIO.tin.length) h += `<div class=\"acts\"><button class=\"btn\" data-a=\"radtin\">", "if (cur === 'ma') h += `<div class=\"sub\">Chọn chuyện</div><div class=\"acts\">${MA.ten.map((n, i) => `<button class=\"btn${i === mi ? ' g' : ''}\" data-a=\"radma\" data-i=\"${i}\">${n}</button>`).join('')}</div>`; if (RADIO.tin.length) h += `<div class=\"acts\"><button class=\"btn\" data-a=\"radtin\">")
rep("else if (a === 'radde'){", "else if (a === 'radma'){ ST.radMa = +b.dataset.i || 0; radStart('ma'); renderSheet(); return; } else if (a === 'radde'){")
rep("function VOL(){ return Object.assign", open('v160x.js', encoding='utf-8').read() + "function VOL(){ return Object.assign")
# chợ: tải lại danh sách xuồng bà con trong lúc đang ở chợ
rep("CNX.rlD = c.d; if (!(CHM.on && CHM.kind === 'cn')) CNX.bcL = null; }", "CNX.rlD = c.d; if (!(CHM.on && CHM.kind === 'cn')) CNX.bcL = null; else cnbFresh(); }")
rep("CNX.bcL = null; CHM.B = cnoBuild(); CHM.on = true;", "CNX.bcL = null; CHM.B = cnoBuild(); CNX.scSg = cnbSg(); CNX.bcP = 0; CNX.pollAt = Date.now(); CHM.on = true;")

# ===== đợt 4: sổ hái ké lấy số thật từ máy chủ (hàm mv2_stolen), đổi máy vẫn đếm đúng =====
rep("catch (e) { NB2.sug = NB2.sug || []; } } catch (e) { NB2.err = String(e.message || e); }",
    "catch (e) { NB2.sug = NB2.sug || []; } try { const S = await rpc('mv2_stolen', { p_code: CLOUD.cred.code, p_secret: CLOUD.cred.secret }); if (S && typeof S === 'object') for (const k in S){ const n = Math.min(DOICONG, S[k] | 0); if (n > vdOf(k).s) vdPut(k, { s: n }); } } catch (e) {} } catch (e) { NB2.err = String(e.message || e); }")
# ===== đợt 5 (18/11): mở nhiều tab là đứng; rãnh cỏ ở liếp cây; bỏ giới hạn 10 món mua ở bến =====
# 5a) tab đang ẩn thì khoan dựng vườn, chờ người chơi quay lại tab mới dựng tiếp
rep("if (performance.now() - LDT < 50) return; return new Promise(r => { let d = 0;",
    "if (document.hidden) return new Promise(r => { const f = () => { if (!document.hidden){ document.removeEventListener('visibilitychange', f); LDT = performance.now(); r(); } }; document.addEventListener('visibilitychange', f); }); if (performance.now() - LDT < 50) return; return new Promise(r => { let d = 0;")
# 5b) bộ vẽ icon: chỉ một khung WebGL phụ cho cả game, không tự huỷ rồi dựng lại (WebKit chỉ cho 16 khung, lố là rút khung của vườn)
rep("if (!R || R.getContext().isContextLost()){ R = ICR.r = new T.WebGLRenderer(", "if (!R || R.getContext().isContextLost()){ window.__icNew = (window.__icNew || 0) + 1; R = ICR.r = new T.WebGLRenderer(")
rep("let R = ICR.r; if (!R || R === ri || toonLost(R)) R = ICR.r = new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true }); const z = ri.getSize(",
    "let R = ICR.r; if (!R || R === ri || toonLost(R)){ if ((ICR.n = (ICR.n || 0) + 1) > 6) throw new Error('ic: het luot dung khung ve'); window.__icNew = (window.__icNew || 0) + 1; R = ICR.r = new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true }); } const z = ri.getSize(")
rep("function toonFresh(ri){ const old = ICR.r; ICR.r = null; if (old){ try { old.dispose(); old.forceContextLoss(); } catch (e) {} } if (ri !== old && !toonLost(ri)){ try { ri.forceContextLoss(); } catch (e) {} } return toonLive(ri); }",
    "function toonFresh(ri){ const R = toonLive(ri); try { R.setRenderTarget(null); R.resetState(); R.clear(); } catch (e) {} return R; }")
rep("const ri = aoIc.ri || (aoIc.ri = new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true })); ri.setPixelRatio(1);", "const ri = ICR(); ri.setPixelRatio(1);")
rep("ICON.ghe = window.__gheIc(ri); ICR.free(); }", "ICON.ghe = window.__gheIc(ri); }")
# 5b2) vẽ xong mỗi icon thì trả bộ nhớ hình khối cho máy (trước dồn hơn 5000 khối trong khung phụ, WebKit rút khung)
rep("ri.render(sc, cm); TOONLAST = ri.domElement.toDataURL('image/png'); return; }", "toonDraw(ri, sc, cm); TOONLAST = ri.domElement.toDataURL('image/png'); return; }")
# 5b3) cảnh icon lớn (có cảnh hơn 3000 khối) thì vẽ từng mớ 500 khối rồi trả bộ nhớ liền: khung phụ không bao giờ giữ quá vài ngàn vùng nhớ (WebKit sập bộ vẽ khi một khung giữ hơn ~12 ngàn)
rep("function toonRender0(ri, sc, cm){", """function toonDraw(ri, sc, cm){ const ms = [], gs = new Set(); sc.traverse(o => { if (o.geometry){ gs.add(o.geometry); if (o.visible) ms.push(o); } });
  const fin = () => { try { for (const g of gs) g.dispose(); } catch (e) {} };
  if (gs.size <= 700 || ri.shadowMap.enabled){ ri.render(sc, cm); fin(); return; }
  const tr = o => { const m = Array.isArray(o.material) ? o.material[0] : o.material; return m && m.transparent ? 1 : 0; }; ms.sort((a, b) => tr(a) - tr(b));
  const mk = ms.map(o => o.layers.mask), ac = ri.autoClear, last = new Map(); ms.forEach((o, i) => last.set(o.geometry, i)); window.__icChunk = (window.__icChunk || 0) + 1;
  try { for (const o of ms) o.layers.set(31); ri.autoClear = false; ri.clear();
    for (let i = 0; i < ms.length; ){ const seen = new Set(); let j = i; while (j < ms.length && (seen.size < 500 || seen.has(ms[j].geometry))){ seen.add(ms[j].geometry); j++; }
      for (let k = i; k < j; k++) ms[k].layers.mask = mk[k]; ri.render(sc, cm); for (let k = i; k < j; k++) ms[k].layers.set(31);
      for (const g of seen) if (last.get(g) < j) g.dispose(); i = j; } }
  finally { ms.forEach((o, i) => o.layers.mask = mk[i]); ri.autoClear = ac; fin(); } }
function toonRender0(ri, sc, cm){""")
# 5c) cây trồng trên hai ô: lấp đất chỗ hở giữa hai ô và chỗ hở với cây kế bên (trước lòi cỏ)
rep("function refreshPlot(id){ SHDIRTY = 1;", """function pairFill(id){ const v = PV[id]; if (!v) return; if (!(ST.pairs && ST.pairs[id] && PL[ST.pairs[id]]) || !v.root.visible){ if (v.fill) v.fill.visible = false; return; }
  const u = unionB(id); let x0 = u[0] + .04, x1 = u[2] - .04;
  for (const h in ST.pairs){ if (h === id || !PL[h] || !PL[ST.pairs[h]] || !PV[h] || !PV[h].root.visible) continue; const q = unionB(h); if (Math.abs(q[1] - u[1]) > .05 || Math.abs(q[3] - u[3]) > .05) continue; const dR = q[0] - u[2], dL = u[0] - q[2]; if (dR > 0 && dR < .3) x1 = u[2] + dR / 2 + .002; if (dL > 0 && dL < .3) x0 = u[0] - dL / 2 - .002; }
  if (!v.fill){ v.fill = new T.Mesh(new T.BoxGeometry(1, .03, 1), new T.MeshStandardMaterial({ color: '#7E5434', flatShading: true, roughness: 1 })); v.fill.receiveShadow = true; v.fill.userData.keep = true; v.root.add(v.fill); }
  v.fill.scale.set(x1 - x0, 1, u[3] - u[1] - .08); v.fill.position.set((x0 + x1) / 2, -.004, (u[1] + u[3]) / 2); v.fill.visible = true; }
function pairFillAll(){ try { for (const h in (ST.pairs || {})) pairFill(h); for (const k in PV) if (PV[k] && PV[k].fill && !(ST.pairs && ST.pairs[k])) PV[k].fill.visible = false; } catch (e) {} }
function refreshPlot(id){ SHDIRTY = 1;""")
rep("    if (!on || nh) v.want = null; else if (lk && !guest){", "    if (host || v.fill) pairFillAll();\n    if (!on || nh) v.want = null; else if (lk && !guest){")
# 5d) bến bà con: mua thoải mái, hết giới hạn 10 món một ngày (xuồng con bày bán vẫn 10 món)
rep("n = Math.min(n, cnbLeft(bt, it), CNB.cap - b.buy); if (n <= 0) return toast(b.buy >= CNB.cap ? cnL('Hôm nay con mua đủ 10 món ở bến rồi, mai ghé nữa nghe.', 'You have bought your 10 items at the pier today. Come back tomorrow.') : cnL('Xuồng này hết món đó rồi con.', 'This boat is out of that.'), 'dan');",
    "n = Math.min(n, cnbLeft(bt, it), 10); if (n <= 0) return toast(cnL('Xuồng này hết món đó rồi con.', 'This boat is out of that.'), 'dan');")
rep("if (w === 'cap') b.buy = CNB.cap; else it.q = 0; save(); renderSheet(); return toast(w === 'cap' ? cnL('Hôm nay con mua đủ 10 món ở bến rồi, mai ghé nữa nghe.', 'You have bought your 10 items at the pier today. Come back tomorrow.') :",
    "if (w !== 'cap') it.q = 0; save(); renderSheet(); return toast(w === 'cap' ? cnL('Bến đang đông quá, lát con ghé lại nghe.', 'The pier is busy. Try again in a bit.') :")
rep("const left = CNB.cap - b.buy;", "")
rep("n = Math.min(l, left), nd = N[it.k] || 0;", "n = Math.min(l, 10), nd = N[it.k] || 0;")
rep(": l ? cnL('Đủ 10 món', 'Limit reached') : cnL('Hết', 'Out')}", ": cnL('Hết', 'Out')}")
rep("h += `<div class=\"meta\">${left ? cnL(`Hôm nay con còn mua được ${left} món ở bến.`, `You can still buy ${left} items at the pier today.`) : cnL('Hôm nay con mua đủ 10 món ở bến rồi.', 'You have bought your 10 items at the pier today.')}</div>` + UX.cta(", "h += UX.cta(")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
