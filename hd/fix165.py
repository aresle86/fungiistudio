# v164 -> v165:
# Chợ nổi + Bến bà con: bấm ghe hay bị trúng ghe khác.
# Cũ: bắn tia vô hộp bao của từng ghe (hộp tính luôn cây bẹo, cờ nên cao lêu nghêu), ghe nào gần máy quay thì ăn
#     -> hộp ghe trước che ghe sau; bấm vô bảng tên cũng trúng ghe đứng trước.
# Mới (cnoPick): chọn theo hình trên màn hình.
#   1) Bấm trúng bảng tên ghe nào thì chọn ghe đó (viền nới cho đủ 44px thì tính ngang hàng với thân ghe). Bảng tên xuồng bà con treo ở gốc cảnh nên ghép với xuồng gần nó nhất.
#   2) Không thì xét thân ghe (hộp bao cắt bớt phần cột cờ, bề ngang ghe không quá 1,8), nới cho đủ 44px; nhiều ghe trùng thì lấy ghe có tâm gần ngón tay nhất.
#   3) Ở Bến bà con bảng tên treo trên ngọn cây bẹo nên chiếc xuồng nằm ngay dưới đuôi bảng thật ra là xuồng hàng sau;
#      người chơi thì đọc bảng nào bấm xuồng dưới bảng đó -> bấm trúng thân xuồng thì lấy bảng tên gần nhất phía trên ngón tay.
#   4) Không trúng ghe nào thì giữ kết quả cũ (bến, khoảng trống).
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), n, a[:60])
    s = s.replace(a, b)
rep("BUILD = 'v164'", "BUILD = 'v165'")

rep("if (CHM.kind === 'cn'){ cnoTap(best); }", "if (CHM.kind === 'cn'){ cnoTap(cnoPick(cx, cy, best)); }")
rep("function cnoTap(best){",
    "function cnoRects(){ const B = CHM.B, C = CHM.cam, out = []; if (!B || !C) return out; C.updateMatrixWorld(); const vi = C.matrixWorldInverse, v = new T.Vector3();\n"
    "  const P = (x, y, z) => { v.set(x, y, z).applyMatrix4(vi); if (v.z > -.05) return null; v.applyMatrix4(C.projectionMatrix); return [(v.x + 1) / 2 * innerWidth, (1 - v.y) / 2 * innerHeight]; };\n"
    "  const R = (pts, mn, pad) => { let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9; for (const p of pts){ if (!p) return null; x0 = Math.min(x0, p[0]); y0 = Math.min(y0, p[1]); x1 = Math.max(x1, p[0]); y1 = Math.max(y1, p[1]); }\n"
    "    const px = Math.max(pad, (mn - (x1 - x0)) / 2), py = Math.max(pad, (mn - (y1 - y0)) / 2); x0 -= px; x1 += px; y0 -= py; y1 += py; if (x1 < 0 || y1 < 0 || x0 > innerWidth || y0 > innerHeight) return null; return [x0, y0, x1, y1]; };\n"
    "  const rt = new T.Vector3().setFromMatrixColumn(C.matrixWorld, 0), up = new T.Vector3().setFromMatrixColumn(C.matrixWorld, 1), wp = new T.Vector3(), ws = new T.Vector3();\n"
    "  for (const o of B.tags || []){ let p = o, ok = true, tag = null; while (p){ if (p.visible === false) ok = false; if (!tag && p.userData && p.userData.tag) tag = p.userData.tag; p = p.parent; } if (!ok) continue; o.getWorldPosition(wp);\n"
    "    if (!tag && o.userData.bt) tag = 'cn:ben'; if (!tag && o.userData.far){ let dm = 6.25; for (const [t, bb] of B.hits){ if (t.indexOf('cn:bc:')) continue; const dx = (bb.min.x + bb.max.x) / 2 - wp.x, dz = (bb.min.z + bb.max.z) / 2 - wp.z, d = dx * dx + dz * dz; if (d < dm){ dm = d; tag = t; } } } if (!tag) continue;\n"
    "    o.getWorldPosition(wp); o.getWorldScale(ws); const hw = ws.x / 2, a = -o.center.y * ws.y, b = (1 - o.center.y) * ws.y;\n"
    "    const pp = [P(wp.x - rt.x * hw + up.x * a, wp.y - rt.y * hw + up.y * a, wp.z - rt.z * hw + up.z * a), P(wp.x + rt.x * hw + up.x * b, wp.y + rt.y * hw + up.y * b, wp.z + rt.z * hw + up.z * b)], r = R(pp, 0, 0), r2 = R(pp, 44, 4); if (r) out.push([tag, r, o.userData.far ? 2 : 1]); if (r2) out.push([tag, r2, 3]); }\n"
    "  for (const [t, bb, o] of B.hits){ if (t === 'cn:ben') continue; const h = bb.max.y - bb.min.y, ym = bb.min.y + Math.min(h, Math.max(.9, h * .5)), pts = []; let z0 = bb.min.z, z1 = bb.max.z; if (o){ o.getWorldPosition(wp); z0 = Math.max(z0, wp.z - .9); z1 = Math.min(z1, wp.z + .9); if (z1 < z0){ z0 = bb.min.z; z1 = bb.max.z; } }\n"
    "    for (const X of [bb.min.x, bb.max.x]) for (const Y of [bb.min.y, ym]) for (const Z of [z0, z1]) pts.push(P(X, Y, Z)); const r = R(pts, 44, 6); if (r) out.push([t, r, 0]); }\n"
    "  return out; }\n"
    "function cnoPick(cx, cy, old){ try { if (CNX.son) return old; let best = null, bd = 1e9, bt = 0, on = 0; const rs = cnoRects(); for (const [t, r, isTag] of rs){ if (cx < r[0] || cx > r[2] || cy < r[1] || cy > r[3]) continue; const tg = isTag === 1 || isTag === 2; if (!isTag) on = 1; if (bt && !tg) continue;\n"
    "    const d = Math.max(Math.abs(cx - (r[0] + r[2]) / 2) / (r[2] - r[0]), Math.abs(cy - (r[1] + r[3]) / 2) / (r[3] - r[1])); if ((tg && !bt) || d < bd){ bd = d; best = t; bt = tg ? 1 : 0; } }\n"
    "  if (!bt && CNX.ben){ let ud = 1e9, ut = null; for (const [t, r, isTag] of rs){ if (isTag !== 2) continue; const dy = cy - r[3]; if (cx < r[0] || cx > r[2] || dy <= 0 || dy > (on ? Math.max(96, 2.2 * (r[3] - r[1])) : 36)) continue; if (dy < ud){ ud = dy; ut = t; } } if (ut) return ut; }\n"
    "  return best || old; } catch (e) { return old; } }\n"
    "function cnoTap(best){")

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
