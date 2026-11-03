const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_claim.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=2;g.ST.xp=99999;g.ST.qd={};g.ST.seen.hello=1;g.ST.dd={n:1,d:new Date().toDateString(),last:Date.now()};document.querySelectorAll('.ddt').forEach(e=>e.remove());for(let i=0;i<30;i++)window.__tick();});
await p.waitForTimeout(1500);
const bubPos=()=>p.evaluate(()=>{const g=window.__g,T=g.T;let bb=null;for(const x of window.__BUBALL){if(x.visible&&x.userData.pl&&x.userData.pl.userData.url===window.__UIC.sickle){let o=x,v=true;while(o){if(!o.visible){v=false;break;}o=o.parent;}if(v)bb=x;}}if(!bb)return null;const w=new T.Vector3();bb.getWorldPosition(w);w.project(g.cam);return [(w.x+1)/2*innerWidth,(1-w.y)/2*innerHeight];});
const weed=()=>p.evaluate(()=>window.__g.ST.weed||0);
// camera tới mé mương để thấy bong bóng
await p.evaluate(()=>{const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(2.5,.3,4.6);c.object.position.copy(c.target).add(d);c.object.zoom=1.6;c.object.updateProjectionMatrix();for(let i=0;i<5;i++)window.__tick();});await p.waitForTimeout(800);
let bp=await bubPos();console.log('bub',bp,'weed0',await weed());
if(bp){await p.touchscreen.tap(bp[0],bp[1]);await p.waitForTimeout(800);console.log('after tap bubble',await weed());}

// bấm nút Liềm
await p.evaluate(()=>document.getElementById('tCut').click());await p.waitForTimeout(2500);console.log('tool',await p.evaluate(()=>{const t=window.__T;return JSON.stringify([t&&t.TOOL, document.querySelector('#tstw')&&document.querySelector('#tstw').innerText]);}));
bp=await bubPos();console.log('bub2',bp);
if(bp){await p.touchscreen.tap(bp[0],bp[1]);await p.waitForTimeout(800);console.log('after tool tap',await weed());}

console.log(errs.join('\n')||'no errors');await b.close();})();
