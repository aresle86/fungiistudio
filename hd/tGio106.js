// v106 giỏ lục bình: lục bình mọc riêng dưới mương, vịt chỉ ăn khi máng trống, vớt lên gác bếp đếm x/5, đem phơi từ hiên, đan giỏ
// dựng trang: cat x40f.js x106.js xpop.js > /tmp/x.js; python3 gen_test2.py /tmp/x.js live/v106a.html lp/mv2_t106.html
const {chromium}=require('playwright');
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:15,xp:13300,xu:3000,inv:{},gb:{lucbinh:3},seeds:{},plots:{},
 qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1,15:1},
 land:{H1:{st:'own'},H2:{st:'own'},H3:{st:'own'}},open:[],nong:{own:1,at:'H2',trays:[null,null,null,null],done:3,made:{otkho:1}},
 vit:{n:12,trough:10,eggs:0,acc:0,lv:2,fixed:1},odd:{list:[],acc:{}},realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});let bad=0;
for(const [tag,vw] of [['ph',{width:390,height:664}],['pc',{width:1280,height:800}]]){
const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.setDefaultTimeout(180000);
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
await p.goto('http://127.0.0.1:8777/mv2_t106.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(1500);
const ev=(f,a)=>p.evaluate(f,a);const ok=(c,m)=>{console.log(`${tag} ${c?'OK ':'SAI'} ${m}`);if(!c) bad++;};
const shot=async n=>{await p.waitForTimeout(400);await p.screenshot({path:`../gio_${tag}_${n}.png`});};
// 1) 8 tiếng vắng nhà, mọc từng phút: lục bình có chỗ riêng, tối đa 4 bụi
const sp=await ev(()=>{const g=window.__g;for(let i=0;i<8*60;i++) g.sim(60);const L=g.ST.odd.list;return {lb:L.filter(o=>o.k==='lucbinh').length,bo:L.filter(o=>o.k!=='lucbinh').length};});
ok(sp.lb===4,`sau 8 tiếng: ${sp.lb} bụi lục bình (mong 4), ${sp.bo} việc trên bờ (≤4)`);ok(sp.bo<=4,'việc trên bờ vẫn tối đa 4');
// 2) máng còn đồ ăn: lục bình lên gác bếp, không vô máng vịt
const r2=await ev(()=>{const g=window.__g,C=window.__C;g.ST.vit.trough=10;const t0=g.ST.vit.trough;for(let i=0;i<2;i++){const o=g.ST.odd.list.find(o=>o.k==='lucbinh');try{C.oddDo(o);}catch(e){return {err:e.message+' '+(e.stack||'').split('\n')[1]};}}return {lb:g.ST.gb.lucbinh,tr:g.ST.vit.trough,t0,seen:!!g.ST.seen.lbgb,s5:!!g.ST.seen.lb5};});
if(r2.err) console.log(tag,'LỖI oddDo',r2.err);ok(r2.lb===5&&r2.tr===r2.t0,`máng ${r2.t0} phần: 2 bụi lên gác bếp (gác bếp ${r2.lb}, máng ${r2.tr})`);ok(r2.seen&&r2.s5,'Ngoại dặn đem phơi (lbgb) và đủ 5 bó (lb5)');
// 3) máng trống: lục bình vô máng vịt
const r3=await ev(()=>{const g=window.__g,C=window.__C;g.ST.vit.trough=0;const o=g.ST.odd.list.find(o=>o.k==='lucbinh');C.oddDo(o);return {lb:g.ST.gb.lucbinh,tr:g.ST.vit.trough};});
ok(r3.tr===1&&r3.lb===5,`máng trống: bụi thứ 3 vô máng vịt (máng ${r3.tr}, gác bếp ${r3.lb})`);
// 4) bảng hiên nhà: đủ tươi, nút đem phơi
await ev(()=>window.__g.openSheet('gio'));await shot('1du_tuoi');
const b4=await ev(()=>({btn:!!document.querySelector('[data-a=giophoi]'),hero:document.querySelector('#sheet').innerText.split('\n').slice(0,4).join(' / ')}));
ok(b4.btn,`có nút đem phơi · ${b4.hero}`);
await p.click('[data-a=giophoi]');await p.waitForTimeout(500);
const r5=await ev(()=>{const g=window.__g;return {tray:JSON.stringify(g.ST.nong.trays.find(t=>t&&t.k==='lucbinhkho')),lb:g.ST.gb.lucbinh||0,hero:document.querySelector('#sheet').innerText.split('\n').slice(0,3).join(' / ')};});
ok(r5.tray&&r5.tray.includes('10800')&&r5.lb===0,`trải ra nong (${r5.tray}), gác bếp còn ${r5.lb} · ${r5.hero}`);await shot('2dang_phoi');
// 5) khô rồi: lấy ở nong, đan giỏ
const r6=await ev(()=>{const g=window.__g;const T=g.ST.nong.trays.find(t=>t&&t.k==='lucbinhkho');T.t=0;g.closeSheet();g.openSheet('nong');return 1;});
await p.click('[data-a=ntakeall]');await p.waitForTimeout(400);
await ev(()=>{window.__g.closeSheet();window.__g.openSheet('gio');});await shot('3du_kho');
const r7=await ev(()=>({kho:window.__g.ST.gb.lucbinhkho,put:!!document.querySelector('[data-a=gioput]:not([disabled])')}));
ok(r7.kho===5&&r7.put,`lấy về 5 bó khô (${r7.kho}), nút nhờ Ngoại đan bật`);
await p.click('[data-a=gioput]');await p.waitForTimeout(400);
const r8=await ev(()=>({on:window.__g.ST.gio.on,kho:window.__g.ST.gb.lucbinhkho}));ok(r8.on===1&&r8.kho===0,'Ngoại bắt đầu đan, dùng 5 bó khô');
// 6) cấp dưới mở giỏ: lục bình như cũ (2 bụi), vịt ăn trước
console.log(tag,errs.length?'ERR '+errs.join(' | '):'no errors');if(errs.length) bad++;await p.close();}
console.log('DONE',bad,'chỗ sai');await b.close();})();
