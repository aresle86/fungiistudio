const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for(const [W,H,n] of [[1200,630,'og'],[1080,1080,'square'],[1080,1920,'story']]){const p=await b.newPage({viewport:{width:W,height:H},deviceScaleFactor:1});await p.goto('http://127.0.0.1:8777/loadprev.html');await p.evaluate(()=>document.fonts.ready);
await p.addStyleTag({content:'#load .lbar,#load .lbird{display:none!important}'});await p.waitForTimeout(3500);await p.screenshot({path:`../../logo/thumb_${n}.png`});await p.close();}
await b.close();})();
