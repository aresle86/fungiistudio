// Mock Sổ theo hd/hud-hethong.md: tab thẻ đánh dấu sách (một chữ + icon, màu khu), tiêu đề là bảng tên, thẻ việc trắng viền mực, nút "Đi làm" phụ.
// Chỉ chèn CSS + đổi chữ tab để chụp duyệt, không sửa game. node tSo.js → ../hud12/<pc|ph>_<viec|kho>.png
const {chromium}=require('playwright');const fs=require('fs');fs.mkdirSync('../hud12',{recursive:true});const PAGE=process.env.PAGE||'mv2_live110b.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:12,xp:7600,xu:3000,inv:{oi:6,cai:6,trungga:4},gb:{cui:4,muoi:2},seeds:{cai:3},plots:{},qd:Object.fromEntries(Array.from({length:10},(_, i)=>[i+3,1])),tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
const CSS=`
:root{--k:#4A2F1E;--pap:#FFF8EA;--ink2:#8A5D3B}
/* tab: thẻ đánh dấu sách thò mép, icon + một chữ, màu khu; tab mở to hơn, liền trang */
.bktabs{gap:8px!important}
.bkt{border:2px solid var(--k)!important;box-shadow:0 3px 0 var(--k)!important;text-shadow:none!important;color:var(--k)!important;font:400 14px/1 var(--f-game)!important;filter:none!important;padding:0!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;gap:3px!important}
.bkt img{filter:none!important;width:36px!important;height:36px!important;margin:0!important}
.bkt span{display:block!important;font-size:13px!important}
.bkt.off{opacity:1!important;filter:saturate(.55) brightness(1.08)!important}
.bkt[data-k="viec"]{background:#F6B49F!important}.bkt[data-k="kho"]{background:#F5D27A!important}.bkt[data-k="giong"]{background:#B9D79F!important}
@media (min-width:561px){
 .bktabs{left:calc(100% - 4px)!important;right:auto!important;top:40px!important;bottom:auto!important;flex-direction:column!important;align-items:flex-start!important}
 .bkt{border-radius:0 12px 12px 0!important;border-left:0!important}
 .bkt.on{width:92px!important;height:76px!important}.bkt.off{width:78px!important;height:66px!important}
}
@media (max-width:560px){
 .bktabs{flex-direction:row!important;align-items:flex-end!important}
 .bkt{border-radius:12px 12px 0 0!important;border-bottom:0!important}
 .bkt.on{width:88px!important;height:66px!important}.bkt.off{width:74px!important;height:56px!important}
}
/* tiêu đề trang: bảng tên màu khu, chữ mực */
.bkhd{transform:none!important;margin:0 0 6px!important;padding:4px 14px 4px 6px!important;border:2px solid var(--k);border-radius:10px!important;box-shadow:0 3px 0 var(--k)!important}
.bkhd img{filter:none!important;width:34px!important;height:34px!important;margin:0!important}
.bkhd b{text-shadow:none!important;color:var(--k)!important;font-size:20px!important}
.uxt{color:var(--k)!important;font-size:15px!important}
.uxt small{color:var(--ink2)!important;font:600 12px var(--f-body)!important}
/* thẻ việc cấp */
.qcd{background:#fff!important;box-shadow:0 3px 0 var(--k)!important;border:2px solid var(--k);border-radius:10px!important;position:relative}
.qcd{column-gap:10px}.qcd .qg{display:flex!important;align-items:center;gap:10px;margin:8px 0 0 -54px!important}.qcd .qg img{width:24px;height:24px;flex:none;margin:0 10px}.qcd .qg span{flex:1}
.qcd .mbar{margin-left:0!important;width:100%!important}   /* icon phần việc nằm dưới cột icon lớn, chữ thẳng mép trái với tiêu đề */
.qcd>img{width:44px!important;height:44px!important}
/* thẻ việc hôm nay */
.tkc{background:#fff!important;box-shadow:0 3px 0 var(--k)!important;border:2px solid var(--k);border-radius:10px!important;padding:8px 10px!important;margin-bottom:10px!important}
.tkc>img{width:40px!important;height:40px!important;flex:none}
.tkc .tt b{font:400 15px/1.15 var(--f-game);color:var(--k)}
.tkc .tt span{color:var(--ink2)!important;font-weight:600!important}
.tkc{position:relative;align-items:flex-start!important}
.tkc>img{margin-top:2px}
.tkc .tt{padding-right:84px}
.tkc .tt .mbar{margin-top:5px!important}
.tkc .rw{position:absolute;right:10px;top:10px;width:72px;height:24px;box-sizing:border-box;justify-content:center;padding:0 4px!important}
.tkc .tkgo{position:absolute;right:10px;bottom:10px;margin:0!important;background:var(--pap)!important;color:var(--k)!important;border:2px solid var(--k)!important;border-radius:8px!important;box-shadow:0 2px 0 var(--k)!important;font:400 12px/1 var(--f-game)!important;padding:0!important;min-height:0!important;height:24px!important;width:72px!important;box-sizing:border-box;display:inline-flex!important;align-items:center!important;justify-content:center!important}
.tkc{min-height:72px;box-sizing:border-box}
.tkc .tt{padding-right:84px!important}
.tkc .rw{background:#FFF3C4;border:2px solid var(--k);border-radius:8px;padding:2px 7px 2px 3px;color:var(--k)!important}
.tkc.done{background:#EEF7E4!important}
.tkc.bonus{background:#FFF8E0!important}
.mbar,.uxh .bar{height:10px!important;border-radius:4px!important;background:#6B4529!important;border:2px solid var(--k);box-sizing:border-box}
.mbar i,.uxh .bar i{background:#F2C64A!important;border-radius:2px!important}
`;
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['pc',{width:1280,height:800}],['ph',{width:390,height:664}]]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});p.setDefaultTimeout(300000);
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded',timeout:120000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(1500);
 await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>{e.hidden=true});});
 for(const tab of ['viec','kho']){
  await p.evaluate(([c,t])=>{window.__w.openBook(t);let st=document.getElementById('somock');if(!st){st=document.createElement('style');st.id='somock';document.body.appendChild(st);}st.textContent=c;
   const L={viec:'Việc',kho:'Kho',giong:'Sưu tập'};document.querySelectorAll('.bkt').forEach(x=>{const s=x.querySelector('span');if(s)s.textContent=L[x.dataset.k]||s.textContent;});
   const IC=window.__x.ICON,map=[[/bón|phân/i,'phan'],[/phơi|sấy/i,'nong'],[/trứng/i,'trungga'],[/cá|câu/i,'caro'],[/ghe/i,'ghe'],[/đơn|giao/i,'cho'],[/giỏ/i,'gio'],[/hái|trái/i,'xoai'],[/liếp|gieo/i,'cai']];document.querySelectorAll('.qcd .qg').forEach(q=>{if(q.querySelector('img'))return;const t=q.textContent,m=map.find(([r])=>r.test(t));const im=document.createElement('img');im.src=IC[m?m[1]:'la']||'';q.prepend(im);});
   const hd=document.querySelector('.bkhd');if(hd){hd.style.setProperty('background',{viec:'#F6B49F',kho:'#F5D27A',giong:'#B9D79F'}[t],'important');}},[CSS,tab]);
  await p.waitForTimeout(700);await p.screenshot({path:`../hud12/${tag}_${tab}.png`});}
 await p.close();}
console.log('so mock done');await b.close();})();
