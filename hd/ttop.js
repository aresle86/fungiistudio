const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const save=JSON.stringify({v:1,eco:2,split:1,qv2:1,exp:1,open:['A1','A1b','A2','B1','B1b','B2','D1','D1b'],fg:{cai:1},xu:900,inv:{rom:1},seeds:{},lu:0,gt:9000,real:Date.now(),spd:1,ovr:12,realTime:false,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'Nhu',garden:'Nhu'},lv:6,xp:320,qd:{3:1,4:1,5:1,6:1},plots:{}});
const p=await b.newPage({viewport:{width:1400,height:1100}});
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(800);
await p.evaluate(()=>{window.__stop=true;const g=window.__g,c=g.cam;c.position.set(5,40,2.5);c.up.set(0,0,-1);c.lookAt(5,0,2.5);c.position.set(3,40,3);c.lookAt(3,0,3);c.zoom=1;const A=innerWidth/innerHeight;c.left=-9*A;c.right=9*A;c.top=9;c.bottom=-9;c.updateProjectionMatrix();window.__tick();
 document.querySelectorAll('#hud,.hud,#ngoai,#bar,#tools').forEach(e=>e.style.display='none');
 for(let x=-8;x<=14;x++)for(let z=-5;z<=10;z++){const v=new g.T.Vector3(x,0,z).project(c);const d=document.createElement('div');d.textContent=(x%2==0&&z%2==0)?x+','+z:'+';d.style.cssText=`position:fixed;left:${(v.x+1)/2*innerWidth}px;top:${(1-v.y)/2*innerHeight}px;font:10px monospace;color:#f0f;z-index:999;pointer-events:none`;document.body.appendChild(d);}});
await p.waitForTimeout(300);await p.screenshot({path:'qc2/top.png',timeout:200000});await b.close();})();
