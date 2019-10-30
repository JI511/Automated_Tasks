#!/bin/bash
# checkout specific repos or update if already exists

cd /home/pi/Desktop/Programs
if [ -d "/home/pi/Desktop/Programs/Personal_Fitness" ]
then
    cd Personal_Fitness/
    pwd
    echo "Directory already exists, updating"
    git pull origin master
else
    pwd
    echo "Directory does not exists, checking out"
    git clone https://github.com/JI511/Personal_Fitness.git
fi

cd /home/pi/Desktop/Programs
if [ -d "/home/pi/Desktop/Programs/NBA_Beautiful_Data" ]
then
    cd NBA_Beautiful_Data/
    pwd
    echo "Directory already exists, updating"
    git pull origin master
else
    pwd
    echo "Directory does not exists, checking out"
    git clone https://github.com/JI511/NBA_Beautiful_Data.git
fi

cd /home/pi/Desktop/Programs/Automated_Tasks
python log_date.py
