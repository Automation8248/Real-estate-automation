import os, smtplib
from email.mime.text import MIMEText

def send_email(to, subject, body):
    user=os.getenv("EMAIL_USER")
    pwd=os.getenv("EMAIL_PASS")
    msg=MIMEText(body)
    msg["From"]=user
    msg["To"]=to
    msg["Subject"]=subject
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(user,pwd)
    s.send_message(msg)
    s.quit()
  
