#!/usr/bin/python3
'''
Using a pile of coins of different values to determine
the fewest number of coins needed to meet a given amount total
'''


def makeChange(coins, total):
    '''
    Determines the fewest number of coins needed to meet a given amount
    Args:
        coins (list): List of values of coins in possession
        total (int): The desired amount to be met
    Returns:
        Fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    '''
    # Returns 0 indicating that no coins are needed
    if total <= 0:
        return 0

    # Create list to hold the fewest number of coins needed for each total
    num_coins = [float('inf')] * (total + 1)
    num_coins[0] = 0

    # Calculates how many times each coins can be used to make change
    # for the remaining total
    for few_coin in coins:
        for amt in range(few_coin, total + 1):
            num_coins[amt] = min(num_coins[amt],
                                 num_coins[amt - few_coin] + 1)

    # Returns the fewest number of coins needed to make the desired total
    # else the change will not be possible
    # if few_num_coins[total] != float('inf'):
    return num_coins[total] if num_coins[total] != float('inf') else -1
    # else:
    # return -1
