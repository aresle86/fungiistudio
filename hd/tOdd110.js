// v110: lục bình trên sông / vướng xuồng, mũi tên lần đầu cho củi + lục bình, lá rụng chỗ thấy, lục bình không vô hố ủ, bảng hố ủ có thanh.
const {chromium}=require('playwright');const fs=require('fs');fs.mkdirSync('../hud10',{recursive:true});const PAGE=process.env.PAGE||'mv2_t110.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:13,xp:9300,xu:2000,inv:{},seeds:{},plots:{},
 qd:Object.fromEntries(Array.from({length:11},(_, i)=>[i+3,1])),land:{H1:{st:'own'},H2:{st:'own'},H3:{st:'own'}},open:[],
 ho:{own:1,at:'H3',mat:3,bags:0,t:0,done:0,pct:Date.now()},ga:{hens:4,rooster:1,trough:8,eggs:0,acc:0,lv:1,brood:null,fixed:1},vit:{n:4,trough:8,eggs:0,acc:0,lv:1,fixed:1},
 odd:{list:[],acc:{}},tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
let bad=0;const ok=(c,m)=>{console.log((c?'OK ':'SAI ')+m);if(!c)bad++;};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['pc',{width:1280,height:800}],['ph',{width:390,height:664}]]){
const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});p.setDefaultTimeout(300000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded',timeout:120000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});
await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>{e.hidden=true});});
const r=await p.evaluate(()=>{const O=window.__O,L=O.ST.odd.list;L.length=0;let riv=0;for(let i=0;i<200;i++){const s=O.oddSpot('lucbinh');if(s.r)riv++;}
 L.push({k:'lucbinh',x:3.15,z:8.85,r:1},{k:'lucbinh',x:5.7,z:8.9,r:1},{k:'lucbinh',x:-.6,z:8.8,r:1},{k:'cui',x:6.6,z:-1.1},{k:'la',x:6.5,z:1.2},{k:'la',x:4.6,z:1.6});return riv;});
ok(r>120,'lục bình phần nhiều trên sông ('+r+'/200)');
await p.waitForTimeout(1500);await p.screenshot({path:`../hud10/${tag}_odd.png`});
const d=await p.evaluate(()=>{const O=window.__O,ST=O.ST,o=ST.odd.list.find(x=>x.k==='lucbinh');ST.vit.trough=ST.vit.n*2;const m0=ST.ho.mat;O.oddDo(o);return [m0,ST.ho.mat,!!ST.seen.pick_lucbinh];});
ok(d[0]===d[1]&&d[2],'lục bình không vô hố ủ ('+d+')');
await p.evaluate(()=>window.__x.openSheet('ho'));await p.waitForTimeout(700);await p.screenshot({path:`../hud10/${tag}_ho.png`});
ok(!errs.length,'không lỗi trang '+errs.join(' | '));await p.close();}
console.log(bad?'XONG · '+bad+' SAI':'XONG · tất cả đúng');await b.close();})();
