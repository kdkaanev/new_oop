class EmailCalidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        name = self.email.split('@')[0]

    def __is_mail_valid(self, mail):
        pass

    def __is_domain_valid(self, domain):
        pass

    def validate(self, email):
        self.email = email