const fs=require('fs');const L=m=>fs.appendFileSync('t62.log',m+'\n');fs.writeFileSync('t62.log','');
const {chromium}=require('playwright');(async()=>{const [,,W,H,tag]=process.argv;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:+W,height:+H},hasTouch:+W<700,isMobile:+W<700});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));p.on('console',m=>{if(m.type()==='error'||m.type()==='warning')errs.push('CON '+m.text());});
await p.addInitScript(()=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');}}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;});const tick=async(n=2)=>{await p.evaluate(n=>{for(let i=0;i<n;i++)window.__tick();},n);await p.waitForTimeout(150);};
await tick();const sh=n=>p.screenshot({path:`qc4/${tag}_${n}.png`});
L('intro hidden? '+await p.evaluate(()=>document.getElementById('intro').hidden));
await p.evaluate(()=>window.__w.openIntro());await tick();await sh('intro0');
await p.click('#inGo');await tick();L('go w/o pick, intro still: '+!(await p.evaluate(()=>document.getElementById('intro').hidden)));
await p.click('#avs .avc:nth-child(3)');await p.fill('#inName','Bé Na');await tick();await p.waitForTimeout(600);await sh('intro1');
await p.click('#inGo');await tick();L('player '+await p.evaluate(()=>JSON.stringify(window.__g.ST.player)));
await p.evaluate(()=>{const g=window.__g;g.ST.lv=2;g.ST.xp=16;g.closeSheet();window.__w.hud();window.__w.gainXP(0.0001);});await tick();await sh('lv2');
L('weedOn '+await p.evaluate(()=>window.__w.weedOn())+' cutTray hidden '+await p.evaluate(()=>document.getElementById('tCut').hidden));
await p.evaluate(()=>window.__w.weedGo());for(let i=0;i<30;i++)await tick(1);await sh('weedgo');
// cut via stroke at clump positions
const r=await p.evaluate(()=>{const w=window.__w,out=[];for(const i of [0,1,2]){const [x,z]=w.WEEDP[i];out.push(w.weedAt(x+.05,z));}return out.join(',')+' weed='+window.__g.ST.weed+' xp='+window.__g.ST.xp;});L('cut3 '+r);await tick();await sh('weed3');
// tap a clump on screen
const sc=await p.evaluate(()=>{const g=window.__g,[x,z]=window.__w.WEEDP[3],v=new g.T.Vector3(x,.12,z).project(g.cam);return [(v.x+1)/2*innerWidth,(1-v.y)/2*innerHeight];});
await p.evaluate(()=>window.__w.clearTool());if(+W<700){await p.touchscreen.tap(sc[0],sc[1]);}else{await p.mouse.click(sc[0],sc[1]);}await tick();L('after tap weed='+await p.evaluate(()=>window.__g.ST.weed));
await p.evaluate(()=>window.__w.openBook('viec'));await tick();await sh('book');
await p.evaluate(()=>{window.__w.closeBook();const w=window.__w;for(const i of w.weedLeft()){const [x,z]=w.WEEDP[i];w.weedAt(x,z);} });await tick();await p.waitForTimeout(900);await sh('lvup');
L('lv '+await p.evaluate(()=>window.__g.ST.lv+' xp '+window.__g.ST.xp+' lvup shown '+!document.getElementById('lvup').hidden));
await p.click('#lvOk',{timeout:5000}).catch(()=>{});await tick();await sh('after');
await p.evaluate(()=>{const g=window.__g;g.ST.lv=4;g.ST.xp=100;window.__w.hud();});await tick();await sh('lv4');
await p.evaluate(()=>window.__w.openBook('viec'));await tick();await sh('book4');
L(errs.join('\n'));await b.close();})();
