const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const pl=(crop,g,moist)=>({crop,g,moist,dry:0,mulch:0,soil:.5,cut:0});
const save=JSON.stringify({v:1,eco:2,split:1,exp:1,open:['A1','A1b','A2','B1','B1b','B2','D1','D1b'],fg:{cai:1,hanh:1},xu:500,inv:{rom:1,cai:6,hanh:4,trungga:2},seeds:{cai:2},lu:0,gt:9000,real:Date.now()-4*3600*1000,spd:1,realTime:false,ovr:12,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'Ares',garden:'Địa Đàng'},lv:4,xp:90,qd:{2:1,4:1},ga:{hens:2,rooster:1,trough:1,eggs:0,acc:0,lv:0,brood:null},plots:{A1:pl('cai',100,.9),A2:pl('hanh',100,.9),B1:pl('raumuong',200,.9),B2:pl('cai',300,.9)}});
for (const [w,h,tag] of [[1280,800,'d'],[390,844,'m']]){
const p=await b.newPage({viewport:{width:w,height:h},hasTouch:tag==='m',isMobile:tag==='m'});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});await p.waitForTimeout(1500);
await p.evaluate(()=>{window.__stop=true;});const tick=async()=>{await p.evaluate(()=>{for(let i=0;i<2;i++)window.__tick();});await p.waitForTimeout(250);};await tick();
const st=await p.evaluate(()=>{const S=window.__g.ST;return {odd:(S.odd&&S.odd.list||[]).map(o=>o.k+':'+(o.id||'')),ord:(S.ord&&S.ord.list||[]).map(o=>o.who+' '+o.items.map(i=>i.join('x')).join(',')+' '+o.xu),ng:document.getElementById('ngoaiTxt').textContent,seeds:S.seeds,rom:S.inv.rom,ob:document.querySelector('#bCho .ob')?.textContent}});console.log(tag,JSON.stringify(st));
const t0=Date.now();await p.evaluate(()=>1);console.log('eval ms',Date.now()-t0, errs.join('|'));await p.screenshot({path:`qc2/o_${tag}_world.png`,timeout:120000});
await p.evaluate(()=>window.__g.openSheet('cho'));await tick();await p.screenshot({path:`qc2/o_${tag}_cho.png`});
// deliver first possible
const r=await p.evaluate(()=>{const b=document.querySelector('[data-a=ordgive]:not([disabled])');if(!b)return 'none';const x0=window.__g.ST.xu;b.click();return [x0,window.__g.ST.xu,window.__g.ST.ord.list.length]});console.log(tag,'give',JSON.stringify(r));
console.log(tag,'errs',errs.join('|'));await p.close();}
await b.close();})();
