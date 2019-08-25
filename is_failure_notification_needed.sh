#!/bin/bash
# reads the unit test output log to see if failures occurred. Will notify user if true.

echo "starting.." > status.txt
/usr/bin/python3 check_log_file.py ../Personal_Fitness/logs.txt config.txt
if [ $? -eq 1 ]
then
  echo "Error!" >> status.txt
else
  echo "Looks good!" >> status.txt
fi
