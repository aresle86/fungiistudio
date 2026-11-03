const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const save=JSON.stringify({v:1,eco:2,split:1,open:['A1','A1b','A2','B1','B1b','B2'],fg:{cai:1},xu:500,inv:{rom:1},seeds:{},lu:0,gt:9000,real:Date.now()-3*3600*1000,spd:1,ovr:12,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'A',garden:'B'},lv:4,xp:90,qd:{2:1,4:1},ga:{hens:2,rooster:1,trough:1,eggs:0,acc:0,lv:0,brood:null},plots:{}});
for (const [w,h,tag] of [[1280,800,'d'],[390,844,'m']]){const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:2,isMobile:tag==='m',hasTouch:tag==='m'});
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,{timeout:300000});await p.waitForTimeout(2600);await p.evaluate(()=>{window.__stop=true;});
const r=await p.evaluate(()=>{const e=document.querySelector('#ngoai .pt').getBoundingClientRect();return [e.left,e.top,e.width,e.height,document.getElementById('ngoaiImg').src.slice(0,30)]});console.log(tag,r);
await p.screenshot({path:`qc2/ng_${tag}.png`,clip:{x:Math.max(0,r[0]-30),y:Math.max(0,r[1]-30),width:260,height:240},timeout:120000});await p.close();}
await b.close();})();
