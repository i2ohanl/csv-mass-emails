import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_logging import log

log = log()

def print_email(email_msg):
    for part in email_msg.walk():
        if part.get_content_type() == 'text/plain':
            email_body = part.get_payload(decode=True).decode('utf-8')
    print()
    print("To:", email_msg["To"])
    print("Subject:", email_msg["Subject"])
    print(email_body)
    print()


    
def generate_email(sender_email, subject, reciever_email, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg['To'] = reciever_email
    msg.attach(MIMEText(body, 'plain'))
    return msg