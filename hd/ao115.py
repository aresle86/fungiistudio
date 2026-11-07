# ao115: ao nhỏ mua đủ đồ bớt chật: hai cầu dời ra hai đầu hẹp, cầu ván sang giữa mé trước, cây bần ra sau ao, chừa mặt nước và chiếc ghe. python3 ao115.py vào ra
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
rep("if (on('sen')) for (const [x, z, s0, b] of [[-.62, -.12, 1, 1], [-.4, .2, .9, 0], [-.8, .2, .85, 1]]) sen(x, z, s0, b); if (on('sung')) { sung(-.08, .46, 1); sung(.02, -.46, .9); }",
    "if (on('sen')) for (const [x, z, s0, b] of [[-.5, -.3, 1, 1], [-.32, .02, .9, 0], [-.48, .24, .85, 1]]) sen(x, z, s0, b); if (on('sung')) { sung(.14, .28, 1); sung(.02, -.46, .9); }")
rep("if (on('long')) longAo(-.42, .92, .8); if (on('chuoi')) chuoi(-1.22, -.84, .8); if (on('duanuoc')) duaNuoc(1.38, .08, .62); if (on('ban')) ban(1.32, .82, .7); if (on('caukhi')) cauKhi(.12, .95, .18, -.92); if (on('cautre')) cauTre(-1.02, -.5, .5, 0); if (on('cauvan')) { cau(.5, .96, .56, .35, .2); for (let i = 0; i < 2; i++) M(box(.22, .03, .08), '#8A5D3B', .5, .1 - i * .04, 1.0 + i * .08); }",
    "if (on('long')) longAo(-.38, .94, .8); if (on('chuoi')) chuoi(-1.22, -.84, .8); if (on('duanuoc')) duaNuoc(1.38, .08, .62); if (on('ban')) ban(-1.33, .24, .7); if (on('caukhi')) cauKhi(-.88, .72, -.82, -.72); if (on('cautre')) cauTre(1.0, -.04, .86, Math.PI / 2); if (on('cauvan')) { cau(-.18, .96, -.14, .4, .2); for (let i = 0; i < 2; i++) M(box(.22, .03, .08), '#8A5D3B', -.18, .1 - i * .04, 1.0 + i * .08); }")
open(dst,'w',encoding='utf-8').write(s)
