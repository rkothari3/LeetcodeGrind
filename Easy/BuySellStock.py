class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 0

        maxProf = 0

        while right < (len(prices) - 1):
            right += 1
            if prices[left] > prices[right]:
                left = right
            profit = prices[right] - prices[left]

            if profit > maxProf:
                maxProf = profit
        return maxProf