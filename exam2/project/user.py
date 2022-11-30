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
        if not value and value is not str:
            raise ValueError("Invalid username!")
        self._username = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 6 and value is not int:
            raise ValueError("Users under the age of 6 are not allowed!")
        self._age = value

    def __str__(self):
        result =  f"Username: {self.username}, Age: {self.age}\n" \
               "Liked movies: \n"
        if not self.movies_liked:
            result += "No movies liked. \n"
        else:
            for movie in self.movies_liked:
                result += movie.details() + "\n"
        if not self.movies_owned:
            result += "No movies owned. \n"
        else:
            for movie in self.movies_owned:
                result += movie.details() + "\n"
        return result.strip()





