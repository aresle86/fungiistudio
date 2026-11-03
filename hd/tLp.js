const {chromium}=require('playwright');(async()=>{const [,,W,H,tag]=process.argv;const b=await chromium.launch();
const p=await b.newPage({viewport:{width:+W,height:+H}});await p.goto('http://127.0.0.1:8777/loadprev.html');await p.evaluate(()=>document.fonts.ready);
const ts=(process.argv[5]||'300,800,1200,1600,2100,3000').split(',').map(Number);let last=0;for(const t of ts){await p.waitForTimeout(t-last);last=t;await p.screenshot({path:`../../logo/P_${tag}_${t}.png`});}
await p.evaluate(()=>window.__done());await p.waitForTimeout(500);await p.screenshot({path:`../../logo/P_${tag}_out.png`});await b.close();})();
