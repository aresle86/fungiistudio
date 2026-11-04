// chụp quyển Sổ với tab làm lại (tabso.css) để gửi duyệt: máy tính + điện thoại, tab Kho đang mở và tab Việc đang mở
// dựng trang: python3 gen_test2.py /tmp/x.js live/v107a.html lp/mv2_t107.html
const {chromium}=require('playwright');const fs=require('fs');
const CSS=fs.readFileSync('tabso.css','utf8');
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:16,xp:13400,xu:3000,inv:{oi:6,chuoi:4,cai:6},gb:{cui:4},seeds:{cai:3},plots:{},
 qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1,15:1,16:1},fishLog:{caro:{n:1}},realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['pc',{width:1280,height:800}],['ph',{width:390,height:664}]]) for(const css of [0,1]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});p.setDefaultTimeout(180000);
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/mv2_t107.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(800);
 if(css) await p.evaluate(c=>{const st=document.createElement('style');st.textContent=c;document.body.appendChild(st);},CSS);
 await p.evaluate(()=>window.__w.openBook('kho'));await p.waitForTimeout(500);await p.screenshot({path:`../tabso_${tag}_${css?'moi':'cu'}_kho.png`});
 await p.evaluate(()=>window.__w.openBook('viec'));await p.waitForTimeout(500);await p.screenshot({path:`../tabso_${tag}_${css?'moi':'cu'}_viec.png`});
 await p.close();}
console.log('shots done');await b.close();})();
