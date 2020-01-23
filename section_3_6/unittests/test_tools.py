import unittest
from mymodule.tools import compute_change_coins, compute_total_change, count_coins_in

class TestToolsMethods(unittest.TestCase):

    def test_check_coins_in_with_valid_coins(self):
        self.assertEqual(count_coins_in([1, 1, 10, 10, 20]), 42)

    def test_check_coins_in_with_invalid_coins(self):
        with self.assertRaises(AssertionError):
            count_coins_in([1, 3, 10, 20])

    def test_compute_total_change_valid_purchase(self):
        self.assertEqual(compute_total_change(10, 5), 5)

    def test_compute_total_change_purchase_greater_than_money_in(self):
        with self.assertRaises(AssertionError):
            compute_total_change(1, 10)

    def test_compute_change_coins_no_change(self):
        coinsback = compute_change_coins(0)
        self.assertDictEqual(coinsback, {1: 0, 10: 0, 20: 0})

    def test_compute_change_coins_change(self):
        coinsback = compute_change_coins(99)
        self.assertDictEqual(coinsback, {1: 9, 10: 1, 20: 4})

if __name__ == '__main__':
    unittest.main()

