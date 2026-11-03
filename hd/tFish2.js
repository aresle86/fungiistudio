const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:780},isMobile:true,hasTouch:true});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
const r=await p.evaluate(()=>{const g=window.__g,ST=g.ST,F=window.__FM,o={};ST.lv=9;window.__stop=true;F.fmEnter();for(let i=0;i<30;i++)window.__tick();
 ST.autoReel=true;const res=[];for(let round=0;round<5;round++){const s=F.FSH.list[0];F.fmCast(s.m.position.x,s.m.position.z);let gd=0;while(!['bite','aim','done'].includes(F.FM.ph)&&gd<4000){F.fmTick(gd*.016,.05);gd++;}
 const a=F.FM.ph;if(a==='bite'){F.fmTap(0,0);if(round==0)o.btn=document.querySelector('.fauto')?.textContent;gd=0;while(F.FM.ph==='reel'&&gd<6000){F.fmTick(gd*.016,.05);gd++;}}res.push(a+'>'+F.FM.ph);if(F.FM.ph==='done'){o.card=document.querySelector('.fcard b')?.textContent;F.FM.ph='aim';}}
 o.auto=res;
 // early tap lose
 const s=F.FSH.list[0];F.fmCast(s.m.position.x,s.m.position.z);let gd=0;while(F.FM.ph!=='nibble'&&gd<3000){F.fmTick(gd*.016,.05);gd++;}o.ph0=F.FM.ph;F.fmTap(0,0);o.afterEarly=F.FM.ph;
 ST.cau.n=0;{const s=F.FSH.list[0]||F.fshSpawn?.();F.fmCast(F.FSH.list[0].m.position.x,F.FSH.list[0].m.position.z);let gd=0;while(F.FM.ph!=='nibble'&&gd<3000){F.fmTick(gd*.016,.05);gd++;}o.ph1=F.FM.ph;F.fmTap(0,0);o.after1=F.FM.ph;o.bait=document.body.innerText.match(/mồi[^\n]*/)?.[0];}o.oc=!!window.__x.ICON.oc;return o;});
console.log(JSON.stringify(r),'errs',errs.slice(0,3));await b.close();})();
