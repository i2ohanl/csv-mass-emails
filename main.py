import argparse
import logging as log
from tqdm import tqdm
import models.smtp_server as smtp_server
import utils.email_utils as email_utils
import utils.validation_utils as validation_utils
from models.csv_data import CSVData
from email_logging import log

log = log()

def processCsvAndSendEmail(csv_path, test):
    server = smtp_server.ServerHandler()
    csv_data_handler = CSVData(csv_path)
    csv_data_handler.generate_emails()
    if test == False:
        executable = server.send_email
        server.start()
    else:
        log.info("Test config selected, printing all emails")
        executable = email_utils.print_email
    handle_email_data(executable, csv_data_handler.emails)
    server.quit_if_started()

def handle_email_data(func, emails):
    for email in tqdm(emails, disable=(func.__name__ == "print_email")):
      email_msg = email.generate_mime_email()
      func(email_msg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a CSV file.")
    parser.add_argument("-f", type=str, help="Path to the CSV file")
    parser.add_argument("--test", action='store_true', help="Test run (prints emails in console)")
    args = parser.parse_args()

    csv_path = args.f
    try:
      validation_utils.validate_csv_path(csv_path)
      log.info("CSV path provided:", csv_path)
    except Exception as e:
      log.error(e.args[0])
    processCsvAndSendEmail(csv_path, args.test)