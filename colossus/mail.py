"""

Sending mail through Mailtrap (https://mailtrap.io/) for testing only.
can be modified according to different SMTP domains.

Required fields -> SMTP Login details from configurations.ini

"""

import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from configparser import ConfigParser

def mail(pri, cipherKey, nonce):
    configur = ConfigParser()
    configur.read('configurations.ini')

    msg = MIMEMultipart()

    msg['Subject'] = 'Test mail with attachment'
    msg['From'] = configur.get('SMTPlogin', 'sender_address')
    msg['To'] = configur.get('SMTPlogin', 'receiver_address')

    # decrypt.py must be in the same directry, in case the location is modified it shouldbe reflected here also
    filename = 'decrypt.py'
    with open(filename, 'r') as f:
        part = MIMEApplication(f.read(), Name=basename(filename))

    part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
    msg.attach(part)

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login(configur.get('SMTPlogin', 'mailtrap_user'), configur.get('SMTPlogin', 'mailtrap_password'))
        server.sendmail(configur.get('SMTPlogin', 'sender_address'), configur.get('SMTPlogin', 'receiver_address'), msg.as_string())
        print("Successfully sent email")
