from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email_logging import log
import os

@dataclass(init = True)
class EmailData:
  reciever_email: str
  subject: str
  body: str
  attachments: list[str]

  log = log()

  def generate_mime_email(self):
    sender_email = os.getenv('MASS_EMAIL_ID')
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg['Subject'] = self.subject
    msg['To'] = self.reciever_email
    msg.attach(MIMEText(self.body, 'plain'))

    if len(self.attachments) > 0:
      for attachment_path in self.attachments:
        # try:
          with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)  
            part.add_header(
              "Content-Disposition",
              f"attachment; filename={os.path.basename(attachment_path)}",
            )  
            msg.attach(part)
        # except Exception as e:
        #   log.error(f"Could not attach file {attachment_path}: {str(e)}")
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
