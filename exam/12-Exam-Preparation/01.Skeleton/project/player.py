from unicodedata import name


class Player:
    MIN_AGE = 12
    MAX_STAMINA = 100
    MIN_STAMINA = 0
    names = set()
    def __init__(self, name: str, age: int, stamina = 100):
        self.name = name
        self.age = age
        self.stamina = stamina


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name not valid!")
        if value in self.names:
            raise ValueError(f"Name {value} is already used!")
        self.names.add(value)
        self.__name = value


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.MIN_AGE:
            raise ValueError('The player cannot be under 12 years old!')
        self.__age = value

    
    @property
    def stamina(self):
        return self.__stamina


    @stamina.setter
    def stamina(self, value):
        if self.MIN_STAMINA < value > self.MAX_STAMINA:
            raise ValueError('Stamina not valid!')
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.__stamina < self.MAX_STAMINA

    def __str__(self) -> str:
        return f'Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}'


    

