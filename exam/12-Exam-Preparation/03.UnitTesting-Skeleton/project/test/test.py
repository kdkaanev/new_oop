from project.movie import Movie
from unittest import TestCase


class TestMovie(TestCase):
    NAME = 'Huj'
    YEAR = 1956
    RATiNG = 8
    MIN_YEAR = 1887

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATiNG)

    def test_init_mouve(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATiNG, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter__when_is_empty_string__espected_raise(self):
        with self.assertRaises(ValueError) as er:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(er.exception))

    def test_year_setter__when_year_less_min_year__espected_raise(self):
        with self.assertRaises(ValueError) as er:
            self.movie.year = self.MIN_YEAR - 1
        self.assertEqual("Year is not valid!", str(er.exception))

    def test_add_actor__when_actor_is_not_exist__espected_add(self):
        first = 'hujo'
        second = 'mujo'
        self.movie.add_actor(first)
        self.movie.add_actor(second)
        self.assertEqual([first, second], self.movie.actors)

    def test_add_actor__when_actor_already_been_added__espected_not_add(self):
        name = 'hujo'
        self.movie.actors = [name]
        result = self.movie.add_actor(name)

        self.assertEqual(f"{name} is already added in the list of actors!", result)
        self.assertEqual([name], self.movie.actors)








