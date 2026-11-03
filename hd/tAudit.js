// QA giao diện: nút nhỏ hơn 44px, chữ dưới 12px, tương phản chữ dưới 4.5:1, draw call, fps — ở vườn, Chợ, Sổ, vòng chọn
// dựng trang: cat x40f.js x106.js xpop.js > /tmp/x.js; python3 gen_test2.py /tmp/x.js live/v106a.html lp/mv2_t106.html
const {chromium}=require('playwright');
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:16,xp:13400,xu:3000,inv:{oi:6,chuoi:4,cai:6},gb:{cui:4},seeds:{cai:3},plots:{},
 qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1,15:1,16:1},
 land:{H1:{st:'own'},H2:{st:'own'},H3:{st:'own'},H4:{st:'own'},H5:{st:'own'},H6:{st:'own'},H7:{st:'own'},H8:{st:'own'}},open:['H5'],
 nong:{own:1,at:'H2',trays:[null,null,null,null],done:3,made:{otkho:1}},khap:{own:1,at:'H3',jars:[null,null],done:2,made:{dacai:1}},
 dc:{rao:'rao_tre',ga:'ga_tre',vit:'vit_mac',own:{},bag:{sanh:1},items:[{k:'cong_tre',at:'H4'}]},
 ft:{vusua:{st:2,told:2,t:Date.now()-1e8}},fishLog:{caro:{n:1},caloc:{n:2}},buom:{bu_phuong:1},realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
function audit(){
 const lum=c=>{const m=c.match(/[\d.]+/g);if(!m) return null;const [r,g,b]=m.slice(0,3).map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*r+.7152*g+.0722*b;};
 const alpha=c=>{const m=c.match(/[\d.]+/g);return m&&m.length>3?+m[3]:1;};
 const bgOf=e=>{for(let n=e;n&&n!==document.documentElement;n=n.parentElement){const c=getComputedStyle(n);if(c.backgroundImage!=='none'&&!/gradient/.test(c.backgroundImage)) return null;const g=c.backgroundImage.match(/rgba?\([^)]+\)/);if(g&&n!==e) return g[0];if(alpha(c.backgroundColor)>.9) return c.backgroundColor;}return null;};
 const vis=e=>{const r=e.getBoundingClientRect();if(r.width<1||r.height<1||r.bottom<0||r.top>innerHeight||r.right<0||r.left>innerWidth) return false;for(let n=e;n;n=n.parentElement){const c=getComputedStyle(n);if(c.display==='none'||c.visibility==='hidden'||+c.opacity<.1) return false;}return true;};
 const name=e=>(e.id?'#'+e.id:'')+(typeof e.className==='string'&&e.className.trim()?'.'+e.className.trim().split(/\s+/).slice(0,2).join('.'):'')+' «'+(e.getAttribute('aria-label')||e.textContent||'').trim().replace(/\s+/g,' ').slice(0,22)+'»';
 const small=[],tiny=[],low=[];
 for(const e of document.querySelectorAll('button,[role=button],a,input,select,[data-a],[data-b],[data-r]')){ if(!vis(e)) continue; const r=e.getBoundingClientRect(); if(Math.min(r.width,r.height)<44) small.push(name(e)+' '+Math.round(r.width)+'×'+Math.round(r.height)); }
 const seen=new Set();
 for(const e of document.querySelectorAll('body *')){ if(e.closest('#c,svg,canvas')) continue; const t=[...e.childNodes].filter(n=>n.nodeType===3&&n.textContent.trim()).map(n=>n.textContent.trim()).join(' '); if(!t||!vis(e)) continue;
  const c=getComputedStyle(e),fs=parseFloat(c.fontSize),k=t.slice(0,24);
  if(fs<12&&!seen.has('f'+k)){seen.add('f'+k);tiny.push(fs+'px «'+k+'»');}
  const bg=bgOf(e); if(bg&&c.textShadow==='none'){const L1=lum(c.color),L2=lum(bg); if(L1!=null&&L2!=null){const cr=(Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05); const big=fs>=18.66||(fs>=14&&+c.fontWeight>=700); if(cr<(big?3:4.5)&&!seen.has('c'+k)){seen.add('c'+k);low.push(cr.toFixed(2)+':1 '+fs+'px «'+k+'» '+c.color+' on '+bg);}}}
 }
 return {small,tiny,low};
}
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['ph',{width:390,height:664}],['pc',{width:1280,height:800}]]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.setDefaultTimeout(180000);
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/mv2_t106.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(2500);
 const perf=await p.evaluate(async()=>{const r=window.__r,inf=r&&r.info;let n=0;const t0=performance.now();await new Promise(res=>{const f=()=>{n++;performance.now()-t0<3000?requestAnimationFrame(f):res();};requestAnimationFrame(f);});
  return {fps:Math.round(n/3),calls:inf&&inf.render.calls,tris:inf&&inf.render.triangles,geo:inf&&inf.memory.geometries,tex:inf&&inf.memory.textures,heapMB:performance.memory?Math.round(performance.memory.usedJSHeapSize/1e6):null};});
 console.log(`\n=== ${tag} perf (swiftshader, chỉ để so tương đối)`,JSON.stringify(perf));
 const SC=[['vườn',async()=>{}],['Chợ',async()=>p.evaluate(()=>window.__g.openSheet('cho'))],['Chợ › Tiệm',async()=>p.evaluate(()=>{window.__U.SHEET.tab='tiem';window.__U.renderSheet();})],
  ['Sổ › Việc',async()=>p.evaluate(()=>{window.__g.closeSheet();window.__w.openBook('viec');})],['Sổ › Kho',async()=>p.evaluate(()=>window.__w.openBook('kho'))],['Sổ › Cá',async()=>p.evaluate(()=>window.__w.openBook('ca'))],
  ['vòng gieo',async()=>p.evaluate(()=>{window.__w.closeBook();window.__G.openRing('H5','seed');})]];
 for(const [n,f] of SC){await f();await p.waitForTimeout(700);const a=await p.evaluate(audit);
  console.log(`\n--- ${tag} ${n}: ${a.small.length} nút <44px · ${a.tiny.length} chữ <12px · ${a.low.length} chữ tương phản thấp`);
  if(a.small.length) console.log('  nút nhỏ: '+a.small.slice(0,14).join(' | '));
  if(a.tiny.length) console.log('  chữ nhỏ: '+a.tiny.slice(0,10).join(' | '));
  if(a.low.length) console.log('  tương phản: '+a.low.slice(0,8).join(' | '));
  await p.screenshot({path:`../qa_${tag}_${SC.findIndex(x=>x[0]===n)+1}.png`});}
 console.log(tag,errs.length?'ERR '+errs.join(' | '):'no errors');await p.close();}
await b.close();})();
