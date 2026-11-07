// tNm116: món phơi, sấy, muối mới. node tNm116.js [trang]
const {chromium}=require('playwright');const PAGE=process.argv[2]||'mv2_t116a.html';let bad=0;const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)bad++};const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SV={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1,nong1:1,say1:1},player:{av:1,name:'Q',garden:'Q'},lv:16,xp:80000,xu:50000,inv:{khoqua:9,tep:40,bap:9,caloc:6,oi:15,chuoi:6,khe:18,linh:12},gb:{muoi:6,duong:2,cui:3},seeds:{},plots:{},qd:Object.fromEntries(Array.from({length:14},(_,i)=>[i+3,1])),realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0},ftrD:today,
 nong:{own:1,at:'H3',trays:[null,null,null,null,null,null,null,null],done:3,made:{}},say:{own:1,at:'H5',trays:[null,null],done:3,made:{}},khap:{own:1,at:'H4',jars:[null,null],done:3,made:{}},open:['H3','H4','H5']};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});const p=await b.newPage({viewport:{width:390,height:844}});p.setDefaultTimeout(400000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SV));
await p.goto('http://127.0.0.1:8777/'+PAGE);await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(2000);
const r=await p.evaluate(()=>{const X=window.__DCX0.get(),S=X.ST,out={};const N=X.nong,K=X.khap,L=X.lsay;
 const run=(obj,slots,i,k)=>{obj.put(i,k);const t=slots[i];if(!t)return 'không bỏ vô được';t.t=0;const before=JSON.stringify([S.gb[k]||0,S.inv[k]||0]);const okT=obj.take(i);return okT?'ok':'không lấy ra được '+before};
 ['trakhoqua','tepphoi','bapphoi','khocaloc'].forEach((k,i)=>out[k]=run(N,S.nong.trays,i,k));
 ['oisay','chuoisay'].forEach((k,i)=>out[k]=run(L,S.say.trays,i,k));out.khesay=run(L,S.say.trays,0,'khesay');
 out.mamtep=run(K,S.khap.jars,0,'mamtep');out.mamcalinh=run(K,S.khap.jars,1,'mamcalinh');
 const ks=['trakhoqua','tepphoi','bapphoi','khocaloc','oisay','chuoisay','khesay','mamtep','mamcalinh'];
 return {out,have:ks.map(k=>[k,S.gb[k]||0]),icon:ks.filter(k=>!(window.__x.ICON[k])),sell:ks.map(k=>[k,X.GD(k).sell,X.GD(k).name])}});
console.log(JSON.stringify(r));
for(const [k,v] of Object.entries(r.out))ok(v==='ok',`${k}: ${v}`);
ok(r.have.every(([k,n])=>n>=1),'đồ làm xong nằm trên gác bếp '+JSON.stringify(r.have));ok(r.icon.length===0,'món nào cũng có hình '+r.icon);
ok(r.sell.every(([k,s])=>s>0),'món nào cũng có giá');
await p.evaluate(()=>{const X=window.__DCX0.get();X.openSheet('cho')});await p.waitForTimeout(800);await p.screenshot({path:'/tmp/nm116_cho.png'});
ok(errs.length===0,'không lỗi '+errs[0]);await b.close();console.log('DONE',bad?bad+' FAIL':'all pass');})();
