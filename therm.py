import smtplib
import time
from email.mime.text import MIMEText

user_email, password = 'your_user_name@gmail.com', 'your_16_char_password'

idx = 0
while 1:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user_email, password)
    msg = MIMEText('')
    msg['Subject'] = 'temp:' + '23*F ' + time.asctime()
    server.sendmail('user_email', 'email_to_notifiy_1 email_to_notify_2 email_to_notify_3'.split(), msg.as_string())
    server.close()
    time.sleep(60*60)
    idx+=1
    print idx
    
