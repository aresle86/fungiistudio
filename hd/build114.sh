#!/bin/zsh
# Dựng bản mới nhất theo chuỗi: deco113 → sv114 → aog114 → opt114 → fix114 → rad114. ./build114.sh [thư mục nhạc]
set -e
python3 deco113.py live/v112a.html live/v113w.html
python3 sv114.py live/v113w.html live/v114a.html
python3 aog114.py live/v114a.html live/v114b.html
python3 opt114.py live/v114b.html live/v114c.html
python3 fix114.py live/v114c.html live/v114d.html
python3 rad114.py live/v114d.html live/v114e.html ${1:-nhac}
python3 multi114.py live/v114e.html live/v114f.html
python3 qc115.py live/v114f.html live/v115_1.html
python3 chau115.py live/v115_1.html live/v115_1b.html
python3 ga115.py live/v115_1b.html live/v115_1c.html
python3 vis115.py live/v115_1c.html live/v115_1d.html
python3 perf115.py live/v115_1d.html live/v115_1e.html
python3 sync115.py live/v115_1e.html live/v115_1f.html
python3 load115.py live/v115_1f.html live/v115_2.html
python3 en111.py live/v115_2.html live/v115f.html v115f
python3 draw115.py live/v115_2.html live/v115_3.html
python3 ui115g.py live/v115_3.html live/v115_3b.html
python3 note115.py live/v115_3b.html live/v115_3c.html
python3 en111.py live/v115_3c.html live/v115h.html v115h
