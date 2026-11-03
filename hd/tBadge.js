const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [w,h,tag] of [[390,700,'m'],[1280,760,'d']]){const p=await b.newPage({viewport:{width:w,height:h},isMobile:tag==='m',hasTouch:tag==='m'});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{const g=window.__g,ST=g.ST;ST.player={av:1,name:'Na',garden:'V'};ST.lv=4;document.querySelectorAll('.lvup,#intro').forEach(e=>e.hidden=true);});
await p.waitForTimeout(800);await p.evaluate(()=>{const ob=document.querySelector('#bCho .ob');if(ob){ob.textContent='1';ob.hidden=false;ob.style.display='';}const kb=document.querySelector('#bCho .kb');if(kb){kb.hidden=false;kb.textContent='18/20';}window.__stop=true;});
await p.waitForTimeout(300);const r=await p.evaluate(()=>document.querySelector('.ui.bot .row').getBoundingClientRect().toJSON());
await p.screenshot({path:`../badge_${tag}.png`,clip:{x:Math.max(0,r.x-20),y:r.y-30,width:Math.min(w,r.width+40),height:r.height+40},timeout:120000});await p.close();}
await b.close();})();
