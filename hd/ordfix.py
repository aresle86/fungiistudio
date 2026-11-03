#!/usr/bin/env python3
"""v102: đơn vừa sức (cá ít, trái cây không quá một vụ, ghe tối đa 3 món, không đòi món nấu chưa có);
cây cổ tích: chỉ rõ chạm vô đốm sáng, bong bóng đếm giờ khi cây đang lớn."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# ---------- đơn hàng xóm ----------
# cá: chỉ một đơn có cá cùng lúc, mỗi đơn 1-2 con (câu mỗi ngày có hạn)
rep("for (const k of Object.keys(ST.fishLog || {})) if (FISHK[k] && FISHK[k].tier <= 1) pool.push(k);",
    "if (!((ST.ord && ST.ord.list) || []).some(o => o.items.some(([k2]) => FISHK[k2]))) for (const k of Object.keys(ST.fishLog || {})) if (FISHK[k] && FISHK[k].tier <= 1) pool.push(k);   /* cá: một đơn có cá thôi */")
# trái cây không quá ~60% một vụ, cá không cộng thêm
rep("return [k, base + (lv >= 6 ? 1 : 0)]; });",
    "if (FISHK[k]) return [k, Math.min(2, base)]; const q0 = base + (lv >= 6 ? 1 : 0); return [k, CROPS[k] && CROPS[k].tree ? Math.min(q0, Math.max(2, Math.round((CROPS[k].yield || 4) * .6))) : q0]; });   /* đơn vừa sức một vụ */")
# ---------- ghe bẹo: tối đa 3 món, món nấu chỉ khi đang có, đồ làm ra 1-2, cá tối đa 2, trái cây tối đa một vụ ----------
rep("const items = [...m.entries()].slice(0, 4).map(([k, q]) => [k, Math.min(PHOI[k] || SAY[k] || MUOI[k] || DISH[k] ? 2 : 8, Math.max(2, q))]),",
    "const items = [...m.entries()].filter(([k]) => !DISH[k] || has(k) >= 1).slice(0, 3).map(([k, q]) => [k, PHOI[k] || SAY[k] || MUOI[k] || DISH[k] ? Math.max(1, Math.min(2, q)) : FISHK[k] ? Math.min(2, q) : CROPS[k] && CROPS[k].tree ? Math.min(Math.max(2, q), Math.max(2, Math.round((CROPS[k].yield || 4) * .8))) : Math.min(8, Math.max(2, q))]),")

# ---------- cây cổ tích: chỉ rõ việc cần làm ----------
rep("if (F.st === 0 && !F.said){ F.said = 1; save(); setTimeout(() => say('Chỗ đất kia lạ lắm con, có đốm sáng với đom đóm bay quanh. Lại coi thử đi.', 'vui', { idle: true }), 1500); }",
    "if (F.st === 0 && !F.said){ F.said = 1; save(); setTimeout(() => { say('Chỗ đất kia lạ lắm con, có đốm sáng với đom đóm bay quanh. Chạm vô đốm sáng coi thử đi.', 'vui', { idle: true }); try { const pp = ftPos(k); if (!VISIT) camTo(new T.Vector3(pp[0], .3, pp[1]), Math.max(cam.zoom, DEFZ() * 1.1)); } catch (e) {} }, 1500); }")
# cây đang lớn: bong bóng có thanh đếm giờ tới đoạn chuyện kế
rep("else if (k === 'khevang' && st >= 3 && F.told >= 3 && F.wk !== wkKey()) objBub(V, v, UIC.coin, t, hy); }",
    "else if (k === 'khevang' && st >= 3 && F.told >= 3 && F.wk !== wkKey()) objBub(V, v, UIC.coin, t, hy); else if (st >= 1 && st < D.max && D.dur[st]){ const T0 = D.dur[st] * 1000 / (ST.spd || 1), el = Date.now() - F.t; objBub(V, v, UIC['ft_' + k] || ICON.la, t, hy, Math.min(1, el / T0), Math.max(0, T0 - el)); } }")
# kể xong một đoạn: báo bao lâu nữa có đoạn kế
rep("function ftTell(k){ const F = ST.ft[k], D = FT[k]; if (!F || F.told >= F.st) return; const txt = D.parts[F.told]; F.told++; save(); say(txt, 'vui', { now: true }); sfx('say');",
    "function ftTell(k){ const F = ST.ft[k], D = FT[k]; if (!F || F.told >= F.st) return; const txt = D.parts[F.told]; F.told++; save(); say(txt, 'vui', { now: true }); sfx('say'); if (F.told === F.st && F.st < D.max && D.dur[F.st]) setTimeout(() => toast(`Cây đang lớn. Chừng ${growS(D.dur[F.st])} nữa lại chạm nghe tiếp chuyện`), 2600);")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
