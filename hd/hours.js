const {chromium}=require('playwright');(async()=>{const [,,out,hs]=process.argv;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1440,height:900}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','2')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});await p.waitForTimeout(1200);await p.evaluate(()=>{window.__stop=true;});await p.waitForTimeout(200);
for(const h of hs.split(',')){await p.evaluate(h=>{const g=window.__g;g.ST.realTime=false;g.ST.ovr=+h;document.querySelector('#ngoai').hidden=true;for(let i=0;i<3;i++)window.__tick();},h);await p.waitForTimeout(300);await p.screenshot({path:out+'_'+h+'.png',timeout:180000});}
console.log(errs.join('\n'));await b.close();})();
