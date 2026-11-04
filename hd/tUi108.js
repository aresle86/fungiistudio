// chụp v108a: vườn (thẻ Ngoại nhờ, khay), chuồng gà, và các bảng khác để soát hệ thống mới. PAGE=mv2_t108.html node tUi108.js
const {chromium}=require('playwright');const fs=require('fs');fs.mkdirSync('../hud8',{recursive:true});
const PAGE=process.env.PAGE||'mv2_t108.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:16,xp:13400,xu:3000,inv:{oi:6,chuoi:4,cai:6},gb:{cui:4},seeds:{cai:3},plots:{},
 qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1,15:1,16:1},land:{H1:{st:'own'},H2:{st:'own'},H3:{st:'own'}},open:['H1'],
 nong:{own:1,at:'H2',trays:[null,null,null,null],done:3,made:{}},ga:{hens:4,rooster:1,trough:4,eggs:0,acc:0,lv:1,brood:null,fixed:1},vit:{n:6,trough:8,eggs:0,acc:0,lv:1,fixed:1},
 tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
const STEPS=[['vuon',()=>{}],['ga',()=>window.__x.openSheet('ga')],['vit',()=>window.__x.openSheet('vit')],['cho',()=>window.__x.openSheet('cho')],['nong',()=>window.__x.openSheet('nong')],['plot',()=>window.__x.openSheet('plot',window.__x.PLOTS[0].id)],['set',()=>window.__x.openSheet('set')],['ao',()=>window.__x.openSheet('big','ao')]];
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['ph',{width:390,height:664}],['pc',{width:1280,height:800}]]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});p.setDefaultTimeout(180000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(2500);
 await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>{e.hidden=true});});
 for(const [n,f] of STEPS){try{await p.evaluate(f);}catch(e){console.log(tag,n,'ERR',e.message.slice(0,100));}await p.waitForTimeout(600);await p.screenshot({path:`../hud8/${tag}_${n}.png`});
  try{await p.evaluate(()=>{const x=document.getElementById('shX');if(x&&!document.getElementById('sheet').hidden)x.click();});}catch(e){}await p.waitForTimeout(300);}
 // trạng thái hết rơm, hết hạt
 await p.evaluate(()=>{window.__g.ST.inv.rom=0;window.__g.ST.seeds={};window.__w.hud();});await p.waitForTimeout(400);await p.screenshot({path:`../hud8/${tag}_vuon_het.png`});
 console.log(tag,'errors:',errs.length,errs.slice(0,3));await p.close();}
console.log('ui108 shots done');await b.close();})();
