// Mock bảng "Ô đất trống": 4 ô lựa chọn Liếp · Cây · Giàn · Đồ, chạm một ô thì hiện phần chọn bên dưới. Chụp 4 trạng thái.
const {chromium}=require('playwright');const fs=require('fs');fs.mkdirSync('../hud15',{recursive:true});const PAGE=process.env.PAGE||'mv2_t110e.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:13,xp:9400,xu:3000,inv:{},gb:{},seeds:{cai:3},plots:{},qd:Object.fromEntries(Array.from({length:11},(_, i)=>[i+3,1])),land:{H1:{st:'own'},H2:{st:'own'},H5:{st:'own'}},open:[],nong:{own:1,at:'H2',trays:[null,null,null,null],done:2,made:{}},tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
const CSS=`
#shB .od4{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:2px 0 12px}
#shB .od4 button{appearance:none;background:#fff;border:2px solid #4A2F1E;border-radius:10px;box-shadow:0 3px 0 #4A2F1E;padding:8px 2px 6px;display:flex;flex-direction:column;align-items:center;gap:4px;font:400 14px var(--f-game);color:#4A2F1E;cursor:pointer}
#shB .od4 button img{width:40px;height:40px}
#shB .od4 button.on{background:#FFF0B8;transform:translateY(2px);box-shadow:0 1px 0 #4A2F1E}
#shB .odp{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
#shB .odp .it{background:#fff;border:2px solid #4A2F1E;border-radius:10px;box-shadow:0 3px 0 #4A2F1E;padding:8px 4px 6px;display:flex;flex-direction:column;align-items:center;gap:3px;text-align:center}
#shB .odp .it img{width:40px;height:40px}
#shB .odp .it b{font:400 13px/1.15 var(--f-game);color:#4A2F1E;min-height:2.3em}
#shB .odp .it .pr{display:flex;align-items:center;gap:3px;font:700 12px var(--f-body);color:#8A5D3B}
#shB .odp .it .pr img{width:14px;height:14px}
#shB .odp .it.bag{background:#F3FBE9}
#shB .odh{font:400 15px var(--f-game);color:#4A2F1E;margin:0 0 8px}
#shB .odn{font:400 15px/1.35 var(--f-hand);color:#4A2F1E;margin-top:10px}
`;
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['ph',{width:390,height:664}],['pc',{width:1280,height:800}]]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});p.setDefaultTimeout(300000);
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded',timeout:300000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(1500);
 await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>{e.hidden=true});window.__x.openSheet('plot','H1');});await p.waitForTimeout(600);
 for(const mode of ['lieu','cay','gian','do']){
  await p.evaluate(([c,mode])=>{const I=window.__x.ICON,U=window.__AVIMG||{};let st=document.getElementById('odmock');if(!st){st=document.createElement('style');st.id='odmock';document.body.appendChild(st);}st.textContent=c;
   const sh=document.getElementById('shB'),coin='data:image/svg+xml;utf8,'+encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><circle cx="16" cy="16" r="14" fill="#F4C12E" stroke="#4A2F1E" stroke-width="3"/><circle cx="16" cy="16" r="8" fill="none" stroke="#B8860B" stroke-width="2"/></svg>');
   const tile=(k,ic,t)=>`<button class="${mode===k?'on':''}"><img src="${ic}">${t}</button>`;
   const it=(ic,t,pr,cls='')=>`<div class="it ${cls}"><img src="${ic}"><b>${t}</b>${pr!=null?`<span class="pr">${pr===''?'':`<img src="${coin}">`}${pr===''?'trong túi':pr}</span>`:''}</div>`;
   let body='';
   if(mode==='lieu') body=`<div class="odh">Đắp liếp trồng rau</div><div class="odp">${it(I.cai,'Liếp rau','60')}</div><div class="odn">Đất phù sa, đắp liếp là gieo được liền nghe con.</div>`;
   if(mode==='cay') body=`<div class="odh">Trồng cây trái · chiếm ô này và ô dưới</div><div class="odp">${it(I.chuoi,'Chuối','40')}${it(I.oi,'Ổi','55')}${it(I.khe,'Khế','70')}${it(I.xoai,'Xoài','90')}</div><div class="odn">Cây trái trồng một lần, vụ nào cũng ra trái.</div>`;
   if(mode==='gian') body=`<div class="odh">Dựng giàn tre cho dây leo</div><div class="odp">${it(I.khoqua,'Giàn khổ qua','120')}</div><div class="odn">Cần 2 cây tre. Giàn dựng rồi trồng dây leo hoài được.</div>`;
   if(mode==='do') body=`<div class="odh">Đặt đồ · trong túi</div><div class="odp">${it(I.khap,'Khạp muối','','bag')}${it(I.nong,'Nong thứ hai','','bag')}${it(I.ho,'Hố ủ phân','','bag')}</div><div class="odh" style="margin-top:12px">Mua thêm ở Chợ</div><div class="odp">${it(I.khap,'Khạp thứ hai','350')}${it(I.say,'Lò sấy','600')}${it(I.ong||I.matong,'Thùng ong','500')}</div>`;
   sh.innerHTML=`<div class="uxh"><div class="hi"><img src="${I.cuoc}"></div><div class="tx"><b>Đất của con</b><span>Chọn làm gì trên ô này</span></div></div><div class="od4">${tile('lieu',I.cai,'Liếp')}${tile('cay',I.xoai,'Cây')}${tile('gian',I.khoqua,'Giàn')}${tile('do',I.khap,'Đồ')}</div>${body}`;},[CSS,mode]);
  await p.waitForTimeout(400);await p.screenshot({path:`../hud15/${tag}_${mode}.png`});}
 await p.close();}
console.log('od mock done');await b.close();})();
