p='live/vuon3d.html';s=open(p,encoding='utf8').read()
def rep(a,b,cnt=1):
    global s
    n=s.count(a); assert n==cnt,(n,a[:100]); s=s.replace(a,b)
# decor chừa mé sông
rep("rocks(7.2, 7.95, .8, 3); rocks(8.45, 7.05, .9, 3);","rocks(10.55, 7.95, .8, 3); rocks(10.9, 6.85, .9, 3);")
rep("tulips(6.3, 7.6, '#EDB940', 4);","tulips(5.65, 7.65, '#EDB940', 4);")
rep("bush(6.9, 7.1, .8);","bush(10.35, 7.35, .8);")
rep("for (const x of [-2.4, -1.6, 7.6, 8.6, 10.2]){","for (const x of [-2.4, -1.6, 5.75, 10.9, 11.6]){")
rep("if (x > -5.15 && x < -1.45 && z > -.85 && z < 1.65) continue;","if (x > -5.15 && x < -1.45 && z > -.85 && z < 1.65) continue; if (x > 6.1 && x < 9.8 && z > 6.7 && z < 8.3) continue;")
rep("for (let i = 0; i < 26; i++){ const x = R(-2, 10), z = R(5.5, 8); if (x > .8 && x < 7 && z < 6.4) continue;","for (let i = 0; i < 26; i++){ const x = R(-2, 10), z = R(5.5, 8); if (x > .8 && x < 7 && z < 6.4) continue; if (x > 6.1 && x < 9.8 && z > 6.7) continue;")
# bán cả kho: bán luôn trứng, cá
rep("for (const k of Object.keys(ST.inv)) if (CROPS[k] && ST.inv[k] > 0) act.sell(k, ST.inv[k]);","for (const k of Object.keys(ST.inv)) if (GD(k) && !GD(k).nosell && ST.inv[k] > 0) act.sell(k, ST.inv[k]);")
# đất bồi mé sông: đắp xong đất tốt sẵn
rep("    ST.xu -= c0; ST.open.push(id);","    ST.xu -= c0; ST.open.push(id); if (P.zone === 'song' && ST.plots[id]) ST.plots[id].soil = 1;")
# lên cấp
rep("  if (n === BAI.lv){","""  if (n === 8) say('Ngoại còn hai cái khạp da lươn với chỗ đào hố ủ phân. Ra chợ mua về đặt ở bãi hông nhà nghe con. Khạp muối dưa, hố ủ lá với lục bình thành phân.', 'vui', { idle: true });
  if (n === SONG.lv){ say('Đất bồi mé sông màu mỡ lắm, Ngoại cho con mở tám ô ngoài đó. Rảnh ra bến thả cần câu cá rô, cá lóc. Lò ấp trấu cạnh chuồng vịt cũng dùng được rồi.', 'vui', { idle: true }); setTimeout(() => { if (!VISIT) camTo(new T.Vector3(SONGC.x, .3, SONGC.z), Math.max(cam.zoom, DEFZ() * 1.1)); }, 1600); }
  if (n === BAI.lv){""")
rep("${n === 7 ? ', bãi hông nhà 12 ô, Sửa vườn, nong phơi ớt' : ''}","${n === 7 ? ', bãi hông nhà 12 ô, Sửa vườn, nong phơi ớt' : ''}${n === 8 ? ', khạp muối, hố ủ phân' : ''}${n === 9 ? ', mé sông 8 ô, câu cá ở bến, lò ấp vịt, canh chua cá lóc' : ''}")
rep("  11: { t: 'goal', txt: 'Trồng đủ 3 loại cây trái',","  10: { t: 'pay', xu: 200, txt: 'Đắp bờ mé sông chống lở', how: 'Đóng cừ tre, đắp đất dọc mé sông cho mùa nước khỏi lở bờ. Mốc chặn' },\n  11: { t: 'goal', txt: 'Trồng đủ 3 loại cây trái',")
# đơn hàng: cá, đồ muối
rep("try { for (const k of Object.keys(ST.nong.made || {})) if (PHOI[k]) pool.push(k); } catch (e) {}","try { for (const k of Object.keys(ST.nong.made || {})) if (PHOI[k]) pool.push(k); for (const k of Object.keys(ST.khap.made || {})) if (MUOI[k]) pool.push(k); if ((ST.cau.tot || 0) > 0) pool.push('caro', 'caloc'); } catch (e) {}")
rep("const known = pool.filter(k => k === 'trungga' || k === 'trungvit' || PHOI[k] ||","const known = pool.filter(k => k === 'trungga' || k === 'trungvit' || PHOI[k] || MUOI[k] || k === 'caro' || k === 'caloc' ||")
rep("base = PHOI[k] ? 1 :","base = PHOI[k] || k === 'dacai' ? 1 : k === 'hotvit' || k === 'caro' || k === 'caloc' ? 2 :")
rep("otkho: 'giã muối ớt', chuoiphoi: 'cho tụi nhỏ ăn vặt',","otkho: 'giã muối ớt', chuoiphoi: 'cho tụi nhỏ ăn vặt', dacai: 'ăn với thịt kho', hotvit: 'ăn cháo trắng', caro: 'kho tộ', caloc: 'nướng trui',")
# vườn mẫu
rep("  m.nong = { own: 1, at: 'H3',","  for (const [id, k, g] of [['S1', 'bap', 1.3], ['S2', 'cai', 1.3], ['S3', 'cachua', .7], ['S5', 'raumuong', 1.3], ['S6', 'ot', .9]]){ m.open.push(id); m.plots[id] = pl0(k, g, .85); m.plots[id].soil = 1; }\n  m.qd[10] = 1; m.khap = { own: 1, at: 'H4', jars: [{ k: 'dacai', t: 0, T: 1 }, { k: 'hotvit', t: 40000, T: 86400 }], done: 2, made: { dacai: 1 } }; m.ho = { own: 1, at: 'H12', mat: 4, t: 30000, bags: 2, done: 2 };\n  m.nong = { own: 1, at: 'H3',")
# bờ mé sông: cừ tre, hiện sau khi đắp bờ
a="/* --- câu cá ở bến"
assert s.count(a)==1
s=s.replace(a,"""/* --- bờ mé sông (việc lên cấp 10): hàng cừ tre đóng dọc bờ, đất đắp phía sau --- */
const BOV = (() => { const root = DYN(G(0, 0, 0)), pr = ROOT; ROOT = root; const z = R0 - .06;
  for (let x = SONG.x0 - .1; x <= SONG.x0 + 3.65; x += .09) M(cyl(.018, .022, R(.2, .28), 5), pick([C.bamboo, '#B8A25A', '#A8904a']), x, .02, z, { p: root });
  for (const y of [.07, .15]) M(box(3.8, .02, .02), '#8A6A3A', SONG.x0 + 1.77, y, z - .025, { p: root }); M(box(3.8, .05, .16), '#7A5236', SONG.x0 + 1.77, .0, z - .1, { p: root, cast: false });
  ROOT = pr; root.visible = false; return { root }; })();
function boTick(){ BOV.root.visible = (ST.lv || 1) >= SONG.lv && !!(ST.qd || {})[10]; }
"""+a)
open(p,'w',encoding='utf8').write(s); print('ok')
