import re

def validate_email(email):
    email_regex = r'^[^@]+@[^@]+\.[^@]+$'
    if re.match(email_regex, email) == None:
        raise Exception("Invalid email format: " + email)

def validate_password(password):
    password_regex = r'^([a-z0-9]{4} ){3}[a-z0-9]{4}$'
    if re.match(password_regex, password) == None:
        raise Exception("Invalid password format, recheck and try again")
    
def validate_csv_path(path):
    if path == None:
        raise Exception("CSV file path missing. Please enter valid .csv file path using \"-f your_file.csv\"")
    path_regex = r'^.*\.csv$'
    if re.match(path_regex, path) == None:
        raise Exception("Invalid path: " + path + ". The file should be a .csv file")