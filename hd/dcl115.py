# dcl115: đồ trang trí mở dần từ cấp 3 tới 20; đơn hàng xoay vòng đều, có trái cây, không bỏ quên cây cũ. python3 dcl115.py vào ra
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
LV={3:['rao_go'],4:['chuong_ga_go'],5:['rao_bup','chuong_ga_ngoi'],6:['chuong_vit_la','chuong_vit_ton'],7:['lu_da_luon','ghe_da','bong_giay'],8:['den_long','vong'],9:['cauvua','ban_ghe_tre'],10:['den_sao','nguyetque','lu_mua'],11:['sudo','kimquyt','bu_nhin'],12:['vantue','bu_nhin_do'],13:['mai_chieu_thuy','hon_non_bo'],14:['cong_tre','bu_nhin_hoa'],15:['sanh','van_ngua'],16:['gian_bg','cong_gach'],17:['coi_xay'],18:['xuong'],19:['gieng'],20:['choi_la','mieu']}
m=",".join(f"{k}:{n}" for n,ks in LV.items() for k in ks)
rep("const DC = { lv: 13 };","const DC = { lv: 3 }, DCLV = {"+m+"}, dcLvOk = k => (ST.lv || 1) >= (DCLV[k] || 1) || !!(ST.dc && (ST.dc.own[k] || ST.dc.bag[k] > 0 || (ST.dc.items || []).some(x => x.k === k)));")
rep("function dcBuy(k){ const d = DCK[k]; if (!d || d.sp || !dcOn()) return;","function dcBuy(k){ const d = DCK[k]; if (!d || d.sp || !dcOn() || !dcLvOk(k)) return;")
rep("const sec = (t, cat) => `<div class=\"sub\">${t}</div>` + Object.keys(DCK).filter(k => DCK[k].cat === cat).sort((a, b) => (DCK[a].price || 0) - (DCK[b].price || 0)).map(row).join('');",
"const sec = (t, cat) => { const L = Object.keys(DCK).filter(k => DCK[k].cat === cat && dcLvOk(k)).sort((a, b) => (DCK[a].price || 0) - (DCK[b].price || 0)); return L.length ? `<div class=\"sub\">${t}</div>` + L.map(row).join('') : ''; }, nxt = Object.keys(DCLV).filter(k => DCLV[k] > (ST.lv || 1)).sort((a, b) => DCLV[a] - DCLV[b])[0];")
rep("sec('Đồ kiểng · đặt trên một ô đất trống', 'k'); }","sec('Đồ kiểng · đặt trên một ô đất trống', 'k') + (nxt ? `<div class=\"note\">Lên cấp ${DCLV[nxt]} Tiệm có thêm ${DCK[nxt].name.toLowerCase()}.</div>` : ''); }")
rep("if (dcOn() && !((ST.dc && ST.dc.items) || []).length) F.push({ lv: DC.lv + .5,","if ((ST.lv || 1) >= 7 && !((ST.dc && ST.dc.items) || []).length) F.push({ lv: 7.5,")
rep("13: [['dc_cong_gach', 'Trang trí vườn'], ['nong', 'Giàn nong hai tầng, thêm khạp']]","13: [['nong', 'Giàn nong hai tầng, thêm khạp']]")
rep("const icOf = k => ICON[k] || UIC[k] ||","for (const k in DCLV){ if (!DCK[k]) continue; const L = LVFEAT[DCLV[k]] = LVFEAT[DCLV[k]] || []; if (L.filter(x => String(x[0]).startsWith('dc_')).length < 2) L.push(['dc_' + k, DCK[k].name]); }\nconst icOf = k => ICON[k] || UIC[k] ||")
rep("13: ['Chợ giờ có bán đồ trang trí rồi. Con chọn rào, chậu kiểng làm vườn mình đẹp lên nghe.'],","13: ['Tiệm giờ có mai chiếu thủy với hòn non bộ đẹp lắm. Có dư xu con sắm dần cho vườn nghe.'],")
# đơn hàng: lâu chưa đặt thì càng dễ đặt, có trái cây cho hàng xóm, ghe cũng xoay vòng
rep("vegW = k => (1 + Math.min(3, (now - (last[k] || 0)) / 864e5)) * (fav.includes(k) ? 2 : 1);","vegW = k => Math.pow(1 + Math.min(4, (now - (last[k] || 0)) / 864e5) * 2, 2) * (fav.includes(k) ? 1.5 : 1);")
rep("const pre = Object.keys({ ...PHOI, ...MUOI, ...(lv >= 11 ? SAY : {}) }).filter(ok),","const fruits = Object.keys(CROPS).filter(k => CROPS[k].tree && !CROPS[k].rare && ok(k)), pre = Object.keys({ ...PHOI, ...MUOI, ...(lv >= 11 ? SAY : {}) }).filter(ok),")
rep("const sideOf = c => c === 'egg' ?","const sideOf = c => c === 'fruit' ? (k => k && [k, Math.max(2, Math.round(CROPS[k].yield * .4))])(pickW(fruits, vegW)) : c === 'egg' ?")
rep("lv < 11 ? [['egg', .45], ['pre', .55]] : lv < 15 ? [['egg', .3], ['pre', .4], ['fish', .3]] : [['egg', .2], ['pre', .3], ['fish', .3], ['spec', .2]];","lv < 11 ? [['egg', .4], ['pre', .4], ['fruit', .2]] : lv < 15 ? [['egg', .25], ['pre', .3], ['fish', .25], ['fruit', .2]] : [['egg', .15], ['pre', .25], ['fish', .25], ['spec', .15], ['fruit', .2]];")
rep("pick2 = [...pool].sort(() => Math.random() - .5).slice(0, nk);","L9 = (ST.ord.last = ST.ord.last || {}), pW = k => Math.random() * Math.pow(1 + Math.min(4, (Date.now() - (L9[k] || 0)) / 864e5) * 2, 2), pick2 = pool.map(k => [k, pW(k)]).sort((a, b) => b[1] - a[1]).slice(0, nk).map(x => x[0]); for (const k of pick2) L9[k] = Date.now();")
rep('GD, levelUp, sfx, errSend,','GD, levelUp, sfx, ordMake, dcLvOk, errSend,')
open(dst,'w',encoding='utf-8').write(s)
