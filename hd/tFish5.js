const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:600}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='warning'||m.type()==='error')errs.push(m.text())});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
const r=await p.evaluate(async()=>{window.__stop=true;const g=window.__g,ST=g.ST,F=window.__FM,o={};ST.lv=9;ST.player={av:1,name:'Na',garden:'Vườn Na'};document.querySelectorAll('.lvup,#intro').forEach(e=>e.hidden=true);
 o.moon=F.moonAge().toFixed(1)+' '+F.trang();o.nuoc=F.nuoc();o.wk=F.wkKey();
 // cá hô: force rằm, đêm, tép
 ST.tm='fixed';ST.ovr=22;ST.trangTest='ram';ST.inv.tep=40;ST.cau.pity=80;F.fmEnter();for(let i=0;i<5;i++)window.__tick();F.FM.bait='tep';o.avail=F.fAvail(F.FISHK.caho);
 let got=null;for(let i=0;i<15&&!got;i++){F.FM.ph='aim';F.fmCast(F.CAUV.rest.x-2.5,9.9);o.sp=F.spotOf(F.FM.bob.x,F.FM.bob.z);if(F.FM.tgt&&F.FISHK[F.FM.tgt.k].tier===4)got=1;}
 o.hoTgt=got; ST.autoReel=true; if(got){let gd=0;while(!['bite','aim','done'].includes(F.FM.ph)&&gd<6000){F.fmTick(gd*.016,.05);gd++;}if(F.FM.ph==='bite'){F.fmTap(0,0);gd=0;while(F.FM.ph==='reel'&&gd<12000){F.fmTick(gd*.016,.05);gd++;}}o.hoEnd=F.FM.ph;o.hoInv=ST.inv.caho||0;o.badge=ST.hoBadge;o.card=document.querySelector('.fcard')?.innerText.replace(/\n/g,' | ');}
 // groups
 for(const k of F.grpList('dem'))ST.fishLog[k]={n:1,max:.5};F.grpCheck();o.fgrp=JSON.stringify(ST.fgrp);
 // weekly
 o.fishWk=JSON.stringify(ST.fishWk);ST.hoiLast={wk:'2026-10-19',me1:1,n:3,k:'caloc'};ST.hoiSeen='';const xu0=ST.xu;F.hoiReward();o.cupXu=ST.xu-xu0;o.cup=ST.cup;
 // records board
 ST.fishLog.caloc={n:2,max:2.1};ST.fishLog.chep={n:1,max:1.4};for(let i=0;i<3;i++)window.__tick();o.board=F.KBEN.bd.visible+' '+F.KBEN.key;o.den=F.KBEN.den.visible;o.cupVis=F.KBEN.cup.visible;
 return o;});
console.log(JSON.stringify(r,null,1));
await p.screenshot({path:'../f3_card.png',timeout:90000,animations:'disabled'}).catch(e=>console.log('cardfail'));
await p.evaluate(async()=>{await window.__FM.fishShare('caloc',2.1);});await p.waitForTimeout(800);await p.screenshot({path:'../f3_share.png',timeout:90000,animations:'disabled'}).catch(e=>console.log('sharefail'));
await p.evaluate(()=>{document.querySelector('.fshare').hidden=true;const F=window.__FM;F.fmExit();const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(3.2,.2,8.2);c.object.position.copy(c.target).add(d);c.object.zoom=4.5;c.object.updateProjectionMatrix();window.__g.ST.tm='day';for(let i=0;i<4;i++)window.__tick();});
const u=await p.evaluate(()=>{window.__r.render(window.__S,window.__g.cam);return window.__r.domElement.toDataURL('image/png');});fs.writeFileSync('../f3_ben.png',Buffer.from(u.split(',')[1],'base64'));
await p.evaluate(()=>window.__x.openBook('ca'));await p.waitForTimeout(600);await p.screenshot({path:'../f3_book.png',timeout:90000,animations:'disabled'}).catch(e=>console.log('bookfail'));
console.log('errs',errs.filter(e=>!/TUNNEL|Failed to load|ERR_/.test(e)).slice(0,6));await b.close();})();
