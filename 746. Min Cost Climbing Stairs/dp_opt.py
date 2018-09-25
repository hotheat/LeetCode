class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp_i1, dp_i2 = 0, 0
        i = 2
        while i <= len(cost):
            dp_i1, dp_i2 = min(dp_i1 + cost[i - 1], dp_i2 + cost[i - 2]), dp_i1
            i += 1
        return dp_i1


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
s = Solution()
print(s.minCostClimbingStairs(cost))
