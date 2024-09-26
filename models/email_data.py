from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

@dataclass(init = True)
class EmailData:
  reciever_email: str
  subject: str
  body: str
  attachments: list[str] = None

  def generate_mime_email(self):
    sender_email = os.getenv('MASS_EMAIL_ID')
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg['Subject'] = self.subject
    msg['To'] = self.reciever_email
    msg.attach(MIMEText(self.body, 'plain'))
    return msg
  
  def print_email(email_msg):
    for part in email_msg.walk():
        if part.get_content_type() == 'text/plain':
            email_body = part.get_payload(decode=True).decode('utf-8')
    print()
    print("To:", email_msg["To"])
    print("Subject:", email_msg["Subject"])
    print(email_body)
    print()
