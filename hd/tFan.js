const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1100,height:700},deviceScaleFactor:1});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=20;g.ST.seen.hello=1;g.ST.xu=500;for(let i=0;i<10;i++)window.__tick();});
await p.evaluate(()=>document.getElementById('tSeed').click());await p.waitForTimeout(500);
const st=()=>p.evaluate(()=>{const sc=document.querySelector('#fan .fsc');const v=s=>{const e=document.querySelector(s);return e&&getComputedStyle(e).display!=='none'};return {sl:Math.round(sc.scrollLeft),sw:sc.scrollWidth,cw:sc.clientWidth,L:v('#fan .fnav.l'),R:v('#fan .fnav.r')}});
console.log('open',JSON.stringify(await st()));
await p.screenshot({path:'../fan0.png',timeout:300000});
// kéo ngang trên một thẻ bằng chuột
const r=await p.evaluate(()=>{const e=document.querySelectorAll('#fan .sk')[3].getBoundingClientRect();return [e.x+e.width/2,e.y+e.height/2]});
await p.mouse.move(r[0],r[1]);await p.mouse.down();for(let i=1;i<=10;i++)await p.mouse.move(r[0]-i*25,r[1]+2);await p.mouse.up();
console.log('drag',JSON.stringify(await st()), 'tool', await p.evaluate(()=>document.body.classList.contains('tooling')));
await p.mouse.move(r[0],r[1]);await p.mouse.wheel(0,300);await p.waitForTimeout(300);console.log('wheel',JSON.stringify(await st()));
await p.click('#fan .fnav.l');await p.waitForTimeout(800);console.log('arrowL',JSON.stringify(await st()));
await p.screenshot({path:'../fan1.png',timeout:300000});
// kéo dọc vẫn bốc hạt
const r2=await p.evaluate(()=>{const e=document.querySelectorAll('#fan .sk')[0].getBoundingClientRect();return [e.x+e.width/2,e.y+e.height/2]});
await p.mouse.move(r2[0],r2[1]);await p.mouse.down();for(let i=1;i<=6;i++)await p.mouse.move(r2[0],r2[1]-i*25);
console.log('vertical stroke',await p.evaluate(()=>document.body.classList.contains('drag')||document.body.classList.contains('tooling')));await p.mouse.up();
// lời Ngoại
const S=await p.evaluate(()=>{const Y=window.__SY,g=window.__g,out={};
 Y.say('Câu đang nói dài dài một chút cho Ngoại bận.','vui',{now:true});
 let alive=true; Y.say('Có sâu kìa','dan',{ok:()=>alive}); out.q1=Y.SAYQ.length; alive=false;
 for(let i=0;i<200;i++)window.__tick(); out.txt=document.getElementById('ngoaiTxt').textContent; out.q2=Y.SAYQ.length;
 alive=true; Y.say('Héo kìa','lo',{now:true,ok:()=>alive}); for(let i=0;i<5;i++)window.__tick(); out.showing=!document.getElementById('ngoai').hidden; alive=false; for(let i=0;i<30;i++)window.__tick(); out.after=!document.getElementById('ngoai').hidden;
 return out;});
console.log('say',JSON.stringify(S));
console.log(errs.join('\n')||'no errors');await b.close();})();
