from project.movie_specification.movie import Movie

class Thriller(Movie):
    def __init__(self, title, year, owner, age_restriction = 16):
        super(Thriller, self).__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self._age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 16:
            raise ValueError("Thriller movies must be restricted for audience under 6 years!")
        self._age_restriction = value

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self._age_restriction}, Likes:{Movie.likes}, Owned by:{self.owner.username}"

