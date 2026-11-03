const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for (const [w,h,mob,n] of [[1000,640,false,'bk_d'],[390,780,true,'bk_m']]){const p=await b.newPage({viewport:{width:w,height:h},isMobile:mob,hasTouch:mob});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;const ST=window.__g.ST;ST.player={av:1,name:'Na',garden:'V'};document.querySelectorAll('.lvup,#intro').forEach(e=>e.hidden=true);ST.lv=1;ST.buom={trangcai:2,phuong:1};window.__x.openBook('buom');});await p.waitForTimeout(600);
await p.screenshot({path:'../'+n+'.png',timeout:90000,animations:'disabled'}).catch(()=>console.log('fail',n));await p.close();}
await b.close();})();
