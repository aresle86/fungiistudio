# NHÁP v150: cấp đi tiếp sau 20 (tới 30), mỗi cấp Ngoại cho quà hạt giống quý; chợ huyện 21, sầu riêng 22, dừa sáp 24 tự mở theo bảng có sẵn.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v149f'", "BUILD = 'v150'")
# bảng kinh nghiệm: mỗi cấp sau 20 cách nhau 5.000 rồi tăng dần 500
rep("18000, 20500, 23500, 26500];", "18000, 20500, 23500, 26500, 31500, 37000, 43000, 49500, 56500, 64000, 72000, 80500, 89500, 99000];")
# quà mỗi cấp sau 20: giống quý (bình thường chỉ Tiệm Tết có), cấp lẻ dưa hấu, cấp chẵn cúc
rep("function checkLevel(){ for (;;){",
    "const lvGift = n => n > 20 ? (n % 2 ? ['duahau', 5, 'Quà Ngoại: dưa hấu ruột vàng', 'Ngoại để dành cho con năm bao hạt dưa hấu ruột vàng nè. Giống Tết đó, ngoài Tết hông ai bán đâu.'] : ['cuc', 5, 'Quà Ngoại: cúc mâm xôi', 'Ngoại để dành cho con năm bao hạt cúc mâm xôi nè. Giống Tết đó, ngoài Tết hông ai bán đâu.']) : null;\n"
    "try { Object.assign(UIEN, { 'Quà Ngoại: dưa hấu ruột vàng': 'Gift: golden watermelon seeds', 'Quà Ngoại: cúc mâm xôi': 'Gift: chrysanthemum seeds', 'Ngoại để dành cho con năm bao hạt dưa hấu ruột vàng nè. Giống Tết đó, ngoài Tết hông ai bán đâu.': 'Grandma saved you five bags of golden watermelon seeds. A rare kind, nobody sells it outside of Tết.', 'Ngoại để dành cho con năm bao hạt cúc mâm xôi nè. Giống Tết đó, ngoài Tết hông ai bán đâu.': 'Grandma saved you five bags of chrysanthemum seeds. A rare kind, nobody sells it outside of Tết.' }); } catch (e) {}\n"
    "function checkLevel(){ for (;;){")
# sau cấp 20 mỗi lần chỉ lên một cấp (dư kinh nghiệm thì lần cộng sau lên tiếp), khỏi chồng bảng chúc mừng
rep("return; } levelUp(n); } }", "return; } levelUp(n); if (n > 20) return; } }")
rep("for (const k of ks) ST.seeds[k] = (ST.seeds[k] || 0) + 1; try { moiSet(n, ks); } catch (e) {}",
    "for (const k of ks) ST.seeds[k] = (ST.seeds[k] || 0) + 1; { const gf = lvGift(n); if (gf){ ST.seeds[gf[0]] = (ST.seeds[gf[0]] || 0) + gf[1]; lvSay(gf[3], 'vui', { idle: true }); save(); } } try { moiSet(n, ks); } catch (e) {}")
rep("...(CAU.them.some(([l]) => l === n) ? [['cancau', 'Câu thêm cá']] : [])];\n  $('#lvN').textContent = n;",
    "...(CAU.them.some(([l]) => l === n) ? [['cancau', 'Câu thêm cá']] : []), ...(lvGift(n) ? [[lvGift(n)[0], lvGift(n)[2]]] : [])];\n  $('#lvN').textContent = n;")
# thẻ lên cấp: quà Ngoại xếp sau đồ mới mở; cấp 22, 24 báo luôn món mới của bếp
rep("const rk = ([k, t]) => /^dc_/.test(k) ? 3 :", "const rk = ([k, t]) => /^Quà Ngoại/.test(t) ? 5 : /^dc_/.test(k) ? 3 :")
rep("(LVFEAT[QN.lv] = LVFEAT[QN.lv] || []).push(['nuockhe', 'Quầy nước']);",
    "(LVFEAT[QN.lv] = LVFEAT[QN.lv] || []).push(['nuockhe', 'Quầy nước']); (LVFEAT[22] = LVFEAT[22] || []).push(['chesaurieng', 'Chè sầu riêng']); (LVFEAT[24] = LVFEAT[24] || []).push(['duasapdam', 'Dừa sáp dầm']); try { Object.assign(UIEN, { 'Chè sầu riêng': 'Durian sweet soup', 'Dừa sáp dầm': 'Mashed wax coconut' }); } catch (e) {}")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
