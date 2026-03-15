import unittest
from prep import strange_function

class MyTestCase(unittest.TestCase):
    def test_strange_function1(self):
        self.assertEqual(
            first=strange_function(1, 2, 3, 4),
            second='behaviour 3'
        )

    def test_get_behaviour1(self):
        self.assertEqual(
            first=strange_function(1, 1, 3, 4),
            second='behaviour 1'
        )

    def test_get_behaviour2(self):
        self.assertEqual(
            first=strange_function(1, 1, 4, 3),
            second='behaviour 2'
        )

    def test_get_behaviour4(self):
        self.assertEqual(
            first=strange_function(4, 3, 1, 1),
            second='behaviour 4'
        )

    def test_get_behaviour5(self):
        self.assertEqual(
            first=strange_function(4, 2, 1, 4),
            second='behaviour 5'
        )

    def test_get_behaviour6(self):
        self.assertEqual(
            first=strange_function(4, 2, 4, 4),
            second='behaviour 6'
        )
