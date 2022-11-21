from project.movie_specification.movie import Movie

class Action(Movie):
    def __init__(self, title, year, owner, age_restriction = 12):
        super(Action, self).__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self._age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 12:
            raise ValueError("Action movies must be restricted for audience under 12 years!")
        self._age_restriction = value

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, Age restriction:{self._age_restriction}, Likes:{Movie.likes}, Owned by:{self.owner.username}"

