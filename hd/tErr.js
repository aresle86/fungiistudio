const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:600,height:400}});p.on('pageerror',e=>console.log('PERR',e.message));p.on('console',m=>{if(m.type()!=='log')console.log('C',m.type(),m.text().slice(0,200))});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});try{await p.waitForFunction(()=>window.__ready,{timeout:150000});console.log('READY');}catch(e){console.log('NOTREADY',await p.evaluate(()=>document.querySelector('#load small')&&document.querySelector('#load small').textContent));}
await b.close();})();
