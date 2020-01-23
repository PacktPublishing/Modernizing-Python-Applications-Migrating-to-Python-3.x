import unittest
from mymodule.tools import compute_change_coins, compute_total_change, count_coins_in

class TestBasic(unittest.TestCase):
    def setUp(self):
        self.purchase = 7
        self.coins_in = [1, 1, 10, 10, 20, 20] #62
        self.expected_change = {1: 5, 10: 1, 20: 2} # 55

    def test_correctness_of_change(self):
        money_in = count_coins_in(self.coins_in)
        change = compute_total_change(money_in, self.purchase)
        coins_out = compute_change_coins(change)
        self.assertDictEqual(coins_out, self.expected_change)


if __name__ == '__main__':
    unittest.main()