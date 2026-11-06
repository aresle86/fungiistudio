# ui115g: số báo Chợ gọn lại; thẻ đơn: nút giao là chính, Để bữa khác lùi thành chữ. python3 ui115g.py live/v115_3.html live/v115_3b.html
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
css="""
/* v115g: báo kho nhỏ gọn, thò ra bên trái icon, không che quầy chợ và nhãn */
#bCho .kb{bottom:auto!important;top:14px!important;left:auto!important;right:calc(100% - 20px)!important;margin:0!important;width:max-content!important;min-width:0!important;font-size:10px!important;line-height:1!important;padding:2px 5px 1px!important;background:#F5C451;color:#4A2F1E;box-shadow:0 0 0 1.5px #4A2F1E!important}
#bCho .kb.full{background:#C24A2E;color:#fff}
/* thẻ đơn: nút giao chiếm chỗ, Để bữa khác chỉ là chữ */
.ordr .oa .btn.g:disabled{opacity:1!important;filter:none!important;background:#DDE8C8!important;color:#4F6B33!important;text-shadow:none!important}
#sheet .ordr .oa .btn.oskip,.sheet .ordr .oa .btn.oskip{background:transparent!important;background-image:none!important}
.ordr .oa .oskip::before,.ordr .oa .oskip::after{display:none!important}
.ordr .oa .btn.g{white-space:nowrap}
.ordr .oa .oskip{background:none!important;box-shadow:none!important;border:0!important;color:#8A5D3B!important;text-shadow:none!important;font:600 13px/1.1 var(--f-body,'Baloo 2'),sans-serif!important;min-height:44px!important;min-width:44px;padding:4px 6px!important;white-space:nowrap}
.ordr .oa .oskip:active{transform:none!important;color:#4A2F1E!important}
@media (max-width:560px){ .ordr .oa{gap:8px;justify-content:flex-start!important} .ordr .oa .btn.g{flex:1 1 auto;min-width:0;font-size:15px!important;padding-left:8px;padding-right:8px} .ordr .oa .oskip{flex:0 0 auto} }
"""
i=s.rfind('</style>',0,s.find('<script type="module">')); assert i>0
s=s[:i]+css+s[i:]
rep("""<button class="btn g" data-a="ordgive" data-k="${o.id}" ${ok ? '' : 'disabled'}>Giao · ${o.xu} xu</button>""","""<button class="btn g" data-a="ordgive" data-k="${o.id}" ${ok ? '' : 'disabled'}>${ok ? `Giao · ${o.xu} xu` : `Còn thiếu ${o.items.reduce((n, [k, q]) => n + Math.max(0, q - has(k)), 0)} món · ${o.xu} xu`}</button>""")
open(dst,'w',encoding='utf-8').write(s)
