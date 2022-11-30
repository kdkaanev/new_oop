from project.movie_specification.movie import Movie


class Action(Movie):
    def __init__(self, title, year, owner, age_restriction):
        super().__init__(title, year, owner, age_restriction)
        self.likes = 0

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"
