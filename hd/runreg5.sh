#!/bin/bash
cd "$(dirname "$0")/lp"
: > ../reg5.txt
for t in terr2 tnew told tga tbai todd tbep tqa tvis tT tR tC tV tL; do echo "== $t" >> ../reg5.txt; timeout 600 node ../$t.js qc4/r_$t 2>&1 | grep -v TUNNEL | tail -3 >> ../reg5.txt; done
timeout 900 node ../tG.js 1200 800 d
for f in tT tR tC tV tL tG_d; do echo "## $f" >> ../reg5.txt; cat ../$f.log >> ../reg5.txt; done
echo ALLDONE >> ../reg5.txt
