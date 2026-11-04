// Mock bộ khung chung dựng NGAY TRÊN khung gỗ cũ của game (giữ bảng, thanh việc, nút; chỉ đổi ruột): chụp pc + ph, có bảng và không bảng.
// node tKhung.js → mock/khung2_*.png
const {chromium}=require('playwright');const fs=require('fs');
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:16,xp:13400,xu:3000,inv:{oi:6},gb:{},seeds:{cai:3},plots:{},qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1,15:1,16:1},land:{H1:{st:'own'},H2:{st:'own'}},ga:{hens:4,rooster:1,trough:4,eggs:0,acc:0,lv:1,brood:null,fixed:1},tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
const CSS=`
/* ===== Mock v4 theo hd/hud-hethong.md: menu/khay giữ kiểu cũ; thẻ, nút, thanh theo hệ thống ===== */
:root{--k:#4A2F1E;--pap:#FFF8EA;--pap2:#F6EBD3;--ln:#E3C9A6;--gold:#F2C64A;--ink2:#8A5D3B;--groove:#6B4529}
#sheet{background:linear-gradient(#9A6A3C 0,#9A6A3C 34px,#FFF8EA 34px)!important}
.shH{background:#9A6A3C!important}
/* thanh việc: khung .nxq + ghim giữ, ruột 3 ô; nhãn cách ô 8px */
.nxq{max-width:none!important;width:min(392px,calc(100vw - 24px))!important;padding:18px 8px 8px!important;display:block!important;border-radius:16px!important}
.nxq>small{top:-11px!important;left:10px!important;padding:3px 9px!important;line-height:1!important;font-size:11px!important;border-radius:8px!important;border:2px solid var(--k)!important;box-shadow:0 2px 0 var(--k)!important;text-shadow:none!important}
.nxq .qrow{display:flex;gap:6px}
.nxq .q{flex:1;min-width:0;background:#fff;border:2px solid var(--k);border-radius:10px;padding:6px 5px 5px;display:flex;flex-direction:column;align-items:center;gap:4px;box-shadow:0 2px 0 var(--k)}
.nxq .q img{width:30px;height:30px}
.nxq .q .t{font:400 12px/1.1 var(--f-game);color:var(--k);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:100%}
.bar{height:14px;border-radius:6px;background:var(--groove);border:2px solid var(--k);position:relative;overflow:hidden;box-sizing:border-box}
.bar i{position:absolute;left:0;top:0;bottom:0;background:var(--gold);border-radius:4px}
.bar em{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:400 10px/1 var(--f-game);font-style:normal;color:#fff;text-shadow:1px 1px 0 var(--k),-1px 1px 0 var(--k),1px -1px 0 var(--k),-1px -1px 0 var(--k)}
.bar.s{height:10px;border-radius:4px}.bar.s i{border-radius:2px}
.nxq .q .bar{border-radius:4px}.nxq .q .bar i{border-radius:2px}
.nxq .q .bar.mini{height:12px;margin-top:2px}.nxq .q .bar.mini em{font-size:9px}
.nxq .q .more{position:absolute;right:-6px;top:-8px;background:var(--k);color:#fff;font:400 10px/16px var(--f-game);padding:0 5px;border-radius:8px}
.nxq .q{position:relative}.nxq .q>*{flex:none}
.nxq .q .tag{position:absolute;left:-6px;top:-8px;background:var(--gold);border:2px solid var(--k);color:var(--k);font:400 9px/12px var(--f-game);padding:0 5px;border-radius:7px;letter-spacing:.04em}
.nxq .q .steps{display:flex;gap:4px;height:6px;margin-top:-1px}.nxq .q .steps i{width:6px;height:6px;border-radius:50%;background:#EADBB8;border:1px solid var(--k);box-sizing:border-box}.nxq .q .steps i.on{background:var(--gold)}
.nxq .q .sub{font:600 10px/1 var(--f-body);color:var(--ink2);white-space:nowrap;overflow:hidden;max-width:100%;text-overflow:ellipsis;margin-top:-2px}
.nxq .q .bar{width:100%}
.nxq .q.done{background:#FFF0B8}
.nxq .q .claim{height:22px;box-sizing:border-box;width:100%;justify-content:center;background:var(--gold);border:2px solid var(--k);border-radius:6px;padding:0 6px;font:400 12px/1 var(--f-game);color:var(--k);display:flex;align-items:center;gap:3px;white-space:nowrap}
.nxq .q .claim img{width:13px;height:13px}
/* khay trái: badge đỏ đếm, hết thì icon mờ + nhãn vàng mua */
#tray .tn{display:none!important}
#tray .tl{position:relative!important;overflow:visible!important}
#tray .tl .cnt{position:absolute;top:-2px;right:0;min-width:20px;height:20px;padding:0 6px;border-radius:10px;background:#D9483A;border:2px solid #FBF7EE;color:#fff;font:400 12px/16px var(--f-game);text-align:center;box-sizing:border-box}
#tray .tl.empty img{opacity:.55}
#tray .tl.empty .tg{background:linear-gradient(#FFE27A,#F2C64A)!important;color:#4A2F1E!important;text-shadow:none!important}
/* ruột bảng */
#shB .mk{display:flex;flex-direction:column;gap:10px;padding-top:6px}
#shB .mst{display:flex;align-items:center;gap:12px;padding:10px;border-radius:16px;background:var(--pap2);border:2px solid var(--ln)}
#shB .mst .big{width:60px;height:60px;border-radius:10px;background:#fff;border:2px solid var(--k);display:flex;align-items:center;justify-content:center;flex:none}
#shB .mst .big img{width:48px;height:48px}
#shB .mst .r{flex:1;min-width:0}
#shB .mst h3{margin:0;font:400 20px/1.1 var(--f-game);color:var(--k);text-shadow:none}
#shB .mst .sub{display:flex;align-items:center;gap:8px;margin-top:6px;font:600 13px var(--f-body);color:var(--ink2)}
#shB .mst .sub .bar{flex:1}
#shB .cells{display:flex;gap:8px}
#shB .cell{flex:1;min-width:0;background:#fff;border:2px solid var(--k);border-radius:10px;padding:8px 6px 7px;display:flex;flex-direction:column;align-items:center;gap:5px;box-shadow:0 3px 0 var(--k)}
#shB .cell img{width:30px;height:30px}
#shB .cell b{font:400 24px/1 var(--f-game);color:var(--k)}
#shB .cell b small{font:600 13px var(--f-body);color:var(--ink2)}
#shB .cell .bar{width:100%}
#shB .cell .lb{font:600 12px var(--f-body);color:var(--ink2);text-align:center}
#shB .eggs{display:flex;gap:2px;flex-wrap:wrap;justify-content:center;height:26px;align-content:center}
#shB .eggs img{width:14px;height:14px}#shB .eggs img.o{opacity:.25;filter:grayscale(1)}
#shB .mbtn{display:flex;align-items:center;justify-content:center;gap:8px;height:50px;border-radius:10px;border:2px solid var(--k);background:#7DB84A;box-shadow:0 3px 0 var(--k);font:400 19px var(--f-game);color:#FBF7EE;text-shadow:0 1px 0 var(--k);position:relative;box-sizing:border-box}
#shB .mbtn img{width:24px;height:24px}
#shB .mbtn .cost{position:absolute;right:8px;top:50%;transform:translateY(-50%);background:rgba(0,0,0,.2);border-radius:6px;padding:2px 7px;font:600 12px var(--f-body);display:flex;align-items:center;gap:3px;text-shadow:none}
#shB .mbtn .cost img{width:14px;height:14px}
#shB .more{display:flex;gap:8px}
#shB .mbtn.w{flex:1;height:44px;font-size:16px;background:var(--pap);color:var(--k);text-shadow:none}
#shB .hint{display:flex;align-items:center;gap:8px;font:400 16px/1.3 "Patrick Hand",var(--f-body);color:var(--k);padding:0 2px;text-shadow:none}
#shB .hint .av{width:30px;height:30px;border-radius:50%;border:2px solid var(--k);background:#F3EADB;overflow:hidden;flex:none;box-sizing:border-box}
#shB .hint .av img{width:100%;height:100%;object-fit:cover;display:block}
`;
const XU='data:image/svg+xml;utf8,'+encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><circle cx="16" cy="16" r="14" fill="#F4C12E" stroke="#4A2F1E" stroke-width="3"/><circle cx="16" cy="16" r="8" fill="none" stroke="#B8860B" stroke-width="2"/></svg>');
const FILL=(I,ng,xu)=>{
 const sh=document.getElementById('shB');
 const eggO=`<img src="${I.trungga}" class="o">`.repeat(6);
 sh.innerHTML=`<div class="mk">
  <div class="mst"><div class="big"><img src="${I.mai}"></div><div class="r"><h3>Gà đang đẻ</h3><div class="sub">Trứng kế<span class="bar"><i style="width:62%"></i></span><b>2g58</b></div></div></div>
  <div class="cells">
   <div class="cell"><img src="${I.bap}"><b>4<small>/8</small></b><div class="bar s"><i style="width:50%"></i></div><div class="lb">Máng ăn · đủ 3g</div></div>
   <div class="cell"><img src="${I.trungga}"><b>0<small>/12</small></b><div class="eggs">${eggO}</div><div class="lb">Trong ổ</div></div>
   <div class="cell"><img src="${I.mai}"><b>4<small>+1</small></b><div class="eggs"><img src="${I.mai}"><img src="${I.mai}"><img src="${I.mai}"><img src="${I.mai}"><img src="${I.trong}"></div><div class="lb">Đàn · 5/6 chỗ</div></div>
  </div>
  <div class="mbtn"><img src="${I.bap}">Cho ăn<span class="cost"><img src="${xu}">6/phần</span></div>
  <div class="more"><div class="mbtn w"><img src="${I.mai}">Mua gà mái</div><div class="mbtn w"><img src="${I.trungga}">Ấp 1 trứng</div></div>
 </div>`;
 const q=document.getElementById('nxq');
 if(q){q.hidden=false;q.style.display='block';q.innerHTML=`<small>NGOẠI NHỜ</small><div class="qrow">
  <div class="q lv"><span class="tag">CẤP</span><img src="${I.caro}"><div class="t">Đào ao cá</div><div class="bar"><i style="width:0"></i><em>0/1</em></div><div class="steps"><i class="on"></i><i></i></div></div>
  <div class="q"><img src="${I.gio}"><div class="t">Đan 1 giỏ</div><div class="bar"><i style="width:0"></i><em>0/1</em></div></div>
  <div class="q done"><img src="${I.raumuong}"><div class="t">Gieo 2 liếp</div><div class="claim"><img src="${xu}">+65 Nhận</div><span class="more">+3</span></div></div>`;}
 const tr=document.getElementById('tray');if(tr){const ts=document.getElementById('tSeed'),rm=document.getElementById('tRom');if(ts&&!ts.querySelector('.cnt')){const c=document.createElement('i');c.className='cnt';c.textContent='3';ts.appendChild(c);}if(rm){rm.classList.add('empty');rm.querySelector('.tg').textContent='+ 5 xu';}}
};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['pc',{width:1280,height:800}],['ph',{width:390,height:664}]]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});p.setDefaultTimeout(180000);
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/mv2_t107.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(2500);
 await p.evaluate(c=>{window.__XU='data:image/svg+xml;utf8,'+encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><circle cx="16" cy="16" r="14" fill="#F4C12E" stroke="#4A2F1E" stroke-width="3"/><circle cx="16" cy="16" r="8" fill="none" stroke="#B8860B" stroke-width="2"/></svg>');window.__stop=true;document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>{e.hidden=true});const st=document.createElement('style');st.textContent=c;document.body.appendChild(st);},CSS);
 await p.evaluate(()=>window.__x.openSheet('ga'));await p.waitForTimeout(500);
 await p.evaluate((f)=>{const I=window.__x.ICON;const ng=document.getElementById('ngoaiImg').src;eval('('+f+')')(I,ng,window.__XU);const q=document.getElementById('nxq');if(q){q.style.setProperty('display','none','important');}},FILL.toString());
 await p.waitForTimeout(400);await p.screenshot({path:`mock/khung2_${tag}.png`});
 await p.evaluate(()=>{document.getElementById('shX').click();});await p.waitForTimeout(500);
 await p.evaluate((f)=>{const I=window.__x.ICON;const ng=document.getElementById('ngoaiImg').src;const q=document.getElementById('nxq');document.body.classList.remove('sheeton');eval('('+f+')')(I,ng,window.__XU);},FILL.toString());
 await p.waitForTimeout(400);await p.screenshot({path:`mock/khung2_${tag}_vuon.png`});
 await p.close();}
console.log('khung2 done');await b.close();})();
