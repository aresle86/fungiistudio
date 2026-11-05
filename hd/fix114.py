# fix114: ghe bẹo trong Chợ và nhiệm vụ ngày, đèn đỏ ban đêm. python3 fix114.py live/v114c.html live/v114d.html
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
rep("const BUILD = 'v114c'","const BUILD = 'v114d'")
# Chợ, bến: nói rõ khi ghe chưa tới hay đã đi
rep("  else if (nOk) h += UX.hero(ICON.cho, `${nOk} đơn giao được rồi`, 'Hàng xóm đang chờ ở bến', 'go');","  else if (nOk) h += UX.hero(ICON.cho, `${nOk} đơn giao được rồi`, 'Hàng xóm đang chờ ở bến', 'go');\n  else if (gheOn() && !ST.ghe.o) h += UX.hero(ICON.ghe, 'Ghe bẹo chưa có ở bến', ST.ghe.d === dayKey() ? 'Hôm nay ghe đi rồi, mai sáng ghé lại' : 'Sáng sớm ghe mới ghé');")
# việc trong ngày: ghe đi rồi thì đổi việc khác, khỏi kẹt
rep("function gheTick(t){ const on = gheOn() && !!ST.ghe.o && !VISIT; GHEV.root.visible = on; GHEV.b.visible = false; if (!on) return;","function gheTaskFix(){ try { const L = ST.tasks && ST.tasks.list; if (!L || ST.ghe.o || ST.ghe.d !== dayKey()) return; const i = L.findIndex(x => x.t === 'ghe' && !x.done); if (i < 0) return; const have = new Set(L.map(x => x.t + ':' + (x.k || ''))), f = featTasks().find(x => x.t !== 'ghe' && !have.has(x.t + ':' + (x.k || ''))) || (have.has('water:') ? { t: 'sell', txt: 'Bán 6 món ở chợ', need: 6, rw: ['coin', 15] } : { t: 'water', txt: 'Tưới liếp 3 lần', need: 3, rw: ['coin', 15] }); L[i] = { ...f, have: 0, done: false }; soBadge(); save(); } catch (e) {} }\nfunction gheTick(t){ const on = gheOn() && !!ST.ghe.o && !VISIT; GHEV.root.visible = on; GHEV.b.visible = false; if (!on){ if (!VISIT && gheOn()) gheTaskFix(); return; }")
# đèn lồng đỏ: giữ màu đỏ ban đêm, không ngả vàng trắng
rep("const LAMP = new T.MeshStandardMaterial({ color: '#E25A3B', emissive: '#ff8a3a', emissiveIntensity: 0, flatShading: true, roughness: .6 });","const LAMP = new T.MeshStandardMaterial({ color: '#E25A3B', emissive: '#ff8a3a', emissiveIntensity: 0, flatShading: true, roughness: .6 }), LAMPR = new T.MeshStandardMaterial({ color: '#D8402A', emissive: '#F2381A', emissiveIntensity: 0, flatShading: true, roughness: .6 });")
rep("const lamT = (x, y, z, rr) => { lit(sph(rr, 9, 7), LAMP, x, y, z,","const lamT = (x, y, z, rr) => { lit(sph(rr, 9, 7), LAMPR, x, y, z,")
rep("LAMP.emissiveIntensity = night * (1.6 + Math.sin(t * 11) * .15);","LAMP.emissiveIntensity = night * (1.6 + Math.sin(t * 11) * .15); LAMPR.emissiveIntensity = night * (.95 + Math.sin(t * 11) * .08);")
rep("get: () => ({ S, r, closeSheet,","get: () => ({ gheTaskFix, benHTML, S, r, closeSheet,")
open(dst,'w',encoding='utf-8').write(s); print('ok',len(s))
