#!/bin/bash
cd "$(dirname "$0")/lp"
: > ../reg2.txt
for t in terr2 tnew told tga tbai todd tbep tqa tvis; do echo "== $t" >> ../reg2.txt; timeout 600 node ../$t.js qc4/r_$t 2>&1 | grep -v TUNNEL | tail -8 >> ../reg2.txt; done
rm -f qc4/m_* qc4/d_*
timeout 900 node ../t62.js 1200 800 d; cp t62.log ../t62d.log
timeout 900 node ../t62.js 390 844 m; cp t62.log ../t62m.log
echo ALLDONE >> ../reg2.txt
