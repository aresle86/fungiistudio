// v107 hố ủ: hốt phân chuồng gà vịt (6 tiếng 1 phần, tối đa 4) thay "bỏ rau dư"; hái liếp đất mệt thì hiện "Đất mệt · hụt N"
// dựng trang: cat x40f.js x106.js xpop.js > /tmp/x.js; python3 gen_test2.py /tmp/x.js live/v107a.html lp/mv2_t107.html
const {chromium}=require('playwright');
const PAGE=process.env.PAGE||'mv2_t107.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:13,xp:9300,xu:2000,inv:{},seeds:{},plots:{},
 qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1},land:{H1:{st:'own'},H2:{st:'own'},H3:{st:'own'}},open:[],
 ho:{own:1,at:'H3',mat:0,bags:0,t:0,done:0,pct:Date.now()-13*3600e3},ga:{hens:2,rooster:1,trough:4,eggs:0,acc:0,lv:0,brood:null,fixed:1},
 realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});let bad=0;
const ok=(c,m)=>{console.log(`${c?'OK ':'SAI'} ${m}`);if(!c) bad++;};
const p=await b.newPage({viewport:{width:390,height:664},deviceScaleFactor:2,hasTouch:true});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.setDefaultTimeout(180000);
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(1500);
await p.evaluate(()=>window.__g.openSheet('ho'));await p.waitForTimeout(400);await p.screenshot({path:'../ho107_1.png'});
const b1=await p.evaluate(()=>{const e=document.querySelector('[data-a=hophan]');return {btn:!!e,txt:e?e.innerText.replace(/\n/g,' '):'',dis:e?e.disabled:null,rau:!!document.querySelector('[data-a=horau]')};});
ok(b1.btn&&!b1.dis&&/2 phần/.test(b1.txt)&&!b1.rau,`nút hốt phân chuồng (${b1.txt}), không còn nút bỏ rau dư`);
await p.click('[data-a=hophan]');await p.waitForTimeout(400);
const r1=await p.evaluate(()=>({mat:window.__g.ST.ho.mat,left:document.querySelector('[data-a=hophan]')&&document.querySelector('[data-a=hophan]').innerText.replace(/\n/g,' ')}));
ok(r1.mat===2,`hố ủ +2 phần (${r1.mat}), nút còn: ${r1.left}`);
// liếp đất mệt
const r2=await p.evaluate(async()=>{const g=window.__g,V=window.__V,P=window.__G.PLOTS.find(P=>!P.tree&&!P.trellis&&!P.bai&&g.ST.plots[P.id]);const q=g.ST.plots[P.id];q.crop='cai';q.g=V.CROPS.cai.grow+10;q.moist=1;q.soil=.15;g.refreshPlot(P.id);g.closeSheet();
 g.act.harvest(P.id);await new Promise(r=>setTimeout(r,900));return {fl:[...document.querySelectorAll('#fx .fl')].map(e=>e.textContent).join(' | '),seen:!!g.ST.seen.datmet};});
ok(/Đất mệt · hụt/.test(r2.fl)&&r2.seen,`hái liếp đất mệt: ${r2.fl} · Ngoại giải thích ${r2.seen}`);
// gác bếp: mua thêm kệ
const r3=await p.evaluate(async()=>{const g=window.__g;g.ST.gb.muoi=2;window.__w.openBook('kho');await new Promise(r=>setTimeout(r,300));const b=document.querySelector('[data-b=gbx]');const t0=b?b.textContent:'';if(b) b.click();await new Promise(r=>setTimeout(r,300));const b2=document.querySelector('[data-b=gbx]');return {t0,gbx:g.ST.gbx,xu:g.ST.xu,t1:b2?b2.textContent:'',cap:(document.querySelector('#bk').innerText.match(/Gác bếp · \d+\/(\d+)/)||[])[1]};});
ok(/150 xu/.test(r3.t0)&&r3.gbx===1&&r3.xu===1850&&r3.cap==='30'&&/250 xu/.test(r3.t1),`thêm kệ gác bếp: ${r3.t0} → kệ ${r3.gbx}, xu ${r3.xu}, sức chứa ${r3.cap}, nút kế ${r3.t1}`);
ok(!errs.length,'không lỗi trang '+errs.join(' | '));
console.log('DONE',bad,'chỗ sai');await b.close();})();
