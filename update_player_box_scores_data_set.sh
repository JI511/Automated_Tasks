#!/bin/bash

cd /home/pi/Desktop/Programs/NBA_Beautiful_Data
python main.py --yesterday
git add player_box_scores.csv
git commit -m "Daily player box score update from raspi"
git push origin master