from project.movie_specification.movie import Movie

class Fantasy(Movie):
    def __init__(self, title, year, owner, age_restriction = 6):
        super(Fantasy, self).__init__(title, year, owner, age_restriction)
        self.likes = 0

    @property
    def age_restriction(self):
        return self._age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 6:
            raise ValueError("Fantasy movies must be restricted for audience under 6 years!")
        self._age_restriction = value

    def details(self):
        return f"Fantasy - Title:{self.title}, Year:{self.year}, Age restriction:{self._age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"

