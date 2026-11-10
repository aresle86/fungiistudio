// v129: tải vườn từ mạng phải giữ đúng mốc giờ của bản trên mạng (cây lớn bù đúng thời gian vắng, không bù hai lần, đồng hồ lệch không làm hỏng)
const {chromium}=require('playwright');const PAGE=process.env.PAGE||'mv2_t129.html';
const SV=(lv,xu,xp,rev,real,gt)=>({v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1,sap1:1},player:{av:1,name:'Q',garden:'Q'},spd:1,lv,xu,xp,rev,gt:gt||0,real:real||Date.now(),inv:{},gb:{},seeds:{},plots:{a:1},qd:{},land:{},dc:{}});
let bad=0;const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)bad++};
(async()=>{const b=await chromium.launch({args:['--use-angle=metal','--enable-gpu','--ignore-gpu-blocklist']});
const run=async(name,local,server,rev0,again)=>{const c=await b.newContext({viewport:{width:390,height:844}});const p=await c.newPage();p.setDefaultTimeout(180000);const e=[];p.on('pageerror',x=>e.push(x.message));let srv={rev:server.rev,data:server};
 await p.route(u=>!u.href.startsWith('http://127.0.0.1')||u.href.includes('/rpc/'),r=>{const u=r.request().url();const m=u.match(/rpc\/(mv2_\w+)/);if(!m)return r.abort();let q={};try{q=JSON.parse(r.request().postData()||'{}')}catch(x){}if(m[1]==='mv2_save2'){if(q.p_rev<=srv.rev)return r.fulfill({json:{ok:false,stale:true,rev:srv.rev}});srv={rev:q.p_rev,data:q.p_data};return r.fulfill({json:{ok:true}})}if(m[1]==='mv2_restore')return r.fulfill({json:srv});return r.fulfill({json:m[1]==='mv2_inbox'?[]:{ok:true}})});
 await p.addInitScript(([s,rv])=>{if(sessionStorage.getItem('t'))return;sessionStorage.setItem('t','1');localStorage.clear();localStorage.setItem('mv3d-q','0');localStorage.setItem('mv2-lang','vi');localStorage.setItem('mv2-state',s);localStorage.setItem('mv2-cloud',JSON.stringify({code:'MV-TEST',secret:'AAAABBBBCCCC'}));localStorage.setItem('mv2-rev',String(rv))},[JSON.stringify(local),rev0]);
 const t0=Date.now();await p.goto('http://127.0.0.1:8777/'+PAGE,{timeout:300000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(9000);await p.waitForFunction(()=>window.__ready&&window.__DCX0,null,{timeout:400000});await p.waitForTimeout(5000);await p.waitForFunction(()=>window.__ready&&window.__DCX0,null,{timeout:400000});
 const rd=()=>p.evaluate(()=>{const G=window.__g;return {lv:G.ST.lv,gt:G.ST.gt,real:G.ST.real,now:Date.now()}});
 let r=await rd();r.el=(Date.now()-t0)/1000;
 if(again){await p.reload();await p.waitForFunction(()=>window.__ready&&window.__DCX0,null,{timeout:400000});await p.waitForTimeout(4000);r.b=await rd();r.el2=(Date.now()-t0)/1000}
 console.log(' ',name,JSON.stringify(r));await c.close();return {r,e}};
const now=Date.now(),H=3600;
let x=await run('bản mạng lưu 2 tiếng trước',SV(5,100,300,9,now,50),{...SV(12,5000,9000,12,now-2*H*1000,1000),rev:12},9,true);
ok(x.r.lv===12,'đã tải bản mạng');ok(x.r.gt>=1000+2*H-5&&x.r.gt<=1000+2*H+x.r.el+30,'cây lớn bù đúng 2 tiếng vắng (gt '+Math.round(x.r.gt)+')');
ok(x.r.b.gt-x.r.gt<=x.r.el2+30,'mở lại không bù lần hai (thêm '+Math.round(x.r.b.gt-x.r.gt)+' giây)');ok(x.r.real<=x.r.now,'mốc giờ không vượt hiện tại');ok(!x.e.length,'không lỗi '+x.e[0]);
x=await run('đồng hồ máy kia chạy nhanh 1 tiếng',SV(5,100,300,9,now,50),{...SV(12,5000,9000,12,now+H*1000,1000),rev:12},9);
ok(x.r.lv===12&&x.r.gt>=1000&&x.r.gt<=1000+x.r.el+30,'mốc giờ ở tương lai: không bù, không âm (gt '+Math.round(x.r.gt)+')');ok(x.r.real<=x.r.now,'mốc giờ được kéo về hiện tại');
x=await run('bản mạng lưu 30 ngày trước',SV(5,100,300,9,now,50),{...SV(12,5000,9000,12,now-30*86400*1000,1000),rev:12},9);
ok(x.r.lv===12&&x.r.gt>=1000+7*86400-5&&x.r.gt<=1000+7*86400+x.r.el+30,'vắng lâu: bù tối đa 7 ngày (gt '+Math.round(x.r.gt)+')');ok(!x.e.length,'không lỗi '+x.e[0]);
console.log(bad?'CÓ SAI '+bad:'DONE all pass');await b.close();process.exit(bad?1:0)})().catch(x=>{console.error('CRASH',x.message.slice(0,300));process.exit(2)});
