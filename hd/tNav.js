const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:430,height:860},deviceScaleFactor:2});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));p.on('console',m=>{if(/nav/.test(m.text()))errs.push(m.text())});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').hidden=true;document.getElementById('intro').style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=6;g.ST.xp=900;g.ST.tm='fixed';g.ST.ovr=10;g.ST.seen.hello=1;});
const run=n=>p.evaluate(n=>{for(let i=0;i<n;i++)window.__tick();},n);
await run(30);await p.waitForTimeout(800);
// kéo camera đi xa (góc trái) để các bong bóng nằm ngoài khung
await p.evaluate(()=>{const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(-5,0,-1.5);c.object.position.copy(c.target).add(d);c.object.zoom=1.8;c.object.updateProjectionMatrix();});
await run(5);await p.waitForTimeout(700);await run(3);await p.screenshot({path:'../nav_arrows.png',timeout:120000});
const arr=await p.evaluate(()=>[...document.querySelectorAll('.nava')].filter(e=>!e.hidden).map(e=>[e.style.left,e.style.top,e.querySelector('b').textContent]));console.log('arrows',JSON.stringify(arr));
const card=await p.evaluate(()=>{window.__FT3.nxq();const e=document.getElementById('nxq');return [e.hidden,e.dataset.a,e.textContent.slice(0,60)]});console.log('card',JSON.stringify(card));
// chạm mũi tên đầu tiên
if(arr.length){await p.click('.nava:not([hidden])',{force:true});for(let i=0;i<40;i++){await run(1);await p.waitForTimeout(16);}await p.screenshot({path:'../nav_after_arrow.png',timeout:120000});}
// chạm thẻ việc
await p.evaluate(()=>{const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(-5,0,-1.5);c.object.position.copy(c.target).add(d);});await run(5);
await p.evaluate(()=>window.__FT3.nxq());await p.click('#nxq',{force:true});for(let i=0;i<40;i++){await run(1);await p.waitForTimeout(16);}await p.waitForTimeout(300);await run(2);await p.screenshot({path:'../nav_after_card.png',timeout:120000});
console.log('after card',await p.evaluate(()=>{const g=window.__g;return JSON.stringify({tool:document.body.classList.contains('tooling'),target:window.__ctl.target.toArray().map(x=>+x.toFixed(2)),sheet:!document.getElementById('sheet')||document.getElementById('sheet').hidden?0:1})}));
for(const [t,k] of [['water',''],['plant',''],['harvest','hanh']]){await p.evaluate(([t,k])=>{const c=window.__ctl;c.target.set(-5,0,-1.5);document.body.classList.remove('tooling');window.__FT3.taskGo(t,k);},[t,k]);for(let i=0;i<40;i++){await run(1);await p.waitForTimeout(16);}await p.waitForTimeout(300);await run(2);await p.screenshot({path:'../nav_'+t+'.png',timeout:120000});console.log(t,await p.evaluate(()=>window.__ctl.target.toArray().map(x=>+x.toFixed(2))));}
// từng loại việc
console.log('tasks',await p.evaluate(()=>JSON.stringify(window.__g.ST.tasks.list.map(x=>[x.t,x.k,x.txt]))));
await p.evaluate(()=>{window.__g.ST.lv=2;window.__FT3.hud();window.__FT3.nxq();});await run(2);console.log('card2',await p.evaluate(()=>document.getElementById('nxq').dataset.a));await p.click('#nxq',{force:true});await p.waitForTimeout(1200);await run(3);await p.screenshot({path:'../nav_book.png',timeout:120000});
console.log(errs.join('\n')||'no errors');await b.close();})();
