# hide115: mật thư giấu thật: không ghim, Ngoại "có nhắn lại" câu gợi ý, chạm đúng túm lá mới ra thư; Sổ có Ngoại chỉ giùm, quá 1 ngày ghim tự hiện. python3 hide115.py vào ra
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
# câu gợi ý: có quà dùng câu anh Ares viết, không quà dùng câu không nhắc tới quà
rep("  tabs: { spot: 'Gợi ý chỗ giấu', qua: 'Lời gửi quà', khia: 'Cà khịa', cadao: 'Ca dao', do: 'Câu đố' },",
"""  tabs: { qua: 'Lời gửi quà', khia: 'Cà khịa', cadao: 'Ca dao', do: 'Câu đố' },
  hints: { chuoi: ['Tàu lá đong đưa, có chuyện này kẹp trong đó.', 'Thư tui núp chỗ trái còn xanh, lá thì to.', 'Chỗ nào có buồng có nải, thư nằm đó.'], da: ['Nước trôi đá đứng, thư nằm kế bên.', 'Ra mé sông coi thử, có cục đá giữ giùm tui chuyện bí mật.', 'Men theo mé nước, gặp hòn đá bự thì dòm quanh.'], khap: ['Thư tui hổng ướt đâu, nằm sát bên khạp thôi.', 'Khát nước thì ra múc, tiện tay kiếm thư luôn.', 'Chỗ trữ nước mưa, dòm kế bên coi.'], rom: ['Tìm chỗ gà hay bươi, mà bươi nhẹ tay thôi.', 'Rơm vàng một đống, thư nhỏ một lá.', 'Thư núp trong rơm, bươi nhẹ tay nghen.'] },""")
rep("const noteSp = k =>","const noteHint = n => { const L = n.gk ? NOTE.texts.filter(x => x.g === n.spot).map(x => x.s) : (NOTE.hints[n.spot] || []), x = L.length ? L[Math.abs(+n.id || 0) % L.length] : ''; return EN && typeof enT === 'function' ? enT(x) : x; }, NOTE_DAY = 86400000, noteShown = n => !!n.show || !n.at || Date.now() - n.at > NOTE_DAY;\nconst noteSp = k =>")
# bảng chọn câu: bỏ nhóm gợi ý chỗ giấu
rep("tabs = g ? ['spot', 'qua', 'khia', 'cadao', 'do'] : ['khia', 'cadao', 'do']","tabs = g ? ['qua', 'khia', 'cadao', 'do'] : ['khia', 'cadao', 'do']")
rep("""  if (!g && V.myInv.length) h += `<div class="nhint">Kẹp quà thì có thêm câu gợi ý chỗ giấu.</div>`;\n""","")
# túm lá chạm được, ghim chỉ hiện khi Ngoại chỉ giùm hay quá 1 ngày
rep("const w = G(.2, .12, .22, .5, root);","const w = G(.2, .12, .22, .5, root), pick0 = new T.Mesh(new T.BoxGeometry(.7, .6, .7), new T.MeshBasicMaterial({ visible: false })); pick0.position.set(.2, .25, .22); root.add(pick0);")
rep("out[k] = { root, w, b, hit: b.children.find(c => c.userData.bub) };","out[k] = { root, w, b, pick0, hit: b.children.find(c => c.userData.bub) };")
rep("v.root.visible = !!n; v.b.visible = !!n; if (!n) continue; try { bubIcon(v.b, ICON.thu); } catch (e) {} v.hit.userData.note = n.id;","const pin = !!n && noteShown(n); v.root.visible = !!n; v.b.visible = pin; if (!n) continue; v.pick0.userData.note = n.id; if (pin){ try { bubIcon(v.b, ICON.thu); } catch (e) {} v.hit.userData.note = n.id; }")
rep("const hs = Object.values(NOTEV).filter(v => v.b.visible).map(v => v.hit); if (!hs.length) return false;","const hs = []; for (const v of Object.values(NOTEV)) if (v.root.visible){ hs.push(v.pick0); if (v.b.visible) hs.push(v.hit); } if (!hs.length) return false;")
rep("sfx('pick'); openSheet('thu', h.object.userData.note); return true; }","noteFound(h.object.userData.note); return true; }")
rep("function noteOpen(id){","function noteFound(id){ const n = (ST.notes || []).find(x => x.id === id), D = n && NOTE.spots[n.spot]; if (D){ for (let i = 0; i < 14; i++) puff('leaf', D.at[0] + .2 + R(-.25, .25), .3, D.at[1] + .22 + R(-.25, .25), 1, pick(['#6E9F57', '#8fb85a', '#F5D27A']), .8); sfx('pop'); buzz(15); } openSheet('thu', id); }\nfunction noteOpen(id){")
# hộp thư: ghi giờ, Ngoại nhắn lại câu gợi ý
rep("gs: pl.gs ? 1 : 0 }); b.note = pl.spot; }","gs: pl.gs ? 1 : 0, at: Date.now() }); b.note = ST.notes[ST.notes.length - 1]; }")
rep("if (b.note && NOTE.spots[b.note]) bits.push(`giấu lá thư ở ${noteSp(b.note)}`);","")
rep("const t = bits.length ? `Hồi nãy ${b.name} ghé, ${bits.join(', ')","let t = bits.length ? `Hồi nãy ${b.name} ghé, ${bits.join(', ')")
rep("TS.push([t, b.steal.length > b.water + b.help.length ? 'lo' : 'vui']); }","if (b.note && NOTE.spots[b.note.spot]) t = bits.length ? `${t} ${b.name} có nhắn lại: ${noteHint(b.note)}` : `Hồi nãy ${b.name} ghé, có nhắn lại: ${noteHint(b.note)}`; TS.push([t, b.steal.length > b.water + b.help.length ? 'lo' : 'vui']); }")
rep("if (TS.length === 1) say(TS[0][0], TS[0][1], { idle: true });","if (TS.length > 1) for (const b of Object.values(by)) if (b.note && NOTE.spots[b.note.spot]) setTimeout(() => say(`${b.name} có nhắn lại: ${noteHint(b.note)}`, 'vui', { idle: true }), 7000); if (TS.length === 1) say(TS[0][0], TS[0][1], { idle: true });")
rep("else if (a === 'gahatch'){ closeBook(); openSheet('ga'); return; }","else if (a === 'gahatch'){ closeBook(); openSheet('ga'); return; }   else if (a === 'thuchi'){ const L = (ST.notes || []).filter(n => !n.read); L.forEach(n => { n.show = 1; }); save(); closeBook(); const D = L[0] && NOTE.spots[L[0].spot]; if (D){ try { camTo(new T.Vector3(D.at[0], .3, D.at[1]), Math.max(cam.zoom, DEFZ() * 1.3)); } catch (e) {} say(`Thư nằm ở ${noteSp(L[0].spot)} đó con. Chạm vô mà lấy.`, 'vui', { now: true }); } return; }")
# Sổ: còn thư chưa tìm ra
rep("(un ? `<div class=\"bkhn\" style=\"font-size:13px;opacity:.8\">Còn ${un} lá đang giấu trong vườn, kiếm chỗ có lá rung nghe con.</div>` : '')",
    "(un ? `<div class=\"bkhn\" style=\"font-size:13px;opacity:.8\">Còn ${un} lá chưa tìm ra, kiếm chỗ có lá rung nghe con.</div>${all.filter(n => !n.read).map(n => `<div class=\"thh\"><b>${esc(n.name || 'Hàng xóm')} nhắn:</b> ${esc(noteHint(n))}</div>`).join('')}${all.some(n => !n.read && !noteShown(n)) ? '<button class=\"bkmv\" data-b=\"thuchi\">Ngoại chỉ giùm</button>' : ''}` : '')")
rep(".nhint{margin-top:6px;font:500 13px/1.3 var(--f-body);color:#8A5D3B}",".thh{margin:6px 0;font:400 17px/1.3 var(--f-hand);color:#4A2F1E}.thh b{font:600 13px/1.3 var(--f-body);color:#8A5D3B}")
rep("if (c.g >= 0 && !had && c.t < 0) c.tab = 'spot';","if (c.g >= 0 && !had && c.t < 0) c.tab = 'qua';")
rep("if (!g && (c.tab === 'spot' || c.tab === 'qua')) c.tab = 'khia';","if (!g && c.tab === 'qua') c.tab = 'khia';")
open(dst,'w',encoding='utf-8').write(s)
