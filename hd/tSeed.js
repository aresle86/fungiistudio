const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:400}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const r=await p.evaluate(async()=>{window.__stop=true;const u=window.__UIC.seedbag;return [u,await window.__FT3.sticker(u)];});
await p.setContent('<body style="margin:0;background:#86B06A;display:flex;gap:40px;align-items:end;padding:20px"><img src="'+r[0]+'" width="260" style="background:#FFF8EA;border-radius:12px"><img src="'+r[1]+'" width="160"><img src="'+r[1]+'" width="80"><img src="'+r[1]+'" width="54"></body>');
await p.screenshot({path:'../seed.png'});console.log(errs.join('|')||'no errors');await b.close();})();
