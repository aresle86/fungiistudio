// dò vì sao chữ tab Sổ không mở (off) trên điện thoại không hiện khi áp tabso.css
const {chromium}=require('playwright');const fs=require('fs');
const CSS=fs.readFileSync('tabso.css','utf8');
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:16,xp:13400,xu:3000,inv:{cai:6},seeds:{cai:3},plots:{},qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1,15:1,16:1},realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:664},deviceScaleFactor:2,hasTouch:true});p.setDefaultTimeout(180000);
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
await p.goto('http://127.0.0.1:8777/mv2_t107.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(800);
await p.evaluate(c=>{const st=document.createElement('style');st.textContent=c;document.body.appendChild(st);},CSS);await p.evaluate(()=>window.__w.openBook('kho'));await p.waitForTimeout(500);
console.log(await p.evaluate(()=>[...document.querySelectorAll('.bkt')].map(t=>{const s=t.querySelector('span'),c=s&&getComputedStyle(s),r=s&&s.getBoundingClientRect();return {cls:t.className,html:t.innerHTML.slice(0,80),span:s?{text:s.textContent,fs:c.fontSize,disp:c.display,color:c.color,w:Math.round(r.width),h:Math.round(r.height),op:c.opacity,vis:c.visibility}:null,btn:{w:Math.round(t.getBoundingClientRect().width),fs:getComputedStyle(t).fontSize,ov:getComputedStyle(t).overflow}}})));
await b.close();})();
