const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});const p=await b.newPage({viewport:{width:800,height:600}});p.on('pageerror',e=>console.log('ERR',e.message));p.on('console',m=>{if(m.type()==='error')console.log('CE',m.text())});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,{timeout:300000});
const r=await p.evaluate(()=>{const c=document.getElementById('coinic');return [c.width, c.toDataURL().length, document.querySelectorAll('canvas').length]});console.log(r);
const d=await p.evaluate(()=>document.getElementById('coinic').toDataURL());require('fs').writeFileSync('qc2/coinc.png',Buffer.from(d.split(',')[1],'base64'));await b.close();})();
