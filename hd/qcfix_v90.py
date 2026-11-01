# QC v90: tiến trình cấp — chỉ hiện cái đang làm được ở cấp hiện tại (anh Ares chốt 1/11).
#  - Việc Ngoại dặn loại "góp xu" chỉ hiện khi đã đủ kinh nghiệm (trước đó không làm được).
#  - Việc loại "làm dần" (phát cỏ, đắp liếp, giao đơn…) vẫn hiện vì làm được ngay, nhưng không còn nhắc "lên cấp N", "làm trước được".
#  - Thẻ "Việc tiếp theo": khi chưa tới việc Ngoại nhờ thì gợi việc hôm nay còn dở (đó là cách kiếm kinh nghiệm), hết việc thì nhắc chăm vườn.
#  - Bỏ chữ tắt "kn", bỏ đồng xu làm biểu tượng việc, bỏ khối "Cấp N mở" (báo trước cấp sau), bỏ dòng "Việc hôm nay 5/5" khi đã xong hết.
import sys
P = sys.argv[1] if len(sys.argv) > 1 else 'live/vuon3d.html'
s = open(P, encoding='utf-8').read(); log = []
def rep(old, new, n=1, tag=''):
    global s
    c = s.count(old)
    if c != n: sys.exit(f'FAIL [{tag}] khớp {c} lần, cần {n}: {old[:90]!r}')
    s = s.replace(old, new); log.append(tag)

rep("const BUILD = 'v89'", "const BUILD = 'v90'", tag='build v90')

# --- Thẻ "Việc tiếp theo" ---
rep("let ic = UIC.task, t = '', em = '', f = 0, go = false, act = 'book';",
    "let ic = UIC.task, t = '', em = '', f = 0, go = false, act = 'book', lab = 'VIỆC TIẾP THEO', isTask = false;", tag='thẻ: biến nhãn')
rep("else if (q && q.t === 'weed'){ ic = UIC.sickle; t = q.txt; em = `${ST.weed || 0}/${q.need}`; f = (ST.weed || 0) / q.need; go = true; act = 'weed'; }",
    "else if (q && q.t === 'weed'){ ic = UIC.sickle; t = q.txt; em = `${ST.weed || 0}/${q.need}`; f = (ST.weed || 0) / q.need; go = true; act = 'weed'; lab = 'NGOẠI NHỜ'; }", tag='thẻ: phát cỏ')
rep("else if (q && q.t === 'goal'){ const g = q.goals.find(([, f2, nn]) => f2() < nn) || q.goals[0], v = Math.min(g[2], g[1]()); t = g[0]; em = `${v}/${g[2]}`; f = v / g[2]; go = ready; }",
    "else if (q && q.t === 'goal'){ const g = q.goals.find(([, f2, nn]) => f2() < nn) || q.goals[0], v = Math.min(g[2], g[1]()); t = g[0]; em = `${v}/${g[2]}`; f = v / g[2]; go = ready; lab = 'NGOẠI NHỜ'; }", tag='thẻ: việc làm dần')
rep("else if (q && q.t === 'pay'){ ic = UIC.coin; t = q.txt; if (!ready){ em = `còn ${need - xp} kn`; f = (xp - prev) / (need - prev); } else { em = `${Math.min(ST.xu, q.xu)}/${q.xu} xu`; f = Math.min(1, ST.xu / q.xu); go = ST.xu >= q.xu; } }",
    "else if (q && q.t === 'pay' && ready){ ic = ICON.cuoc || UIC.task; t = q.txt; em = `${Math.min(ST.xu, q.xu)}/${q.xu} xu`; f = Math.min(1, ST.xu / q.xu); go = ST.xu >= q.xu; lab = 'NGOẠI NHỜ'; }", tag='thẻ: góp xu chỉ khi đủ kinh nghiệm')
rep("else { ic = UIC.sprout || UIC.task; t = `Lên cấp ${n}`; em = `còn ${need - xp} kn`; f = (xp - prev) / (need - prev); }",
    "else { let td = null; try { ensureTasks(); td = ST.tasks.list.find(x => !x.done); } catch (e) {}\n"
    "    if (td){ try { ic = TASKIC(td); } catch (e) { ic = UIC.task; } t = td.txt; em = td.need > 1 ? `${td.have}/${td.need}` : 'chưa làm'; f = td.have / td.need; lab = 'VIỆC HÔM NAY'; isTask = true; }\n"
    "    else { ic = UIC.sprout || UIC.task; t = 'Chăm vườn thêm'; em = `còn ${need - xp} kinh nghiệm`; f = (xp - prev) / (need - prev); } }", tag='thẻ: chưa tới việc Ngoại nhờ')
rep("dl = `<span class=\"nqd\" data-d=\"1\">Việc hôm nay ${dn}/${L2.length}</span>`; } catch (e) {}",
    "if (!isTask && dn < L2.length) dl = `<span class=\"nqd\" data-d=\"1\">Việc hôm nay ${dn}/${L2.length}</span>`; } catch (e) {}", tag='thẻ: ẩn việc hôm nay đã xong')
rep("const h = `<small>${go ? 'LÀM LIỀN' : 'VIỆC TIẾP THEO'}</small>",
    "const h = `<small>${go ? 'LÀM LIỀN' : lab}</small>", tag='thẻ: nhãn')

# --- Sổ › Việc của Ngoại ---
rep("if (!q || !need) return ''; const ready = xp >= need, early = q.t !== 'pay';\n  let h = UX.title(`Việc Ngoại dặn · lên cấp ${n}`, early ? (ready ? 'làm xong là lên cấp' : 'làm trước được') : (ready ? 'đủ kinh nghiệm rồi' : `còn ${need - xp} kinh nghiệm`));",
    "if (!q || !need) return ''; const ready = xp >= need, early = q.t !== 'pay'; if (!early && !ready) return '';\n  let h = UX.title('Ngoại nhờ', ready ? 'xong việc này là lên cấp' : '');", tag='Sổ: ẩn việc góp xu chưa làm được')
rep("const qi = q.t === 'weed' ? UIC.sickle : q.t === 'pay' ? (q.exp || n === 10 || n === 12 || n === 18 ? ICON.cuoc : UIC.coin) : UIC.task;",
    "const qi = q.t === 'weed' ? UIC.sickle : q.t === 'pay' ? (ICON.cuoc || UIC.task) : UIC.task;", tag='Sổ: biểu tượng việc')
rep("<span>Trả ${q.xu} xu${!ready ? '<small>chưa đủ kinh nghiệm</small>' : ST.xu < q.xu ? `<small>còn thiếu ${q.xu - ST.xu} xu</small>` : ''}</span>",
    "<span>Góp ${q.xu} xu${ST.xu < q.xu ? `<small>còn thiếu ${q.xu - ST.xu} xu</small>` : ''}</span>", tag='Sổ: nút góp xu')
rep("ready ? (q ? `Đủ kinh nghiệm rồi, xong việc Ngoại dặn là lên cấp ${n}` : `Sắp lên cấp ${n}`)",
    "ready ? (q ? 'Đủ kinh nghiệm rồi, làm việc Ngoại nhờ là lên cấp' : `Sắp lên cấp ${n}`)", tag='Sổ: câu cấp')
rep("  if (feats.length) h += UX.title(`Cấp ${n} mở`) + `<div class=\"ulk\">${feats.map(([k, t]) => `<span><img src=\"${icOf(k)}\" alt=\"\">${t}</span>`).join('')}</div>`;\n  return h + UX.more('Kinh nghiệm có từ đâu'",
    "  return h + UX.more('Kinh nghiệm có từ đâu'", tag='Sổ: bỏ khối báo trước cấp sau')

open(P, 'w', encoding='utf-8').write(s); print('OK', len(log), 'chỗ vá:', ', '.join(log))
