const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:780},isMobile:true,hasTouch:true,deviceScaleFactor:2});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='warning'||m.type()==='error')errs.push(m.text())});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
const r=await p.evaluate(()=>{const g=window.__g,ST=g.ST,F=window.__FM,o={};ST.lv=9;window.__stop=true;
 o.nk=Object.keys(F.FISHK).length; o.gio=F.gioNow(); o.mua=F.muaSong();
 F.fmEnter();for(let i=0;i<30;i++)window.__tick(); o.moi=JSON.stringify(ST.moi); o.chips=[...document.querySelectorAll('.fmoi')].map(b=>b.textContent+(b.disabled?'(x)':'')).join('|');
 // spots
 const sp={};for(let i=0;i<300;i++){const x=F.FAREA? 0:0;} 
 // choose bait trun
 document.querySelector('.fmoi[data-k="trun"]').click(); o.bait=F.FM.bait;for(let i=0;i<5;i++)window.__tick();
 // tally spawn picks per spot under current hour
 const cnt={};for(const s2 of ['gan','giua','me']){cnt[s2]={};for(let i=0;i<400;i++){const k=F.fishPick(s2);cnt[s2][k]=(cnt[s2][k]||0)+1;}}o.cnt=JSON.stringify(cnt);
 // catch with bait -> bonus
 ST.autoReel=true;const res=[];let guard2=0;while(F.cauLeft()>0&&guard2<20){guard2++;if(!F.FSH.list.length)window.__tick();const s=F.FSH.list[0];F.fmCast(s.m.position.x,s.m.position.z);let gd=0;while(!['bite','aim','done'].includes(F.FM.ph)&&gd<4000){F.fmTick(gd*.016,.05);gd++;}const a=F.FM.ph;if(a==='bite'){F.fmTap(0,0);gd=0;while(F.FM.ph==='reel'&&gd<8000){F.fmTick(gd*.016,.05);gd++;}}if(!F.FSH.list.length)window.__tick();res.push(a+'>'+F.FM.ph+':'+(F.FM.used||'-'));if(F.FM.ph==='done')F.FM.ph='aim';}
 o.res=res.join(' ');o.cap=F.cauCap();o.trunLeft=ST.moi.trun;o.log=Object.keys(ST.fishLog).join(',');
 // rare: force combo — set hour via ST.tm fixed
 ST.tm='fixed';ST.ovr=6;ST.muaSong='mua';ST.cau.n=0;ST.cau.bonus='';ST.moi.trun=50;F.FM.bait='trun';ST.cau.pity=60;F.fshClear();for(let i=0;i<5;i++)window.__tick();
 // cast at 'me' spot: near our bank away from bến
 let rare=null;for(let tries=0;tries<10&&!rare;tries++){F.FM.ph='aim';const bx=F.CAUV.rest.x-2.6, bz=8.95; F.fmCast(bx,bz); o.spotRare=F.spotOf(F.FM.bob.x,F.FM.bob.z); if(F.FM.tgt&&F.FISHK[F.FM.tgt.k].tier===3) rare=F.FM.tgt.k;}
 o.rare=rare; if(rare){let gd=0;while(!['bite','aim','done'].includes(F.FM.ph)&&gd<6000){F.fmTick(gd*.016,.05);gd++;}if(F.FM.ph==='bite'){F.fmTap(0,0);gd=0;while(F.FM.ph==='reel'&&gd<9000){F.fmTick(gd*.016,.05);gd++;}}o.rareEnd=F.FM.ph;o.pity=ST.cau.pity;}
 return o;});
console.log(JSON.stringify(r,null,1));
await p.evaluate(()=>{const F=window.__FM;F.FM.ph='aim';document.querySelector('.fui').hidden=false;window.__x&&0;});
await p.evaluate(()=>{const F=window.__FM;F.fmExit();window.__g.ST.tm='real';F.fmEnter();for(let i=0;i<10;i++)window.__tick();});
await p.screenshot({path:'../f2_aim.png',timeout:60000}).catch(()=>console.log('shotfail'));
// cook
const ck=await p.evaluate(()=>{const g=window.__g,ST=g.ST,o={};ST.lv=9;ST.bep=ST.bep||{};ST.bep.lit=1;ST.bep.pots=[null,null];ST.bep.made={};ST.inv.caro=4;ST.inv.caloc=2;ST.inv.rom=5;ST.inv.ot=3;ST.inv.tep=5;ST.inv.khe=2;ST.gb=ST.gb||{};ST.gb.cui=5;ST.gb.duong=3;ST.gb.muoi=3;ST.inv.sacran=4;
 window.__FM.fmExit();g.openSheet('bep');const sh=document.querySelector('#sheet,.sheet');o.bep=(sh&&sh.innerText||'').slice(0,200);return o;});
console.log(JSON.stringify(ck));
await p.evaluate(()=>{window.__x.openBook('ca');});await p.waitForTimeout(500);await p.screenshot({path:'../f2_book.png',timeout:60000}).catch(()=>{});
console.log('errs',errs.filter(e=>!/TUNNEL/.test(e)).slice(0,5));await b.close();})();
