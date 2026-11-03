const {chromium}=require('playwright');(async()=>{const [,,out]=process.argv;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1000,height:700}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',JSON.stringify({v:1,eco:2,xu:100,inv:{rom:2},seeds:{cai:1},gt:9000,real:Date.now(),spd:1,realTime:false,ovr:12,seen:{hello:1},player:{av:0,name:'A',garden:'B'},lv:6,xp:360,qd:{2:1,5:1,6:1},exp:1,plots:{}}));}}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;window.__g.openSheet('set');});
for(let i=0;i<6;i++){await p.click('[data-a=lvup]');await p.waitForTimeout(200);}
await p.click('[data-a=xu1k]');
console.log(JSON.stringify(await p.evaluate(()=>({lv:window.__g.ST.lv,xu:window.__g.ST.xu,seeds:window.__g.ST.seeds,vis:['T1','T5'].map(k=>window.__g.PV[k].root.visible)}))));
await p.evaluate(()=>{for(let i=0;i<2;i++)window.__tick();});await p.screenshot({path:out});
await p.click('[data-a=lvdn]');console.log(await p.evaluate(()=>window.__g.ST.lv+' '+window.__g.PV.T5.root.visible));
console.log(errs.join('\n'));await b.close();})();
