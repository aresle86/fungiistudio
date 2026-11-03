const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for (const [w,h,tag] of [[1280,800,'d'],[390,844,'m']]){
const p=await b.newPage({viewport:{width:w,height:h}});p.on('pageerror',e=>console.log('ERR',tag,e.message));await p.addInitScript(()=>{try{localStorage.clear()}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});await p.evaluate(()=>{window.__stop=true;});
await p.waitForTimeout(1500);await p.evaluate(()=>{window.__tick();});
await p.click('#bSo');await p.waitForTimeout(700);await p.screenshot({path:`bk_${tag}_giong.png`});
if(tag==='m'){await p.click('.stk[data-k="ot"]');await p.waitForTimeout(300);await p.screenshot({path:`bk_${tag}_seed.png`});}
else {await p.click('.stk[data-k="bap"]');await p.waitForTimeout(300);await p.screenshot({path:`bk_${tag}_seed.png`});}
await p.click('.bkt[data-k="kho"]');await p.waitForTimeout(300);await p.screenshot({path:`bk_${tag}_kho.png`});
await p.click('.bkt[data-k="viec"]');await p.waitForTimeout(300);await p.screenshot({path:`bk_${tag}_viec.png`});
await p.click('.bkt[data-k="giong"]');await p.waitForTimeout(200);
if(tag==='m') await p.click('.stk[data-k="cai"]');
await p.click('[data-b="hold"]');await p.waitForTimeout(300);
await p.evaluate(()=>{window.__book.trySeedOn('C2');window.__tick();});await p.waitForTimeout(500);await p.screenshot({path:`bk_${tag}_hold.png`});
await p.close();}
await b.close();})();
