import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_mail(subject, body):

    sender_email = "emodikoff@gmail.com"
    sender_password = os.getenv("PASSWORD")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    receiver_mail = sender_email

    msg = MIMEMultipart()
    msg['From:'] = sender_email
    msg['To'] = receiver_mail
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(sender_email,sender_password)
        text = msg.as_string()
        server.sendmail(sender_email,receiver_mail,text)
        server.quit()
        print("Благодаря вече всичко е планирано очаквай изненада 🥳")
    except Exception as e:
        print(f"Нещо си объркала ако е много батак ми прати това което следва 😂: {e}")