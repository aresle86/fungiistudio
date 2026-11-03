const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const url=process.argv[2];const p=await b.newPage({viewport:{width:1440,height:860},deviceScaleFactor:1});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/'+url,{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=10;g.ST.seen.hello=1;g.ST.xu=900;document.querySelectorAll('.ddt').forEach(e=>e.remove());for(let i=0;i<10;i++)window.__tick();window.__stop=true;});

const tr=await p.evaluate(()=>{const e=document.getElementById('tSeed').getBoundingClientRect();return [e.x+e.width/2,e.y+e.height/2,getComputedStyle(document.getElementById('tSeed')).visibility];});console.log('tSeed',tr);
await p.mouse.click(tr[0],tr[1]);await p.waitForTimeout(600);
const st=()=>p.evaluate(()=>{const sc=document.querySelector('#fan .fsc');if(!sc)return 'nofan';const r=document.getElementById('fan').getBoundingClientRect();return [Math.round(sc.scrollLeft),sc.scrollWidth,sc.clientWidth,Math.round(r.x),Math.round(r.width),document.querySelectorAll('#fan .sk').length];});
console.log('open',JSON.stringify(await st()));
const r=await p.evaluate(()=>{const e=document.querySelectorAll('#fan .sk')[3].getBoundingClientRect();return [e.x+e.width/2,e.y+e.height/2]});
await p.mouse.move(r[0],r[1]);await p.mouse.down();for(let i=1;i<=10;i++)await p.mouse.move(r[0]-i*25,r[1]-i*2.5);await p.mouse.up();await p.waitForTimeout(300);console.log('drag',JSON.stringify(await st()),await p.evaluate(()=>document.body.classList.contains('tooling')));
await p.mouse.move(r[0],r[1]);await p.mouse.wheel(0,400);await p.waitForTimeout(300);console.log('wheel',JSON.stringify(await st()));
const hit=await p.evaluate(([x,y])=>{const e=document.elementFromPoint(x,y);return e?e.className+'|'+(e.closest('#fan')?'infan':'out'):'none'},r);console.log('hit',hit);
console.log(errs.join('\n')||'no errors');await b.close();})();
