const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1300,height:800}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const r=await p.evaluate(()=>{const g=window.__g,ST=g.ST,X=window.__FT2,o={};document.getElementById('intro').style.display='none';ST.player={av:1,name:'Na',garden:'V'};ST.lv=18;ST.xp=4300;
 ST.kheHv=5;ST.duaHv=3;X.ftCheck();o.k=JSON.stringify([ST.ft.khevang,ST.ft.sodua,ST.ft.duahau]);
 const song=window.__x.PLOTS.filter(P=>P.zone==='song').map(P=>P.id);o.song=song.length;if(song[0]&&!ST.open.includes(song[0]))ST.open.push(song[0]);ST.plots[song[0]]=ST.plots[song[0]]||{};ST.plots[song[0]].crop=null;
 ST.dhN='2026-1-1';X.ftCheck();o.dh=JSON.stringify(ST.ft.duahau);
 for(const k of ['duahau','khevang','sodua']){X.ftTap(k);const F=ST.ft[k];F.st=3;F.told=1;X.ftTell(k);X.ftTell(k);o[k]=JSON.stringify(F);}
 const x0=ST.inv.duahau||0;X.ftTap('duahau');o.dua=(ST.inv.duahau||0)-x0;X.ftTap('khevang');o.vang=ST.vang;X.ftTap('khevang');o.vang2=ST.vang;
 const P=window.__x.PLOTS.find(P=>ST.open.includes(P.id)&&/^A/.test(P.id));g.act.plant(P.id,'cai');ST.plots[P.id].moist=0;ST.sdW=0;window.__FT3.sdHelp();o.watered=ST.plots[P.id].moist;
 ST.xu=100;o.pay=window.__FT3.dcPay(250,'test');o.after=[ST.xu,ST.vang];
 o.q=[14,15,16,17,18,19,20].map(n=>{const q=window.__x&&0;return n;});
 for(let i=0;i<5;i++)window.__tick();return o;});
console.log(JSON.stringify(r,null,1));
await p.evaluate(()=>{window.__stop=true;const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(-5.5,.5,6.5);c.object.position.copy(c.target).add(d);c.object.zoom=1.2;c.object.updateProjectionMatrix();for(let i=0;i<4;i++)window.__tick();});

await p.evaluate(()=>window.__OB('cotich'));await p.waitForTimeout(400);console.log(await p.evaluate(()=>{const d=document.createElement('div');d.innerHTML=window.__FT2.pgCotich(0);return d.innerText.slice(-1500);}));await p.screenshot({path:'../ft6b.png',timeout:120000}).catch(()=>console.log('shotfail'));
await p.evaluate(()=>{window.__g.ST.lv=13;window.__g.ST.qd={};window.__OB('viec');});await p.waitForTimeout(300);console.log(await p.evaluate(()=>document.querySelector('.uxbk')?.innerText.slice(0,200)));
console.log(errs.join('\n'));await b.close();})();
