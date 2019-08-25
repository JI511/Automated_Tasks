
import sys
import os
import argparse
import smtplib
from email.message import EmailMessage


def main(log_path, pass_path):
    my_log_path = str(log_path)
    my_pass_path = str(pass_path)
    if os.path.exists(my_log_path) and my_log_path.endswith('.txt') and \
            os.path.exists(my_pass_path) and my_pass_path.endswith('.txt'):
        try:
            p_file = open(my_pass_path, 'r')
            gmail_pass = p_file.read()
            p_file.close()
            file = open(my_log_path, 'r')
            for line in file.readlines():
                if 'ERROR' in line or 'FAIL' in line:
                    gmail_sender = 'johnspibot@gmail.com'
                    recipient = 'johningwersen11@gmail.com'
                    subject = 'Personal_Fitness Repo Test Failure'
                    msg_body = 'Unit test failure!'
                    body = '\r\n'.join(['To: %s' % recipient,
                                        'From: %s' % gmail_sender,
                                        'Subject: %s' % subject,
                                        '', msg_body])
                    server = smtplib.SMTP(host='smtp.gmail.com', port=13268)
                    server.ehlo()
                    server.starttls()
                    server.login('johnspibot@gmail.com', gmail_pass)
                    try:
                        server.sendmail(gmail_sender, [recipient], body)
                    except:
                        print("There was an error")
                    server.quit()
                    sys.exit(1)
            file.close()
            sys.exit(0)
        except Exception:
            raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("log_path", help='The desired log file to check for unit test results.')
    parser.add_argument("pass_path", help='Path to a config.txt file that stores password for gmail.')
    args = parser.parse_args()
    main(args.log_path, args.pass_path)
