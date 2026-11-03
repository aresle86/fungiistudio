const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:600,height:400}});p.on('pageerror',e=>console.log('PERR',e.message));p.on('console',m=>{if(m.type()==='warning')console.log('W',m.text().slice(0,200))});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:150000});
const T=async n=>p.evaluate(n=>{window.__stop=true;const t0=performance.now();for(let i=0;i<n;i++)window.__tick();return (performance.now()-t0)/n|0;},n);
await p.evaluate(()=>{const ST=window.__g.ST;ST.player={av:1,name:'Na',garden:'V'};ST.lv=5;document.querySelectorAll('.lvup,#intro').forEach(e=>e.hidden=true);});
console.log('base',await T(5));await p.evaluate(()=>{window.__g.ST.muaTest='tet';window.__g.ST.tetDayTest=0;});console.log('tet',await T(5));console.log('st',await p.evaluate(()=>{const t0=performance.now();for(let i=0;i<20;i++)window.__TT.seasonTick(i);return (performance.now()-t0)/20}));await p.evaluate(()=>{window.__TT.seasonTick=null;const T2=window.__TT.TETV;T2.root.visible=false;});console.log('hidden-season-run',await p.evaluate(()=>{window.__stop=true;const o=window.__TT.TETV;const t0=performance.now();for(let i=0;i<5;i++){window.__tick();o.root.visible=false;o.boat.visible=false;}return (performance.now()-t0)/5|0;}));
await b.close();})();
