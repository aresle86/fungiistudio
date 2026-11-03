const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:900}});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const keys=['caro','sacran','sacbuom','rophi','diec','mevinh','chot','bongcat','tep','he','caloc','catre','thatlat','keo','chach','luon','linh','lang','ngat','chep','tomcang','chanhduc','bongtuong','bonglau','tra','cadua','hu','rodauvang','locbong','caho'];
const m=await p.evaluate(ks=>{window.__stop=true;const o={};for(const k of ks)o[k]=window.__ICONS[k]||'';return o;},keys);
console.log('missing',keys.filter(k=>!m[k]));
await p.setContent('<body style="margin:0;background:#FFFBF2;display:grid;grid-template-columns:repeat(6,200px);font:14px sans-serif">'+keys.map(k=>`<div style="text-align:center;padding:4px;border:1px solid #eee"><img src="${m[k]}" width="180" height="180"><br>${k}</div>`).join('')+'</body>');
await p.screenshot({path:'../fishIcons.png',fullPage:true});await b.close();})();
