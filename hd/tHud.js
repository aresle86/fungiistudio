const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});const errs=[];
for(const [vw,vh,tag] of [[360,740,'p360'],[390,844,'p390'],[1440,860,'lap']]){
const p=await b.newPage({viewport:{width:vw,height:vh},deviceScaleFactor:1});p.on('pageerror',e=>errs.push(tag+' ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.addStyleTag({content:'.ddt{display:none!important}'});
await p.evaluate(()=>{window.__stop=true;const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av:0,name:'Địa Đàng',garden:'V'};g.ST.lv=7;g.ST.xp=1300;g.ST.tm='fixed';g.ST.ovr=17.2;g.ST.seen.hello=1;g.ST.xu=500;window.__FT3.placeAvatar();for(let i=0;i<40;i++)window.__tick();window.__FT3.hud();window.__FT3.nxq();});
await p.waitForTimeout(2500);await p.evaluate(()=>{for(let i=0;i<3;i++)window.__tick();});
await p.screenshot({path:'../hud_'+tag+'.png',timeout:300000});
if(tag==='lap'){await p.evaluate(()=>{const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(8.75,0,7.6);c.object.position.copy(c.target).add(d);c.object.zoom=2.2;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();});await p.screenshot({path:'../land_song.png',timeout:300000});
 await p.evaluate(()=>{const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(-3.2,0,3);c.object.position.copy(c.target).add(d);c.object.zoom=1.9;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();});await p.screenshot({path:'../land_bai.png',timeout:300000});}
await p.close();}
console.log(errs.join('\n')||'no errors');await b.close();})();
