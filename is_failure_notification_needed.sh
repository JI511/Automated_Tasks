#!/bin/bash
# reads the unit test output log to see if failures occurred. Will notify user if true.

/usr/bin/python3 check_log_file.py ../Personal_Fitness/logs.txt config.txt
if [ $? -eq 1 ]
then
  echo Error!
fi
