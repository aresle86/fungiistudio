const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const DB={farms:{},fol:[],ev:[],seq:1};
const route=async r=>{const fn=r.request().url().split('/rpc/')[1];const a=JSON.parse(r.request().postData()||'{}');let out=null;const auth=()=>{const f=DB.farms[a.p_code];return f&&f.secret===a.p_secret?f:null;};
 const bad=()=>r.fulfill({status:400,body:JSON.stringify({message:'not allowed'})});
 if(fn==='mv2_register'){const code='MV-'+['AAAA','BBBB','CCCC'][Object.keys(DB.farms).length];DB.farms[code]={code,secret:'SECRETSECRET',name:a.p_name,garden:a.p_garden,lv:1,av:0,data:null,upd:new Date().toISOString()};out={code,secret:'SECRETSECRET'};}
 else if(fn==='mv2_save'){const f=auth();if(!f)return bad();Object.assign(f,{data:a.p_data,name:a.p_name,garden:a.p_garden,lv:a.p_lv,av:a.p_av,upd:new Date().toISOString()});out=f.upd;}
 else if(fn==='mv2_peek'){const f=DB.farms[a.p_code];out=f&&f.data?{code:f.code,name:f.name,garden:f.garden,lv:f.lv,av:f.av,data:f.data,updated_at:f.upd}:null;}
 else if(fn==='mv2_follow'){const f=auth();if(!f)return bad();const o=DB.farms[a.p_other];if(!o)out=null;else{DB.fol.push([f.code,o.code]);out={code:o.code,name:o.name,garden:o.garden,lv:o.lv,av:o.av};}}
 else if(fn==='mv2_neighbors'){const f=auth();if(!f)return bad();const set=new Set(DB.fol.filter(x=>x[0]===f.code).map(x=>x[1]));DB.ev.filter(e=>e.owner===f.code).forEach(e=>set.add(e.visitor));out=[...set].map(c=>{const o=DB.farms[c];return {code:c,name:o.name,garden:o.garden,lv:o.lv,av:o.av,updated_at:o.upd,followed:DB.fol.some(x=>x[0]===f.code&&x[1]===c),last_visit:null};});}
 else if(fn==='mv2_act'){const f=auth();if(!f)return bad();const n=DB.ev.filter(e=>e.visitor===f.code&&e.owner===a.p_other&&e.kind===a.p_kind).length;const mx={steal:2,water:3,gift:1,ask:1,repay:1,visit:50}[a.p_kind];if(n>=mx){out={ok:false,left:0};}else{DB.ev.push({id:DB.seq++,owner:a.p_other,visitor:f.code,kind:a.p_kind,payload:a.p_payload,consumed:false});out={ok:true,left:mx-n-1};}}
 else if(fn==='mv2_inbox'){const f=auth();if(!f)return bad();out=DB.ev.filter(e=>e.owner===f.code&&!e.consumed).map(e=>({id:e.id,kind:e.kind,payload:e.payload,created_at:new Date().toISOString(),code:e.visitor,name:DB.farms[e.visitor].name}));}
 else if(fn==='mv2_ack'){DB.ev.forEach(e=>{if(a.p_ids.includes(e.id))e.consumed=true;});out=null;}
 r.fulfill({status:200,contentType:'application/json',body:JSON.stringify(out)});};
const pl=(crop,g,moist)=>({crop,g,moist,dry:0,mulch:0,soil:.9,cut:0});
const mk=(name,extra)=>JSON.stringify(Object.assign({v:1,eco:2,split:1,qv2:1,open:['A1','A1b','A2','B1','B1b','B2'],fg:{cai:1,hanh:1},xu:500,inv:{rom:1,cai:4,hanh:3},seeds:{cai:2,hanh:1},lu:0,gt:9000,real:Date.now(),spd:1,ovr:12,realTime:false,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:1,name,garden:'Vườn '+name},lv:5,xp:200,qd:{3:1,4:1,5:1},plots:{}},extra||{}));
const open=async(save)=>{const ctx=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true});await ctx.route('**/rest/v1/rpc/**',route);const p=await ctx.newPage();p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));
 await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
 await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded',timeout:120000});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});return [ctx,p];};
// B: owner with an over-ripe cải and a dry bed
let [cB,pB]=await open(mk('Bé',{plots:{A1:pl('cai',9000,.9),B1:pl('hanh',300,0)},real:Date.now()-2*3600*1000}));await pB.waitForTimeout(6000);await cB.close();
console.log('B saved',!!DB.farms['MV-AAAA']&&!!DB.farms['MV-AAAA'].data);
// A: follows B via link, visits, steals + waters + gifts
let [cA,pA]=await open(mk('An'));await pA.waitForTimeout(6000);
await pA.evaluate(()=>{window.__g.openSheet('ben');});await pA.waitForTimeout(400);await pA.fill('#nbIn','mv-aaaa');await pA.evaluate(()=>document.querySelector('[data-a=nbadd]').click());await pA.waitForTimeout(800);
console.log('A neighbors',await pA.evaluate(()=>[...document.querySelectorAll('.vcard.nb b')].map(e=>e.textContent)));
await pA.evaluate(()=>document.querySelector('[data-a=nbgo]').click());await pA.waitForTimeout(1500);await pA.waitForFunction(()=>window.__ready,null,{timeout:300000});await pA.waitForTimeout(1200);
console.log('A visit',await pA.evaluate(()=>[document.body.classList.contains('visit'),document.querySelector('.vbar b').textContent,document.getElementById('vInfo').textContent]));
for(const id of ['A1','B1']){const c=await pA.evaluate(id=>{const g=window.__g,v=g.PV[id];const q=new g.T.Vector3(v.cx,.1,v.cz).project(g.cam);return [(q.x+1)/2*innerWidth,(1-q.y)/2*innerHeight];},id);await pA.mouse.click(c[0],c[1]);await pA.waitForTimeout(700);}
console.log('A after taps',await pA.evaluate(()=>[document.getElementById('vInfo').textContent,document.getElementById('ngoaiTxt').textContent.slice(0,60)]));
await pA.evaluate(()=>document.getElementById('vMore').click());await pA.waitForTimeout(300);await pA.evaluate(()=>document.querySelector('[data-a=vgift]').click());await pA.waitForTimeout(500);await pA.evaluate(()=>document.querySelector('[data-a=vask]').click());await pA.waitForTimeout(500);
await pA.evaluate(()=>{window.__g.closeSheet();document.getElementById('vHome').click();});await pA.waitForTimeout(1500);await pA.waitForFunction(()=>window.__ready,null,{timeout:300000});await pA.waitForTimeout(1500);
console.log('A home',await pA.evaluate(()=>[JSON.stringify(window.__g.ST.inv),JSON.stringify(window.__g.ST.seeds),window.__g.ST.xp,document.getElementById('ngoaiTxt').textContent.slice(0,80)]),pA.errs);
await cA.close();
console.log('events',DB.ev.map(e=>e.kind+':'+JSON.stringify(e.payload)).join(' | '));
// B comes back: inbox applied
[cB,pB]=await open(mk('Bé',{plots:{A1:pl('cai',9000,.9),B1:pl('hanh',300,0)},real:Date.now()-2*3600*1000}));
await pB.evaluate(()=>{localStorage.setItem('mv2-cloud',JSON.stringify({code:'MV-AAAA',secret:'SECRETSECRET'}));});await pB.reload({waitUntil:'domcontentloaded'});await pB.waitForFunction(()=>window.__ready,null,{timeout:300000});await pB.waitForTimeout(11000);
console.log('B back',await pB.evaluate(()=>{const S=window.__g.ST;return [S.plots.A1.stolen,S.plots.B1.moist,JSON.stringify(S.inv),document.getElementById('ngoaiTxt').textContent]}),pB.errs);
await b.close();})();
