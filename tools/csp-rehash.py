# Recompute the CSP script hashes in index.html after editing any inline <script>.
# Usage: python3 tools/csp-rehash.py index.html
import re,hashlib,base64,sys
p=sys.argv[1];h=open(p).read()
hs=["'sha256-"+base64.b64encode(hashlib.sha256(m.group(1).encode()).digest()).decode()+"'" for m in re.finditer(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>',h,re.S)]
m=re.search(r"script-src 'self'((?: 'sha256-[^']+')+);",h)
old=m.group(1);h=h.replace(old,' '+' '.join(hs),1)
open(p,'w').write(h);print('hashes',len(hs),'changed',old.strip()!=' '.join(hs))
