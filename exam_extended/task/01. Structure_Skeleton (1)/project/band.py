class Band:
    def __init__(self, name: str):
        self.name = name
        self.members = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Band name should contain at least one character!")
        self.__name = value

    def __str__(self) -> str:
        return f"{self.__class__.__name__} with {len(self.members)} members."