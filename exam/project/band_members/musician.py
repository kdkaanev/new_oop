from abc import ABC, abstractmethod


class Musician(ABC):
    MUSICIAN_MIN_AGE = 16
    EMPTY_NAME_ERROR_MESSAGE = "Musician name cannot be empty!"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__string_is_empty(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__min_age_musician(value)
        self.__age = value

    @abstractmethod
    def learn_new_skill(self, new_skill: str):
        self.__new_skill_already_learned(new_skill)

        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."

    @abstractmethod
    @property
    def type(self):
        pass

    def __string_is_empty(self, name: str):
        if not name or name.isspace():
            raise ValueError(self.EMPTY_NAME_ERROR_MESSAGE)

    def __min_age_musician(self, age):
        if age < self.MUSICIAN_MIN_AGE:
            raise ValueError(f'"Musicians should be at least {self.MUSICIAN_MIN_AGE} years old!"')

    def __new_skill_already_learned(self, skill):
        if skill in self.skills:
            raise Exception(f"{skill} is already learned!")
