const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const errs=[];
for(const [vw,vh,tag] of [[1440,860,'lap'],[430,860,'pho']]){
const p=await b.newPage({viewport:{width:vw,height:vh},deviceScaleFactor:tag==='pho'?2:1});p.on('pageerror',e=>errs.push(tag+' ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.addStyleTag({content:'.ddt{display:none!important}'});
await p.evaluate(()=>{window.__stop=true;const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=6;g.ST.xp=0;g.ST.tm='fixed';g.ST.ovr=10;g.ST.seen.hello=1;g.ST.xu=500;g.ST.inv.rom=5;g.ST.tre=0;g.ST.ga.fixed=1;window.__FT3.placeAvatar();});
const run=n=>p.evaluate(n=>{for(let i=0;i<n;i++)window.__tick();},n);const shot=n=>p.screenshot({path:'../u1_'+tag+'_'+n+'.png',timeout:120000});
await run(40);await p.evaluate(()=>{window.__FT3.hud();window.__FT3.nxq();window.__FT3.vuonBadge();});await run(2);await p.waitForTimeout(400);
console.log(tag,'card gather',await p.evaluate(()=>document.getElementById('nxq').innerText.replace(/\s+/g,' ')));
await shot('home');
// đủ đồ rồi dựng chuồng vịt
await p.evaluate(()=>{const g=window.__g;g.ST.tre=3;window.__FT3.penFix('vit');window.__FT3.hud();window.__FT3.nxq();});await run(3);
console.log(tag,'card build',await p.evaluate(()=>document.getElementById('nxq').innerText.replace(/\s+/g,' ')),await p.evaluate(()=>document.getElementById('nxq').dataset.a));
await p.evaluate(()=>{const g=window.__g;g.ST.bld.vit.t-=40*60e3;window.__FT3.nxq();});await run(2);
console.log(tag,'card build 40m',await p.evaluate(()=>document.getElementById('nxq').innerText.replace(/\s+/g,' ')));
await shot('build');
await p.evaluate(()=>{const b=document.getElementById('bVuon');console.log(b.hidden);b.click();});await p.waitForTimeout(800);await shot('vuon');
await p.close();}
console.log(errs.join('\n')||'no errors');await b.close();})();
