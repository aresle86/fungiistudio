const {chromium}=require('playwright');(async()=>{const [,,dir]=process.argv;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const pl=(crop,g,moist)=>({crop,g,moist,dry:0,mulch:0,soil:.9,cut:0});
const save=JSON.stringify({v:1,eco:2,split:1,open:['A1','A1b','A2','B1','B1b','B2','A2b','B2b'],fg:{cai:1,hanh:1,raumuong:1,ot:1},xu:1517,inv:{rom:3,cai:12,hanh:6,trungga:3},seeds:{cai:2,hanh:1},lu:0,gt:9000,real:Date.now(),spd:1,realTime:false,ovr:12,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:1,name:'Claude Opus 5.5 nè con',garden:'Vườn nhà Ngoại ở miệt vườn'},lv:3,xp:40,qd:{2:1},ga:{hens:2,rooster:1,trough:0,eggs:3,acc:0,lv:0,brood:null},
 plots:{A1:pl('cai',1800,.8),A1b:pl('hanh',900,0),A2:pl(null,0,.5),B1:pl('raumuong',2400,.8),B1b:pl('ot',3000,.8),B2:pl(null,0,.5),A2b:pl('cai',300,.8),B2b:pl(null,0,.5)}});
for (const [w,h,tag] of [[1280,800,'d'],[390,844,'m']]){const p=await b.newPage({viewport:{width:w,height:h},hasTouch:tag==='m',isMobile:tag==='m',deviceScaleFactor:1});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;});const tick=async()=>{await p.evaluate(()=>{for(let i=0;i<2;i++)window.__tick();});await p.waitForTimeout(200);};
const shot=async(n,f)=>{if(f)await p.evaluate(f);await tick();await p.screenshot({path:`${dir}/${tag}_${n}.png`});};
await shot('00_away');
await shot('01_hud',()=>{window.__g.closeSheet();});
await shot('02_bar',()=>{document.getElementById('tSeed').click();window.__g.say('Liếp này đang có cây rồi, chọn liếp trống con.','dan',{now:true});});
await shot('03_plot',()=>{document.getElementById('tSeed').click();window.__g.openSheet('plot','A1b');});
await shot('04_cho',()=>{window.__g.openSheet('cho');});
await shot('05_ga',()=>{window.__g.openSheet('ga');});
await shot('06_set',()=>{window.__g.openSheet('set');});
await shot('07_kho',()=>{window.__g.closeSheet();window.__x.openBook('kho');});
await shot('08_giong',()=>{window.__x.openBook('giong');});
await shot('09_viec',()=>{window.__x.openBook('viec');});
await shot('10_night',()=>{document.querySelector('#book').hidden=true;window.__g.ST.ovr=20.5;});
await shot('11_lock',()=>{window.__g.ST.ovr=12;window.__g.openSheet('plot','C1');});
console.log(tag,errs.join('|'));await p.close();}
await b.close();})();
