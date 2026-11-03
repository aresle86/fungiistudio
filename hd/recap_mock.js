/* hình mẫu "Một năm ở vườn Ngoại": tiêm vào trang game chạy thật, dùng icon và font của game */
window.__recapMock = (photo, S) => {
  const I = window.__ICONS, U = window.__UIC, A = window.__AVIMG || {};
  const css = `
@font-face{font-family:"Patrick Hand";src:url(./node_modules/@fontsource/patrick-hand/files/patrick-hand-vietnamese-400-normal.woff2);unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB}
@font-face{font-family:"Patrick Hand";src:url(./node_modules/@fontsource/patrick-hand/files/patrick-hand-latin-400-normal.woff2)}
.yrc-scrim{position:fixed;inset:0;background:rgba(43,30,20,.55);z-index:80;display:flex;align-items:center;justify-content:center;padding:16px;box-sizing:border-box}
.yrc{position:relative;width:min(860px,100%);max-height:100%;overflow:auto;background:#FFF8EA;border:8px solid #9A6A3C;border-radius:26px;box-shadow:0 0 0 3px #4A2F1E,0 8px 0 3px #4A2F1E,0 24px 40px rgba(0,0,0,.35);box-sizing:border-box;font-family:"Baloo 2",system-ui,sans-serif;color:#4A2F1E}
.yrc-h{background:linear-gradient(#B07A46,#9A6A3C);border-bottom:3px solid #4A2F1E;padding:12px 18px 12px;text-align:center;position:relative}
.yrc-h b{display:block;font:400 30px/1.1 "Paytone One";color:#FFF8EA;text-shadow:0 3px 0 #4A2F1E}
.yrc-h span{display:block;margin-top:4px;font-weight:600;font-size:15px;color:#FCE9C8}
.yrc-h::before,.yrc-h::after{content:'';position:absolute;top:50%;width:14px;height:14px;margin-top:-7px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#FF8A7A,#D9483A 55%,#8E2418)}
.yrc-h::before{left:16px}.yrc-h::after{right:16px}
.yrc-b{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:18px;padding:18px 20px 8px}
.yrc-ph{position:relative;align-self:start;background:#fff;padding:10px 10px 34px;box-shadow:0 0 0 2px #E3C9A6,0 6px 14px rgba(74,47,30,.25);transform:rotate(-2deg);margin:6px 4px 0}
.yrc-ph img{display:block;width:100%;aspect-ratio:4/3;object-fit:cover}
.yrc-ph i{position:absolute;left:0;right:0;bottom:6px;text-align:center;font:400 19px "Baloo 2",system-ui,sans-serif;font-style:italic;font-style:normal;color:#6B4529}
.yrc-ph::before{content:'';position:absolute;left:50%;top:-12px;width:86px;height:24px;margin-left:-43px;background:rgba(242,198,74,.75);transform:rotate(3deg)}
.yrc-st{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;align-content:start}
.yrc-s{background:#FFFBF2;border-radius:16px;box-shadow:0 0 0 2px #EBCB8F,0 3px 0 #D9B57A;padding:8px 4px 6px;text-align:center}
.yrc-s img{display:block;width:56px;height:56px;margin:0 auto}
.yrc-s b{display:block;font:400 26px/1 "Paytone One";color:#4A2F1E;margin-top:2px}
.yrc-s span{display:block;font-weight:600;font-size:13px;line-height:1.15;color:#8A5D3B;margin-top:2px}
.yrc-l{margin:6px 20px 0;padding:14px 18px 12px;background:#FCF3E0;border-radius:14px;box-shadow:inset 0 0 0 2px #EBD5AE;font:600 18px/1.4 "Baloo 2",system-ui,sans-serif;font-style:italic;color:#4A2F1E}
.yrc-l p{margin:0 0 6px}
.yrc-l .sg{text-align:right;margin:0}
.yrc-f{display:flex;gap:12px;justify-content:center;padding:14px 20px 20px}
.yrc-f .btn{min-width:200px;font:400 17px "Paytone One";color:#FFF8EA;padding:10px 16px 9px;text-shadow:0 2px 0 rgba(74,47,30,.6);display:inline-flex;align-items:center;justify-content:center;gap:8px;cursor:pointer}
.yrc-f .btn img{width:30px;height:30px}
@media (max-width:560px){ .yrc-b{grid-template-columns:1fr;padding:14px 14px 4px} .yrc-h b{font-size:24px} .yrc-st{gap:6px} .yrc-s img{width:44px;height:44px} .yrc-s b{font-size:22px} .yrc-l{margin:6px 14px 0;font-size:18px} .yrc-f{flex-direction:column;padding:12px 14px 16px} .yrc-f .btn{min-width:0} }
`;
  const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  const stat = (img, n, t) => `<div class="yrc-s"><img src="${img}" alt=""><b>${n}</b><span>${t}</span></div>`;
  const d = document.createElement('div'); d.className = 'yrc-scrim';
  d.innerHTML = `<div class="yrc" role="dialog" aria-label="Một năm ở vườn Ngoại">
  <div class="yrc-h"><b>Một năm ở vườn Ngoại</b><span>Vườn ${S.garden} · ${S.days} ngày về vườn</span></div>
  <div class="yrc-b">
    <div class="yrc-ph"><img src="${photo}" alt="Ảnh vườn"><i>Vườn nhà mình, ngày thứ ${S.days}</i></div>
    <div class="yrc-st">
      ${stat(I.cai, S.harv, 'Rổ rau đã hái')}
      ${stat(I.xoai, S.tree, 'Vụ cây trái')}
      ${stat(I.caro, S.fish, 'Loài cá câu được')}
      ${stat(I.canhchuaca, S.cook, 'Nồi Ngoại nấu')}
      ${stat(U.bu_trangcai, S.bu, 'Loài bướm ghé')}
      ${stat(A.banbe || I.cai, S.guest, 'Lượt bạn ghé')}
    </div>
  </div>
  <div class="yrc-l"><p>Con về với Ngoại tròn một năm rồi đó. Ba mươi bữa con về, mình hái ${S.harv} rổ rau, câu được ${S.fish} loài cá, nấu ${S.cook} nồi canh nồi kho ăn chung.</p><p>Vườn mình giờ bướm về đậu, bạn bè ghé chơi, cây trái ra đều. Ngoại già rồi, thấy con thương đất thương cây vầy là Ngoại mừng lắm.</p><p class="sg">Ngoại</p></div>
  <div class="yrc-f"><button class="btn g">Treo ảnh trong nhà</button><button class="btn">Lưu hình</button></div>
</div>`;
  document.body.appendChild(d);
};
