// v107 đổi công: vườn bạn chín hết vẫn đổi công được bằng "hái giùm"; chủ vườn nhận rau qua hộp thư. Server được giả lập.
// dựng trang: cat x40f.js x106.js xpop.js > /tmp/x.js; python3 gen_test2.py /tmp/x.js live/v107a.html lp/mv2_t107.html
const {chromium}=require('playwright');
const PAGE=process.env.PAGE||'mv2_t107.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const ME={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:10,xp:4300,xu:900,inv:{},seeds:{},plots:{},qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1},realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});let bad=0;
const ok=(c,m)=>{console.log(`${c?'OK ':'SAI'} ${m}`);if(!c) bad++;};
const mk=async(init,arg,inbox)=>{const p=await b.newPage({viewport:{width:900,height:640}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.setDefaultTimeout(180000);
 const calls=[];
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),async r=>{const u=r.request().url();const m=u.match(/rpc\/(mv2_\w+)/);if(!m) return r.abort();let body=null;try{body=JSON.parse(r.request().postData()||'{}')}catch(e){}calls.push([m[1],body]);
  const res={mv2_act:{ok:true,left:4},mv2_inbox:inbox||[],mv2_ack:null}[m[1]];return r.fulfill({status:200,contentType:'application/json',body:JSON.stringify(res===undefined?null:res)});});
 await p.addInitScript(init,arg);await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(1200);return {p,errs,calls};};
// ---- 1) người ghé: vườn bạn toàn liếp chín ----
{const {p,errs,calls}=await mk(([me])=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',me);localStorage.setItem('mv2-cloud',JSON.stringify({code:'MEME',secret:'s'}));
  const st=JSON.parse(me);st.player={av:2,name:'Tư',garden:'Tư'};sessionStorage.setItem('mv2-visit',JSON.stringify({kind:'ban',code:'TUTU',owner:'Tư',name:'Vườn Tư',myLv:10,left:5,cong:0,state:st,loot:{inv:{},xp:0,water:0,friend:'Tư',giftOut:[]}}));},[JSON.stringify(ME)]);
 const ids=await p.evaluate(()=>{const g=window.__g,V=window.__V,ids=window.__G.PLOTS.filter(P=>!P.tree&&!P.trellis&&!P.bai&&g.ST.plots[P.id]).slice(0,3).map(P=>P.id);
  for(const id of ids){const q=g.ST.plots[id];q.crop='cai';q.g=V.CROPS.cai.grow+10;q.moist=1;g.refreshPlot(id);}return ids;});
 ok(ids.length===3,'có 3 liếp chín để thử: '+ids.join(','));
 await p.waitForTimeout(1500);
 const intro=await p.evaluate(()=>window.__V.SAY);ok(/hái giùm/.test(intro),'Ngoại giới thiệu có "hái giùm": '+intro);
 const r1=await p.evaluate(async id=>{const V=window.__V;await V.visitTap(id);const S=V.VISIT;return {cong:S.cong,help:S.loot.help,crop:window.__g.ST.plots[id].crop,info:document.querySelector('#vInfo').textContent};},ids[0]);
 ok(r1.cong===1&&r1.help===1&&!r1.crop,`chạm liếp chín khi chưa có công = hái giùm (công ${r1.cong}, hái giùm ${r1.help}, liếp ${r1.crop||'trống'}) · ${r1.info}`);
 ok(calls.some(c=>c[0]==='mv2_act'&&c[1]&&c[1].p_kind==='help'),'gửi server loại help');
 const r2=await p.evaluate(async id=>{const V=window.__V;await V.visitTap(id);const S=V.VISIT;return {cong:S.cong,inv:JSON.stringify(S.loot.inv),crop:window.__g.ST.plots[id].crop};},ids[1]);
 ok(r2.cong===0&&/cai/.test(r2.inv),`liếp thứ hai = hái ké đem về (công ${r2.cong}, túi ${r2.inv})`);
 ok(!errs.length,'không lỗi trang '+errs.join(' | '));await p.close();}
// ---- 2) chủ vườn: hộp thư có help ----
{let pid=null;const {p,errs}=await mk(([me])=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',me);localStorage.setItem('mv2-cloud',JSON.stringify({code:'MEME',secret:'s'}));},[JSON.stringify(ME)],
  [{id:1,code:'TUTU',name:'Tư',kind:'help',payload:{id:'__PID__',k:'cai',n:3}}]);
 // đặt liếp chín rồi gọi hộp thư với đúng id liếp
 const r=await p.evaluate(async()=>{const g=window.__g,V=window.__V,P=window.__G.PLOTS.find(P=>!P.tree&&!P.trellis&&!P.bai&&g.ST.plots[P.id]);const q=g.ST.plots[P.id];q.crop='cai';q.g=V.CROPS.cai.grow+10;q.moist=1;g.refreshPlot(P.id);
  const f0=window.fetch;window.fetch=(u,o)=>f0(u,o).then(async res=>{if(/mv2_inbox/.test(u)){const t=(await res.text()).replace('__PID__',P.id);return new Response(t,{status:200,headers:{'Content-Type':'application/json'}});}return res;});
  const inv0=g.ST.inv.cai||0;await V.cloudInbox();await new Promise(r=>setTimeout(r,1500));const SY=window.__SY,H=[...(window.__H.SAYH||[]).map(h=>h.t||h),...(SY.SAYQ||[]).map(q=>q[0]),...(SY.IDLEQ||[]).map(q=>q[0])].join(' / ');return {inv0,inv:g.ST.inv.cai||0,crop:q.crop||g.ST.plots[P.id].crop,say:H+' / '+V.SAY};});
 ok(r.inv>r.inv0&&!r.crop,`chủ vườn nhận rau vô kho (cải ${r.inv0} → ${r.inv}), liếp ${r.crop||'trống'}`);
 ok(/hái giùm/.test(r.say)&&!/đòi nợ/.test(r.say),'Ngoại báo hái giùm, không nhắc đòi nợ: '+r.say);
 ok(!errs.length,'không lỗi trang '+errs.join(' | '));await p.close();}
console.log('DONE',bad,'chỗ sai');await b.close();})();
