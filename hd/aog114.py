# aog114: đưa ao ba bậc vào game. python3 aog114.py live/v114a.html live/v114b.html
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
rd=lambda f:open(f,encoding='utf-8').read()
rep("const BUILD = 'v114a'","const BUILD = 'v114b'")
i=s.index("function block4(id){"); j=s.index("await LDY(0);",i)
s=s[:i]+rd('aog114.js')+s[j:]
rep("const bigCells = k => { const B = ST.big[k]; return B && B.at ? block4(B.at) || [] : []; };","const bigCells = k => { const B = ST.big[k]; return B && B.at ? blockN(B.at, ...bigSz(k)) || [] : []; };")
i=s.index("function bigFit(id, me){"); j=s.index("function bigCenter(k){",i)
s=s[:i]+"function bigFit(id, me){ const P = PL[id]; if (!P || !P.bai) return null; const [Z] = ZGRID[zoneOf(P)], i = +id.slice(1) - 1, pre = id[0], [cn, rn] = bigSz(me); for (let dy = 0; dy < rn; dy++) for (let dx = 0; dx < cn; dx++){ if (i % Z.cols < dx) continue; const j = i - dx - dy * Z.cols; if (j < 0) continue; const a = pre + (j + 1), B = blockN(a, cn, rn); if (B && B.includes(id) && B.every(x => bigCellFree(x, me))) return a; } return null; }\n"+s[j:]
rep("function bigPlace(k, id){ const a = bigFit(id, k); if (!a) return false;","function bigPlace(k, id){ if (k === 'ao' && ST.big.ao && ST.big.ao.to) return false; const a = bigFit(id, k); if (!a) return false;")
rep("ST.big.ao = { own: 1, at: null };","ST.big.ao = { own: 1, at: null, tier: 1, dc: {}, nuoi: [] };")
i=s.index("// ao cá: bờ đất, nước, lục bình, cá kỷ lục bơi vòng"); j=s.index("const aoHit = (cx, cy)",i)
s=s[:i]+rd('aog114b.js')+"await LDY(0);\n"+s[j:]
rep("function bigHTML(k){ const D = BIGD[k],","function bigHTML(k){ if (k === 'ao') return aoHTML(); const D = BIGD[k],")
rep("else if (k === 'ao') setTimeout(() => say('Đào ao xong rồi! Cá nào con câu được, đẹp nhất Ngoại thả vô ao nuôi. Bạn bè ghé chơi là thấy liền.', 'vui', { idle: true }), 300);","else if (k === 'ao'){ const A0 = ST.big.ao, up = A0 && A0.to; if (up){ A0.tier = up; delete A0.to; delete A0.at0; aoHSet(); save(); } setTimeout(() => say(up ? `${AOT[up].name} xong rồi con! Rộng rinh chưa, thả thêm cá đi.` : 'Đào ao xong rồi! Bấm vô ao mà thả cá nuôi, lớn rồi kéo lưới. Bạn bè ghé chơi là thấy liền.', 'vui', { idle: true }), 300); }")
rep("V.root.visible = true; V.root.position.set(at[0], 0, at[1]); V.b.visible = false;","V.root.visible = !(k === 'ao' && ST.big.ao && ST.big.ao.to); V.root.position.set(at[0], 0, at[1]); V.b.visible = false;")
rep("else if (a === 'aobuy'){ aoBuy(id); return; }","else if (a === 'aobuy'){ aoBuy(id); return; } else if (a === 'aotha'){ aoTha(b.dataset.k); return; } else if (a === 'aoluoi'){ aoLuoi(); return; } else if (a === 'aodc'){ aoDcBuy(b.dataset.k); return; } else if (a === 'aoup'){ aoUp(); return; }")
rep("const a = bigFit(id, sapBk(it)); return a ? block4(a) : null; }","const a = bigFit(id, sapBk(it)); return a ? blockN(a, ...bigSz(sapBk(it))) : null; }")
rep("' (2×2 ô)'","' (' + bigSz(SUA.move).join('×') + ' ô)'")
rep("else toast('Cần bốn ô đất trống của con nằm sát nhau, hai ô ngang hai ô dọc, chưa đắp liếp.', 'dan', { now: true });","else toast(`Cần đủ ${bigSz(mk).join('×')} ô đất trống của con nằm sát nhau, chưa đắp liếp.`, 'dan', { now: true });")
rep("const mm = new T.Mesh(mergeGeometries(list, false), mt); mm.castShadow = true; g.add(mm);","const mm = new T.Mesh(mergeGeometries(list, false), mt); mm.castShadow = !mt.userData.noSh; mm.receiveShadow = !!mt.userData.noSh; g.add(mm);")
rep("dcFxTick(t, night, DCV.items.values());","dcFxTick(t, night, AOV.g && AOV.root.visible ? [...DCV.items.values(), AOV.g] : DCV.items.values());")
a="  return {\n  bu_nhin_do(){"
rep(a,"  return {\n"+rd('ao114_models.js')+"  bu_nhin_do(){")
rep("get: () => ({ BAK,","get: () => ({ S, r, closeSheet, aoUp, aoTha, aoLuoi, aoDcBuy, aoSync, AOV, AOT, AOD, aoGiong, bigCells, bigFit, bigPlace, BAK,")
open(dst,'w',encoding='utf-8').write(s); print('ok',len(s))
