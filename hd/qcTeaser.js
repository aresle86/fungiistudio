// Kiểm phần "không báo trước cấp sau": thẻ Ngoại nhờ, túi hạt, Sổ giống, bong bóng liềm, bảng đất, cảnh tổng.
const fs=require('fs');const {chromium}=require('playwright');const OUT=process.argv[2];
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:844},isMobile:true,hasTouch:true,deviceScaleFactor:2});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','0')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const setup=async(xu)=>p.evaluate((xu)=>{window.__stop=true;const g=window.__g,w=window.__w,ST=g.ST;ST.player={av:1,name:'Như',garden:'V'};
 document.querySelectorAll('#intro,#lvup,.lvup,#ngoai,.ddt').forEach(e=>{e.hidden=true;e.classList&&e.classList.remove('on');});window.LVON=false;document.body.classList.remove('lvon');
 ST.lv=6;ST.xp=452;ST.xu=xu;ST.qd={2:1,3:1,4:1,5:1,6:1};ST.ga.fixed=1;ST.vit=ST.vit||{};ST.vit.fixed=1;ST.tm='fixed';ST.ovr=9.5;
 try{w.openBook('viec');w.closeBook();}catch(e){} ST.tasks.list.forEach(x=>{x.done=1;x.have=x.need;});w.hud();w.nxq();for(let i=0;i<4;i++)window.__tick();
 let bub=0;for(const P of window.__x.PLOTS){const v=window.__g.PV[P.id];if(v&&v.want==='d')bub++;}return bub;},xu);
const r={};
r.bubLiem_58xu=await setup(58);
await p.waitForTimeout(300);try{await p.screenshot({path:`${OUT}/t_canh_58xu.png`,timeout:45000});}catch(e){}
r.card=await p.evaluate(()=>document.getElementById('nxq').innerText.replace(/\s+/g,' '));
r.bubLiem_500xu=await setup(500);
// túi hạt
r.fan=await p.evaluate(()=>{const b=document.querySelector('[data-b="seed"],#bSeed,#bHat')||[...document.querySelectorAll('button')].find(x=>/Hạt/.test(x.innerText));if(b)b.click();for(let i=0;i<2;i++)window.__tick();const f=document.getElementById('fan');return f?{shown:!f.hidden,locks:f.querySelectorAll('.sk.lock').length,items:[...f.querySelectorAll('.sk b')].map(x=>x.innerText).join('|')}:null;});
await p.waitForTimeout(300);try{await p.screenshot({path:`${OUT}/t_tuihat.png`,timeout:45000});}catch(e){}
await p.evaluate(()=>{const f=document.getElementById('fan');if(f)f.hidden=true;});
// Sổ giống
r.giong=await p.evaluate(()=>{window.__w.openBook('giong');for(let i=0;i<2;i++)window.__tick();const bk=document.getElementById('book');return {locks:bk.querySelectorAll('.stk.lock').length,cap:(bk.innerText.match(/Mở ở cấp \d+/g)||[]).length,items:[...bk.querySelectorAll('.stk b')].map(x=>x.innerText).join('|')};});
await p.waitForTimeout(300);try{await p.screenshot({path:`${OUT}/t_sogiong.png`,timeout:45000});}catch(e){}
await p.evaluate(()=>window.__w.closeBook());
// chữ "cấp" còn hiện ở đâu trên màn chính + các bảng ở cấp 6
r.capText=await p.evaluate(()=>{const g=window.__g,out=[];const scan=(n)=>{const t=document.body.innerText;for(const m of t.matchAll(/[^\n]{0,30}(Tới cấp|Mở ở cấp|cấp \d+ mới|lên cấp \d+)[^\n]{0,30}/g))out.push(n+': '+m[0].trim());};scan('màn chính');
 for(const k of ['cho','ga','vit','bep','nong','khap','set','ben']){try{g.openSheet(k);window.__tick();scan('bảng '+k);g.closeSheet();}catch(e){}}
 for(const t of ['giong','kho','viec','cotich']){try{window.__w.openBook(t);window.__tick();scan('Sổ '+t);window.__w.closeBook();}catch(e){}}return [...new Set(out)];});
console.log(JSON.stringify(r,null,1));console.log('errs',errs);await b.close();})();
