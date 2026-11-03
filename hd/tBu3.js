const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1000,height:640}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
const T0=Date.now();await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});console.log('ready',Date.now()-T0);
const r=await p.evaluate(()=>{window.__stop=true;const g=window.__g,ST=g.ST,X=window.__BU,o={};ST.lv=9;ST.player={av:1,name:'Na',garden:'V'};document.querySelectorAll('.lvup,#intro').forEach(e=>e.hidden=true);
 o.kinds=X.buKinds();for(let i=0;i<600;i++)window.__tick();o.n=X.BUV.list.length;o.ks=X.BUV.list.map(b=>b.k).join(',');
 if(X.BUV.list[0]){X.buCatch(X.BUV.list[0]);}o.buom=JSON.stringify(ST.buom);
 const b0=X.BUV.list[1];if(b0){const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.copy(b0.m.position);c.object.position.copy(c.target).add(d);c.object.zoom=5;c.object.updateProjectionMatrix();b0.rest=5;}
 for(let i=0;i<3;i++)window.__tick();window.__r.render(window.__S,g.cam);o.u=window.__r.domElement.toDataURL('image/png');return o;});
fs.writeFileSync('../buom.png',Buffer.from(r.u.split(',')[1],'base64'));delete r.u;console.log(JSON.stringify(r),Date.now()-T0);console.log('ob',await p.evaluate(()=>typeof (window.__x||{}).openBook));
await p.evaluate(()=>window.__x.openBook('buom'));await p.waitForTimeout(500);await p.screenshot({path:'../buom_book.png',timeout:90000,animations:'disabled'}).catch(()=>console.log('bookfail'));
console.log('errs',errs.filter(e=>!/TUNNEL|ERR_|Failed to load/.test(e)).slice(0,6));await b.close();})();
