const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:600}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const S=await p.evaluate(()=>{window.__stop=true;const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=6;g.ST.seen.hello=1;
 const Y=window.__SY,ng=document.getElementById('ngoai'),out={};
 Y.say('Câu A đang nói.','vui',{now:true});
 let sau=true; Y.say('Có sâu kìa','dan',{ok:()=>sau}); Y.say('Câu C bình thường.','vui');
 sau=false; ng.click(); out.afterClick1=document.getElementById('ngoaiTxt').textContent;
 // sayOnce với việc lặt vặt: chưa có sâu thì không nói, không đánh dấu đã nói
 g.ST.odd={list:[],acc:{}}; delete g.ST.seen.tst; Y.sayOnce('tst','Sâu nè','dan',()=>g.ST.odd.list.length>0); out.seenWhenNone=!!g.ST.seen.tst;
 // idle queue: sâu bắt xong trước khi tới lượt thì bỏ và cho phép nói lại lần sau
 Y.IDLEQ.length=0; Y.IDLEQ.push(['Sâu idle','dan',{ok:()=>false,key:'tst2'}]); g.ST.seen.tst2=1; ng.hidden=true;
 return out;});
await p.waitForTimeout(4000);
const S2=await p.evaluate(()=>({idleLeft:window.__SY.IDLEQ.length,seen2:!!window.__g.ST.seen.tst2,txt:document.getElementById('ngoaiTxt').textContent}));
console.log(JSON.stringify(S),JSON.stringify(S2));console.log(errs.join('\n')||'no errors');await b.close();})();
