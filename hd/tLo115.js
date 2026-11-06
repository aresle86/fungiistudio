const {chromium}=require('playwright');const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());const PAGE=process.argv[2]||'mv2_t115i.html';
let fails=0;const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)fails++};
const SV=(vit,lo,inv={trungvit:4},gb={cui:1})=>({v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:16,xp:20000,xu:1000,inv,gb,seeds:{},plots:{},qd:Object.fromEntries(Array.from({length:14},(_,i)=>[i+3,1])),vit:{n:vit[0],lv:vit[1],trough:8,eggs:0,acc:0,fixed:1},lo,realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}});
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const mk=async(sv,lang='')=>{const p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:2});p.setDefaultTimeout(240000);p.errs=[];p.on('pageerror',e=>p.errs.push(e.message));await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());await p.addInitScript(([s,l])=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);if(l)localStorage.setItem('mv2-lang',l)},[JSON.stringify(sv),lang]);await p.goto('http://127.0.0.1:8777/'+PAGE);await p.waitForFunction(()=>window.__ready);await p.waitForTimeout(2500);await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>e.hidden=true);document.querySelectorAll('.ddt').forEach(e=>e.classList.remove('on'));window.__x.openSheet('lo')});await p.waitForTimeout(500);return p};
const st=p=>p.evaluate(()=>{const S=window.__DCX0.get().ST;return {xu:S.xu,n:S.vit.n,on:S.lo.on,t:S.lo.t,hatch:S.lo.hatch,ln:S.lo.n,egg:S.inv.trungvit||0,cui:(S.gb||{}).cui||0}});
const btn=(p,a)=>p.evaluate(a=>{const e=document.querySelector(`[data-a="${a}"]`);return e?{t:e.textContent.trim(),dis:e.disabled}:null},a);
const txt=p=>p.evaluate(()=>document.querySelector('#ngoaiTxt').textContent);
const fin=p=>p.evaluate(()=>{const S=window.__DCX0.get().ST;S.lo.t=0;S.lo.hatch=S.lo.n;window.__x.openSheet('lo')});
const clk=async(p,a)=>{await p.evaluate(a=>document.querySelector(`[data-a="${a}"]`).click(),a);await p.waitForTimeout(500)};
const body=p=>p.evaluate(()=>document.querySelector('.sheet').innerText);
// 1. chuồng 12/12, mức cao nhất
let p=await mk(SV([12,2],{t:0,on:0,done:3,hatch:0}));let x=await btn(p,'loput');ok(x&&!x.dis&&/Ấp 4/.test(x.t),`12/12 nút ấp bấm được: ${JSON.stringify(x)}`);let bd=await body(p);ok(/Chuồng đầy, nở dư thì Ngoại bán giùm 40 xu/.test(bd),'12/12 báo trước sẽ bán giùm');await p.screenshot({path:'/tmp/lo_1.png'});
await clk(p,'loput');let s=await st(p);ok(s.on&&s.egg===0&&s.cui===0&&s.ln===4,`12/12 vô lò đủ 4 trứng: ${JSON.stringify(s)}`);
await fin(p);await p.waitForTimeout(400);x=await btn(p,'lohatch');ok(x&&!x.dis&&/Nhờ Ngoại bán 4/.test(x.t),`nở: nút nhờ bán: ${x&&x.t}`);bd=await body(p);ok(!/Muốn giữ/.test(bd),'12/12 không gợi ý nới chuồng');await p.waitForTimeout(1500);await p.screenshot({path:'/tmp/lo_2.png'});
await clk(p,'lohatch');s=await st(p);ok(s.xu===1160&&s.n===12&&!s.on&&!s.hatch,`bán 4 con +160 xu: ${JSON.stringify(s)}`);ok(/4 con vịt con Ngoại bán/.test(await txt(p)),'Ngoại báo: '+await txt(p));ok(p.errs.length===0,'không lỗi '+p.errs[0]);await p.close();
// 2. bản lưu đang kẹt: lò có vịt nở, chuồng 12/12
p=await mk(SV([12,2],{t:0,on:1,done:3,hatch:3,n:4,T:64800}));x=await btn(p,'lohatch');ok(x&&!x.dis,`kẹt cũ: nút bấm được ${x&&x.t}`);await clk(p,'lohatch');s=await st(p);ok(s.xu===1120&&!s.on&&!s.hatch,`kẹt cũ gỡ được +120: ${JSON.stringify(s)}`);ok((await btn(p,'loput')),'lò trống lại');await p.close();
// 3. còn 1 chỗ, chưa nới hết: 1 con vào chuồng, 3 con bán, có gợi ý nới
p=await mk(SV([3,0],{t:0,on:1,done:3,hatch:4,n:4,T:64800}));bd=await body(p);ok(/Chuồng còn 1 chỗ, dư 3 con/.test(bd)&&/Muốn giữ thì nới chuồng/.test(bd),'còn 1 chỗ: báo rõ, gợi ý nới');x=await btn(p,'lohatch');ok(/Bắt vịt con/.test(x.t),'nút vẫn là bắt');await p.screenshot({path:'/tmp/lo_3.png'});await clk(p,'lohatch');s=await st(p);ok(s.n===4&&s.xu===1120&&!s.on,`1 vào chuồng, 3 bán: ${JSON.stringify(s)}`);await p.close();
// 4. chuồng rộng: không bán con nào
p=await mk(SV([2,1],{t:0,on:1,done:3,hatch:4,n:4,T:64800}));await clk(p,'lohatch');s=await st(p);ok(s.n===6&&s.xu===1000&&!s.on,`đủ chỗ: 4 vào chuồng, không bán: ${JSON.stringify(s)}`);ok(/Nở 4 con/.test(await txt(p)),'câu cũ');await p.close();
// 5. thiếu trứng vẫn khóa
p=await mk(SV([3,0],{t:0,on:0,done:3,hatch:0},{trungvit:2}));x=await btn(p,'loput');ok(x.dis,'thiếu trứng: khóa');await p.close();
// 6. tiếng Anh
p=await mk(SV([12,2],{t:0,on:1,done:3,hatch:4,n:4,T:64800}),'en');await p.evaluate(()=>{const d=[...document.querySelectorAll('.sheet details')];d.forEach(e=>e.open=true)});await p.waitForTimeout(300);bd=await body(p);console.log(bd.slice(0,700));ok(!/Chuồng|Ngoại|Nhờ|nở|\bcon\b/.test(bd),'tiếng Anh không sót chữ Việt');await p.screenshot({path:'/tmp/lo_4.png'});await p.close();
console.log(fails?`DONE ${fails} FAIL`:'DONE all pass');await b.close()})();
