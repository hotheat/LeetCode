class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        min_price, max_profit = prices[0], 0
        for i in prices[1:]:
            min_price = min(min_price, i)
            profit = i - min_price
            max_profit = max(profit, max_profit)
        # print(min_price)
        print(prices.index(max_profit + min_price))
        return max_profit


arr = [7, 1, 5, 6, 3, 2]
s = Solution()
print(s.maxProfit(arr))
