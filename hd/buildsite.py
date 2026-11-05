import json
import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
src=open('live/vuon3d.html',encoding='utf8').read()
head='''<!doctype html>
<html lang="vi"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Mệt phố thì về vườn. Về vườn… mệt hơn. Về quê làm vườn với Ngoại ở miền Tây: gieo rau, nuôi gà, nấu bếp củi, giao đơn cho hàng xóm, chèo xuồng ghé vườn.">
<meta name="theme-color" content="#447130">
<link rel="manifest" href="manifest.webmanifest">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Miệt Vườn">
<link rel="icon" href="favicon-32.png" type="image/png" sizes="32x32">
<link rel="icon" href="favicon-64.png" type="image/png" sizes="64x64">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Fungii">
<meta property="og:url" content="https://fungiistudio.com/mietvuon2/">
<meta property="og:title" content="Miệt Vườn 2.0">
<meta property="og:description" content="Mệt phố thì về vườn. Về vườn… mệt hơn.">
<meta property="og:image" content="https://fungiistudio.com/mietvuon2/og.jpg?v=113">
<meta property="og:image:alt" content="Nhà lá miền Tây dưới chữ Miệt Vườn 2.0, bảng gỗ ghi: Mệt phố thì về vườn. Về vườn… mệt hơn.">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Miệt Vườn 2.0">
<meta name="twitter:description" content="Mệt phố thì về vườn. Về vườn… mệt hơn.">
<meta name="twitter:image" content="https://fungiistudio.com/mietvuon2/og.jpg?v=113">
<style>html,body{margin:0;padding:0}</style>
'''
out=head+src.replace('<title>Miệt Vườn 2.0</title>','<title>Miệt Vườn 2.0 · Fungii</title>',1)+'\n</body></html>\n'
open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','mietvuon2/')+'index.html','w',encoding='utf8').write(out)
man={"name":"Miệt Vườn 2.0","short_name":"Miệt Vườn","lang":"vi","start_url":"./","scope":"./","display":"standalone","orientation":"any","background_color":"#86B06A","theme_color":"#86B06A","icons":[{"src":"apple-touch-icon.png","sizes":"180x180","type":"image/png"},{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png"}]}
open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','mietvuon2/')+'manifest.webmanifest','w',encoding='utf8').write(json.dumps(man,ensure_ascii=False,indent=1))
print('ok')
