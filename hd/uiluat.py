# Luật giao diện bằng máy (hud-hethong.md mục 10). Dùng hai cách:
#   python3 uiluat.py <file.html>            -> soát: in mọi chỗ lệch luật, thoát mã 1 nếu còn
#   from uiluat import chuyen; s = chuyen(s) -> đổi mọi số lệch về nấc gần nhất (số nằm giữa hai nấc thì lên nấc trên)
# Vùng áp: mọi khối <style>, mọi style="..." và .style.x = '...' trong mã.
import re, sys

SP_OK = {0, 1, 2, 4, 8, 12, 16, 24}          # trên 24 là chừa chỗ theo kích thước hình/nút, không thuộc thang
RD_OK = {0, 1, 2, 4, 6, 10, 16, 24, 999}
SP_PROP = r'(?<![-\w])(gap|row-gap|column-gap|padding(?:-(?:top|right|bottom|left|inline|block))?|margin(?:-(?:top|right|bottom|left|inline|block))?)\s*:\s*([^;}"\'`<]+)'
RD_PROP = r'(?<![-\w])(border(?:-(?:top|bottom)-(?:left|right))?-radius)\s*:\s*([^;}"\'`<]+)'
FS_PROP = r'(?<![-\w])(font-size)\s*:\s*([^;}"\'`<]+)'
FH_PROP = r'(?<![-\w])(font)\s*:\s*([^;}"\'`<]+)'
PX = r'(-?\d*\.?\d+)px'

def sp_map(v):
    a = abs(v); sg = -1 if v < 0 else 1
    if a < 3 or a > 24: return v
    for lo, hi in ((2, 4), (4, 8), (8, 12), (12, 16), (16, 24)):
        if lo <= a <= hi: return sg * (lo if (a - lo) < (hi - a) else hi)
def rd_map(v):
    if v < 3 or v in RD_OK: return v
    if v >= 99: return 999
    if v > 26: return v
    for lo, hi in ((2, 4), (4, 6), (6, 10), (10, 16), (16, 24), (24, 32)):
        if lo <= v <= hi: return lo if (v - lo) < (hi - v) else hi
def fs_map(v):
    if v < 12: return 12
    return int(v + 0.5) if v != int(v) else v
def num(v): return str(int(v)) if v == int(v) else str(v)

def regions(s):
    out = [(m.start(1), m.end(1)) for m in re.finditer(r'<style[^>]*>(.*?)</style>', s, flags=re.S)]
    end = out[-1][1] if out else 0
    out += [(m.start(1), m.end(1)) for m in re.finditer(r'style=\\?"([^"]*)"', s) if m.start() > end]
    out += [(m.start(2), m.end(2)) for m in re.finditer(r'\.style\.(gap|padding\w*|margin\w*|borderRadius|fontSize)\s*=\s*[\'"`]([^\'"`]*)', s) if m.start() > end]
    out += [(m.start(1), m.end(1)) for m in re.finditer(r'\.style\.cssText\s*\+?=\s*[\'"`]([^\'"`]*)', s) if m.start() > end]
    return out

def walk(seg, fix):
    bad = []
    def do(prop_re, mapper, okf, first_only=False):
        nonlocal seg
        def decl(m):
            cnt = [0]
            def one(x):
                cnt[0] += 1
                if first_only and cnt[0] > 1: return x.group(0)
                v = float(x.group(1)); n = mapper(v)
                if not okf(v): bad.append((m.group(1), x.group(0), m.group(0)[:70]))
                return (num(n) + 'px') if fix else x.group(0)
            return m.group(0)[:m.start(2) - m.start(0)] + re.sub(PX, one, m.group(2))
        seg = re.sub(prop_re, decl, seg)
    do(SP_PROP, sp_map, lambda v: abs(v) in SP_OK or abs(v) > 24 or abs(v) < 3)
    do(RD_PROP, rd_map, lambda v: v in RD_OK or v < 3 or (26 < v < 99))
    do(FS_PROP, fs_map, lambda v: v >= 12 and v == int(v))
    do(FH_PROP, fs_map, lambda v: v >= 12 and v == int(v), first_only=True)
    return seg, bad

def run(s, fix):
    out, bad, last = [], [], 0
    for a, b in sorted(regions(s)):
        if a < last: continue
        seg, bd = walk(s[a:b], fix); out.append(s[last:a]); out.append(seg); bad += bd; last = b
    out.append(s[last:]); return ''.join(out), bad
def chuyen(s): return run(s, True)[0]
def soat(s): return run(s, False)[1]

if __name__ == '__main__':
    bad = soat(open(sys.argv[1], encoding='utf-8').read())
    import collections
    c = collections.Counter(p.split('-')[0] if not p.startswith('border') else 'bo-goc' for p, _, _ in bad)
    for p, v, ctx in bad[:40]: print(p, v, '|', ctx)
    print('LECH LUAT', len(bad), dict(c)); sys.exit(1 if bad else 0)
