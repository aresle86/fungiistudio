#!/bin/bash
cd "$(dirname "$0")/lp"
timeout 900 node ../tG.js 1200 800 d
timeout 900 node ../tG.js 390 844 m
echo DONE >> ../tG_m.log
