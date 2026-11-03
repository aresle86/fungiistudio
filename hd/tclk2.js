const {chromium}=require('playwright');const fs=require('fs');const L=m=>fs.appendFileSync('tclk.log',m+'\n');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for (const [nm,off] of [['dawn',0],['dusk',33.2],['night',37.5]]){
const save=JSON.stringify({v:1,eco:2,split:1,open:['A1','A1b','A2','B1','B1b','B2'],fg:{cai:1},xu:150,inv:{rom:3},seeds:{cai:2},lu:0,gt:0,real:Date.now(),spd:1,seen:{hello:1,sold:1},player:{av:2,name:'Nhu',garden:'Nhu'},lv:2,xp:12,qd:{},plots:{},tm:'game',clk0:Date.now()-(off+ (nm==='dawn'?0.4:0))*60000});
const p=await b.newPage({viewport:{width:390,height:844},isMobile:true,hasTouch:true});
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(2500);
await p.evaluate(()=>{window.__stop=true;});await p.waitForTimeout(200);await p.screenshot({path:`qc3/clk_${nm}.png`,timeout:200000});L(nm+' '+await p.evaluate(()=>document.getElementById('tt').textContent));await p.close();}
await b.close();L('END');})().catch(e=>{L('FAIL '+e.message.slice(0,300));process.exit(1)});
