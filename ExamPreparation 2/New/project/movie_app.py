from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    USER_EXIST_ERROR_MESSAGE = "User already exists!"
    USER_NOT_EXIST_ERR0R_MESSAGE = "This user does not exist!"
    MOVIE_UPLOADED_ERROR_MESSAGE = "Movie already added to the collection!"

    def __init__(self):
        self.user_collection = []
        self.movies_collection = []
        self.user_by_username = {}

    def register_user(self, username: str, age: int):
        user = self.__get_user_by_username(username)
        if user:
            raise Exception(self.USER_EXIST_ERROR_MESSAGE)
        user = User(username, age)
        self.user_collection.append(user)
        self.user_by_username[user.username] = user

    def upload_movie(self, username: str, movie: Movie):
        user = self.__get_user_by_username(username)
        self.__validate_user_exist(user)

        self.__validate_is_movie_owner(user, movie)
        self.__validate_movie_not_uploaded(movie)
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__get_user_by_username(username)

        self.__validate_movie_uploadet(movie)

        movie.title = kwargs.get('title', movie.title)
        movie.year = kwargs.get('year', movie.year)
        movie.age_restriction = kwargs.get(('age_restriction', movie.age_restriction))
        return f"{user.username} successfully edited {movie.title} movie."

    def __get_user_by_username(self, username):
        return self.user_by_username.get(username, None)

    def __validate_user_exist(self, user):
        if user is None
            raise Exception(self.USER_NOT_EXIST_ERR0R_MESSAGE)

    def __validate_is_movie_owner(self, user, movie):
        if user != movie.owner:
            raise Exception(self.__build_not_movie_owner_error_message(user, movie))

    def __validate_movie_not_uploaded(self, movie):
        matching_movies = [m for m in self.movies_collection]
        if matching_movies:
            raise Exception(self.MOVIE_UPLOADED_ERROR_MESSAGE)

    def __validate_movie_uploaded(self, movie):
        try:
            self.__validate_movie_not_uploaded(movie)
            raise Exception(self.__bulid_movie_not_uploaded_error_mesage(movie))
        except:
            pass

    @staticmethod
    def __build_not_movie_owner_error_message(user, movie):
        return f"{user.username} is not the owner of the movie {movie.title}!"

    @staticmethod
    def __bulid_movie_not_uploaded_error_mesage(movie):
        return f"The movie {movie.title} is not uploaded!"
