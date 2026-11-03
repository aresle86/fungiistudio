const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:430,height:860}});const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=9;window.__FT3.fmEnter();});await p.waitForTimeout(6000);
const a=await p.evaluate(()=>{const e=document.querySelector('.ddt');return !!(e&&e.classList.contains('on'))});
await p.evaluate(()=>window.__FT3.fmExit());await p.waitForTimeout(4000);
const c=await p.evaluate(()=>{const e=document.querySelector('.ddt');return !!(e&&e.classList.contains('on'))});
console.log('trong lúc câu hiện:',a,' · thoát câu rồi hiện:',c,errs.join('|'));await b.close();})();
