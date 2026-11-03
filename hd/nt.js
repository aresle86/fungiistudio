const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for (const [w,h,tag,hr] of [[1100,760,'d',20.5]]){
const p=await b.newPage({viewport:{width:w,height:h}});p.on('pageerror',e=>console.log('ERR',e.message));await p.addInitScript(()=>{try{localStorage.clear()}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});
await p.evaluate(h=>{window.__stop=true;const g=window.__g;g.ST.realTime=false;g.ST.ovr=h;document.querySelector('#ngoai').hidden=true;window.__tick();window.__tick();},hr);
await p.screenshot({path:`nt_${tag}.png`,timeout:120000});await p.close();}
await b.close();})();
