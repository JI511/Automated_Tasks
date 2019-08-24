#!/bin/bash
# checkout specific repos or update if already exists

cd /home/pi/Desktop/Programs/Personal_Fitness
if [ -d "/home/pi/Desktop/Programs/Personal_Fitness" ]
then
    pwd
    echo "Directory already exists, updating"
    git pull origin master
else
    pwd
    echo "Directory does not exists, checking out"
    git clone https://github.com/JI511/Personal_Fitness.git
fi
