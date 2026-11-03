const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:844},hasTouch:true,isMobile:true});p.on('pageerror',e=>console.log('ERR',e.message));await p.addInitScript(()=>{try{localStorage.clear()}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});await p.evaluate(()=>{window.__stop=true;window.__tick();});
await p.waitForTimeout(1200);await p.evaluate(()=>window.__tick());
const pos=async()=>await p.evaluate(()=>JSON.stringify([document.querySelector('#bSo').getBoundingClientRect().top, !document.querySelector('#ngoai').hidden]));
console.log(await pos());await p.screenshot({path:'qcm1.png',timeout:120000});
await p.evaluate(()=>{document.querySelector('#ngoai').hidden=true;});console.log(await pos());
await p.tap('#tSeed');await p.waitForTimeout(300);await p.screenshot({path:'qcm2.png',timeout:120000});await b.close();})();
