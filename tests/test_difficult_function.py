import unittest

from unittest.mock import MagicMock, patch
from lecture import difficult_function, complex_math

class MyTestCase(unittest.TestCase):
    @patch('lecture.complex_math')
    def test_difficult_function(self, complex_math):
        complex_math.return_value = 0
        self.assertEqual(first="solved!",
                         second=difficult_function(1,2))