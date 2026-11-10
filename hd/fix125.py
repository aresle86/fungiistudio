# -*- coding: utf-8 -*-
# v125 sau v124b: ánh sáng theo giờ làm lại. Nắng mạnh và ấm hơn, ánh trời bù ít lại (vật có mặt sáng mặt tối),
# mặt trời xuống thấp lúc sáng sớm và chiều (bóng đổ dài), đêm ngả xanh trăng. Sương mỏng phía xa chỉ bật trên máy tính và iPad
# (điện thoại tắt để không nặng thêm). Cột KF thêm 2 cột cuối: sương [gần, xa].
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v124b'", "BUILD = 'v125'")
OLD = """const KF = [
  [0, '#4a5a8e', '#2a3346', .9, '#a8bcff', .42, .24, 1, '#2E3E62', 1.05],
  [4.6, '#4a5a8e', '#2a3346', .9, '#a8bcff', .42, .24, 1, '#2E3E62', 1.05],
  [5.3, '#c89aa8', '#5a5a6a', 1.0, '#ff9a7a', .7, .17, .45, '#b08a8a', 1.0],
  [5.9, '#ffd6b4', '#b0a886', 2.0, '#ffb070', 1.7, .3, .05, '#c79a7a', 1.12],
  [6.6, '#ffe6c0', '#b4ae84', 2.15, '#ffc684', 1.9, .32, 0, '#9ab070', 1.14],
  [8.2, '#fff0da', '#a4b080', 1.85, '#ffe2b0', 1.65, .26, 0, '#86B06A', 1.07],
  [12, '#fff4e2', '#94a474', 1.45, '#fff0d8', 1.38, .2, 0, '#86B06A', .97],
  [16, '#ffe6c0', '#a0a070', 1.55, '#ffc27a', 1.75, .22, 0, '#8aa860', 1.03],
  [17.8, '#f6b896', '#8a7a70', 1.35, '#ff9a64', 1.4, .2, .2, '#a08a6a', 1.05],
  [19, '#6a6a9a', '#3a3a4a', .95, '#a89aff', .45, .22, .85, '#454a72', 1.02],
  [20, '#4a5a8e', '#2a3346', .9, '#a8bcff', .42, .24, 1, '#2E3E62', 1.05],
  [24, '#4a5a8e', '#2a3346', .9, '#a8bcff', .42, .24, 1, '#2E3E62', 1.05]];"""
NEW = """const KF = [
  [0, '#3f58a0', '#1e2a44', .95, '#9fb8ff', .62, .16, 1, '#26365c', 1.05, 20, 70],
  [4.6, '#3f58a0', '#1e2a44', .95, '#9fb8ff', .62, .16, 1, '#26365c', 1.05, 20, 70],
  [5.3, '#b98aa6', '#4c4a60', .85, '#ff8a66', 1.1, .12, .45, '#b58a8c', 1.0, 16, 52],
  [5.9, '#f4e2cc', '#b0a878', 1.6, '#ffa860', 3.0, .2, .05, '#e8c090', 1.12, 22, 70],
  [6.6, '#f6ead2', '#b0ac7c', 1.7, '#ffbe78', 3.2, .2, 0, '#d8c890', 1.14, 24, 80],
  [8.2, '#f4f0e2', '#a4b080', 1.55, '#ffe0ac', 2.8, .18, 0, '#a4c080', 1.07, 30, 110],
  [12, '#f2f4ec', '#94a874', 1.35, '#fff0d8', 2.4, .16, 0, '#8cb46e', 1.0, 34, 140],
  [16, '#f6e8cc', '#a4a66c', 1.5, '#ffc680', 3.0, .18, 0, '#a8b46c', 1.05, 28, 100],
  [17.8, '#eec4b4', '#98846c', 1.4, '#ff985a', 2.9, .18, .2, '#d09c74', 1.1, 22, 70],
  [19, '#5c62a4', '#30324c', .9, '#a89aff', .6, .14, .85, '#40487a', 1.02, 18, 60],
  [20, '#3f58a0', '#1e2a44', .95, '#9fb8ff', .62, .16, 1, '#26365c', 1.05, 20, 70],
  [24, '#3f58a0', '#1e2a44', .95, '#9fb8ff', .62, .16, 1, '#26365c', 1.05, 20, 70]];
const FOG = MOBILE ? null : new T.Fog('#8cb46e', 34, 140); if (FOG) S.fog = FOG;   /* sương xa: điện thoại tắt */"""
rep(OLD, NEW)
rep("S.background.copy(lc(8)); r.toneMappingExposure = ln(9);", "S.background.copy(lc(8)); r.toneMappingExposure = ln(9); if (FOG){ FOG.color.copy(S.background); FOG.near = ln(10); FOG.far = ln(11); }")
rep("el = Math.max(.42, Math.sin(a2)); sun.position.set(ctr.x - Math.cos(a2) * 14, ctr.y + el * 16, ctr.z - 4 + Math.cos(a2) * 6); }", "el = Math.max(.34, Math.sin(a2) * .92); sun.position.set(ctr.x - Math.cos(a2) * 15, ctr.y + el * 16, ctr.z - 3 + Math.cos(a2) * 7); }")
rep("else sun.position.set(ctr.x - 7, ctr.y + 14, ctr.z - 5); }", "else sun.position.set(ctr.x - 9, ctr.y + 11, ctr.z - 6); }")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
