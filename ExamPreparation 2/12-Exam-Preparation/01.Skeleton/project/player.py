from project import controller
from project.utill import validate
from project import supply
class Player:
    MIN_PLAYER_AGE = 12
    MIN_STAMINA = 0
    MAX_STAMINA = 100
    STAMINA_ERROR_MESSAGE = "Stamina not valid!"
    NAME_ERROR_MESSAGE = "Name not valid!"
    player_name = []
    def __init__(self, name: str, age: int, stamina=MAX_STAMINA):
        self.name = name
        self.age = age
        self.stamina = stamina






    @property
    def name (self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_empty_string(value, self.NAME_ERROR_MESSAGE)
        self.__validate_name_exist(value)
        self.player_name.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_min_number(value, self.__generate_age_error_message(value), self.MIN_PLAYER_AGE)
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        self.__validate_min_number(value, self.STAMINA_ERROR_MESSAGE, self.MIN_STAMINA)
        self.__validate_max_number(value, self.STAMINA_ERROR_MESSAGE, self.MAX_STAMINA)
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < self.MAX_STAMINA

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

    def __validate_name_exist(self,name):
        for n in self.player_name:
            if n == name:
                raise Exception(f"Name {name} is already used!")


    def __generate_name_exist_error_message(self,name):
        return f"Name {name} is already used!"

    def __generate_age_error_message(self,age):
        return f"The player cannot be under {self.MIN_PLAYER_AGE} years old!"

    @staticmethod
    def __validate_empty_string(name, err_message):
        if not isinstance(name, str) or len(name) == 0:
            raise err_message

    @staticmethod
    def __validate_min_number(value, err_message, num):
        if not isinstance(value, (int, float)) or value < num:
            raise ValueError(err_message)

    @staticmethod
    def __validate_max_number(value, err_message, num):
        if not isinstance(value, (int, float)) or value > num:
            raise ValueError(err_message)

