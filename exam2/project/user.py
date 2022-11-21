class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return  self._username

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Invalid username!")
        self._username = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self._age = value

    def __str__(self):
        result =  f"Username: {self.username}, Age: {self.age}\n" \
               "Liked movies: \n"
        if not self.movies_liked:
            result += "No movies liked. \n"
        else:
            for muve in self.movies_liked:
                result += muve.details() + "\n"
        if not self.movies_owned:
            result += "No movies owned. \n"
        else:
            for muve in self.movies_owned:
                result += muve.details() + "\n"
        return result.strip()





