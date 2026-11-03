const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:800,height:600}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','0')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,{timeout:240000});await p.evaluate(()=>{window.__stop=true});
const out=await p.evaluate(()=>window.__catalog());fs.mkdirSync(__dirname+'/cat',{recursive:true});for(const [k,v] of Object.entries(out))fs.writeFileSync(__dirname+'/cat/'+k+'.png',Buffer.from(v.split(',')[1],'base64'));
console.log(Object.keys(out).length);console.log(errs.join('\n'));await b.close();})();
