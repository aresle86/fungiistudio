#!/bin/bash
cd "$(dirname "$0")"
bash runreg5.sh
: > extra.txt
for t in tLand tTet tCloud tTree tFish tFish3 tFish5 tFt tDd tBig tDc tTc tNg tFt6 tMai tNha tBld tTB; do echo "== $t" >> extra.txt; (cd lp && timeout 600 node ../$t.js 2>&1 | grep -v TUNNEL | tail -4) >> extra.txt; done
echo ALLDONE >> extra.txt
