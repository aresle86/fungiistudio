const {chromium}=require('playwright');(async()=>{const [,,w,h,out]=process.argv;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:+w,height:+h}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000}).catch(()=>console.log('notready',errs));await p.waitForTimeout(1000);
await p.evaluate(()=>{window.__stop=true;const g=window.__g;g.ST.realTime=false;g.ST.ovr=12;g.act.harvest('B2');g.say('Trời, được tới 12 bó lận!','nhay');for(let i=0;i<3;i++)window.__tick();});
await p.waitForTimeout(3500);await p.screenshot({path:out,timeout:180000});console.log(errs.join('\n'));await b.close();})();
