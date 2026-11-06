const { chromium } = require('playwright'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:800,height:860}});
for(const n of process.argv.slice(2)){const u=t=>'data:image/png;base64,'+fs.readFileSync(`/tmp/pin_${t}_${n}.png`).toString('base64');await p.setContent(`<body style="margin:0;background:#fff;display:flex;gap:8px"><img src="${u('f')}" width=390><img src="${u('g')}" width=390>`);await p.waitForTimeout(300);await p.screenshot({path:`/tmp/cmp_${n}.png`});}
await b.close();})();
