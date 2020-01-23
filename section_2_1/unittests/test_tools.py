import unittest
from mymodule.tools import compute_change_coins, compute_total_change, count_coins_in

class TestToolsMethods(unittest.TestCase):

    def test_check_coins_in_with_valid_coins(self):
        self.assertEqual(count_coins_in([1, 1, 10, 10, 20]), 42)

    def test_check_coins_in_with_invalid_coins(self):
        with self.assertRaises(AssertionError):
            count_coins_in([1, 3, 10, 20])



