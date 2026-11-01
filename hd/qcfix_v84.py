# QC v84: vá các lỗi đã tái hiện. Mỗi chỗ vá phải khớp đúng số lần mong đợi, không thì dừng.
import sys
P = sys.argv[1] if len(sys.argv) > 1 else 'live/vuon3d.html'
s = open(P, encoding='utf-8').read()
log = []

def rep(old, new, n=1, tag=''):
    global s
    c = s.count(old)
    if c != n:
        sys.exit(f'FAIL [{tag}] khớp {c} lần, cần {n}: {old[:80]!r}')
    s = s.replace(old, new)
    log.append(tag)

# 0. Đổi số bản
rep("const BUILD = 'v83'", "const BUILD = 'v84'", tag='build v84')

# 1. Cây cổ tích: dur tính bằng giây, Date.now() bằng mili-giây → lớn nhanh gấp 1000 lần
rep("Date.now() - F.t >= D.dur[F.st] / (ST.spd || 1)",
    "Date.now() - F.t >= D.dur[F.st] * 1000 / (ST.spd || 1)", tag='cổ tích lớn theo giờ thật')

# 2. Hạt giống quý mùa Tết (dưa hấu ruột vàng, cúc mâm xôi) làm vỡ Sổ giống
rep("n = ST.seeds[k] || 0, [ni, nl] = NEED[k];",
    "n = ST.seeds[k] || 0, [ni, nl] = NEED[k] || (c.kind === 'patch' ? ['drop', 'Ưa ẩm'] : ['sun', 'Ưa nắng']);", tag='NEED giống quý')
rep("${TIPS[k].map(x => '· ' + x).join('<br>')}",
    "${(TIPS[k] || ['Giống quý mùa Tết, chăm như rau thường là lên.', 'Chín tới thì lấp lánh, hái liền cho đẹp.']).map(x => '· ' + x).join('<br>')}", tag='TIPS giống quý')

# 3. Bảng liếp vẽ lại mỗi 0,4 s làm mục "Khác" tự đóng, mất cuộn
rep("if (SHEET && SHEET.kind === 'plot') renderSheet(); }",
    "if (SHEET && SHEET.kind === 'plot') sheetSoft(); }", tag='bảng liếp giữ trạng thái')
rep("function renderSheet(){",
    "function sheetSoft(){ if (shB.querySelector('.ing')) return; const op = [...shB.querySelectorAll('details')].map(d => d.open), sc = shB.scrollTop; renderSheet(); const ds = shB.querySelectorAll('details'); if (ds.length === op.length) ds.forEach((d, i) => { if (op[i]) d.open = true; }); shB.scrollTop = sc; }\nfunction renderSheet(){", tag='sheetSoft')

# 4. Bướm: chạm 2 lần ghi sổ 2 lần; bướm đã chạm không bay đi; rò geometry/material
rep("b.life -= dt; const p = b.m.position; if (b.rest > 0){",
    "b.life -= dt; const p = b.m.position; if (b.life <= 0){ } else if (b.rest > 0){", tag='bướm bay đi')
rep("if (p.y > 3){ BUV.root.remove(b.m); BUV.list.splice(BUV.list.indexOf(b), 1); }",
    "if (p.y > 3){ BUV.root.remove(b.m); b.m.traverse(o => { if (o.geometry) o.geometry.dispose(); }); for (const q of (b.m.userData.own || [])) q.dispose(); if (b.hit && b.hit.material) b.hit.material.dispose(); BUV.list.splice(BUV.list.indexOf(b), 1); }", tag='bướm dispose')
rep("for (const b of BUV.list){ if (ray.intersectObject(b.hit, false).length) return b; }",
    "for (const b of BUV.list){ if (b.caught || b.life <= 0) continue; if (ray.intersectObject(b.hit, false).length) return b; }", tag='bướm không chạm lại')
rep("function buCatch(b){ const first",
    "function buCatch(b){ if (!b || b.caught) return; b.caught = 1; const first", tag='bướm chặn bắt đôi')
rep("mb = new T.MeshStandardMaterial({ color: d.b, side: T.DoubleSide, flatShading: true, roughness: .7 });",
    "mb = new T.MeshStandardMaterial({ color: d.b, side: T.DoubleSide, flatShading: true, roughness: .7 }); g.userData.own = [ma, mb];", tag='bướm giữ material')

# 5. Tên vườn của người khác chèn thẳng vào innerHTML (XSS → đọc được mã bí mật)
rep("b.innerHTML = `<div><b>${VISIT.name}</b>",
    "b.innerHTML = `<div><b>${String(VISIT.name || '').replace(/[&<>\"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '\"': '&quot;' }[c]))}</b>", tag='esc tên vườn')

# 6. Việc "Quét lá" (cấp 2) không có câu thoại → say(undefined)
rep("lucbinh: 'Lục bình mọc nghẹt mương rồi. Vớt lên phơi khô, phủ liếp như rơm được đó con.' }[o.k], 'dan');",
    "lucbinh: 'Lục bình mọc nghẹt mương rồi. Vớt lên phơi khô, phủ liếp như rơm được đó con.', la: 'Lá khô rụng đầy sân kìa con. Quét gom lại, để dành ủ phân bón rau.' }[o.k], 'dan');", tag='câu quét lá')
rep("function say(txt, mood = 'vui', o = {}){ ",
    "function say(txt, mood = 'vui', o = {}){ if (!txt) return; ", tag='say chặn rỗng')

# 7. Bảng gà: "Trứng kế tiếp chừng 0 giây" khi mái đang ấp
rep("else h += UX.hero(ICON.mai, 'Gà đang đẻ', `Trứng kế tiếp chừng ${fmtT(next)}`",
    "else if (next == null) h += UX.hero(ICON.mai, 'Gà mái đang ấp', 'Ấp nở xong gà mái mới đẻ lại nghe con', '');\n  else h += UX.hero(ICON.mai, 'Gà đang đẻ', `Trứng kế tiếp chừng ${fmtT(next)}`", tag='gà đang ấp')

# 8. Mương đất mới không vẽ lại (LANDN tăng 3/frame nên %30===1 không bao giờ đúng)
rep("function muongTick(){ if ((LANDN % 30) !== 1 && MUV.key) return;",
    "function muongTick(){ MUV.n = (MUV.n || 0) + 1; if ((MUV.n % 30) !== 1 && MUV.key) return;", tag='mương vẽ lại')

# 9. Hoa rau muống không gắn vào cây (dồn về giữa liếp)
rep("if (fl) M(cone(.025, .04, 5), '#F2D7E8', R(-.04, .04), .3 * s, R(-.04, .04), { r: [Math.PI, 0, 0] }); }",
    "if (fl) M(cone(.025, .04, 5), '#F2D7E8', R(-.04, .04), .3 * s, R(-.04, .04), { r: [Math.PI, 0, 0], p: g }); }", tag='hoa rau muống')

# 10. Câu trúng lục bình bỏ vào kho rau thay vì gác bếp → kẹt kho
rep("if (junk === 'lucbinh') ST.inv.lucbinh = (ST.inv.lucbinh || 0) + 1;",
    "if (junk === 'lucbinh'){ const sl = STORE('lucbinh'); sl.lucbinh = (sl.lucbinh || 0) + 1; }", tag='lục bình lên gác bếp')

# 11. Một lỗi trong tick làm game đứng hình vĩnh viễn → bọc lại, vẫn báo lỗi ra console
tail = "  saveT += dt; if (saveT > 5){ saveT = 0; save(); }\n  requestAnimationFrame(tick); }\n{ const L0 = $('#load')"
rep(tail, "  saveT += dt; if (saveT > 5){ saveT = 0; save(); }\n}\nconst TERR = new Set();\nfunction tick(){ try { tickIn(); } catch (e) { const k = String(e && e.message); if (!TERR.has(k)){ TERR.add(k); setTimeout(() => { throw e; }, 0); } }\n  requestAnimationFrame(tick); }\n{ const L0 = $('#load')", tag='tick không đứng hình')
rep("function tick(){ const dt = Math.min(clock.getDelta(), .05)", "function tickIn(){ const dt = Math.min(clock.getDelta(), .05)", tag='tickIn')

# 12. Câu trong hàng chờ vẫn nói đè khi đang mở bảng; ép 4,5 s làm câu dài tắt sớm
#    (chỉ sửa trong tick; xem đoạn gốc trước khi vá)
rep("if (SAYQ.length){ const [a, b] = SAYQ.shift(); say(a, b, { now: true }); sayT = 4.5; } else ng.hidden = true; } }",
    "if (SAYQ.length && !busy()){ const [a, b] = SAYQ.shift(); say(a, b, { now: true }); } else { for (const q of SAYQ.splice(0)) if (!IDLEQ.some(x => x[0] === q[0])) IDLEQ.push(q); ng.hidden = true; } } }", tag='hàng chờ lời Ngoại')
# 13. Kiểm bản mới tải lại 1 MB mỗi lần quay lại app → tối đa 1 lần / 10 phút
rep("async function buildCheck(){ try { if (!/^https?:/.test(location.protocol)) return;",
    "let BCK = 0;\nasync function buildCheck(){ try { if (!/^https?:/.test(location.protocol)) return; if (Date.now() - BCK < 10 * 60000) return; BCK = Date.now();", tag='buildCheck thưa')

open(P, 'w', encoding='utf-8').write(s)
print('OK', len(log), 'chỗ vá:', ', '.join(log))
