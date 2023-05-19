#!/usr/bin/python3
    """
    Calculate the fewest number of coins needed to meet a given total.

    """

def makeChange(coins, total):
    """
    Args:
        coins (list[int]): A list of coin values.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed to meet the total.
            Returns 0 if the total is 0 or less.
            Returns -1 if the total cannot be met by any combination of coins.

    """

    if total <= 0:
        return 0

    # Initialize the array with large values except for position 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the minimum number of coins for each value
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check if the total can be achieved
    if dp[total] == float('inf'):
        return -1

    return dp[total]
