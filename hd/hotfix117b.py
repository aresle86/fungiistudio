# hotfix117b: cpN (đếm dòng "+xu" bay cạnh ô xu) khai báo bằng let ở sâu trong mã; nếu lúc dựng cảnh có việc cộng/trừ xu
# (vd vườn vừa đủ điểm lên cấp ngay khi mở) thì coinPop chạy trước khai báo -> "Cannot access 'cpN' before initialization".
# Sửa: khai báo cpN bằng var ở đầu mã module.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
assert s.count('let cpN = 0;') == 1
s = s.replace('let cpN = 0;', '/* cpN khai báo ở đầu mã (hotfix117b) */')
i = s.index('<script type="module">') + len('<script type="module">')
s = s[:i] + '\nvar cpN = 0;   // hotfix117b: dùng được cả lúc đang dựng cảnh\n' + s[i:]
if len(sys.argv) > 3: s = s.replace("BUILD = '" + sys.argv[3] + "'", "BUILD = '" + sys.argv[4] + "'")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
