const {chromium}=require('playwright');const PAGE=process.argv[2]||'mv2_t115m.html';const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
let fails=0;const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)fails++};
const SV=(o={})=>({v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1,don1:1},player:{av:1,name:'Q',garden:'Q'},lv:12,xp:9000,xu:1000,inv:{cai:6,hanh:6},gb:{},seeds:{},plots:{},qd:Object.fromEntries(Array.from({length:10},(_,i)=>[i+3,1])),realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0},...o});
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const mk=async(sv,lang='')=>{const p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:2});p.setDefaultTimeout(240000);p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());await p.addInitScript(([s,l])=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);if(l)localStorage.setItem('mv2-lang',l)},[JSON.stringify(sv),lang]);await p.goto('http://127.0.0.1:8777/'+PAGE);await p.waitForFunction(()=>window.__ready);await p.waitForTimeout(2500);await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>e.hidden=true);document.querySelectorAll('.ddt').forEach(e=>e.classList.remove('on'));window.LVON=false;document.body.classList.remove('lvon')});return p};
const S=p=>p.evaluate(()=>window.__DCX0.get().fxS());
const shot=(p,n)=>p.screenshot({path:`/tmp/fx_${n}.png`,timeout:120000});
const xuSeq=async(p,ms)=>{await p.waitForTimeout(ms);return p.evaluate(()=>{const a=window.__xuSeq||[];window.__xuOb&&window.__xuOb.disconnect();return a})};
const xuWatch=p=>p.evaluate(()=>{const e=document.querySelector('#xu');window.__xuSeq=[e.textContent];window.__xuOb=new MutationObserver(()=>window.__xuSeq.push(e.textContent));window.__xuOb.observe(e,{childList:true,characterData:true,subtree:true})});
const ORD=(id='o1',who='Dì Năm',items=[['cai',2],['hanh',1]])=>({id,who,why:'nấu canh chua',items,xu:120,xp:5});
// 1. hái bằng nút trong bảng: rau bay vô nút Chợ
let p=await mk(SV());
let r=await p.evaluate(()=>{const O=window.__x,g=window.__g,P=O.PLOTS.find(P=>!P.tree&&!P.trellis&&!P.bai&&g.ST.plots[P.id]);const q=g.ST.plots[P.id];q.crop='cai';q.g=9e9;q.moist=1;g.refreshPlot(P.id);O.openSheet('plot',P.id);return P.id});
await p.waitForTimeout(400);const inv0=await p.evaluate(()=>window.__g.ST.inv.cai);
const hv=await p.evaluate(()=>{const b=document.querySelector('[data-a=harvest]');if(!b)return false;b.click();return true});ok(hv,'có nút hái');
await p.waitForTimeout(220);let f=await p.evaluate(()=>[...document.querySelectorAll('.fly.arc')].length);ok(f>=1&&f<=4,`rau đang bay: ${f} món`);await shot(p,'1a');await p.waitForTimeout(250);await shot(p,'1b');
await p.waitForTimeout(900);f=await p.evaluate(()=>document.querySelectorAll('.fly').length);ok(f===0,'bay xong gỡ sạch');ok(await p.evaluate(()=>window.__g.ST.inv.cai)>inv0,'vô kho thật');
// 2. giao đơn: khúc sông, xuồng chèo, số xu chạy
await p.evaluate(O=>{const g=window.__g;g.ST.ord=g.ST.ord||{list:[],acc:0};g.ST.ord.list=[O];g.ST.inv.cai=6;g.ST.inv.hanh=6;g.ST.xu=1000;window.__w.hud();g.openSheet('cho')},ORD());await p.waitForTimeout(600);
await xuWatch(p);await p.evaluate(()=>{const b=document.querySelector('[data-a=ordgive]:not([disabled])');window.__hasOrd=!!b;if(b)b.click()});ok(await p.evaluate(()=>window.__hasOrd),'có nút giao');
const seq=await xuSeq(p,1500);const un=[...new Set(seq)];console.log('xu:',un.join(' > '));ok(un.length>=3,`số xu chạy qua ${un.length} mốc`);
const vis=await p.evaluate(()=>{const v=document.querySelector('.ordgo');return v?v.querySelector('b').textContent:null});console.log('khúc sông:',vis);
await p.evaluate(()=>{});await shot(p,'2c');
await p.waitForTimeout(900);ok(await p.evaluate(()=>!document.querySelector('.ordgo')),'khúc sông tự thu lại');ok((await p.evaluate(()=>document.querySelector('#xu').textContent)).replace(/\D/g,'')==='1120','số xu dừng đúng 1.120');
let s0=await S(p);ok(!s0.xg,'bảng còn mở thì chưa chèo');
await p.evaluate(()=>window.__g.closeSheet());await p.waitForTimeout(1500);s0=await S(p);ok(s0.xg,`đóng bảng: xuồng ra (${s0.xgN} khối)`);await p.waitForTimeout(2500);const s1=await S(p);console.log('xuồng x',s0.xgx,'>',s1.xgx);ok(s1.xgx>s0.xgx,'xuồng chèo đi');await shot(p,'2d');await p.waitForTimeout(3000);await shot(p,'2e');
ok(p.errs.length===0,'không lỗi '+p.errs[0]);await p.close();
// 3. chụp từng khung khúc sông
p=await mk(SV());await p.evaluate(O=>{const g=window.__g;g.ST.ord=g.ST.ord||{list:[],acc:0};g.ST.ord.list=[O,{...O,id:'o2',who:'Chú Ba'}];g.ST.inv.cai=8;g.ST.inv.hanh=6;g.openSheet('cho')},ORD());await p.waitForTimeout(600);await shot(p,'3a');
await p.evaluate(()=>document.querySelector('[data-a=ordgive]:not([disabled])').click());await p.waitForTimeout(150);await shot(p,'3b');await p.waitForTimeout(300);await shot(p,'3c');await p.waitForTimeout(350);await shot(p,'3d');
ok(p.errs.length===0,'không lỗi '+p.errs[0]);await p.close();
// 4. ghe bẹo nhổ sào
p=await mk(SV({ghe:{d:today,o:{who:'Ghe bẹo cô Sáu',items:[['cai',2]],xu:200,xp:5,ghe:1,seen:Date.now()},done:0}}));
await p.evaluate(()=>{const g=window.__g;g.ST.ghe.d=window.__e.GHE?g.ST.ghe.d:g.ST.ghe.d;g.ST.inv.cai=6;window.__e.camTo(new (g.T.Vector3)(6,.3,9),1.4)});await p.waitForTimeout(2500);await shot(p,'4a');
let g0=await S(p);ok(g0.ghev,'ghe đang đậu');await p.evaluate(()=>{window.__g.openSheet('cho');window.__e.gheGive(document.body)});await p.waitForTimeout(800);let g1=await S(p);ok(g1.ggo&&g1.ghev&&g1.ghex===g0.ghex,'giao đủ, bảng còn mở: ghe chờ');
await p.evaluate(()=>window.__g.closeSheet());await p.waitForTimeout(3500);let g2=await S(p);console.log('ghe x',g0.ghex,'>',g2.ghex);ok(g2.ghex>g0.ghex&&g2.ggo,'đóng bảng: ghe nhổ sào đi');await shot(p,'4b');await p.evaluate(()=>{});ok(p.errs.length===0,'không lỗi '+p.errs[0]);await p.close();
// 5. pháo hoa khi đóng thẻ lên cấp
p=await mk(SV());await p.evaluate(()=>window.__x.levelUp(13));await p.waitForTimeout(1600);ok(await p.evaluate(()=>!document.querySelector('.lvup').hidden),'thẻ lên cấp hiện');ok(!(await S(p)).fw,'thẻ còn mở: chưa bắn');await p.evaluate(()=>document.querySelector('#lvOk').click());
await p.waitForTimeout(500);ok((await S(p)).fw&&await p.evaluate(()=>!!document.querySelector('#fwC')),'đóng thẻ: pháo hoa');
for(const n of ['5a','5b','5c','5d']){await p.waitForTimeout(450);await shot(p,n)}
const tt=Date.now();await p.waitForFunction(()=>!document.querySelector('#fwC'),null,{timeout:30000}).catch(()=>{});ok(await p.evaluate(()=>!document.querySelector('#fwC')),`bắn xong tự gỡ lớp vẽ (${Date.now()-tt}ms)`);
ok(p.errs.length===0,'không lỗi '+p.errs[0]);await p.close();
// 6. giảm chuyển động: bỏ bay, số nhảy thẳng
const c6=await b.newContext({reducedMotion:'reduce',viewport:{width:390,height:844}});p=await c6.newPage();p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SV()));await p.goto('http://127.0.0.1:8777/'+PAGE);await p.waitForFunction(()=>window.__ready);await p.waitForTimeout(2500);
await p.evaluate(O=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>e.hidden=true);const g=window.__g;g.ST.ord=g.ST.ord||{list:[],acc:0};g.ST.ord.list=[O];g.ST.inv.cai=6;g.ST.inv.hanh=6;g.ST.xu=1000;window.__w.hud();g.openSheet('cho')},ORD());await p.waitForTimeout(500);await p.evaluate(()=>document.querySelector('[data-a=ordgive]:not([disabled])').click());await p.waitForTimeout(120);
r=await p.evaluate(()=>[document.querySelectorAll('.fly').length,!!document.querySelector('.ordgo'),document.querySelector('#xu').textContent]);ok(r[0]===0&&!r[1]&&r[2].replace(/\D/g,'')==='1120',`giảm chuyển động: ${JSON.stringify(r)}`);ok(p.errs.length===0,'không lỗi '+p.errs[0]);await c6.close();
// 7. tiếng Anh
p=await mk(SV(),'en');await p.evaluate(O=>{const g=window.__g;g.ST.ord=g.ST.ord||{list:[],acc:0};g.ST.ord.list=[O];g.ST.inv.cai=6;g.ST.inv.hanh=6;g.openSheet('cho')},ORD());await p.waitForTimeout(600);await p.evaluate(()=>{document.querySelector('[data-a=ordgive]:not([disabled])').click()});await p.waitForTimeout(250);const en=await p.evaluate(()=>{const v=document.querySelector('.ordgo');return v?v.querySelector('b').textContent:null});console.log('EN:',en);ok(en&&!/chèo|xuồng/.test(en),'tiếng Anh khúc sông');await shot(p,'7a');ok(p.errs.length===0,'không lỗi '+p.errs[0]);await p.close();
console.log(fails?`DONE ${fails} FAIL`:'DONE all pass');await b.close()})();
