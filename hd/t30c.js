const {chromium}=require('playwright');(async()=>{const [,,out]=process.argv;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:300}});await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;document.body.innerHTML='<div id=gg style="background:#FBF7EE;display:flex;gap:10px;padding:10px"></div>';for(const k of ['daubap','mongtoi','duahau','cuc','maichau','lixi','chuoi'])document.getElementById('gg').innerHTML+=`<img src="${window.__x.ICON[k]}" width=150>`;});
await p.waitForTimeout(300);await p.screenshot({path:out});await b.close();})();
