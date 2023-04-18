class Jockey:
    MIN_JOCKEY_AGE = 18
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 0:
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MIN_JOCKEY_AGE:
            return ValueError(f"Jockeys must be at least {self.MIN_JOCKEY_AGE - 1} to participate in the race!")
        self.__age = value