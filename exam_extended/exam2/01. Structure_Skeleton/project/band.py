class Band:
    EMPTY_STRING_ERROR_MESSAGE = "Band name should contain at least one character!"

    def __init__(self, name: str):
        self.name = name
        self.members = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value.isspace():
            raise ValueError(self.EMPTY_STRING_ERROR_MESSAGE)
        self.__name = value

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."
