/usr/bin/python3 check_log_file.py ../Personal_Fitness/logs.txt
if [ $? -eq 1 ]
then
  echo Error!
fi
