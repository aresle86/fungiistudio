#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sao lưu dữ liệu Miệt Vườn từ Supabase về máy (chỉ đọc).

Chạy:  python3 ~/Documents/fungiistudio/hd/saoluu.py
Lưu vào ~/MietVuon-saoluu/<ngày giờ>/, giữ 12 bản mới nhất.
Cần: hd/.baoloi-key (khóa quản trị) và hàm mv2_admin_export trên Supabase
(hd/sql/mv2_admin_export.sql). Không in khóa ra màn hình.
"""
import json, os, re, shutil, sys, time, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
URL = 'https://zgfanxtjdvioxpgpbcke.supabase.co/rest/v1/rpc/mv2_admin_export'
OUT = os.path.expanduser('~/MietVuon-saoluu')
KEEP = 12
TABLES = ['mv2_farms', 'mv2_events', 'mv2_steps', 'mv2_reports', 'mv2_days',
          'mv2_errs', 'mv2_follows', 'feedback', 'notes', 'mv_farms', 'mv_keys',
          '_functions', '_schema']


def pubkey():
    s = open(os.path.join(ROOT, 'mietvuon2', 'index.html'), encoding='utf-8').read()
    m = re.search(r'sb_publishable_[A-Za-z0-9_-]+', s)
    if not m:
        sys.exit('Không tìm thấy khóa publishable trong mietvuon2/index.html')
    return m.group(0)


def call(apikey, admin, tbl):
    body = json.dumps({'p_key': admin, 'p_tbl': tbl}).encode()
    req = urllib.request.Request(URL, data=body, method='POST', headers={
        'apikey': apikey, 'Authorization': 'Bearer ' + apikey,
        'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode('utf-8'))


def main():
    kp = os.path.join(HERE, '.baoloi-key')
    if not os.path.exists(kp):
        sys.exit('Thiếu file khóa hd/.baoloi-key')
    admin = open(kp, encoding='utf-8').read().strip()
    apikey = pubkey()
    stamp = time.strftime('%Y-%m-%d_%H%M')
    tmp = os.path.join(OUT, '.dang-luu-' + stamp)
    os.makedirs(tmp, exist_ok=True)
    os.chmod(OUT, 0o700)
    total = 0
    try:
        for t in TABLES:
            try:
                rows = call(apikey, admin, t)
            except urllib.error.HTTPError as e:
                msg = e.read().decode('utf-8', 'replace')[:200]
                if 'mv2_admin_export' in msg and ('not find' in msg or 'PGRST202' in msg):
                    sys.exit('Supabase chưa có hàm mv2_admin_export (hd/sql/mv2_admin_export.sql).')
                if 'not allowed' in msg:
                    sys.exit('Khóa quản trị không đúng.')
                sys.exit('Lỗi khi lấy %s: HTTP %s %s' % (t, e.code, msg))
            with open(os.path.join(tmp, t + '.json'), 'w', encoding='utf-8') as f:
                json.dump(rows, f, ensure_ascii=False)
            n = len(rows) if isinstance(rows, list) else 1
            total += n
            print('%-12s %5d dòng' % (t, n))
    except SystemExit:
        shutil.rmtree(tmp, ignore_errors=True)
        raise
    dst = os.path.join(OUT, stamp)
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.rename(tmp, dst)
    olds = sorted(d for d in os.listdir(OUT) if re.match(r'^\d{4}-\d\d-\d\d_\d{4}$', d))
    for d in olds[:-KEEP]:
        shutil.rmtree(os.path.join(OUT, d), ignore_errors=True)
    print('Xong: %d dòng, lưu ở %s' % (total, dst))


if __name__ == '__main__':
    main()
