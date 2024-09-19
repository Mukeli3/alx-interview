#!/usr/bin/python3
"""
This module defines the coin change problem,  dynamic programming approach
used to find the minimum number of coins required to make up a given total
amount given coin denominations list
"""


def makeChange(coins, total):
    """
    Function determines the fewest number of coins needed to meet
    given amt, total
    Args:
        coins: list of values of the coins in possession
        total: the total
    Return:
         fewest numbe of coins needed to meet total
    """
    if total <= 0:
        return 0

    # dynamic programming list
    dp = [float('inf')] * (total + 1)

    dp[0] = 0  # Base case

    for coin in coins:
        for amt in range(coin, total + 1):
            dp[amt] = min(dp[amt], dp[amt - coin] + 1)

    if dp[total] != float('inf'):
        return dp[total]
    else:
        return -1
