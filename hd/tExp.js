const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const PAGE=process.argv[2],EXPS=process.argv[3]==='1',TAG=process.argv[4];
const p=await b.newPage({viewport:{width:1000,height:640}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));let nav=0;p.on('framenavigated',f=>{if(f===p.mainFrame())nav++});
await p.addInitScript(([ex])=>{if(sessionStorage.getItem('i1'))return;sessionStorage.setItem('i1','1');localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',JSON.stringify({v:1,eco:2,split:1,qv2:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:4,xp:200,xu:500,inv:{},seeds:{},plots:{},qd:ex?{3:1,4:1,5:1}:{3:1,4:1},exp:ex?1:0,realTime:true,spd:1,real:Date.now()}))},[EXPS]);
await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const cam=()=>p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#lvup,.ngoai').forEach(e=>e.hidden=true);const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(8.2,0,4.2);c.object.position.copy(c.target).add(d);c.object.zoom=2.2;c.object.updateProjectionMatrix();window.__stop=true;for(let i=0;i<4;i++)window.__tick();});
await cam();await p.screenshot({path:'../exp_'+TAG+'_a.png'});
if(!EXPS){await p.evaluate(()=>window.__e.doQuest(5));await p.waitForTimeout(2500);await cam();await p.screenshot({path:'../exp_'+TAG+'_b.png'});
 const r=await p.evaluate(()=>{const G=window.__G;const S=window.__g.ST;const pl=G.PLOTS.filter(P=>P.exp).map(P=>P.id);const before=S.open.length;window.__g.act.openBed('D1');return {pl,exp:S.exp,lv:S.lv,openD1:S.open.includes('D1'),xu:S.xu};});console.log('after',JSON.stringify(r),'nav',nav);
 await p.waitForTimeout(500);await cam();await p.screenshot({path:'../exp_'+TAG+'_c.png'});}
console.log(errs.join('\n')||'no errors');await b.close();})();
