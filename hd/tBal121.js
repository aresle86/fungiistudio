// tBal121: sầu riêng mở cấp 22, dừa sáp cấp 24, mỗi cây có món cùng cấp (có biểu tượng, tên tiếng Anh, nấu thử được); lá dừa tối đa 6, tre 5. node tBal121.js [trang]
const {chromium}=require('playwright');const fs=require('fs');const PAGE=process.argv[2]||'mv2_t121a.html';let bad=0;const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)bad++};const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const src=fs.readFileSync('lp/'+PAGE,'utf8');
ok(/saurieng: 22, duasap: 24 \}\);/.test(src),'UNLOCK: sầu riêng 22, dừa sáp 24');
ok(/ladua: \{[^}]*max: 6,/.test(src)&&/tredon: \{[^}]*max: 5,/.test(src),'bản đồ chứa tối đa 6 lá dừa, 5 cây tre');
ok(/"chesaurieng": "Durian sweet soup"/.test(src)&&/"duasapdam": "Mashed wax coconut"/.test(src),'tên tiếng Anh 2 món');
const SV={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1,sap1:1},player:{av:1,name:'Q',garden:'Q'},lv:24,xp:40000,xu:50000,inv:{saurieng:2,dua:2,duasap:2},gb:{cui:10,duong:3},seeds:{},plots:{},qd:Object.fromEntries(Array.from({length:22},(_,i)=>[i+3,1])),realTime:true,spd:1,real:Date.now(),dd:{last:today,n:3,full:0},ftrD:today};
(async()=>{const b=await chromium.launch({args:['--use-angle=metal','--enable-gpu','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:844}});p.setDefaultTimeout(300000);const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());await p.addInitScript(s=>{localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SV));
await p.goto('http://127.0.0.1:8777/'+PAGE);await p.waitForFunction('window.__ready');await p.waitForTimeout(2000);
const r=await p.evaluate(()=>{const N=window.__N,I=window.__x.ICON;return ['chesaurieng','duasapdam'].map(k=>[k,N.DISH[k]&&N.DISH[k].lv,(I[k]||'').length])});
ok(r[0][1]===22&&r[0][2]>2000,'chè sầu riêng cấp 22, biểu tượng '+r[0][2]);ok(r[1][1]===24&&r[1][2]>2000,'dừa sáp dầm cấp 24, biểu tượng '+r[1][2]);
const c=await p.evaluate(()=>{const N=window.__N,ST=window.__g.ST;ST.bep=ST.bep||{pots:[null,null,null],made:{}};if(!ST.bep.pots)ST.bep.pots=[null,null,null];const a=N.bepCan('chesaurieng');N.bepCook('chesaurieng');const b2=N.bepCan('duasapdam');N.bepCook('duasapdam');return {a,b2,pot:JSON.stringify(ST.bep.pots),sr:ST.inv.saurieng,ds:ST.inv.duasap}});
ok(c.a&&c.b2&&/chesaurieng/.test(c.pot)&&/duasapdam/.test(c.pot)&&c.sr===1&&c.ds===1,'nấu thử 2 món '+JSON.stringify(c));
ok(errs.length===0,'không lỗi '+(errs[0]||''));await b.close();console.log('DONE',bad?bad+' FAIL':'all pass');})();
