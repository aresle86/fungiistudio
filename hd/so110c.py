# v110c — Sổ theo hệ thống giao diện (anh Ares duyệt mock 4/11): tab thẻ đánh dấu sách một chữ + icon, màu khu;
# tiêu đề trang bảng tên cùng màu, chữ mực; thẻ việc trắng viền mực, cột thưởng + "Đi làm" cố định 72px;
# mỗi phần việc Ngoại nhờ có icon, chữ thẳng mép trái với tiêu đề; bỏ nhãn "Sổ vườn của Ngoại".
# Dùng: python3 so110c.py live/v110b.html live/v110c.html   (CSS ở so110c.css)
import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:80], c, n); s = s.replace(a, b)
css = open('so110c.css', encoding='utf-8').read()
css += "\n.bklab{display:none!important}\n.bkt.on{transform:none!important}\n"
i = s.rfind('</style>'); s = s[:i + 8] + '<style id="s110c">' + css + '</style>' + s[i + 8:]
rep("const hdr = tab => { const [n, c, dc, ic] = BTAB[tab]; return `<div class=\"bkhd\" style=\"background:${c}\"><img src=\"${UIC[ic]}\" alt=\"\"><b style=\"text-shadow:${ring(dc, 2.2)},0 3px 0 ${dc}\">${n}</b></div>`; };",
    "const SOC = { viec: '#F6B49F', kho: '#F5D27A' }, soC = k => SOC[k] || '#B9D79F';   /* màu khu: Việc, Kho, Sưu tập */\nconst hdr = tab => { const [n, c, dc, ic] = BTAB[tab]; return `<div class=\"bkhd\" style=\"background:${soC(tab)}\"><img src=\"${UIC[ic]}\" alt=\"\"><b>${n}</b></div>`; };")
rep("style=\"background:${c};text-shadow:${ring(dc, 1.6)}\" aria-label=\"${n}\" aria-pressed=\"${on}\"><img src=\"${UIC[ic] || ICON[ic]}\" alt=\"\"><span>${nr ? (k === 'viec' ? 'Việc' : n) : n.replace('Việc của Ngoại', 'Việc của<br>Ngoại').replace('Bộ sưu tập', 'Bộ sưu<br>tập')}</span></button>`",
    "style=\"background:${soC(k)}\" aria-label=\"${n}\" aria-pressed=\"${on}\"><img src=\"${UIC[ic] || ICON[ic]}\" alt=\"\"><span>${k === 'viec' ? 'Việc' : k === 'kho' ? 'Kho' : 'Sưu tập'}</span></button>`")
rep("if (q.t === 'goal') body += q.goals.map(([t, f2, nn]) => { const v = Math.min(nn, f2()); return `<div class=\"qg${v >= nn ? ' ok' : ''}\"><span>",
    "if (q.t === 'goal') body += q.goals.map(([t, f2, nn]) => { const v = Math.min(nn, f2()); return `<div class=\"qg${v >= nn ? ' ok' : ''}\"><img src=\"${gIcon(t)}\" alt=\"\"><span>")
rep("const narrow = () => innerWidth <= 760;",
    "const narrow = () => innerWidth <= 760;\nconst GIC = [[/bón|phân|ủ/i, 'phan'], [/phơi|sấy|nong/i, 'nong'], [/trứng|gà/i, 'trungga'], [/vịt/i, 'trungvit'], [/cá|câu/i, 'caro'], [/ghe/i, 'ghe'], [/đơn|giao/i, 'cho'], [/giỏ/i, 'gio'], [/mái|nhà|sửa/i, 'cuoc'], [/hái|trái|cây/i, 'xoai'], [/liếp|gieo|đắp/i, 'cai'], [/xu|góp/i, 'xu']], gIcon = t => { const m = GIC.find(([r]) => r.test(t)); return (m && (ICON[m[1]] || UIC[m[1]])) || UIC.task || ICON.la; };   /* icon cho từng phần việc Ngoại nhờ */")
rep("const BUILD = 'v110b'", "const BUILD = 'v110c'")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
