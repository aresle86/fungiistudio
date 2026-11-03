const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:600}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));p.on('console',m=>{if(/BOT/.test(m.text()))errs.push(m.text())});
const T0=new Date('2026-11-04T07:30:00+07:00').getTime();
await p.addInitScript(([t0])=>{const RD=Date;let off=t0-RD.now();window.__off=v=>{off=v-RD.now()};class FD extends RD{constructor(...a){if(a.length===0)super(RD.now()+off);else super(...a)}static now(){return RD.now()+off}}window.Date=FD;
 try{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',JSON.stringify({v:1,eco:2,split:1,qv2:1,seen:{hello:1},player:{av:1,name:'Bot',garden:'Bot'},lv:1,xp:0,xu:100,inv:{},seeds:{},plots:{},realTime:true,spd:1,real:t0}))}catch(e){}},[T0]);
await p.goto('http://127.0.0.1:8777/mv2_bot.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const dump=()=>p.evaluate(()=>{const g=window.__g,S=g.ST;return JSON.stringify({xu:S.xu,xp:S.xp,open:S.open,inv:S.inv,seeds:S.seeds,plots:Object.fromEntries(Object.entries(S.plots).filter(([k,v])=>v.crop).map(([k,v])=>[k,[v.crop,Math.round(v.g),+v.moist.toFixed(2)]]))})});
console.log(await dump());
for(let i=0;i<4;i++){const r=await p.evaluate(i=>{window.__stop=true;const B=window.__bot;B.step(i?3600:0);B.visit(0);return 1},i);console.log(i,await dump());}
console.log(errs.join('\n')||'no errors');await b.close();})();
