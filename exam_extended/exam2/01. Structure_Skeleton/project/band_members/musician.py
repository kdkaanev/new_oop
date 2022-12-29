from abc import ABC, abstractmethod



class Musician(ABC):
    learned_skills = []
    MIN_MUSICIANS_AGE = 16
    EMPTY_STRING_ERROR_MESSAGE = "Musician name cannot be empty!"

    @abstractmethod
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value.isspace():
            raise ValueError(self.EMPTY_STRING_ERROR_MESSAGE)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MIN_MUSICIANS_AGE:
            raise ValueError(f"Musicians should be at least {self.MIN_MUSICIANS_AGE} years old!")
        self.__age = value

    @abstractmethod
    def learn_new_skill(self, new_skill: str):
        pass
    @abstractmethod
    def type(self):
        pass
