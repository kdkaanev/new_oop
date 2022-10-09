

from TestWorker.test_cat import Cat
import unittest
from unittest import TestCase


class TestCat(TestCase):
    NAME = 'Puh'
    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test_eat__espect_size_increased(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_eat__espect_is_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_eat__when_already_fed__espected_raise(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertIsNotNone(ex)

    def test_sleep__when_not_fed__espected_raise(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertIsNotNone(ex)



    def test_sleep__when_already_sliping__espected_non_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

if __name__ == '__name__':
    unittest.main()