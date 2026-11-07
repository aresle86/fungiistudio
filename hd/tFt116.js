// tFt116: lời đồn cây cổ tích, Sổ ghi lại, đốm sáng nút Sổ, điềm báo, cảnh mở từng cây. node tFt116.js [trang]
const {chromium}=require('playwright');const PAGE=process.argv[2]||'mv2_t116a.html';let bad=0;const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)bad++};const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SV=(lv,x)=>({v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv,xp:80000,xu:50000,inv:{},gb:{},seeds:{},plots:{},qd:Object.fromEntries(Array.from({length:Math.max(0,lv-2)},(_,i)=>[i+3,1])),realTime:true,spd:1,real:Date.now(),dd:{last:today,n:3,full:0},...x});
const SHOT=process.env.SHOT||'/tmp/ft116';require('fs').mkdirSync(SHOT,{recursive:true});
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const mk=async(sv,vp)=>{const p=await b.newPage({viewport:vp||{width:390,height:844}});p.setDefaultTimeout(240000);p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(sv));await p.goto('http://127.0.0.1:8777/'+PAGE);await p.waitForFunction(()=>window.__ready);await p.waitForTimeout(2500);await p.evaluate(()=>document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>e.hidden=true));return p};
const X=(p,f)=>p.evaluate(`(${f})(window.__DCX0.get(),window.__O.ST)`);
const old=Date.now()-2*864e5;
if(!process.env.ONLY){
// 1. lời đồn hiện ra: thẻ riêng, có nút, có đốm sáng nút Sổ
let p=await mk(SV(14,{ftr:{vusua:{t0:old,n:0,last:0,h:[]}}}));
await p.waitForFunction(()=>document.querySelector('#ngoai').hidden,null,{timeout:90000});
await X(p,(X,S)=>{S.ftrD='';X.ftrCheck()});await p.waitForTimeout(700);
let r=await p.evaluate(()=>{const c=document.querySelector('.ftr');return c&&{t:c.innerText,on:c.classList.contains('on'),b:c.querySelectorAll('button').length,dot:!!document.querySelector('#bSo .ftb')}});
console.log(JSON.stringify(r));ok(r&&r.on&&/đầu ngõ/.test(r.t)&&r.b===2,'lời đồn hiện thẻ riêng, có 2 nút');ok(r&&r.dot,'nút Sổ có đốm sáng');
await p.screenshot({path:SHOT+'/1_loidon_ph.png'});
await p.waitForTimeout(6000);ok(await p.evaluate(()=>!!document.querySelector('.ftr.on')),'thẻ không tự tắt sau 6 giây');
r=await X(p,(X,S)=>[S.ftr.vusua.n,S.ftrD]);ok(r[0]===1,'ghi đã kể nấc 1');
await X(p,(X,S)=>{X.ftrCheck()});await p.waitForTimeout(300);ok(await p.evaluate(()=>document.querySelectorAll('.ftr').length===1),'một ngày chỉ một thẻ');
await p.evaluate(()=>document.querySelector('.ftr button[data-a=so]').click());await p.waitForTimeout(900);
r=await p.evaluate(()=>{const t=document.querySelector('.bkov,.book,#book')?document.body.innerText:'';return {so:/Ngoại có nói/.test(document.body.innerText),prg:/7 ngày liền/.test(document.body.innerText),dot:!!document.querySelector('#bSo .ftb')}});
console.log(JSON.stringify(r));ok(r.so&&r.prg,'Sổ ghi lại lời Ngoại và tiến độ');ok(!r.dot,'mở Sổ cổ tích thì tắt đốm sáng');
await p.screenshot({path:SHOT+'/2_so_ph.png'});
ok(p.errs.length===0,'không lỗi '+p.errs[0]);await p.close();
// 2. nấc sau: 3 ngày sau ra nấc 2, có tiến độ
p=await mk(SV(14,{ftr:{vusua:{t0:old-9*864e5,n:1,last:Date.now()-3.1*864e5,h:[0]}},ftrD:''}));
await p.waitForFunction(()=>document.querySelector('#ngoai').hidden,null,{timeout:90000});await X(p,(X,S)=>X.ftrCheck());await p.waitForTimeout(600);
r=await p.evaluate(()=>{const c=document.querySelector('.ftr');return c&&c.innerText});ok(r&&/Đủ bảy ngày liền/.test(r)&&/\/7 ngày liền/.test(r),'nấc 2 rủ làm rõ hơn, có tiến độ');
ok(p.errs.length===0,'không lỗi '+p.errs[0]);await p.close();
// 3. điềm báo: nấc 3 rồi thì có đom đóm ở chỗ cây, chạm vô Ngoại kể lại
p=await mk(SV(16,{ftr:{khevang:{t0:old,n:3,last:Date.now(),h:[0,1,2]},vusua:{t0:old,n:1,last:Date.now(),h:[0]},tretramdot:{t0:old,n:1,last:Date.now(),h:[0]},traucau:{t0:old,n:1,last:Date.now(),h:[0]},duahau:{t0:old,n:1,last:Date.now(),h:[0]}},ftrD:today}));
await p.waitForTimeout(1500);r=await X(p,(X,S)=>[X.ftOmen('khevang'),!!(X.OMV.khevang&&X.OMV.khevang.g.visible)]);ok(r[0]&&r[1],'điềm báo hiện đom đóm');
await X(p,(X)=>{X.closeSheet&&X.closeSheet()});await p.evaluate(()=>{const c=document.querySelector('.ftr');if(c)c.remove()});
await p.evaluate(()=>{window.__x&&0});await X(p,(X,S)=>{const pp=X.OMV.khevang.g.position;window.__w&&0;});
await X(p,(X,S)=>{const g=X.OMV.khevang.g.position;window.__O&&0;});await p.evaluate(()=>{const X=window.__DCX0.get(),g=X.OMV.khevang.g.position;window.__e.camTo(g.clone(),1.6*window.__e.cam?.zoom||undefined)});await p.waitForTimeout(1500);await p.screenshot({path:SHOT+'/3_diembao_ph.png'});
await X(p,(X)=>X.ftTap('khevang'));await p.waitForTimeout(600);r=await p.evaluate(()=>{const c=document.querySelector('.ftr');return c&&c.innerText});ok(r&&/năm vụ/.test(r),'chạm điềm báo Ngoại kể lại');
ok(p.errs.length===0,'không lỗi '+p.errs[0]);await p.close();
}
// 4. cảnh mở từng cây
for(const k of ['vusua','tretramdot','traucau','duahau','khevang','sodua']){
  const lv={vusua:6,tretramdot:9,traucau:12,duahau:14,khevang:16,sodua:18}[k];
  p=await mk(SV(lv,{ft:{[k]:{st:0,told:0,t:Date.now(),said:1}},ftrD:today}));
  await p.waitForTimeout(800);await p.evaluate(()=>{document.querySelectorAll('.ftr').forEach(e=>e.remove());const n=document.querySelector('#ngoai');if(n)n.hidden=true});
  await p.evaluate(k=>window.__DCX0.get().ftTap(k),k);
  await p.waitForTimeout(1600);await p.screenshot({path:`${SHOT}/4_${k}_a.png`});
  await p.waitForTimeout(1400);await p.screenshot({path:`${SHOT}/4_${k}_b.png`});
  await p.waitForTimeout(1100);await p.screenshot({path:`${SHOT}/4_${k}_c.png`});
  await p.waitForFunction(()=>!!document.querySelector('.ftv'),null,{timeout:180000}).catch(()=>{});r=await p.evaluate(()=>{const v=document.querySelector('.ftv');return v&&v.innerText});ok(r&&r.length>3,`${k}: lật trang Sổ hiện tên truyện (${(r||'').split('\n')[0]})`);
  await p.waitForFunction(()=>!window.__DCX0.get().CERE&&!document.querySelector('.ftv,.ftblk'),null,{timeout:240000}).catch(()=>{});await p.waitForTimeout(1500);r=await p.evaluate(k=>{const X=window.__DCX0.get(),S=window.__O.ST;return [S.ft[k].st,S.ft[k].told,!!X.CERE,!!document.querySelector('.ftblk'),!!document.querySelector('.ftv')]},k);console.log(k,JSON.stringify(r));
  ok(r[0]===1&&r[1]===1&&!r[2]&&!r[3]&&!r[4],`${k}: diễn xong, Ngoại kể đoạn 1, gỡ hết lớp chặn`);
  await p.screenshot({path:`${SHOT}/4_${k}_d.png`});
  ok(p.errs.length===0,`${k}: không lỗi `+p.errs[0]);await p.close();
}
// 5. máy tính: thẻ lời đồn
p=await mk(SV(14,{ftr:{duahau:{t0:old,n:2,last:Date.now()-5*864e5,h:[0,1]},vusua:{t0:old,n:1,last:Date.now(),h:[0]},tretramdot:{t0:old,n:1,last:Date.now(),h:[0]},traucau:{t0:old,n:1,last:Date.now(),h:[0]}},ftrD:''}),{width:1280,height:800});
await p.waitForFunction(()=>document.querySelector('#ngoai').hidden,null,{timeout:90000});await X(p,(X)=>X.ftrCheck());await p.waitForTimeout(800);await p.screenshot({path:SHOT+'/5_loidon_pc.png'});
r=await p.evaluate(()=>{const c=document.querySelector('.ftr');return c&&c.innerText});ok(r&&/tám giờ/.test(r),'nấc 3 dưa hấu nói rõ giờ');
ok(p.errs.length===0,'không lỗi '+p.errs[0]);await p.close();
await b.close();console.log('DONE',bad?bad+' FAIL':'all pass');})();
