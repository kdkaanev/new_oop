class Profile:
    def __init__(self, username, password):
        self.usernsme = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password (self, value):
        is_correct_lengh = len(value) >= 8
        is_uper = [ch for ch in value if ch.isupper()]
        is_digit = [num for num in value if num.isdigit()] 
        is_correct = (is_correct_lengh and len(is_uper) > 0 and len(is_digit) > 0)
        if not is_correct:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{Profile.__username}" and password: {"*" * len(Profile.__password)}'



correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)

