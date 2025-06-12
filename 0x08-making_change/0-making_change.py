#!/usr/bin/python3
"""
Solution to the coin change problem using dynamic programming.
This module contains a function to find the minimum number of coins
needed to make a given total amount.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): List of coin denominations available
        total (int): Target amount to make change for
    
    Returns:
        int: Minimum number of coins needed, or -1 if impossible
    """
    # Handle edge cases
    if total <= 0:
        return 0
    
    # Initialize dp array with infinity for all amounts except 0
    # dp[i] represents minimum coins needed to make amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0
    
    # Fill the dp array using bottom-up approach
    for amount in range(1, total + 1):
        # Try each coin denomination
        for coin in coins:
            # If coin value is less than or equal to current amount
            # and we can make (amount - coin), then we can make amount
            if coin <= amount and dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # Return result: -1 if impossible, otherwise minimum coins needed
    return dp[total] if dp[total] != float('inf') else -1
