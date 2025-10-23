



class Email:
    def __init__(self, email_address, email_type):
        self.email_address = email_address
        self.email_type = email_type

    def __str__(self):
        return f"{self.email_address} ({self.email_type})"
