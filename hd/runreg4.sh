#!/bin/bash
cd "$(dirname "$0")/lp"
: > ../reg4.txt
for t in terr2 tnew told tga tbai todd tbep tqa tvis tT tR; do echo "== $t" >> ../reg4.txt; timeout 600 node ../$t.js qc4/r_$t 2>&1 | grep -v TUNNEL | tail -4 >> ../reg4.txt; done
timeout 900 node ../tG.js 1200 800 d; echo "== tG" >> ../reg4.txt; cat ../tG_d.log >> ../reg4.txt
cat ../tT.log ../tR.log >> ../reg4.txt
echo ALLDONE >> ../reg4.txt
