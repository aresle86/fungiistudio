const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:640},deviceScaleFactor:1.5});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',JSON.stringify({v:1,eco:2,split:1,qv2:1,exp:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:12,xp:7600,xu:900,inv:{oi:12,chuoi:4,cai:6,trungga:4},gb:{otkho:3,dacai:2,cui:4},seeds:{},plots:{T2:{crop:'oi',g:1e6,moist:1,soil:1,dry:0}},qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1},nong:{own:1,at:'H2',trays:[null,null,null,null],done:3,made:{otkho:1}},khap:{own:1,at:'H3',jars:[null,null],done:2,made:{dacai:1}},fishLog:{caro:{n:1}},realTime:true,spd:1,real:Date.now()}))});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const r=await p.evaluate(()=>{window.__stop=true;const S=window.__g.ST,E=window.__e;const out={};
 S.ghe.o=null;S.ghe.d='';E.gheSim();out.ghe1=JSON.stringify(S.ghe.o&&{items:S.ghe.o.items,lead:S.ghe.o.lead,xu:S.ghe.o.xu});
 // deliver lead
 E.gheGive();out.afterLead=JSON.stringify({o:S.ghe.o,done:S.ghe.done,lead:S.leadDone});
 S.ghe.d='';E.gheSim();out.ghe2=JSON.stringify(S.ghe.o&&S.ghe.o.items);
 const xu0=S.xu;E.gheGive();out.part=JSON.stringify({got:S.ghe.o&&S.ghe.o.got,xu:S.xu-xu0});
 if(S.ghe.o){S.ghe.o.seen=Date.now()-7*3600e3;const x1=S.xu;E.gheSim();out.expire=JSON.stringify({o:S.ghe.o,paid:S.xu-x1});}
 // neighbor orders roles
 const nb=[];for(let i=0;i<30;i++){S.ord.list=[];window.__g.sim(25*60+1);for(const o of S.ord.list)nb.push(o.items.map(x=>x[0]).join('+')+(o.lead?'*':''));}out.nb=[...new Set(nb)].slice(0,20).join(' ');
 return out;});
for(const [k,v] of Object.entries(r))console.log(k,v);
await p.evaluate(()=>{const S=window.__g.ST;S.ghe.d='';window.__e.gheSim();window.__g.openSheet('ben');});await p.waitForTimeout(600);await p.screenshot({path:'../ghe104.png'});
console.log(errs.join('\n')||'no errors');await b.close();})();
