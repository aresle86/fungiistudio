const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
console.log(await p.evaluate(()=>{window.__stop=true;let n=0,h=0;window.__S.traverse(o=>{if(o.isMesh&&o.parent===window.__S||o.isGroup&&o.parent===window.__S){n++;h+=o.position.x*1.3+o.position.z*2.7+o.position.y;}});return n+' '+h.toFixed(4);}),errs.join('|'));await b.close();})();
