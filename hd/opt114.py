# opt114: gộp mảnh nhỏ để giảm lượt vẽ. python3 opt114.py live/v114b.html live/v114c.html
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
rep("const BUILD = 'v114b'","const BUILD = 'v114c'")
# gộp nhóm chỉ di chuyển nguyên khối, giữ món sáng đêm và đèn
rep("function mergeLocal(G0){","function mergeLive(G0){ const par = G0.parent, pos = G0.position.clone(), q = G0.quaternion.clone(), sc = G0.scale.clone(); if (par) par.remove(G0); G0.position.set(0, 0, 0); G0.quaternion.identity(); G0.scale.set(1, 1, 1); G0.updateMatrixWorld(true); const ms = mergeMeshes(G0), keep = []; G0.traverse(o => { if (o !== G0 && ((o.isMesh && o.userData.keep) || o.isLight)) keep.push(o); }); for (const o of keep) G0.attach(o); for (const c of [...G0.children]) if (!keep.includes(c)) G0.remove(c); for (const m of ms) G0.add(m); G0.position.copy(pos); G0.quaternion.copy(q); G0.scale.copy(sc); if (par) par.add(G0); }\nfunction mergeLocal(G0){")
rep("try { mergeLocal(COOP0); mergeLocal(FENCE0); } catch (e) { console.warn('merge', e); }","try { mergeLocal(COOP0); mergeLocal(FENCE0); for (const h of HYA) mergeLive(h.g); mergeLive(BOAT); const gb = GHEV.root.children.find(c => c !== GHEV.hit); if (gb) mergeLive(gb); } catch (e) { console.warn('merge', e); }")
i=s.index('function landFence(v){'); j=s.index('\n  ROOT = pr; }',i)
s=s[:j]+"\n  ROOT = pr; { const ms = mergeMeshes(g); g.clear(); for (const m of ms) g.add(m); } }"+s[j+len('\n  ROOT = pr; }'):]
open(dst,'w',encoding='utf-8').write(s); print('ok',len(s))
