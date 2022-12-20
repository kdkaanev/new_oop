
import os
from


class User:
    MIN_USERNAME_LENGTH = 1
    MIN_AGE = 6

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_username(value)
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    def __validate_username(self, username):
        valiodate_non_empty_string(username, "Invalid username!")

    def __validate_age(self, age):
        if age is not int or age < self.MIN_AGE:
            raise ValueError(f"Users under the age of {self.MIN_AGE} are not allowed!")

    def __str__(self):
        movies_liked_str = "No movies liked."
        if self.movies_liked:
            movies_liked_str = os.linesep.join(m.details() for m in self.movies_liked)

        movies_owned_str = "No movies owned."
        if self.movies_owned:
            movies_owned_str = os.linesep.join(m.details() for m in self.movies_owned)

        return f"Username: {self.username}, Age: {self.age}" \
               "Liked movies:" \
               f'{movies_liked_str}' \
               "Owned movies:" \
               f'{movies_owned_str}'
