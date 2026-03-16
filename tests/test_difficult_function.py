import unittest

from unittest.mock import patch
from lecture import difficult_function

class MyTestCase(unittest.TestCase):
    @patch('lecture.complex_math')
    def test_difficult_function_1(self, complex_math_mock):
        complex_math_mock.return_value = 0
        self.assertEqual(first="solved!",
                         second=difficult_function(1,2))

    @patch('lecture.complex_math')
    def test_difficult_function_2(self, complex_math_mock):
        complex_math_mock.return_value = 1
        self.assertEqual(first="not yet",
                         second=difficult_function(1,2))