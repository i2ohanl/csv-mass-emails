from dataclasses import dataclass
from models.email_data import EmailData
from utils import string_utils
from utils import validation_utils
from email_logging import log
import csv
import sys

log = log()

@dataclass(init=True)
class CSVData:
  csv_file_path: str
  emails: list[EmailData] = None

  def generate_emails(self):
    self.emails = list()
    with open(self.csv_file_path, mode='r') as file:
      csv_reader = csv.reader(file)
      
      subject = next(csv_reader)[1]
      body_template = next(csv_reader)[1]
      next(csv_reader) # Skip headers

      try:
        for row in csv_reader:
          reciever_email = row[0]
          data = row[1:]
          validation_utils.validate_email(reciever_email)
          body = string_utils.replace_placeholders(body_template, data)
          
          email = EmailData(reciever_email, subject, body)
          self.emails.append(email)
        # TODO: Make option to skip invalid data
      except Exception as e:
        log.error(e.args[0])
        sys.exit(1)

  


