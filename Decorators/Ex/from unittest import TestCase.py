from unittest import TestCase



class FirstTests(TestCase):
    def test_expect_1_to_equal_1(self):
        self.assertEqual(1, 2)