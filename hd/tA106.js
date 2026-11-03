const {chromium}=require('playwright');
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:16,xp:13400,xu:3000,inv:{oi:6,chuoi:4,cai:6},gb:{cui:4},seeds:{cai:3},plots:{},
 qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1,15:1,16:1},
 land:{H1:{st:'own'},H2:{st:'own'},H3:{st:'own'},H4:{st:'own'},H5:{st:'own'},H6:{st:'own'},H7:{st:'own'},H8:{st:'own'}},open:['H5'],
 nong:{own:1,at:'H2',trays:[null,null,null,null],done:3,made:{otkho:1}},khap:{own:1,at:'H3',jars:[null,null],done:2,made:{dacai:1}},
 dc:{rao:'rao_tre',ga:'ga_tre',vit:'vit_mac',own:{},bag:{sanh:1},items:[{k:'cong_tre',at:'H4'}]},
 ft:{vusua:{st:2,told:2,t:Date.now()-1e8}},fishLog:{caro:{n:1},caloc:{n:2}},buom:{bu_phuong:1},realTime:true,spd:1,real:Date.now(),dd:{last:(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date()),n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['pc',{width:1280,height:800}],['ph',{width:390,height:664}]]){
const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});const errs=[];await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());p.on('pageerror',e=>errs.push('ERR '+e.message+' @ '+(e.stack||'').split('\n').slice(1,3).join(' ')));p.setDefaultTimeout(180000);
await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
await p.goto('http://127.0.0.1:8777/mv2_t106.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(1500);
const shot=async n=>{await p.waitForTimeout(500);await p.screenshot({path:`../a106_${tag}_${n}.png`,timeout:180000});};
const ev=(f,a)=>p.evaluate(f,a);
await ev(()=>{window.__w.openBook('viec')});await shot('1viec');
await ev(()=>{window.__w.openBook('ca')});await shot('2bst_ca');
// bấm chip Cổ tích
await p.click('.bkchip:has-text("Cổ tích")');await shot('3bst_cotich');
const t=await ev(()=>[...document.querySelectorAll('.bkt')].map(x=>x.getAttribute('aria-label')+':'+x.className).join(' | '));console.log(tag,'tabs',t);
const ch=await ev(()=>[...document.querySelectorAll('.bkchip')].map(x=>x.textContent+(x.classList.contains('on')?'*':'')).join(','));console.log(tag,'chips',ch);
await p.click('.bkchip:has-text("Giống")');await shot('4bst_giong');
// bấm tab Kho rồi Bộ sưu tập: nhớ chip cuối
await p.click('.bkt[data-k="kho"]');await p.click('.bkt[aria-label="Bộ sưu tập"]');console.log(tag,'resume',await ev(()=>document.querySelector('.bkchip.on')&&document.querySelector('.bkchip.on').textContent));
// dời cây từ sổ
await p.click('.bkchip:has-text("Cổ tích")');const mv=await p.$('.bkmv');console.log(tag,'movebtn',!!mv);if(mv){await mv.click();await shot('5move_bar');console.log(tag,'SUA',await ev(()=>JSON.stringify(window.__U.SUA)), await ev(()=>document.querySelector('#suaBar').innerText.replace(/\n/g,' / ')));
 await p.click('#suaOk');console.log(tag,'after cancel',await ev(()=>JSON.stringify(window.__U.SUA)+' bar hidden '+document.querySelector('#suaBar').hidden));}
await ev(()=>{window.__w.closeBook();window.__g.openSheet('cho');window.__U.SHEET.tab='tiem';window.__U.renderSheet();});await shot('6cho_tiem');
console.log(tag,'seg',await ev(()=>[...document.querySelectorAll('.sg')].map(x=>x.textContent).join(',')));
await ev(()=>window.__g.closeSheet());
// chạm thẳng đồ kiểng: chiếu tâm ô H4 ra màn hình rồi bấm
const tapCell=async id=>{await ev(id=>{const {cam,PV,T}=window.__g;window.__e.camTo(new T.Vector3(PV[id].cx,.3,PV[id].cz),cam.zoom);},id);await p.waitForTimeout(2500);const xy=await ev(id=>{const {cam,PV,T}=window.__g;const v=new T.Vector3(PV[id].cx,.15,PV[id].cz).project(cam);return [(v.x+1)/2*innerWidth,(1-v.y)/2*innerHeight];},id);
 await ev(()=>window.__e.camTo&&0);if(tag==='ph') await p.touchscreen.tap(xy[0],xy[1]); else await p.mouse.click(xy[0],xy[1]);await p.waitForTimeout(700);return xy;};
await ev(()=>{const {cam,PV,T}=window.__g;window.__e.camTo(new T.Vector3(PV.H4.cx,.3,PV.H4.cz),cam.zoom*1.3);});await p.waitForTimeout(1500);
console.log(tag,'tap H4 at',await tapCell('H4'),'sheet',await ev(()=>window.__U.SHEET&&window.__U.SHEET.kind+':'+document.querySelector('#shT').textContent));await shot('7tap_deco');
await ev(()=>window.__g.closeSheet());
console.log(tag,'tap H2',await tapCell('H2'),'sheet',await ev(()=>window.__U.SHEET&&window.__U.SHEET.kind+':'+document.querySelector('#shT').textContent));
await ev(()=>window.__g.closeSheet());
console.log(tag,'tap H6 (đất trống)',await tapCell('H6'),'sheet',await ev(()=>window.__U.SHEET&&window.__U.SHEET.kind+':'+document.querySelector('#shT').textContent));await shot('8tap_own');
await ev(()=>window.__g.closeSheet());
// liếp trống: vòng gieo có nút san
await ev(()=>window.__G.openRing('H5','seed'));await shot('9ring_san');console.log(tag,'ring san',await ev(()=>!!document.querySelector('[data-r="san"]')));
await p.click('[data-r="san"]');console.log(tag,'after san open',await ev(()=>JSON.stringify(window.__g.ST.open)+' '+JSON.stringify(window.__g.ST.land.H5)));
// đặt đồ kiểng từ túi: thanh đặt + chạm ô
await ev(()=>window.__U.suaOn(true,'dc:sanh'));await shot('10place_bar');console.log(tag,'bar',await ev(()=>document.querySelector('#suaBar').innerText.replace(/\n/g,' / ')),'bSua hidden',await ev(()=>document.querySelector('#bSua').hidden));
await tapCell('H7');console.log(tag,'placed',await ev(()=>JSON.stringify(window.__g.ST.dc.items)+' SUA '+JSON.stringify(window.__U.SUA)+' bar hidden '+document.querySelector('#suaBar').hidden));
console.log(tag,errs.join('\n')||'no errors');await p.close();}
await b.close();})();
