from typing import Any
from unittest import TestCase

from extended_list import IntegerList


class TestIntegerList(TestCase):
    DATA = []
    def setUp(self) -> None:
        self.integer = IntegerList()
        
    def test_init__input_args_espected_int(self):
        self.assertEqual(self.DATA, self.integer.__data)

    def test_add__element_not_integer__espected_raise(self):
        integer = IntegerList('huj')
        with self.assertRaises(ValueError) as ex:
            integer.add()
            self.assertEqual( "Element is not Integer", ex)


    def test_remove_index__index_out_of_range__espected_raise(self):
        self.DATA = []
        with self.assertRaises(IndexError) as ex:
            self.integer.remove_index()
            self.assertEqual("Index is out of range", ex)

    def test_get__index_out_of_range__espected_raise(self):
        self.DATA = []
        with self.assertRaises(IndexError) as ex:
            self.integer.get()
            self.assertEqual("Index is out of range", ex)
            

    def test_insert__index_out_of_range__espected_raise(self):
        with self.assertRaises(IndexError) as ex:
            self.integer.test()
            self.assertEqual("Index is out of range", ex)

    def test_insert__element_not_integer__espected_raise(self):
        pass

    def test_get_biggest__espected_element_0_is_biggest(self):
        pass        