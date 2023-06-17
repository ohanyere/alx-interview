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

    # Sort the coins in descending order
    # Sorting the coins in descending order allows the algorithm
    # to start with the largest denomination and progressively
    # use smaller denominations to make change
    coins.sort(reverse=True)

    # keep track of the number of coins
    num_coins = 0

    # Store the amount still needed to be made
    remaining_total = total

    # Calculates how many times each coins can be used to make change
    # for the remaining total
    for few_coin in coins:
        if few_coin <= remaining_total:
            num_coins += remaining_total // few_coin
            remaining_total %= few_coin

    # Returns the fewest number of coins needed to make the desired total
    # else the change will not be possible
    return num_coins if remaining_total == 0 else -1
