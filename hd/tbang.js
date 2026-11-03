const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const save=JSON.stringify({v:1,eco:2,split:1,open:['A1','A1b','A2','B1','B1b','B2'],fg:{cai:1},xu:150,inv:{rom:3},seeds:{cai:2},lu:0,gt:9000,real:Date.now(),spd:1,seen:{hello:1,sold:1},player:{av:2,name:'Nhu',garden:'Nhu'},lv:2,xp:40,qd:{},plots:{},realTime:false,ovr:12});
const p=await b.newPage({viewport:{width:900,height:600}});
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(1500);
console.log(await p.evaluate(()=>[...document.querySelectorAll('body *')].filter(e=>e.textContent.trim()==='!'&&e.children.length===0&&e.offsetParent).map(e=>{const r=e.getBoundingClientRect();return [e.tagName,e.id,e.className,e.parentElement.id,e.parentElement.className,Math.round(r.x),Math.round(r.y)]})));
await b.close();})();
