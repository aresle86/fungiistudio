const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
for(const [w,h,n,cl] of [[1280,800,'d',''],[390,844,'m',''],[844,390,'ml','']]){const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:1});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1');window.__keepLoad=1}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html',{waitUntil:'commit'});await p.waitForTimeout(3500);
await p.evaluate(cl=>{const l=document.getElementById('load');if(l){l.hidden=false;l.classList.remove('out','done');const i=l.querySelector('.lbar i');i.style.setProperty('--p','41%');l.querySelector('.lpc').textContent='41%';if(cl)l.classList.add(cl);}},cl);
await p.screenshot({path:'../ld_'+n+'.png',timeout:120000}).catch(e=>console.log('fail',e.message.slice(0,80)));await p.close();}
await b.close();})();
