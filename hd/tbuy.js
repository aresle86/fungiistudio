const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const save=JSON.stringify({v:1,eco:2,split:1,open:['A1','A1b','A2','B1','B1b','B2'],fg:{cai:1},xu:300,inv:{rom:1,cai:3},seeds:{cai:1},lu:0,gt:9000,real:Date.now(),spd:1,ovr:12,realTime:false,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'Nhu',garden:'Nhu'},lv:1,xp:9,qd:{},plots:{}});
const p=await b.newPage({viewport:{width:390,height:844},isMobile:true,hasTouch:true});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(800);
await p.evaluate(()=>{window.__stop=true;window.__g.openSheet('cho');});await p.waitForTimeout(200);
console.log(await p.evaluate(()=>{document.querySelector('[data-a=buyrom][data-n="5"]').click();return [document.querySelectorAll('.buyl').length,document.querySelectorAll('img.fly').length,window.__g.ST.inv.rom]}));await p.waitForTimeout(120);await p.screenshot({path:'qc2/buy.png'});
// idle queue: open fan, trigger level up via xp, check ngoai deferred
await p.evaluate(()=>{window.__g.closeSheet();document.getElementById('tSeed').click();window.__x.levelUp(2);});await p.waitForTimeout(600);
const a=await p.evaluate(()=>[document.getElementById('ngoai').hidden,document.getElementById('ngoaiTxt').textContent.slice(0,30)]);
await p.evaluate(()=>{document.getElementById('tSeed').click();});await p.waitForTimeout(2600);
const c=await p.evaluate(()=>[document.getElementById('ngoai').hidden,document.getElementById('ngoaiTxt').textContent.slice(0,40)]);
// open book while fan open
await p.evaluate(()=>{document.getElementById('tSeed').click();window.__x.openBook('giong');});await p.waitForTimeout(200);
const d=await p.evaluate(()=>[document.getElementById('fan').hidden,document.body.classList.contains('fanon')]);
console.log('during fan',a,'after close',c,'book',d,errs);await b.close();})();
