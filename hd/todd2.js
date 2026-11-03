const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const pl=(crop,g,moist)=>({crop,g,moist,dry:0,mulch:0,soil:.5,cut:0});
const save=JSON.stringify({v:1,eco:2,split:1,exp:1,open:['A1','A1b','A2','B1','B1b','B2','D1','D1b'],fg:{cai:1,hanh:1},xu:500,inv:{rom:1,cai:6,hanh:4,trungga:2},seeds:{cai:2},lu:0,gt:9000,real:Date.now()-4*3600*1000,spd:1,realTime:false,ovr:12,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'Ares',garden:'Địa Đàng'},lv:4,xp:90,qd:{2:1,4:1},ga:{hens:2,rooster:1,trough:1,eggs:0,acc:0,lv:0,brood:null},plots:{A1:pl('cai',100,.9),A2:pl('hanh',100,.9),B1:pl('raumuong',200,.9),B2:pl('cai',300,.9)}});
const p=await b.newPage({viewport:{width:1280,height:800},deviceScaleFactor:3});
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});await p.waitForTimeout(800);
await p.evaluate(()=>{window.__stop=true;});const tick=async()=>{await p.evaluate(()=>{for(let j=0;j<3;j++)window.__tick();});await p.waitForTimeout(250);};
const odd=await p.evaluate(()=>window.__g.ST.odd.list.map(o=>[o.k,o.x,o.z]));console.log(JSON.stringify(odd));
await tick();await p.waitForTimeout(2500);await tick();let i=0;for(const [k,x,z] of odd){const sc=await p.evaluate(([x,z])=>{const g=window.__g;const v=new g.T.Vector3(x,.15,z).project(g.cam);return [(v.x+1)/2*innerWidth,(1-v.y)/2*innerHeight];},[x,z]);
 await p.screenshot({path:`qc2/odd_${i++}_${k}.png`,clip:{x:Math.max(0,sc[0]-60),y:Math.max(0,sc[1]-45),width:120,height:90},timeout:120000});}
await b.close();})();
