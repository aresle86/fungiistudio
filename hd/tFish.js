const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:780},isMobile:true,hasTouch:true,deviceScaleFactor:2});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='warning')errs.push(m.text())});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
const shot=async n=>{const u=await p.evaluate(()=>{window.__r.render(window.__S,window.__g.cam);return window.__r.domElement.toDataURL('image/png');});fs.writeFileSync('../'+n+'.png',Buffer.from(u.split(',')[1],'base64'));};
const r=await p.evaluate(async()=>{const g=window.__g,ST=g.ST,F=window.__FM,o={};ST.player={av:1,name:'Na',garden:'V'};ST.lv=9;ST.qd=ST.qd||{};for(let i=2;i<=9;i++)ST.qd[i]=1;document.querySelectorAll('.lvup,#intro').forEach(e=>e.hidden=true);window.__stop=true;
F.fmEnter();o.on=F.FM.on;for(let i=0;i<40;i++)window.__tick();o.sh=F.FSH.list.length;o.ui=document.querySelector('.fui').innerText.slice(0,80);
const results=[];for(let round=0;round<6;round++){const s=F.FSH.list[0];F.fmCast(s.m.position.x,s.m.position.z);let guard=0;while(F.FM.ph!=='bite'&&F.FM.ph!=='aim'&&F.FM.ph!=='done'&&guard<4000){F.fmTick(guard*.016,.05);guard++;}
 const ph1=F.FM.ph;if(ph1==='bite'){F.fmTap(0,0);F.FM.hold=true;guard=0;while(F.FM.ph==='reel'&&guard<4000){F.FM.hold=F.FM.ten<.7;F.fmTick(guard*.016,.05);guard++;}}results.push(ph1+'>'+F.FM.ph);if(F.FM.ph==='done')F.FM.ph='aim';}
o.res=results;o.log=JSON.stringify(ST.fishLog);o.inv=Object.entries(ST.inv).filter(([k])=>F.FISHK[k]).map(([k,n])=>k+':'+n).join(',');o.left=ST.cau.n;return o;});
console.log(JSON.stringify(r));
await p.evaluate(()=>{const F=window.__FM;F.fmExit();F.fmEnter();for(let i=0;i<30;i++)window.__tick();const s=F.FSH.list[0];F.fmCast(s.m.position.x,s.m.position.z);for(let i=0;i<60;i++)F.fmTick(i*.03,.03);});
await p.evaluate(()=>{const c=window.__ctl,F=window.__FM;const d=c.object.position.clone().sub(c.target);c.target.set(2.2,.2,9.4);c.object.position.copy(c.target).add(d);c.object.zoom=2.4;c.object.updateProjectionMatrix();});
await shot('fish_view');await p.screenshot({path:'../fish_ui.png',timeout:60000}).catch(()=>{});
await p.evaluate(()=>window.__FM.fmCatch('caloc'));await p.waitForTimeout(400);await p.screenshot({path:'../fish_card.png',timeout:60000}).catch(()=>console.log('cardshot fail'));
await p.evaluate(()=>{window.__FM.fmExit();window.__x.openBook('ca');});await p.waitForTimeout(600);await p.screenshot({path:'../fish_book.png',timeout:60000}).catch(()=>console.log('bookshot fail'));
console.log('errs',errs.filter(e=>!/TUNNEL/.test(e)).slice(0,5));await b.close();})();
