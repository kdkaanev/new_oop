import os

from project.movie_specification.movie import Movie
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
        ***Only the owner of the given movie can upload it.***
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

        self.__validate_user_not_owner_movie(user, movie)
        self.__validate_movie_already_exist(movie)

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        """
        ***Only the owner of the movie given can edit it. You will always be given usernames of registered users.***
        ***In this method, as kwargs you can receive one or more key-value pairs***
           Each key will be a movie's attribute name ("title", "year", or "age_restriction")
           The value will be the new value for that attribute
           You will not receive anything different from the keys mentioned above.
           The method edits the movie attributes with the given values
            - returns the message "{username} successfully edited {movie_title} movie."
            -If the movie is not uploaded
                raise an Exception with the message "The movie {movie_title} is not uploaded!"
            -If the user does not own that movie
            raise an Exception with the message "{username given} is not the owner of the movie {movie_title}!"


        """

        user = self.__get_user_by_name(username)
        self.__validate_movie_not_exist(movie)
        self.__validate_user_not_owner_movie(user, movie)

        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            elif key == "year":
                movie.year = value
            elif key == "age_restriction":
                movie.owner = value
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        """
        ***Only the owner of the movie given can delete it***
        ***You will always be given usernames of registered users***
    This method deletes the movie given in both 'movies_collection' and user's 'movies_owned' lists.
        -Return the message "{username} successfully deleted {movie_title} movie."
    If the movie is not uploaded
        -Raise an Exception with the message "The movie {movie_title} is not uploaded!"
    If the user does not own that movie
        -Raise Exception with the message "{username given} is not the owner of the movie {movie_title}!"


        """
        user = self.__get_user_by_name(username)
        self.__validate_movie_not_exist(movie)
        self.__validate_user_not_owner_movie(user, movie)

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        """
        ***Owners cannot like their own movies***
        ***You will always be given usernames of registered users and uploaded movies.***
        Increases the value of the movie attribute 'likes' by 1.
        Adds the movie to the user's list 'movies_liked'.
            -Returns the message "{username} liked {movie_title} movie."
        If the user is also the owner:
            -Raise an Exception with the message "{username} is the owner of the movie {movie_title}!"
        If the user already liked that movie:
            -Raise an Exception with the message "{username} already liked the movie {movie_title}!"


        """
        user = self.__get_user_by_name(username)
        self.__validate_user_owner_movie(user, movie)
        self.__validate_user_liked_movie(user, movie)

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        """
        ***Only the user who has liked the movie can dislike it***
        ***You will always be given usernames of registered users and uploaded movies-***
        Decreases the value of the movie attribute 'likes' by 1.
            -Removes that movie from the user's 'movies_liked' list.
            -Returns the message "{username} disliked {movie_title} movie."
•	    If the user didn't like that movie in the first place:
            -Raise an Exception with the message "{username} has not liked the movie {movie_title}!"

        """
        user = self.__get_user_by_name(username)
        self.__validate_user_not_liked_movie(user, movie)

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        """
        Sorts all movies uploaded by the year in descending order.
        If there are two or more movies of the same year:
            -Sort them by title:
            -It should return the 'details()' for each movie on separate lines in the format.
	    If there are no movies uploaded:
	        -Returns: "No movies found."
	    """
        if not self.movies_collection:
            return "No movies found."

        sorted_movie = sorted(self.movies_collection, key=self.__movie_order_by)
        return os.linesep.join(m.details() for m in sorted_movie)

    def __str__(self):
        """
            Return a string on 2 lines for all users' usernames and movies titles in the following format:
            "All users: {all users' usernames separated by a comma and a space ", "}"
                -If no users: "All users: No users."
            "All movies: {all movies' titles separated by a comma and a space ", "}"
                -If no movies: "All movies: No movies."

        """
        user_string = 'No users.'
        movie_string = 'No movies.'

        if self.users_collection:
            user_string = ', '.join(u.username for u in self.users_collection)
        if self.movies_collection:
            movie_string = ', '.join(m.title for m in self.movies_collection)

        return f'''All users: {user_string}
All movies: {movie_string}
'''


    def __get_user_by_name(self, username):
        return self.users_by_name.get(username, None)

    def __validate_user_owner_movie(self, user, movie):
        if movie in user.movies_owned:
            return f"{user.username} is the owner of the movie {movie.title}!"

    def __validate_user_not_owner_movie(self, user, movie):
        if movie not in user.movies_owned:
            return f"{user.username} is not the owner of the movie {movie.title}!"

    def __validate_movie_already_exist(self, movie):
        matching_movie = [m for m in self.movies_collection if m == movie]
        if matching_movie:
            raise Exception("Movie already added to the collection!")

    def __validate_movie_not_exist(self, movie):
        matching_movie = [m for m in self.movies_collection if m == movie]
        if not matching_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")

    @staticmethod
    def __validate_user_liked_movie(user, movie):
        liked_movie = [m for m in user.movies_liked if m == movie]
        if liked_movie:
            return f"{user.name} already liked the movie {movie.title}!"

    @staticmethod
    def __validate_user_not_liked_movie(user, movie):
        liked_movie = [m for m in user.movies_liked if m == movie]
        if not liked_movie:
            return f"{user.name} has not liked the movie {movie.title}!"

    @staticmethod
    def __movie_order_by(movie: Movie):
        return (-movie.year, movie.title)

