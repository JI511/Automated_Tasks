
import sys
import os
import argparse
import smtplib
from email.message import EmailMessage


def main(path):
    file_path = str(path)
    if os.path.exists(file_path) and file_path.endswith('.txt'):
        try:
            file = open(file_path, 'r')
            for line in file.readlines():
                if 'ERROR' in line or 'FAIL' in line:
                    msg = EmailMessage()
                    msg.set_content('Unit test failure!')
                    msg['Subject'] = 'Personal_Fitness Repo Test Failure'
                    msg['From'] = 'johningwersen11@gmail.com'
                    msg['To'] = 'johningwersen11@gmail.com'
                    s = smtplib.SMTP('localhost')
                    s.send_message(msg)
                    s.quit()
                    sys.exit(1)
            sys.exit(0)
        except Exception:
            raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help='The desired log file to check for unit test results.')
    args = parser.parse_args()
    main(args.path)
