import smtplib
import os
import sys
import utils.validation_utils as validation_utils
from email_logging import log

log = log()

class ServerHandler:

  _server = None
  _sender_email = None
  _sender_password = None

  def __init__(self):
    email = os.getenv('MASS_EMAIL_ID')
    password = os.getenv('MASS_EMAIL_PASSWORD')

    try:
      validation_utils.validate_email(email)
      log.info("Proceeding with sender email:", email)
      validation_utils.validate_password(password)
    except Exception as e:
      log.error(e.args[0])
      sys.exit(1)

    self._sender_email = email
    self._sender_password = password

  def start(self):
    log.info("Starting smtp server")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)      # Create the SMTP session
    server.login(self._sender_email, self._sender_password)       # Login with the provided credentials
    log.info("Email login successful!")
    self._server = server

  def send_email(self, email_msg):
    reciever_email = email_msg["To"]
    email = email_msg.as_string()
    self._server.sendmail(self._sender_email, reciever_email, email)
    log.email_sent("Email sent to:", reciever_email)

  def quit_if_started(self):
    if self._server:
      log.info("All emails sent successfully! Shutting down server")
      self._server.quit()
