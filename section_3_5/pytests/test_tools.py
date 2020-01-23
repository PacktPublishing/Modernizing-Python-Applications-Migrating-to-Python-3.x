import pytest
from mymodule.tools import compute_change_coins, compute_total_change, count_coins_in

def test_check_coins_in_with_valid_coins():
    assert count_coins_in([1, 1, 10, 10, 20]) == 42

def test_check_coins_in_with_invalid_coins():
    with pytest.raises(AssertionError):
        count_coins_in([1, 3, 10, 20])

def test_compute_total_change_valid_purchase():
    assert compute_total_change(10, 5) == 5

def test_compute_total_change_purchase_greater_than_money_in():
    with pytest.raises(AssertionError):
        compute_total_change(1, 10)

def test_compute_change_coins_no_change():
    coinsback = compute_change_coins(0)
    assert sorted(coinsback.items()) == [(1, 0), (10, 0), (20, 0)]

def test_compute_change_coins_change():
    coinsback = compute_change_coins(99)
    assert sorted(coinsback.items()) == [(1, 9), (10, 1), (20, 4)]

