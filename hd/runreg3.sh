#!/bin/bash
cd "$(dirname "$0")/lp"
: > ../reg3.txt
for t in terr2 tnew tbai tqa todd; do echo "== $t" >> ../reg3.txt; timeout 600 node ../$t.js qc4/r_$t 2>&1 | grep -v TUNNEL | tail -5 >> ../reg3.txt; done
echo ALLDONE >> ../reg3.txt
