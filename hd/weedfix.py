#!/usr/bin/env python3
"""v100: phát cỏ mé mương dễ bấm — chạm thẳng bong bóng cái liềm là phát bụi đó (trước đây chạm bong bóng trượt xuống đất phía sau nên không ăn);
cầm liềm vẫn thấy bong bóng chỉ bụi kế; bấm nút Liềm khi đang có việc phát cỏ thì bay tới bụi gần nhất + nhắc ngắn; bong bóng màu cam (việc cần làm)."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep("WEEDV.bub = bubbleK('h'); try { bubIcon(WEEDV.bub, UIC.sickle); } catch (e) {} }",
    "WEEDV.bub = bubbleK('h'); try { bubIcon(WEEDV.bub, UIC.sickle); bubCol(WEEDV.bub, BUBC.lam); } catch (e) {} }\nfunction weedBubHit(cx, cy){ const b = WEEDV.bub; if (!b || !b.visible || WEEDV.nx == null || WEEDV.nx < 0) return -1; ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); const h = b.children.find(c => c.userData.bub); return h && ray.intersectObject(h, false).length ? WEEDV.nx : -1; }   /* chạm trúng bong bóng liềm thì tính là chạm bụi cỏ nó chỉ */")
rep("const b = WEEDV.bub, show = nx >= 0 && !(TOOL && TOOL.kind === 'cut');", "WEEDV.nx = nx; const b = WEEDV.bub, show = nx >= 0;")
rep("try { if (!weedOn()) return null; const g = groundAt(e.clientX, e.clientY);",
    "try { if (!weedOn()) return null; { const bi = weedBubHit(e.clientX, e.clientY); if (bi >= 0) return { x: WEEDP[bi][0], z: WEEDP[bi][1] }; } const g = groundAt(e.clientX, e.clientY);")
rep("  if (!s.moved && TOOL && !TOOL.temp && !TOOL.temp2){ const g = groundAt(e.clientX, e.clientY),",
    "  if (!s.moved && TOOL && TOOL.kind === 'cut'){ try { const bi = weedBubHit(e.clientX, e.clientY); if (bi >= 0 && weedAt(WEEDP[bi][0], WEEDP[bi][1], .1)){ save(); hud(); return; } } catch (er) {} }   /* cầm liềm chạm bong bóng: phát bụi đó */\n  if (!s.moved && TOOL && !TOOL.temp && !TOOL.temp2){ const g = groundAt(e.clientX, e.clientY),")
rep("TRAY.cut.addEventListener('click', () => setTool(TOOL && TOOL.kind === 'cut' ? null : { kind: 'cut' }));",
    "TRAY.cut.addEventListener('click', () => { if (TOOL && TOOL.kind === 'cut') return setTool(null); let w = false; try { w = weedOn() && weedLeft().length > 0; } catch (e) {} if (w){ weedGo(); toast('Chạm hay vuốt liềm qua bụi cỏ có bong bóng'); } else setTool({ kind: 'cut' }); });   /* đang có việc phát cỏ: bay tới bụi gần nhất, nhắc ngắn */")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
