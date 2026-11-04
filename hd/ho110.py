# v110 hố ủ (danh sách trước quảng bá A5): ba nguồn đồ ủ rõ ràng
#  - Hái rau (không phải cây trái) thì gốc rễ, lá già tự vô hố, chữ bay "+1 gốc rau vô hố ủ"; Ngoại dặn lần đầu.
#  - Phân chuồng ra theo số gà vịt: cứ 3 con thêm 1 phần mỗi 6 tiếng (tối thiểu 1), tích tối đa 8 phần.
#  - Có phân chuồng chờ hốt thì hố ủ nổi bong bóng; bảng hố ủ hiện ba nguồn bằng ô icon.
# Dùng: python3 ho110.py live/v110a.html live/v110a.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:80], c, n); s = s.replace(a, b)

rep("function phanCh(){ const H = ST.ho; let on = false; try { on = gaOn() || vitOn(); } catch (e) {} if (!H || !on) return 0; if (!H.pct) H.pct = Date.now(); return Math.min(4, Math.floor((Date.now() - H.pct) / PHANT)); }",
    "const phanK = () => { let n = 0; try { if (gaOn()) n += ST.ga.hens + ST.ga.rooster; if (vitOn()) n += ST.vit.n; } catch (e) {} return Math.max(1, Math.floor(n / 3)); };   /* cứ 3 con gà vịt thêm 1 phần mỗi 6 tiếng */\nfunction phanCh(){ const H = ST.ho; let on = false; try { on = gaOn() || vitOn(); } catch (e) {} if (!H || !on) return 0; if (!H.pct) H.pct = Date.now(); return Math.min(8, Math.floor((Date.now() - H.pct) / PHANT) * phanK()); }")
rep("if (!hoAdd(n)) return; H.pct = n >= a ? Date.now() : H.pct + n * PHANT;",
    "if (!hoAdd(n)) return; H.pct = n >= a ? Date.now() : H.pct + Math.ceil(n / phanK()) * PHANT;")
# hái rau: gốc rễ vô hố
rep("ST.inv[p.crop] = (ST.inv[p.crop] || 0) + n; p.stolen = 0; if (!c.tree){",
    "ST.inv[p.crop] = (ST.inv[p.crop] || 0) + n; p.stolen = 0; if (!c.tree && ownObj('ho') && hoRoom()){ hoAdd(1); const v1 = PV[id]; setTimeout(() => floatAt(v1.cx, .45, v1.cz, '+1 gốc rau vô hố ủ', '#D9B77A'), 1100); setTimeout(() => sayOnce('gocrau', 'Gốc rễ với lá già hái ra Ngoại bỏ vô hố ủ hết, đủ đồ là ủ ra phân bón lại cho đất.', 'vui'), 1600); } if (!c.tree){")
# bong bóng hố ủ khi có phân chuồng chờ hốt
rep("  if (H.bags) objBub(HOV, v, ICON.phan, t); }",
    "  if (H.bags) objBub(HOV, v, ICON.phan, t); else if (hoRoom() && phanCh() >= 1) objBub(HOV, v, ICON.mai, t); else if (H.t > 0) objBub(HOV, v, ICON.ho, t, .62, 1 - H.t / (H.done ? HO.t : HO.first)); }")   # đang ủ: bong bóng có thanh
rep("UX.btn('hophan', 'Hốt phân chuồng', { img: ICON.phan,", "UX.btn('hophan', 'Hốt phân chuồng', { g: !H.bags && phanCh() >= 1 && hoRoom(), img: ICON.phan,")
# bảng: ba nguồn
rep("else h += UX.hero(ICON.ho, `Cần thêm ${Math.max(0, HO.need - H.mat)} phần đồ ủ`, 'Quét lá, vớt lục bình, hốt phân chuồng gà vịt bỏ vô hố', H.mat ? '' : 'warn');",
    "else h += UX.hero(ICON.ho, `Cần thêm ${Math.max(0, HO.need - H.mat)} phần đồ ủ`, 'Hái rau, hốt phân chuồng, quét lá bỏ vô', '', [H.mat / HO.need, '#8A5D3B']);")
rep("  h += '<div class=\"uxs\">' + UX.card('Đồ ủ trong hố', `${H.mat}/${HO.need} <small>phần</small>`, UX.pips(ICON.la || ICON.lucbinh, Math.min(H.mat, HO.need), HO.need)) + UX.card('Phân đã ủ', `${H.bags || 0}/${HO.max} <small>bao</small>`, UX.pips(ICON.phan, H.bags || 0, HO.max), H.bags ? 'go' : '') + '</div>';",
    "  const pc = phanCh(); h += '<div class=\"uxs three\">' + UX.card(phanOn() ? `Phân chuồng · ${phanK()} phần/6 giờ` : 'Phân chuồng', pc ? `${pc}<small> chờ hốt</small>` : '0', '', pc ? 'go' : '', ICON.mai) + UX.card('Gốc rau · tự vô khi hái', '+1', '', '', ICON.cai) + UX.card('Lá rụng, lục bình', '+1–2', '', '', ICON.la || ICON.lucbinh) + '</div>'\n    + '<div class=\"uxs one\">' + UX.card('Phân đã ủ', `${H.bags || 0}<small>/${HO.max} bao</small>`, UX.pips(ICON.phan, H.bags || 0, HO.max), H.bags ? 'go' : '', ICON.phan) + '</div>';")
rep("Quét lá rụng +2 phần, vớt lục bình +1 phần (vịt no rồi thì lục bình vô hố), chuồng gà vịt sáu tiếng hốt được 1 phần phân.",
    "Hái rau thì gốc rễ, lá già tự vô hố +1 phần. Chuồng gà vịt cứ ba con ra 1 phần phân mỗi sáu tiếng, bấm Hốt phân chuồng bỏ vô. Quét lá rụng +2 phần, vớt lục bình +1 phần (vịt no rồi thì lục bình vô hố).")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
