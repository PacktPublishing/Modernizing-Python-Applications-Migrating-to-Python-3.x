ALLOWED_COINS = {1, 10, 20}

def count_coins_in(coins):
  assert set(coins) - ALLOWED_COINS == set([])
  return sum(coins)

def compute_total_change(total_money_in, purchase_price):
  assert total_money_in >= purchase_price
  return total_money_in-purchase_price

def compute_change_coins(money_back):
  returned_coins = {}
  for coin_val in sorted(ALLOWED_COINS, reverse=True):
    returned_coins[coin_val] = money_back/coin_val
    money_back -= coin_val*returned_coins[coin_val]
  return returned_coins



