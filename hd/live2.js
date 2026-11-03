const {chromium}=require('playwright');(async()=>{const [,,out,w,h,hours,q]=process.argv;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:+w,height:+h},deviceScaleFactor:1});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));p.on('console',m=>{if(['error','warning'].includes(m.type()))errs.push(m.type()+' '+m.text().slice(0,200))});
await p.addInitScript(q=>{try{localStorage.setItem('mv3d-play','0');localStorage.setItem('mv3d-q',q)}catch(e){}},q||'2');
const t0=Date.now();await p.goto('http://127.0.0.1:8777/live_test2.html');await p.waitForFunction(()=>window.__ready,{timeout:240000});console.log('ready',(Date.now()-t0)/1000);
await p.evaluate(()=>{window.__stop=true});await p.waitForTimeout(1500);
for(const hh of hours.split(',')){const ms=await p.evaluate(h=>{window.__set(+h);const t=performance.now();for(let i=0;i<4;i++)window.__tick();return (performance.now()-t)/4;},hh);await p.waitForTimeout(300);await p.screenshot({path:out+'_'+hh+'.png',timeout:120000});console.log(hh,'frame ms',ms.toFixed(0));}
console.log(await p.evaluate(()=>JSON.stringify(window.__r.info.render)+' tris; geoms '+window.__r.info.memory.geometries));console.log(errs.slice(0,15).join('\n'));await b.close();})();
