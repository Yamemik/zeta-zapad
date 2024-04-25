from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(text, email):
    msg = MIMEMultipart()
    msg['From'] = "para22mount@gmail.com"
    msg['To'] = email
    msg['Subject'] = "No replay"
    msg.attach(MIMEText(text, 'plain'))

    smtpObj = smtplib.SMTP('smtp.gmail.com')
    smtpObj.starttls()
    smtpObj.login(msg['From'], 'wknl lnwz yuzg wmul')
    smtpObj.sendmail(msg['From'], msg['To'], msg.as_string())
    smtpObj.quit()