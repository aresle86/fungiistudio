// tSc117: sân cỏ (đất thổ cư) và giá khai hoang mới. node tSc117.js [trang]
const {chromium}=require('playwright');const PAGE=process.argv[2]||'mv2_t117a.html';let bad=0;const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)bad++};const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SV=(lv,x)=>({v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1,sap1:1},player:{av:1,name:'Q',garden:'Q'},lv,xp:90000,xu:3000,inv:{},gb:{},seeds:{cai:5},plots:{},qd:Object.fromEntries(Array.from({length:Math.max(0,lv-2)},(_,i)=>[i+3,1])),realTime:true,spd:1,real:Date.now(),dd:{last:today,n:3,full:0},ftrD:today,dc:{rao:'rao_tre',ga:'ga_tre',vit:'vit_mac',own:{},bag:{ghe_da:2,lu_da_luon:1,chai_la:1},items:[]},...x});
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
const mk=async(sv)=>{const p=await b.newPage({viewport:{width:390,height:844}});p.setDefaultTimeout(400000);p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());await p.addInitScript(s=>{if(!localStorage.getItem('mv2-state')){localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)}},JSON.stringify(sv));await p.goto('http://127.0.0.1:8777/'+PAGE);await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(2000);await p.evaluate(()=>document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>e.hidden=true));return p};
const E=(p,f)=>p.evaluate(`(()=>{const X=window.__DCX0.get(),S=X.ST;return (${f})(X,S)})()`);
// cấp 6: chưa có sân cỏ
let p=await mk(SV(6,{}));let r=await E(p,(X,S)=>[Object.values(X.PL).filter(P=>P.co).length,X.PL.K1&&X.sapFree('K1',{t:'dc',k:'ghe_da'})]);ok(r[0]===7,'có 7 chỗ sân cỏ');ok(!r[1],'cấp 6 chưa đặt được');await p.close();
// cấp 7: mua, đặt, giá tăng dần
p=await mk(SV(7,{}));
r=await E(p,(X,S)=>{const out={};out.c0=X.coCost();out.free0=X.sapFree('K1',{t:'dc',k:'ghe_da'});out.put0=X.dcPlace('ghe_da','K1');out.buy=X.coBuy('K1');out.xu=S.xu;out.c1=X.coCost();out.put=X.dcPlace('ghe_da','K1');out.items=S.dc.items.map(i=>i.at);
 out.obj=X.sapFree('K2',{t:'obj',k:'nong'});X.coBuy('K2');out.obj2=X.sapFree('K2',{t:'obj',k:'nong'});out.big=X.bigFit('K2','ao');out.why=X.sapFree('K2',{t:'dc',k:'lu_da_luon'});
 out.land=[...Array(3)].map((_,i)=>0);return out});
console.log(JSON.stringify(r));
ok(r.c0===500,'miếng đầu 500 xu');ok(!r.free0&&!r.put0,'chưa mua thì chưa đặt được');ok(r.buy&&r.xu===2500,'mua được, trừ 500 xu');ok(r.c1===565,'miếng sau mắc hơn ('+r.c1+')');ok(r.put&&r.items.includes('K1'),'đặt ghế đá lên sân cỏ');
ok(!r.obj2,'không đặt nong phơi lên sân cỏ');ok(!r.big,'không đào ao trên sân cỏ');ok(r.why,'sân cỏ trống còn đặt đồ được');
// chạm sân cỏ ngoài chế độ Sắp vườn không mở bảng đắp liếp; cầm hạt không sáng sân cỏ
r=await E(p,(X,S)=>{const v=X.PV.K2;return {want:v.want,bed:v.bedG&&v.bedG.visible,mow:v.mow&&v.mow.visible,locked:true}});ok(!r.want&&!r.bed&&!r.mow,'sân cỏ không hiện liếp, cọc tre, bong bóng');
// Sắp vườn: thấy chỗ chưa mua có nút đồng xu
await E(p,(X)=>X.sapMode(true));await p.waitForTimeout(1500);r=await p.evaluate(()=>[document.querySelectorAll('#sapSvg .cobuy').length,document.querySelectorAll('.sapplus.cob').length]);ok(r[0]>=1&&r[1]>=1,'Sắp vườn có chỗ chưa mua với nút đồng xu '+r);
await p.screenshot({path:'/tmp/sc117_sap.png'});
// giá khai hoang mới
r=await E(p,(X,S)=>{const L=X.ST.land||{};return 0});
// lưu rồi mở lại
await p.evaluate(()=>{window.__DCX0.get();});await p.reload();await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(2000);
r=await E(p,(X,S)=>[S.coOwn,S.dc.items.map(i=>i.k+'@'+i.at)]);ok(r[0].includes('K1')&&r[0].includes('K2')&&r[1].includes('ghe_da@K1'),'mở lại vẫn còn đất và ghế đá '+JSON.stringify(r));
ok(p.errs.length===0,'không lỗi '+p.errs[0]);await p.close();
// giá khai hoang: ô đầu bãi hông nhà 200 xu
p=await mk(SV(7,{}));r=await p.evaluate(()=>{const X=window.__DCX0.get();X.openSheet('plot','H5');return document.querySelector('.sheet')&&document.querySelector('.sheet').innerText.replace(/\s+/g,' ')});ok(/200 xu/.test(r||''),'khai hoang ô đầu 200 xu: '+(r||'').slice(0,160));ok(!/nửa tiền/.test(r||''),'không còn câu nửa tiền');
ok(p.errs.length===0,'không lỗi '+p.errs[0]);await p.close();
await b.close();console.log('DONE',bad?bad+' FAIL':'all pass');})();
