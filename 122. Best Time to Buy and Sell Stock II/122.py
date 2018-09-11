class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        else:
            max_profit = 0
            for i, v in enumerate(prices[:-1]):
                if prices[i + 1] - prices[i] > 0:
                    max_profit += prices[i + 1] - prices[i]
            return max_profit


arr = [1, 7, 2, 3, 6, 7, 6, 7]
s = Solution()
print(s.maxProfit(arr))
