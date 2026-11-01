const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1000,height:640}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='warning'||m.type()==='error')errs.push(m.text())});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
const shot=async n=>{const u=await p.evaluate(()=>{window.__r.render(window.__S,window.__g.cam);return window.__r.domElement.toDataURL('image/png');});fs.writeFileSync('../'+n+'.png',Buffer.from(u.split(',')[1],'base64'));};
const r=await p.evaluate(()=>{window.__stop=true;const g=window.__g,ST=g.ST,X=window.__FT2,o={};ST.lv=9;ST.player={av:1,name:'Na',garden:'V'};document.querySelectorAll('.lvup,#intro').forEach(e=>e.hidden=true);g.ST.tm='fixed';g.ST.ovr=18.8;
 ST.ft.vusua={st:0,told:0,t:Date.now()};ST.kqHv=3;X.ftCheck();o.tre=JSON.stringify(ST.ft.tretramdot);
 for(let i=0;i<4;i++)window.__tick();o.vis=X.FTV.vusua.root.visible+' '+X.FTV.vusua.b.visible;
 X.ftTap('vusua');o.v1=JSON.stringify(ST.ft.vusua);
 // advance stages
 for(let s=0;s<4;s++){ST.ft.vusua.t-=13*3600e3;X.ftCheck();}o.v2=ST.ft.vusua.st;
 for(let i=0;i<5;i++)X.ftTap('vusua');o.told=ST.ft.vusua.told;X.ftTap('vusua');o.fruit=ST.inv.vusua;
 // tre
 X.ftTap('tretramdot');ST.ft.tretramdot.t-=7*3600e3;X.ftCheck();o.t2=ST.ft.tretramdot.st;X.ftTap('tretramdot');X.ftTap('tretramdot');for(let i=0;i<3;i++)window.__tick();o.dots=X.FDV.list.length;
 return o;});
console.log(JSON.stringify(r));
await p.evaluate(()=>{const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(-5.6,1.0,4.6);c.object.position.copy(c.target).add(d);c.object.zoom=1.7;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();});
await shot('ftg_dots');
const r2=await p.evaluate(async()=>{const X=window.__FT2,ST=window.__g.ST;for(const d of [...X.FDV.list]){X.fdTake(d);}for(let i=0;i<3;i++)window.__tick();for(const d of [...X.FDV.list])X.fdTake(d);for(let i=0;i<3;i++)window.__tick();const o={dot:ST.ft.tretramdot.dot};X.ftTap('tretramdot');for(let i=0;i<120;i++)window.__tick();await new Promise(r=>setTimeout(r,3000));for(let i=0;i<5;i++)window.__tick();o.st=ST.ft.tretramdot.st;o.told=ST.ft.tretramdot.told;return o;});
console.log(JSON.stringify(r2));
await shot('ftg_full');
await p.evaluate(()=>window.__x.openBook('cotich'));await p.waitForTimeout(600);await p.screenshot({path:'../ftg_book.png',timeout:90000,animations:'disabled'}).catch(()=>console.log('bookfail'));
console.log('errs',errs.filter(e=>!/TUNNEL|ERR_|Failed to load/.test(e)).slice(0,6));await b.close();})();
