def num_coins(amount, coin_vals):
    min_coins = amount
    if amount in coin_vals:
        return 1

    else:
        for i in [c for c in coin_vals if c <= amount]:
            num = 1 + num_coins(amount-i, coin_vals)
            if num < min_coins:
                min_coins = num
    return min_coins



print(num_coins(30, [1, 5, 10, 25]))
