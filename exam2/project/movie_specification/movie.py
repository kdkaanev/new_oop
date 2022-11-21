from abc import ABC, abstractmethod
from project.user import User

class Movie(ABC):
    MIN_MOVIE_YEAR = 1888
    def __int__(self, title: str, year: int, owner: object, age_restriction: int):
        self.age_restriction = age_restriction
        self.owner = owner
        self.year = year
        self.title = title
        self.likes = 0

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("The title cannot be empty string!")
        self._title = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value < self.MIN_MOVIE_YEAR:
            raise ValueError("Movies weren't made before 1888!")
        self._year = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")
        self._owner = value

    @abstractmethod
    def details(self):
        pass


