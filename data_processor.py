import csv
import sys
import utils.string_utils as string_utils
import utils.email_utils as email_utils
import utils.validation_utils as validation_utils
from email_logging import log

log = log()

def parse_csv_data(csv_path):
  log.info("Proceeding to parse csv")
  result = dict()
  with open(csv_path, mode='r') as file:
        csv_reader = csv.reader(file)

        result["subject"] = next(csv_reader)[1]
        body_template = next(csv_reader)[1]

        next(csv_reader) # Skip headers

        result["email_data"] = list()
        try:
          for row in csv_reader:
            row_data = dict()
            row_data["body"] = string_utils.replace_placeholders(body_template, row[1:])
            reviever_email = row[0]
            validation_utils.validate_email(reviever_email)
            row_data["reciever_email"] = row[0]
            result["email_data"].append(row_data)
        # TODO: Make option to skip invalid data
        except Exception as e:
          log.error(e.args[0])
          sys.exit(1)
  log.info("Parsed csv, valid email data points found:", len(result["email_data"]))
  return result

def process_email_data(func, sender_email, data):
    subject = data["subject"]
    log.info("Email subject:", subject)
    for row_data in data["email_data"]:
      reciever_email = row_data["reciever_email"]
      body = row_data["body"]
      email_msg = email_utils.generate_email(sender_email, subject, reciever_email, body)
      func(email_msg)
      


