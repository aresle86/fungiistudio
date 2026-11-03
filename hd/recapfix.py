#!/usr/bin/env python3
"""v99: Ba mươi bữa ở vườn Ngoại — về vườn đủ 30 ngày thì hiện trang kỷ niệm: ảnh vườn chụp lúc đó (ẩn bong bóng), 6 số liệu, lời Ngoại,
nút Treo ảnh trong nhà (khung ảnh trên vách hông nhà) và Lưu ảnh kỷ niệm. Đếm thêm số rổ rau thu hoạch."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

rep("document.querySelector('.ddt.on, .lvup:not([hidden]), .fui .fcard, #tstw .tst')", "document.querySelector('.ddt.on, .lvup:not([hidden]), .fui .fcard, #tstw .tst, .yrc-scrim')")
rep("harvest(id, bonus = 1){ stepMark('harvest1');", "harvest(id, bonus = 1){ stepMark('harvest1'); if (!PL[id].tree) ST.hvN = (ST.hvN || 0) + 1;")

JS = r"""/* --- Ba mươi bữa ở vườn Ngoại: trang kỷ niệm ngày thứ 30 --- */
const YR = { at: [2.4 + 1.4 + .012, .75, .35 + .55], frame: null };
function yrStats(){ const n = o => Object.keys(o || {}).length; return { harv: ST.hvN || 0, tree: ST.treeHv || 0, fish: Object.keys(ST.fishLog || {}).filter(k => FISHK[k]).length, cook: Object.values((ST.bep && ST.bep.made) || {}).reduce((a, b) => a + (+b || 0), 0), bu: n(ST.buom), guest: ST.guestN || 0 }; }
function yrPhoto(){ const hid = []; for (const g of (window.__BUBALL || [])) if (g.visible){ g.visible = false; hid.push(g); } const sv = { p: cam.position.clone(), t: ctl.target.clone(), z: cam.zoom }, off = cam.position.clone().sub(ctl.target);
  ctl.target.set(3.2, .3, 3.0); cam.position.copy(ctl.target).add(off); cam.zoom = DEFZ() * 1.05; cam.updateProjectionMatrix(); cam.updateMatrixWorld(); r.render(S, cam);
  const src = r.domElement, W = src.width, H = src.height, a = 4 / 3; let sw = W, sh = W / a; if (sh > H){ sh = H; sw = H * a; } const c = document.createElement('canvas'); c.width = 640; c.height = 480; c.getContext('2d').drawImage(src, (W - sw) / 2, (H - sh) / 2, sw, sh, 0, 0, 640, 480);
  const c2 = document.createElement('canvas'); c2.width = 320; c2.height = 240; c2.getContext('2d').drawImage(c, 0, 0, 320, 240);
  cam.position.copy(sv.p); ctl.target.copy(sv.t); cam.zoom = sv.z; cam.updateProjectionMatrix(); for (const g of hid) g.visible = true; return [c.toDataURL('image/jpeg', .86), c2.toDataURL('image/jpeg', .78)]; }
function yrFrame(){ if (!ST.yr || !ST.yr.hang || !ST.yr.ph || VISIT){ if (YR.frame) YR.frame.visible = false; return; } if (YR.frame){ YR.frame.visible = true; return; }
  const g = DYN(G(YR.at[0], YR.at[1], YR.at[2], Math.PI / 2)); M(box(.34, .27, .025), '#6B4529', 0, 0, .012, { p: g }); M(box(.3, .23, .01), '#FFF8EA', 0, 0, .026, { p: g, cast: false });
  const im = new Image(), tx = new T.Texture(im); tx.colorSpace = T.SRGBColorSpace; im.onload = () => { tx.needsUpdate = true; }; im.src = ST.yr.ph;
  const pl = new T.Mesh(new T.PlaneGeometry(.26, .195), new T.MeshBasicMaterial({ map: tx, toneMapped: false })); pl.position.set(0, .006, .032); g.add(pl); M(cyl(.004, .004, .1, 3), C.ink, 0, .17, .01, { p: g, r: [0, 0, 0], cast: false }); M(sph(.012, 6, 4), '#B8862E', 0, .22, .012, { p: g, cast: false });
  YR.frame = g; }
function yrSave(full){ const W = 900, H = 1040, c = document.createElement('canvas'); c.width = W; c.height = H; const x = c.getContext('2d'); x.fillStyle = '#FFF8EA'; x.fillRect(0, 0, W, H); x.fillStyle = '#9A6A3C'; x.fillRect(0, 0, W, 150);
  x.fillStyle = '#FFF8EA'; x.textAlign = 'center'; x.font = '400 54px "Paytone One"'; x.fillText('Ba mươi bữa ở vườn Ngoại', W / 2, 82); x.font = '600 28px "Baloo 2"'; x.fillStyle = '#FCE9C8'; x.fillText(`Vườn ${ST.player.garden || ''} · Kỷ niệm ngày thứ 30`, W / 2, 126);
  const im = new Image(); im.onload = () => { x.save(); x.translate(W / 2, 560); x.rotate(-.025); x.fillStyle = '#fff'; x.shadowColor = 'rgba(74,47,30,.3)'; x.shadowBlur = 24; x.shadowOffsetY = 8; x.fillRect(-370, -340, 740, 640); x.shadowColor = 'transparent'; x.drawImage(im, -350, -320, 700, 525);
    x.fillStyle = '#6B4529'; x.font = 'italic 600 34px "Baloo 2"'; x.fillText('Vườn nhà mình sau ba mươi bữa', 0, 262); x.restore();
    const a = document.createElement('a'); a.download = 'mietvuon-30-bua.png'; a.href = c.toDataURL('image/png'); document.body.appendChild(a); a.click(); a.remove(); toast('Đã lưu ảnh kỷ niệm'); }; im.src = full; }
function yrShow(again){ if (document.querySelector('.yrc-scrim')) return; let full;
  if (!again || !ST.yr || !ST.yr.ph){ const [f, sm] = yrPhoto(); full = f; ST.yr = Object.assign(ST.yr || {}, { d: dayKey(), s: yrStats(), ph: sm }); save(); } else full = ST.yr.ph;
  const Sx = ST.yr.s, I = ICON, U = UIC, stat = (img, nn, t) => `<div class="yrc-s"><img src="${img}" alt=""><b>${nn}</b><span>${t}</span></div>`, d = document.createElement('div'); d.className = 'yrc-scrim';
  d.innerHTML = `<div class="yrc" role="dialog" aria-label="Ba mươi bữa ở vườn Ngoại"><button class="x yrc-x" aria-label="Đóng">×</button>
  <div class="yrc-h"><b>Ba mươi bữa ở vườn Ngoại</b><span><em>Vườn ${esc(ST.player.garden || '')}</em> · <em>Kỷ niệm ngày thứ 30</em></span></div>
  <div class="yrc-b"><div class="yrc-ph"><img src="${full}" alt="Ảnh vườn"><i>Vườn nhà mình sau ba mươi bữa</i></div>
  <div class="yrc-st">${stat(I.cai, Sx.harv, 'Rổ rau thu hoạch')}${stat(I.xoai, Sx.tree, 'Đợt hái trái')}${stat(I.caro, Sx.fish, 'Loài cá đã câu')}${stat(I.canhchuaca, Sx.cook, 'Nồi Ngoại nấu')}${stat(U.bu_trangcai, Sx.bu, 'Loài bướm ghé vườn')}${stat(AVIMG.banbe || I.cai, Sx.guest, 'Lượt bạn ghé chơi')}</div></div>
  <div class="yrc-l"><p>Mới đó mà ba mươi bữa rồi hen. Từ mấy liếp đất trống, giờ rau lên xanh mướt, cây cũng có trái ăn. Bếp lại đỏ lửa, bạn bè lâu lâu ghé chơi, vui cả nhà.</p><p>Ngoại thích nhất mấy lúc hai bà cháu ngồi coi bướm đậu ngoài vườn. Chẳng làm gì, vậy mà vui. Mai mình trồng thêm ít bông nghen, cho tụi nó còn ghé nữa.</p><p class="sg">— Ngoại</p></div>
  <div class="yrc-f"><button class="btn g" data-y="hang">${ST.yr.hang ? 'Coi ảnh trên vách' : 'Treo ảnh trong nhà'}</button><button class="btn" data-y="save">Lưu ảnh kỷ niệm</button></div></div>`;
  document.body.appendChild(d); document.body.classList.add('yron'); sfx('up');
  const close = () => { d.remove(); document.body.classList.remove('yron'); };
  d.addEventListener('click', e => { const b = e.target.closest('[data-y], .yrc-x'); if (!b) return; if (b.classList.contains('yrc-x')) return close();
    if (b.dataset.y === 'hang'){ ST.yr.hang = 1; save(); yrFrame(); close(); camTo(new T.Vector3(YR.at[0] + .3, .5, YR.at[2]), Math.max(cam.zoom, DEFZ() * 2.4)); toast('Ảnh kỷ niệm treo trên vách hông nhà rồi'); }
    else if (b.dataset.y === 'save') yrSave(full); }); }
function yrTick(){ try { if (VISIT || !ST.player) return; yrFrame(); if (!ST.yr && (ST.daysN || 0) >= 30 && !busy() && !document.querySelector('.yrc-scrim')) yrShow(); } catch (e) {} }
setInterval(yrTick, 1500);
window.__YR = { yrShow, yrStats, yrFrame, YR };
function navaTick(dt){"""
rep("function navaTick(dt){", JS)
CSS = r"""
/* ===== v99 Ba mươi bữa ở vườn Ngoại ===== */
.yrc-scrim{position:fixed;inset:0;background:rgba(43,30,20,.55);z-index:80;display:flex;align-items:center;justify-content:center;padding:16px;box-sizing:border-box}
.yrc{position:relative;width:min(860px,100%);max-height:100%;overflow:auto;background:#FFF8EA;border:8px solid #9A6A3C;border-radius:26px;box-shadow:0 0 0 3px #4A2F1E,0 8px 0 3px #4A2F1E,0 24px 40px rgba(0,0,0,.35);box-sizing:border-box;color:#4A2F1E;-webkit-overflow-scrolling:touch}
.yrc-h{background:linear-gradient(#B07A46,#9A6A3C);border-bottom:3px solid #4A2F1E;padding:12px 56px;text-align:center;position:relative}
.yrc-h b{display:block;font:400 30px/1.1 var(--f-game);color:#FFF8EA;text-shadow:0 3px 0 #4A2F1E}
.yrc-h span{display:block;margin-top:4px;font-weight:600;font-size:15px;color:#FCE9C8}.yrc-h em{font-style:normal;white-space:nowrap}
.yrc-x{position:absolute!important;right:12px;top:14px;z-index:2;width:40px!important;height:40px!important;border-radius:50%!important;background:radial-gradient(circle at 35% 30%,#F07A6A,#D9483A 60%,#9E2A1E)!important;color:#fff!important;box-shadow:0 0 0 3px #4A2F1E,0 3px 0 3px #4A2F1E!important;font:700 24px/40px var(--f-body)!important;text-align:center;padding:0!important}
.yrc-b{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:18px;padding:18px 20px 8px}
.yrc-ph{position:relative;align-self:start;background:#fff;padding:10px 10px 36px;box-shadow:0 0 0 2px #E3C9A6,0 6px 14px rgba(74,47,30,.25);transform:rotate(-2deg);margin:6px 4px 0}
.yrc-ph img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover}
.yrc-ph i{position:absolute;left:0;right:0;bottom:7px;text-align:center;font-weight:600;font-size:17px;color:#6B4529}
.yrc-ph::before{content:'';position:absolute;left:50%;top:-12px;width:86px;height:24px;margin-left:-43px;background:rgba(242,198,74,.75);transform:rotate(3deg)}
.yrc-st{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;align-content:start}
.yrc-s{background:#FFFBF2;border-radius:16px;box-shadow:0 0 0 2px #EBCB8F,0 3px 0 #D9B57A;padding:8px 4px 6px;text-align:center}
.yrc-s img{display:block;width:56px;height:56px;margin:0 auto}
.yrc-s b{display:block;font:400 26px/1 var(--f-game);color:#4A2F1E;margin-top:2px}
.yrc-s span{display:block;font-weight:600;font-size:13px;line-height:1.15;color:#8A5D3B;margin-top:2px}
.yrc-l{margin:6px 20px 0;padding:14px 18px 12px;background:#FCF3E0;border-radius:14px;box-shadow:inset 0 0 0 2px #EBD5AE;font-weight:600;font-size:18px;line-height:1.45;font-style:italic;color:#4A2F1E}
.yrc-l p{margin:0 0 6px}.yrc-l .sg{text-align:right;margin:0;font-style:normal;font-family:var(--f-game);font-weight:400;color:#8A5D3B}
.yrc-f{display:flex;gap:12px;justify-content:center;padding:14px 20px 20px}
.yrc-f .btn{min-width:210px;font:400 17px var(--f-game);color:#FFF8EA;padding:10px 16px 9px;text-shadow:0 2px 0 rgba(74,47,30,.6);cursor:pointer}
body.yron .nava,body.yron .ngoai{display:none!important}
@media (max-width:560px){ .yrc-b{grid-template-columns:1fr;padding:14px 14px 4px} .yrc-h{padding:10px 42px} .yrc-h b{font-size:min(19px,4.4vw);white-space:nowrap} .yrc-h span{font-size:min(13px,3.2vw)} .yrc-x{width:32px!important;height:32px!important;line-height:32px!important;font-size:20px!important;right:8px;top:12px} .yrc-st{gap:6px} .yrc-s img{width:44px;height:44px} .yrc-s b{font-size:22px} .yrc-l{margin:6px 14px 0;font-size:16px} .yrc-f{flex-direction:column;padding:12px 14px 16px} .yrc-f .btn{min-width:0} }
"""
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
