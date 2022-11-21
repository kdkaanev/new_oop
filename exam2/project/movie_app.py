from movie_specification.movie import Movie
from user import User


class MovieApp:
    USER_EXIST_ERROR_MESAGE = "User already exists!"

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []
        self.users_by_name = {}

    def register_user(self, username: str, age: int):
        """
        Creates an instance of the User class with the given username and age, and:
         - If the user (object) is not in the users_collection list, add him/her and return the message:
            "{username} registered successfully."
         -If a user with the same username is already registered, raise an Exception with the message
            "User already exists!"


        """
        user = self.__get_user_by_name(username)
        if user:
            raise Exception(self.USER_EXIST_ERROR_MESAGE)
        user = User(username, age)
        self.users_collection.append(user)
        self.users_by_name[user.username] = user
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        """
        Only the owner of the given movie can upload it.
        The method adds the movie to the user's movies_owned list as well as the movies_collection list:
        - If the addition is successful, returns the message:
            "{username} successfully added {movie_title} movie."
        - If the user with the username provided is not registered in the app, raise an Exception with the message:
            "This user does not exist!"
        - If the user exists, but he/she is not the owner of the given movie, raise an Exception with the message:
            "{username_given} is not the owner of the movie {movie_title}!"
        - If the movie object is already uploaded, raise an Exception with the message:
            "Movie already added to the collection!"

        """
        user = self.__get_user_by_name(username)
        if not user:
            raise Exception("This user does not exist!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        if movie not in User.








    def edit_movie(self, username: str, movie: Movie, **kwargs):
        pass

    def delete_movie(self, username: str, movie: Movie):
        pass

    def like_movie(self, username: str, movie: Movie):
        pass

    def dislike_movie(self, username: str, movie: Movie):
        pass

    def display_movies(self):
        pass

    def __str__(self):
        pass

    def __get_user_by_name(self, username):
        return self.users_by_name.get(username, None)
