import json
from typing import Dict

from shared import FILE_PATH_ROOT
from models import Email



class EmailsRepo:
    def __init__(self, file_path=FILE_PATH_ROOT + "emails.json"):
        self.file_path = file_path
        self.emails = self.get_all_emails()

    def save_email(self, email: Email):
        self.emails.append(email)
        emails_dicts = [self._email_to_dict(email) for email in self.emails]
        with open(self.file_path, "w") as file_writer:
            json.dump(emails_dicts, file_writer, indent=4)

    def get_all_emails(self):
        try:
            with open(self.file_path, "r") as file_reader:
                self.emails = json.load(file_reader)
            # Opis nize u komentaru
            return [self._dict_to_email(email) for email in self.emails]
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return []
        except Exception as e:
            print(f"Error reading emails from file: {e}")
            return []

    def _dict_to_email(self, email_dict: Dict):
        return Email(email_dict['email_address'], email_dict['email_type'])

    def _email_to_dict(self, email: Email):
        return {'email_address': email.email_address, 'email_type': email.email_type}


'''
Pojasnjenje linije 24

nova_lista = []
for element in elements:
    nova_lista.append(element.lower())

Ovo gore se moze napisati krace koristeci list comprehension:
nova_lista = [element.lower() for element in elements]
return nova_lista

return [element.lower() for element in elements]
'''