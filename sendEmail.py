import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# # comment implies that the field needs to be filled in
def sendEmail(subject, message_body):
    fromaddr = "smtp-mailjet@joshsisto.com"  # from email address
    toaddr = "josh@joshsisto.com"  # destination email address
    smtp_user = "591b58f61363d5d9d7518d7e96ecefd0"  # SMTP username used for authentication
    smtp_pass = "cea1ca5b0ce623b465c02da9816832ad"  # SMTP password used for authentication
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject  # subject

    body = message_body  # body
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('in-v3.mailjet.com', 587)  # e.g. ('in-v3.mailjet.com', 587)
    server.starttls()
    server.login(smtp_user, smtp_pass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()