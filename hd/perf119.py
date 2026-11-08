# perf119: chống nóng máy, đợt 1 (đo bằng tPerf119 / tPerfBrk trên chip đồ họa thật).
#  1) Bóng đổ tính theo nhịp thời gian thay vì mỗi khung: điện thoại 160 ms (~6 lần/giây) ở mọi mức; máy tính 33 ms ở mức Cao, 80 ms ở mức Vừa.
#     Trồng, hái, đổi ô (refreshPlot) thì đánh dấu tính lại ngay ở khung kế.
#     (Đo: bước tính bóng chiếm ~44% lần vẽ và ~34% tam giác của một khung có tính bóng; mức Cao trước đây tính 60 lần/giây.)
#  2) Điện thoại: giới hạn hình khi để yên áp cho mọi mức (trước đây mức Cao không giới hạn, vẽ 60 hình/giây):
#     ~30 hình/giây (nhịp 30 ms vì khung màn hình 16,7 ms), để yên quá 8 giây không chạm thì ~20 (nhịp 45 ms); máy đuối (AQ) cũng ~20; để yên quá 1 phút (để máy chờ rau lớn) thì ~12 (nhịp 80 ms).
#  3) Điện thoại mức Cao: độ nét tối đa 1,75 thay vì 2.
#  Biến mới khai báo bằng var ở đầu module (bài học cpN: tránh dùng trước khai báo lúc dựng cảnh).
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a))
    s = s.replace(a, b)

rep("var cpN = 0;   // hotfix117b: dùng được cả lúc đang dựng cảnh\n",
    "var cpN = 0;   // hotfix117b: dùng được cả lúc đang dựng cảnh\nvar SHDIRTY = 1, SHT = 0;   // v119: bóng đổ cần tính lại / lần tính gần nhất\n")
# 1) bóng đổ theo nhịp thời gian
rep("if (r.shadowMap.enabled){ r.shadowMap.autoUpdate = QI >= 2; if (QI < 2 && (SHF = (SHF + 1) % (MOBILE ? 4 : 2)) === 0) r.shadowMap.needsUpdate = true; }",
    "if (r.shadowMap.enabled){ r.shadowMap.autoUpdate = false; const shN = performance.now(), shGap = MOBILE ? 160 : (QI >= 2 ? 33 : 80); if (SHDIRTY || shN - SHT >= shGap){ SHT = shN; SHDIRTY = 0; r.shadowMap.needsUpdate = true; } }")
rep("function refreshPlot(id){ const p = ST.plots[id],", "function refreshPlot(id){ SHDIRTY = 1; const p = ST.plots[id],")
# 2) giới hạn hình khi để yên trên điện thoại, mọi mức
rep("idle = MOBILE && QI < 2 && !window.__stop && fn >= FRH, gap = idle ? (AQ.lv >= 1 ? 41 : 28) : 0;",
    "idle = MOBILE && !window.__stop && fn >= FRH, gap = idle ? (fn - FRH > 60000 ? 80 : AQ.lv >= 1 || fn - FRH > 8000 ? 45 : 30) : 0;")
# 3) độ nét mức Cao trên điện thoại
rep("{ pr: Math.min(devicePixelRatio, 2), sh: 4096, fx: 1 }]", "{ pr: Math.min(devicePixelRatio, MOBILE ? 1.75 : 2), sh: 4096, fx: 1 }]")
# 4) sọc trên đất mé sông = bóng của thanh rào ngang dài, mảnh (tắt bóng đổ thì mất): thanh ngang không đổ bóng, cột vẫn đổ bóng
rep("for (const yy of [.12, .27]) M(box(.03, .04, v1 - v0), C.woodD, u, yy, (v0 + v1) / 2); }",
    "for (const yy of [.12, .27]) M(box(.03, .04, v1 - v0), C.woodD, u, yy, (v0 + v1) / 2, { cast: false }); }")
rep("for (const y of [.07, .15]) M(box(ZW(SONG) + .3, .02, .02), '#8A6A3A', SONG.x0 + ZW(SONG) / 2, y, z - .025, { p: root });",
    "for (const y of [.07, .15]) M(box(ZW(SONG) + .3, .02, .02), '#8A6A3A', SONG.x0 + ZW(SONG) / 2, y, z - .025, { p: root, cast: false });")
# 5) lên cấp tăng lượt câu: Ngoại nói đúng số con, đang câu thì thanh câu cập nhật liền
rep("lvSay('Dạo này cá về nhiều lắm con. Từ nay mỗi ngày con câu thêm được vài con nữa nghe.', 'vui', { idle: true });",
    "{ lvSay(`Dạo này cá về nhiều lắm con. Từ nay mỗi ngày con câu được ${cauCap() - (ST.cau.bonus === dayKey() ? 1 : 0)} con nghe.`, 'vui', { idle: !FM.on }); try { if (FM.on && FM.ph === 'aim') fuiAim(); } catch (e) {} }")
rep('["^Mồi (.+) hợp con', '["^Dạo này cá về nhiều lắm con\\\\. Từ nay mỗi ngày con câu được (\\\\d+) con nghe\\\\.$", "The fish are running these days, dear. From now on you can catch $1 a day."], ["^Mồi (.+) hợp con')
rep("`Hôm nay câu đủ ${cauCap()} con rồi`", "`Hôm nay câu đủ ${cauCap()} con rồi, mai câu tiếp`")
# 6) mương nhỏ xen giữa các hàng ô: vuông như mương lớn. Khúc liền nhau gộp một dải, hai đầu có bờ đất đóng lại (trước đây
#    nước chạy ra tới mép, đầu mương hở). Khúc mương "khô" giữa hai ô đất không trồng: không vẽ gì nữa (trước đây phủ 5 miếng
#    cỏ xanh đậm nhạt xen kẽ, lệch màu cỏ thật nên hiện thành sọc, kể cả khi tắt bóng đổ — anh Ares thấy ở mé sông).
old_i = "  const tmp = new T.Group(), pr = ROOT; ROOT = tmp; for (const [a, b, last, wet] of segs){"
assert s.count(old_i) == 1
i = s.index(old_i); j = s.index("  ROOT = pr; for (const m of mergeMeshes(tmp)) MUV.root.add(m); }", i)
s = s[:i] + r"""  const tmp = new T.Group(), pr = ROOT; ROOT = tmp;
  const runs = []; for (const sg of segs){ const [a, b, last, wet] = sg; if (!wet) continue; const A = PL[a].b, B = PL[b].b, L = runs[runs.length - 1]; if (L && Math.abs(L.z0 - A[3]) < 1e-6 && Math.abs(A[0] - L.xe) < .2){ L.x1 = A[2] + .05; L.xe = A[2]; L.ids.push(a); } else runs.push({ x0: A[0] - .05, x1: A[2] + .05, xe: A[2], z0: A[3], z1: B[1], ids: [a] }); }
  for (const u of runs){ const { x0, x1, z0, z1 } = u, cx = (x0 + x1) / 2, cz = (z0 + z1) / 2, w = x1 - x0, l = z1 - z0;
    M(box(w, .03, l), '#7E5434', cx, -.005, cz, { cast: false, sway: 0 }); M(box(w - .08, .02, l - .08), C.water, cx, .006, cz, { cast: false, sway: 0 });   /* bờ đất bao quanh cả bốn phía */
    const ps = sd; sd = 900 + u.ids[0].charCodeAt(1) * 7 + u.ids[0].length; for (const id of u.ids){ if (rnd() < .5){ const A = PL[id].b; for (let k = 0; k < 2; k++) M(new T.CylinderGeometry(.05, .05, .006, 7), '#6FB04A', (A[0] + A[2]) / 2 + R(-(A[2] - A[0]) / 3, (A[2] - A[0]) / 3), .02, cz + R(-.03, .03), { cast: false, sway: 0 }); } } sd = ps; }
""" + s[j:]

# 7) (bỏ) bo góc mương lớn: anh Ares muốn mương lớn vuông như cũ, chỉ giữ bo đầu mương nhỏ giữa các hàng ô ở mục 6

# 8) laptop: thanh chọn hạt giống kéo ngang bằng chuột để cuộn (trước chỉ vuốt được trên màn hình cảm ứng), lăn chuột cũng cuộn ngang.
#    Kéo xuống vẫn là gieo qua nhiều liếp; kéo ngang quá 6 điểm ảnh thì là cuộn, buông ra không tính là chọn hạt.
rep("RING.addEventListener('pointerdown', e => { const b = e.target.closest('.rgi'); if (!b) return; const k = b.dataset.k, x0 = e.clientX, y0 = e.clientY, pid = e.pointerId; let started = false;",
    "RING.addEventListener('pointerdown', e => { const b = e.target.closest('.rgi'); if (!b) return; const k = b.dataset.k, x0 = e.clientX, y0 = e.clientY, pid = e.pointerId, rgs = b.closest('.rgs'), sl0 = rgs ? rgs.scrollLeft : 0, mouse = e.pointerType !== 'touch'; let started = false, scr = false;")
rep("const mv = ev => { if (ev.pointerId !== pid || started) return; const dx = ev.clientX - x0, dy = ev.clientY - y0; if (Math.hypot(dx, dy) > 10 && Math.abs(dy) > Math.abs(dx) * .8){ started = true; const id = RINGID;",
    "const mv = ev => { if (ev.pointerId !== pid || started) return; const dx = ev.clientX - x0, dy = ev.clientY - y0; if (mouse && rgs && (scr || (Math.abs(dx) > 6 && Math.abs(dx) >= Math.abs(dy)))){ scr = true; rgs.scrollLeft = sl0 - dx; return; } if (Math.hypot(dx, dy) > 10 && Math.abs(dy) > Math.abs(dx) * .8){ started = true; const id = RINGID;")
rep("const up = ev => { if (ev.pointerId !== pid) return; done(); if (started){ if (TOOL && TOOL.temp2) setTool(null); hud(); return; } const id = RINGID;",
    "const up = ev => { if (ev.pointerId !== pid) return; done(); if (scr) return; if (started){ if (TOOL && TOOL.temp2) setTool(null); hud(); return; } const id = RINGID;")
rep("RING.addEventListener('pointerdown', e => { const b = e.target.closest('.rgi'); if (!b) return; const k = b.dataset.k, x0 = e.clientX, y0 = e.clientY, pid = e.pointerId, rgs",
    "RING.addEventListener('wheel', e => { const g = e.target.closest('.rgs'); if (!g || g.scrollWidth <= g.clientWidth) return; if (Math.abs(e.deltaY) > Math.abs(e.deltaX)){ g.scrollLeft += e.deltaY; e.preventDefault(); } }, { passive: false }); RING.addEventListener('pointerdown', e => { const b = e.target.closest('.rgi'); if (!b) return; const k = b.dataset.k, x0 = e.clientX, y0 = e.clientY, pid = e.pointerId, rgs")

s = s.replace("BUILD = 'v118a'", "BUILD = 'v119a'")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
