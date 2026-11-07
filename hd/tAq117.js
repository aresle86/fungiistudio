// tAq117: chất lượng đồ hoạ tự hạ khi máy đuối, tự nâng khi mát lại. node tAq117.js [trang]
const {chromium}=require('playwright');const PAGE=process.argv[2]||'mv2_t117a.html';let bad=0;const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)bad++};const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SV={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:10,xp:90000,xu:3000,inv:{},gb:{},seeds:{},plots:{},qd:Object.fromEntries(Array.from({length:8},(_,i)=>[i+3,1])),realTime:true,spd:1,real:Date.now(),dd:{last:today,n:3,full:0},ftrD:today};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});const p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:2});p.setDefaultTimeout(400000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','2');localStorage.setItem('mv2-state',s)},JSON.stringify(SV));
await p.goto('http://127.0.0.1:8777/'+PAGE);await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(2000);
const r=await p.evaluate(()=>{const X=window.__DCX0.get(),A=X.AQ,R=X.r,out={};const snap=()=>[A.lv,R.getPixelRatio(),R.shadowMap.enabled,X.aqQ().sh];
 X.aqSet(0);out.l0=snap();
 // giả lập máy đuối: 4 lần đo liền, mỗi lần 2 giây chỉ có 12 hình (6 hình/giây)
 A.t0=0;A.bad=0;A.good=0;let fn=100000;X.AQ.lv=0;window.__aqT=fn;const run=(sec,fps)=>{const n=Math.round(sec*fps);const step=1000/fps;for(let i=0;i<n;i++){fn+=step;window.__DCX0.get();A.t0===0?(A.t0=fn,A.n=0):0;X.aqTick?0:0;}};
 return {l0:out.l0}});
console.log(JSON.stringify(r));ok(r.l0[0]===0&&r.l0[1]===2&&r.l0[2]===true&&r.l0[3]===4096,'mặc định giữ chất lượng cao: '+JSON.stringify(r.l0));
const s=await p.evaluate(()=>{const X=window.__DCX0.get(),A=X.AQ,R=X.r;const out=[];for(const l of [1,2,3,2,0]){X.aqSet(l);out.push([l,A.lv,R.getPixelRatio(),R.shadowMap.enabled,X.aqQ().sh])}return out});
console.log(JSON.stringify(s));ok(s[0][4]===1024&&s[0][2]===2,'bậc 1: bóng đổ nhẹ hơn, giữ độ nét');ok(s[1][2]===1.25,'bậc 2: độ nét 1,25');ok(s[2][2]===1&&s[2][3]===false,'bậc 3: độ nét 1, tắt bóng');ok(s[4][2]===2&&s[4][3]===true&&s[4][4]===4096,'nâng về lại đủ chất lượng');
const u=await p.evaluate(()=>{const X=window.__DCX0.get(),A=X.AQ;X.aqSet(0);A.t0=0;A.bad=0;A.good=0;let fn=100000;const run=(sec,fps)=>{const n=Math.round(sec*fps);for(let i=0;i<n;i++){fn+=1000/fps;X.aqTick(fn,0);}};
 const o={};run(2,60);run(6,10);o.short=A.lv;run(4,10);o.after8=A.lv;run(20,60);o.notYet=A.lv;run(45,60);o.back=A.lv;window.__stop=1;return o});
console.log(JSON.stringify(u));ok(u.short===0,'đuối 6 giây thì chưa hạ');ok(u.after8===1,'đuối khoảng 8 giây thì hạ một bậc');ok(u.notYet===1,'mát lại 20 giây chưa nâng');ok(u.back===0,'mát lại 1 phút thì nâng lại');
await p.evaluate(()=>{window.__stop=0;window.__DCX0.get().aqSet(0)});await p.waitForTimeout(20000);const t=await p.evaluate(()=>{const A=window.__DCX0.get().AQ;return {lv:A.lv,fps:A.fps,log:A.log}});console.log('máy test thật',JSON.stringify(t));
ok(errs.length===0,'không lỗi '+errs[0]);await b.close();console.log('DONE',bad?bad+' FAIL':'all pass');})();
