class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Brute Force - Nah hella ineff
        # Greedy - Choose max denom. first - Not ideal as it will give u incorrect answers some cases.
        # BFS w/ DP - Best

        # dp array where i = amount, dp[i] = # of coins
        dp = [amount + 1] * (amount + 1) # bc we want dp[0] thru dp[amount]
        dp[0] = 0 # base case

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If unreachable, return -1
        return dp[amount] if dp[amount] <= amount else -1
