# Automated_Tasks
Bash and Python scripts that are run via Cron Jobs. Used in tandem with a Raspberry Pi 3B+.
Currently configured to run every 20 minutes.

First, check_for_modifications.sh is run to determine if my Personal_Fitness repo has been checked out yet on the device. If not, it will clone master. If it already exists it will check if the repository is up to date.

Second, all unit tests will be run with unit_test_executor.sh.

Third, is_failure_notification_needed.sh will use the python script check_log_file.py to determine if the unit test executed without error or failure. If an error or failure occurred, the user will be notified via email.
