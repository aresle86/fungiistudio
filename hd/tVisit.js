const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for (const lv of [4]){
const p=await b.newPage({viewport:{width:390,height:700},isMobile:true,hasTouch:true,deviceScaleFactor:1});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');}}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(lv=>{const g=window.__g;g.ST.player={av:1,name:'Na',garden:'V'};g.ST.lv=lv;window.__VG();},lv);
await p.waitForTimeout(1500);await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const st=async tag=>{const r=await p.evaluate(()=>{const v=document.querySelector('.vbar'),h=document.getElementById('vHome');if(!h)return 'NO vHome';const R=h.getBoundingClientRect(),e=document.elementFromPoint(R.x+R.width/2,R.y+R.height/2);return JSON.stringify({n:document.querySelectorAll('.vbar').length,r:[R.x|0,R.y|0,R.width|0,R.height|0],vis:getComputedStyle(v).display+'/'+getComputedStyle(v).visibility,top:e===h||h.contains(e)?'ok':(e&&(e.id||e.className))})});console.log(lv,tag,r);};
await st('load');await p.waitForTimeout(4000);await st('4s');
for (const [x,y] of [[205,350],[235,400],[120,370],[300,355]]){await p.touchscreen.tap(x,y);await p.waitForTimeout(1200);await st('tap'+x);await p.screenshot({path:'vis_t'+x+'.png',timeout:120000});}
console.log(errs.slice(0,5).join('\n'));await p.close();}
await b.close();})();
