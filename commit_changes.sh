#!/bin/bash

cd /home/pi/Desktop/Programs/Automated_Tasks
git pull origin master
git add .
git commit -m "Auto-commit of changes."
git push origin master