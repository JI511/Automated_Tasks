# Automated_Tasks
Bash and Python scripts that are run via Cron Jobs. Used in tandem with a Raspberry Pi 3B+.

Some are configured to run daily, others every hour.

First, check_for_modifications.sh is run to determine if some of my repos have been checked out yet on the device. If not, script will clone master. If repo already exists it will check if the repository is up to date.

Second, all unit tests will be run for Personal_Fitness with unit_test_executor.sh.

Third, is_failure_notification_needed.sh will use the python script check_log_file.py to determine if the unit test executed without error or failure. If an error or failure occurred, I will be notified via email.
