import pytest
from mymodule.tools import compute_change_coins, compute_total_change, count_coins_in

def test_check_coins_in_with_valid_coins():
    assert count_coins_in([1, 1, 10, 10, 20]) == 42

def test_check_coins_in_with_invalid_coins():
    with pytest.raises(AssertionError):
        count_coins_in([1, 3, 10, 20])




