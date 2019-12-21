#!/bin/bash

cd /home/pi/Desktop/Programs/NBA_Beautiful_Data
python3 main.py --update_to_current --log
git add player_box_scores.csv log.ini
git commit -m "Daily player box score update from raspi"
git push origin master