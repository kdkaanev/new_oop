from abc import ABC, abstractmethod

from project.user import User
from project.utils.validates import validate_non_empty_string, validate_greater_that_value


class Movie(ABC):
    MIN_YEAR = 1888
    MIN_AGE_RESTRICTION = None

    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return

    @title.setter
    def title(self, value):
        self.__validate_title(value)
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__validate_year(value)
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__validate_owner(value)
        self.owner = value

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        self.__validate_age_restriction(value)
        self.__age_restriction = value

    @property
    def age_restriction_error_message(self):
        return f"{self.type} movies must be restricted for audience under {self.age_restriction} years!"

    @staticmethod
    def __validate_title(title):
        validate_non_empty_string(title, "The title cannot be empty string!")

    @classmethod
    def __validate_year(cls, year):
        validate_greater_that_value(year, cls.MIN_YEAR, f"Movies weren't made before {cls.MIN_YEAR}!")

    @staticmethod
    def __validate_owner(owner):
        if owner not in User:
            raise ValueError("The owner must be an object of type User!")

    def validate_age_restriction(self, age_restriction):
        validate_greater_that_value(age_restriction, self.MIN_AGE_RESTRICTION, self.age_restriction_error_message)

    def details(self):
        return f"{self.type} -" \
               f'Title:{self.title},' \
               f'Year:{self.year},' \
               f'Age restriction:{self.age_restriction},' \
               f'Likes:{self.likes},' \
               f'Owned by:{self.owner.usrname}'

    @abstractmethod
    @property
    def type(self):
        return
