// v107 Cài đặt › Trời trong vườn: chỉ 2 nút (Giờ trong vườn, Luôn ban ngày); chỉnh tay giờ chỉ khi ?dev; save cũ tm=real tự về game
const {chromium}=require('playwright');
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:5,xp:190,xu:300,inv:{},seeds:{},plots:{},qd:{3:1,4:1,5:1},tm:'real',realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});let bad=0;const ok=(c,m)=>{console.log(`${c?'OK ':'SAI'} ${m}`);if(!c) bad++;};
for(const q of ['','?dev']){const p=await b.newPage({viewport:{width:900,height:640}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.setDefaultTimeout(180000);
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/mv2_t107.html'+q,{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(800);
 const r=await p.evaluate(()=>{window.__g.openSheet('set');const tm=[...document.querySelectorAll('[data-a=tm]')].map(b=>b.textContent.trim());return {tm,hour:document.querySelectorAll('[data-a=hour]').length,mode:window.__g.ST.tm,real:document.body.innerText.includes('Theo giờ thật')};});
 if(!q){ok(r.tm.join(',')==='Giờ trong vườn,Luôn ban ngày'&&r.hour===0&&!r.real,`không ?dev: nút ${r.tm.join(', ')} · chỉnh tay ${r.hour} · còn chữ "Theo giờ thật" ${r.real}`);ok(r.mode==='game',`save cũ tm=real → ${r.mode}`);}
 else ok(r.hour===4,`?dev: có ${r.hour} nút chỉnh tay giờ`);
 ok(!errs.length,'không lỗi trang '+errs.join(' | '));await p.close();}
console.log('DONE',bad,'chỗ sai');await b.close();})();
