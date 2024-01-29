#Gmail Automation

import smtplib
from email.mime.text import MIMEText

def sendEmail(subject,body,sender,recipient,password):
    print(sender)
    print(password)
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
        server.login(sender,password)
        server.sendmail(sender,recipient,msg.as_string())
    print("Sent")
    
