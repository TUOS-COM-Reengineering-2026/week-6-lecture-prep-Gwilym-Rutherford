import unittest

from unittest.mock import MagicMock
from lecture import randomised_function

class MyTestCase(unittest.TestCase):

    def test_randomised_function(self):
        randomised_function = MagicMock(return_value = "software")
        self.assertEqual('software', randomised_function())
        
