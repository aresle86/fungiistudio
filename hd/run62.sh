#!/bin/bash
cd "$(dirname "$0")/lp"
rm -f qc4/m_* qc4/d_lvup.png
timeout 900 node ../t62.js 1200 800 d
timeout 900 node ../t62.js 390 844 m
echo DONE >> t62.log
