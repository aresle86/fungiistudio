const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});const p=await b.newPage({viewport:{width:390,height:740},deviceScaleFactor:2,hasTouch:true});
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
await p.addInitScript(()=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',JSON.stringify({v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:11,xp:7600,xu:500,inv:{},seeds:{cai:3},plots:{},qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1},tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now()}))});
await p.goto('http://127.0.0.1:8777/mv2_t112a.html',{timeout:300000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(1500);
await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>e.hidden=true);window.__x.openBook('viec')});await p.waitForTimeout(800);
console.log(await p.evaluate(()=>{const out=[];for(const e of document.querySelectorAll('#bk *, #bk')){const cs=getComputedStyle(e);if((cs.overflowY==='auto'||cs.overflowY==='scroll')&&e.scrollHeight>e.clientHeight+2){const r=e.getBoundingClientRect();out.push({tag:e.tagName,id:e.id,cls:e.className,top:r.top,h:r.height,pt:cs.paddingTop,sh:e.scrollHeight,mask:cs.webkitMaskImage})}}
 const bk=document.getElementById('bk');return JSON.stringify({out,bk:bk&&bk.parentElement.className,kids:[...bk.children].map(c=>c.className+':'+c.getBoundingClientRect().top.toFixed(0))})}));
await p.screenshot({path:'../hud16/bk0.png'});
await p.evaluate(()=>{for(const e of document.querySelectorAll('#bk *, #bk')){const cs=getComputedStyle(e);if((cs.overflowY==='auto'||cs.overflowY==='scroll')&&e.scrollHeight>e.clientHeight+2)e.scrollTop=130}});await p.waitForTimeout(300);
await p.screenshot({path:'../hud16/bk1.png'});await b.close();})();
