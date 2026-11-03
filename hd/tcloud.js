const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const DB={}; const calls=[];
const route=async r=>{const fn=r.request().url().split('/rpc/')[1];const a=JSON.parse(r.request().postData()||'{}');calls.push(fn);let out=null;
 if(fn==='mv2_register'){out={code:'MV-TEST',secret:'ABCDEFGHJKMN'};DB['MV-TEST']={secret:'ABCDEFGHJKMN',data:null};}
 else if(fn==='mv2_save'){if(!DB[a.p_code]||DB[a.p_code].secret!==a.p_secret)return r.fulfill({status:400,body:JSON.stringify({message:'not allowed'})});DB[a.p_code].data=a.p_data;out=new Date().toISOString();}
 else if(fn==='mv2_restore'){const d=DB[a.p_code];if(!d||d.secret!==a.p_secret)return r.fulfill({status:400,body:JSON.stringify({message:'not allowed'})});out={code:a.p_code,data:d.data};}
 r.fulfill({status:200,contentType:'application/json',body:JSON.stringify(out)});};
const save=JSON.stringify({v:1,eco:2,split:1,open:['A1','A1b','A2','B1','B1b','B2'],fg:{cai:1},xu:777,inv:{rom:1},seeds:{},lu:0,gt:9000,real:Date.now(),spd:1,ovr:12,realTime:false,seen:{hello:1},player:{av:2,name:'Ares',garden:'Địa Đàng'},lv:3,xp:40,qd:{2:1},plots:{}});
const ctx1=await b.newContext();await ctx1.route('**/rest/v1/rpc/**',route);const p=await ctx1.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(6000);
console.log('calls',calls.join(','),'saved xu',DB['MV-TEST']&&DB['MV-TEST'].data&&DB['MV-TEST'].data.xu, 'cred',await p.evaluate(()=>localStorage.getItem('mv2-cloud')));
await p.evaluate(()=>window.__g.openSheet('set'));await p.waitForTimeout(300);
console.log('set text',await p.evaluate(()=>[...document.querySelectorAll('#shB .vcard b, #shB .rc')].map(e=>e.textContent).join(' | ')));
await p.evaluate(()=>{window.__stop=true;});await p.waitForTimeout(300);await p.screenshot({path:'qc2/cloud_set.png',timeout:120000});await p.evaluate(()=>{window.__stop=false;window.__tick();});
await ctx1.close();// second device restores
const ctx2=await b.newContext();await ctx2.route('**/rest/v1/rpc/**',route);const p2=await ctx2.newPage();p2.on('pageerror',e=>errs.push('p2 '+e.message));
await p2.addInitScript(()=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');}}catch(e){}});
await p2.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded',timeout:120000});await p2.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p2.evaluate(()=>{document.getElementById('intro').hidden=true;window.__g.openSheet('set');document.querySelector('[data-a=cldres]').click();});await p2.waitForTimeout(300);
await p2.fill('#rIn','mv-test-abcd-efgh-jkmn');await p2.evaluate(()=>document.querySelector('[data-a=cldgo]').click());
await p2.waitForTimeout(3000);await p2.waitForFunction(()=>window.__ready,null,{timeout:300000});
console.log('p2 restored xu',await p2.evaluate(()=>[window.__g.ST.xu,window.__g.ST.player&&window.__g.ST.player.garden,localStorage.getItem('mv2-cloud')]));
console.log('errs',errs.join('|'));await b.close();})();
