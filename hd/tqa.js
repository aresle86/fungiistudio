const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const mk=(lv,xp,extra)=>JSON.stringify(Object.assign({v:1,eco:2,split:1,open:['A1','A1b','A2','B1','B1b','B2'],fg:{cai:1,hanh:1},xu:500,inv:{rom:1,cai:6,hanh:4,trungga:3},seeds:{cai:1},lu:0,gt:9000,real:Date.now(),spd:1,ovr:12,realTime:false,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'Nhu',garden:'Nhu'},lv,xp,qd:{2:1},plots:{}},extra||{}));
const run=async(tag,save,fn)=>{const p=await b.newPage({viewport:{width:390,height:844},isMobile:true,hasTouch:true});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(700);await p.evaluate(()=>{window.__stop=true;});
const r=await fn(p);console.log(tag,JSON.stringify(r),errs.join('|'));await p.close();};
// old save at lv2 with weed done -> migrated qd[3]
await run('mig2',mk(2,20,{qd:{2:1}}),p=>p.evaluate(()=>({qd:window.__g.ST.qd,qv2:window.__g.ST.qv2,nq:document.getElementById('bSo').querySelector('.kb')&&!document.getElementById('bSo').querySelector('.kb').hidden})));
// lv3 with xp enough for 4: goal quest; open 2 beds + deliver order -> level 4
await run('goal4',mk(3,90,{qd:{2:1,3:1},qv2:1,ord:{list:[],acc:0,first:1,done:0}}),async p=>{const a=await p.evaluate(()=>window.__g.ST.lv);
 await p.evaluate(()=>{const S=window.__g.ST;S.open.push('A2b','B2b');S.ord.done=1;window.__x.openBook('viec');});await p.waitForTimeout(300);
 const pg=await p.evaluate(()=>[...document.querySelectorAll('.qg')].map(e=>e.textContent));
 await p.evaluate(()=>{window.__x.act.water('A1');});await p.waitForTimeout(200);
 return {lv0:a,lv:await p.evaluate(()=>window.__g.ST.lv),qd:await p.evaluate(()=>window.__g.ST.qd),goals:pg};});
// Sổ opens Việc tab; chợ tabs
await run('so+cho',mk(3,40,{qv2:1,qd:{2:1,3:1},ord:{list:[{id:'1',who:'Cô Tư',why:'nấu canh chua',items:[['cai',2]],xu:30,xp:3}],acc:0,first:1,done:0}}),async p=>{await p.evaluate(()=>document.getElementById('bSo').click());await p.waitForTimeout(200);const tab=await p.evaluate(()=>document.querySelector('.bkt.on').getAttribute('data-k'));
 await p.evaluate(()=>{window.__x.openBook;document.querySelector('[data-b=close]').click();document.getElementById('bCho').click();});await p.waitForTimeout(200);
 const t1=await p.evaluate(()=>[document.querySelector('.sg.on').textContent,document.querySelectorAll('.ordr').length,document.querySelectorAll('.srow').length]);
 await p.evaluate(()=>document.querySelector('[data-a=ctab][data-k=mua]').click());await p.waitForTimeout(150);
 const t2=await p.evaluate(()=>[document.querySelector('.sg.on').textContent,document.querySelectorAll('.srow').length]);
 await p.screenshot({path:'qc2/cho_tabs.png',timeout:120000});
 return {tab,t1,t2};});
await b.close();})();
