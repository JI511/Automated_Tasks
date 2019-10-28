#!/bin/bash

cd /home/pi/Desktop/Programs/Automated_Tasks
python main.py --yesterday
git add .
git commit -m "Daily player box score update from raspi"
git push origin master