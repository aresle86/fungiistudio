const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:1});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=20;g.ST.seen.hello=1;g.ST.xu=900;document.querySelectorAll('.ddt').forEach(e=>e.remove());window.__stop=true;for(let i=0;i<10;i++)window.__tick();document.getElementById('tSeed').click();});
await p.waitForTimeout(500);
const st=()=>p.evaluate(()=>{const sc=document.querySelector('#fan .fsc');return [Math.round(sc.scrollLeft),sc.scrollWidth,sc.clientWidth,document.body.classList.contains('tooling'),!document.getElementById('fan').hidden];});
console.log('open',JSON.stringify(await st()));
const r=await p.evaluate(()=>{const e=document.querySelectorAll('#fan .sk')[2].getBoundingClientRect();return [e.x+e.width/2,e.y+e.height/2]});
// vuốt ngang lệch lên chút (kiểu ngón tay): không được bốc hạt
await p.mouse.move(r[0],r[1]);await p.mouse.down();for(let i=1;i<=8;i++){await p.mouse.move(r[0]-i*22,r[1]-i*3);}await p.mouse.up();await p.waitForTimeout(600);
console.log('diag swipe',JSON.stringify(await st()));
// kéo hẳn lên: bốc hạt
const r2=await p.evaluate(()=>{const e=document.querySelectorAll('#fan .sk')[1].getBoundingClientRect();return [e.x+e.width/2,e.y+e.height/2]});
await p.mouse.move(r2[0],r2[1]);await p.mouse.down();for(let i=1;i<=6;i++)await p.mouse.move(r2[0]+i,r2[1]-i*20);
console.log('up drag tooling',await p.evaluate(()=>document.body.classList.contains('tooling')||document.body.classList.contains('drag')));await p.mouse.up();
// phủ rơm: task
const m=await p.evaluate(()=>{const g=window.__g;const T=g.ST.tasks;let x=T.list.find(y=>y.t==='mulch');if(!x){T.list[0]={t:'mulch',txt:'Phủ rơm kín các liếp',need:1,rw:['coin',15],have:0,done:false};x=T.list[0];}
 const G=window.__G;const beds=G.PLOTS.filter(P=>!P.tree&&!P.trellis&&g.ST.plots[P.id]&&g.ST.open.includes?true:true);
 const out={before:[x.have,x.need,x.done]};for(const id in g.ST.plots){const P=G.PL[id];if(P&&!P.tree&&!P.trellis)g.ST.plots[id].mulch=g.ST.gt+99999;}
 return out;});
await p.waitForTimeout(3500);
console.log('mulch',JSON.stringify(m),await p.evaluate(()=>{const x=window.__g.ST.tasks.list.find(y=>y.t==='mulch');return JSON.stringify([x.have,x.need,x.done,x.cl,x.txt]);}));
console.log(errs.join('\n')||'no errors');await b.close();})();
