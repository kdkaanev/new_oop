class Concert:
    CORRECT_GENRE = ["Metal", "Rock", "Jazz"]

    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__not_correct_genre(value)
        self.__genre = value

    @property
    def audience(self):
        return self.__audience

    @audience.setter
    def audience(self, value):
        self.__not_min_count(value)
        self.__audience = value

    @property
    def ticket_price(self):
        return self.ticket_price

    @ticket_price.setter
    def ticket_price(self, value):
        self.__not_min_ticketprice(value)
        self.__ticket_price = value

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        self.__expenses__is_negative_number(value)
        self.__expenses = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        self.__name_plase_not_correct(value)
        self.__place = value

    def __str__(self):
        return f"{self.genre} concert at {self.place}."

    def __not_correct_genre(self, genre):
        if genre not in self.CORRECT_GENRE:
            raise ValueError(f"Our group doesn't play {genre}!")

    @staticmethod
    def __not_min_count(count):
        if count < 1:
            raise ValueError("At least one person should attend the concert!")

    @staticmethod
    def __not_min_ticketprice(price):
        if price < 1.0:
            raise ValueError("Ticket price must be at least 1.00$!")

    @staticmethod
    def __expenses__is_negative_number(number):
        if number < 0.00:
            raise ValueError("Expenses cannot be a negative number!")

    @staticmethod
    def __name_plase_not_correct(name:str):
        if len(name) < 2 or name.isspace():
            return "Place must contain at least 2 chars. It cannot be empty!"

