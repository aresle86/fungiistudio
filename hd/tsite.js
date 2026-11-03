const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:844},isMobile:true,hasTouch:true,deviceScaleFactor:3});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://127.0.0.1:8777/site.html');await p.waitForTimeout(20000);
console.log(await p.evaluate(()=>[document.compatMode,innerWidth,innerHeight,document.getElementById('c').width,document.getElementById('c').height,document.title,!document.getElementById('intro').hidden,document.getElementById('load').hidden]),errs);
await p.screenshot({path:'qc2/site.png',timeout:120000});await b.close();})();
