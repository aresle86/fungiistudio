const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [w,h,tag] of [[390,844,'m'],[1280,800,'d']]){const p=await b.newPage({viewport:{width:w,height:h}});p.on('pageerror',e=>console.log('ERR',e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{const g=window.__g;g.ST.player={av:1,name:'Na',garden:'V'};g.ST.lv=12;g.ST.xu=999;document.querySelectorAll('.lvup,#intro').forEach(e=>e.hidden=true);});
let best='';for(const k of ['set','nong','khap','lo','ga','bep','ho','gio','ben','visit']){const sh=await p.evaluate(k=>{try{window.__x.openSheet(k);}catch(e){return -1}const s=document.getElementById('shB');return s.scrollHeight-s.clientHeight;},k);console.log(k,sh);if(sh>100&&!best)best=k;}
await p.evaluate(k=>window.__x.openSheet(k),best||'set');await p.waitForTimeout(800);const r=await p.evaluate(()=>{const s=document.getElementById('shB');s.scrollTop=140;window.__stop=true;return [s.scrollHeight,s.clientHeight,document.getElementById('sheet').scrollHeight,document.getElementById('sheet').clientHeight];});console.log(tag,r);
await p.waitForTimeout(400);await p.screenshot({path:`../sh_${tag}.png`});await p.close();}
await b.close();})();
